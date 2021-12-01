import random

def anipassword():
    characters = ['naruto', 'godofshinobi', 'ichigo', 'shinihollquin', 'zangetsu','BankaiTensa', 'Goku', 'Kakarot', 'goku', 'kakarot', 'SSJGod', 'SonGoku', 'deku', 'izukumido', 'GreatestHero', 'greatesthero', 'tanjiro' 'Tanjiro', 'DanceoftheFireGod', 'Luffy', 'Strawhat', 'luffy', 'strawhat', 'Vegeta', 'Piccolo', 'Gon', 'Killua', 'Meruem', 'Zoro', 'Frieza', 'WickedBloodline', 'SaiyanPrince', 'Bakugo', 'Kenshin', 'LightYagami', 'Riku', 'Aizen', 'BlackBeard', 'Shanks', 'MonkeyDGarp', 'WhiteBeard', 'EdwardNewgate', 'Kaido', 'Crocodile', 'Mugen', 'SpikeSpiegel', 'YusukeUrameshi', 'Gogeta', 'Vegito', 'PotaraFusion']

    settings = ['konoha', 'Konoha','landoffire', 'LandofFire', 'HiddenLeaf', 'hiddenleaf', 'GoingMerry', 'goingmerry', 'ThousandSunny', 'thousandsunny','SoulSociety', 'EastBranch', 'GrandLine', 'grandline', 'gr@ndLine', 'Alabasta', 'WholeCakeIsland', 'Onigashima', 'Dressrosa', 'Namek', 'PlanetVegeta', 'Universe7']

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