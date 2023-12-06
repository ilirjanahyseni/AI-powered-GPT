
"""
ISBN Book Info Fetcher:
This Python script fetches book information from the Google Books API using scanned ISBNs and stores it in a CSV file. 
It utilizes Google Cloud for API key management and data retrieval. 
First step in organizing personal book collection.
"""

import requests
import csv
def fetch_book_info(isbn):
    api_key = 'My_Key'  # Replace with your actual API key
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

isbn_list = [ "9780143028468", "9780140294729", "9780385424011", "9780983632948",
    "9780740700255", "9780399579660", "9780800736521", "9781572241244",
    "9781850153085", "9780061582486", "9780375701719", "9781400052189",
    "9780826209122", "9780375714368", "9780156628709", "9780393340662",
    "9780099760115", "9780544947108", "9781593081218", "9781593081522",
    "9780679783305", "9780805069853", "9781847241474", "9780385502535",
    "9781451626650", "9781400031726", "9780713630343", "9780140440034",
    "9780140440034", "9781840224306", "9781476746586", "9780495094920",
    "9780307945020", "9780553375404", "9780241951644", "9780553379013",
    "9780192860927", "9780140097191", "9780767904421", "9780385479561",
    "9780553214635", "9780143117001", "9780804190114", "9780312464516",
    "9780883961988", "9780684843261", "9780791086780", "9780198558033",
    "9780763631208", "9781403715777", "9781555910945", "9789951063821",
    "9789951063777", "9789951063791", "9780965555500", "9781426220951",
    "9780385364362", "9780756630799", "9781603761840", "9783319468570",
    "9780963378453", "9780681890435", "9780761104872", "9780312448417",
    "9780060674403", "9780299250843", "9780812971835", "9780812986471",
    "9780553375404", "9780812986679", "9780451530578", "9780451487841",
    "9780451530271", "9781566196888", "9781416572459", "9780345466631",
    "9780553210095", "9780375707285", "9780763621643", "9780142437339",
    "9781798500620", "9781453055434", "9780446310789", "9780140086836",
    "9780679755333", "9780553277456", "9789994312931", "9780142437179",
    "9780375752513", "9780385545136", "9780140048971", "9780948397424",
    "9780060740450", "9780743487580", "9780486284736", "9780802130341",
    "9780385751537", "9780679756972", "9780452011670", "9780756638801",
    "9780385520379", "9780199535958", "9780316182355", "9780300087017",
    "9780061245619", "9780385189507", "9780525434955", "9780393960587",
    "9780143114246", "9780679428954", "9781603580557", "9781433811258",
    "9780470551714", "9780143115007", "9780744026955", "9780736077453",
    "9781439079454", "9781419737497", "9781480354883", "9781423455301",
    "9781495090257", "9781495023392", "9781423455332", "9781423426684",
    "9781502765673", "9781502802149", "9781540030221", "9780825610981",
    "9780486493770", "9780593297063", "9781118859209", "9781558605527",
    "9781565920002", "9780300196214", "9780696201684"]  # Scanned ISBNs

with open('books.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=["ISBN", "Title", "Authors", "PublishedDate", "PageCount", "Categories"])
    writer.writeheader()
    for isbn in isbn_list:
        book_info = fetch_book_info(isbn)
        print(book_info)  # Debugging: print book info
        writer.writerow(book_info)
