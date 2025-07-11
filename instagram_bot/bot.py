from instapy import InstaPy
from instapy import smart_run

# Instagram credentials
insta_username = 'YOUR_USERNAME'  # Replace with your Instagram username
insta_password = 'YOUR_PASSWORD'  # Replace with your Instagram password

# List of comments to choose from
comments_list = [
    "Great post!",
    "Love this!",
    "Amazing content!",
    "So true!",
    "Nice shot!",
    "Keep it up!",
    "Inspiring!",
    "Awesome!",
    "Looks good!",
    "Fantastic!"
]

# Get an InstaPy session
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)

try:
    with smart_run(session):
        # General settings
        session.set_do_comment(enabled=True, percentage=25) # Comment on 25% of interacted posts
        session.set_comments(comments_list, media='Photo') # Provide the list of comments

        # Activity
        # You can specify tags to interact with, or interact with a user's followers/following, etc.
        # For example, to interact with posts based on tags:
        # session.like_by_tags(['#instagood', '#photooftheday'], amount=10)
        # session.interact_by_tags(['#travel', '#adventure'], amount=5, media='Photo', interact=True)


        # For now, let's set up a simple interaction to test commenting.
        # This will like 1-2 posts from the user 'target_username' and potentially comment.
        # Replace 'target_username' with a real Instagram username for testing.
        # session.interact_user_followers(['target_username'], amount=2, randomzie=False, interact=True)

        # IMPORTANT: To make the bot actually post comments randomly on user posts,
        # you'll need to configure more specific interaction methods above.
        # The current setup only *enables* commenting if an interaction (like, follow) occurs.

        print(f"Bot started. Will use comments: {comments_list}")
        print("PLease configure specific interaction methods (e.g., like_by_tags, interact_user_followers) to trigger comments.")
        print("Ensure you replace 'YOUR_USERNAME' and 'YOUR_PASSWORD' with your credentials.")
        print("If you want to test commenting, uncomment and configure an interaction line like session.interact_user_followers.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # End the session
    # session.end() # This is often handled by smart_run, but can be called explicitly if needed.
    print("Bot session finished.")

if __name__ == "__main__":
    # The script will run when executed.
    # The main logic is already within the try/except block.
    pass
