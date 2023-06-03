from typing import Callable

from telegram import Update, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from keyboards.keyboards import Keyboard
import logging

from routes.routes import Routes, StartEndRoutes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    """Send message on `/start`."""
    user = update.message.from_user
    # logging.info("User %s started the conversation.", user.first_name) #START LOGGGGING
    reply_markup = InlineKeyboardMarkup(Keyboard.MAIN_KEYBOARD)
    await update.message.reply_text(
        "Start handler, Choose a route", reply_markup=reply_markup
    )
    return StartEndRoutes.start_route


async def start_over(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    """Prompt same text & keyboard as `start` does but not as new message"""
    query = update.callback_query
    await query.answer()
    reply_markup = InlineKeyboardMarkup(Keyboard.MAIN_KEYBOARD)
    await query.edit_message_text(
        text="Start handler, Choose a route again", reply_markup=reply_markup
    )
    return StartEndRoutes.start_route


async def brend(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    """Show new choice of buttons"""
    query = update.callback_query
    await query.answer()
    reply_markup = InlineKeyboardMarkup(Keyboard.BREND_KEYBOARD)
    await query.edit_message_text(text="BREND", reply_markup=reply_markup)
    return StartEndRoutes.end_route


async def model(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    """Show new choice of buttons"""
    query = update.callback_query
    await query.answer()
    reply_markup = InlineKeyboardMarkup(Keyboard.MODEL_KEYBOARD)
    await query.edit_message_text(text="MODEL", reply_markup=reply_markup)
    return StartEndRoutes.end_route


async def pts(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    """Show new choice of buttons"""
    query = update.callback_query
    await query.answer()
    reply_markup = InlineKeyboardMarkup(Keyboard.PTS_KEYBOARD)
    await query.edit_message_text(text="PTS", reply_markup=reply_markup)
    return StartEndRoutes.end_route


async def body_type(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    """Show new choice of buttons"""
    query = update.callback_query
    await query.answer()
    reply_markup = InlineKeyboardMarkup(Keyboard.BODY_TYPE_KEYBOARD)
    await query.edit_message_text(text="BODYTYPE", reply_markup=reply_markup)
    return StartEndRoutes.end_route


async def drive(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    """Show new choice of buttons"""
    query = update.callback_query
    await query.answer()
    reply_markup = InlineKeyboardMarkup(Keyboard.DRIVE_KEYBOARD)
    await query.edit_message_text(text="DRIVE", reply_markup=reply_markup)
    return StartEndRoutes.end_route


async def engine_capacity(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    """Show new choice of buttons"""
    query = update.callback_query
    await query.answer()
    reply_markup = InlineKeyboardMarkup(Keyboard.ENGINE_CAPACITY_KEYBOARD)
    await query.edit_message_text(text="ENGINE_CAPACITY", reply_markup=reply_markup)
    return StartEndRoutes.end_route


async def yeah(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    """Show new choice of buttons"""
    query = update.callback_query
    await query.answer()
    reply_markup = InlineKeyboardMarkup(Keyboard.YEAR_KEYBOARD)
    await query.edit_message_text(text="YEAR", reply_markup=reply_markup)
    return StartEndRoutes.end_route


async def fuel_type(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    """Show new choice of buttons"""
    query = update.callback_query
    await query.answer()
    reply_markup = InlineKeyboardMarkup(Keyboard.FUEL_TYPE_KEYBOARD)
    await query.edit_message_text(text="FUEL_TYPE", reply_markup=reply_markup)
    return StartEndRoutes.end_route


async def buget(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    """Show new choice of buttons"""
    query = update.callback_query
    await query.answer()
    reply_markup = InlineKeyboardMarkup(Keyboard.BUGET_KEYBOARD)
    await query.edit_message_text(text="BUGET", reply_markup=reply_markup)
    return StartEndRoutes.end_route


async def send(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    """Show new choice of buttons"""
    query = update.callback_query
    await query.answer()
    reply_markup = InlineKeyboardMarkup(Keyboard.MAIN_KEYBOARD)
    await query.edit_message_text(
        text="SENDED", reply_markup=reply_markup  # поставить ограничение
    )
    return StartEndRoutes.end_route


async def tax(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    """Show new choice of buttons"""
    query = update.callback_query
    await query.answer()
    reply_markup = InlineKeyboardMarkup(Keyboard.MAIN_KEYBOARD)
    await query.edit_message_text(text="TAX", reply_markup=reply_markup)
    return StartEndRoutes.start_route


# async def end(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
#     """Returns `ConversationHandler.END`, which tells the
#     ConversationHandler that the conversation is over.
#     """
#     query = update.callback_query
#     await query.answer()
#     await query.edit_message_text(text="See you next time!")
#     return ConversationHandler.END
