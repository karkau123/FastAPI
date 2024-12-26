from fastapi import FastAPI
# fastapi is the main package/library
#FastAPI is the specific class you're importing from it


app = FastAPI()


# ? is the query parameter
@app.get('/blog')   # this decorator will run the below function at some port no
def index(limit=10, published:bool=True):
    
    if (published):
        return {'data': f'{limit} published blogs from the Database'}
    else:
        return {'data': f'{limit} blogs from the Database'}
    



@app.get('blog/unpublished')
def unpublished():
    return {'data': "all unpublihed blogs"}


@app.get('/blog/{id}')  # use curly braces as you want dynamic id 
def show(id:int):
    #fetch blog with id = id
    return{'data' : id }





 

@app.get('/blog/{id}/comments')  # use curly braces as you want dynamic id 
def comments(id):
    #fetch blog with id = id
     return {
            "data": [
                {"id": 1, "comment": "First comment"},
                {"id": 2, "comment": "Second comment"}
            ]
        }

# for testing 