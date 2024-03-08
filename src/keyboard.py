import math
'''
This file initializes the layout of the current keyboard and calculates
the distance function from different rows/keys.
'''
KEYBOARD_LAYOUT = {
            'Q': (0, 0), 'W': (0, 1), 'E': (0, 2), 'R': (0, 3), 'T': (0, 4),
            'Y': (0, 5), 'U': (0, 6), 'I': (0, 7), 'O': (0, 8), 'P': (0, 9),
            'A': (1, 0), 'S': (1, 1), 'D': (1, 2), 'F': (1, 3), 'G': (1, 4),
            'H': (1, 5), 'J': (1, 6), 'K': (1, 7), 'L': (1, 8), ';': (1, 9),
            'Z': (2, 0), 'X': (2, 1), 'C': (2, 2), 'V': (2, 3), 'B': (2, 4),
            'N': (2, 5), 'M': (2, 6), ',': (2, 7), '.': (2, 8), '/': (2, 9)
        }
STARTING_FINGER = ['A', 'S', 'D', 'F', 'J', 'K', 'L', ';']

class keyboard():
    def __init__(self) -> None:
        self.design = KEYBOARD_LAYOUT
        self.fingerplacement = STARTING_FINGER
    
    def euclideanDistance(self,Point1, Point2):
        x1,y1 = Point1
        x2, y2 = Point2
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
 

    def distance(self, word):
        total_distance = 0
        distance_list = []
        fromto_list = []
        for letter in word:
            Point1 = self.design[letter]
            for fingeron in self.fingerplacement:
                Point2 = self.design[fingeron]
                temp_calculation = self.euclideanDistance(Point1,Point2)
                distance_list.append(temp_calculation)
                fromto_list.append((fingeron,letter))

        index_min_dist = distance_list.index(min(distance_list))
        where_from = fromto_list[index_min_dist][0]
        to = fromto_list[index_min_dist][1]
        
        self.fingerplacement[self.fingerplacement.index(where_from)] = to
        #where_from = self.design[fromto_list[index_min_dist][0]]
        #to = fromto_list[index_min_dist][1]
        #Change the fingerplacment list accordingly 

        #print(where_from, to)
        return self.fingerplacement
        #return min(distance_list)

                       
def main():
    keyboardinstant = keyboard()
    print(keyboardinstant.distance('H'))
    
if __name__ == "__main__":
    main()


