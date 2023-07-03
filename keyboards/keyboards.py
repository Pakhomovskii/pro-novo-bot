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
            InlineKeyboardButton("Тип кузова", callback_data=str(Routes.body_type)),
        ],
        [
            InlineKeyboardButton("Привод", callback_data=str(Routes.drive)),
            InlineKeyboardButton("Объем двигателя", callback_data=str(Routes.engine_capacity)),
        ],
        [
            InlineKeyboardButton("Год", callback_data=str(Routes.year)),
            InlineKeyboardButton("Тип топлива", callback_data=str(Routes.fuel_type)),
        ],
        [InlineKeyboardButton("Бюджет", callback_data=str(Routes.budget))],

        [InlineKeyboardButton("Обнулить конструктор", callback_data=str(Routes.delete))
         ],

        [
            InlineKeyboardButton("Отправить авто для подбора", callback_data=str(Routes.send)),
            InlineKeyboardButton("Расчет полной стоимости", callback_data=str(Routes.tax)),
        ],
    ]

    BRAND_KEYBOARD = [
        [
            InlineKeyboardButton("Мазда", callback_data=str(RoutesBrand.mazda)),
            InlineKeyboardButton("Субару", callback_data=str(RoutesBrand.subaru)),
            InlineKeyboardButton("<---Назад", callback_data=str(Routes.back)),
        ]
    ]

    MODEL_KEYBOARD_MAZDA = [
        [
            InlineKeyboardButton("CX-8", callback_data=str(RoutesModel.cx_8)),
            InlineKeyboardButton("<---Назад", callback_data=str(Routes.back)),
        ]
    ]

    MODEL_KEYBOARD_SUBARU = [
        [
            InlineKeyboardButton("Импреза", callback_data=str(RoutesModel.impreza)),
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

    HAND_DRIVE_KEYBOARD = [
        [
            InlineKeyboardButton("Правый", callback_data=str(RoutesHandDrive.hand_drive_right)), ],
        [InlineKeyboardButton("Левый", callback_data=str(RoutesHandDrive.hand_drive_left)), ],
        [InlineKeyboardButton("<---Назад", callback_data=str(Routes.back)),
         ]
    ]

    BODY_TYPE_KEYBOARD = [
        [
            # InlineKeyboardButton("Седан", callback_data=str(Routes.back)),
            # InlineKeyboardButton("Хечбек", callback_data=str(Routes.back)),
            # InlineKeyboardButton("<---Назад", callback_data=str(Routes.back)),
        ]
    ]

    DRIVE_KEYBOARD = [
        [
            # InlineKeyboardButton("Задний", callback_data=str(Routes.back)),
            # InlineKeyboardButton("Передний", callback_data=str(Routes.back)),
            # InlineKeyboardButton("Полный", callback_data=str(Routes.back)),
            # InlineKeyboardButton("<---Назад", callback_data=str(Routes.back)),
        ]
    ]

    ENGINE_CAPACITY_KEYBOARD = [
        [
            InlineKeyboardButton("1.0", callback_data=str(RoutesEngineCapacity._10)),
            InlineKeyboardButton("1.1", callback_data=str(RoutesEngineCapacity._11)),
            InlineKeyboardButton("1.2", callback_data=str(RoutesEngineCapacity._12)),
            InlineKeyboardButton("1.3", callback_data=str(RoutesEngineCapacity._13)),
            InlineKeyboardButton("1.4", callback_data=str(RoutesEngineCapacity._14)),
            InlineKeyboardButton("1.5", callback_data=str(RoutesEngineCapacity._15)),
            InlineKeyboardButton("1.6", callback_data=str(RoutesEngineCapacity._16)),
            InlineKeyboardButton("1.7", callback_data=str(RoutesEngineCapacity._17)),
            InlineKeyboardButton("1.8", callback_data=str(RoutesEngineCapacity._18)),
            InlineKeyboardButton("1.9", callback_data=str(RoutesEngineCapacity._19)),
        ],
        [
            InlineKeyboardButton("2.0", callback_data=str(RoutesEngineCapacity._20)),
            InlineKeyboardButton("2.1", callback_data=str(RoutesEngineCapacity._21)),
            InlineKeyboardButton("2.2", callback_data=str(RoutesEngineCapacity._22)),
            InlineKeyboardButton("2.3", callback_data=str(RoutesEngineCapacity._23)),
            InlineKeyboardButton("2.4", callback_data=str(RoutesEngineCapacity._24)),
            InlineKeyboardButton("2.5", callback_data=str(RoutesEngineCapacity._25)),
            InlineKeyboardButton("2.6", callback_data=str(RoutesEngineCapacity._26)),
            InlineKeyboardButton("2.7", callback_data=str(RoutesEngineCapacity._27)),
            InlineKeyboardButton("2.8", callback_data=str(RoutesEngineCapacity._28)),
            InlineKeyboardButton("2.9", callback_data=str(RoutesEngineCapacity._29)),
        ],
        [
            InlineKeyboardButton("3.0", callback_data=str(RoutesEngineCapacity._30)),
            InlineKeyboardButton("3.1", callback_data=str(RoutesEngineCapacity._31)),
            InlineKeyboardButton("3.2", callback_data=str(RoutesEngineCapacity._32)),
            InlineKeyboardButton("3.3", callback_data=str(RoutesEngineCapacity._33)),
            InlineKeyboardButton("3.4", callback_data=str(RoutesEngineCapacity._34)),
            InlineKeyboardButton("3.5", callback_data=str(RoutesEngineCapacity._35)),
            InlineKeyboardButton("3.6", callback_data=str(RoutesEngineCapacity._36)),
            InlineKeyboardButton("3.7", callback_data=str(RoutesEngineCapacity._37)),
            InlineKeyboardButton("3.8", callback_data=str(RoutesEngineCapacity._38)),
            InlineKeyboardButton("3.9", callback_data=str(RoutesEngineCapacity._39)),
        ],
        [
            InlineKeyboardButton("4.0", callback_data=str(RoutesEngineCapacity._40)),
            InlineKeyboardButton("4.1", callback_data=str(RoutesEngineCapacity._41)),
            InlineKeyboardButton("4.2", callback_data=str(RoutesEngineCapacity._42)),
            InlineKeyboardButton("4.3", callback_data=str(RoutesEngineCapacity._43)),
            InlineKeyboardButton("4.4", callback_data=str(RoutesEngineCapacity._44)),
            InlineKeyboardButton("4.5", callback_data=str(RoutesEngineCapacity._45)),
            InlineKeyboardButton("4.6", callback_data=str(RoutesEngineCapacity._46)),
            InlineKeyboardButton("4.7", callback_data=str(RoutesEngineCapacity._47)),
            InlineKeyboardButton("4.8", callback_data=str(RoutesEngineCapacity._48)),
            InlineKeyboardButton("4.9", callback_data=str(RoutesEngineCapacity._49)),
        ],
        [
            InlineKeyboardButton("5.0", callback_data=str(RoutesEngineCapacity._50)),
            InlineKeyboardButton("5.1", callback_data=str(RoutesEngineCapacity._51)),
            InlineKeyboardButton("5.2", callback_data=str(RoutesEngineCapacity._52)),
            InlineKeyboardButton("5.3", callback_data=str(RoutesEngineCapacity._53)),
            InlineKeyboardButton("5.4", callback_data=str(RoutesEngineCapacity._54)),
            InlineKeyboardButton("5.5", callback_data=str(RoutesEngineCapacity._55)),
            InlineKeyboardButton("5.6", callback_data=str(RoutesEngineCapacity._56)),
            InlineKeyboardButton("5.7", callback_data=str(RoutesEngineCapacity._57)),
            InlineKeyboardButton("5.8", callback_data=str(RoutesEngineCapacity._58)),
            InlineKeyboardButton("5.9", callback_data=str(RoutesEngineCapacity._59)),
        ],

        [
            InlineKeyboardButton("Отмена", callback_data=str(Routes.back)),
        ]
    ]

    FUEL_TYPE_KEYBOARD = [
        [
            # InlineKeyboardButton("Бензин", callback_data=str(Routes.back)),
            # InlineKeyboardButton("Дизель", callback_data=str(Routes.back)),
            # InlineKeyboardButton("<---Назад", callback_data=str(Routes.back)),
        ]
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

    SEND = [
        [
            InlineKeyboardButton("<---Назад", callback_data=str(Routes.back)),
        ]
    ]

    TAX = [
        [
            # InlineKeyboardButton("<---Назад", callback_data=str(Routes.back)),
        ]
    ]

    DELETE = [
        [
            # InlineKeyboardButton("Обнулить конструктор", callback_data=str(Routes.delete)),
            # InlineKeyboardButton("<---Назад", callback_data=str(Routes.back)),
        ]
    ]
