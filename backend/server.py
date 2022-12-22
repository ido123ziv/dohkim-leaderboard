from blacksheep import Application
from db_handler import get_data, update_data
app = Application()
get = app.router.get
post = app.router.post


@get("/")
def home(request):
    return get_data()
    # return "GET Example"


@post("/")
def post_example(request):
    return "POST Example"
