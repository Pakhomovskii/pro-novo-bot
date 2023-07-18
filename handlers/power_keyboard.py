from telegram import Update
from telegram.ext import ContextTypes

from handlers.handlers import show_keyboard1, show_keyboard2
from keyboards.keyboards import Keyboard


async def pone(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return await show_keyboard1(update, context, Keyboard.POWER_POWER_KEYBOARD, text="1", opa="л.с.")


async def ptwo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return await show_keyboard1(update, context, Keyboard.POWER_POWER_KEYBOARD, text="2", opa="л.с.")


async def pthree(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return await show_keyboard1(update, context, Keyboard.POWER_POWER_KEYBOARD, text="3", opa="л.с.")


async def pfour(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return await show_keyboard1(update, context, Keyboard.POWER_POWER_KEYBOARD, text="4", opa="л.с.")


async def pfive(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return await show_keyboard1(update, context, Keyboard.POWER_POWER_KEYBOARD, text="5", opa="л.с.")


async def psix(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return await show_keyboard1(update, context, Keyboard.POWER_POWER_KEYBOARD, text="6", opa="л.с.")


async def pseven(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return await show_keyboard1(update, context, Keyboard.POWER_POWER_KEYBOARD, text="7", opa="л.с.")


async def peight(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return await show_keyboard1(update, context, Keyboard.POWER_POWER_KEYBOARD, text="8", opa="л.с.")


async def pnine(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return await show_keyboard1(update, context, Keyboard.POWER_POWER_KEYBOARD, text="9", opa="л.с.")


async def pzero(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return await show_keyboard1(update, context, Keyboard.POWER_POWER_KEYBOARD, text="0", opa="л.с.")


async def pone2(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("22222dddd")
    return await show_keyboard2(update, context, Keyboard.POWER_POWER_KEYBOARD2, text="1", opa="л.с.")


async def ptwo2(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return await show_keyboard2(update, context, Keyboard.POWER_POWER_KEYBOARD2, text="2", opa="л.с.")


async def pthree2(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return await show_keyboard2(update, context, Keyboard.POWER_POWER_KEYBOARD2, text="3", opa="л.с.")


async def pfour2(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return await show_keyboard2(update, context, Keyboard.POWER_POWER_KEYBOARD2, text="4", opa="л.с.")


async def pfive2(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return await show_keyboard2(update, context, Keyboard.POWER_POWER_KEYBOARD2, text="5", opa="л.с.")


async def psix2(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return await show_keyboard2(update, context, Keyboard.POWER_POWER_KEYBOARD2, text="6", opa="л.с.")


async def pseven2(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return await show_keyboard2(update, context, Keyboard.POWER_POWER_KEYBOARD2, text="7", opa="л.с.")


async def peight2(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return await show_keyboard2(update, context, Keyboard.POWER_POWER_KEYBOARD2, text="8", opa="л.с.")


async def pnine2(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return await show_keyboard2(update, context, Keyboard.POWER_POWER_KEYBOARD2, text="9", opa="л.с.")


async def pzero2(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return await show_keyboard2(update, context, Keyboard.POWER_POWER_KEYBOARD2, text="0", opa="л.с.")
