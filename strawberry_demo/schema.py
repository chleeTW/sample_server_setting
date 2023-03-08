import typing
import strawberry
import asyncio
from typing import AsyncGenerator

def get_author_for_book(root) -> "Author":
    return Author(name="Michael Crichton")

def get_books_for_author(root):
    return [Book(title="Jurassic Park")]

@strawberry.type
class Book:
    title: str
    author: "Author" = strawberry.field(resolver=get_author_for_book)

@strawberry.type
class Author:
    name: str
    books: typing.List[Book] = strawberry.field(resolver=get_books_for_author)

def get_books():
    return  [
        Book(
            title="The Great Gatsby",
            author="F. Scott Fitzgerald",
        ),
    ]
    

def get_authors(root) -> typing.List[Author]:
    return [Author(name="Michael Crichton")]
    
@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "world"

@strawberry.type
class Query:
    authors: typing.List[Author] = strawberry.field(resolver=get_authors)
    books: typing.List[Book] = strawberry.field(resolver=get_books_for_author)

@strawberry.input
class AddBookInput:
    title: str = strawberry.field(description="The title of the book")
    author: str = strawberry.field(description="The name of the author")

@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_book(self, book: AddBookInput) -> Book:
        print(f"Adding {book.title} by {book.author}")
        return Book(title=book.title)

    @strawberry.mutation
    def restart() -> None: # 무효 결과가 있는 Mutation은 GQL 모범 사례에 위배됨
        print(f'Restarting the server')

@strawberry.type
class Subscription:
    @strawberry.subscription
    async def count(self, target: int = 100) -> AsyncGenerator[int, None]:
        for i in range(target):
            yield i
            await asyncio.sleep(0.5)

schema = strawberry.Schema(query=Query, mutation=Mutation, subscription=Subscription)