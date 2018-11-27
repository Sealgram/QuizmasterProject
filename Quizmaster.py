import os, time, random

os.chdir("Categories")
def start():
    print("What is your Username? (ex: 'username.txt')")
    username = input(">>>")
    username = username + '.txt'
    player = open(username, 'w+')
    player.write(username)
    player.write("\n")
    player.write("Score:")
    player.write("\n")
    print("Profile Created!")
    print("")
    time.sleep(1)
    return username


def categoryselect():
    categories = ['Video Games', 'Computer Building', 'The Great Outdoors of Ontario', 'Toronto', 'Game of Thrones']
    random.shuffle(categories)
    y = random.randint(0, 4)
    category = categories[y]
    print("Here is the category whose questions you will be answering!")
    print(category)
    if category == 'Video Games':
        category = 'Category 1'
    elif category == 'Computer Building':
        category = 'Category 2'
    elif category == 'The Great Outdoors of Ontario':
        category = 'Category 3'
    elif category == 'Toronto':
        category = 'Category 4'
    elif category == 'Game of Thrones':
        category = 'Category 5'
    return category


def category1(username):
    category = open("Category 1", "r")
    line = category.readlines()
    player = open(username, 'a+')
    questions = [3, 5, 7, 9, 11]
    while 0 == 0:
        y = random.choice(questions)
        print("Here is the first question...")
        print(line[y])
        print("Input your Answer: ")
        PlayerResponse1 = input(">>>")
        y = y + 1
        if PlayerResponse1.lower() == line[y].strip():
            print("You are Correct!")
            print("")
            player.write("+1 Point\n")
            break
        elif PlayerResponse1.lower() != line[y].strip():
            print("That is wrong!")
            print("")
            break
    while 0 == 0:
        y = y - 1
        questions.remove(y)
        y = random.choice(questions)
        print("Here is the second question...")
        print(line[y])
        print("Input your Answer: ")
        PlayerResponse2 = input(">>>")
        y = y + 1
        if PlayerResponse2.lower() == line[y].strip():
            print("You are Correct!")
            print("")
            player.write("+1 Point\n")
            break
        elif PlayerResponse2.lower() != line[y].strip():
            print("That is wrong!")
            print("")
            break
    while 0 == 0:
        y = y - 1
        questions.remove(y)
        y = random.choice(questions)
        print("Here is the third question...")
        print(line[y])
        print("Input your Answer: ")
        PlayerResponse3 = input(">>>")
        y = y + 1
        if PlayerResponse3.lower() == line[y].strip():
            print("You are Correct!")
            print("")
            player.write("+1 Point\n")
            break
        elif PlayerResponse3.lower() != line[y].strip():
            print("That is wrong!")
            print("")
            break
    time.sleep(1)
    while 0 == 0:
        y = y - 1
        questions.remove(y)
        y = random.choice(questions)
        print("Here is the fourth question...")
        print(line[y])
        print("Input your Answer: ")
        PlayerResponse4 = input(">>>")
        y = y + 1
        if PlayerResponse4.lower() == line[y].strip():
            print("You are Correct!")
            print("")
            player.write("+1 Point\n")
            break
        elif PlayerResponse4.lower() != line[y].strip():
            print("That is wrong!")
            print("")
            break
    time.sleep(1)
    while 0 == 0:
        y = y - 1
        questions.remove(y)
        y = random.choice(questions)
        print("Here is the fifth question...")
        print(line[y])
        print("Input your Answer: ")
        PlayerResponse5 = input(">>>")
        y = y + 1
        if PlayerResponse5.lower() == line[y].strip():
            print("You are Correct!")
            print("")
            player.write("+1 Point\n")
            break
        elif PlayerResponse5.lower() != line[y].strip():
            print("That is wrong!")
            print("")
            break
    time.sleep(1)
    print("End of Category 1.")
    print("")
    time.sleep(1)
    print("Here is your total score, including Category 1:")
    player = open(username, 'r')
    playerline = player.readlines()
    print(playerline)


