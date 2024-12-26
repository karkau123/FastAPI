from fastapi import FastAPI
# fastapi is the main package/library
#FastAPI is the specific class you're importing from it


app = FastAPI()



@app.get('/')
def index():
    return {'data':{'name' : 'Roshni'}}


@app.get('/about')
def about():
    return{'data':{'about page'}}

