def friend(x):

    real_friends = []
    for friend in x:
        if len(friend) == 4:
            real_friends.append(friend)
    return real_friends

print(friend(["Ryan", "Kieran", "Mark"]))