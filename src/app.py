from litestar import Litestar, get


@get("/")
async def index() -> str:
    return "Hello, World!"


@get("/greeting")
async def greeting(name: str) -> str:
    return f"Hello, {name.title()}!"


# test comment
app = Litestar([index, greeting])
