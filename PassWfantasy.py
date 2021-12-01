import random
def fantpassword():
    # Customize the password
    length = int(input('How long would you like the terms to be? Please enter a number: '))
    special = input('Do you want special characters? (y/n): ')
    
    characters = ['whitewolf', 'houseStark', 'houseTargaryen', 'houseLannister', 'Sauron', 'Legolas', 'legolas', 'frodo', 'HarryPotter', 'Frodo', 'Fr0d0', 'Whitewalker', 'WhIteWAlker', 'Drogon', 'Revan', 'Jedi', 'Sith', 'J3di', 'S!th', 'DarthVader', 'Kenobi', 'BenKenobi', 'LukeSkywalker', 'Gollum', 'Greyjoy', 'TheonReek', 'KhalDrogo', 'HermoineGranger', 'RonWeasley', 'BilboBaggins', 'Vesemir', 'Ciri']

    settings = ['Mordor', 'MiddleEarth', 'Hogwarts', 'Mustafar', 'Coruscant', 'Hoth', 'mustafar', 'MustaFar', 'Tatooine', 'Westeros', 'KingsLanding', 'esos', 'dorne', '3s0s', 'd0rn3', 'Winterfell', 'W!nt3rFell', 'Lannisport', 'IronIslands', 'CastleBlack', 'Braavos', 'VaesDothrak', 'Blavakin', 'Novigrad', 'Velen']

    a = random.randint(0,9)
    b = random.randint(0,9)
    c = random.randint(0,9)
    d = random.randint(0,9)

    charRandom = random.choice(characters)[:length//2]
    charList = [charRandom.lower(), charRandom.title(), charRandom]
          
    setRandom = random.choice(settings)[:length//2]
    setList = [setRandom.lower(), setRandom.title(), setRandom]

    extra = ['!', '?', '$', '#', '%', '&', '*']

    print('Generating password:')
    if special == 'y':
        password = random.choice(extra) + random.choice(charList) + random.choice(setList) + str(a) + str(b) + str(c) + str(d) + random.choice(extra)
    elif special == 'n':
        password = random.choice(charList) + random.choice(setList) + str(a) + str(b) + str(c) + str(d)
    print('Password:', password)
