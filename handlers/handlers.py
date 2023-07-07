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
                               update_user_order_power, update_user_order_year, delete_user_order, get_user_id_from_db)
from keyboards.keyboards import Keyboard
from routes.routes import Routes, StartEndRoutes
from tax.tax import calculate_sum

MAIN_REPLAY_TEXT = emoji.emojize(
    "🔹Марка:    {}\n🔹Модель:    {}\n🔹Руль:    {}\n🔹Мощность ДВС*:    {}\n🔹Привод:    {}\n🔹Объем ДВС*:    {}\n🔹Возраст авто*:    {}\n🔹Тип топлива:    {}\n🔹Стоимость*:    {}\n\n*Обязательные поля для расчета таможенных платежей\n\nЕсли бот не реагирует нажмите /start")
REPLAY_TEXT_TO_SEND = (
    "🔹Марка:    {}\n🔹Модель:    {}\n🔹Руль:    {}\n🔹Мощность:    {}\n🔹Привод:    {}\n🔹Объем ДВС:    {}\n🔹Возраст авто:    {}\n🔹Тип топлива:    {}\n🔹Стоимость:    {}\n\n")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    """Send message on `/start`."""
    user_chat_id = update.message.from_user.id
    user_name = update.message.from_user.username
    user_first_name = update.message.from_user.first_name
    # create user
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
        # logging.info("User %s started the conversation.", user.first_name) # TODO START LOGGGGING
        reply_markup = InlineKeyboardMarkup(Keyboard.MAIN_KEYBOARD)

        await update.message.reply_text(
            "Начните собирать свой конструктор! Выбранные параметры будут отражаться здесь автоматически\n\nЕсли бот не реагирует нажмите /start",
            reply_markup=reply_markup
        )
        return StartEndRoutes.start_route


