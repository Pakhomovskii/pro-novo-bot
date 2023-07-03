import os

from dotenv import load_dotenv
from telegram import __version__ as TG_VER
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ConversationHandler,
)

from handlers.brands import subaru, mazda
from handlers.budget_keyboards import (
    one, two, three, four, five, six, seven, eight, nine, zero, zero2, nine2, eight2,
    seven2, six2, five2, four2, three2, two2, one2
)
from handlers.engine_capacity import _10, _11, _12, _13, _14, _15, _16, _17, _18, _19, _20, _21, _22, _23, _24, _25, \
    _26, _27, _28, _29, _30, _31, _32, _33, _34, _35, _36, _37, _38, _39, _40, _41, _42, _43, _44, _45, _46, _47, _48, \
    _49, _50, _51, _52, _53, _54, _55, _56, _57, _58, _59
from handlers.hand_drive import hand_drive_right, hand_drive_left
from handlers.handlers import (

    brand, \
    budget, send,
    start, start_over, aplay_new_budget, aplay_new_budget2, model, year,
    engine_capacity, hand_drive,

)
from handlers.models import impreza, cx_8
from handlers.year import year_more_7, year_3_5, year_less_3, year_5_7
from routes.routes import Routes, StartEndRoutes, RoutesBrand, RoutesModel, RoutesBudgetKeyboard1, RoutesEngineCapacity, \
    RoutesYear, RoutesHandDrive

load_dotenv()
TOKEN = os.getenv("TOKEN")

try:
    from telegram import __version_info__
except ImportError:
    __version_info__ = (0, 0, 0, 0, 0)

if __version_info__ < (20, 0, 0, "alpha", 1):
    raise RuntimeError(
        f"This example is not compatible with your current PTB version {TG_VER}. To view the "
        f"{TG_VER} version of this example, "
        f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
    )


