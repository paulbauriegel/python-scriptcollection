import genanki
from pathlib import Path
import re
from easygui import codebox
import tkinter as tk
import pymsgbox
from contextlib import contextmanager

my_model = genanki.Model(
    1607392319,
    'Simple Model',
    fields=[
        {'name': 'Question'},
        {'name': 'Answer'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '{{Question}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
        },
    ])

my_deck = genanki.Deck(
    2059400110,
    'IT-Sicherheit')

contents = Path('IT-Sicherheit-Fragen-TINF15AIBC.txt').read_text()
n = 0
for frage in re.split(r"\n\d+\.", contents):
    front, back = frage.split("\n", 1)
    front = front.strip()
    n += 1
    i = 0
    while not(front.endswith(".") or front.endswith("?")
              or front.endswith(")") or front.endswith(":")) and i<2:
        i += 1
        newfront, back = back.split("\n", 1)
        front += newfront
    if front.startswith("- "):
        front = front[2:]
    my_note = genanki.Note(
        model=my_model,
        fields=[front, back.replace("\n","<br>")])
    my_deck.add_note(my_note)
    print(back.replace("\n", "<br>"))

    #with tk(timeout=1.5):
     #   codebox("Contents of file " + filename, "Show File Contents", text)
    #pymsgbox.native.alert(back, front)
    #if(n>15):
     #   print("Frage: ", front, "\n\nAntwort: ", back)
genanki.Package(my_deck).write_to_file('it-sicherheit.apkg')