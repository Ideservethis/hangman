import re

def is_valid_email(email):
    # Regular expression pattern for email validation
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

# Example usage:
emails = [
    'user@example.com',
    'user123@example.co.uk',
    'user.name@example.com',
    'user+tag@example.com',
    'user_name@example-domain.com',
    'user@example'
]

for email in emails:
    if is_valid_email(email):
        print(f"{email} is a valid email address.")
    else:
        print(f"{email} is not a valid email address.")
