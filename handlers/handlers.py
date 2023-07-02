from typing import List

from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes

from database.database import create_user, get_user_order, show_temporary_budget, \
    edit_temporary_budget, update_user_order_brand, update_user_order_model, delete_user_temporary_budget, \
    update_user_order_budget, get_user_contact
from keyboards.keyboards import Keyboard
from routes.routes import StartEndRoutes, Routes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    """Send message on `/start`."""
    user_chat_id = update.message.from_user.id
    user_name = update.message.from_user.username
    user_first_name = update.message.from_user.first_name
    # create user
    await create_user(user_chat_id, user_name, user_first_name)
    # logging.info("User %s started the conversation.", user.first_name) # TODO START LOGGGGING
    reply_markup = InlineKeyboardMarkup(Keyboard.MAIN_KEYBOARD)
    await update.message.reply_text(
        "Начните собирать свой конструктор! Выбранные параметры будут отражаться здесь автоматически",
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
        await update_user_order_brand(brand=text, user_chat_id=user_chat_id)
    if key == "model":
        await update_user_order_model(model=text, user_chat_id=user_chat_id)

    query = update.callback_query
    await query.answer()

    reply_markup = InlineKeyboardMarkup(Keyboard.MAIN_KEYBOARD)

    reply_text = ""
    for row in await get_user_order(update.callback_query.from_user.id):
        reply_text += "Brand: {}\nModel: {}\nPTS: {}\nBody Type: {}\nDrive: {}\nEngine Capacity: {}\nYear: {}\nFuel Type: {}\nBudget: {}\n\n".format(
            row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
    if reply_text:
        await query.edit_message_text(
            text=reply_text, reply_markup=reply_markup
        )
    return StartEndRoutes.start_route


async def show_specific_keyboard(update: Update, context: ContextTypes.DEFAULT_TYPE, text: str,
                                 keyboard: List[List[InlineKeyboardButton]], user_chat_id=None):
    query = update.callback_query
    await query.answer()
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text=text, reply_markup=reply_markup)

    if text == "brand":
        return StartEndRoutes.brand
    if text == "model":
        # user_chat_id = update.callback_query.from_user.id
        # model_user = await get_user_model(user_chat_id)
        # if model_user[0][0] == "Мазда":
        #     return StartEndRoutes.model_mazda
        # if model_user[0][0] == "Субару":
        #     return StartEndRoutes.model_subaruzz
        return StartEndRoutes.model
    if text == "budget":
        return StartEndRoutes.budget2
    if text == "send":
        user_chat_id = update.callback_query.from_user.id
        user_tg_name = await get_user_contact(user_chat_id)

        reply_text = ""
        for row in await get_user_order(update.callback_query.from_user.id):
            reply_text += "Марка: {}\nМодель: {}\nПТС: {}\nТип кузова: {}\nПривод: {}\nОбъем двигателя: {}\nГод: {}\nТип топлива: {}\nБюджет: {}\n\n".format(
                row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])

        if reply_text:
            text = "Новый заказ:\n\n" + reply_text + f"@{user_tg_name[0][0]}"
            await context.bot.send_message(chat_id=270900337, text=text, )
        print(type(user_tg_name[0][0]))
        if user_tg_name[0][0] is None:
            print(user_tg_name[0][0])
            text = "Мы не смогли отправить вашу анкету, т.к. ваше имя в Телеграмме не определено.\n" \
                   "Пожалуйста, свяжитесь с нашим специалистом @Aleksei_Novopashin"
            await context.bot.send_message(chat_id=user_chat_id, text=text, )

        return Routes.send
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
    return await show_specific_keyboard(update, context, "model", Keyboard.MODEL_KEYBOARD)


# async def model_subaru(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.model:
#     return await show_specific_keyboard(update, context, "model_mazda", Keyboard.MODEL_KEYBOARD_SUBARU)
#
#
# async def model_mazda(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.model:
#     return await show_specific_keyboard(update, context, "model_subary", Keyboard.MODEL_KEYBOARD_MAZDA)


async def pts(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_specific_keyboard(update, context, "pts", Keyboard.PTS_KEYBOARD)


async def body_type(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_specific_keyboard(update, context, "body_type", Keyboard.BODY_TYPE_KEYBOARD)


async def drive(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_specific_keyboard(update, context, "drive", Keyboard.DRIVE_KEYBOARD)


async def engine_capacity(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_specific_keyboard(update, context, "engine_capacity", Keyboard.ENGINE_CAPACITY_KEYBOARD)


async def yeah(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_specific_keyboard(update, context, "yeah", Keyboard.YEAR_KEYBOARD)


async def fuel_type(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_specific_keyboard(update, context, "fuel_type", Keyboard.FUEL_TYPE_KEYBOARD)


async def budget(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.budget:
    return await show_specific_keyboard(update, context, "budget", Keyboard.BUDGET_KEYBOARD)


async def send(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_specific_keyboard(update, context, "send", Keyboard.SEND)


async def tax(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_specific_keyboard(update, context, "DRIVE", Keyboard.TAX)


async def delete(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_specific_keyboard(update, context, "DRIVE", Keyboard.DELETE)
