import tkinter as tk
from Class import *
import os
import pickle

settingsCFG = PasswordConfig()
docs = f'{os.path.expanduser('~')}\\Documents\\PasswordCommander'
firstTime = True
if os.path.exists(docs):
    cfgfile = open(f'{docs}\\default.cfg', 'rb')
    settingsCFG = pickle.load(cfgfile)
    cfgfile.close()
    firstTime = False
    if os.path.exists(f'{docs}\\Templates'):
        ...
    else:
        os.makedirs(f'{docs}\\Templates')
else:
    os.makedirs(docs)
    cfgfile = open(f'{docs}\\default.cfg', 'ab')
    pickle.dump(settingsCFG, cfgfile)
    cfgfile.close()
    firstTime = True
    if os.path.exists(f'{docs}\\Templates'):
        ...
    else:
        os.makedirs(f'{docs}\\Templates')

Main = tk.Tk()
wordFrame = tk.Frame(Main)
wordControlFrame = tk.Frame(Main)
settingsFrame = tk.Frame(Main)

<<<<<<< HEAD
VERSION = '0.04'
EDITDATE = '6/28/2024'
=======
VERSION = '0.03'
EDITDATE = '6/26/2024'
>>>>>>> 460f12c6ee2d43a0b9fe8ca93b358d3a60ce0e1a
numberCheck = tk.IntVar()
letterCheck = tk.IntVar()
letterCheck2 = tk.IntVar()
specialCheck = tk.IntVar()
spaceCheck = tk.IntVar()
<<<<<<< HEAD
numberCheck.set(1)
letterCheck.set(1)
letterCheck2.set(1)
specialCheck.set(1)
spaceCheck.set(0)
clicked = tk.StringVar()
clicked.set('15')
lowestMinLength = 5

options = []
temp = 50
while temp >= lowestMinLength:
    options.append(str(temp))
    temp -= 1
=======

numberCheck.set(settingsCFG.number)
letterCheck.set(settingsCFG.letter)
letterCheck2.set(settingsCFG.LETTER)
specialCheck.set(settingsCFG.special)
spaceCheck.set(settingsCFG.space)

>>>>>>> 460f12c6ee2d43a0b9fe8ca93b358d3a60ce0e1a

wordFrame.grid(row=0, column=0)
wordControlFrame.grid(row=1, column=0)
settingsFrame.grid(row=0, column=1)

# word frame to display selection
wordsText = tk.Text(wordFrame, height=10, width=15)
wordsText.pack()

# control frame for buttons
newButton = tk.Button(wordControlFrame, text='New', command=lambda: ...)
newButton.grid(row=0, column=0)
clipButton = tk.Button(wordControlFrame, text='Copy', command=lambda: ...)
clipButton.grid(row=0, column=1)

# settings frame
numberButton = tk.Checkbutton(settingsFrame, text='Numbers',
                              variable=numberCheck,
                              onvalue=1,
                              offvalue=0)
numberButton.pack()
letterButton = tk.Checkbutton(settingsFrame, text='Letters (Lower)',
                              variable=letterCheck,
                              onvalue=1,
                              offvalue=0,
                              padx=3)
letterButton.pack()
letterButton2 = tk.Checkbutton(settingsFrame, text='Letters (Upper)',
                               variable=letterCheck2,
                               onvalue=1,
                               offvalue=0,
                               padx=3)
letterButton2.pack()
specialButton = tk.Checkbutton(settingsFrame, text='Special Characters',
                               variable=specialCheck,
                               onvalue=1,
                               offvalue=2,
                               padx=7)
specialButton.pack()
spaceButton = tk.Checkbutton(settingsFrame, text='space',
                             variable=spaceCheck,
                             onvalue=1,
                             offvalue=2,
                             padx=3)
spaceButton.pack()

with open('words.txt', 'r') as file:
    Words = file.readlines()
for i, word in enumerate(Words):
    wordsText.insert(f'{i}.0', word)

tk.mainloop()
