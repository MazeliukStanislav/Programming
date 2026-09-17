# Laba2
# User's data storage(dict)
users = {
    "student1": {
        "password": "1234",
        "grades": [9, 10, 7, 12, 5, 8, 3, 11]
    },
    "student2": {
        "password": "2345",
        "grades": [6, 8, 4, 10, 7, 3, 12, 9]
    },
    "student3": {
        "password": "3456",
        "grades": [12, 11, 10, 9, 8, 5, 4, 2]
    },
    "student4": {
        "password": "4567",
        "grades": [5, 7, 9, 6, 3, 4, 10, 8]
    }
}


# User Authentication
login = input("Введіть логін: ")
password = input("Введіть пароль: ")


# Verification login and password
# Check login and password
while login not in users or users[login]["password"] != password:
    print("\nНеправильні дані. Спробуйте ще раз.")

    login = input("Введіть логін: ")
    password = input("Введіть пароль: ")

    grades = users[login]["grades"]

    print("\nВхід успішний!")
    print("Ваші оцінки:")

    # Get grades
    for grade in grades:
        print(grade, end=" ")


    # Grade counters
    satisfactory = 0
    unsatisfactory = 0


    # Count satisfactory and unsaticfactory grades
    for grade in grades:
        if 5 <= grade <= 12:
            satisfactory += 1
        elif 1 <= grade <= 4:
            unsatisfactory += 1


    # Result
    print("\n\nКількість задовільних оцінок:", satisfactory)
    print("Кількість незадовільних оцінок:", unsatisfactory)

