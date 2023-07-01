from typing import List

from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes

from database.database import create_user, get_user_order, show_temporary_budget, \
    edit_temporary_budget, update_user_order_brand, update_user_order_model
from keyboards.keyboards import Keyboard
from routes.routes import StartEndRoutes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    """Send message on `/start`."""
    user_chat_id = update.message.from_user.id
    user_name = update.message.from_user.username
    user_first_name = update.message.from_user.first_name
    # create user
    await create_user(user_chat_id, user_name, user_first_name)
    # logging.info("User %s started the conversation.", user.first_name) #START LOGGGGING
    reply_markup = InlineKeyboardMarkup(Keyboard.MAIN_KEYBOARD)
    await update.message.reply_text(
        "Start handler, Choose a route", reply_markup=reply_markup
    )
    return StartEndRoutes.start_route


# async def start_over(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:  # TODO maybe need to be
#     # removed
#     """Prompt same text & keyboard as `start` does but not as new message"""
#
#     query = update.callback_query
#     await query.answer()
#     reply_markup = InlineKeyboardMarkup(Keyboard.MAIN_KEYBOARD)
#     reply_text = ""
#     for row in await get_user_order(update.callback_query.from_user.id):
#         reply_text += "Brand: {}\nModel: {}\nPTS: {}\nBody Type: {}\nDrive: {}\nEngine Capacity: {}\nYear: {}\nFuel Type: {}\nBudget: {}\n\n".format(
#             row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
#     await query.edit_message_text(
#         text=reply_text, reply_markup=reply_markup
#     )
#     return StartEndRoutes.end_route

# async def start_over2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:  # TODO maybe need to be
#     # removed
#     """Prompt same text & keyboard as `start` does but not as new message"""
#
#     query = update.callback_query
#     await query.answer()
#     reply_markup = InlineKeyboardMarkup(Keyboard.MAIN_KEYBOARD)
#     reply_text = ""
#     for row in await get_user_order(update.callback_query.from_user.id):
#         reply_text += "Brand: {}\nModel: {}\nPTS: {}\nBody Type: {}\nDrive: {}\nEngine Capacity: {}\nYear: {}\nFuel Type: {}\nBudget: {}\n\n".format(
#             row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
#     await query.edit_message_text(
#         text=reply_text, reply_markup=reply_markup
#     )
#     return StartEndRoutes.end_route


