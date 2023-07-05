from telegram import Update
from telegram.ext import ContextTypes

from handlers.handlers import show_keyboard1, show_keyboard2
from keyboards.keyboards import Keyboard
from routes.routes import StartEndRoutes


async def one(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.budget:
    return await show_keyboard1(update, context, "1", Keyboard.BUDGET_KEYBOARD)


async def two(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.budget:
    return await show_keyboard1(update, context, "2", Keyboard.BUDGET_KEYBOARD)


async def three(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.budget:
    return await show_keyboard1(update, context, "3", Keyboard.BUDGET_KEYBOARD)


async def four(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.budget:
    return await show_keyboard1(update, context, "4", Keyboard.BUDGET_KEYBOARD)


async def five(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.budget:
    return await show_keyboard1(update, context, "5", Keyboard.BUDGET_KEYBOARD)


async def six(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.budget:
    return await show_keyboard1(update, context, "6", Keyboard.BUDGET_KEYBOARD)


async def seven(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.budget:
    return await show_keyboard1(update, context, "7", Keyboard.BUDGET_KEYBOARD)


async def eight(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.budget:
    return await show_keyboard1(update, context, "8", Keyboard.BUDGET_KEYBOARD)


async def nine(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.budget:
    return await show_keyboard1(update, context, "9", Keyboard.BUDGET_KEYBOARD)


async def zero(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.budget:
    return await show_keyboard1(update, context, "0", Keyboard.BUDGET_KEYBOARD)


async def one2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.budget2:
    return await show_keyboard2(update, context, "1", Keyboard.BUDGET_KEYBOARD2)


async def two2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.budget2:
    return await show_keyboard2(update, context, "2", Keyboard.BUDGET_KEYBOARD2)


async def three2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.budget2:
    return await show_keyboard2(update, context, "3", Keyboard.BUDGET_KEYBOARD2)


async def four2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.budget2:
    return await show_keyboard2(update, context, "4", Keyboard.BUDGET_KEYBOARD2)


async def five2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.budget2:
    return await show_keyboard2(update, context, "5", Keyboard.BUDGET_KEYBOARD2)


async def six2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.budget2:
    return await show_keyboard2(update, context, "6", Keyboard.BUDGET_KEYBOARD2)


async def seven2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.budget2:
    return await show_keyboard2(update, context, "7", Keyboard.BUDGET_KEYBOARD2)


async def eight2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.budget2:
    return await show_keyboard2(update, context, "8", Keyboard.BUDGET_KEYBOARD2)


async def nine2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.budget2:
    return await show_keyboard2(update, context, "9", Keyboard.BUDGET_KEYBOARD2)


async def zero2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.budget2:
    return await show_keyboard2(update, context, "0", Keyboard.BUDGET_KEYBOARD2)
