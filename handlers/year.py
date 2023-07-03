from telegram import Update
from telegram.ext import ContextTypes

from handlers.handlers import show_specific_keyboard_to_change_order
from keyboards.keyboards import Keyboard
from routes.routes import StartEndRoutes


async def year_less_3(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_specific_keyboard_to_change_order(update, context, "year", "меньше 3-х лет",
                                                        Keyboard.YEAR_KEYBOARD)


async def year_3_5(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_specific_keyboard_to_change_order(update, context, "year", "3-5 лет",
                                                        Keyboard.YEAR_KEYBOARD)


async def year_5_7(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_specific_keyboard_to_change_order(update, context, "year", "5-7 лет",
                                                        Keyboard.YEAR_KEYBOARD)


async def year_more_7(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_specific_keyboard_to_change_order(update, context, "year", "больше 7 лет",
                                                        Keyboard.YEAR_KEYBOARD)
