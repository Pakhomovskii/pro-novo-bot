class StartEndRoutes:
    (end_route,
     start_route,
     brand,
     hand_drive,

     year,
     model,
     model_acura,
     model_mazda,
     model_subaru,
     model_daewoo,
     model_datsun,
     power,
     power2,
     engine,
     drive,
     budget,
     budget2,
     fuel_type,
     tax) \
     = range(19)


# class StartSpecialRoutes:
#  (power,
#  power2) \
#          = range(2)


class Routes:
 (brand,
  model,
  hand_drive,
  power,
  power2,
  drive,
  year,
  engine,
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
  aplay_new_power,
  aplay_new_power2
  ) \
  = range(23)


class RoutesBrand:
 (acura,
  daewoo,
  subaru,
  mazda,
  datsun
  ) \
  = range(5)


class RoutesModel:
 (impreza,
  cx_8,
  MDX,
  ZDX,
  ILX,
  RDX,
  TSX,
  nexia,
  matiz,
  gentra,
  lanos,
  winstorm,
  mi_do,
  on_do

  ) \
  = range(14)


class RoutesYear:
 (year_less_3,
  year_3_5,
  year_5_7,
  year_more_7) \
  = range(4)


class RoutesDrive:
 (rear,
  front,
  drive_four,
  connected) \
  = range(4)


class RoutesPower:
 (v_50_100,
  v_101_150,
  v_151_200,
  v_201_250,
  v_251_300,
  v_301_350,
  v_351_400) \
  = range(7)


class RoutesFuel:
 (petrol,
  diesel,
  hybrid,
  electro,) \
  = range(4)


class RoutesEngine:
 (r_10,
  r_11,
  r_12,
  r_13,
  r_14,
  r_15,
  r_16,
  r_17,
  r_18,
  r_19,
  r_20,
  r_21,
  r_22,
  r_23,
  r_24,
  r_25,
  r_26,
  r_27,
  r_28,
  r_29,
  r_30,
  r_31,
  r_32,
  r_33,
  r_34,
  r_35,
  r_36,
  r_37,
  r_38,
  r_39,
  r_40,
  r_41,
  r_42,
  r_43,
  r_44,
  r_45,
  r_46,
  r_47,
  r_48,
  r_49,
  r_50,
  r_51,
  r_52,
  r_53,
  r_54,
  r_55,
  r_56,
  r_57
  ) \
  = range(48)


class RoutesHandDrive:
 (hand_drive_right,
  hand_drive_left) \
  = range(2)


# class RoutesBudget:
#     (keyboard1,
#      keyboard2
#      ) \
#         = range(2)


class RoutesBudgetKeyboard1:
 (one, two, three, four, five, six, seven, eight, nine, zero) = range(10)


class RoutesBudgetKeyboard2:
 (one2, two2, three2, four2, five2, six2, seven2, eight2, nine2, zero2) = range(10)


class RoutesPowerKeyboard1:
 (pone, ptwo, pthree, pfour, pfive, psix, pseven, peight, pnine, pzero) = range(10)


class RoutesPowerKeyboard2:
 (pone2, ptwo2, pthree2, pfour2, pfive2, psix2, pseven2, peight2, pnine2, pzero2) = range(10)

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