def category2(username):
    category = open("Category 2", "r")
    line = category.readlines()
    player = open(username, 'a+')
    questions = [3, 5, 7, 9, 11]
    while 0 == 0:
        y = random.choice(questions)
        print("Here is the first question...")
        print(line[y])
        print("Input your Answer: ")
        PlayerResponse1 = input(">>>")
        y = y + 1
        if PlayerResponse1.lower() == line[y].strip():
            print("You are Correct!")
            print("")
            player.write("+1 Point\n")
            break
        elif PlayerResponse1.lower() != line[y].strip():
            print("That is wrong!")
            print("")
            break
    while 0 == 0:
        y = y - 1
        questions.remove(y)
        y = random.choice(questions)
        print("Here is the second question...")
        print(line[y])
        print("Input your Answer: ")
        PlayerResponse2 = input(">>>")
        y = y + 1
        if PlayerResponse2.lower() == line[y].strip():
            print("You are Correct!")
            print("")
            player.write("+1 Point\n")
            break
        elif PlayerResponse2.lower() != line[y].strip():
            print("That is wrong!")
            print("")
            break
    while 0 == 0:
        y = y - 1
        questions.remove(y)
        y = random.choice(questions)
        print("Here is the third question...")
        print(line[y])
        print("Input your Answer: ")
        PlayerResponse3 = input(">>>")
        y = y + 1
        if PlayerResponse3.lower() == line[y].strip():
            print("You are Correct!")
            print("")
            player.write("+1 Point\n")
            break
        elif PlayerResponse3.lower() != line[y].strip():
            print("That is wrong!")
            print("")
            break
    time.sleep(1)
    while 0 == 0:
        y = y - 1
        questions.remove(y)
        y = random.choice(questions)
        print("Here is the fourth question...")
        print(line[y])
        print("Input your Answer: ")
        PlayerResponse4 = input(">>>")
        y = y + 1
        if PlayerResponse4.lower() == line[y].strip():
            print("You are Correct!")
            print("")
            player.write("+1 Point\n")
            break
        elif PlayerResponse4.lower() != line[y].strip():
            print("That is wrong!")
            print("")
            break
    time.sleep(1)
    while 0 == 0:
        y = y - 1
        questions.remove(y)
        y = random.choice(questions)
        print("Here is the fifth question...")
        print(line[y])
        print("Input your Answer: ")
        PlayerResponse5 = input(">>>")
        y = y + 1
        if PlayerResponse5.lower() == line[y].strip():
            print("You are Correct!")
            print("")
            player.write("+1 Point\n")
            break
        elif PlayerResponse5.lower() != line[y].strip():
            print("That is wrong!")
            print("")
            break
    time.sleep(1)
    print("End of Category 2.")
    print("")
    time.sleep(1)
    print("Here is your total score, including category 2:")
    player = open(username, 'r')
    playerline = player.readlines()
    print(playerline)


