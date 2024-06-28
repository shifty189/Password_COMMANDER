import tkinter as tk

Main = tk.Tk()
wordFrame = tk.Frame(Main)
wordControlFrame = tk.Frame(Main)
settingsFrame = tk.Frame(Main)

VERSION = '0.03'
EDITDATE = '6/27/2024'
numberCheck = tk.IntVar()
letterCheck = tk.IntVar()
letterCheck2 = tk.IntVar()
specialCheck = tk.IntVar()
spaceCheck = tk.IntVar()
numberCheck.set(1)
letterCheck.set(1)
letterCheck2.set(1)
specialCheck.set(1)
spaceCheck.set(0)
clicked = tk.StringVar()
clicked.set('15')

options = []
temp = 50
while temp > 0:
    options.append(str(temp))
    temp -= 1

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
lengthOption = tk.OptionMenu(settingsFrame, clicked, *options)
lengthOption.grid(row=0, column=1)
lengthLabel = tk.Label(settingsFrame, text='Length')
lengthLabel.grid(row=0, column=0)
numberButton = tk.Checkbutton(settingsFrame, text='Numbers',
                              variable=numberCheck,
                              onvalue=1,
                              offvalue=0)
numberButton.grid(row=1, column=0)
letterButton = tk.Checkbutton(settingsFrame, text='Letters (Lower)',
                              variable=letterCheck,
                              onvalue=1,
                              offvalue=0,
                              padx=3)
letterButton.grid(row=2, column=0)
letterButton2 = tk.Checkbutton(settingsFrame, text='Letters (Upper)',
                               variable=letterCheck2,
                               onvalue=1,
                               offvalue=0,
                               padx=3)
letterButton2.grid(row=3, column=0)
specialButton = tk.Checkbutton(settingsFrame, text='Special Characters',
                               variable=specialCheck,
                               onvalue=1,
                               offvalue=2,
                               padx=7)
specialButton.grid(row=4, column=0)
spaceButton = tk.Checkbutton(settingsFrame, text='space',
                             variable=spaceCheck,
                             onvalue=1,
                             offvalue=2,
                             padx=3)
spaceButton.grid(row=5, column=0)

with open('words.txt', 'r') as file:
    Words = file.readlines()
for i, word in enumerate(Words):
    wordsText.insert(f'{i}.0', word)

tk.mainloop()
