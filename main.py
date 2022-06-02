class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks
    
    # Function to display all the books in the Library
    def displaybooks(self):
        for book in self.books:
            print("\t", "*",book)

    # Function to borrow book from library
    def borrowbook(self, bookname):
        if bookname in self.books:
            print(f"You have been issued a {bookname} book. Please return within 30 Days: ")
            self.books.remove(bookname)
            return True
        else:
            print("Sorry! This book is already issued, please wait until it returned")
            return False

    # Function to return book to Library

    def returnbook(self, bookname):
        self.books.append(bookname)
        print(f"Thanks for returning {bookname} book. Hope you enjoyed reading this ")

    

class Student:
    # function to request to borrow book from Library
    def requestborrowbook(self):
        self.borrowbook = input("Enter the Name of the book to Borrow: ")
        return self.borrowbook

    def returnbook(self):
        self.returnbook = input("Enter the Name of the book to Return: ")
        return self.returnbook


if __name__ == "__main__":

    library = Library(["Python", "Django", "Mysql", "Alogriths", "PHP"])
    # library.displaybooks()
    student = Student()

while(True):
    welcomemsg = '''================= Welcome to Library =====================
    please select an option
    1> Display all Books
    2> Borrow a Book
    3> Return a Book
    4> Exit
    '''
    print(welcomemsg)
    user = int(input("Enter a Choice : "))

    try:
        if user == 1:
            print("Books available are: ")
            library.displaybooks()
        elif user ==2:
            library.borrowbook(student.requestborrowbook())
        elif user ==3:
            library.returnbook(student.returnbook())

        elif user ==4:
            print("Thank you for using Library")
            exit()

    except ValueError:
        print("Choose from options only")
        

