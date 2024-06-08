import requests
import json

# Replace with your Page Access Token
ACCESS_TOKEN = 'YOUR_PAGE_ACCESS_TOKEN'
PAGE_ID = 'YOUR_PAGE_ID'

def get_page_posts(page_id, access_token):
    url = f'https://graph.facebook.com/{page_id}/posts'
    params = {
        'access_token': access_token
    }
    response = requests.get(url, params=params)
    return response.json()

def post_comment(post_id, message, access_token):
    url = f'https://graph.facebook.com/{post_id}/comments'
    params = {
        'message': message,
        'access_token': access_token
    }
    response = requests.post(url, data=params)
    return response.json()

def main():
    # Get recent posts
    posts = get_page_posts(PAGE_ID, ACCESS_TOKEN)

    for post in posts['data']:
        post_id = post['id']
        message = 'Thank you for your comment!'
        
        # Post a comment on each post
        result = post_comment(post_id, message, ACCESS_TOKEN)
        print(f"Commented on post {post_id}: {result}")

if __name__ == "__main__":
    main()
