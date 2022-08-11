from fastapi import FastAPI
from routers import person_router, address_router
import uvicorn

app = FastAPI()
app.include_router(person_router.person_router)
app.include_router(address_router.address_router)


@app.get("/")
async def Hg():
    return {"asdasd": "Hello World"}


def main():
    uvicorn.run("routes:app", reload=True, debug=True, host="0.0.0.0", port=8000)


if __name__ == ("__main__"):
    main()
