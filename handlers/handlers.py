import logging
from typing import List

import emoji
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes

from database.database import (create_user, delete_user_model,
                               delete_user_temporary_budget,
                               edit_temporary_budget, get_user_brand,
                               get_user_contact, get_user_order,
                               show_temporary_budget, update_user_order_brand,
                               update_user_order_budget,
                               update_user_order_drive,
                               update_user_order_engine_capacity,
                               update_user_order_fuel,
                               update_user_order_hand_drive,
                               update_user_order_model,
                               update_user_order_power, update_user_order_year, delete_user_order, get_user_id_from_db,
                               get_user_budget, get_user_fuel_type, get_user_power)
from keyboards.keyboards import Keyboard
from routes.routes import Routes, StartEndRoutes
from tax.tax import calculate_sum, get_euro

MAIN_REPLAY_TEXT = emoji.emojize(
    "🔹Brand:                       {}\n"
    "🔹Model:                    {}\n"
    "🔹Сar steering wheel:                    {}\n"
    "🔹Power*:             {} л.с.\n"
    "🔹Drive unit:                     {}\n"
    "🔹Engine volume*:            {} л.\n"
    "🔹Car age*:         {}\n"
    "🔹Fuel type*:          {}\n"
    "🔹Price*:             {} руб\n\n"
    "*Required fields for calculating customs duties\n\n"
    "If the bot does not respond, click /start")
REPLAY_TEXT_TO_SEND = (
    "🔹Марка:    {}\n🔹Модель:    {}\n🔹Руль:    {}\n🔹Мощность:    {}\n🔹Привод:    {}\n🔹Объем ДВС:    {}\n"
    "🔹Возраст авто:    {}\n🔹Тип топлива:    {}\n🔹Стоимость:    {}\n\n")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    """Send message on `/start`."""
    user_chat_id = update.message.from_user.id
    user_name = update.message.from_user.username
    user_first_name = update.message.from_user.first_name
    user_id_from_db = await get_user_id_from_db(user_chat_id)

    if user_id_from_db:
        reply_markup = InlineKeyboardMarkup(Keyboard.MAIN_KEYBOARD)
        reply_text = ""
        for row in await get_user_order(user_chat_id):
            reply_text += MAIN_REPLAY_TEXT.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7],
                                                  row[8])
        await update.message.reply_text(reply_text,
                                        reply_markup=reply_markup
                                        )
        return StartEndRoutes.start_route
    else:

        await create_user(user_chat_id, user_name, user_first_name)

        logging.info("User %s started the conversation", user_chat_id)

        reply_markup = InlineKeyboardMarkup(Keyboard.MAIN_KEYBOARD)

        await update.message.reply_text(
            "Start building your own constructor! The selected parameters will be automatically reflected here.\n\n"
            " If the bot is not responding, press /start",
            reply_markup=reply_markup
        )
        return StartEndRoutes.start_route


