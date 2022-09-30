import views
from core.utils import Route, Handler

routes = [
    Route("/", endpoint=None, view_func=views.home),
    Route("/register", endpoint=None, view_func=views.reg, methods=['POST', 'GET']),
    Route("/login", endpoint=None, view_func=views.login, methods=['POST', 'GET']),
    Route("/master", endpoint=None, view_func=views.master_page, methods=['GET']),
    Route("/sin/<name>", endpoint=None, view_func=views.sin, methods=['GET']),
    Route("/edit_create_questions/<exam_id>", endpoint=None, view_func=views.sin, methods=['GET', 'POST']),
    Route("/add_exam", endpoint=None, view_func=views.create_exam, methods=['GET', 'POST']),
    Route("/test", endpoint=None, view_func=views.home1, methods=['GET', 'POST']),

    Handler(404, views.not_found)
]
