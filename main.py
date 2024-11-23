
class Book:
    def __init__(self, book_id, title, author, year):
        self.id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.status = 'В наличии'

class Library:
    def __init__(self):
        self.books = []
        self.next_id = 1

    def add_book(self, title, author, year):
        book = Book(self.next_id, title, author, year)
        self.books.append(book)
        self.next_id += 1

    def remove_book(self, book_id):
        self.books = [book for book in self.books if book.id != book_id]

    def search_book(self, request):
        result = [book for book in self.books if request.lower() in (book.title.lower() or book.author.lower() or str(book.year))]
        return result

    def display_books(self):
        for book in self.books:
            print(f'ID: {book.id}, Title: {book.title}, Author: {book.author}, Year: {book.year}, Status: {book.status}')

    def change_status(self, book_id, new_status):
        for book in self.books:
            if book in self.books:
                book.status = new_status
                break

def main():
    library = Library()
    while True:
        action = int(input('Выберите дейстие: 1 - добавить книгу, 2 - удалить книгу, 3 - поиск книги, 4 - иззменить статус книги, 5 - показать список книг, 6 - выход: '))
        if action == 1:
            title = input('Введите название книги: ')
            author = input('Введите автора: ')
            year = int(input('Введите год издания: '))
            library.add_book(title, author, year)
        elif action == 2:
            book_id = int(input('Введите ID книги для удаления: '))
            library.remove_book(book_id)
        elif action == 3:
            request = input('Введите название, автора или год для поиска: ')
            result = library.search_book(request)
            for book in result:
                print(f'ID: {book.id}, Title: {book.title}, Author: {book.author}, Year: {book.year}, Status: {book.status}')
        elif action == 4:
            book_id = int(input('Введите ID книги для изменения статуса: '))
            new_status = input('Введите новый статус (в наличии или выдана): ')
            library.change_status(book_id, new_status)
        elif action == 5:
            library.display_books()
        elif action == 6:
            break

if __name__ == '__main__':
    main()