async def start_over(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_specific_keyboard_to_change_order(update, context, "", "", Keyboard.MAIN_KEYBOARD)


async def start_over2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_specific_keyboard_to_change_order(update, context, "", "", Keyboard.MAIN_KEYBOARD2)


async def show_specific_keyboard_to_change_order(update: Update, context: ContextTypes.DEFAULT_TYPE, key: str,
                                                 text: str,
                                                 keyboard: List[List[InlineKeyboardButton]]) -> StartEndRoutes:
    user_chat_id = update.callback_query.from_user.id

    if key == "aplay_new_budget":
        old_value = await show_temporary_budget(user_chat_id)
        await update_user_order_budget(budget=old_value[0][0], user_chat_id=user_chat_id)

    if key == "aplay_new_power":
        # we use the same table because it is cleared all the time
        old_value = await show_temporary_budget(user_chat_id)
        await update_user_order_power(power=old_value[0][0], user_chat_id=user_chat_id)

    await delete_user_temporary_budget(user_chat_id)

    update_functions = {
        "brand": update_user_order_brand,
        "model": update_user_order_model,
        "engine": update_user_order_engine_capacity,
        "year": update_user_order_year,
        "hand_drive": update_user_order_hand_drive,
        "drive": update_user_order_drive,
        "fuel_type": update_user_order_fuel
    }

    if key in update_functions:
        update_function = update_functions[key]
        await update_function(text, user_chat_id)
    # for brand handler it's necessary to clear model each time when you chose another brand
    elif key == "brand":
        await delete_user_model(user_chat_id)
        await update_user_order_brand(text, user_chat_id)
    query = update.callback_query
    await query.answer()

    reply_markup = InlineKeyboardMarkup(Keyboard.MAIN_KEYBOARD)

    reply_text = ""
    for row in await get_user_order(update.callback_query.from_user.id):
        reply_text += MAIN_REPLAY_TEXT.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
    if reply_text:
        await query.edit_message_text(
            text=reply_text, reply_markup=reply_markup
        )

    logging.info("User %s started main page", user_chat_id)

    return StartEndRoutes.start_route


async def show_pop_up(update: Update, context: ContextTypes.DEFAULT_TYPE, text=None):
    query = update.callback_query
    if text == "tax":
        try:  # TODO: make this without the exeption
            user_chat_id = update.callback_query.from_user.id
            user_tax = await calculate_sum(user_chat_id)
            fuel_type = await get_user_fuel_type(user_chat_id)
            user_budget = await get_user_budget(user_chat_id)
            eur_rub = await get_euro()

            if int(user_budget[0][0]) / eur_rub <= 200000:
                customs_clearance = 755
            elif 200000 < int(user_budget[0][0]) / eur_rub <= 450000:
                customs_clearance = 1550
            elif 450000 < int(user_budget[0][0]) / eur_rub <= 1200000:
                customs_clearance = 3100
            else:
                customs_clearance = 8530
            if fuel_type[0][0] != "Электро":
                utilization = 5200
                await context.bot.answer_callback_query(callback_query_id=query.id,
                                                        text=f"Recycling fee {utilization} RUB\n"
                                                             f"Customs duties {round(float(user_tax), 2)} RUB\n"
                                                             f"Customs clearance {round(customs_clearance, 2)} RUB\n\n"
                                                             f"All customs expenses {round(utilization + float(user_tax) + customs_clearance, 2)} RUB\n\n"

                                                             f"Rate EUR {round(eur_rub, 2)} RUB."
                                                        ,
                                                        show_alert=True)
            else:
                utilization = 122000
                posh = float(user_budget[0][0]) * 0.15
                user_power = await get_user_power(user_chat_id)

                if int(user_power[0][0]) > 90:
                    akciz = 55 * int(user_power[0][0])
                else:
                    akciz = 0
                nds = (utilization + posh + akciz) * 0.2
                await context.bot.answer_callback_query(callback_query_id=query.id,
                                                        text=f"Recycling fee {utilization} RUB\n"
                                                             f"Customs duty (15%) {round(posh, 2)} RUB\n"
                                                             f"Excise duty {round(akciz, 2)} RUB\n"
                                                             f"Customs clearance {round(customs_clearance, 2)} RUB\n"
                                                             f"VAT (20%) {round(nds, 2)} RUB\n\n"
                                                             f"All customs expenses {round(utilization + posh + akciz + customs_clearance + nds, 2)} RUB\n\n"

                                                             f"Rate EUR {round(eur_rub, 2)} RUB"
                                                        ,
                                                        show_alert=True)
        except:
            await context.bot.answer_callback_query(callback_query_id=query.id,
                                                    text=f"Not enough data to calculate customs duties",
                                                    show_alert=True)
    if text == "send":
        user_chat_id = update.callback_query.from_user.id
        user_tg_name = await get_user_contact(user_chat_id)
        if user_tg_name[0][0] is not None:
            reply_text = ""
            for row in await get_user_order(update.callback_query.from_user.id):
                reply_text += REPLAY_TEXT_TO_SEND.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7],
                                                         row[8])
            if reply_text:
                text = "Новый заказ:\n\n" + reply_text + f"@{user_tg_name[0][0]}"
                await context.bot.send_message(chat_id=557195190, text=text)
                await context.bot.answer_callback_query(callback_query_id=query.id,
                                                        text="Your application has been successfully submitted"
                                                             " and our specialist will contact you soon.\n\n"
                                                             "Thank you for using our bot =)",
                                                        show_alert=True)
        else:
            text2 = "We have sent your application without a name because it is not specified in Telegram.\n" \
                    "Please inform our specialist about this @Aleksei_Novopashin"
            await context.bot.send_message(chat_id=user_chat_id, text=text2)


