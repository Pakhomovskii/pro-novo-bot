from typing import Callable

from telegram import Update, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from database.database import create_user, update_user_order
from keyboards.keyboards import Keyboard
import logging

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
    await query.answer()
    reply_markup = InlineKeyboardMarkup(Keyboard.MAIN_KEYBOARD)
    await query.edit_message_text(
        text="Start handler, Choose a route again", reply_markup=reply_markup
    )
    return StartEndRoutes.start_route


async def brand(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes: # USE INLIIIIINE MARKAP
    """Show new choice of buttons"""
    # user_chat_id = update.update_id

    # query = update.callback_query
    # data = query.data
    # print(f"data{type(data)}")
    # if data:
        # Redirect to the end route or perform any desired action
        # query.answer("You reached the end!")
    #     # return StartEndRoutes.end_route
    # await query.answer()
    # print("OOOOOOOOOOOOOOOOOOOO")
    # await update_user_order(brend=data, user_chat_id=user_chat_id)
    # print("AAAAAAAAAAAAAAAAa")
    # if data == 'Мазда':
    #     return StartEndRoutes.end_route

    reply_markup = InlineKeyboardMarkup(Keyboard.BRAND_KEYBOARD)
    # await query.edit_message_text(text="BRAND", reply_markup=reply_markup)
    await update.callback_query.message.edit_text("Please choose:", reply_markup=reply_markup)
    # await update.message.reply_text("Please choose:", reply_markup=reply_markup)

    # await query.answer()
    print("BBBBBBBBBBBBBBBBBB")
    query = update.callback_query
    data = query.data
    print("oooo")
    if data=="Мазда":
        return StartEndRoutes.end_route
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


async def budget(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    """Show new choice of buttons"""
    query = update.callback_query
    await query.answer()
    reply_markup = InlineKeyboardMarkup(Keyboard.BUDGET_KEYBOARD)
    await query.edit_message_text(text="BUDGET", reply_markup=reply_markup)

    return StartEndRoutes.end_route


async def send(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    """Show new choice of buttons"""
    query = update.callback_query
    await query.answer()
    reply_markup = InlineKeyboardMarkup(Keyboard.SEND)
    await query.edit_message_text(
        text="SENDED", reply_markup=reply_markup  # поставить ограничение
    )
    return StartEndRoutes.end_route


async def tax(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    """Show new choice of buttons"""
    query = update.callback_query
    await query.answer()
    reply_markup = InlineKeyboardMarkup(Keyboard.TAX)
    await query.edit_message_text(text="TAX", reply_markup=reply_markup)
    return StartEndRoutes.end_route


async def delete(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    """Show new choice of buttons"""
    query = update.callback_query
    await query.answer()
    reply_markup = InlineKeyboardMarkup(Keyboard.DELETE)
    await query.edit_message_text(text="DELETE", reply_markup=reply_markup)
    return StartEndRoutes.end_route

# async def update_user_order(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
#     """Show new choice of buttons"""
#     query = update.callback_query
#     await query.answer()
#     reply_markup = InlineKeyboardMarkup(Keyboard.MAIN_KEYBOARD)
#     await query.edit_message_text(text="UPDATE", reply_markup=reply_markup)
#     return StartEndRoutes.end_route

# async def user_budget(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     query = update.callback_query
#     await query.answer()
#     reply_markup = InlineKeyboardMarkup(Keyboard.BUDGET_KEYBOARD)
#     await query.edit_message_text(text="BUDGET_ANSWER", reply_markup=reply_markup)
#     return StartEndRoutes.end_route

#
# async def user_budget_answer1(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     query = update.callback_query
#     await query.answer()
#     reply_markup = InlineKeyboardMarkup(Keyboard.BUDGET_KEYBOARD_TYPING1)
#     await query.edit_message_text(text="BUDGET1", reply_markup=reply_markup)
#     return UserAnswerRoutes2.user_budget_answer2
#
#
# async def user_budget_answer2(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     query = update.callback_query
#     await query.answer()
#     reply_markup = InlineKeyboardMarkup(Keyboard.BUDGET_KEYBOARD_TYPING2)
#     await query.edit_message_text(text="BUDGET2", reply_markup=reply_markup)
#     return UserAnswerRoutes1.user_budget_answer1
