# def friend(x):
#     friends = []
#     for i in x:
#         if len(list(i)) == 4:
#             friends.append(i)
#     print(friends)

def friend(x):
    friend_list = [i for i in x if len(list(i)) == 4]
    return friend_list
