#!/usr/bin/env python3
"""
module to obtain the HTML content of a particular URL and returns it.
"""

import requests
import redis
import time

def get_page(url: str) -> str:
    """
    Fetches the HTML content of a given URL and returns it.

    Args:
        url (str): The URL to fetch.

    Returns:
        str: The HTML content of the URL.
    """
    # Connect to Redis
    redis_client = redis.Redis()

    # Check if the URL content is already cached
    cached_html = redis_client.get(url)
    if cached_html:
        # If cached, return the cached HTML
        return cached_html.decode()

    # If not cached, fetch the HTML content using requests
    response = requests.get(url)
    html_content = response.text

    # Cache the result with an expiration time of 10 seconds
    redis_client.setex(url, 10, html_content)

    return html_content

if __name__ == "__main__":
    # Example usage
    url = "http://slowwly.robertomurray.co.uk/delay/1000/url/https://www.example.com"
    start_time = time.time()
    html_content = get_page(url)
    elapsed_time = time.time() - start_time

    print("Elapsed Time:", elapsed_time)
    print(html_content)
