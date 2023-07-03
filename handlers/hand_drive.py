from telegram import Update
from telegram.ext import ContextTypes

from handlers.handlers import show_specific_keyboard_to_change_order
from keyboards.keyboards import Keyboard
from routes.routes import StartEndRoutes


async def hand_drive_right(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_specific_keyboard_to_change_order(update, context, "hand_drive", "Правый",
                                                        Keyboard.HAND_DRIVE_KEYBOARD)


async def hand_drive_left(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_specific_keyboard_to_change_order(update, context, "hand_drive", "Левый",
                                                        Keyboard.HAND_DRIVE_KEYBOARD)
