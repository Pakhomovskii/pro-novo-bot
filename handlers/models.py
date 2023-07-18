from telegram import Update
from telegram.ext import ContextTypes

from handlers.handlers import show_specific_keyboard_to_change_order
from keyboards.keyboards import Keyboard
from routes.routes import StartEndRoutes


class Acura:
    async def MDX(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.model:
        return await show_specific_keyboard_to_change_order(update, context, "model", " MDX",
                                                            Keyboard.MODEL_KEYBOARD_ACURA)

    async def RDX(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.model:
        return await show_specific_keyboard_to_change_order(update, context, "model", " RDX",
                                                            Keyboard.MODEL_KEYBOARD_ACURA)

    async def TSX(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.model:
        return await show_specific_keyboard_to_change_order(update, context, "model", " TSX",
                                                            Keyboard.MODEL_KEYBOARD_ACURA)

    async def ZDX(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.model:
        return await show_specific_keyboard_to_change_order(update, context, "model", " ZDX",
                                                            Keyboard.MODEL_KEYBOARD_ACURA)

    async def ILX(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.model:
        return await show_specific_keyboard_to_change_order(update, context, "model", " ILX",
                                                            Keyboard.MODEL_KEYBOARD_ACURA)


class Daewoo:
    async def nexia(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.model:
        return await show_specific_keyboard_to_change_order(update, context, "model", " nexia",
                                                            Keyboard.MODEL_KEYBOARD_DAEWOO)

    async def matiz(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.model:
        return await show_specific_keyboard_to_change_order(update, context, "model", " matiz",
                                                            Keyboard.MODEL_KEYBOARD_DAEWOO)

    async def gentra(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.model:
        return await show_specific_keyboard_to_change_order(update, context, "model", " gentra",
                                                            Keyboard.MODEL_KEYBOARD_DAEWOO)

    async def lanos(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.model:
        return await show_specific_keyboard_to_change_order(update, context, "model", " lanos",

                                                            Keyboard.MODEL_KEYBOARD_DAEWOO)

    async def winstorm(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.model:
        return await show_specific_keyboard_to_change_order(update, context, "model", " winstorm",
                                                            Keyboard.MODEL_KEYBOARD_DAEWOO)


class Datsun:
    pass


class Genesis:
    pass


class Honda:
    pass


class Hyundai:
    pass


class Infinity:
    pass


class Isuzu:
    pass


class KIA:
    pass


class Lexus:
    pass


class Mazda:
    async def cx_8(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.model:
        return await show_specific_keyboard_to_change_order(update, context, "model", " CX-8",
                                                            Keyboard.MODEL_KEYBOARD_MAZDA)


class Mitsubishi:
    pass


class SsangYong:
    pass


class Subaru:
    async def impreza(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.model:
        return await show_specific_keyboard_to_change_order(update, context, "model", "Impreza",
                                                            Keyboard.MODEL_KEYBOARD_SUBARU)


class Suzuki:
    pass


class Toyota:
    pass
