from telegram import Update
from telegram.ext import ContextTypes

from handlers.handlers import show_keyboard1, show_keyboard2
from keyboards.keyboards import Keyboard
from routes.routes import StartEndRoutes


async def one(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.budget:
    return await show_keyboard1(update, context, Keyboard.BUDGET_KEYBOARD, text="1", opa=" euro")


async def two(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.budget:
    return await show_keyboard1(update, context, Keyboard.BUDGET_KEYBOARD, text="2", opa=" euro")


async def three(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.budget:
    return await show_keyboard1(update, context, Keyboard.BUDGET_KEYBOARD, text="3", opa=" euro")


async def four(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.budget:
    return await show_keyboard1(update, context, Keyboard.BUDGET_KEYBOARD, text="4", opa=" euro")


async def five(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.budget:
    return await show_keyboard1(update, context, Keyboard.BUDGET_KEYBOARD, text="5", opa=" euro")


async def six(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.budget:
    return await show_keyboard1(update, context, Keyboard.BUDGET_KEYBOARD, text="6", opa=" euro")


async def seven(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.budget:
    return await show_keyboard1(update, context, Keyboard.BUDGET_KEYBOARD, text="7", opa=" euro")


async def eight(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.budget:
    return await show_keyboard1(update, context, Keyboard.BUDGET_KEYBOARD, text="8", opa=" euro")


async def nine(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.budget:
    return await show_keyboard1(update, context, Keyboard.BUDGET_KEYBOARD, text="9", opa=" euro")


async def zero(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.budget:
    return await show_keyboard1(update, context, Keyboard.BUDGET_KEYBOARD, text="0", opa=" euro")


async def one2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.budget2:
    return await show_keyboard2(update, context, Keyboard.BUDGET_KEYBOARD2, text="1", opa=" euro")


async def two2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.budget2:
    return await show_keyboard2(update, context, Keyboard.BUDGET_KEYBOARD2, text="2", opa=" euro")


async def three2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.budget2:
    return await show_keyboard2(update, context, Keyboard.BUDGET_KEYBOARD2, text="3", opa=" euro")


async def four2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.budget2:
    return await show_keyboard2(update, context, Keyboard.BUDGET_KEYBOARD2, text="4", opa=" euro")


async def five2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.budget2:
    return await show_keyboard2(update, context, Keyboard.BUDGET_KEYBOARD2, text="5", opa=" euro")


async def six2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.budget2:
    return await show_keyboard2(update, context, Keyboard.BUDGET_KEYBOARD2, text="6", opa=" euro")


async def seven2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.budget2:
    return await show_keyboard2(update, context, Keyboard.BUDGET_KEYBOARD2, text="7", opa=" euro")


async def eight2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.budget2:
    return await show_keyboard2(update, context, Keyboard.BUDGET_KEYBOARD2, text="8", opa=" euro")


async def nine2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.budget2:
    return await show_keyboard2(update, context, Keyboard.BUDGET_KEYBOARD2, text="9", opa=" euro")


async def zero2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.budget2:
    return await show_keyboard2(update, context, Keyboard.BUDGET_KEYBOARD2, text="0", opa=" euro")
