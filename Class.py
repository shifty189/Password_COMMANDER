import random

VERSION = '0.07'
EDITDATE = '7/19/2024'


class PasswordConfig:
    def __init__(self, length=15, num=True, let=True, upper=True, spec=True, space=False, easy=True):
        self.length = length
        self.number = num
        self.letter = let
        self.upper = upper
        self.special = spec
        self.space = space
        self.easypassword = easy
        self.speciallist = ['!', '@', '#', '$', '%', '^', '&', '*', '+']
        self.letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                        't', 'u', 'v', 'w', 'x', 'y', 'z']

    def generatePassword(self):
        password = ''
        if not self.easypassword:
            options = []
            if self.number:
                options.append('number')
            if self.letter:
                options.append('letter')
            if self.upper:
                options.append('upper')
            if self.special:
                options.append('special')
            if self.space:
                options.append('space')
            tempLength = self.length
            while tempLength > 0:
                pick = random.choice(options)
                if pick == 'number':
                    password = password + str(random.randint(0,9))
                if pick == 'letter':
                    password = password + random.choice(self.letters)
                if pick == 'upper':
                    let = random.choice(self.letters)
                    password = password + let
                if pick == 'special':
                    password = password + random.choice(self.speciallist)
                if pick == 'space':
                    password = password + ' '
                tempLength -= 1
        else:
            with open('words.txt', 'r') as file:
                dicWords = file.readlines()
                password = random.choice(dicWords)
        return password