async def show_specific_keyboard(update: Update, context: ContextTypes.DEFAULT_TYPE, text: str,
                                 keyboard: List[List[InlineKeyboardButton]], user_chat_id=None):
    query = update.callback_query
    await query.answer()
    reply_markup = InlineKeyboardMarkup(keyboard)
    if text == "brand":
        await query.edit_message_text(text="Select car brand", reply_markup=reply_markup)
        return StartEndRoutes.brand
    if text == "model_acura":
        await query.edit_message_text(text="Models Acura", reply_markup=reply_markup)
        return StartEndRoutes.model_acura
    if text == "model_daewoo":
        await query.edit_message_text(text="Models Daewoo", reply_markup=reply_markup)
        return StartEndRoutes.model_daewoo
    if text == "model_subaru":
        await query.edit_message_text(text="Models Subaru", reply_markup=reply_markup)
        return StartEndRoutes.model_subaru
    if text == "model_mazda":
        await query.edit_message_text(text="Models Mazda", reply_markup=reply_markup)
        return StartEndRoutes.model_mazda
    if text == "model_datsun":
        await query.edit_message_text(text="Models Datsun", reply_markup=reply_markup)
        return StartEndRoutes.model_datsun
    if text == "model_genesis":
        await query.edit_message_text(text="Models Genesis", reply_markup=reply_markup)
        return StartEndRoutes.model_genesis
    if text == "model_honda":
        await query.edit_message_text(text="Models Honda", reply_markup=reply_markup)
        return StartEndRoutes.model_honda
    if text == "model_toyota":
        await query.edit_message_text(text="Models Toyota", reply_markup=reply_markup)
        return StartEndRoutes.model_toyota
    if text == "hand_drive":
        await query.edit_message_text(text="steering wheel", reply_markup=reply_markup)
        return StartEndRoutes.hand_drive
    if text == "power":
        await query.edit_message_text(text="0л.с.", reply_markup=reply_markup)
        return StartEndRoutes.power2
    if text == "budget":
        await query.edit_message_text(text="0руб", reply_markup=reply_markup)
        return StartEndRoutes.budget2
    if text == "year":
        await query.edit_message_text(text="Age Auto", reply_markup=reply_markup)
        return StartEndRoutes.year
    if text == "engine":
        await query.edit_message_text(text="Engine capacity in liters", reply_markup=reply_markup)
        return StartEndRoutes.engine
    if text == "drive":
        await query.edit_message_text(text="Drive unit", reply_markup=reply_markup)
        return StartEndRoutes.drive
    if text == "fuel_type":
        await query.edit_message_text(text="Fuel type", reply_markup=reply_markup)
        return StartEndRoutes.fuel_type
    if text == "delete":
        await query.edit_message_text(text="Your profile has been deleted. To return to the main menu, click Back",
                                      reply_markup=reply_markup)
        user_chat_id = update.callback_query.from_user.id
        await delete_user_order(user_chat_id=user_chat_id)

        return Routes.start_over
    return None


async def show_keyboard1(update: Update, context: ContextTypes.DEFAULT_TYPE,
                         keyboard: List[List[InlineKeyboardButton]], text="", opa=""):
    user_chat_id = update.callback_query.from_user.id
    query = update.callback_query
    await query.answer()
    reply_markup = InlineKeyboardMarkup(keyboard)
    old_value = await show_temporary_budget(user_chat_id)
    new_value = old_value[0][0] + text
    await edit_temporary_budget(value=new_value, user_chat_id=user_chat_id)
    new_value = await show_temporary_budget(user_chat_id)
    await query.edit_message_text(
        text=new_value[0][0] + opa, reply_markup=reply_markup
    )
    if opa == "руб":
        return StartEndRoutes.budget2
    else:
        return StartEndRoutes.power2


