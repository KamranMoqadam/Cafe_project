from back_end.views.home_route.views import *
from core.utils import Route, Handler
from back_end.views.register_route.form import Regesiter, logout
from back_end.views.shop_card_route.shop_card import shop_card
from back_end.views.checkout_route.checkout import checkout
from back_end.views.my_orders_route.my_orders import my_orders

from back_end.views.about_route.views import about
routes = [
    Route("/", endpoint=None, view_func=home),
    Route("/get_items/<cat_id>", endpoint=None, view_func=get_items),
    Route("/reg", endpoint=None, view_func=Regesiter, methods=['GET', 'POST']),
    Route("/logout", endpoint=None, view_func=logout, methods=['GET']),
    Route("/shop_card", endpoint=None, view_func=shop_card, methods=['POST']),
    Route("/check_out", endpoint=None, view_func=checkout, methods=['POST']),
    Route("/my_orders/<user_id>", endpoint=None, view_func=my_orders, methods=['GET']),
    Route("/about", endpoint=None, view_func=about,methods=['GET','POST'])

]
