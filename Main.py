import tkinter as tk

import Class
import os
import pickle
import messagebox


VERSION = '0.10'
EDITDATE = '8/7/2024'
minimumClassVersion = '0.10'

# Class version check
if float(minimumClassVersion) > float(Class.VERSION):
    raise ValueError('Class file version is to old, update Class.py')


def saveConfig(lenT, number, letter, up, speciel, Wspace, Easy):
    global docs
    newConfig = Class.PasswordConfig(len=lenT, num=number, let=letter, upper=up, spec=speciel, space=Wspace, easy=Easy)
    with open(f'{docs}\\default.cfg', 'wb') as cfgfile:
        pickle.dump(newConfig, cfgfile)
    messagebox.showinfo(title='saved', message='config saved')


def getWords(config):
    global wordsText
    wordsText.delete('1.0', tk.END)
    Words = []
    temp = 5
    while temp > -1:
        Words.append(config.generatePassword())
        temp -= 1
    for i, word in enumerate(Words):
        wordsText.insert(f'{i}.4', word + "\n")


docs = f'{os.path.expanduser("~")}\\Documents\\PasswordCommander'
firstTime = True
if os.path.exists(docs):
    firstTime = False
    try:
        cfgfile = open(f'{docs}\\default.cfg', 'rb')
        settingsCFG = pickle.load(cfgfile)
    except FileNotFoundError:
        print('loading file error')
        # settingsCFG = Class.PasswordConfig()
        # cfgfile = open(f'{docs}\\default.cfg', 'ab')
        # pickle.dump(settingsCFG, cfgfile)

    cfgfile.close()
    firstTime = False
    if not os.path.exists(f'{docs}\\Templates'):
        os.makedirs(f'{docs}\\Templates')
else:
    os.makedirs(docs)
    settingsCFG = Class.PasswordConfig()
    with open(f'{docs}\\default.cfg', 'ab') as cfgfile:
        pickle.dump(settingsCFG, cfgfile)
    firstTime = True
    if not os.path.exists(f'{docs}\\Templates'):
        os.makedirs(f'{docs}\\Templates')

Main = tk.Tk()
wordFrame = tk.Frame(Main)
wordControlFrame = tk.Frame(Main)
settingsFrame = tk.Frame(Main)


numberCheck = tk.IntVar()
letterCheck = tk.IntVar()
letterCheck2 = tk.IntVar()
specialCheck = tk.IntVar()
spaceCheck = tk.IntVar()
easyCheck = tk.IntVar()
if settingsCFG.easypassword == 1:
    easyCheck.set(1)
numberCheck.set(1)
letterCheck.set(1)
letterCheck2.set(1)
specialCheck.set(1)
spaceCheck.set(0)
lowestMinLength = 5

options = []
temp = 50
while temp >= lowestMinLength:
    options.append(str(temp))
    temp -= 1

numberCheck.set(settingsCFG.number)
letterCheck.set(settingsCFG.letter)
letterCheck2.set(settingsCFG.upper)
specialCheck.set(settingsCFG.special)
spaceCheck.set(settingsCFG.space)


wordFrame.grid(row=0, column=0)
wordControlFrame.grid(row=1, column=0)
settingsFrame.grid(row=0, column=1)

# word frame to display selection
wordsText = tk.Text(wordFrame, height=10, width=20)
wordsText.pack()

# control frame for buttons
# newButton = tk.Button(wordControlFrame, text='New', command=lambda: ...)
# newButton.grid(row=0, column=0)
# clipButton = tk.Button(wordControlFrame, text='Copy', command=lambda: ...)
# clipButton.grid(row=0, column=1)
moreWordsButton = tk.Button(wordControlFrame, text='New Words', command=lambda: getWords(settingsCFG))
moreWordsButton.grid(row=1, column=0)

# settings frame
lengthVar = tk.StringVar()
lengthVar.set(settingsCFG.length)
lengthSelect = tk.OptionMenu(settingsFrame, lengthVar, *options)
lengthSelect.pack()
easyButton = tk.Checkbutton(settingsFrame, text='Easy',
                            variable=easyCheck,
                            onvalue=1,
                            offvalue=0)
easyButton.pack()
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
# print(spaceCheck.get())
saveButton = tk.Button(settingsFrame, text='Save', command=lambda: saveConfig(lengthVar.get(), numberCheck.get(),
                                                                              letterCheck.get(), letterCheck2.get(),
                                                                              specialCheck.get(), spaceCheck.get(),
                                                                              easyCheck.get()
                                                                              )
                       )
saveButton.pack()

getWords(settingsCFG)
# Words = []
# temp = 5
# while temp > 0:
#     Words.append(settingsCFG.generatePassword())
#     temp -= 1
# for i, word in enumerate(Words):
#     wordsText.insert(f'{i}.4', word + "\n")

tk.mainloop()
