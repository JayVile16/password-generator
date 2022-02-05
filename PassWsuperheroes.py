mport random
import sqlite3

ask = str(input("What genre of password do you want? (1. comics, 2. manga/anime, or 3. fantasy): "))
spec = input("Do you want special characters? (Ex. '!' or '?') y/n: ")

digits = str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))
special = ['!', '$', '*', '?', '@']


conn = sqlite3.connect('pop_database.db')
cursor = conn.cursor()


def comicPS():
    db = cursor.execute("SELECT Comics from Password_Database")
    row = cursor.fetchall()

    x = random.randint(0,len(row)-1)
    y = random.randint(0,len(row)-1)

    tup = row[x]+row[y]
    word = ''.join(tup)

    if spec == 'y':
        options = [(word+random.choice(special)),(random.choice(special)+word+random.choice(special))]
        password = random.choice(options) + digits
        print(password)
    elif spec == 'n':
        password = word + digits
        print(password)
    else:
        print("Please enter y(yes) or n(no)")


def mangaPS():
    db = cursor.execute("SELECT Manga from Password_Database")
    row = cursor.fetchall()

    x = random.randint(0,len(row)-1)
    y = random.randint(0,len(row)-1)

    tup = row[x]+row[y]
    word = ''.join(tup)

    if spec == 'y':
        options = [(word+random.choice(special)),(random.choice(special)+word+random.choice(special))]
        password = random.choice(options) + digits
        print(password)
    elif spec == 'n':
        password = word + digits
        print(password)
    else:
        print("Please enter y(yes) or n(no)")

def fantasyPS():
    db = cursor.execute("SELECT Fantasy from Password_Database")
    row = cursor.fetchall()

    x = random.randint(0,len(row)-1)
    y = random.randint(0,len(row)-1)

    tup = row[x]+row[y]
    word = ''.join(tup)

    if spec == 'y':
        options = [(word+random.choice(special)),(random.choice(special)+word+random.choice(special))]
        password = random.choice(options) + digits
        print(password)
    elif spec == 'n':
        password = word + digits
        print(password)
    else:
        print("Please enter y(yes) or n(no)")

if ask == '1':
    comicPS()
elif ask == '2':
    mangaPS()
elif ask == '3':
    fantasyPS()
else:
    print('Please enter a valid number.')
