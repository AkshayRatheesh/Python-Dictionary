from fastapi import FastAPI, Response, status, HTTPException

import json

# from fastapi.params import Body
# from pydantic import BaseModel 
# from typing import Optional
# from random import randrange

# import psycopg2
# from psycopg2.extras import RealDictCursor
# import time

app = FastAPI()



# class Post(BaseModel):
#     title: str
#     contents: str
#     published: bool = True  #this is going to optional input, because we set default calue as Troe
#     rating : Optional[int] = None # this is also an optional field, if data not passed then this field going to empty

# #database stuff
# while True:
    
#     try:
#         conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres',
#                                 password='112233', cursor_factory=RealDictCursor)
#         cursor =conn.cursor()
#         print("database connection success")
#         break
#     except Exception as error:
#         print("connection failed")
#         print(error)
#         time.sleep(2)
        



# my_posts = [{"title":"title one", "contents":"nothing 1", "id": 1},{
#     "title":"title two", "contents":"nothing 2", "id": 2}]

# def find_post(id):
#     for p in my_posts:
#         if p["id"] == id:
#             return p

# def find_index_post(id):
#     for i, p in enumerate(my_posts):
#         if p['id'] == id:
#             return i    
    

@app.get("/")
def read_root():
    return {"Hello": "world akshay"}


@app.get("/posts")
def get_posts():
    
    data = json.load(open('dictionary_compact.json'))  
    meaning = data["post"]
     
    return {"data": meaning}


# @app.post("/posts", status_code=status.HTTP_201_CREATED)
# def create_posts(post:Post):
#     # post_dict= post.dict() # convert into a dictionary
#     # post_dict['id']= randrange(0, 1000)
#     # my_posts.append(post_dict)
    
#     cursor.execute("""INSERT INTO post (title, content ) VALUES (%s, %s) RETURNING * """,(post.title, post.contents))
    
#     new_post = cursor.fetchone()
    
#     conn.commit() #saving to database
    
#     return{"data": new_post}


# @app.get("/posts/{id}")
# def get_post(id: int, response: Response):
    
#     cursor.execute("""SELECT * FROM post WHERE id=%s """,(str(id),))
#     post = cursor.fetchone()
       
#     # post = find_post(id)
#     if not post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"post with id {id} not found")
        
#         ## response.status_code = status.HTTP_404_NOT_FOUND
#         ## return {'message': f"post with id {id} not found"}
        
#     return {"post_detail":post}

# #delete post
# @app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_post(id: int):
#     #index = find_index_post(id)
    
#     cursor.execute("""DELETE FROM post WHERE id=%s RETURNING * """,(str(id),))
#     deleted_post= cursor.fetchone()
    
#     conn.commit()
    
#     if deleted_post == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"post with id {id} not found")
    
#     #my_posts.pop(index)
#     return Response(status_code=status.HTTP_204_NO_CONTENT)


# #update request
# @app.put("/posts/{id}")
# def update_post(id : int, post: Post):

#     #index = find_index_post(id)
#     cursor.execute("""UPDATE post SET title =%s, content =%s WHERE id=%s RETURNING *""" , (post.title, post.contents, str(id), ))
#     updated_post = cursor.fetchone()
#     conn.commit()
    
    
#     if updated_post == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"post with id {id} not found")
  
#     # post_dict = post.dict()
#     # post_dict['id'] = id
#     # my_posts[index] =post_dict
#     return{"data": updated_post}


    