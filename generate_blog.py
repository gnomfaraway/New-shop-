
import openai, os, datetime

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_blog_post():
    today = datetime.date.today().strftime("%B %d, %Y")
    prompt = f"Write a 600-word helpful blog post with tips about AI tools for social media and ads. Add value and mention an example tool without sounding spammy."
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1200
    )
    return f"# AI Marketing Tips ({today})\n\n" + response.choices[0].message["content"]

def save_post(content):
    filename = f"blog/post_{datetime.date.today()}.md"
    os.makedirs("blog", exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

def post_to_socials(content):
    # Placeholder: Here you would add API calls for Reddit, Twitter, Pinterest
    print("Would auto-post to Reddit, Twitter, Pinterest with link to blog.")

if __name__ == "__main__":
    post = generate_blog_post()
    save_post(post)
    post_to_socials(post)
