'''
This file initializes the layout of the current keyboard and calculates
the distance function from different rows/keys.
'''

class keyboard():
    def __init__(self) -> None:
        self.toprow = ['Q','W','E','R','T','Y','U', 'I','O','P']
        self.middlerow = ['A','S','D','F','G','H','J','K','L']
        self.bottomrow = ['Z','X','C','V','B','N','M']
        self.fingerlist = [counter for counter in self.middlerow if counter !='H' and counter !='G'] # The typical fingers which fingers start at

    
    def fingerOn(self):
        return self.fingerlist

def main():
    keyboardinstant = keyboard()
    print(keyboardinstant.fingerOn())
    
if __name__ == "__main__":
    main()