from telegram import Update
from telegram.ext import ContextTypes

from handlers.handlers import show_specific_keyboard_to_change_order
from keyboards.keyboards import Keyboard
from routes.routes import StartEndRoutes


async def petrol(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_specific_keyboard_to_change_order(update, context, "fuel_type", "Бензин",
                                                        Keyboard.FUEL_KEYBOARD)


async def diesel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_specific_keyboard_to_change_order(update, context, "fuel_type", "Дизель",
                                                        Keyboard.FUEL_KEYBOARD)


async def hybrid(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_specific_keyboard_to_change_order(update, context, "fuel_type", "Гибрид",
                                                        Keyboard.FUEL_KEYBOARD)


async def electro(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_specific_keyboard_to_change_order(update, context, "fuel_type", "Электро",
                                                        Keyboard.FUEL_KEYBOARD)
