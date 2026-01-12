# The uid array contains sample user IDs for a popular website. The IDs must be unique. Create a function
# f(uid) that returns true if all the given IDs are unique. Otherwise, the function returns false. Example:
# f(["john5","ann123","JOHN5","xxx","abc333","a10"]) returns True
# f(["abc123","ann","abc123","a10"]) returns False 

def f(uid):
    if set(uid) == uid:
        return True
    else:
        return False



print(f(["john5","ann123","JOHN5","xxx","abc333","a10"]))