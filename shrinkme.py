from helper import create_shrinkme_link

def get_verification_link(user_id: int) -> str:
    original_url = f"https://example.com/verify/{user_id}"  # Replace with real redirect
    return create_shrinkme_link(original_url)
