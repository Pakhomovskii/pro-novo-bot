from telegram import InlineKeyboardButton
from routes.routes import *


class Keyboard:
    MAIN_KEYBOARD = [
        [
            InlineKeyboardButton("Марка", callback_data=str(Routes.brand)),
            InlineKeyboardButton("Модель", callback_data=str(Routes.model)),
        ],
        [
            InlineKeyboardButton("Авто под ПТС", callback_data=str(Routes.pts)),
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
            InlineKeyboardButton("Мазда", callback_data=str(Routes.back)),
            InlineKeyboardButton("Лада", callback_data=str(Routes.back)),
            InlineKeyboardButton("<---Назад", callback_data=str(Routes.back)),
        ]
    ]

    MODEL_KEYBOARD = [
        [
            InlineKeyboardButton("Калина", callback_data=str(Routes.back)),
            InlineKeyboardButton("Калина2", callback_data=str(Routes.back)),
            InlineKeyboardButton("<---Назад", callback_data=str(Routes.back)),
        ]
    ]

    PTS_KEYBOARD = [
        [
            InlineKeyboardButton("Дa", callback_data=str(Routes.back)),
            InlineKeyboardButton("Нет", callback_data=str(Routes.back)),
            InlineKeyboardButton("<---Назад", callback_data=str(Routes.back)),
        ]
    ]

    BODY_TYPE_KEYBOARD = [
        [
            InlineKeyboardButton("Седан", callback_data=str(Routes.back)),
            InlineKeyboardButton("Хечбек", callback_data=str(Routes.back)),
            InlineKeyboardButton("<---Назад", callback_data=str(Routes.back)),
        ]
    ]

    DRIVE_KEYBOARD = [
        [
            InlineKeyboardButton("Задний", callback_data=str(Routes.back)),
            InlineKeyboardButton("Передний", callback_data=str(Routes.back)),
            InlineKeyboardButton("Полный", callback_data=str(Routes.back)),
            InlineKeyboardButton("<---Назад", callback_data=str(Routes.back)),
        ]
    ]

    ENGINE_CAPACITY_KEYBOARD = [
        [
            InlineKeyboardButton("1", callback_data=str(Routes.back)),
            InlineKeyboardButton("2", callback_data=str(Routes.back)),
            InlineKeyboardButton("3", callback_data=str(Routes.back)),
            InlineKeyboardButton("<---Назад", callback_data=str(Routes.back)),
        ]
    ]

    YEAR_KEYBOARD = [
        [
            InlineKeyboardButton("2000", callback_data=str(Routes.back)),
            InlineKeyboardButton("2002", callback_data=str(Routes.back)),
            InlineKeyboardButton("2003", callback_data=str(Routes.back)),
            InlineKeyboardButton("<---Назад", callback_data=str(Routes.back)),
        ]
    ]

    FUEL_TYPE_KEYBOARD = [
        [
            InlineKeyboardButton("Бензин", callback_data=str(Routes.back)),
            InlineKeyboardButton("Дизель", callback_data=str(Routes.back)),
            InlineKeyboardButton("<---Назад", callback_data=str(Routes.back)),
        ]
    ]

    BUDGET_KEYBOARD = [
        [
            InlineKeyboardButton("1", callback_data=str("1")),
            InlineKeyboardButton("2", callback_data=str("3")),
            InlineKeyboardButton("3", callback_data=str("2")),
            ],
        [
            InlineKeyboardButton("4", callback_data=str("4")),
            InlineKeyboardButton("5", callback_data=str("5")),
            InlineKeyboardButton("6", callback_data=str("6")),
        ],
        [
            InlineKeyboardButton("7", callback_data=str("7")),
            InlineKeyboardButton("8", callback_data=str("8")),
            InlineKeyboardButton("9", callback_data=str("9")),
        ],
        [
            InlineKeyboardButton("0", callback_data=str("0")),
        ],
        [
            InlineKeyboardButton("Применить", callback_data=str(Routes.back)),
        ],

            [
                InlineKeyboardButton("Отмена", callback_data=str(Routes.back)),
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
            InlineKeyboardButton("Обнулить конструктор", callback_data=str(Routes.delete)),
            InlineKeyboardButton("<---Назад", callback_data=str(Routes.back)),
        ]
    ]

    # BUDGET_KEYBOARD_TYPING1 = [
    #     [
    #         InlineKeyboardButton("1", callback_data=str(UserAnswerRoutes2.user_budget_answer2)),
    #         InlineKeyboardButton("2", callback_data=str(UserAnswerRoutes2.user_budget_answer2)),
    #         InlineKeyboardButton("3", callback_data=str(UserAnswerRoutes2.user_budget_answer2)),
    #
    #     ],
        # [
        #     InlineKeyboardButton("4", callback_data=str(UserAnswerRoutes2.user_budget_answer2)),
        #     InlineKeyboardButton("5", callback_data=str(UserAnswerRoutes2.user_budget_answer2)),
        #     InlineKeyboardButton("6", callback_data=str(UserAnswerRoutes2.user_budget_answer2)),
        #
        # ],
        # [
        #     InlineKeyboardButton("7", callback_data=str(UserAnswerRoutes2.user_budget_answer2)),
        #     InlineKeyboardButton("8", callback_data=str(UserAnswerRoutes2.user_budget_answer2)),
        #     InlineKeyboardButton("9", callback_data=str(UserAnswerRoutes2.user_budget_answer2)),
        #
        # ],
        # [
        #     InlineKeyboardButton("0", callback_data=str(UserAnswerRoutes2.user_budget_answer2)),
        # ],

        # [
        #     InlineKeyboardButton("Применить", callback_data=str(Routes.second_back)),
        #     InlineKeyboardButton("<---Назад", callback_data=str(Routes.second_back)),
        # ]
    # ]
    #
    # BUDGET_KEYBOARD_TYPING2 = [
    #     [
    #         InlineKeyboardButton("1", callback_data=str(UserAnswerRoutes1.user_budget_answer1)),
    #         InlineKeyboardButton("2", callback_data=str(UserAnswerRoutes1.user_budget_answer1)),
    #         InlineKeyboardButton("3", callback_data=str(UserAnswerRoutes1.user_budget_answer1)),
    #     ]
        #
        # ],
        # [
        #     InlineKeyboardButton("4", callback_data=str(UserAnswerRoutes1.user_budget_answer1)),
        #     InlineKeyboardButton("5", callback_data=str(UserAnswerRoutes1.user_budget_answer1)),
        #     InlineKeyboardButton("6", callback_data=str(UserAnswerRoutes1.user_budget_answer1)),
        #
        # ],
        # [
        #     InlineKeyboardButton("7", callback_data=str(UserAnswerRoutes1.user_budget_answer1)),
        #     InlineKeyboardButton("8", callback_data=str(UserAnswerRoutes1.user_budget_answer1)),
        #     InlineKeyboardButton("9", callback_data=str(UserAnswerRoutes1.user_budget_answer1)),
        #
        # ],
        # [
        #     InlineKeyboardButton("0", callback_data=str(UserAnswerRoutes1.user_budget_answer1)),
        # ],

        # [
        #     InlineKeyboardButton("Применить", callback_data=str(Routes.third_back)),
        #     InlineKeyboardButton("<---Назад", callback_data=str(Routes.third_back)),
        # ]


