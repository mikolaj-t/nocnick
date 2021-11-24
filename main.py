import praw
import config
import time
import checker

def main():
    if not config.init():
        return

    print("Authenticating the reddit account...")
    reddit = praw.Reddit(
        client_id = config.client_id(),
        client_secret = config.client_secret(),
        user_agent = config.user_agent(),
        username = config.username(),
        password = config.password(),
    )

    print("Authenticated successfully!")
    
    lastChecked = {}

    while(True):
        for post in reddit.subreddit(config.subreddit()).stream.submissions():
            if not hasattr(post, "post_hint"): continue
            if post.post_hint != "image": continue

            subredditName = post.subreddit.display_name
            if subredditName in lastChecked and lastChecked[subredditName] >= post.created_utc:
                continue
            else:
                lastChecked[subredditName] = post.created_utc

            url = post.url

            imageText = checker.check(url)

            if config.debug:
                print(url + " contents:")
                print(imageText)

            if "u/" in imageText:
                if config.mod_mode: 
                    post.reply("Hello there, your image post contains a reddit username so according to the subreddit rules it has been deleted!\n\n\n"
                                "*I am a bot, this action was performed automatically*    | [source code](https://github.com/mikolaj-t/nocnick)")
                    post.delete()
                    print("Deleted post " + post.id)
                else:
                    print("Post " + post.id + " would be deleted")

        time.sleep(10.0)
                    
    
if __name__ == "__main__":
    main()