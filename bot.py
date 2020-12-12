from instapy import InstaPy
import os 


import os 

insta_username = os.environ['INSTA_USER']
insta_password = os.environ['INSTA_PASSWORD']

# get a session!
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=True,
                  multi_logs=True)
                  
session.login()
session.like_by_tags(["developer", "coding"])

session.set_do_like(True, percentage=70)
session.set_delimit_liking(enabled=True, max=100, min=0)
# session.set_delimit_commenting(enabled=True, max=20, min=0)
session.set_do_comment(True, percentage=55)
session.set_comments(["Nice", "I loved it...", "Great quality","Awsm","Good","Nice Job!!!","Clean Work"])
 # settings
    session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    max_followers=4590,
                                    min_followers=100)

session.set_quota_supervisor(enabled=True, sleep_after=["likes", "comments_d", "follows", "unfollows", "server_calls_h"], sleepyhead=True, stochastic_flow=True, notify_me=True,
                                    peak_likes=(57, 585),
                                    peak_comments=(21, 182),
)


session.end()

