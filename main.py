import asyncio
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
async def root():
    return HTMLResponse(str(open("test.html").read()), status_code=200)

@app.get("/addnewitem")
async def root():
    return HTMLResponse(str(open("addnewitem.html").read()), status_code=200)

@app.get("/additem.php")
async def root():
    return HTMLResponse(str(open("additem.php").read()), status_code=200)

@app.get("/removeitem")
async def root():
    return HTMLResponse(str(open("removeitem.html").read()), status_code=200)

@app.get("/remitem.php")
async def root():
    return HTMLResponse(str(open("remitem.php").read()), status_code=200)

@app.get("/rentitem")
async def root():
    return HTMLResponse(str(open("rentitem.html").read()), status_code=200)

@app.get("/rentitem.php")
async def root():
    return HTMLResponse(str(open("rentitem.php").read()), status_code=200)

@app.get("/unrentitem")
async def root():
    return HTMLResponse(str(open("unrentitem.html").read()), status_code=200)

@app.get("/unrentitem.php")
async def root():
    return HTMLResponse(str(open("unrentitem.php").read()), status_code=200)

@app.get("/search.php")
async def root():
    return HTMLResponse(str(open("search.php").read()), status_code=200)
