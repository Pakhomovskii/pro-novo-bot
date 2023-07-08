from telegram import InlineKeyboardButton

from routes.routes import *


class Keyboard:
    MAIN_KEYBOARD = [
        [
            InlineKeyboardButton("Марка", callback_data=str(Routes.brand)),
            InlineKeyboardButton("Модель", callback_data=str(Routes.model)),
        ],
        [
            InlineKeyboardButton("Руль", callback_data=str(Routes.hand_drive)),
            InlineKeyboardButton("Мощность ДВС", callback_data=str(Routes.power)),
        ],
        [
            InlineKeyboardButton("Привод", callback_data=str(Routes.drive)),
            InlineKeyboardButton("Объем ДВС", callback_data=str(Routes.engine)),
        ],
        [
            InlineKeyboardButton("Возраст Авто", callback_data=str(Routes.year)),
            InlineKeyboardButton("Тип топлива", callback_data=str(Routes.fuel_type)),
        ],
        [InlineKeyboardButton("Бюджет", callback_data=str(Routes.budget)),

         InlineKeyboardButton("Обнулить анкету", callback_data=str(Routes.delete))
         ],

        [
            InlineKeyboardButton("Отправить авто нам для подбора", callback_data=str(Routes.send)), ],
        [InlineKeyboardButton("Расчет всех платежей", callback_data=str(Routes.tax)),
         ],
    ]

    BRAND_KEYBOARD = [
        [
            InlineKeyboardButton("Acura", callback_data=str(RoutesBrand.acura)),
            InlineKeyboardButton("Mazda", callback_data=str(RoutesBrand.mazda)),
            InlineKeyboardButton("Subaru", callback_data=str(RoutesBrand.subaru)),
            InlineKeyboardButton("<---Назад", callback_data=str(Routes.back)),
        ]
    ]

    MODEL_KEYBOARD_ACURA = [
        [InlineKeyboardButton("MDX", callback_data=str(RoutesModel.MDX)), ],
        [InlineKeyboardButton("RDX", callback_data=str(RoutesModel.RDX)), ],
        [InlineKeyboardButton("TSX", callback_data=str(RoutesModel.TSX)), ],
        [InlineKeyboardButton("ZDX", callback_data=str(RoutesModel.ZDX)), ],
        [InlineKeyboardButton("ILX", callback_data=str(RoutesModel.ILX)), ],
        [InlineKeyboardButton("<---Назад", callback_data=str(Routes.back)), ]
    ]

    MODEL_KEYBOARD_MAZDA = [
        [
            InlineKeyboardButton("CX-8", callback_data=str(RoutesModel.cx_8)),
            InlineKeyboardButton("<---Назад", callback_data=str(Routes.back)),
        ]
    ]

    MODEL_KEYBOARD_SUBARU = [
        [
            InlineKeyboardButton("Impreza", callback_data=str(RoutesModel.impreza)),
            InlineKeyboardButton("<---Назад", callback_data=str(Routes.back)),
        ]
    ]

    YEAR_KEYBOARD = [
        [
            InlineKeyboardButton("меньше 3-х лет", callback_data=str(RoutesYear.year_less_3)), ],
        [
            InlineKeyboardButton("3-5 лет", callback_data=str(RoutesYear.year_3_5)), ],
        [
            InlineKeyboardButton("5-7 лет", callback_data=str(RoutesYear.year_5_7)), ],
        [
            InlineKeyboardButton("больше 7 лет", callback_data=str(RoutesYear.year_more_7)), ],
        [
            InlineKeyboardButton("<---Назад", callback_data=str(Routes.back)),
        ]
    ]

    ENGINE_KEYBOARD = [

        [
            InlineKeyboardButton("1.0", callback_data=str(RoutesEngine.r_10)),
            InlineKeyboardButton("1.1", callback_data=str(RoutesEngine.r_11)),
            InlineKeyboardButton("1.2", callback_data=str(RoutesEngine.r_12)),
            InlineKeyboardButton("1.3", callback_data=str(RoutesEngine.r_13)),
            InlineKeyboardButton("1.4", callback_data=str(RoutesEngine.r_14)),
            InlineKeyboardButton("1.5", callback_data=str(RoutesEngine.r_15)),
            InlineKeyboardButton("1.6", callback_data=str(RoutesEngine.r_16)),
            InlineKeyboardButton("1.7", callback_data=str(RoutesEngine.r_17)),
            InlineKeyboardButton("1.8", callback_data=str(RoutesEngine.r_18)),
            InlineKeyboardButton("1.9", callback_data=str(RoutesEngine.r_19)),
        ],
        [
            InlineKeyboardButton("2.0", callback_data=str(RoutesEngine.r_20)),
            InlineKeyboardButton("2.1", callback_data=str(RoutesEngine.r_21)),
            InlineKeyboardButton("2.2", callback_data=str(RoutesEngine.r_22)),
            InlineKeyboardButton("2.3", callback_data=str(RoutesEngine.r_23)),
            InlineKeyboardButton("2.4", callback_data=str(RoutesEngine.r_24)),
            InlineKeyboardButton("2.5", callback_data=str(RoutesEngine.r_25)),
            InlineKeyboardButton("2.6", callback_data=str(RoutesEngine.r_26)),
            InlineKeyboardButton("2.7", callback_data=str(RoutesEngine.r_27)),
            InlineKeyboardButton("2.8", callback_data=str(RoutesEngine.r_28)),
            InlineKeyboardButton("2.9", callback_data=str(RoutesEngine.r_29)),
        ],
        [
            InlineKeyboardButton("3.0", callback_data=str(RoutesEngine.r_30)),
            InlineKeyboardButton("3.1", callback_data=str(RoutesEngine.r_31)),
            InlineKeyboardButton("3.2", callback_data=str(RoutesEngine.r_32)),
            InlineKeyboardButton("3.3", callback_data=str(RoutesEngine.r_33)),
            InlineKeyboardButton("3.4", callback_data=str(RoutesEngine.r_34)),
            InlineKeyboardButton("3.5", callback_data=str(RoutesEngine.r_35)),
            InlineKeyboardButton("3.6", callback_data=str(RoutesEngine.r_36)),
            InlineKeyboardButton("3.7", callback_data=str(RoutesEngine.r_37)),
            InlineKeyboardButton("3.8", callback_data=str(RoutesEngine.r_38)),
            InlineKeyboardButton("3.9", callback_data=str(RoutesEngine.r_39)),
        ],
        [
            InlineKeyboardButton("4.0", callback_data=str(RoutesEngine.r_40)),
            InlineKeyboardButton("4.1", callback_data=str(RoutesEngine.r_41)),
            InlineKeyboardButton("4.2", callback_data=str(RoutesEngine.r_42)),
            InlineKeyboardButton("4.3", callback_data=str(RoutesEngine.r_43)),
            InlineKeyboardButton("4.4", callback_data=str(RoutesEngine.r_44)),
            InlineKeyboardButton("4.5", callback_data=str(RoutesEngine.r_45)),
            InlineKeyboardButton("4.6", callback_data=str(RoutesEngine.r_46)),
            InlineKeyboardButton("4.7", callback_data=str(RoutesEngine.r_47)),
            InlineKeyboardButton("4.8", callback_data=str(RoutesEngine.r_48)),
            InlineKeyboardButton("4.9", callback_data=str(RoutesEngine.r_49)),
        ],
        [
            InlineKeyboardButton("5.0", callback_data=str(RoutesEngine.r_50)),
            InlineKeyboardButton("5.1", callback_data=str(RoutesEngine.r_51)),
            InlineKeyboardButton("5.2", callback_data=str(RoutesEngine.r_52)),
            InlineKeyboardButton("5.3", callback_data=str(RoutesEngine.r_53)),
            InlineKeyboardButton("5.4", callback_data=str(RoutesEngine.r_54)),
            InlineKeyboardButton("5.5", callback_data=str(RoutesEngine.r_55)),
            InlineKeyboardButton("5.6", callback_data=str(RoutesEngine.r_56)),
            InlineKeyboardButton("5.7", callback_data=str(RoutesEngine.r_57)),

        ],
        [
            InlineKeyboardButton("<---Назад", callback_data=str(Routes.back)),
        ]
    ]

    HAND_DRIVE_KEYBOARD = [
        [
            InlineKeyboardButton("Правый", callback_data=str(RoutesHandDrive.hand_drive_right)), ],
        [InlineKeyboardButton("Левый", callback_data=str(RoutesHandDrive.hand_drive_left)), ],
        [InlineKeyboardButton("<---Назад", callback_data=str(Routes.back)),
         ]
    ]

    DRIVE_KEYBOARD = [

        [InlineKeyboardButton("Задний", callback_data=str(RoutesDrive.rear)), ],
        [InlineKeyboardButton("Передний", callback_data=str(RoutesDrive.front)), ],
        [InlineKeyboardButton("Полный", callback_data=str(RoutesDrive.drive_four)), ],
        [InlineKeyboardButton("Подключаемый", callback_data=str(RoutesDrive.connected)), ],
        [InlineKeyboardButton("<---Назад", callback_data=str(Routes.back)), ]

    ]

    FUEL_KEYBOARD = [

        [InlineKeyboardButton("Бензин", callback_data=str(RoutesFuel.petrol)), ],
        [InlineKeyboardButton("Дизель", callback_data=str(RoutesFuel.diesel)), ],
        [InlineKeyboardButton("Гибрид", callback_data=str(RoutesFuel.hybrid)), ],
        [InlineKeyboardButton("Электро", callback_data=str(RoutesFuel.electro)), ],
        [InlineKeyboardButton("<---Назад", callback_data=str(Routes.back)), ],

    ]

    BUDGET_KEYBOARD2 = [
        [
            InlineKeyboardButton("1", callback_data=str(RoutesBudgetKeyboard1.one)),
            InlineKeyboardButton("2", callback_data=str(RoutesBudgetKeyboard1.two)),
            InlineKeyboardButton("3", callback_data=str(RoutesBudgetKeyboard1.three)),
        ],
        [
            InlineKeyboardButton("4", callback_data=str(RoutesBudgetKeyboard1.four)),
            InlineKeyboardButton("5", callback_data=str(RoutesBudgetKeyboard1.five)),
            InlineKeyboardButton("6", callback_data=str(RoutesBudgetKeyboard1.six)),
        ],
        [
            InlineKeyboardButton("7", callback_data=str(RoutesBudgetKeyboard1.seven)),
            InlineKeyboardButton("8", callback_data=str(RoutesBudgetKeyboard1.eight)),
            InlineKeyboardButton("9", callback_data=str(RoutesBudgetKeyboard1.nine)),
        ],
        [
            InlineKeyboardButton("0", callback_data=str(RoutesBudgetKeyboard1.zero)),
        ],
        [
            InlineKeyboardButton("Применить", callback_data=str(Routes.aplay_new_budget)),
        ],

        [
            InlineKeyboardButton("Отмена", callback_data=str(Routes.back)),
        ]
    ]

    BUDGET_KEYBOARD = [
        [
            InlineKeyboardButton("1", callback_data=str(RoutesBudgetKeyboard2.one2)),
            InlineKeyboardButton("2", callback_data=str(RoutesBudgetKeyboard2.two2)),
            InlineKeyboardButton("3", callback_data=str(RoutesBudgetKeyboard2.three2)),
        ],
        [
            InlineKeyboardButton("4", callback_data=str(RoutesBudgetKeyboard2.four2)),
            InlineKeyboardButton("5", callback_data=str(RoutesBudgetKeyboard2.five2)),
            InlineKeyboardButton("6", callback_data=str(RoutesBudgetKeyboard2.six2)),
        ],
        [
            InlineKeyboardButton("7", callback_data=str(RoutesBudgetKeyboard2.seven2)),
            InlineKeyboardButton("8", callback_data=str(RoutesBudgetKeyboard2.eight2)),
            InlineKeyboardButton("9", callback_data=str(RoutesBudgetKeyboard2.nine2)),
        ],
        [
            InlineKeyboardButton("0", callback_data=str(RoutesBudgetKeyboard2.zero2)),
        ],
        [
            InlineKeyboardButton("Применить", callback_data=str(Routes.aplay_new_budget2)),
        ],

        [
            InlineKeyboardButton("Отмена", callback_data=str(Routes.back2)),
        ]
    ]

    POWER_POWER_KEYBOARD2 = [
        [
            InlineKeyboardButton("1", callback_data=str(RoutesPowerKeyboard1.pone)),
            InlineKeyboardButton("2", callback_data=str(RoutesPowerKeyboard1.ptwo)),
            InlineKeyboardButton("3", callback_data=str(RoutesPowerKeyboard1.pthree)),
        ],
        [
            InlineKeyboardButton("4", callback_data=str(RoutesPowerKeyboard1.pfour)),
            InlineKeyboardButton("5", callback_data=str(RoutesPowerKeyboard1.pfive)),
            InlineKeyboardButton("6", callback_data=str(RoutesPowerKeyboard1.psix)),
        ],
        [
            InlineKeyboardButton("7", callback_data=str(RoutesPowerKeyboard1.pseven)),
            InlineKeyboardButton("8", callback_data=str(RoutesPowerKeyboard1.peight)),
            InlineKeyboardButton("9", callback_data=str(RoutesPowerKeyboard1.pnine)),
        ],
        [
            InlineKeyboardButton("0", callback_data=str(RoutesPowerKeyboard1.pzero)),
        ],
        [
            InlineKeyboardButton("Применить", callback_data=str(Routes.aplay_new_power)),
        ],

        [
            InlineKeyboardButton("Отмена", callback_data=str(Routes.back)),
        ]
    ]

    POWER_POWER_KEYBOARD = [
        [
            InlineKeyboardButton("1", callback_data=str(RoutesPowerKeyboard2.pone2)),
            InlineKeyboardButton("2", callback_data=str(RoutesPowerKeyboard2.ptwo2)),
            InlineKeyboardButton("3", callback_data=str(RoutesPowerKeyboard2.pthree2)),
        ],
        [
            InlineKeyboardButton("4", callback_data=str(RoutesPowerKeyboard2.pfour2)),
            InlineKeyboardButton("5", callback_data=str(RoutesPowerKeyboard2.pfive2)),
            InlineKeyboardButton("6", callback_data=str(RoutesPowerKeyboard2.psix2)),
        ],
        [
            InlineKeyboardButton("7", callback_data=str(RoutesPowerKeyboard2.pseven2)),
            InlineKeyboardButton("8", callback_data=str(RoutesPowerKeyboard2.peight2)),
            InlineKeyboardButton("9", callback_data=str(RoutesPowerKeyboard2.pnine2)),
        ],
        [
            InlineKeyboardButton("0", callback_data=str(RoutesPowerKeyboard2.pzero2)),
        ],
        [
            InlineKeyboardButton("Применить", callback_data=str(Routes.aplay_new_power2)),
        ],

        [
            InlineKeyboardButton("Отмена", callback_data=str(Routes.back2)),
        ]
    ]

    SEND = [
        [
            InlineKeyboardButton("<---Назад", callback_data=str(Routes.back)),
        ]
    ]

    TAX = [
        [
            InlineKeyboardButton("<---Назад", callback_data=str(Routes.back)),
        ]
    ]

    DELETE = [
        [
            InlineKeyboardButton("<---Назад", callback_data=str(Routes.back)),
        ]
    ]
