print("Welcome to my computer quiz!")
Playing = input("Do you want to play? ")
if Playing != "yes":
    quit()
print("Great! Lets Play! :)")
score = 0

answer = input("what does CPU stand for? ")
if answer == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect :(")

answer = input("what does RAM stand for? ")
if answer == "random access memory":
    print("Correct!")
    score += 1
else:
        print("Incorrect :(")

answer = input("What was the program language Python named after? ")
if answer == "monty python":
    print("Correct!")
    score += 1
else:
    print("Incorrect :(")

answer = input("Is programming cool? ")
if answer == "yes":
    print("Correct!")
    score += 1
else:
    print("Incorrect :(")
print("great job your score is "+ str(score))