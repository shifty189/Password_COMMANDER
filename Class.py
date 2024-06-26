VERSION = '0.02'
EDITDATE = '6/25/2024'

class PasswordConfig:
    def __init__(self, num=True, let=True, LET=True, spec=True, space=True, easy=False):
        self.number = num
        self.letter = let
        self.LETTER = LET
        self.special = spec
        self.space = space
        self.easypassword = easy
        self.speciallist = ['!','@','#','$','%','^','&','*','+']
