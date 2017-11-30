def follow(db, userid):

    user_following = db.user.find_one({"_id":userid})["followings"]
    if user_following:
        print("\nYour following list : ", user_following)
    else: print("\nYour following list is empty")

    follow_id = input("\nplease enter want to follow : ")
    #try:
    if db.user.find_one({"_id":follow_id}):
        if follow_id not in db.user.find_one({"_id":userid})["followings"]:
            # follow_id = db.user.find_one({"name":follow_name})["_id"]
            db.user.update_one({"_id":userid},{"$push":{"followings":follow_id}})
            db.user.update_one({"_id":follow_id},{"$push":{"follower":userid}})
        else :
            print("\nThat user already following")
    else :
        print("\nThere is not user that id")
  #  print(db.user.find_one({"_id":userid})["followings"])

        # '''
        # 1. 팔로우하고자 하는 유저가 존재하는지 확인, 없으면 경고 출력
        #
        # 2. 팔로우하고자 하는 유저가 나의 팔로잉 목록에 있는지 확인, 있으면 경고 출력
        #
        # 3. 팔로잉 목록에 없으면,
        #     나의 팔로잉 목록에 팔로우할 유저id 추가 + 상대방의 팔로워 목록에 내 id 추가
        # '''
    # except Exception as e:
    #     print("could not operate following %s\n" %e)

def unfollow(db, userid):

    user_following = db.user.find_one({"_id":userid})["followings"]
    if user_following:
        print("\nYour following list : ", user_following)
    else: print("\nYour following list is empty")

    unfollow_id = input("\nplease enter want to unfollow : ")
    #try:
    if db.user.find_one({"_id":unfollow_id}):
        if unfollow_id in db.user.find_one({"_id":userid})["followings"]:
            # follow_id = db.user.find_one({"name":follow_name})["_id"]
            db.user.update_one({"_id":userid},{"$pull":{"followings":unfollow_id}})
            db.user.update_one({"name":unfollow_id},{"$pull":{"follower":userid}})
        else :
            print("\nThat user is not in following list")
    else :
        print("\nThere is not user that id")

    # try:

        # '''
        # 1. 언팔로우하고자하는 유저가 존재하는지 확인, 없으면 경고 출력
        #
        # 2. 언팔로우하고자 하는 유저가 나의 팔로잉 목록에 있는지 확인, 없으면 경고 출력
        #
        # 3. 팔로잉 목록에 있으면,
        #     나의 팔로잉 목록에서 언팔로우할 유저id 제거 + 상대방의 팔로워 목록에서 내 id 제거
        # '''
    # except Exception as e:
    #     sys.stderr.write("could not operate following %s\n" %e)
    pass