from fastapi import FastAPI, Header, status
from fastapi.exceptions import HTTPException
from typing import Optional
from pydantic import BaseModel
from typing import List

app = FastAPI()
 

books = [
    {
        "id": 1,
        "title": "Order above wear.",
        "author": "Karen Murphy",
        "publisher": "Larson Group",
        "published_date": "1970-08-14",
        "page_count": 688,
        "language": "Spanish"
    },
    {
        "id": 2,
        "title": "Miss mission.",
        "author": "Julia Jones",
        "publisher": "Cook Group",
        "published_date": "2018-11-27",
        "page_count": 406,
        "language": "English"
    },
    {
        "id": 3,
        "title": "School learn.",
        "author": "Douglas Rodriguez",
        "publisher": "Taylor Ltd",
        "published_date": "2004-07-15",
        "page_count": 358,
        "language": "Japanese"
    },
    {
        "id": 4,
        "title": "Lot magazine news who possible.",
        "author": "Dr. Jennifer Evans",
        "publisher": "Hill PLC",
        "published_date": "1979-02-28",
        "page_count": 933,
        "language": "Spanish"
    },
    {
        "id": 5,
        "title": "Left recognize he answer ago.",
        "author": "Robert White Jr.",
        "publisher": "Jensen-Martinez",
        "published_date": "2023-10-27",
        "page_count": 397,
        "language": "Italian"
    },
    {
        "id": 6,
        "title": "All my.",
        "author": "Angela Miller",
        "publisher": "Taylor Inc",
        "published_date": "2013-08-16",
        "page_count": 523,
        "language": "Japanese"
    },
    {
        "id": 7,
        "title": "Expert vote garden full white.",
        "author": "Nicole Clark",
        "publisher": "Rogers, Ortiz and Barnes",
        "published_date": "1971-03-22",
        "page_count": 467,
        "language": "Russian"
    },
    {
        "id": 8,
        "title": "Republican why enough as between.",
        "author": "Caleb Thompson",
        "publisher": "Davis, Huynh and Underwood",
        "published_date": "1998-11-02",
        "page_count": 618,
        "language": "Portuguese"
    },
    {
        "id": 9,
        "title": "Huge class team.",
        "author": "Martin Hall",
        "publisher": "Hall, Smith and Evans",
        "published_date": "1970-01-30",
        "page_count": 973,
        "language": "Chinese"
    },
    {
        "id": 10,
        "title": "The enjoy old also maintain.",
        "author": "Sarah Reid DDS",
        "publisher": "Morgan-Hoffman",
        "published_date": "1981-03-18",
        "page_count": 101,
        "language": "Russian"
    }
]


class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str

class BookUpdateModel(BaseModel):
    title: str
    author: str
    publisher: str
    page_count: int
    language: str


@app.get('/books', response_model=List[Book])
async def get_all_books():
    return books

@app.post('/books', status_code=status.HTTP_201_CREATED)
async def create_a_book(book_data: Book) -> dict:
    new_book = book_data.model_dump()

    books.append(new_book)

    return new_book

@app.get('/books/{book_id}')
async def get_book(book_id: int) -> dict:
    for book in books:
        if book['id'] == book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="Book not found")

@app.patch('/books/{book_id}')
async def update_book(book_id: int, book_update_data: BookUpdateModel) -> dict:
    
    for book in books:
        if book['id'] == book_id:
            book['title'] = book_update_data.title
            book['publisher'] = book_update_data.publisher
            book['page_count'] = book_update_data.page_count
            book['language'] = book_update_data.language

            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                        detail="Books not found")

@app.delete ('/books/{book_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int):
    for book in books:
        if book['id'] == book_id:
            books.remove(book)

            return {}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                        detail="Book not found")