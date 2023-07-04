from telegram import Update
from telegram.ext import ContextTypes

from handlers.handlers import show_specific_keyboard_to_change_order
from keyboards.keyboards import Keyboard
from routes.routes import StartEndRoutes


async def v_50_100(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_specific_keyboard_to_change_order(update, context, "power", "50_100 л.с.",
                                                        Keyboard.POWER_KEYBOARD)


async def v_101_150(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_specific_keyboard_to_change_order(update, context, "power", "101_150 л.с.",
                                                        Keyboard.POWER_KEYBOARD)


async def v_151_200(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_specific_keyboard_to_change_order(update, context, "power", "151_200 л.с.",
                                                        Keyboard.POWER_KEYBOARD)


async def v_201_250(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_specific_keyboard_to_change_order(update, context, "power", "201_250 л.с.",
                                                        Keyboard.POWER_KEYBOARD)


async def v_251_300(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_specific_keyboard_to_change_order(update, context, "power", "251_300 л.с.",
                                                        Keyboard.POWER_KEYBOARD)


async def v_301_350(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_specific_keyboard_to_change_order(update, context, "power", "301_350 л.с.",
                                                        Keyboard.POWER_KEYBOARD)


async def v_351_400(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_specific_keyboard_to_change_order(update, context, "power", "351_400 л.с.",
                                                        Keyboard.POWER_KEYBOARD)
