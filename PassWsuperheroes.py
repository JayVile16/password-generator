import random

def SHpassword():
    characters = ['batman', 'Batman', 'Superman', 'supes', 'manofsteel', 'wonderwoman' 'princessDiana', 'DianaPrince' 'PrincessDiana', 'Greenlantern', 'greenlantern', 'flash', 'fastestmanalive','speedforce', 'wallyBarry', 'redlightning', 'darkknight', 'GL', 'WW', 'darkSeid', 'DarkSeid', 'DS', 'nightwing', 'Nightwing', 'RedRobin', 'RR', 'R3dR0bin', 'Robin', 'BoyWonder', 'Damien', 'Superboy', 'JonathanKent', 'superboy', 'ConnorKent', 'LexLuthor', 'l3x', 'L3x', 'Luthor', 'Joker', 'ClownPrinceofCrime', 'cl0wnpr!nceofCrim3', 'BB', 'BlueBeetle', 'Aquaman', 'aquaman', 'JasonTodd', 'RedHood', 'orphan', 'Orphan', 'redhood', 'batgirl', 'oracle', 'Oracle', 'Batgirl', 'Spiderman', 'Spidey', 'Webhead', 'spidey', 'Thor', 'CaptainAmerica', 'RasAlGhul', 'EbenezerDarrk', 'TheWrath', 'Azarael', 'Riddler', 'bane', 'Bane', 'riddler']

    settings = ['Gotham', 'Metropolis', 'Themyscira', 'goth@m', 'm3trop0lis', 'Apokolips', 'aPokolips', '@pok0l!pS', 'Atlantis', 'Bludhaven', 'starCity', 'StarCity', 'NewGenesis', 'BatCave', 'CrimeAlley', 'LexCorp', 'IcebergLounge', 'SanctumSanctorum', 'BaxterBuilding', 'AvengersTower', 'WayneManor', 'WayneTower', 'FortressofSolitude']

    a = random.randint(0,9)
    b = random.randint(0,9)
    c = random.randint(0,9)
    d = random.randint(0,9)


    charRandom = random.choice(characters)
    charList = [charRandom.lower(), charRandom.title(), charRandom]
          
    setRandom = random.choice(settings)
    setList = [setRandom.lower(), setRandom.title(), setRandom]

    extra = ['!', '?', '$', '#', '%', '&', '*']

    print('Generating password:')
    password = random.choice(extra) + random.choice(charList) + random.choice(setList) + str(a) + str(b) + str(c) + str(d) + random.choice(extra)
    print('Password:', password)

