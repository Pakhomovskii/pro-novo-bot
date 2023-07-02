from telegram import Update
from telegram.ext import ContextTypes

from handlers.handlers import show_specific_keyboard_to_change_order
from keyboards.keyboards import Keyboard
from routes.routes import StartEndRoutes


async def impreza(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.model:
    return await show_specific_keyboard_to_change_order(update, context, "model", "impreza", Keyboard.MODEL_KEYBOARD)


async def cx_8(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.model:
    return await show_specific_keyboard_to_change_order(update, context, "model", " CX-8", Keyboard.MODEL_KEYBOARD)
