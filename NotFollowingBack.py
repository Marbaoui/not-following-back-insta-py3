from instaloader import Instaloader, Profile


def main():
    targetProfile = "The target profie"
    Username = "Your username"
    Pass = "Your password"
 
from instaloader import Instaloader, Profile
import os


known_account =  [] # contains know insta account to not include in comparison

print("loading...")
targetProfile = "The target profie"
Username = "Your username"
Pass = os.getenv("passinsta")
L = Instaloader()
profile = Profile.from_username(L.context, targetProfile)
L.login(Username, Pass)
def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

following = set(profile.get_followees())
followers = set(profile.get_followers())


notFollowers= intersection((following^followers), following)

notFollowersUsername = list(map(lambda user: user.username, notFollowers))
result = list(filter(lambda x: x not in known_account, notFollowersUsername))
print(result)
