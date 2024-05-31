import re

def extract_urls(text):
    # Regular expression pattern to match URLs
    url_pattern = r'https?://\S+'

    # Find all matches of URLs in the text
    urls = re.findall(url_pattern, text)

    return urls

# Example usage:
text = """
Here is a website: https://www.example.com
And another one: http://sub.example.com/page.html
You can also visit this: www.subdomain.example.org
But don't forget: ftp://ftp.example.net
"""

urls = extract_urls(text)
print("Extracted URLs:")
for url in urls:
    print(url)
