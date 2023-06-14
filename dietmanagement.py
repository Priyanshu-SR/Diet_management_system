def getTime():
    import datetime
    return datetime.datetime.now()


def log():
    print("What do you want to lock\npress\n1)diet\n2)exercise")
    j = int(input())
    if (j == 1):
        print("Give your file a name")
        x = getTime()
        name = input()
        print("Enter the clients name")
        try:
            with open(name, "x") as f:
                pass
        except Exception as e:
            pass
        f = open(name, "r+")
        f.write(str(x) + " " + input())
        f.close()

        f = open(name, "a+")
        print("Enter the diet you have consumed")
        f.write("\n" + input())
        f.close()

        f = open(name, "r+")
        print(f.read())
        f.close()

    elif (j == 2):
        print("Give your file a name")
        x = getTime()
        name = input()
        print("Enter the clients name")
        try:
            with open(name, "x") as f:
                pass
        except Exception as e:
            pass
        f = open(name, "r+")
        f.write(str(x)+" "+input())
        f.close()

        f = open(name, "a+")
        print("Also enter the exercise you have done")
        f.write("\n" + input())
        f.close()

        f = open(name, "r+")
        print(f.read())
        f.close()

    else:
        print("Invalid selection")
        exit()


def retrieve():
    print("Enter the file name")
    name = input()
    with open(name) as f:
        print(f.read())


print("Do you want to lock the information or retrive it ?\npress \n1)Lock \n2)Retrive")
i = int(input())
if (i == 1):
    log()
elif (i == 2):
    retrieve()
else:
    print("Invalid selection")