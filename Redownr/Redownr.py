import praw
import pyimgur

client_id = "9a387a6750052fa"
client_secret = "f611bdbcec253c83635527c46ad1ca67047ca722"

class Redownr: 

    def __init__(self):
        self.r = praw.Reddit(user_agent="redownr")
        self.i = pyimgur.Imgur(client_id)
        self.subs = self.load_config("subreddits.txt")
        self.users = self.load_config("users.txt")
        #imgur.get_image("3rYHhEu").download(path="C:\\Users\\acurcie\\Desktop")


    def load_config(self, file):
        f = open("config/%s" % file)
        contents = f.readlines()
        f.close()
        return contents

    def load_links(self):
        for s in self.subs:
            for link in self.r.get_subreddit(s).get_hot(limit=self.limit):
                print(link.url, link.author, link.title)
        

def handle_arguments(r):
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", "-l",
                        help="Limits number of submissions retrieved; default = 20, 0 = unlimited",
                        type=int)
    args = parser.parse_args()
    r.limit = args.limit if args.limit else 20

if __name__ == "__main__":
    r = Redownr()
    handle_arguments(r)
    r.load_links()