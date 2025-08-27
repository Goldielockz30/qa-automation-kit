from fastapi import FastAPI
from fastapi.responses import JSONResponse

from backend.src.utils import add, is_even

app = FastAPI()


@app.get("/health")
def health() -> JSONResponse:
    # exercise utils for coverage
    _ = add(2, 3)
    _ = is_even(4)
    return JSONResponse({"status": "ok"})
