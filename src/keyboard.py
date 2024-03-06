'''
This file initializes the layout of the current keyboard and calculates
the distance function from different rows/keys.
'''

class keyboard():
    def __init__(self) -> None:
        self.toprow = ['Q','W','E','R','T','Y','U', 'I','O','P']
        self.middlerow = ['A','S','D','F','G','H','J','K','L']
        self.bottomrow = ['Z','X','C','V','B','N','M']

    
    def getboard(self):
        return self.board

def main():
    keyboardinstant = keyboard()
    print(keyboardinstant.getboard())
    
if __name__ == "__main__":
    main()