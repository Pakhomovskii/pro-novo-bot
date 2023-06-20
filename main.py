import os
import subprocess
from dotenv import load_dotenv
from handlers.handlers import (

    brand, \
    model, pts, body_type, drive, engine_capacity, yeah, fuel_type, budget, send,
    tax, \
    start_over, start, delete, update_user_order, mazda
)

from telegram import __version__ as TG_VER
from routes.routes import Routes, StartEndRoutes

from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ConversationHandler,
)

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
    """Run the bot."""

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
                CallbackQueryHandler(pts, pattern="^" + str(Routes.pts) + "$"),
                CallbackQueryHandler(body_type, pattern="^" + str(Routes.body_type) + "$"),
                CallbackQueryHandler(drive, pattern="^" + str(Routes.drive) + "$"),
                CallbackQueryHandler(
                    engine_capacity, pattern="^" + str(Routes.engine_capacity) + "$"
                ),
                CallbackQueryHandler(yeah, pattern="^" + str(Routes.year) + "$"),
                CallbackQueryHandler(fuel_type, pattern="^" + str(Routes.fuel_type) + "$"),
                CallbackQueryHandler(budget, pattern="^" + str(Routes.budget) + "$"),
                CallbackQueryHandler(delete, pattern="^" + str(Routes.delete) + "$"),
                CallbackQueryHandler(send, pattern="^" + str(Routes.send) + "$"),
                CallbackQueryHandler(tax, pattern="^" + str(Routes.tax) + "$"),
                # CallbackQueryHandler(start_over, pattern="^" + str(Routes.start_over) + "$"),

                # CallbackQueryHandler(start_over, pattern="^" + str(Routes.back) + "$"),

                # CallbackQueryHandler(user_budget_answer1, pattern="^" + str(Routes.first_keyboard) + "$"),
                # CallbackQueryHandler(start_over, pattern="^" + str(Routes.second_back) + "$"),
                # CallbackQueryHandler(user_budget_answer2, pattern="^" + str(Routes.second_keyboard) + "$"),
                # CallbackQueryHandler(start_over, pattern="^" + str(Routes.third_back) + "$"),


            ],
            StartEndRoutes.end_route: [
                CallbackQueryHandler(start_over, pattern="^" + str(Routes.back) + "$"),
                CallbackQueryHandler(mazda, pattern="^" + str(Routes.mazda) + "$"),

                # CallbackQueryHandler(update_user_order, pattern="^" + str(Routes.update_user_order) + "$"),

            ],
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
