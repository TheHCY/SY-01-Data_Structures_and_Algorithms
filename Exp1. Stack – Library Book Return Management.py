#Stack – Library Book Return Management. Implement a stack to manage returned books with Push (Return Book), Pop (Arrange Book), Peek (Top Book), and Display operations. 

stack = []
while True:
    print("\n1. Return Book (push)")
    print("2. Arrange Book (pop)")
    print("3. Top Book (peek)")
    print("4. Exit\n")

    choice = int(input("Enter number according to your Choice "))

    if choice == 1:
        book = input("Enter Book name: ")
        stack.append(book)

    elif choice == 2:
        if stack:
            print("Arrange Book :", stack.pop())
        else:
            print("No book to arrange")

    elif choice == 3:
        if stack:
            print("Top book:", stack[-1])
        else:
            print("No book to show")

    elif choice == 4:
        break

    else:
        print("You entered wrong choice, please select again")
