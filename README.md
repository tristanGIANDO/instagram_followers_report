# Instagram Followers Updates

Thanks to a scraping method, stay informed about who unfollows you or doesn't follow you back, etc...

Beware, it's a bit manual. I coded this in an afternoon just to practice scraping info.

## Getting started

### Requirements

Install `BeautifulSoup` -> `pip install bs4`

### Collect data

1. Go to instagram PC version and click on "followers" from your profile.
2. Scroll through all your followers until they are all loaded.
3. Right-click "Inspect element".
4. Identify the element in the inspector, then right-click "copy element".
5. Paste element into HTML file

6. Execute the code, specifying the newly created HTML files

P.S.: To retrieve the users you follow, it's exactly the same,
but click on "following".

## Example of use

```py
if __name__ == "__main__":
    # get files
    followers_at_time_A = "followers_A.html"
    followers_at_time_B = "followers_B.html"
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
```

_Output:_

```bash
3 people followed you:
 ['user_01', 'user_06', 'user_56']

2 people unfollowed you:
 ['user_76', 'user_45']

You follow 462 people who follow you back

120 users don't follow you back :
 ['user90', ..., user_128]
 ```
