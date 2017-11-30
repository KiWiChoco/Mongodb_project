import pymongo

def wall(db,userid):
# """
# Display your posts. Of course, get all posts would be fine.
# However, the function that supports displaying a few posts, e.g., five posts, looks much better than displaying all posts.
# Remind the lab4 that dealt with cursor.
# """
    walls = db.posts.find({"id":userid}).sort([("_id",pymongo.DESCENDING)])
    for self_wall in walls:
        print("post_id : ",self_wall["_id"],'\n'
              "title : ",self_wall["title"], '\n'
              "text : ",self_wall["txt"],'\n'
              "comment : ",self_wall["comment"], '\n'
              "like : ",self_wall["like"], '\n'
                )
        print("-"*80)