import asyncio
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
async def root():
    return HTMLResponse(str(open("test.html").read()), status_code=200)

def bootup():
    print("Server is ready.")

if __name__ == '__main__':
    bootup()
