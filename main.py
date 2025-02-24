from datetime import datetime

if __name__ == '__main__':
    ADULT = 18
    date = datetime.now().year

    name = str(input("Enter your name: "))
    surname = str(input("Enter your surname: "))
    born = int(input("Enter your year of born: "))
    len_of_surname = len(surname)
    age = date - born
    print(f"Hello, {name} {surname.upper()}, {age} yo, lenght of surname is {surname.__len__()}")

    print("Female" if name[-1] == 'a'else 'Male')

    adulthood = abs(age - ADULT)
    if age < 18:
        print(f"You are child. \nYou'll be an adult in {adulthood} years")
    elif age > 18:
        print(f"You are adult since {adulthood} years")
    else: print(f"You are an adult since this year")