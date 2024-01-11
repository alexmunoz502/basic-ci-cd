import uvicorn
import os
from litestar import Litestar, get


@get("/")
async def index() -> str:
    return "Hello, World!"


@get("/greeting")
async def greeting(name: str = "world") -> str:
    return f"Hello, {name.title()}!"


@get("/farewell")
async def farewell(name: str = "world") -> str:
    return f"Goodbye, {name}!"


app = Litestar([index, greeting])


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
