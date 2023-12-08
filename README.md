# AI-powered-library

Personal AI Librarian:  Custom GPT Bookshelf Explorer 

https://chat.openai.com/g/g-54hwDuiRA-personal-ai-librarian 
## 
![AI Library copy](https://github.com/ilirjanahyseni/personal-library/assets/92699878/61033d70-68e2-4d1e-bfa9-c8e7a26693a2) 

## 
### Scope and Features 
Inventory Management: catalogs books, including details like title, author, genre, publication year, and personal annotations.

Search Functionality: can search for books by various criteria and reading progress/status of each book. 

Reading Recommendations: the GPT can suggest books from the library based on topic or preference. 

### Data Collection and Organization Tools
1. Cataloging Books: A comprehensive list of books was created using an [ISBN scan reader](https://play.google.com/store/apps/details?id=org.micla.MiClaScanISBN&hl=en_US&gl=US).

2. Google Cloud Platform: set up an API Key for Google Books API web service. 
3. Python and APIs: used `requests` (HTTP library) to make requests to the web service for book data based on its ISBN.
4. Data Fetching and Storage: querying scripts executed in VS Code [print out details](https://github.com/ilirjanahyseni/AI-powered-library/blob/main/import%20requests2.py) about the books associated with ISBN(s) and/or [store the data]( https://github.com/ilirjanahyseni/AI-powered-library/blob/main/import%20requests.py) in a CSV file. 
