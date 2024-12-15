class library:
    def __init__(self, name,list):
        self.name = name
        self.booklist = list
        self.lenDict={}

    def displayBooks(self):
        print(f"we have following books in our library:{self.name}")
        for book in self.booklist:
            print(book)

    def lendBook(self,user,book):
        if book in self.booklist:
            if book not in self.lenDict.keys():
                self.lenDict.update({book:user})
            print("lender-book database has been updated.you can take the book now.")
        else:
            print(f"book is already being used by {self.lenDict[book]}")
    def addBook(self,book):
        self.booklist.append(book)
        print("book has been added successfully")

    def returnBook(self,book):
       self.lenDict.pop(book)
if __name__ == '__main__':
    books =library(['python','rich dad poor dad','harrypotter','c++','algorithms byclrs'],"let's upskill")

    while True:
        print(f"welcome to the {books.name}library.enter your choice to continue")
        print("1.display books")
        print("2.lend book")
        print("3.add book")
        print("4.return book")
        user_choice =input("enter your choice:")
        if user_choice not in ["1","2","3","4"]:
            print("invalid choice")
            continue
        else:
            user_choice = int(user_choice)
            if user_choice == 1:
                books.displayBooks()
            elif user_choice == 2:
                user = input("enter your name:")
                book = input("enter the book you want to lend:")
                books.lendBook(user,book)
            elif user_choice == 3:
                book = input("enter the book you want to add:")
                books.addBook(book)
            elif user_choice == 4:
                book = input("enter the book you want to return:")
                books.returnBook(book)
            else:
                print("not valid option")
            print("press q to quit and c to continue")
            user_choice2 = ""
            while user_choice2!="c" and user_choice2!="q":
                user_choice2 = input()
                if user_choice2 == "q":
                     exit()
                elif user_choice2 == "c":
                        continue