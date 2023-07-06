from telegram import Update
from telegram.ext import ContextTypes

from handlers.handlers import show_pop_up
from routes.routes import StartEndRoutes


async def send(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes:
    return await show_pop_up(update, context, "send")
