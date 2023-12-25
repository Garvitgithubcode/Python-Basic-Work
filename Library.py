# A library collection of books
class library:
    def showinfo1(self):
        if input1 == "book":
            print(f"The library has {len(books)} books. The books are\n")
            for book in books:
                print(book)

        elif input1 == "biopic":
            print(f"The library has {len(biopics)} books. The books are\n")
            for biopic in biopics:
                print(biopic)

        elif input1 == "adventure":
            print(f"The library has {len(adventures)} books. The books are\n")
            for adventure in adventures:
                print(adventure)

l1=library()
books=library()
biopics=library()
adventures=library()
book=["The Little Engine That Could" ,"Franklin Rides a Bike","Horton Hatches an Egg"]
biopic=['Leonardo da Vinci','Steve Jobs','The Immortal Life of Henrietta Lacks','The Rise of Theodore Roosevelt','The Autobiography of Malcolm X']
adventure=['Into Thin Air','The Lost City of Z','Wild','The River of Doubt','The Snow Leopard']
books=book
biopics=biopic
adventures=adventure
print(f"Hey, We have 3 section in our library\n1. biopics\n2. Adventures\n3. Books")
input1=input("Which section would you like to choose:- ")
if input1=="book":
    l1.showinfo1()
    a=input("\nSo, Which one you choose : ")
    print(f"Here's your book--> {a}")
elif input1=="biopic":
    l1.showinfo1()
    b = input("\nSo, Which one you choose : ")
    print(f"Here's your book--> {b}")
elif input1=="adventure":
    l1.showinfo1()
    c = input("\nSo, Which one you choose : ")
    print(f"Here's your book--> {c}")
else:
    print("Invalid input")
input2=input("You want to add any book name in our library: ")
if input2=="yes":
    d=input("In which section : ")
    e=input("Type book name: ")
    nbook = book
    nbook.append(e)
    print(f"Thanks for suggestion\nWe added your book in our {d} section\nThank you for visit\nHave a nice day ")
elif input2=="no":
    print("Thanks for giving your precious time\nHave a nice day")
else:
    print("Invalid input\nThank you for visit")

