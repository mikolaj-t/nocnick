# nocnick 
nocnick (abbreviation of Not Containing Nicknames) - a reddit bot which automatically detects and removes image submissions containing reddit usernames to prevent harassment of those users.

Built in Python, using PRAW and Pytesseract libraries, using Tesseract OCR to extract text from images

Intended to not yield false-positives - that's why it simply searches for usernames explicitly containing 'u/'. That means it will __not__ replace moderators, but it will take care of some of the work for them.

## How to run
### Option 1 (manually): 
1) Install python
2) Install all the required dependencies listed in `requirements.txt` using `pip`
3) Install [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) and add it to PATH
4) Run `python main.py`

### Option 2 (Docker):
This is the more convienient method, there is an already set up Dockerfile provided in the repo, so you just need to `docker build` and `docker run` 

## Configuration

The first time the bot is started, it will terminate and generate `credentials.yml` file, it is intended to look like this:

```yaml
login: username
password: password
client_id: client_id
client_secret: client_secret
user_agent: user_agent
```
(I got you covered - the `credentials.yml` file is included in `.gitignore` so it won't be pushed to git)

Then you need to change the credentials from the default placeholder ones. In order to use the Reddit API you need to generate OAuth credentials. [PRAW's documentation explains well how to register an app for the bot account.](https://praw.readthedocs.io/en/stable/getting_started/authentication.html#)

Then, there's also `config.yml` in which you can configure some of the bot's functionality:
```yaml
# mode: all for testing purposes, searches /r/all, doesn't delete submissions
# mode: mod for use in production, deletes submissions and checks only moderated communities
mode: mod

# debug: true/false - if true prints debug messages about submissions being checked
debug: false
```
In `mod` mode, the bot will perform its function on all subreddits on which it is added as a moderator. For debug/testing use `all` mode, it will output which posts from /r/all would be deleted, additionally with `debug` set to `true`  it will output the entire detected text contents of checked images.

## License
Shared under MIT License