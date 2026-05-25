class Book:
    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages
b1=Book("Flamingo","James Bond",97)
print(b1.title,b1.author,b1.pages)
