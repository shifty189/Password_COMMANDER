VERSION = '0.03'
EDITDATE = '6/27/2024'

class PasswordConfig:
    def __init__(self, length=15, num=True, let=True, LET=True, spec=True, space=True, easy=False):
        self.length = length
        self.number = num
        self.letter = let
        self.LETTER = LET
        self.special = spec
        self.space = space
        self.easypassword = easy
        self.speciallist = ['!','@','#','$','%','^','&','*','+']
