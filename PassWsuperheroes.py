import random

def SHpassword():
    # Customize the password
    length = int(input('How long would you like the terms to be? Please enter a number: '))
    special = input('Do you want special characters? (y/n): ')

    characters = ['Batman', 'Superman', 'supes', 'manof', 'steel', 'Wonder','Woman' 'princess','Diana', 'Prince', 'pr!ncess', 'pr!nc3ss', 'Green','lantern', 'arrow', 'Flash', 'fastest', 'manalive', 'speedforce', 'wally','barry', 'lightning', 'dark','knight', 'greenL', 'wwoman', 'darkseid', 'DarkSeid', 'DS', 'nightwing', 'NightWing', 'robin', 'RedR', 'R3dR0bin', 'BoyWonder', 'boy', 'damien', 'superboy', 'Jonathan','Kent', 'Connor','Kent', 'Lex', 'Luthor', 'l3x', '1uth0r', 'joker', 'ClownPrince','crime', 'cl0wnpr!nce','cr1m3', 'BlueB', 'bluebeetle', 'blueBeetle', 'aquaman', 'jason', 'todd', 'red', 'hood', 'orphan', '0rphAn', 'redhood', 'Oracle', 'Batgirl', 'Spiderman', 'Spidey', 'Webhead', 'Thor', 'Captain', 'America', 'Ras','AlGhul', 'Ebenezer','Darrk', 'TheWrath', 'Azarael', 'Riddler', 'Bane', 'r?ddlEr', 'Cyborg', 'Martian', 'Manhunter', 'Jonn', 'Jonzz', 'Hawkgirl', 'Hawkman', 'Static', 'Shock', 'Icon', 'Ic0n', 'iC0n', 'Booster', 'Gold', 'Black', 'Jefferson', 'Bruce', 'Wayne', 'KalEl', 'kalel', 'west', ]

    settings = ['Gotham', 'Metropolis', 'Themyscira', 'goth@m', 'm3trop0lis', 'Apokolips', 'aPokolips', '@pok0l!pS', 'Atlantis', 'Bludhaven', 'starCity', 'StarCity', 'NewGenesis', 'BatCave', 'Crime', 'Alley', 'LexCorp', 'Iceberg','Lounge', 'Sanctum','Sanctorum', 'Baxter', 'Building', 'Avengers', 'Tower', 'Wayne','Manor', 'Fortress', 'Solitude']

    a = random.randint(0,9)
    b = random.randint(0,9)
    c = random.randint(0,9)
    d = random.randint(0,9)

    if length % 2 == 1:
        charRandom = random.choice(characters)[:(length//2)+1]
        charList = [charRandom.lower(), charRandom.title(), charRandom]
    else:
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


