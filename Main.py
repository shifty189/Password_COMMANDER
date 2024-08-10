import tkinter as tk
import Class
import os
import pickle
import messagebox


VERSION = '0.19'
EDITDATE = '8/10/2024'
minimumClassVersion = '0.13'

# Class version check
if float(minimumClassVersion) > float(Class.VERSION):
    raise ValueError('Class file version is to old, update Class.py')


def updateChecks():
    """
    this function is used to update the GUI from the loaded config object
    """
    global settingsCFG, lengthVar, numberCheck, letterCheck, letterCheck2
    global specialCheck, spaceCheck, easyCheck
    lengthVar.set(settingsCFG.length)
    numberCheck.set(settingsCFG.number)
    letterCheck.set(settingsCFG.letter)
    letterCheck2.set(settingsCFG.upper)
    specialCheck.set(settingsCFG.special)
    easyCheck.set(settingsCFG.easypassword)


def defaultConfig():
    """
    this function creates a new config from default settings then runs updateCheck to update the GUI
    """
    global settingsCFG
    settingsCFG = Class.PasswordConfig()
    updateChecks()
    getWords(settingsCFG)


def saveSpecial(config, string, window):
    """
    this function updates the loaded config's allowed special charector list with the user input from editSpecial
    function, and destorys that window.
    """
    window.destroy()
    templist = string.split(',')
    config.speciallist = templist


def editSpecial(config):
    """
    this function creates a new window and allows the user to input a comma seperated string to change the loaded
    config's allowed special charector list
    """
    global Main
    specialWindow = tk.Toplevel(Main)
    specialWindow.iconbitmap('commander.ico')
    tempList = ' '
    for i, c in enumerate(config.speciallist):
        if i == 0:
            tempList = c
        else:
            tempList = tempList + f",{c}"
    listText = tk.Label(specialWindow, text='below is all the special characters')
    listText.grid(row=0, column=0)
    listChar = tk.Entry(specialWindow)
    listChar.insert(0, tempList)
    listChar.grid(row=1, column=0)
    explainText = tk.Label(specialWindow, text='you may edit this comma seperated list')
    explainText.grid(row=2, column=0)
    saveChar = tk.Button(specialWindow, text='save', command=lambda: saveSpecial(config, listChar.get(), specialWindow))
    saveChar.grid(row=3, column=0)


def updateconfig():
    """
    this function is used to make a new config with up-to-date information from the checkboxes. used to update
    the config before refreshing the interface without saving the config
    """
    global settingsCFG, lengthVar, numberCheck, letterCheck, letterCheck2
    global specialCheck, spaceCheck, easyCheck

    settingsCFG.length = lengthVar.get()
    settingsCFG.number = numberCheck.get()
    settingsCFG.letter = letterCheck.get()
    settingsCFG.upper = letterCheck2.get()
    settingsCFG.special = specialCheck.get()
    settingsCFG.easypassword = easyCheck.get()

    getWords(settingsCFG)


def saveconfig():
    """
    used the commit the current user input to hard drive
    """
    global settingsCFG, lengthVar, numberCheck, letterCheck, letterCheck2
    global specialCheck, spaceCheck, easyCheck, docs
    settingsCFG.length = lengthVar.get()
    settingsCFG.number = numberCheck.get()
    settingsCFG.letter = letterCheck.get()
    settingsCFG.upper = letterCheck2.get()
    settingsCFG.special = specialCheck.get()
    settingsCFG.easypassword = easyCheck.get()
    with open(f'{docs}\\default.cfg', 'wb') as cfgfile:
        pickle.dump(settingsCFG, cfgfile)
    messagebox.showinfo(title='saved', message='config saved')


def getWords(config):
    """
    this function is used to get a list of 5 words from the config's generatePassword function and insert them into a
    tkinter Text widget used for display to the user
    """
    global wordsText
    wordsText.delete('1.0', tk.END)
    Words = []
    temp = 5
    while temp > -1:
        Words.append(config.generatePassword())
        temp -= 1
    for i, word in enumerate(Words):
        wordsText.insert(tk.END, word + "\n")


docs = f'{os.path.expanduser("~")}\\Documents\\PasswordCommander'
firstTime = True
if os.path.exists(docs):
    firstTime = False
    try:
        with open(f'{docs}\\default.cfg', 'rb') as cfgfile:
            settingsCFG = pickle.load(cfgfile)
    except FileNotFoundError:
        print('loading file error')
        settingsCFG = Class.PasswordConfig()

    firstTime = False
else:
    os.makedirs(docs)
    settingsCFG = Class.PasswordConfig()
    with open(f'{docs}\\default.cfg', 'ab') as cfgfile:
        pickle.dump(settingsCFG, cfgfile)
    firstTime = True


Main = tk.Tk()
Main.title('Password Commander')
Main.iconbitmap('commander.ico')
wordFrame = tk.Frame(Main)
wordControlFrame = tk.Frame(Main)
settingsFrame = tk.Frame(Main)
editFrame = tk.Frame(Main)


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
temp = 45
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
editFrame.grid(row=0, column=2)

# word frame to display selection
wordsText = tk.Text(wordFrame, height=10, width=50)
wordsText.grid(row=0, column=1)

# control frame for buttons
moreWordsButton = tk.Button(wordControlFrame, text='New Words', command=updateconfig)
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
                               offvalue=0,
                               padx=7)
specialButton.pack()

saveButton = tk.Button(settingsFrame, text='Save', command=saveconfig)
saveButton.pack()

# Edit frame
defaultConfigButton = tk.Button(editFrame, text='Default', command=defaultConfig)
defaultConfigButton.pack()
editSpecialButton = tk.Button(editFrame, text='Edit Special', command=lambda: editSpecial(settingsCFG))
editSpecialButton.pack()

getWords(settingsCFG)

tk.mainloop()
