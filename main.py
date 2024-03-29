import os

from dotenv import load_dotenv
from telegram import __version__ as TG_VER
from telegram.ext import (Application, CallbackQueryHandler, CommandHandler,
                          ConversationHandler)

from handlers.brands import mazda, subaru, acura, daewoo, datsun, genesis, honda, toyota
from handlers.budget_keyboards import (eight, eight2, five, five2, four, four2,
                                       nine, nine2, one, one2, seven, seven2,
                                       six, six2, three, three2, two, two2,
                                       zero, zero2)
from handlers.drive import connected, drive_four, front, rear
from handlers.engine import (r_10, r_11, r_12, r_13, r_14, r_15, r_16, r_17,
                             r_18, r_19, r_20, r_21, r_22, r_23, r_24, r_25,
                             r_26, r_27, r_28, r_29, r_30, r_31, r_32, r_33,
                             r_34, r_35, r_36, r_37, r_38, r_39, r_40, r_41,
                             r_42, r_43, r_44, r_45, r_46, r_47, r_48, r_49,
                             r_50, r_51, r_52, r_53, r_54, r_55, r_56, r_57)
from handlers.fuel import diesel, electro, hybrid, petrol
from handlers.hand_drive import hand_drive_left, hand_drive_right
from handlers.handlers import (aplay_new_budget, aplay_new_budget2, brand,
                               budget, drive, engine, hand_drive, model, power,
                               send, start, start_over, year, fuel_type, delete, aplay_new_power, aplay_new_power2,
                               start_over2)
from handlers.models import Mazda, Subaru, Daewoo, Acura, Datsun, Genesis, Honda, Toyota
from handlers.power_keyboard import (pone2, pone, ptwo, pthree, pfive, pfour,
                                     psix, pseven, peight, pnine, pzero, pseven2,
                                     pfive2, pfour2, pthree2, ptwo2,
                                     psix2, peight2, pnine2, pzero2)
from handlers.tax import tax
from handlers.year import year_3_5, year_5_7, year_less_3, year_more_7
from routes.routes import (Routes, RoutesBrand, RoutesBudgetKeyboard1,
                           RoutesBudgetKeyboard2, RoutesDrive, RoutesEngine,
                           RoutesFuel, RoutesHandDrive, RoutesModel,
                           RoutesYear, StartEndRoutes, RoutesPowerKeyboard1, RoutesPowerKeyboard2)

if os.environ.get('DEBUG') == "1":
    load_dotenv()
    TOKEN = os.getenv("TOKEN_DEBUG")
else:
    load_dotenv()
    TOKEN = os.getenv("TOKEN")

try:
    from telegram import __version_info__
