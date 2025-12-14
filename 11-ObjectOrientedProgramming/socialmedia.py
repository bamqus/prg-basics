

class SocialMediaProfile:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def add_post(self, content):
        self.posts.append(content)
        print(f"{self.username} added a new post: {content}")
    
    def display_timeline(self):
        print( "=" * 30)
        print("Your username is:", self.username)
        print("Your list of posts is:", len(self.posts))


def main():
    user = SocialMediaProfile("JohnDoe")
    user.add_post("Hello World!")
    user.add_post("Had a great day at the park!")
    user.add_post("What's up, Natalie? How are you?")
    user.display_timeline()






    
if __name__ == "__main__":
    main()


    

