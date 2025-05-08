import getpass as p
import hashlib

if __name__ == "__main__":
    user = input("enter your username: ")
    passwd = hashlib.sha256(p.getpass().encode()).hexdigest()

    print(user + ":" + passwd )


    #here we also practice some if's

    if user == "bob":
        print("Hello bob")
    elif user == "alice":
        print("Hello alice")
    elif user == "mallery":
        print("Hello mallery")
    else:
        print("I dont know you")
    

    if passwd == "4813494d137e1631bba301d5acab6e7bb7aa74ce1185d456565ef51d737677b2":
        print("nice password!")
    