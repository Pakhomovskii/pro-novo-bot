class StartEndRoutes:
    (end_route,
     start_route,
     brand,
     hand_drive,
     year,
     model,
     model_mazda,
     model_subaru,
     engine_capacity,
     budget,
     budget2) \
     = range(11)



class Routes:
    (brand,
     model,
     hand_drive,
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
     aplay_new_budget2,
     aplay_new_year2,
     aplay_new_year
     ) \
     = range(22)


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


class RoutesYear:
 (year_less_3,
  year_3_5,
  year_5_7,
  year_more_7) \
  = range(4)


class RoutesHandDrive:
 (hand_drive_right,
  hand_drive_left) \
  = range(2)


class RoutesBudget:
 (keyboard1,
  keyboard3
  ) \
  = range(2)


class RoutesEngineCapacity:
 (_10,
  _11,
  _12,
  _13,
  _14,
  _15,
  _16,
  _17,
  _18,
  _19,
  _20,
  _21,
  _22,
  _23,
  _24,
  _25,
  _26,
  _27,
  _28,
  _29,
  _30,
  _31,
  _32,
  _33,
  _34,
  _35,
  _36,
  _37,
  _38,
  _39,
  _40,
  _41,
  _42,
  _43,
  _44,
  _45,
  _46,
  _47,
  _48,
  _49,
  _50,
  _51,
  _52,
  _53,
  _54,
  _55,
  _56,
  _57,
  _58,
  _59,
  ) \
  = range(50)


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
