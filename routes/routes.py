class StartEndRoutes:
    (end_route,
     start_route,
     brand,
     model) \
        = range(4)


#
# class UserAnswerRoutes1:
#     user_budget_answer1 \
#         = range(1)
#
#
# class UserAnswerRoutes2:
#     user_budget_answer2 \
#         = range(1)
#
#
# class AnswerRoutes1:
#     (second_back,
#      first_keyboard,
#      aplay_answer) = range(3)
#
#
# class AnswerRoutes2:
#     (third_back,
#      second_keyboard,
#      aplay_answer2) = range(3)
#

class Routes:
    (brand,
     model,
     pts,
     body_type,
     drive,
     engine_capacity,
     year,
     fuel_type,
     budget,
     send,
     tax,
     delete,
     back,
     back2,
     start_over,
     update_user_order,
     ) \
        = range(16)


class RoutesBrand:
    (subaru,
     mazda
     ) \
        = range(2)


class RoutesModel:
    (kalina,
     granta,
     ) \
        = range(2)


class RoutesBudget:
    (keyboard1,
     keyboard3
     ) \
        = range(2)


class RoutesBudgetKeyboard1:
    (one, two, three, four, five, six, seven, eight, nine, zero) = range(10)


class RoutesBudgetKeyboard2:
    (one2, two2, three2, four2, five2, six2, seven2, eight2, nine2, zero2) = range(10)

# TODO Think about Enum in this case
# from enum import Enum
#
#
# class StartEndRoutes(Enum):
#     end_route = None
#     start_route = None
#
#
# class Routes(Enum):
#     brand = None
#     model = None
#     pts = None
#     body_type = None
#     drive = None
#     engine_capacity = None
#     year = None
#     fuel_type = None
#     budget = None
#     send = None
#     tax = None
#     back = None
#
# from enum import Enum
#
