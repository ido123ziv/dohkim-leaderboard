from blacksheep import Application, FromText

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
    update_data()
    return "POST Example"


@post("/winners")
async def post_win(req: FromText):
    val = req.value
    update_data(val)
    return "POST Example"
