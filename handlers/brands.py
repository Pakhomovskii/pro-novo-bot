from telegram import Update
from telegram.ext import ContextTypes

from handlers.handlers import show_specific_keyboard_to_change_order
from keyboards.keyboards import Keyboard
from routes.routes import StartEndRoutes


async def acura(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_specific_keyboard_to_change_order(update, context, "brand", "Acura", Keyboard.BRAND_KEYBOARD)


async def daewoo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_specific_keyboard_to_change_order(update, context, "brand", "Daewoo", Keyboard.BRAND_KEYBOARD)


async def datsun(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_specific_keyboard_to_change_order(update, context, "brand", "Datsun", Keyboard.BRAND_KEYBOARD)


async def mazda(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_specific_keyboard_to_change_order(update, context, "brand", "Mazda", Keyboard.BRAND_KEYBOARD)


async def subaru(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_specific_keyboard_to_change_order(update, context, "brand", "Subaru", Keyboard.BRAND_KEYBOARD)
