import instaloader

bot = instaloader.Instaloader()

def login(username, password):
    try:
        bot.login(user=username, passwd=password)
        print(f"Logged in as {username}")
    except instaloader.exceptions.InvalidCredentialsException:
        print("Invalid credentials. Please check your username and password.")
    except Exception as e:
        print(f"An error occurred: {e}")

def download_posts(profile_username, download_path):
    try:
        profile = instaloader.Profile.from_username(bot.context, profile_username)

        print(f"Username: {profile.username}")
        print(f"User ID: {profile.userid}")
        print(f"Number of Posts: {profile.mediacount}")
        print(f"Followers: {profile.followers}")
        print(f"Followees: {profile.followees}")
        print(f"Bio: {profile.biography}")
        print(f"External URL: {profile.external_url}")

        followers = [follower.username for follower in profile.get_followers()]
        print(f"Followers: {followers}")

        followees = [followee.username for followee in profile.get_followees()]
        print(f"Followees: {followees}")

        posts = profile.get_posts()
        for index, post in enumerate(posts, 1):
            bot.download_post(post, target=f"{download_path}/{profile_username}_{index}")
        print(f"Posts downloaded successfully to {download_path}")
    except instaloader.exceptions.ProfileNotExistsException:
        print(f"Profile '{profile_username}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    login("your_username", "your_password")

    download_posts("wwe", "downloaded_posts")

