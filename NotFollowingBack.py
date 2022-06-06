from instaloader import Instaloader, Profile


def main():
    targetProfile = "The target profie"
    Username = "Your username"
    Pass = "Your password"
    L = Instaloader()
    profile = Profile.from_username(L.context, targetProfile)
    L.login(Username, Pass)
    def intersection(lst1, lst2):
        return list(set(lst1) & set(lst2))

    following = set(profile.get_followees())
    followers = set(profile.get_followers())

    notFollowers= intersection((following^followers), following)

    notFollowersUsername = (map(lambda user: user.username, notFollowers))

    print(list(notFollowersUsername))

main()
