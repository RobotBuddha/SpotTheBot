def friend_follower_ratio(user):
    friends = user.friends_count + 1
    followers = user.followers_count + 1

    if friends==followers:
        return 0.5
    elif friends>followers:
        ratio = (followers*1.0)/friends
        return 1-(0.5*ratio)
    else:
        ratio = (friends*1.0)/followers
        return 0.5*ratio
