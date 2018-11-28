import os
os.chdir("Categories")
while 0 == 0:
    try:
        username = input("What is the username of the profile you would like to delete? ")
        username = username + ".txt"
        os.remove(username)
    except OSError:
        print("That file does not exist!")
        continue
    else:
        break
print("File Deleted")
