class StartEndRoutes:
    (end_route,
     start_route) \
        = range(2)


class UserAnswerRoutes:
    user_budget_answer \
        = range(1)


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
     back) \
        = range(13)

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
