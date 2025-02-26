from datetime import datetime
date = datetime.now().year
ADULT = 18

def exercise_1(name, surname, born):
    return print(f"Hello, {name} {surname}, born in {born}. \n")


def exercise_2(name, surname):
    name = name.upper()
    surname = surname.upper()
    return print(f"Hello, {name} {surname}. \nYour name has {len(name)} letter and your surname has {len(surname)} letters.\n")


def exercise_3(name, surname, born):
    age = date - born
    return print(f"Hello, {name} {surname}, {age} yo.\n")


def exercise_4(name, surname):
    gender = 'female' if name[-1] == 'a' else 'male'
    return print(f"Hello, {name} {surname}, I can assume that you are a {gender}.\n")

def exercise_5(born):
    age = date - born
    adulthood = abs(age - ADULT)
    if age < 18:
        print(f"You are child. \nYou'll be an adult in {adulthood} years")
    elif age > 18:
        print(f"You are adult since {adulthood} years")
    else:
        print(f"You are an adult since this year")


if __name__ == '__main__':
    #exercise 6
    data = input('Enter your name and surname: ')
    name, surname = data.split(' ', 1)
    #name = str(input("Enter your name: "))
    #surname = str(input("Enter your surname: "))
    born = int(input("Enter your year of born: "))

    exercise_1(name, surname, born)
    exercise_2(name, surname)
    exercise_3(name, surname, born)
    exercise_4(name, surname)
    exercise_5(born)
