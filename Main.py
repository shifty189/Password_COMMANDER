import tkinter as tk

Main = tk.Tk()
wordFrame = tk.Frame(Main)
wordControlFrame = tk.Frame(Main)
settingsFrame = tk.Frame(Main)

VERSION = '0.02'
EDITDATE = '6/25/2024'
numberCheck = tk.IntVar()
letterCheck = tk.IntVar()
letterCheck2 = tk.IntVar()
specialCheck = tk.IntVar()
spaceCheck = tk.IntVar()

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
