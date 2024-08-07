# Instagram Followers Updates

Some tests based on scraping and collecting data from HTML.
I wanted to automate the connection to Instagram but couldn't reproduce the whole process without getting blocked...
So, if you'll excuse me, the data collection is done manually by copying the HTML element containing all the followers.

Later I'd like to make the tool work simply by downloading the full HTML page, but I don't have the time at the moment.

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

### Global updates
```py
tracker = InstagramFollowTracker()

new_followers, old_followers = tracker.see_updates("followers_A.html",
                                                   "followers_B.html")

print(f"{len(new_followers)} people followed you:\n", new_followers)
print(f"{len(old_followers)} people unfollowed you:\n", old_followers)
```
```bash
3 people followed you:
 ['user_01', 'user_06', 'user_56']

2 people unfollowed you:
 ['user_76', 'user_45']
```

### The number of people you follow who follow you back
```py
tracker = InstagramFollowTracker()

friends = tracker.following_back("followers_B.html", "following.html")

print(f"You follow {len(friends)} people who follow you back")
```
```bash
You follow 462 people who follow you back
```

### Users who don't follow you back
```py
tracker = InstagramFollowTracker()

not_following_back_users = tracker.not_following_back("followers_B.html",
                                                      "following.html")

print(f"{len(not_following_back_users)} users don't follow you back :\n",
      not_following_back_users)
```
```bash
120 users don't follow you back :
 ['user90', ..., user_128]
 ```
