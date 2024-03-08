'''
This file initializes the layout of the current keyboard and calculates
the distance function from different rows/keys.
'''
TOP_ROW = ['Q','W','E','R','T','Y','U', 'I','O','P']
MIDDLE_ROW = ['A','S','D','F','G','H','J','K','L']
BOTTOM_ROW = ['Z','X','C','V','B','N','M',',','.','/']
STARTING_FINGER = ['A','S','D','F','J','K','L',';'] #Where your typical fingers start of whilst typing

class keyboard():
    def __init__(self) -> None:
        self.design = [TOP_ROW,MIDDLE_ROW,BOTTOM_ROW] #2d list to represent the keyboard
        self.fingerplacement = [STARTING_FINGER]
    
    def createParallelList(self,rowOne: list[str], removal: list[str]) -> list[str]:
        temp_list = [x for x in rowOne if x not in removal]
        return temp_list
        
    def findIndex(self, target_list: list[str], target: str)->int:
        for i in range(len(target_list)):
            if target_list[i] == target:
                return i
        

    def distance(self, word: str)->float:
        '''
        Calculates the total distance of finger movement which is required to type the word.
        For example, from middle row key to any key on top row would be distance of 1.032. If
        the letter is in same row and left or right to the current finger placement, then 
        it is distace 1. If its from middle row to bottom row, it's 1.118. Distance from bottom 
        row to top is 2.138. 
        
        Special Cases:
        F->T = 1.247, G->R=1.605, F->B=1.803, B->R=2.661, T->V = 2.015. 
        H->U = 1.605, J->Y=1.605, H->M=1.803, M->Y=2.661, U->N = 2.015. 
        For example the word 'NICE' = J->N + K->I + F->C + D->E
        '''
        
        parallel_top = self.createParallelList(TOP_ROW, ['T','Y'])
        parallel_bottom = self.createParallelList(BOTTOM_ROW, ['B'])
        
        

        length = 0
        for letter in range(len(word)):
            if word[letter] in self.fingerplacement:
                length += 0
            elif word[letter] in parallel_top:
                length+=1.032
                #find index for that letter
                new_index = self.findIndex(word[letter])
                #update finger to that letter
                self.fingerplacement[new_index] = word[letter]
                #shift one of the finger up, since its parallel it helps
        
       

        
                


           
                
        
def main():
    keyboardinstant = keyboard()
    print(keyboardinstant.distance('asdf'))
    
if __name__ == "__main__":
    main()