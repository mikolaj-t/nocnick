import yaml
import os;

_configPath = "config.yml"
_credentialsPath = "credentials.yml"

_username = "login"
_password = "password"
_client_id = "client_id"
_client_secret = "client_secret"
_user_agent = "user_agent"


def username():
    return _credentials[_username]
def password():
    return _credentials[_password]
def client_id():
    return _credentials[_client_id]
def client_secret():
    return _credentials[_client_secret]
def user_agent():
    return _credentials[_user_agent]

def subreddit():
    return "mod" if _value["mode"] == "mod" else "all"

def mod_mode():
    return True if _value["mode"] == "mod" else False

def debug():
    return _value["debug"]

def init():
    print("Loading config...")
    if(os.path.exists(_credentialsPath) == False):
        createCredentials()
        return False
    else:
        with open(_configPath) as configFile:
            global _value
            _value = yaml.safe_load(configFile)
        with open(_credentialsPath) as credentialsFile:
            global _credentials 
            _credentials = yaml.safe_load(credentialsFile)
        print("Loading config complete!")
        return True
            
def createCredentials():
    print("credentials.yml not found! Shutting down the bot...")
    with open(_credentialsPath, "w") as credentialsFile:
        credentialsFile.write(_username + ": username\n")
        credentialsFile.write(_password + ": password\n")
        credentialsFile.write(_client_id + ": client_id\n")
        credentialsFile.write(_client_secret + ": client_secret\n")
        credentialsFile.write(_user_agent + ": user_agent\n")
        print("credentials.yml file created, remember to change the placeholder values!")