from telegram import Update
from telegram.ext import ContextTypes

from handlers.handlers import show_specific_keyboard_to_change_order
from keyboards.keyboards import Keyboard
from routes.routes import StartEndRoutes


async def rear(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_specific_keyboard_to_change_order(update, context, "drive", "Задний",
                                                        Keyboard.YEAR_KEYBOARD)


async def front(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_specific_keyboard_to_change_order(update, context, "drive", "Передний",
                                                        Keyboard.YEAR_KEYBOARD)


async def drive_four(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_specific_keyboard_to_change_order(update, context, "drive", "Полный",
                                                        Keyboard.YEAR_KEYBOARD)


async def connected(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_specific_keyboard_to_change_order(update, context, "drive", "Подключаемый",
                                                        Keyboard.YEAR_KEYBOARD)
