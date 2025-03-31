# Beginning: Create Variables
cat_points = 0
dog_points = 0

# Middle: Ask Questions
# Question 1,

answer = input("On a Weekend Would You Rather, A) Nap All Day, or B) Go On a Hike?\n")
if answer.lower() == "a":
    cat_points += 1
elif answer.lower() == "b":
    dog_points += 1
else:
    print("A, B or C Only!")
    answer = input("On a Weekend Would You Rather, A) Nap All Day, or B) Go On a Hike?\n")
    if answer.lower() == "a":
        cat_points += 1
    elif answer.lower() == "b":
        dog_points += 1

# Question 2,

answer = input("Are You, A) An Extrovert, or B) An Introvert?\n")
if answer.lower() == "a":
    dog_points += 1
elif answer.lower() == "b":
    cat_points += 1
else:
    print("A, B or C Only!")
    answer = input("Are You, A) An Extrovert, or B) An Introvert?\n")
    if answer.lower() == "a":
        dog_points += 1
    elif answer.lower() == "b":
        cat_points += 1

# Question 3,

answer = input("Would You Rather Eat Lunch, A) By Yourself, or B) With Friends?\n")
if answer.lower() == "a":
    cat_points += 1
elif answer.lower() == "b":
    dog_points += 1
else:
    print("A, B or C Only!")
    answer = input("Would You Rather Eat Lunch, A) By Yourself, or B) With Friends?\n")
    if answer.lower() == "a":
        cat_points += 1
    elif answer.lower() == "b":
        dog_points += 1

# Question 4,

answer = input("Do You Have, A) A Dog, B) A Cat, C) Both or D) None?\n")
if answer.lower() == "a":
    dog_points += 2
elif answer.lower() == "b":
    cat_points += 2
elif answer.lower() == "c":
    cat_points += 1
    dog_points += 1
elif answer.lower() == "d":
    cat_points -= 1
    dog_points -= 1
else:
    print("A, B or C Only!")
    answer = input("Do You Have, A) A Dog, B) A Cat, C) Both or D) None?\n")
    if answer.lower() == "a":
        dog_points += 2
    elif answer.lower() == "b":
        cat_points += 2
    elif answer.lower() == "c":
        cat_points += 1
        dog_points += 1
    elif answer.lower() == "d":
        cat_points -= 1
        dog_points -= 1


# Question 5,

answer = input("Which Pet Do You Not Want, A) A Dog, B) A Cat, C) Both or D) None?\n")
if answer.lower() == "a":
    dog_points -= 2
elif answer.lower() == "b":
    cat_points -= 2
elif answer.lower() == "c":
    cat_points -= 1
    dog_points -= 1
elif answer.lower() == "d":
    cat_points += 1
    dog_points += 1
else:
    print("A, B or C Only!")
    answer = input("Which Pet Do You Not Want, A) A Dog, B) A Cat, C) Both or D) None?\n")
    if answer.lower() == "a":
        dog_points -= 2
    elif answer.lower() == "b":
        cat_points -= 2
    elif answer.lower() == "c":
        cat_points -= 1
        dog_points -= 1
    elif answer.lower() == "d":
        cat_points += 1
        dog_points += 1

# Question 6,

answer = input("What Meat Do You Like The Most, A) Fish, B) Red Meat, C) Chicken, or D) Other?\n")
if answer.lower() == "a":
    cat_points += 2
elif answer.lower() == "b":
    dog_points += 2
elif answer.lower() == "c":
    cat_points += 1
elif answer.lower() == "d":
    cat_points += 0
else:
    print("A, B or C Only!")
    answer = input("What Meat Do You Like The Most, A) Fish, B) Red Meat, C) Chicken, or D) Other?\n")
    if answer.lower() == "a":
        cat_points += 2
    elif answer.lower() == "b":
        dog_points += 2
    elif answer.lower() == "c":
        cat_points += 1

# Question 7,

answer = input("Do You Want, A) A Lot of Friends, B) A Few Friends, C) None?\n")
if answer.lower() == "a":
    cat_points += 2
elif answer.lower() == "b":
    dog_points += 1
    cat_points += 1
elif answer.lower() == "c":
    cat_points += 1
else:
    print("A, B or C Only!")
    answer = input("Do You Want, A) A Lot of Friends, B) A Few Friends, C) None?\n")
    if answer.lower() == "a":
        dog_points += 2
    elif answer.lower() == "b":
        dog_points += 1
        cat_points += 1
    elif answer.lower() == "c":
        cat_points += 1

answer = input("How Loyal Are You To Friends, A) Super Loyal, B) I like Them, C) I Would Backstab Them ?\n")
if answer.lower() == "a":
    cat_points += 2
elif answer.lower() == "b":
    dog_points += 1
elif answer.lower() == "c":
    cat_points += 1
else:
    print("A, B or C Only!")
    answer = input("How Loyal Are You To Friends, A) Super Loyal, B) I like Them, C) I Would Backstab Them ?\n")
    if answer.lower() == "a":
        cat_points += 2
    elif answer.lower() == "b":
        dog_points += 1
    elif answer.lower() == "c":
        cat_points += 1

# End: Determine Results

if cat_points - 2 > dog_points:
    print("You Are a Cat Person!")
elif dog_points - 2 > cat_points:
    print("You Are a Dog Person!")
else:
    print("You Are Indecisive!")
print("\nCat Points", cat_points, "\nDog Points", dog_points, "\n")