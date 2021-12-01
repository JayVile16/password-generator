import PassWsuperheroes
import PassWanime
import PassWfantasy

genre = str(input('What genre do you want your password to be? Please enter a number (1. Anime, 2. Comics, 3. Fantasy & Sci-Fi): '))

if genre == '1':
     PassWanime.anipassword()

elif genre == '2':
     PassWsuperheroes.SHpassword()

elif genre == '3':
     PassWfantasy.fantpassword()
else:
     print('Please enter one of the following numbers 1, 2, 3?')
