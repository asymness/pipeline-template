#####################################################################
# THIS FILE IS AUTOMATICALLY GENERATED BY UNSTRUCTURED API TOOLS.
# DO NOT MODIFY DIRECTLY
#####################################################################


from fastapi import FastAPI, Request, status

from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address

from .text_input import router as text_input_router
from .hello_world import router as hello_world_router


limiter = Limiter(key_func=get_remote_address)
app = FastAPI(
    title="Unstructured Pipeline API",
    description="""""",
    version="2.1.0",
)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.include_router(text_input_router)
app.include_router(hello_world_router)


@app.get("/healthcheck", status_code=status.HTTP_200_OK)
async def healthcheck(request: Request):
    return {"healthcheck": "HEALTHCHECK STATUS: EVERYTHING OK!"}