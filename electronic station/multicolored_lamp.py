'''
Create a lamp that changes color at every .light() call
'''

class Lamp:

    def __init__(self):
        self.lamp = self.colors()

    def light(self):
        return next(self.lamp)

    def colors(self):
        i = 0
        colors = {0 : "Green", 1: "Red", 2: "Blue", 3: "Yellow"}
        while True:
            yield colors[i]
            i = (i+1) % 4

    
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    lamp_1 = Lamp()
    lamp_2 = Lamp()

    lamp_1.light() #Green
    lamp_1.light() #Red
    lamp_2.light() #Green
    
    assert lamp_1.light() == "Blue"
    assert lamp_1.light() == "Yellow"
    assert lamp_1.light() == "Green"
    assert lamp_2.light() == "Red"
    assert lamp_2.light() == "Blue"
    print("Coding complete? Let's try tests!")
