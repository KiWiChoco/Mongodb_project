import pymongo

def getPosts(db,userid):
# """
# It is similar to the function in wall.py
# Get posts of your followings.
# There can be a few options to sort the posts such as posting date or alphabetical order of following's name.
# """

    followings_list = db.user.find_one({"_id":userid})["followings"]
    followings_posts_id_list = []

    for users in followings_list:
        if db.posts.find_one({"id":users}):
            for id in list(db.posts.find({"id":users})):
                followings_posts_id_list.append(id["_id"])
        else: pass

    for id in sorted(followings_posts_id_list,reverse=True):
        post = db.posts.find_one({"_id": id})
        print("post_id : ",post["_id"],'\n'
              "title : ",post["title"], '\n'
              "text : ",post["txt"],'\n'
              "comment : ",post["comment"], '\n'
              "like : ",post["like"], '\n'
                )
        print("-"*80)