async def start_over(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_specific_keyboard_to_change_order(update, context, "", "", Keyboard.MAIN_KEYBOARD)


async def show_specific_keyboard_to_change_order(update: Update, context: ContextTypes.DEFAULT_TYPE, key: str,
                                                 text: str,
                                                 keyboard: List[List[InlineKeyboardButton]]) -> StartEndRoutes:
    user_chat_id = update.callback_query.from_user.id

    if key == "aplay_new_budget":
        old_value = await show_temporary_budget(user_chat_id)
        await update_user_order_budget(budget=old_value[0][0], user_chat_id=user_chat_id)

    await delete_user_temporary_budget(user_chat_id)

    if key == "brand":
        await delete_user_model(user_chat_id)
        await update_user_order_brand(brand=text, user_chat_id=user_chat_id)

    if key == "model":
        await update_user_order_model(model=text, user_chat_id=user_chat_id)
    # if key == "engine_capacity":
    #     await update_user_order_engine_capacity(engine_capacity=text, user_chat_id=user_chat_id)
    if key == "engine":
        await update_user_order_engine_capacity(engine_capacity=text, user_chat_id=user_chat_id)
    if key == "year":
        await update_user_order_year(year=text, user_chat_id=user_chat_id)
    if key == "hand_drive":
        await update_user_order_hand_drive(hand_drive=text, user_chat_id=user_chat_id)
    if key == "power":
        await update_user_order_power(power=text, user_chat_id=user_chat_id)
    if key == "drive":
        await update_user_order_drive(drive=text, user_chat_id=user_chat_id)
    if key == "fuel_type":
        await update_user_order_fuel(fuel_type=text, user_chat_id=user_chat_id)

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
    return StartEndRoutes.start_route


async def show_pop_up(update: Update, context: ContextTypes.DEFAULT_TYPE, text=None):
    query = update.callback_query
    if text == "tax":
        user_chat_id = update.callback_query.from_user.id
        tax = await calculate_sum(user_chat_id)
        await context.bot.answer_callback_query(callback_query_id=query.id,
                                                text=f"Таможенные сборы составят {tax} руб.", show_alert=True)
    # except:
    #     await context.bot.answer_callback_query(callback_query_id=query.id,
    #                                             text=f"Не хватает данных для расчета таможенных сборов", show_alert=True)

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
                await context.bot.send_message(chat_id=557195190, text=text, )
                await context.bot.answer_callback_query(callback_query_id=query.id,
                                                        text="Ваша анкета была успешно оправлена и скоро с вами свяжется наш специалист.\n\nСпасибо, что воспользовались нашим ботом =)",
                                                        show_alert=True)
        else:
            text2 = "Мы отправили вашу анкету без имени, т.к. оно в Телеграмме не определено.\n" \
                    "Пожалуйста, сообщите это нашему специалисту @Aleksei_Novopashin"
            await context.bot.send_message(chat_id=user_chat_id, text=text2)


async def show_specific_keyboard(update: Update, context: ContextTypes.DEFAULT_TYPE, text: str,
                                 keyboard: List[List[InlineKeyboardButton]], user_chat_id=None):
    query = update.callback_query
    await query.answer()
    reply_markup = InlineKeyboardMarkup(keyboard)
    if text == "brand":
        await query.edit_message_text(text="Выберите марку автомобиля", reply_markup=reply_markup)
        return StartEndRoutes.brand
    if text == "model_subaru":
        await query.edit_message_text(text="Модели Subaru", reply_markup=reply_markup)
        return StartEndRoutes.model_subaru
    if text == "model_mazda":
        await query.edit_message_text(text="Модели Mazda", reply_markup=reply_markup)
        return StartEndRoutes.model_mazda
    if text == "hand_drive":
        await query.edit_message_text(text="Руль", reply_markup=reply_markup)
        return StartEndRoutes.hand_drive
    if text == "budget":
        await query.edit_message_text(
            text="Ваш бюджет в рублях. Начните вводить нужную сумму на клавиатуре. После этого нажмите Применить",
            reply_markup=reply_markup)
        return StartEndRoutes.budget2
    if text == "year":
        await query.edit_message_text(text="Возраст Авто", reply_markup=reply_markup)
        return StartEndRoutes.year
    if text == "engine":
        await query.edit_message_text(text="Объем ДВС", reply_markup=reply_markup)
        return StartEndRoutes.engine
    if text == "power":
        await query.edit_message_text(text="Мощность ДВС", reply_markup=reply_markup)
        return StartEndRoutes.power
    if text == "drive":
        await query.edit_message_text(text="Привод", reply_markup=reply_markup)
        return StartEndRoutes.drive
    if text == "fuel_type":
        await query.edit_message_text(text="Тип топлива", reply_markup=reply_markup)
        return StartEndRoutes.fuel_type
    if text == "delete":
        await query.edit_message_text(text="Ваша анкета былв удалена. Для возврата в основное меню, нажмите Назад",
                                      reply_markup=reply_markup)
        user_chat_id = update.callback_query.from_user.id
        await delete_user_order(user_chat_id=user_chat_id)
        return Routes.delete
    return None


async def show_keyboard1(update: Update, context: ContextTypes.DEFAULT_TYPE, text: str,
                         keyboard: List[List[InlineKeyboardButton]]) -> StartEndRoutes.budget2:
    user_chat_id = update.callback_query.from_user.id
    query = update.callback_query
    await query.answer()
    reply_markup = InlineKeyboardMarkup(keyboard)
    old_value = await show_temporary_budget(user_chat_id)
    new_value = old_value[0][0] + text
    await edit_temporary_budget(value=new_value, user_chat_id=user_chat_id)
    new_value = await show_temporary_budget(user_chat_id)
    await query.edit_message_text(
        text=new_value[0][0], reply_markup=reply_markup
    )
    return StartEndRoutes.budget2


async def show_keyboard2(update: Update, context: ContextTypes.DEFAULT_TYPE, text: str,
                         keyboard: List[List[InlineKeyboardButton]]) -> StartEndRoutes.budget:
    user_chat_id = update.callback_query.from_user.id
    query = update.callback_query
    await query.answer()
    reply_markup = InlineKeyboardMarkup(keyboard)
    old_value = await show_temporary_budget(user_chat_id)
    new_value = old_value[0][0] + text
    await edit_temporary_budget(value=new_value, user_chat_id=user_chat_id)
    new_value = await show_temporary_budget(user_chat_id)
    await query.edit_message_text(
        text=new_value[0][0], reply_markup=reply_markup
    )
    return StartEndRoutes.budget


async def aplay_new_budget(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_specific_keyboard_to_change_order(update, context, "aplay_new_budget", "",
                                                        Keyboard.BUDGET_KEYBOARD2)


async def aplay_new_budget2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_specific_keyboard_to_change_order(update, context, "aplay_new_budget", "",
                                                        Keyboard.BUDGET_KEYBOARD)


async def brand(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.brand:
    return await show_specific_keyboard(update, context, "brand", Keyboard.BRAND_KEYBOARD)


async def model(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.model:
    user_chat_id = update.callback_query.from_user.id
    brand_user = await get_user_brand(user_chat_id)
    if brand_user[0][0] == "Мазда":
        return await show_specific_keyboard(update, context, "model_mazda", Keyboard.MODEL_KEYBOARD_MAZDA)
    if brand_user[0][0] == "Субару":
        return await show_specific_keyboard(update, context, "model_subaru", Keyboard.MODEL_KEYBOARD_SUBARU)
    else:
        query = update.callback_query
        await context.bot.answer_callback_query(callback_query_id=query.id,
                                                text="Сначала выберите Марку автомобиля",
                                                show_alert=True)

async def hand_drive(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_specific_keyboard(update, context, "hand_drive", Keyboard.HAND_DRIVE_KEYBOARD)


async def power(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_specific_keyboard(update, context, "power", Keyboard.POWER_KEYBOARD)


async def drive(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_specific_keyboard(update, context, "drive", Keyboard.DRIVE_KEYBOARD)


async def year(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_specific_keyboard(update, context, "year", Keyboard.YEAR_KEYBOARD)


async def engine(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_specific_keyboard(update, context, "engine", Keyboard.ENGINE_KEYBOARD)


async def fuel_type(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_specific_keyboard(update, context, "fuel_type", Keyboard.FUEL_KEYBOARD)


async def budget(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.budget:
    return await show_specific_keyboard(update, context, "budget", Keyboard.BUDGET_KEYBOARD)


async def send(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    return await show_pop_up(update, context, "send")


async def delete(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_specific_keyboard(update, context, "delete", Keyboard.DELETE)


async def tax(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    return await show_pop_up(update, context, "tax")
