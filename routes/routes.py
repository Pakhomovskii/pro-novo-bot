class StartEndRoutes:
    (end_route,
     start_route,
     brand,
     model,
     model_mazda,
     model_subaru,
     budget,
     budget2) \
        = range(8)


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
     budget2,
     send,
     tax,
     delete,
     back,
     back2,
     start_over,
     start_over2,
     update_user_order,
     aplay_new_budget,
     aplay_new_budget2
     ) \
        = range(20)


class RoutesBrand:
    (subaru,
     mazda
     ) \
        = range(2)


class RoutesModel:
    (impreza,
     cx_8,
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