def category3(username):
    category = open("Category 3", "r")
    line = category.readlines()
    player = open(username, 'a+')
    questions = [3, 5, 7, 9, 11]
    while 0 == 0:
        y = random.choice(questions)
        print("Here is the first question...")
        print(line[y])
        print("Input your Answer: ")
        PlayerResponse1 = input(">>>")
        y = y + 1
        if PlayerResponse1.lower() == line[y].strip():
            print("You are Correct!")
            print("")
            player.write("+1 Point\n")
            break
        elif PlayerResponse1.lower() != line[y].strip():
            print("That is wrong!")
            print("")
            break
    while 0 == 0:
        y = y - 1
        questions.remove(y)
        y = random.choice(questions)
        print("Here is the second question...")
        print(line[y])
        print("Input your Answer: ")
        PlayerResponse2 = input(">>>")
        y = y + 1
        if PlayerResponse2.lower() == line[y].strip():
            print("You are Correct!")
            print("")
            player.write("+1 Point\n")
            break
        elif PlayerResponse2.lower() != line[y].strip():
            print("That is wrong!")
            print("")
            break
    while 0 == 0:
        y = y - 1
        questions.remove(y)
        y = random.choice(questions)
        print("Here is the third question...")
        print(line[y])
        print("Input your Answer: ")
        PlayerResponse3 = input(">>>")
        y = y + 1
        if PlayerResponse3.lower() == line[y].strip():
            print("You are Correct!")
            print("")
            player.write("+1 Point\n")
            break
        elif PlayerResponse3.lower() != line[y].strip():
            print("That is wrong!")
            print("")
            break
    time.sleep(1)
    while 0 == 0:
        y = y - 1
        questions.remove(y)
        y = random.choice(questions)
        print("Here is the fourth question...")
        print(line[y])
        print("Input your Answer: ")
        PlayerResponse4 = input(">>>")
        y = y + 1
        if PlayerResponse4.lower() == line[y].strip():
            print("You are Correct!")
            print("")
            player.write("+1 Point\n")
            break
        elif PlayerResponse4.lower() != line[y].strip():
            print("That is wrong!")
            print("")
            break
    time.sleep(1)
    while 0 == 0:
        y = y - 1
        questions.remove(y)
        y = random.choice(questions)
        print("Here is the fifth question...")
        print(line[y])
        print("Input your Answer: ")
        PlayerResponse5 = input(">>>")
        y = y + 1
        if PlayerResponse5.lower() == line[y].strip():
            print("You are Correct!")
            print("")
            player.write("+1 Point\n")
            break
        elif PlayerResponse5.lower() != line[y].strip():
            print("That is wrong!")
            print("")
            break
    time.sleep(1)
    print("End of Category 3.")
    print("")
    time.sleep(1)
    print("Here is your total score, including category 3:")
    player = open(username, 'r')
    playerline = player.readlines()
    print(playerline)


def category4(username):
    category = open("Category 4", "r")
    line = category.readlines()
    player = open(username, 'a+')
    questions = [3, 5, 7, 9, 11]
    while 0 == 0:
        y = random.choice(questions)
        print("Here is the first question...")
        print(line[y])
        print("Input your Answer: ")
        PlayerResponse1 = input(">>>")
        y = y + 1
        if PlayerResponse1.lower() == line[y].strip():
            print("You are Correct!")
            print("")
            player.write("+1 Point\n")
            break
        elif PlayerResponse1.lower() != line[y].strip():
            print("That is wrong!")
            print("")
            break
    while 0 == 0:
        y = y - 1
        questions.remove(y)
        y = random.choice(questions)
        print("Here is the second question...")
        print(line[y])
        print("Input your Answer: ")
        PlayerResponse2 = input(">>>")
        y = y + 1
        if PlayerResponse2.lower() == line[y].strip():
            print("You are Correct!")
            print("")
            player.write("+1 Point\n")
            break
        elif PlayerResponse2.lower() != line[y].strip():
            print("That is wrong!")
            print("")
            break
    while 0 == 0:
        y = y - 1
        questions.remove(y)
        y = random.choice(questions)
        print("Here is the third question...")
        print(line[y])
        print("Input your Answer: ")
        PlayerResponse3 = input(">>>")
        y = y + 1
        if PlayerResponse3.lower() == line[y].strip():
            print("You are Correct!")
            print("")
            player.write("+1 Point\n")
            break
        elif PlayerResponse3.lower() != line[y].strip():
            print("That is wrong!")
            print("")
            break
    time.sleep(1)
    while 0 == 0:
        y = y - 1
        questions.remove(y)
        y = random.choice(questions)
        print("Here is the fourth question...")
        print(line[y])
        print("Input your Answer: ")
        PlayerResponse4 = input(">>>")
        y = y + 1
        if PlayerResponse4.lower() == line[y].strip():
            print("You are Correct!")
            print("")
            player.write("+1 Point\n")
            break
        elif PlayerResponse4.lower() != line[y].strip():
            print("That is wrong!")
            print("")
            break
    time.sleep(1)
    while 0 == 0:
        y = y - 1
        questions.remove(y)
        y = random.choice(questions)
        print("Here is the fifth question...")
        print(line[y])
        print("Input your Answer: ")
        PlayerResponse5 = input(">>>")
        y = y + 1
        if PlayerResponse5.lower() == line[y].strip():
            print("You are Correct!")
            print("")
            player.write("+1 Point\n")
            break
        elif PlayerResponse5.lower() != line[y].strip():
            print("That is wrong!")
            print("")
            break
    time.sleep(1)
    print("End of Category 4.")
    print("")
    time.sleep(1)
    print("Here is your total score, including category 4:")
    player = open(username, 'r')
    playerline = player.readlines()
    print(playerline)