def main() -> None:
    with open('database/init-database.py', 'r') as file:
        script_code = file.read()
        exec(script_code)

    application = Application.builder().token(TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            StartEndRoutes.start_route: [
                CallbackQueryHandler(brand, pattern="^" + str(Routes.brand) + "$"),

                CallbackQueryHandler(model, pattern="^" + str(Routes.model) + "$"),
                # CallbackQueryHandler(model_mazda, pattern="^" + str(StartEndRoutes.model_mazda) + "$"),
                # CallbackQueryHandler(model_subaru, pattern="^" + str(StartEndRoutes.model_subaru) + "$"),
                CallbackQueryHandler(hand_drive, pattern="^" + str(Routes.hand_drive) + "$"),
                # CallbackQueryHandler(body_type, pattern="^" + str(Routes.body_type) + "$"),
                # CallbackQueryHandler(drive, pattern="^" + str(Routes.drive) + "$"),
                CallbackQueryHandler(engine_capacity, pattern="^" + str(Routes.engine_capacity) + "$"
                                     ),
                CallbackQueryHandler(year, pattern="^" + str(Routes.year) + "$"),
                # CallbackQueryHandler(fuel_type, pattern="^" + str(Routes.fuel_type) + "$"),
                CallbackQueryHandler(budget, pattern="^" + str(Routes.budget) + "$"),
                # CallbackQueryHandler(delete, pattern="^" + str(Routes.delete) + "$"),
                CallbackQueryHandler(send, pattern="^" + str(Routes.send) + "$"),
                # CallbackQueryHandler(tax, pattern="^" + str(Routes.tax) + "$"),
            ],

            StartEndRoutes.budget: [

                CallbackQueryHandler(one, pattern="^" + str(RoutesBudgetKeyboard1.one) + "$"),
                CallbackQueryHandler(two, pattern="^" + str(RoutesBudgetKeyboard1.two) + "$"),
                CallbackQueryHandler(three, pattern="^" + str(RoutesBudgetKeyboard1.three) + "$"),
                CallbackQueryHandler(four, pattern="^" + str(RoutesBudgetKeyboard1.four) + "$"),
                CallbackQueryHandler(five, pattern="^" + str(RoutesBudgetKeyboard1.five) + "$"),
                CallbackQueryHandler(six, pattern="^" + str(RoutesBudgetKeyboard1.six) + "$"),
                CallbackQueryHandler(seven, pattern="^" + str(RoutesBudgetKeyboard1.seven) + "$"),
                CallbackQueryHandler(eight, pattern="^" + str(RoutesBudgetKeyboard1.eight) + "$"),
                CallbackQueryHandler(nine, pattern="^" + str(RoutesBudgetKeyboard1.nine) + "$"),
                CallbackQueryHandler(zero, pattern="^" + str(RoutesBudgetKeyboard1.zero) + "$"),
                CallbackQueryHandler(aplay_new_budget, pattern="^" + str(Routes.aplay_new_budget) + "$"),
                CallbackQueryHandler(start_over, pattern="^" + str(Routes.back) + "$"),
            ],

            StartEndRoutes.budget2: [
                CallbackQueryHandler(one2, pattern="^" + str(RoutesBudgetKeyboard1.one) + "$"),
                CallbackQueryHandler(two2, pattern="^" + str(RoutesBudgetKeyboard1.two) + "$"),
                CallbackQueryHandler(three2, pattern="^" + str(RoutesBudgetKeyboard1.three) + "$"),
                CallbackQueryHandler(four2, pattern="^" + str(RoutesBudgetKeyboard1.four) + "$"),
                CallbackQueryHandler(five2, pattern="^" + str(RoutesBudgetKeyboard1.five) + "$"),
                CallbackQueryHandler(six2, pattern="^" + str(RoutesBudgetKeyboard1.six) + "$"),
                CallbackQueryHandler(seven2, pattern="^" + str(RoutesBudgetKeyboard1.seven) + "$"),
                CallbackQueryHandler(eight2, pattern="^" + str(RoutesBudgetKeyboard1.eight) + "$"),
                CallbackQueryHandler(nine2, pattern="^" + str(RoutesBudgetKeyboard1.nine) + "$"),
                CallbackQueryHandler(zero2, pattern="^" + str(RoutesBudgetKeyboard1.zero) + "$"),
                CallbackQueryHandler(aplay_new_budget2, pattern="^" + str(Routes.aplay_new_budget2) + "$"),
                CallbackQueryHandler(start_over, pattern="^" + str(Routes.back2) + "$"),

            ],
            StartEndRoutes.engine_capacity: [
                CallbackQueryHandler(_10, pattern="^" + str(RoutesEngineCapacity._10) + "$"),
                CallbackQueryHandler(_11, pattern="^" + str(RoutesEngineCapacity._11) + "$"),
                CallbackQueryHandler(_12, pattern="^" + str(RoutesEngineCapacity._12) + "$"),
                CallbackQueryHandler(_13, pattern="^" + str(RoutesEngineCapacity._13) + "$"),
                CallbackQueryHandler(_14, pattern="^" + str(RoutesEngineCapacity._14) + "$"),
                CallbackQueryHandler(_15, pattern="^" + str(RoutesEngineCapacity._15) + "$"),
                CallbackQueryHandler(_16, pattern="^" + str(RoutesEngineCapacity._16) + "$"),
                CallbackQueryHandler(_17, pattern="^" + str(RoutesEngineCapacity._17) + "$"),
                CallbackQueryHandler(_18, pattern="^" + str(RoutesEngineCapacity._18) + "$"),
                CallbackQueryHandler(_19, pattern="^" + str(RoutesEngineCapacity._19) + "$"),
                CallbackQueryHandler(_20, pattern="^" + str(RoutesEngineCapacity._20) + "$"),
                CallbackQueryHandler(_21, pattern="^" + str(RoutesEngineCapacity._21) + "$"),
                CallbackQueryHandler(_22, pattern="^" + str(RoutesEngineCapacity._22) + "$"),
                CallbackQueryHandler(_23, pattern="^" + str(RoutesEngineCapacity._23) + "$"),
                CallbackQueryHandler(_24, pattern="^" + str(RoutesEngineCapacity._24) + "$"),
                CallbackQueryHandler(_25, pattern="^" + str(RoutesEngineCapacity._25) + "$"),
                CallbackQueryHandler(_26, pattern="^" + str(RoutesEngineCapacity._26) + "$"),
                CallbackQueryHandler(_27, pattern="^" + str(RoutesEngineCapacity._27) + "$"),
                CallbackQueryHandler(_28, pattern="^" + str(RoutesEngineCapacity._28) + "$"),
                CallbackQueryHandler(_29, pattern="^" + str(RoutesEngineCapacity._29) + "$"),
                CallbackQueryHandler(_30, pattern="^" + str(RoutesEngineCapacity._30) + "$"),
                CallbackQueryHandler(_31, pattern="^" + str(RoutesEngineCapacity._31) + "$"),
                CallbackQueryHandler(_32, pattern="^" + str(RoutesEngineCapacity._32) + "$"),
                CallbackQueryHandler(_33, pattern="^" + str(RoutesEngineCapacity._33) + "$"),
                CallbackQueryHandler(_34, pattern="^" + str(RoutesEngineCapacity._34) + "$"),
                CallbackQueryHandler(_35, pattern="^" + str(RoutesEngineCapacity._35) + "$"),
                CallbackQueryHandler(_36, pattern="^" + str(RoutesEngineCapacity._36) + "$"),
                CallbackQueryHandler(_37, pattern="^" + str(RoutesEngineCapacity._37) + "$"),
                CallbackQueryHandler(_38, pattern="^" + str(RoutesEngineCapacity._38) + "$"),
                CallbackQueryHandler(_39, pattern="^" + str(RoutesEngineCapacity._39) + "$"),
                CallbackQueryHandler(_40, pattern="^" + str(RoutesEngineCapacity._40) + "$"),
                CallbackQueryHandler(_41, pattern="^" + str(RoutesEngineCapacity._41) + "$"),
                CallbackQueryHandler(_42, pattern="^" + str(RoutesEngineCapacity._42) + "$"),
                CallbackQueryHandler(_43, pattern="^" + str(RoutesEngineCapacity._43) + "$"),
                CallbackQueryHandler(_44, pattern="^" + str(RoutesEngineCapacity._44) + "$"),
                CallbackQueryHandler(_45, pattern="^" + str(RoutesEngineCapacity._45) + "$"),
                CallbackQueryHandler(_46, pattern="^" + str(RoutesEngineCapacity._46) + "$"),
                CallbackQueryHandler(_47, pattern="^" + str(RoutesEngineCapacity._47) + "$"),
                CallbackQueryHandler(_48, pattern="^" + str(RoutesEngineCapacity._48) + "$"),
                CallbackQueryHandler(_49, pattern="^" + str(RoutesEngineCapacity._49) + "$"),
                CallbackQueryHandler(_50, pattern="^" + str(RoutesEngineCapacity._50) + "$"),
                CallbackQueryHandler(_51, pattern="^" + str(RoutesEngineCapacity._51) + "$"),
                CallbackQueryHandler(_52, pattern="^" + str(RoutesEngineCapacity._52) + "$"),
                CallbackQueryHandler(_53, pattern="^" + str(RoutesEngineCapacity._53) + "$"),
                CallbackQueryHandler(_54, pattern="^" + str(RoutesEngineCapacity._54) + "$"),
                CallbackQueryHandler(_55, pattern="^" + str(RoutesEngineCapacity._55) + "$"),
                CallbackQueryHandler(_56, pattern="^" + str(RoutesEngineCapacity._56) + "$"),
                CallbackQueryHandler(_57, pattern="^" + str(RoutesEngineCapacity._57) + "$"),
                CallbackQueryHandler(_58, pattern="^" + str(RoutesEngineCapacity._58) + "$"),
                CallbackQueryHandler(_59, pattern="^" + str(RoutesEngineCapacity._59) + "$"),

                CallbackQueryHandler(start_over, pattern="^" + str(Routes.back) + "$"),

            ],

            Routes.send: [
                CallbackQueryHandler(start_over, pattern="^" + str(Routes.back) + "$"),
                CallbackQueryHandler(start_over, pattern="^" + str(Routes.back2) + "$"),
            ],

            StartEndRoutes.end_route: [
                CallbackQueryHandler(start_over, pattern="^" + str(Routes.back) + "$"),
                CallbackQueryHandler(start_over, pattern="^" + str(Routes.back2) + "$"),
            ],
            StartEndRoutes.brand: [

                CallbackQueryHandler(mazda, pattern="^" + str(RoutesBrand.mazda) + "$"),
                CallbackQueryHandler(subaru, pattern="^" + str(RoutesBrand.subaru) + "$"),
                CallbackQueryHandler(start_over, pattern="^" + str(Routes.back) + "$"),
            ],
            StartEndRoutes.model_mazda: [

                CallbackQueryHandler(cx_8, pattern="^" + str(RoutesModel.cx_8) + "$"),
                CallbackQueryHandler(start_over, pattern="^" + str(Routes.back) + "$"),

            ],
            StartEndRoutes.model_subaru: [

                CallbackQueryHandler(impreza, pattern="^" + str(RoutesModel.impreza) + "$"),
                CallbackQueryHandler(start_over, pattern="^" + str(Routes.back) + "$"),

            ],
            StartEndRoutes.year: [

                CallbackQueryHandler(year_less_3, pattern="^" + str(RoutesYear.year_less_3) + "$"),
                CallbackQueryHandler(year_3_5, pattern="^" + str(RoutesYear.year_3_5) + "$"),
                CallbackQueryHandler(year_5_7, pattern="^" + str(RoutesYear.year_5_7) + "$"),
                CallbackQueryHandler(year_more_7, pattern="^" + str(RoutesYear.year_more_7) + "$"),
                CallbackQueryHandler(start_over, pattern="^" + str(Routes.back) + "$"),

            ],
            StartEndRoutes.hand_drive: [

                CallbackQueryHandler(hand_drive_right, pattern="^" + str(RoutesHandDrive.hand_drive_right) + "$"),
                CallbackQueryHandler(hand_drive_left, pattern="^" + str(RoutesHandDrive.hand_drive_left) + "$"),
                CallbackQueryHandler(start_over, pattern="^" + str(Routes.back) + "$"),
            ],

        },
        fallbacks=[CommandHandler("start", start)],
    )

    application.add_handler(conv_handler)
    application.run_polling()


if __name__ == "__main__":
    main()
