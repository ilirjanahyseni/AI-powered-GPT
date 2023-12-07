"""
This code script fetches book information from the Google Books API based on a given ISBN.
"""

import requests # for making HTTP requests

def fetch_book_info(isbn):
    api_key = 'Insert_Your_API_Key'  # Replace with your actual API key
    url = f'https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}&key={api_key}'

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data.get('totalItems') > 0:
            book = data['items'][0]['volumeInfo']
            # Format the output for easy Excel entry
            authors = ", ".join(book.get('authors', ['Unknown']))
            title = book.get('title', 'Title not found')
            published_date = book.get('publishedDate', 'Date not found')
            page_count = book.get('pageCount', 'Page count not found')
            categories = ", ".join(book.get('categories', ['Category not found']))
            print(f"{isbn}\t{title}\t{authors}\t{published_date}\t{page_count}\t{categories}")
        else:
            print(f"No results found for ISBN: {isbn}")
    else:
        print(f"Failed to fetch data for ISBN: {isbn}. Status code: {response.status_code}")

# Example ISBN
isbn_list = ['9781590300787']  # Add your list of ISBNs
for isbn in isbn_list:
    fetch_book_info(isbn)
