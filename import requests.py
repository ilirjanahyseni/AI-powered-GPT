
"""
ISBN Book Info Fetcher:
This Python script fetches book information from the Google Books API using scanned ISBNs and stores it in a CSV file. 
It utilizes Google Cloud for API key management and data retrieval. 
First step in organizing personal book collection.
"""

import requests
import csv
def fetch_book_info(isbn):
    api_key = 'Insert_Your_API_Key_Here'  # Replace with your  API key
    url = f'https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}&key={api_key}'

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(data)  # Debugging: print API response
        if data.get('totalItems') > 0:
            book = data['items'][0]['volumeInfo']
            return {
                "ISBN": isbn,
                "Title": book.get('title', 'Title not found'),
                "Authors": ", ".join(book.get('authors', ['Unknown'])),
                "PublishedDate": book.get('publishedDate', 'Date not found'),
                "PageCount": book.get('pageCount', 'Page count not found'),
                "Categories": ", ".join(book.get('categories', ['Category not found']))
            }
        else:
            return {"ISBN": isbn, "Title": "No results found"}
    else:
        return {"ISBN": isbn, "Title": f"Failed to fetch data. Status code: {response.status_code}"}

isbn_list = [ "9780747532743"]  # Insert ISBNs here

with open('books.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=["ISBN", "Title", "Authors", "PublishedDate", "PageCount", "Categories"])
    writer.writeheader()
    for isbn in isbn_list:
        book_info = fetch_book_info(isbn)
        print(book_info)  # Debugging: print book info
        writer.writerow(book_info)
