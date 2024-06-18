from bs4 import BeautifulSoup

"""
1. Go to instagram PC version and click on "followers" from your profile.
2. Scroll through all your followers until they are all loaded.
3. Right-click "Inspect element".
4. Identify the element in the inspector, then right-click "copy element".
5. Paste element into HTML file

6. Execute this code, specifying the newly created HTML file

P.S.: To retrieve the users you follow, it's exactly the same,
but click on "following".
"""


def get_usernames(html_file: str) -> list[str]:
    with open(html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')
    img_tags_with_alt = soup.find_all('img', alt=True)

    usernames = []
    for img_tag in img_tags_with_alt:
        text = str(img_tag)
        usernames.append(text.split("Photo de profil de ")[1].split('"')[0])

    # with open("following.json", "w", encoding="utf-8") as f:
    #     json.dump(usernames, f, indent=4)

    return usernames


def find_real_friends(followers_file: str, following_file: str):
    followers = set(get_usernames(followers_file))
    following = set(get_usernames(following_file))

    friends = list(followers & following)
    print(f"You have {len(friends)} real friends :")
    for friend in friends:
        print(friend)

    return friends


def not_follow_back(followers_file: str, following_file: str):
    followers = set(get_usernames(followers_file))
    following = set(get_usernames(following_file))

    not_followers_back = list(following - followers)

    print(f"{len(not_followers_back)} users don't follow you back :")
    for user in not_followers_back:
        print(user)

    return not_followers_back


def followers_updates(followers_file_A: str, followers_file_B: str):
    set_a = set(get_usernames(followers_file_A))
    set_b = set(get_usernames(followers_file_B))

    new_followers = list(set_b - set_a)
    old_followers = list(set_a - set_b)

    print("They followed you :")
    for follower in new_followers:
        print(follower)

    print("They unfollowed you :")
    for user in old_followers:
        print(user)

    return new_followers, old_followers


if __name__ == "__main__":
    followers_updates("followers_A.html", "followers_B.html")

    not_follow_back("followers.html", "following.html")

    find_real_friends("followers_file.html", "following_file.html")