async def show_keyboard2(update: Update, context: ContextTypes.DEFAULT_TYPE,
                         keyboard: List[List[InlineKeyboardButton]], text="", opa=""):
    user_chat_id = update.callback_query.from_user.id
    query = update.callback_query
    await query.answer()
    reply_markup = InlineKeyboardMarkup(keyboard)
    old_value = await show_temporary_budget(user_chat_id)
    new_value = old_value[0][0] + text
    await edit_temporary_budget(value=new_value, user_chat_id=user_chat_id)
    new_value = await show_temporary_budget(user_chat_id)
    await query.edit_message_text(
        text=new_value[0][0] + opa, reply_markup=reply_markup
    )
    if opa == "руб":
        return StartEndRoutes.budget
    else:
        return StartEndRoutes.power


async def aplay_new_budget(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_specific_keyboard_to_change_order(update, context, "aplay_new_budget", "",
                                                        Keyboard.BUDGET_KEYBOARD2)


async def aplay_new_budget2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_specific_keyboard_to_change_order(update, context, "aplay_new_budget", "",
                                                        Keyboard.BUDGET_KEYBOARD)


async def aplay_new_power(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_specific_keyboard_to_change_order(update, context, "aplay_new_power", "",
                                                        Keyboard.POWER_POWER_KEYBOARD2)


async def aplay_new_power2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_specific_keyboard_to_change_order(update, context, "aplay_new_power", "",
                                                        Keyboard.POWER_POWER_KEYBOARD)


async def brand(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.brand:
    return await show_specific_keyboard(update, context, "brand", Keyboard.BRAND_KEYBOARD)


async def hand_drive(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_specific_keyboard(update, context, "hand_drive", Keyboard.HAND_DRIVE_KEYBOARD)


async def power(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_specific_keyboard(update, context, "power", Keyboard.POWER_POWER_KEYBOARD)


async def drive(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_specific_keyboard(update, context, "drive", Keyboard.DRIVE_KEYBOARD)


async def year(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_specific_keyboard(update, context, "year", Keyboard.YEAR_KEYBOARD)


async def engine(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_specific_keyboard(update, context, "engine", Keyboard.ENGINE_KEYBOARD)


async def fuel_type(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_specific_keyboard(update, context, "fuel_type", Keyboard.FUEL_KEYBOARD)


async def budget(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_specific_keyboard(update, context, "budget", Keyboard.BUDGET_KEYBOARD)


async def send(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    return await show_pop_up(update, context, "send")


async def delete(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_specific_keyboard(update, context, "delete", Keyboard.DELETE)


async def tax(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    return await show_pop_up(update, context, "tax")


async def model(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.model:
    user_chat_id = update.callback_query.from_user.id
    brand_user = await get_user_brand(user_chat_id)

    if brand_user[0][0] == "Acura":
        return await show_specific_keyboard(update, context, "model_acura", Keyboard.MODEL_KEYBOARD_ACURA)
    if brand_user[0][0] == "Daewoo":
        return await show_specific_keyboard(update, context, "model_daewoo", Keyboard.MODEL_KEYBOARD_DAEWOO)
    if brand_user[0][0] == "Datsun":
        return await show_specific_keyboard(update, context, "model_datsun", Keyboard.MODEL_KEYBOARD_DATSUN)
    if brand_user[0][0] == "Genesis":
        return await show_specific_keyboard(update, context, "model_genesis", Keyboard.MODEL_KEYBOARD_GENESIS)
    if brand_user[0][0] == "Honda":
        return await show_specific_keyboard(update, context, "model_honda", Keyboard.MODEL_KEYBOARD_HONDA)
    if brand_user[0][0] == "Mazda":
        return await show_specific_keyboard(update, context, "model_mazda", Keyboard.MODEL_KEYBOARD_MAZDA)
    if brand_user[0][0] == "Subaru":
        return await show_specific_keyboard(update, context, "model_subaru", Keyboard.MODEL_KEYBOARD_SUBARU)
    if brand_user[0][0] == "Toyota":
        return await show_specific_keyboard(update, context, "model_toyota", Keyboard.MODEL_KEYBOARD_TOYOTA)
    else:
        query = update.callback_query
        await context.bot.answer_callback_query(callback_query_id=query.id,
                                                text="First select your car brand",
                                                show_alert=True)
