from fastapi import FastAPI,requests
import json
import uvicorn
app = FastAPI()

user_list=[{"name": "myra", "age": 23},{"name": "jaanu", "age": 7},{"name":"swathi",'age':'25'}]

@app.get("/main")
def root():
    return user_list
@app.get("/main/{id:int}")
def root_user(id: int):
    response = user_list[id]
    return dict(response)
@app.put("/main/{id:int}")
def user_put(id:int ,user: dict):
    user_list[id] = user
    return user_list
@app.post("/main")
def user_post(user: dict):
    new_user = user
    user_list.append(new_user)
    return user_list
@app.delete("/main/{id:int}")
def user_del(id:int):
    del user_list[id]
    return user_list
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
