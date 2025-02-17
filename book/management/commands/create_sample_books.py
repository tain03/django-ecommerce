# book/management/commands/create_sample_books.py
from django.core.management.base import BaseCommand
from book.models import Book
from django.utils.text import slugify

class Command(BaseCommand):
    help = 'Creates sample book data'

    def handle(self, *args, **kwargs):
        books_data = [
            {
                'title': 'The Great Gatsby',
                'author': 'F. Scott Fitzgerald',
                'description': 'A story of decadence and excess, following the mysterious millionaire Jay Gatsby.',
                'price': 15.99
            },
            {
                'title': 'To Kill a Mockingbird',
                'author': 'Harper Lee',
                'description': 'A novel about racial injustice and the loss of innocence in the American South.',
                'price': 14.99
            },
            {
                'title': '1984',
                'author': 'George Orwell',
                'description': 'A dystopian novel set in a totalitarian society under constant surveillance.',
                'price': 12.99
            },
            {
                'title': 'Pride and Prejudice',
                'author': 'Jane Austen',
                'description': 'A romantic novel following the emotional development of Elizabeth Bennet.',
                'price': 11.99
            },
            {
                'title': 'The Hobbit',
                'author': 'J.R.R. Tolkien',
                'description': 'A fantasy novel about the adventures of Bilbo Baggins.',
                'price': 16.99
            },
            {
                'title': 'Harry Potter and the Sorcerer\'s Stone',
                'author': 'J.K. Rowling',
                'description': 'The first book in the Harry Potter series about a young wizard.',
                'price': 19.99
            },
            {
                'title': 'The Catcher in the Rye',
                'author': 'J.D. Salinger',
                'description': 'A story of teenage alienation and loss of innocence in America.',
                'price': 13.99
            },
            {
                'title': 'The Da Vinci Code',
                'author': 'Dan Brown',
                'description': 'A mystery thriller following symbologist Robert Langdon.',
                'price': 15.99
            },
            {
                'title': 'The Alchemist',
                'author': 'Paulo Coelho',
                'description': 'A philosophical story about a shepherd boy searching for treasure.',
                'price': 12.99
            },
            {
                'title': 'Lord of the Flies',
                'author': 'William Golding',
                'description': 'A novel about a group of British boys stuck on an uninhabited island.',
                'price': 11.99
            },
            {
                'title': 'The Hunger Games',
                'author': 'Suzanne Collins',
                'description': 'A dystopian novel about annual games where teenagers fight to the death.',
                'price': 14.99
            },
            {
                'title': 'The Road',
                'author': 'Cormac McCarthy',
                'description': 'A post-apocalyptic tale of a journey of a father and his young son.',
                'price': 13.99
            },
            {
                'title': 'One Hundred Years of Solitude',
                'author': 'Gabriel García Márquez',
                'description': 'A multi-generational story of the Buendía family in the fictional town of Macondo.',
                'price': 16.99
            },
            {
                'title': 'Brave New World',
                'author': 'Aldous Huxley',
                'description': 'A dystopian novel set in a futuristic World State of genetically modified citizens.',
                'price': 12.99
            },
            {
                'title': 'The Little Prince',
                'author': 'Antoine de Saint-Exupéry',
                'description': 'A poetic tale about a young prince who visits various planets.',
                'price': 10.99
            },
            {
                'title': 'Crime and Punishment',
                'author': 'Fyodor Dostoevsky',
                'description': 'A novel about the mental anguish and moral dilemmas of a poor ex-student.',
                'price': 15.99
            },
            {
                'title': 'The Picture of Dorian Gray',
                'author': 'Oscar Wilde',
                'description': 'A philosophical novel about a man who sells his soul for eternal youth.',
                'price': 13.99
            },
            {
                'title': 'Alice\'s Adventures in Wonderland',
                'author': 'Lewis Carroll',
                'description': 'A fantasy novel about a girl who falls through a rabbit hole into a fantasy world.',
                'price': 11.99
            },
            {
                'title': 'The Old Man and the Sea',
                'author': 'Ernest Hemingway',
                'description': 'A story about an aging Cuban fisherman who struggles with a giant marlin.',
                'price': 12.99
            },
            {
                'title': 'The Chronicles of Narnia',
                'author': 'C.S. Lewis',
                'description': 'A series of fantasy novels about the magical world of Narnia.',
                'price': 18.99
            }
        ]

        for book_data in books_data:
            book = Book.objects.create(**book_data)
            self.stdout.write(self.style.SUCCESS(f'Created book: {book.title}'))