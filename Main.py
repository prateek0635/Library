class library():
    def __init__(self,name,list):
        self.list=list
        self.name=name
    def Display_Books(self):
        for i in self.list:
            print(i)
    def issue(self,book_name,dic):
        if book_name in dic:
            print(f"Book Already Has been issued to {dic[book_name]} ")
            return 0
        else:
            return {book_name:self.name}
    def Return_Book(self,book_name1,dic):
        if book_name1 in dic:
            print(f"Hello {dic[book_name1]} Your book {book_name1} has been returned")
            return book_name1
        else:
            print(f"Book {book_name1} is not issued")
            return 0
    def Add_book(self,Book_1):
        with open("Book_List.txt",'a') as p:
            p.write(Book_1)



if __name__=="__main__":
    list=[]
    dic={}
    Auth={"Ram":1234,"Shayam":4321}
    print("**************************************************************************")
    print("National Institue of Technology , Patna")
    print("==========================================================================")
    with open('Book_List.txt') as op:
        for i in op.readlines():
            list.append(i)
    Name=input("Please Enter you Good name : ")
    #print(f"Welcome {Name} to the central library of NIT Patna")
    Central_Library=library(Name,list)
    while True:

        print("**************************************************************************")
        print(f"Welcome {Name} to the central library of NIT Patna")
        print("==========================================================================")
        n=int(input("Enter 0 to exit \n Enter 1 for the Display the all book \n Enter 2 for issue the book\n"
                    "Enter 3 to return the book\nEnter 4 to donate a book\n"))
        if n==1:
            Central_Library.Display_Books()
        elif n==2:
            Book_name = input("Enter the book name: ").lower()
            n=Central_Library.issue(Book_name,dic)
            if n!=0:
                dic.update(n)
            print(dic)
        elif n==0:
            exit()
        elif n==3:
            Book_name1=input("Enter the name of book to be return : ")
            k=Central_Library.Return_Book(Book_name1,dic)
            if k!=0:
                del dic[k]
                print(dic)
        elif n==4:
            l=input("Enter the name of you want to Add in this section : ").lower()
            Id=input("Enter Your Authorised ID")
            Pasw=int(input("Enter Your pasword"))
            if Auth[Id]==Pasw:
                Central_Library.Add_book(l)
                print("Book Added succesfully")
            else:
                print("Wrong Pasword")