async def start_over(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_specific_keyboard_to_change_order(update, context, "", "", Keyboard.MAIN_KEYBOARD)


# def update_user_order_model(model, user_chat_id):
#     pass


async def show_specific_keyboard_to_change_order(update: Update, context: ContextTypes.DEFAULT_TYPE, key: str,
                                                 text: str,
                                                 keyboard: List[List[InlineKeyboardButton]]) -> StartEndRoutes:
    user_chat_id = update.callback_query.from_user.id
    if key == "brand":
        print(key)
        await update_user_order_brand(brand=text, user_chat_id=user_chat_id)
    if key == "model":
        print(key)
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


async def mazda(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    print("MAAAA")
    return await show_specific_keyboard_to_change_order(update, context, "brand", "Мазда", Keyboard.BRAND_KEYBOARD)


async def subaru(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    print("SUUU")
    return await show_specific_keyboard_to_change_order(update, context, "brand", "Субару", Keyboard.BRAND_KEYBOARD)


async def kalina(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    print("KAAAA")
    return await show_specific_keyboard_to_change_order(update, context, "model", "Kalina", Keyboard.MODEL_KEYBOARD)


async def granta(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    print("GRAAA")
    return await show_specific_keyboard_to_change_order(update, context, "model", "Гранта", Keyboard.MODEL_KEYBOARD)


async def show_specific_keyboard(update: Update, context: ContextTypes.DEFAULT_TYPE, text: str,
                                 keyboard: List[List[InlineKeyboardButton]]) -> StartEndRoutes:
    query = update.callback_query
    await query.answer()
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text=text, reply_markup=reply_markup)

    if text == "brand":
        return StartEndRoutes.brand
    if text == "model":
        return StartEndRoutes.model


async def brand(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.brand:
    return await show_specific_keyboard(update, context, "brand", Keyboard.BRAND_KEYBOARD)


async def model(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.model:
    return await show_specific_keyboard(update, context, "model", Keyboard.MODEL_KEYBOARD)


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


async def budget(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_specific_keyboard(update, context, "buget", Keyboard.BUDGET_KEYBOARD)


async def budget2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_specific_keyboard(update, context, "buget2", Keyboard.BUDGET_KEYBOARD2)


async def send(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_specific_keyboard(update, context, "send", Keyboard.SEND)


async def tax(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_specific_keyboard(update, context, "DRIVE", Keyboard.TAX)


async def delete(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_specific_keyboard(update, context, "DRIVE", Keyboard.DELETE)


async def show_keyboard1(update: Update, context: ContextTypes.DEFAULT_TYPE, text: str,
                         keyboard: List[List[InlineKeyboardButton]]) -> StartEndRoutes:
    user_chat_id = update.callback_query.from_user.id
    query = update.callback_query
    await query.answer()
    reply_markup = InlineKeyboardMarkup(keyboard)

    old_value = str(show_temporary_budget(user_chat_id))
    new_value = old_value + text
    await edit_temporary_budget(value=new_value, user_chat_id=user_chat_id)
    new_value = str(show_temporary_budget(user_chat_id))
    await query.edit_message_text(
        text=new_value, reply_markup=reply_markup
    )

    return StartEndRoutes.end_route

    # user_chat_id = update.callback_query.from_user.id
    # query = update.callback_query
    # await query.answer()
    # reply_markup = InlineKeyboardMarkup(Keyboard.BUDGET_KEYBOARD)
    # reply_text = ""
    # for row in await show_temporary_budget(update.callback_query.from_user.id):
    #     reply_text += "Бюждет: {}".format(
    #         row[0], )
    #
    # await query.edit_message_text(
    #     text=reply_text, reply_markup=reply_markup
    # )
    # new_value = reply_text + text
    # await edit_temporary_budget(value=new_value, user_chat_id=user_chat_id)
    # return StartEndRoutes.start_route


async def show_keyboard2(update: Update, context: ContextTypes.DEFAULT_TYPE, text: str,
                         keyboard: List[List[InlineKeyboardButton]]) -> StartEndRoutes:
    user_chat_id = update.callback_query.from_user.id
    query = update.callback_query
    await query.answer()
    reply_markup = InlineKeyboardMarkup(keyboard)

    old_value = str(show_temporary_budget(user_chat_id))
    new_value = old_value + text
    await edit_temporary_budget(value=new_value, user_chat_id=user_chat_id)
    new_value = str(show_temporary_budget(user_chat_id))
    await query.edit_message_text(
        text=new_value, reply_markup=reply_markup
    )

    return StartEndRoutes.end_route


async def one(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_keyboard2(update, context, "1", Keyboard.BUDGET_KEYBOARD2)


async def two(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_keyboard2(update, context, "2", Keyboard.BUDGET_KEYBOARD2)


async def three(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_keyboard2(update, context, "3", Keyboard.BUDGET_KEYBOARD2)


async def four(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_keyboard2(update, context, "4", Keyboard.BUDGET_KEYBOARD2)


async def five(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_keyboard2(update, context, "5", Keyboard.BUDGET_KEYBOARD2)


async def six(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_keyboard2(update, context, "6", Keyboard.BUDGET_KEYBOARD2)


async def seven(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_keyboard2(update, context, "7", Keyboard.BUDGET_KEYBOARD2)


async def eight(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_keyboard2(update, context, "8", Keyboard.BUDGET_KEYBOARD2)


async def nine(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_keyboard2(update, context, "9", Keyboard.BUDGET_KEYBOARD2)


async def zero(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_keyboard2(update, context, "0", Keyboard.BUDGET_KEYBOARD2)


async def one2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_keyboard1(update, context, "1", Keyboard.BUDGET_KEYBOARD)


async def two2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_keyboard1(update, context, "2", Keyboard.BUDGET_KEYBOARD)


async def three2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_keyboard1(update, context, "3", Keyboard.BUDGET_KEYBOARD)


async def four2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_keyboard1(update, context, "4", Keyboard.BUDGET_KEYBOARD)


async def five2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_keyboard1(update, context, "5", Keyboard.BUDGET_KEYBOARD)


async def six2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_keyboard1(update, context, "6", Keyboard.BUDGET_KEYBOARD)


async def seven2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_keyboard1(update, context, "7", Keyboard.BUDGET_KEYBOARD)


async def eight2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_keyboard1(update, context, "8", Keyboard.BUDGET_KEYBOARD)


async def nine2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_keyboard1(update, context, "9", Keyboard.BUDGET_KEYBOARD)


async def zero2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_keyboard1(update, context, "0", Keyboard.BUDGET_KEYBOARD)
