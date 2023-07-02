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
from handlers.handlers import (

    brand, \
    budget, send,
    start, start_over, aplay_new_budget, aplay_new_budget2, model,

)
from handlers.models import impreza, cx_8
from routes.routes import Routes, StartEndRoutes, RoutesBrand, RoutesModel, RoutesBudgetKeyboard1

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


def main(model_subaru=None, model_mazda=None) -> None:
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
                # CallbackQueryHandler(pts, pattern="^" + str(Routes.pts) + "$"),
                # CallbackQueryHandler(body_type, pattern="^" + str(Routes.body_type) + "$"),
                # CallbackQueryHandler(drive, pattern="^" + str(Routes.drive) + "$"),
                # CallbackQueryHandler(
                #     engine_capacity, pattern="^" + str(Routes.engine_capacity) + "$"
                # ),
                # CallbackQueryHandler(yeah, pattern="^" + str(Routes.year) + "$"),
                # CallbackQueryHandler(fuel_type, pattern="^" + str(Routes.fuel_type) + "$"),
                CallbackQueryHandler(budget, pattern="^" + str(Routes.budget) + "$"),
                # CallbackQueryHandler(delete, pattern="^" + str(Routes.delete) + "$"),
                CallbackQueryHandler(send, pattern="^" + str(Routes.send) + "$"),
                # CallbackQueryHandler(tax, pattern="^" + str(Routes.tax) + "$"),
            ],

            StartEndRoutes.budget: [
                # CallbackQueryHandler(user_budget_answer1, pattern="^" + str(Routes.first_keyboard) + "$"),
                # CallbackQueryHandler(start_over, pattern="^" + str(Routes.second_back) + "$"),
                # CallbackQueryHandler(user_budget_answer2, pattern="^" + str(Routes.second_keyboard) + "$"),
                # CallbackQueryHandler(start_over, pattern="^" + str(Routes.third_back) + "$"),

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
                # CallbackQueryHandler(user_budget_answer1, pattern="^" + str(Routes.first_keyboard) + "$"),
                # CallbackQueryHandler(start_over, pattern="^" + str(Routes.second_back) + "$"),
                # CallbackQueryHandler(user_budget_answer2, pattern="^" + str(Routes.second_keyboard) + "$"),
                # CallbackQueryHandler(start_over, pattern="^" + str(Routes.third_back) + "$"),

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
            StartEndRoutes.model: [

                CallbackQueryHandler(impreza, pattern="^" + str(RoutesModel.impreza) + "$"),
                CallbackQueryHandler(cx_8, pattern="^" + str(RoutesModel.cx_8) + "$"),
                CallbackQueryHandler(start_over, pattern="^" + str(Routes.back) + "$"),

            ],

            # CallbackQueryHandler(one, pattern="^" + str(RoutesBudgetKeyboard1.one) + "$"),
            # CallbackQueryHandler(two, pattern="^" + str(RoutesBudgetKeyboard1.two) + "$"),
            # CallbackQueryHandler(three, pattern="^" + str(RoutesBudgetKeyboard1.three) + "$"),
            # CallbackQueryHandler(four, pattern="^" + str(RoutesBudgetKeyboard1.four) + "$"),
            # CallbackQueryHandler(five, pattern="^" + str(RoutesBudgetKeyboard1.five) + "$"),
            # CallbackQueryHandler(six, pattern="^" + str(RoutesBudgetKeyboard1.six) + "$"),
            # CallbackQueryHandler(seven, pattern="^" + str(RoutesBudgetKeyboard1.seven) + "$"),
            # CallbackQueryHandler(eight, pattern="^" + str(RoutesBudgetKeyboard1.eight) + "$"),
            # CallbackQueryHandler(nine, pattern="^" + str(RoutesBudgetKeyboard1.nine) + "$"),
            # CallbackQueryHandler(zero, pattern="^" + str(RoutesBudgetKeyboard1.zero) + "$"),
            #
            # CallbackQueryHandler(one2, pattern="^" + str(RoutesBudgetKeyboard2.one2) + "$"),
            # CallbackQueryHandler(two2, pattern="^" + str(RoutesBudgetKeyboard2.two2) + "$"),
            # CallbackQueryHandler(three2, pattern="^" + str(RoutesBudgetKeyboard2.three2) + "$"),
            # CallbackQueryHandler(four2, pattern="^" + str(RoutesBudgetKeyboard2.four2) + "$"),
            # CallbackQueryHandler(five2, pattern="^" + str(RoutesBudgetKeyboard2.five2) + "$"),
            # CallbackQueryHandler(six2, pattern="^" + str(RoutesBudgetKeyboard2.six2) + "$"),
            # CallbackQueryHandler(seven2, pattern="^" + str(RoutesBudgetKeyboard2.seven2) + "$"),
            # CallbackQueryHandler(eight2, pattern="^" + str(RoutesBudgetKeyboard2.eight2) + "$"),
            # CallbackQueryHandler(nine2, pattern="^" + str(RoutesBudgetKeyboard2.nine2) + "$"),
            # CallbackQueryHandler(zero2, pattern="^" + str(RoutesBudgetKeyboard2.zero2) + "$"),

            # CallbackQueryHandler(update_user_order, pattern="^" + str(Routes.update_user_order) + "$"),

            # UserAnswerRoutes1.user_budget_answer1: [
            #     CallbackQueryHandler(user_budget_answer2, pattern="^" + str(AnswerRoutes1.first_keyboard) + "$"),
            #     # CallbackQueryHandler(start_over, pattern="^" + str(Routes.second_back) + "$"),
            # ],
            # UserAnswerRoutes2.user_budget_answer2: [
            #     CallbackQueryHandler(user_budget_answer1, pattern="^" + str(AnswerRoutes2.second_keyboard) + "$"),
            #     # CallbackQueryHandler(start_over, pattern="^" + str(Routes.third_back) + "$"),
            # ],
        },
        fallbacks=[CommandHandler("start", start)],
    )

    application.add_handler(conv_handler)
    application.run_polling()


if __name__ == "__main__":
    main()
