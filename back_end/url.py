from back_end.views.home_route.views import *
from core.utils import Route, Handler
from back_end.views.register_route.form import Regesiter,logout
from back_end.views.about_route.views import about
routes = [
    Route("/", endpoint=None, view_func=home),
    Route("/get_items/<cat_id>", endpoint=None, view_func=get_items),
    Route("/reg", endpoint=None, view_func=Regesiter,methods=['GET','POST']),
    Route("/logout", endpoint=None, view_func=logout,methods=['GET']),
    Route("/about", endpoint=None, view_func=about,methods=['GET','POST'])

]
