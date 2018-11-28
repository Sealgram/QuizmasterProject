import os, time, random

os.chdir("Categories")
score = []


def start():
    print("What is your Username? (ex: 'username')")
    username = input(">>>")
    title = username
    username = username + '.txt'
    player = open(username, 'w+')
    player.write(title)
    player.write("\n")
    player.write("")
    player.write("\n")
    player.write("First attempt:")
    player.write("\n")
    player.write("Score:")
    player.write("\n")
    time.sleep(0.5)
    print("Profile Created!")
    return username


def scoresave(score):
    player = open(username, 'a')
    print("saving score...")
    time.sleep(0.5)
    player.write(score)
    player.write("\n")
    time.sleep(1)
    return username


def username():
    while 0 == 0:
        print("What is your Username you previously saved under? (ex: 'username')")
        username = input(">>>")
        username = username + '.txt'
        try:
            open(username, 'r')
            print("Profile Opened!")
            existingprofile(username)
            break
        except OSError:
            print("That profile does not exist!")
            choice = input("Would you like to try again, or create a new profile? ('try', 'new') ")
            if choice.lower() == 'try':
                continue
            elif choice.lower() == 'new':
                print("")
                start()
                break
    return username


def existingprofile(username):
    player = open(username, 'a')
    player.write("\n")
    player.write("Next Attempt:")
    player.write("\n")
    player.write("Score:")
    player.write("\n")


def categoryselect(categorychoice):
    if categorychoice == 'Category 1':
        categorychoice = 'Video Games'
    elif categorychoice == 'Category 2':
        categorychoice = 'Computer Building'
    elif categorychoice == 'Category 3':
        categorychoice = 'The Great Outdoors of Ontario'
    elif categorychoice == 'Category 4':
        categorychoice = 'Toronto'
    elif categorychoice == 'Category 5':
        categorychoice = 'Game of Thrones'
    categories = ['Video Games', 'Computer Building', 'The Great Outdoors of Ontario', 'Toronto', 'Game of Thrones']
    random.shuffle(categories)
    if categorychoice != 0:
        categories.remove(categorychoice)
    y = random.randint(0, len(categories) - 1)
    category = categories[y]
    print("")
    print("Here is the category whose questions you will be answering!")
    print(category)
    print("")
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


def category(categorychoice):
    categorychoice1 = categoryselect(categorychoice)
    category = open(categorychoice1, "r")
    line = category.readlines()
    questions = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
    while 0 == 0:
        y = random.choice(questions)
        questions.remove(y)
        print("")
        print("Asking Question...")
        print(line[y])
        print("Input your Answer: ")
        PlayerResponse1 = input(">>>")
        y = y + 1
        if PlayerResponse1.title() == line[y].strip():
            print("You are Correct!")
            print("")
            score.append(1)
        elif PlayerResponse1.title() != line[y].strip():
            print("That is wrong!")
            print("")
        if len(questions) == 5:
            break
    time.sleep(1)
    print("End of Category.")
    print("")
    time.sleep(1)
    print("Here is your total score:")
    print(sum(score))
    return categorychoice1


def intro():
    print("")
    print("Welcome to the Quizmaster Python Game!")
    time.sleep(0.3)
    print(" _______          _________ _______  _______  _______  _______ _________ _______  _______ ")
    time.sleep(0.3)
    print("(  ___  )|\     /|\__   __// ___   )(       )(  ___  )(  ____ ||__   __|(  ____ \(  ____ )")
    time.sleep(0.3)
    print("| (   ) || )   ( |   ) (   \/   )  || () () || (   ) || (    \/   ) (   | (    \/| (    )|")
    time.sleep(0.3)
    print("| |   | || |   | |   | |       /   )| || || || (___) || (_____    | |   | (__    | (____)|")
    time.sleep(0.3)
    print("| |   | || |   | |   | |      /   / | |(_)| ||  ___  |(_____  )   | |   |  __)   |     __)")
    time.sleep(0.3)
    print("| | /\| || |   | |   | |     /   /  | |   | || (   ) |      ) |   | |   | (      | (\ (   ")
    time.sleep(0.3)
    print("| (_\ \ || (___) |___) (___ /   (_/\| )   ( || )   ( |/\____) |   | |   | (____/\| ) \ \__")
    time.sleep(0.3)
    print("(____\/_)(_______)\_______/(_______/|/     \||/     \|\_______)   )_(   (_______/|/   \__/")
    time.sleep(0.3)
    print("")
    print("This is a quiz game. 2 Categories will be randomly selected, and you will answer five questions from each.")
    print("Do not use any punctuation in your answers. Your answers are not case sensitive.")
    print("")

intro()
time.sleep(1)
print("Do you Have a Previous Profile you would like to add to, or would you like to make a new one?? ('add', 'new') ")
while 0 == 0:
    profile = input(">>>")
    if profile.title() == 'Add':
        username = username()
        break
    elif profile.title() == 'New':
        username = start()
        break
    elif profile.title() != 'Add' or 'New':
        print("That is not an option!")
        time.sleep(0.5)
        continue
time.sleep(1)
print("Starting Game...")
print("")
categorychoice = 0
categorychoice1 = category(categorychoice)
categorychoice = categorychoice1
print("")
time.sleep(1)
category(categorychoice)
print("")
time.sleep(1)
print("You have answered 2 Categories!")
print("Here is your score!")
print(sum(score))
save = input("Would you like to save your score? ('yes', 'no') ")
if save.title() == 'Yes':
    scoresave(str(sum(score)))
elif save.title() == 'No':
    os.remove(username)
    print("Score Deleted!")
time.sleep(1)
print("")
print("Thanks for Playing!")
