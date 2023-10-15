from fastapi import FastAPI

app=FastAPI()


@app.get("/сложение")
def add (a:int,b:int):
    return {"ответ":a+b}

@app.get("/вычитание")
def subtract (a:int,b:int):
    return {"ответ":a-b}

@app.get("/умножение")
def multiply (a:int,b:int):
    return {"ответ":a*b}

@app.get("/деление")
def divide (a:int,b:int):
    if b!=0:
        return {"ответ":a/b}
    else:
        return {"ошибка":"Деление на ноль"}
