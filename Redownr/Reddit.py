import praw
import re

class Reddit(object):
    """description of class"""
    def __init__(self):
        self.r = praw.Reddit(user_agent="redownr")

    def get_user(self, user_name):
        return User(self.r.get_redditor(user_name))

class User(object):
    """description of class"""
    def __init__(self, user):
        self.user = user
        self.id = user.id
        self.user_name = user.name
        self.links = []

    def _get_submissions(self, limit=5):
        subs = self.user.get_submitted(limit=limit)
        links = [sub.url for sub in subs if "imgur.com" in sub.url]
        return links
        
    def _get_comments(self, limit=5):
        comments = self.user.get_comments(limit=limit)
        links = []
        for com in comments:
            links.extend(re.findall("(?P<url>https?:\/\/[^\s\]\)]+)", com.body))
        return links

    def get_images(self, limit=5):
        self.links = self._get_submissions() + self._get_comments()
        return list(set(self.links))