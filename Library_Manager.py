import json


BOOKS_FILE = "books.json"


def load_books():
    try:
        with open(BOOKS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_books(books):
    with open(BOOKS_FILE, "w") as file:
        json.dump(books, file, indent=4)


def add_book():
    title = input("Enter book title: ").strip()
    author = input("Enter author: ").strip()
    genre = input("Enter genre: ").strip()
    status = input("Enter status (Unread/Reading/Completed): ").strip().capitalize()
    
    if status not in ["Unread", "Reading", "Completed"]:
        print("Invalid status! Defaulting to 'Unread'.")
        status = "Unread"

    try:
        year = int(input("Enter publication year: "))
    except ValueError:
        print("Invalid year! Setting default year to 0.")
        year = 0

    books = load_books()
    books.append({"title": title, "author": author, "genre": genre, "status": status, "year": year})
    save_books(books)
    print("\n Book added successfully!\n")


def display_books():
    books = load_books()
    if not books:
        print("\n No books in the library!\n")
        return

    print("\n Your Books:")
    for index, book in enumerate(books, start=1):
        title = book.get("title", "Unknown Title")
        author = book.get("author", "Unknown Author")
        genre = book.get("genre", "Unknown Genre")
        year = book.get("year", "Unknown Year")
        status = book.get("status", "Unknown Status")

        print(f"{index}. {title} by {author} ({genre}, {year}) - {status}")
    print()


def search_book():
    query = input("Enter book title or author to search: ").strip().lower()
    books = load_books()
    results = [book for book in books if query in book.get("title", "").lower() or query in book.get("author", "").lower()]

    if results:
        print("\n Search Results:")
        for book in results:
            print(f"- {book['title']} by {book['author']} ({book['genre']}, {book['year']}) - {book['status']}")
    else:
        print("\n No books found!")


def delete_book():
    books = load_books()
    if not books:
        print("\n No books to delete!\n")
        return

    display_books()
    try:
        book_index = int(input("Enter the book number to delete: ")) - 1
        if 0 <= book_index < len(books):
            removed_book = books.pop(book_index)
            save_books(books)
            print(f"\n '{removed_book['title']}' deleted successfully!\n")
        else:
            print("\n Invalid book number!\n")
    except ValueError:
        print("\n Please enter a valid number!\n")


def display_statistics():
    books = load_books()
    total_books = len(books)
    completed_books = sum(1 for book in books if book.get("status", "").lower() == "completed")
    reading_books = sum(1 for book in books if book.get("status", "").lower() == "reading")
    unread_books = sum(1 for book in books if book.get("status", "").lower() == "unread")

    print("\n Library Statistics")
    print(f" Total Books: {total_books}")
    print(f" Completed Books: {completed_books}")
    print(f" Currently Reading: {reading_books}")
    print(f" Unread Books: {unread_books}\n")


def main():
    while True:
        print("\n Personal Library Manager")
        print("1 Add Book")
        print("2 View Books")
        print("3 Search Book")
        print("4 Delete Book")
        print("5 View Statistics")
        print("6 Exit")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_book()
        elif choice == "2":
            display_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            delete_book()
        elif choice == "5":
            display_statistics()
        elif choice == "6":
            print("\n Goodbye! Happy Reading!\n")
            break
        else:
            print("\n Invalid choice! Please enter a number between 1-6.\n")

if __name__ == "__main__":
    main()