def category5(username):
    category = open("Category 5", "r")
    line = category.readlines()
    player = open(username, 'a+')
    questions = [3, 5, 7, 9, 11]
    while 0 == 0:
        y = random.choice(questions)
        print("Here is the first question...")
        print(line[y])
        print("Input your Answer: ")
        PlayerResponse1 = input(">>>")
        y = y + 1
        if PlayerResponse1.lower() == line[y].strip():
            print("You are Correct!")
            print("")
            player.write("+1 Point\n")
            break
        elif PlayerResponse1.lower() != line[y].strip():
            print("That is wrong!")
            print("")
            break
    while 0 == 0:
        y = y - 1
        questions.remove(y)
        y = random.choice(questions)
        print("Here is the second question...")
        print(line[y])
        print("Input your Answer: ")
        PlayerResponse2 = input(">>>")
        y = y + 1
        if PlayerResponse2.lower() == line[y].strip():
            print("You are Correct!")
            print("")
            player.write("+1 Point\n")
            break
        elif PlayerResponse2.lower() != line[y].strip():
            print("That is wrong!")
            print("")
            break
    while 0 == 0:
        y = y - 1
        questions.remove(y)
        y = random.choice(questions)
        print("Here is the third question...")
        print(line[y])
        print("Input your Answer: ")
        PlayerResponse3 = input(">>>")
        y = y + 1
        if PlayerResponse3.lower() == line[y].strip():
            print("You are Correct!")
            print("")
            player.write("+1 Point\n")
            break
        elif PlayerResponse3.lower() != line[y].strip():
            print("That is wrong!")
            print("")
            break
    time.sleep(1)
    while 0 == 0:
        y = y - 1
        questions.remove(y)
        y = random.choice(questions)
        print("Here is the fourth question...")
        print(line[y])
        print("Input your Answer: ")
        PlayerResponse4 = input(">>>")
        y = y + 1
        if PlayerResponse4.lower() == line[y].strip():
            print("You are Correct!")
            print("")
            player.write("+1 Point\n")
            break
        elif PlayerResponse4.lower() != line[y].strip():
            print("That is wrong!")
            print("")
            break
    time.sleep(1)
    while 0 == 0:
        y = y - 1
        questions.remove(y)
        y = random.choice(questions)
        print("Here is the fifth question...")
        print(line[y])
        print("Input your Answer: ")
        PlayerResponse5 = input(">>>")
        y = y + 1
        if PlayerResponse5.lower() == line[y].strip():
            print("You are Correct!")
            print("")
            player.write("+1 Point\n")
            break
        elif PlayerResponse5.lower() != line[y].strip():
            print("That is wrong!")
            print("")
            break
    time.sleep(1)
    print("End of Category 5.")
    print("")
    time.sleep(1)
    print("Here is your total score, including category 5:")
    player = open(username, 'r')
    playerline = player.readlines()
    print(playerline)


print("")