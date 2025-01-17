from flask import Flask, render_template
import requests


app = Flask(__name__)

blog_url = 'https://api.npoint.io/d8f5f122aa01ca7e3575'
response = requests.get(url=blog_url)
all_posts = response.json()

@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)

@app.route('/post/<int:post_id>')
def post_redirect(post_id):
    p = None
    for post in all_posts:
        if post['id'] == post_id:
            p = post
            break
    return render_template("post.html", post=p)



if __name__ == "__main__":
    app.run(debug=True)
