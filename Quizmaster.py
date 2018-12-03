# Note that all comments are referencing the line/ lines directly above them. Block comments will tell you what they
# are referencing.
import os, time, random
# Imports functions needed in the code

score = []
# Defines score list to be used later when program is keeping track of the score.

'''
The below function, Highscores, is a system for finding and appending all of the highest scores from the game's
different created profiles into a list.
'''


def highscores():
    # This function will be called at the end of the code, to collect the high scores from created player profiles.
    highscores = []
    # Defines high scores variable to be used in function
    os.chdir('..')
    # Changes the directory back to default, so that the directory 'Profiles' can be targeted.
    profiles = os.listdir('Profiles')
    # Defines variable 'profiles' as a list of all the names of text files contained within the directory 'Profiles'.
    os.chdir('Profiles')
    # Changes the directory to 'profile' so that the text files within can be targeted.
    for x in profiles:
        # for loop that targets every value in the list 'profiles'
        profile = open(x, 'r')
        # opens each file individually in it's run through of the for loop
        line = profile.readlines()
        # defines line as a list of all the lines in the file currently being targeted by the loop
        filesize = len(line)
        # defines filesize as the number of lines in the file
        lineappend = 3
        filelength = 4
        # Defines lineappend and filelength for later use
        highscores.append(line[lineappend].strip())
        # Appends the contents of the third line in the currently targeted file to the highscores list
        while 0 == 0:
            # While loop that only has functionality if the currently targeted file has more than one score in it.
            filelength = filelength + 3
            lineappend = lineappend + 3
            # changes the filelength and lineappend values with each run through of the loop
            if filesize >= filelength:
                highscores.append(line[lineappend].strip())
                # if the filesize is greater than the filelength, appends the next score in the file to the
                # highscores list
            else:
                break
                # if the file currently targeted by the for loop only has one score in it, breaks the while loop
    highscores.sort()
    # sorts the highscores list alphabetically
    for x in highscores:
        print(x)
    # prints the highscores list out line by line nicely


'''
The below function, Start, is a function that creates a new profile based on user input when called.
'''


def start():
    print("What is your Username? (ex: 'username')")
    username = input(">>>")
    # asks the user what username they would like to call themselves, then defines it as variable 'username'.
    title = username
    # Defines the variable 'title' as username so that the user input can be used without the addition ".txt"
    username = username + '.txt'
    # Adds '.txt' to the end of username so that it can be used to create a text file
    player = open(username, 'w+')
    # creates a text file based on the user-defined username
    player.write(title)
    player.write("\n")
    player.write("")
    player.write("\n")
    player.write("First attempt:")
    player.write("\n")
    player.write(title + "'s Score: ")
    # Writes a bunch of stuff in the text file, including the player's custom username (using the variable 'title' so
    #  that the '.txt' is not included.
    time.sleep(0.5)
    print("Profile Created!")
    return username
    # informs the user that the profile has been created and returns the profile's file name to the outer scope.


'''
The below function, Scoresave, is a function that will save the score to the user's profile when called.
'''


def scoresave(score):
    player = open(username, 'a')
    # opens the player's profile in append mode
    print("saving score...")
    time.sleep(0.5)
    player.write(score)
    player.write("\n")
    time.sleep(1)
    print("")
    return username
    # saves the player's score into the player's profile text file and re-returns username


'''
The below function, username, adds functionality if the user chooses to open an existing profile and save
the score from their next play-through of the game to it.
'''


def username():
    while 0 == 0:
        # defensive programming while loop
        print("What is your Username you previously saved under? (ex: 'username')")
        username = input(">>>")
        # defines username as the name the profile has been previously saved under.
        title = username
        username = username + '.txt'
        # Adds '.txt.' to the username variable.
        try:
            open(username, 'r')
            print("Profile Opened!")
            existingprofile(username, title)
            break
            # tries to open a file based on the username inputted, and, if it works, calls the existingprofile function.
        except OSError:
            print("That profile does not exist!")
            choice = input("Would you like to try again, or create a new profile? ('try', 'new') ")
            # if the user inputs a name for a file that does not exist, asks them if they would like to try again (if
            #  they made a typo) or make a new profile.
            if choice.lower() == 'try':
                continue
                # continues the loop if the user inputs that they would like to try opening a profile again.
            elif choice.lower() == 'new':
                print("")
                start()
                break
                # if the user wants to make a new profile, calls the start() function then breaks the loop once it has
                # completed.
    return username
    # returns username again


'''
The below function, existingprofile, is a small function that writes in an  existing profile to format it properly.
'''


def existingprofile(username, title):
    player = open(username, 'a')
    player.write("\n")
    player.write("Next Attempt:")
    player.write("\n")
    player.write(title + "'s Score: ")
    # Appends lines onto the existing profile to format it properly so that another score can be appended.


