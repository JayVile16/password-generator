import random
import sqlite3
import tkinter as tk
import clipboard as c

BACKGROUND_COLOR = "#1C86EE"
ANIME_COLOR = "#FF6347"
COMIC_COLOR = "#EEC900"
FANTASY_COLOR = "#00EE00"

digits = str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))
special = ['!', '$', '*', '?', '@']


conn = sqlite3.connect('pop_database.db')
cursor = conn.cursor()


def comic_ps():
    db = cursor.execute("SELECT Comics from Password_Database")
    column = cursor.fetchall()

    x = random.randint(0, len(column) - 1)
    y = random.randint(0, len(column) - 1)

    tup = column[x] + column[y]

    word = ''.join(tup)

    options = [(word + random.choice(special)), (random.choice(special) + word + random.choice(special)), (word)]

    chosen_ps = random.choice(options) + digits

    comic_password.config(text=chosen_ps)
    c.copy(chosen_ps)


def manga_ps():
    db = cursor.execute("SELECT Manga from Password_Database")
    column = cursor.fetchall()

    x = random.randint(0, len(column) - 1)
    y = random.randint(0, len(column) - 1)

    tup = column[x] + column[y]
    word = ''.join(tup)

    options = [(word + random.choice(special)), (random.choice(special) + word + random.choice(special)), word]
    chosen_ps = random.choice(options) + digits

    manga_password.config(text=chosen_ps)
    c.copy(chosen_ps)


def fantasy_ps():
    db = cursor.execute("SELECT Fantasy from Password_Database")
    column = cursor.fetchall()

    x = random.randint(0, len(column) - 1)
    y = random.randint(0, len(column) - 1)
    tup = column[x] + column[y]

    word = ''.join(tup)

    options = [(word + random.choice(special)), (random.choice(special) + word + random.choice(special)), word]
    chosen_ps = random.choice(options) + digits

    fantasy_password.config(text=chosen_ps)
    c.copy(chosen_ps)


window = tk.Tk()
window.title("My Password")
window.config(background=BACKGROUND_COLOR, padx=30, pady=30, height=600, width=500)

password = tk.Label(text="Which password would you like?", font=("Arial", 18, "bold"), fg="black", bg=BACKGROUND_COLOR)
password.grid(column=1, row=0)

comic_password = tk.Label(text="Password", font=("Arial", 15), fg="black", bg=COMIC_COLOR)
comic_password.grid(column=0, row=1, padx=10, pady=10)
comic_button = tk.Button(text="Comics", fg="black", command=comic_ps)
comic_button.grid(column=0, row=2)

manga_password = tk.Label(text="Password", font=("Arial", 15), fg="black", bg=ANIME_COLOR)
manga_password.grid(column=1, row=1, padx=10, pady=10)
manga_button = tk.Button(text="Anime/Manga", fg="black", command=manga_ps)
manga_button.grid(column=1, row=2)

fantasy_password = tk.Label(text="Password", font=("Arial", 15), fg="black", bg=FANTASY_COLOR)
fantasy_password.grid(column=2, row=1, padx=10, pady=10)
fantasy_button = tk.Button(text="Fantasy/Sci-fi", fg="black", command=fantasy_ps)
fantasy_button.grid(column=2, row=2)

window.mainloop()