except ImportError:
    __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]

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
                CallbackQueryHandler(hand_drive, pattern="^" + str(Routes.hand_drive) + "$"),
                CallbackQueryHandler(power, pattern="^" + str(Routes.power) + "$"),
                CallbackQueryHandler(drive, pattern="^" + str(Routes.drive) + "$"),
                CallbackQueryHandler(year, pattern="^" + str(Routes.year) + "$"),
                CallbackQueryHandler(fuel_type, pattern="^" + str(Routes.fuel_type) + "$"),
                CallbackQueryHandler(engine, pattern="^" + str(Routes.engine) + "$"),
                CallbackQueryHandler(budget, pattern="^" + str(Routes.budget) + "$"),
                CallbackQueryHandler(delete, pattern="^" + str(Routes.delete) + "$"),

                CallbackQueryHandler(send, pattern="^" + str(Routes.send) + "$"),
                CallbackQueryHandler(tax, pattern="^" + str(Routes.tax) + "$"),
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
                CallbackQueryHandler(one2, pattern="^" + str(RoutesBudgetKeyboard2.one2) + "$"),
                CallbackQueryHandler(two2, pattern="^" + str(RoutesBudgetKeyboard2.two2) + "$"),
                CallbackQueryHandler(three2, pattern="^" + str(RoutesBudgetKeyboard2.three2) + "$"),
                CallbackQueryHandler(four2, pattern="^" + str(RoutesBudgetKeyboard2.four2) + "$"),
                CallbackQueryHandler(five2, pattern="^" + str(RoutesBudgetKeyboard2.five2) + "$"),
                CallbackQueryHandler(six2, pattern="^" + str(RoutesBudgetKeyboard2.six2) + "$"),
                CallbackQueryHandler(seven2, pattern="^" + str(RoutesBudgetKeyboard2.seven2) + "$"),
                CallbackQueryHandler(eight2, pattern="^" + str(RoutesBudgetKeyboard2.eight2) + "$"),
                CallbackQueryHandler(nine2, pattern="^" + str(RoutesBudgetKeyboard2.nine2) + "$"),
                CallbackQueryHandler(zero2, pattern="^" + str(RoutesBudgetKeyboard2.zero2) + "$"),
                CallbackQueryHandler(aplay_new_budget2, pattern="^" + str(Routes.aplay_new_budget2) + "$"),
                CallbackQueryHandler(start_over2, pattern="^" + str(Routes.back2) + "$"),

            ],

            StartEndRoutes.power: [

                CallbackQueryHandler(pone, pattern="^" + str(RoutesPowerKeyboard1.pone) + "$"),
                CallbackQueryHandler(ptwo, pattern="^" + str(RoutesPowerKeyboard1.ptwo) + "$"),
                CallbackQueryHandler(pthree, pattern="^" + str(RoutesPowerKeyboard1.pthree) + "$"),
                CallbackQueryHandler(pfour, pattern="^" + str(RoutesPowerKeyboard1.pfour) + "$"),
                CallbackQueryHandler(pfive, pattern="^" + str(RoutesPowerKeyboard1.pfive) + "$"),
                CallbackQueryHandler(psix, pattern="^" + str(RoutesPowerKeyboard1.psix) + "$"),
                CallbackQueryHandler(pseven, pattern="^" + str(RoutesPowerKeyboard1.pseven) + "$"),
                CallbackQueryHandler(peight, pattern="^" + str(RoutesPowerKeyboard1.peight) + "$"),
                CallbackQueryHandler(pnine, pattern="^" + str(RoutesPowerKeyboard1.pnine) + "$"),
                CallbackQueryHandler(pzero, pattern="^" + str(RoutesPowerKeyboard1.pzero) + "$"),
                CallbackQueryHandler(aplay_new_power, pattern="^" + str(Routes.aplay_new_power) + "$"),
                CallbackQueryHandler(start_over, pattern="^" + str(Routes.back) + "$"),
            ],

            StartEndRoutes.power2: [
                CallbackQueryHandler(pone2, pattern="^" + str(RoutesPowerKeyboard2.pone2) + "$"),
                CallbackQueryHandler(ptwo2, pattern="^" + str(RoutesPowerKeyboard2.ptwo2) + "$"),
                CallbackQueryHandler(pthree2, pattern="^" + str(RoutesPowerKeyboard2.pthree2) + "$"),
                CallbackQueryHandler(pfour2, pattern="^" + str(RoutesPowerKeyboard2.pfour2) + "$"),
                CallbackQueryHandler(pfive2, pattern="^" + str(RoutesPowerKeyboard2.pfive2) + "$"),
                CallbackQueryHandler(psix2, pattern="^" + str(RoutesPowerKeyboard2.psix2) + "$"),
                CallbackQueryHandler(pseven2, pattern="^" + str(RoutesPowerKeyboard2.pseven2) + "$"),
                CallbackQueryHandler(peight2, pattern="^" + str(RoutesPowerKeyboard2.peight2) + "$"),
                CallbackQueryHandler(pnine2, pattern="^" + str(RoutesPowerKeyboard2.pnine2) + "$"),
                CallbackQueryHandler(pzero2, pattern="^" + str(RoutesPowerKeyboard2.pzero2) + "$"),
                CallbackQueryHandler(aplay_new_power2, pattern="^" + str(Routes.aplay_new_power2) + "$"),
                CallbackQueryHandler(start_over2, pattern="^" + str(Routes.back2) + "$"),

            ],

            Routes.delete: [
                CallbackQueryHandler(start_over, pattern="^" + str(Routes.back) + "$"),
                # CallbackQueryHandler(start_over2, pattern="^" + str(Routes.back2) + "$"),
            ],

            StartEndRoutes.end_route: [
                CallbackQueryHandler(start_over, pattern="^" + str(Routes.back) + "$"),
                CallbackQueryHandler(start_over2, pattern="^" + str(Routes.back2) + "$"),
            ],
            StartEndRoutes.brand: [
                CallbackQueryHandler(acura, pattern="^" + str(RoutesBrand.acura) + "$"),
                CallbackQueryHandler(daewoo, pattern="^" + str(RoutesBrand.daewoo) + "$"),
                CallbackQueryHandler(datsun, pattern="^" + str(RoutesBrand.datsun) + "$"),
                CallbackQueryHandler(genesis, pattern="^" + str(RoutesBrand.genesis) + "$"),
                CallbackQueryHandler(honda, pattern="^" + str(RoutesBrand.honda) + "$"),
                CallbackQueryHandler(mazda, pattern="^" + str(RoutesBrand.mazda) + "$"),
                CallbackQueryHandler(subaru, pattern="^" + str(RoutesBrand.subaru) + "$"),
                CallbackQueryHandler(toyota, pattern="^" + str(RoutesBrand.toyota) + "$"),
                CallbackQueryHandler(start_over, pattern="^" + str(Routes.back) + "$"),
            ],
            StartEndRoutes.model_acura: [

                CallbackQueryHandler(Acura.MDX, pattern="^" + str(RoutesModel.MDX) + "$"),
                CallbackQueryHandler(Acura.ZDX, pattern="^" + str(RoutesModel.ZDX) + "$"),
                CallbackQueryHandler(Acura.ILX, pattern="^" + str(RoutesModel.ILX) + "$"),
                CallbackQueryHandler(Acura.RDX, pattern="^" + str(RoutesModel.RDX) + "$"),
                CallbackQueryHandler(Acura.TSX, pattern="^" + str(RoutesModel.TSX) + "$"),

                CallbackQueryHandler(start_over, pattern="^" + str(Routes.back) + "$"),

            ],
            StartEndRoutes.model_daewoo: [

                CallbackQueryHandler(Daewoo.nexia, pattern="^" + str(RoutesModel.nexia) + "$"),
                CallbackQueryHandler(Daewoo.matiz, pattern="^" + str(RoutesModel.matiz) + "$"),
                CallbackQueryHandler(Daewoo.gentra, pattern="^" + str(RoutesModel.gentra) + "$"),
                CallbackQueryHandler(Daewoo.lanos, pattern="^" + str(RoutesModel.lanos) + "$"),
                CallbackQueryHandler(Daewoo.winstorm, pattern="^" + str(RoutesModel.winstorm) + "$"),

                CallbackQueryHandler(start_over, pattern="^" + str(Routes.back) + "$"),

            ],
            StartEndRoutes.model_datsun: [

                CallbackQueryHandler(Datsun.mi_do, pattern="^" + str(RoutesModel.mi_do) + "$"),
                CallbackQueryHandler(Datsun.on_do, pattern="^" + str(RoutesModel.on_do) + "$"),

                CallbackQueryHandler(start_over, pattern="^" + str(Routes.back) + "$"),

            ],

            StartEndRoutes.model_genesis: [

                CallbackQueryHandler(Genesis.g70, pattern="^" + str(RoutesModel.g70) + "$"),
                CallbackQueryHandler(Genesis.g80, pattern="^" + str(RoutesModel.g80) + "$"),
                CallbackQueryHandler(Genesis.g90, pattern="^" + str(RoutesModel.g90) + "$"),
                CallbackQueryHandler(Genesis.gv70, pattern="^" + str(RoutesModel.gv70) + "$"),
                CallbackQueryHandler(Genesis.gv80, pattern="^" + str(RoutesModel.gv80) + "$"),

                CallbackQueryHandler(start_over, pattern="^" + str(Routes.back) + "$"),

            ],

            StartEndRoutes.model_honda: [

                CallbackQueryHandler(Honda.fit, pattern="^" + str(RoutesModel.fit) + "$"),
                CallbackQueryHandler(Honda.cr_v, pattern="^" + str(RoutesModel.cr_v) + "$"),
                CallbackQueryHandler(Honda.freed, pattern="^" + str(RoutesModel.freed) + "$"),
                CallbackQueryHandler(Honda.vezel, pattern="^" + str(RoutesModel.vezel) + "$"),
                CallbackQueryHandler(Honda.accord, pattern="^" + str(RoutesModel.accord) + "$"),

                CallbackQueryHandler(start_over, pattern="^" + str(Routes.back) + "$"),

            ],
            StartEndRoutes.model_mazda: [

                CallbackQueryHandler(Mazda.mazda3, pattern="^" + str(RoutesModel.mazda3) + "$"),
                CallbackQueryHandler(Mazda.mazda6, pattern="^" + str(RoutesModel.mazda6) + "$"),
                CallbackQueryHandler(Mazda.cx_5, pattern="^" + str(RoutesModel.cx_5) + "$"),
                CallbackQueryHandler(Mazda.cx_8, pattern="^" + str(RoutesModel.cx_8) + "$"),
                CallbackQueryHandler(Mazda.axela, pattern="^" + str(RoutesModel.axela) + "$"),
                CallbackQueryHandler(Mazda.demio, pattern="^" + str(RoutesModel.demio) + "$"),

                CallbackQueryHandler(start_over, pattern="^" + str(Routes.back) + "$"),

            ],
            StartEndRoutes.model_subaru: [

                CallbackQueryHandler(Subaru.forester, pattern="^" + str(RoutesModel.forester) + "$"),
                CallbackQueryHandler(Subaru.impreza, pattern="^" + str(RoutesModel.impreza) + "$"),
                CallbackQueryHandler(Subaru.legacy, pattern="^" + str(RoutesModel.legacy) + "$"),
                CallbackQueryHandler(Subaru.levorg, pattern="^" + str(RoutesModel.levorg) + "$"),
                CallbackQueryHandler(Subaru.outback, pattern="^" + str(RoutesModel.outback) + "$"),
                CallbackQueryHandler(start_over, pattern="^" + str(Routes.back) + "$"),

            ],

            StartEndRoutes.model_toyota: [

                CallbackQueryHandler(Toyota.camry, pattern="^" + str(RoutesModel.camry) + "$"),
                CallbackQueryHandler(Toyota.corolla, pattern="^" + str(RoutesModel.corolla) + "$"),
                CallbackQueryHandler(Toyota.prado, pattern="^" + str(RoutesModel.prado) + "$"),
                CallbackQueryHandler(Toyota.rav4, pattern="^" + str(RoutesModel.rav4) + "$"),
                CallbackQueryHandler(Toyota.land_cruiser, pattern="^" + str(RoutesModel.land_cruiser) + "$"),
                CallbackQueryHandler(start_over, pattern="^" + str(Routes.back) + "$"),

            ],
            StartEndRoutes.year: [

                CallbackQueryHandler(year_less_3, pattern="^" + str(RoutesYear.year_less_3) + "$"),
                CallbackQueryHandler(year_3_5, pattern="^" + str(RoutesYear.year_3_5) + "$"),
                CallbackQueryHandler(year_5_7, pattern="^" + str(RoutesYear.year_5_7) + "$"),
                CallbackQueryHandler(year_more_7, pattern="^" + str(RoutesYear.year_more_7) + "$"),
                CallbackQueryHandler(start_over, pattern="^" + str(Routes.back) + "$"),

            ],
            StartEndRoutes.engine: [
                CallbackQueryHandler(r_10, pattern="^" + str(RoutesEngine.r_10) + "$"),
                CallbackQueryHandler(r_11, pattern="^" + str(RoutesEngine.r_11) + "$"),

                CallbackQueryHandler(r_12, pattern="^" + str(RoutesEngine.r_12) + "$"),
                CallbackQueryHandler(r_13, pattern="^" + str(RoutesEngine.r_13) + "$"),
                CallbackQueryHandler(r_14, pattern="^" + str(RoutesEngine.r_14) + "$"),
                CallbackQueryHandler(r_15, pattern="^" + str(RoutesEngine.r_15) + "$"),
                CallbackQueryHandler(r_16, pattern="^" + str(RoutesEngine.r_16) + "$"),
                CallbackQueryHandler(r_17, pattern="^" + str(RoutesEngine.r_17) + "$"),
                CallbackQueryHandler(r_18, pattern="^" + str(RoutesEngine.r_18) + "$"),
                CallbackQueryHandler(r_19, pattern="^" + str(RoutesEngine.r_19) + "$"),
                CallbackQueryHandler(r_20, pattern="^" + str(RoutesEngine.r_20) + "$"),
                CallbackQueryHandler(r_21, pattern="^" + str(RoutesEngine.r_21) + "$"),
                CallbackQueryHandler(r_22, pattern="^" + str(RoutesEngine.r_22) + "$"),
                CallbackQueryHandler(r_23, pattern="^" + str(RoutesEngine.r_23) + "$"),
                CallbackQueryHandler(r_24, pattern="^" + str(RoutesEngine.r_24) + "$"),
                CallbackQueryHandler(r_25, pattern="^" + str(RoutesEngine.r_25) + "$"),
                CallbackQueryHandler(r_26, pattern="^" + str(RoutesEngine.r_26) + "$"),
                CallbackQueryHandler(r_27, pattern="^" + str(RoutesEngine.r_27) + "$"),
                CallbackQueryHandler(r_28, pattern="^" + str(RoutesEngine.r_28) + "$"),
                CallbackQueryHandler(r_29, pattern="^" + str(RoutesEngine.r_29) + "$"),
                CallbackQueryHandler(r_30, pattern="^" + str(RoutesEngine.r_30) + "$"),
                CallbackQueryHandler(r_31, pattern="^" + str(RoutesEngine.r_31) + "$"),
                CallbackQueryHandler(r_32, pattern="^" + str(RoutesEngine.r_32) + "$"),
                CallbackQueryHandler(r_33, pattern="^" + str(RoutesEngine.r_33) + "$"),
                CallbackQueryHandler(r_34, pattern="^" + str(RoutesEngine.r_34) + "$"),
                CallbackQueryHandler(r_35, pattern="^" + str(RoutesEngine.r_35) + "$"),
                CallbackQueryHandler(r_36, pattern="^" + str(RoutesEngine.r_36) + "$"),
                CallbackQueryHandler(r_37, pattern="^" + str(RoutesEngine.r_37) + "$"),
                CallbackQueryHandler(r_38, pattern="^" + str(RoutesEngine.r_38) + "$"),
                CallbackQueryHandler(r_39, pattern="^" + str(RoutesEngine.r_39) + "$"),
                CallbackQueryHandler(r_40, pattern="^" + str(RoutesEngine.r_40) + "$"),
                CallbackQueryHandler(r_41, pattern="^" + str(RoutesEngine.r_41) + "$"),
                CallbackQueryHandler(r_42, pattern="^" + str(RoutesEngine.r_42) + "$"),
                CallbackQueryHandler(r_43, pattern="^" + str(RoutesEngine.r_43) + "$"),
                CallbackQueryHandler(r_44, pattern="^" + str(RoutesEngine.r_44) + "$"),
                CallbackQueryHandler(r_45, pattern="^" + str(RoutesEngine.r_45) + "$"),
                CallbackQueryHandler(r_46, pattern="^" + str(RoutesEngine.r_46) + "$"),
                CallbackQueryHandler(r_47, pattern="^" + str(RoutesEngine.r_47) + "$"),
                CallbackQueryHandler(r_48, pattern="^" + str(RoutesEngine.r_48) + "$"),
                CallbackQueryHandler(r_49, pattern="^" + str(RoutesEngine.r_49) + "$"),
                CallbackQueryHandler(r_50, pattern="^" + str(RoutesEngine.r_50) + "$"),
                CallbackQueryHandler(r_51, pattern="^" + str(RoutesEngine.r_51) + "$"),
                CallbackQueryHandler(r_52, pattern="^" + str(RoutesEngine.r_52) + "$"),
                CallbackQueryHandler(r_53, pattern="^" + str(RoutesEngine.r_53) + "$"),
                CallbackQueryHandler(r_54, pattern="^" + str(RoutesEngine.r_54) + "$"),
                CallbackQueryHandler(r_55, pattern="^" + str(RoutesEngine.r_55) + "$"),
                CallbackQueryHandler(r_56, pattern="^" + str(RoutesEngine.r_56) + "$"),
                CallbackQueryHandler(r_57, pattern="^" + str(RoutesEngine.r_57) + "$"),

                CallbackQueryHandler(start_over, pattern="^" + str(Routes.back) + "$"),

            ],
            StartEndRoutes.hand_drive: [

                CallbackQueryHandler(hand_drive_right, pattern="^" + str(RoutesHandDrive.hand_drive_right) + "$"),
                CallbackQueryHandler(hand_drive_left, pattern="^" + str(RoutesHandDrive.hand_drive_left) + "$"),
                CallbackQueryHandler(start_over, pattern="^" + str(Routes.back) + "$"),
            ],

            StartEndRoutes.drive: [

                CallbackQueryHandler(rear, pattern="^" + str(RoutesDrive.rear) + "$"),
                CallbackQueryHandler(front, pattern="^" + str(RoutesDrive.front) + "$"),
                CallbackQueryHandler(drive_four, pattern="^" + str(RoutesDrive.drive_four) + "$"),
                CallbackQueryHandler(connected, pattern="^" + str(RoutesDrive.connected) + "$"),

                CallbackQueryHandler(start_over, pattern="^" + str(Routes.back) + "$"),

            ],
            StartEndRoutes.fuel_type: [

                CallbackQueryHandler(petrol, pattern="^" + str(RoutesFuel.petrol) + "$"),
                CallbackQueryHandler(diesel, pattern="^" + str(RoutesFuel.diesel) + "$"),
                CallbackQueryHandler(hybrid, pattern="^" + str(RoutesFuel.hybrid) + "$"),
                CallbackQueryHandler(electro, pattern="^" + str(RoutesFuel.electro) + "$"),

                CallbackQueryHandler(start_over, pattern="^" + str(Routes.back) + "$"),

            ],

        },
        fallbacks=[CommandHandler("start", start)],
    )

    application.add_handler(conv_handler)
    application.run_polling()


if __name__ == "__main__":
    main()
