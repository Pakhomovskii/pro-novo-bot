from telegram import Update
from telegram.ext import ContextTypes

from handlers.handlers import show_specific_keyboard_to_change_order
from keyboards.keyboards import Keyboard
from routes.routes import StartEndRoutes


class Acura:
    async def MDX(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.model:
        return await show_specific_keyboard_to_change_order(update, context, "model", "MDX",
                                                            Keyboard.MODEL_KEYBOARD_ACURA)

    async def RDX(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.model:
        return await show_specific_keyboard_to_change_order(update, context, "model", "RDX",
                                                            Keyboard.MODEL_KEYBOARD_ACURA)

    async def TSX(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.model:
        return await show_specific_keyboard_to_change_order(update, context, "model", "TSX",
                                                            Keyboard.MODEL_KEYBOARD_ACURA)

    async def ZDX(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.model:
        return await show_specific_keyboard_to_change_order(update, context, "model", "ZDX",
                                                            Keyboard.MODEL_KEYBOARD_ACURA)

    async def ILX(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.model:
        return await show_specific_keyboard_to_change_order(update, context, "model", "ILX",
                                                            Keyboard.MODEL_KEYBOARD_ACURA)


class Daewoo:
    async def nexia(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.model:
        return await show_specific_keyboard_to_change_order(update, context, "model", "nexia",
                                                            Keyboard.MODEL_KEYBOARD_DAEWOO)

    async def matiz(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.model:
        return await show_specific_keyboard_to_change_order(update, context, "model", "matiz",
                                                            Keyboard.MODEL_KEYBOARD_DAEWOO)

    async def gentra(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.model:
        return await show_specific_keyboard_to_change_order(update, context, "model", "gentra",
                                                            Keyboard.MODEL_KEYBOARD_DAEWOO)

    async def lanos(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.model:
        return await show_specific_keyboard_to_change_order(update, context, "model", "lanos",

                                                            Keyboard.MODEL_KEYBOARD_DAEWOO)

    async def winstorm(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.model:
        return await show_specific_keyboard_to_change_order(update, context, "model", "winstorm",
                                                            Keyboard.MODEL_KEYBOARD_DAEWOO)


class Datsun:
    async def mi_do(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.model:
        return await show_specific_keyboard_to_change_order(update, context, "model", "mi_do",
                                                            Keyboard.MODEL_KEYBOARD_DATSUN)

    async def on_do(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.model:
        return await show_specific_keyboard_to_change_order(update, context, "model", "mi_do",
                                                            Keyboard.MODEL_KEYBOARD_DATSUN)


class Genesis:
    async def g70(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.model:
        return await show_specific_keyboard_to_change_order(update, context, "model", "G70",
                                                            Keyboard.MODEL_KEYBOARD_GENESIS)

    async def g80(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.model:
        return await show_specific_keyboard_to_change_order(update, context, "model", "G80",
                                                            Keyboard.MODEL_KEYBOARD_GENESIS)

    async def g90(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.model:
        return await show_specific_keyboard_to_change_order(update, context, "model", "G90",
                                                            Keyboard.MODEL_KEYBOARD_GENESIS)

    async def gv70(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.model:
        return await show_specific_keyboard_to_change_order(update, context, "model", "GV70",
                                                            Keyboard.MODEL_KEYBOARD_GENESIS)

    async def gv80(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.model:
        return await show_specific_keyboard_to_change_order(update, context, "model", "GV80",
                                                            Keyboard.MODEL_KEYBOARD_GENESIS)


class Honda:
    async def fit(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.model:
        return await show_specific_keyboard_to_change_order(update, context, "model", "fit",
                                                            Keyboard.MODEL_KEYBOARD_GENESIS)

    async def freed(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.model:
        return await show_specific_keyboard_to_change_order(update, context, "model", "freed",
                                                            Keyboard.MODEL_KEYBOARD_GENESIS)

    async def cr_v(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.model:
        return await show_specific_keyboard_to_change_order(update, context, "model", "cr_v",
                                                            Keyboard.MODEL_KEYBOARD_GENESIS)

    async def accord(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.model:
        return await show_specific_keyboard_to_change_order(update, context, "model", "accord",
                                                            Keyboard.MODEL_KEYBOARD_GENESIS)

    async def vezel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> StartEndRoutes.model:
        return await show_specific_keyboard_to_change_order(update, context, "model", "vezel",
                                                            Keyboard.MODEL_KEYBOARD_GENESIS)


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
        return await show_specific_keyboard_to_change_order(update, context, "model", "CX-8",
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
