class Book:
    def __init__(self, bookid, title, author):
        self.bookid = bookid
        self.title = title
        self.author = author
        self.is_available = True

  #Get book details
    def get_details(self):
        return f"Book name is {self.title} by {self.author} (ID: {self.bookid})"
    
    
    #Convert book details to dictionary
    def to_dict(self):
        book={}
        book['bookid'] = self.bookid
        book['title'] = self.title
        book['author'] = self.author
        book['is_available'] = self.is_available
        return book