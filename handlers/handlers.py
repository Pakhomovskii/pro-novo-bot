from typing import List

from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes

from database.database import create_user, update_user_order, get_user_order
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


async def start_over(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    """Prompt same text & keyboard as `start` does but not as new message"""
    query = update.callback_query
    user_chat_id = update.callback_query.from_user.id
    await query.answer()

    reply_markup = InlineKeyboardMarkup(Keyboard.MAIN_KEYBOARD)

    reply_text = ""
    for row in await get_user_order(update.callback_query.from_user.id):
        print(reply_text)
        reply_text += "Brend: {}\nModel: {}\nPTS: {}\nBody Type: {}\nDrive: {}\nEngine Capacity: {}\nYear: {}\nFuel Type: {}\nBudget: {}\n\n".format(
            row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])

    await query.edit_message_text(
        text=reply_text, reply_markup=reply_markup
    )
    return StartEndRoutes.end_route

async def mazda(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show new choice of buttons"""

    user_chat_id = update.callback_query.from_user.id
    await update_user_order(brend="Мазда", user_chat_id=user_chat_id)
    query = update.callback_query
    await query.answer()

    reply_markup = InlineKeyboardMarkup(Keyboard.MAIN_KEYBOARD)

    reply_text = ""
    for row in await get_user_order(update.callback_query.from_user.id):
        print(reply_text)
        reply_text += "Brend: {}\nModel: {}\nPTS: {}\nBody Type: {}\nDrive: {}\nEngine Capacity: {}\nYear: {}\nFuel Type: {}\nBudget: {}\n\n".format(
            row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])

    await query.edit_message_text(
        text=reply_text, reply_markup=reply_markup
    )
    return StartEndRoutes.start_route


async def subaru(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show new choice of buttons"""
    user_chat_id = update.callback_query.from_user.id
    await update_user_order(brend="Subaru", user_chat_id=user_chat_id)
    query = update.callback_query
    await query.answer()
    reply_markup = InlineKeyboardMarkup(Keyboard.MAIN_KEYBOARD)
    await query.edit_message_text(
        text="Start handler, Choose a route again!", reply_markup=reply_markup
    )
    return StartEndRoutes.start_route


async def show_specific_keyboard(update: Update, context: ContextTypes.DEFAULT_TYPE, text: str,
                                 keyboard: List[List[InlineKeyboardButton]]) -> StartEndRoutes:
    query = update.callback_query
    await query.answer()
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text=text, reply_markup=reply_markup)
    return StartEndRoutes.end_route


async def brand(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_specific_keyboard(update, context, "brand", Keyboard.BRAND_KEYBOARD)


async def model(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
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
