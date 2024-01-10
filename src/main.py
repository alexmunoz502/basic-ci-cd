import uvicorn
from litestar import Litestar, get


@get("/")
async def index() -> str:
    return "Hello, World!"


@get("/greeting")
async def greeting(name: str) -> str:
    return f"Hello, {name.title()}!"


app = Litestar([index, greeting])


if __name__ == "__main__":
    uvicorn.run(app="main:app", host="0.0.0.0", port=80)
