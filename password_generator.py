import random
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


#def SHpassword():
    # Customize the password
    #length = int(input('How long would you like the terms to be? Please enter a number: '))
    #special = input('Do you want special characters? (y/n): ')

    #characters = ['batman', 'Batman', 'Superman', 'supes', 'manofsteel', 'wonderwoman' 'princessDiana', 'DianaPrince' 'PrincessDiana', 'Greenlantern', 'greenlantern', 'flash', 'fastestmanalive','speedforce', 'wallyBarry', 'redlightning', 'darkknight', 'GL', 'WW', 'darkSeid', 'DarkSeid', 'DS', 'nightwing', 'Nightwing', 'RedRobin', 'RR', 'R3dR0bin', 'Robin', 'BoyWonder', 'Damien', 'Superboy', 'JonathanKent', 'superboy', 'ConnorKent', 'LexLuthor', 'l3x', 'L3x', 'Luthor', 'Joker', 'ClownPrinceofCrime', 'cl0wnpr!nceofCrim3', 'BB', 'BlueBeetle', 'Aquaman', 'aquaman', 'JasonTodd', 'RedHood', 'orphan', 'Orphan', 'redhood', 'batgirl', 'oracle', 'Oracle', 'Batgirl', 'Spiderman', 'Spidey', 'Webhead', 'spidey', 'Thor', 'CaptainAmerica', 'RasAlGhul', 'EbenezerDarrk', 'TheWrath', 'Azarael', 'Riddler', 'bane', 'Bane', 'riddler']

    #settings = ['Gotham', 'Metropolis', 'Themyscira', 'goth@m', 'm3trop0lis', 'Apokolips', 'aPokolips', '@pok0l!pS', 'Atlantis', 'Bludhaven', 'starCity', 'StarCity', 'NewGenesis', 'BatCave', 'CrimeAlley', 'LexCorp', 'IcebergLounge', 'SanctumSanctorum', 'BaxterBuilding', 'AvengersTower', 'WayneManor', 'WayneTower', 'FortressofSolitude']

    #a = random.randint(0,9)
    #b = random.randint(0,9)
    #c = random.randint(0,9)
    #d = random.randint(0,9)


    #charRandom = random.choice(characters)[:length//2]
    #charList = [charRandom.lower(), charRandom.title(), charRandom]
          
    #setRandom = random.choice(settings)[:length//2]
    #setList = [setRandom.lower(), setRandom.title(), setRandom]

    #extra = ['!', '?', '$', '#', '%', '&', '*']

    #print('Generating password:')
    #if special == 'y':
        #password = random.choice(extra) + random.choice(charList) + random.choice(setList) + str(a) + str(b) + str(c) + str(d) + random.choice(extra)
    #elif special == 'n':
        #password = random.choice(charList) + random.choice(setList) + str(a) + str(b) + str(c) + str(d)
    #print('Password:', password)