                       #---LIBRARY MANAGEMENT SYSTEM -----

# note :- Create list_of_books2.txt file 


import datetime
import os
os.getcwd()

class lms:
    

    def __init__(self, list_of_books, library_name):
        self.list_of_books = "list_of_books2.txt"
        self.library_name = library_name
        self.books_dict = {}
        id = 101
        with open(self.list_of_books) as b:
            content = b.readlines()
        for line in content:
            self.books_dict.update({str(id):{'books_title':line.replace("\n",""),'lender_name':'','lend_date':'', 'status':'Available'}})
            id += 1    

    def display(self):
        print("------------------------List of Books---------------------")
        print("Books ID","\t", "Title")
        print("----------------------------------------------------------")
        for key, value in self.books_dict.items():
            print(key,"\t\t", value.get("books_title"), "- [", value.get("status"),"]")

    def issue(self):
        ID = input("Enter Books ID : ")
        current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if ID in self.books_dict.keys():
            if not self.books_dict[ID]['status'] == 'Available':
                print(f"This book is already issued to {self.books_dict[ID]['lender_name']} on {self.books_dict[ID]['lend_date']}")
                
            elif self.books_dict[ID]['status'] == 'Available':
                your_name = input("Enter Your Name : ")
                self.books_dict[ID]['lender_name'] = your_name
                self.books_dict[ID]['lend_date'] = current_date
                self.books_dict[ID]['status']= 'Already Issued'
                print("Book Issued Successfully !!!\n")
        else:
            print("Book ID Not Found !!!")
            return self.issue()

    def add(self):
        New_books = input("Enter Books Title : ")
        if New_books == "":
            return self.add()
        elif len(New_books) > 20:
            print("Books title length is too long !!! Title length limit is 20 characters")
            return self.add()
        else:
            with open(self.list_of_books, "a") as b:
                b.writelines(f"{New_books}\n")
            self.books_dict.update({str(int(max(self.books_dict))+1):{'books_title':New_books,'lender_name':'','lend_date':'', 'status':'Available'}})
            print(f"The books '{New_books}' has been added successfully !!!")

    def ret_book(self):
        ID = input("Enter Books ID : ")
        if ID in self.books_dict.keys():
            if self.books_dict[ID]['status'] == 'Available':
                print("This book is already available in library. Please check book id. !!! ")
                return self.ret_book()
            elif not self.books_dict[ID]['status'] == 'Available':
                self.books_dict[ID]['lender_name'] = ''
                self.books_dict[ID]['lend_date'] = ''
                self.books_dict[ID]['status']= 'Available'
                print("Successfully Updated !!!\n")
        else:
            print("Book ID Not Found !!!")

if __name__ == "__main__":
    try:
        mylms = lms("list_of_books.txt", "Python's") 
        press_key_list = {"D": "Display Books", "I": "Issue Books", "A": "Add Books", "R": "Return Books", "Q": "Quit"}    
        
        key_press = False
        while not (key_press == "q"):
            print(f"\n----------Welcome To {mylms.library_name}'s Library Management System---------\n")
            for key, value in press_key_list.items():
                print("Press", key, "To", value)
            key_press = input("Press Key : ").lower()
            if key_press == "i":
                print("\nCurrent Selection : ISSUE BOOK\n")
                mylms.issue()
                
            elif key_press == "a":
                print("\nCurrent Selection : ADD BOOK\n")
                mylms.add()

            elif key_press == "d":
                print("\nCurrent Selection : DISPLAY BOOKS\n")
                mylms.display()
            
            elif key_press == "r":
                print("\nCurrent Selection : RETURN BOOK\n")
                mylms.ret_book()
            elif key_press == "q":
                break
            else:
                continue
    except Exception as e:
        print("Something went wrong. Please check . !!!")
  