'''
The below function, Categoryselect, randomly selects a category for the program to ask questions from when called.
'''


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
    # changes the name value of the parameter categorychoice so that it  can be printed to the user  properly.
    categories = ['Video Games', 'Computer Building', 'The Great Outdoors of Ontario', 'Toronto', 'Game of Thrones']
    random.shuffle(categories)
    # randomly shuffles the list fo categories
    if categorychoice != 0:
        categories.remove(categorychoice)
        # if this is the second time the function is being called, removes the category that was answered first from
        # the list of selectable categories.
    y = random.randint(0, len(categories) - 1)
    category = categories[y]
    # randomly picks a category and defines it as the variable 'category'.
    print("")
    print("Here is the category whose questions you will be answering!")
    print(category)
    print("")
    # informs the user of the category they will be playing.
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
    # redefines the named category that was selected as 'category #' to make it match the category filenames
    return category


'''
The below function, Category, contains the main function of the game, asking the player questions and answering them.
'''


def category(categorychoice):
    categorychoice1 = categoryselect(categorychoice)
    # Calls the category select function and defines it's return as  a category choice.
    category = open(categorychoice1, "r")
    # Opens the category text file that  was selected by the function 'categoryselect'
    line = category.readlines()
    # Defines 'line' as a list of the lines within the file defined as 'category'
    questions = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
    # Lists all the possible points within the list that a question can exist at
    while 0 == 0:
        # Defensive programming while for asking questions
        y = random.choice(questions)
        # Randomly selects one of the questions from the list
        questions.remove(y)
        # Removes the selected question from the list of possible future questions.
        time.sleep(1)
        print("")
        # Presentation frills
        print(line[y])
        # Prints the question that is being asked
        print("Input your Answer: ")
        playerresponse1 = input(">>>")
        # Defines 'playerresponse1' as the player's response to the asked question
        time.sleep(0.5)
        y = y + 1
        # Moves y down one line, so that it will target the answer instead of the question
        if playerresponse1.title() == line[y].strip():
            print("You are Correct!")
            print("")
            score.append(1)
            # Checks if the player's answer is correct, and appends 1 to the player's score if they are correct.
        elif playerresponse1.title() != line[y].strip():
            print("That is wrong!")
            print("")
            # Checks if the player is wrong, and if they are, informs them so.
        if len(questions) == 5:
            break
            # If 5 questions have been asked, breaks  the while loop, and continues the program.
    time.sleep(1)
    print("End of Category.")
    print("")
    time.sleep(1)
    print("Here is your total score:")
    print(sum(score))
    # Presentation frills & informing the player of their score at the end of each category
    return categorychoice1
    # returns the category choice so that it will not be selected again.


'''
The below function, Intro, contains the sequence that plays at the beginning of the code, printing 'quizmaster' in big
letters. The only reason I put it in a function is because I didn't want to look at it every time I scrolled through my
code.
'''


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


os.chdir('Profiles')
# Changes the directory to 'profiles' so that the player can create/open an existing profile.
intro()
# Plays the intro sequence
time.sleep(1)
while 0 == 0:
    # Defensive programming while loop
    print("Do you Have a Profile you would like to add to, or would you like to make a new one? ('add', 'new') ")
    # Asks the player if they would like to create or add to a profile.
    profile = input(">>>")
    if profile.title() == 'Add':
        username = username()
        break
        # If the player wants to add to a profile, calls the 'username()' function, and uses it to define 'username',
        # which will allow them to open a profile and format the next segment of the text file.
    elif profile.title() == 'New':
        username = start()
        break
        # If the player wants to create a new profile, calls the 'start()' function, (which makes a new profile and
        # formats it properly), and defines it as 'username'.
    elif profile.title() != 'Add' or 'New':
        print("That is not an option!")
        time.sleep(0.5)
        continue
        # If the player inputs something other than 'add' or 'new', tells them  that it is not an option and repeats
        # the loop.
time.sleep(1)
print("Starting Game...")
print("")
# presentation frills
os.chdir('..')
os.chdir('Categories')
# Changes the directory to 'categories', so that the code can access the text files that contain the categories.
categorychoice = 0
# Defines the categorychoice as zero for the first run through
categorychoice1 = category(categorychoice)
# Runs through the first category (where it can randomly select any of the five categories)
categorychoice = categorychoice1
# Defines categorychoice as the returned 'categorychoice1', so that it will not be selected again
print("")
time.sleep(1)
# Presentation frills
category(categorychoice)
# Runs the category function a second time, taking the previous category in as a parameter so that it will not select
# that category again.
print("")
time.sleep(1)
# Presentation frills
print("You have answered 2 Categories!")
print("Here is your score!")
print(sum(score))
# Prints the player's total score
time.sleep(1)
save = input("Would you like to save your score? ('yes', 'no') ")
# Asks if the player would like to save their score
os.chdir('..')
os.chdir('Profiles')
# Changes the directory to 'Profiles', so that the code can interact with the contents of the documents there
if save.title() == 'Yes':
    scoresave(str(sum(score)))
    # If the player would like to save their score, calls the 'scoresave' function with the total score as a string
    # parameter.
elif save.title() == 'No':
    os.remove(username)
    print("Score Deleted!")
    # If the player would not like to save their score, deletes their profile.
time.sleep(1)
print("")
print("Here are the game's all-time highscores!")
highscores()
# Calls the 'highscores' function to show the player the all time highscores, sorted alphabetically by username.
time.sleep(1)
print("")
print("Thanks for Playing!")
# Presentation frills
