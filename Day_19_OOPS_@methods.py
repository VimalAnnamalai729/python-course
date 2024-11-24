# class method

class Book:
    total_books = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.total_books += 1

    @classmethod
    def from_string(cls, book_info):
        book_name, author = book_info.split('-')
        return cls(book_name, author) # Book(book-name, author)

    @classmethod
    def from_pdf(cls, pdf_data):
        book_name, author = pdf_data.split('-')
        return cls(book_name, author)

    @classmethod
    def from_csv(cls, csv_data):
        book_name, author = csv_data['data'].split('-')
        return cls(book_name, author)

    @staticmethod
    def input_formatter(input_data):
        if input_data['format'] == 'PDF':
            book_obj = Book.from_pdf(input_data)
        elif input_data['format'] == 'csv':
            book_obj = Book.from_csv(input_data)
        elif isinstance(input_data['data'], str):
            book_obj = Book.from_string(input_data)
        else:
            book_name, author = input_data.split()
            book_obj = Book(book_name, author)
        return book_obj




# class Filewrapper:
#     def __init__(self, filename):
#         name, format = os.path.split(filename)
#         file_data = open(filename, 'r')



book1 = Book('Secret', 'XXYXYX')
book2 = Book('Book2', 'HINON')
book3 = Book.from_string('THE NEW BOOK- GRTTY')
book4 = Book.input_formatter({'data': 'THE NEW BOOK-HILY', 'format' : 'csv'})
print(book3)