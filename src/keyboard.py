import math
'''
This file initializes the layout of the current keyboard and calculates
the distance function from different rows/keys.

Some bold assumptions in keyboard: 
1) Your finger starts at A,S,D,F,J,K,L.
2) Only move one finger at a time, keeping the other where they are.
3) There are some unnatural way of fingers combinations of finger movement which do not feel 
comfortable or natural whilst typing however with practice still acheivable. 
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
    

    def getKey(self,target):
        keys = [key for key, value in self.design.items() if value == target]
        return keys[0]

    def distance(self, word):
        total=0
        distance = []
        points = []
        for letters in word:
            point1 = self.design[letters]
            for fingers in self.fingerplacement:
                point2 = self.design[fingers]
                #Calculate distance
                distance_between_points = self.euclideanDistance(point1,point2)
                distance.append(distance_between_points)
                points.append((point2,point1))
            #Get the index of the minimum
            total += min(distance)
            index_minimum = distance.index(min(distance))
            from_finger = points[index_minimum][0]
            to_finger = points[index_minimum][1]
            distance.clear()
            points.clear()
            self.fingerplacement[self.fingerplacement.index(self.getKey(from_finger))] = self.getKey(to_finger)
            
        return total
                                
def main():
    keyboardinstant = keyboard()
    print(keyboardinstant.distance('ZEMQ'))
    
if __name__ == "__main__":
    main()

