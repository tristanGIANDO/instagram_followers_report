from bs4 import BeautifulSoup


class InstagramFollowTracker():
    def __init__(self) -> None:
        pass

    def _get_usernames(self, html_file: str) -> list[str]:
        with open(html_file, 'r', encoding='utf-8') as file:
            html_content = file.read()

        soup = BeautifulSoup(html_content, 'html.parser')
        img_tags_with_alt = soup.find_all('img', alt=True)

        usernames = []
        for img_tag in img_tags_with_alt:
            text = str(img_tag)
            usernames.append(
                text.split("Photo de profil de ")[1].split('"')[0])

        return usernames

    def see_updates(self, followers_file_A: str, followers_file_B: str):
        set_a = set(self._get_usernames(followers_file_A))
        set_b = set(self._get_usernames(followers_file_B))

        return list(set_b - set_a), list(set_a - set_b)

    def following_back(self, followers_file: str, following_file: str):
        followers = set(self._get_usernames(followers_file))
        following = set(self._get_usernames(following_file))

        return list(followers & following)

    def not_following_back(self, followers_file: str, following_file: str):
        followers = set(self._get_usernames(followers_file))
        following = set(self._get_usernames(following_file))

        not_followers_back = list(following - followers)

        return not_followers_back


if __name__ == "__main__":
    # get files
    followers_at_time_A = "followers_02.html"
    followers_at_time_B = "followers_240726.html"
    following = "following.html"
    tracker = InstagramFollowTracker()

    # global updates
    new_followers, old_followers = tracker.see_updates(followers_at_time_A,
                                                       followers_at_time_B)
    print(f"{len(new_followers)} people followed you:\n", new_followers)
    print(f"{len(old_followers)} people unfollowed you:\n", old_followers)

    # statistics
    friends = tracker.following_back(followers_at_time_B, following)
    print(f"You follow {len(friends)} people who follow you back")

    not_following_back_users = tracker.not_following_back(followers_at_time_B,
                                                          following)
    print(f"{len(not_following_back_users)} users don't follow you back :\n",
          not_following_back_users)
