from abc import ABC, abstractmethod
import math


class Figure(ABC):
    @abstractmethod
    def culc_square(self):
        pass
        

class Round(Figure):
    def __init__(self, r):
        if r<0:
            raise ValueError
        self.r = r

    def culc_square(self):
        return math.pi*self.r**2
    

class Triangle(Figure):
    def __init__(self, a, b, c):

        sides = [*set([a, b, c])]
        if sides[0]+sides[1]<=sides[2]:
            raise ValueError
        if sides[2] <= 0:
            raise ValueError
        
        if sides[0]**1 + sides[1]**2 == sides[2]**2:
            self.rect = True
        else: 
            self.rect = False
        self.a = sides[0]
        self.b = sides[1]
        self.c = sides[2]

    def culc_square(self):
        if self.rect:
            return self.a*self.b/2
        p = (self.a + self.b + self.c)/2
        return math.sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))
    

def calculate_figure(*sides):
    cls: Figure = None
    print(*sides)
    match len(sides):
        case 1:
            cls=Round
        case 3:
            cls=Triangle
        case _:
            raise ValueError()
    return cls(*sides).culc_square()
