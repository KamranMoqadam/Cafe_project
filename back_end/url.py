from back_end.views.home_route.views import *
from core.utils import Route, Handler

routes = [
    Route("/", endpoint=None, view_func=home),
    Route("/get_items/<cat_id>", endpoint=None, view_func=get_items),

]
