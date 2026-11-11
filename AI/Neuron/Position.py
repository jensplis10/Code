from random import randint


class weight:
    def __init__(self, x:float=randint(-100,100)/100, y:float=randint(-100,100)/100):
        self.x = x
        self.y = y
class Neuron:
    def __init__(self, weight:weight):
        self.weight = weight
    def activate(self, entry1:float, sw:float):
        return entry1 * self.weight.x > sw




neuronsFirst = [Neuron(weight()) for _ in range(100)]
print(neuronsFirst[3].weight.x, neuronsFirst[3].weight.y)


print(neuronsFirst[2].activate(100, 50))








"""
if line == False and output == 1 or line == True and output == 0:
    if line == True:
        kg1 = kg1 - 0.5 if entry1 == 1 else kg1
        kg2 = kg2 - 0.5 if entry2 == 1 else kg2
        sw = sw + 0.5
    else:
        kg1 = kg1 + 0.5 if entry1 == 1 else kg1
        kg2 = kg2 + 0.5 if entry2 == 1 else kg2
        sw = sw - 0.5
for i in range(0, len(wanted_output)):
    fire = wanted_output[i][0] * kg1 + wanted_output[i][1] * kg2 > sw
    if fire == True and wanted_output[i][2] == 1:
        print("Line " + str(i) + " fires correctly")
    elif fire == False and wanted_output[i][2] == 0:
        print("Line " + str(i) + " fires correctly")
    else:
        print("Line " + str(i) + " fires incorrectly")
        break
    exit = True if i == len(wanted_output) - 1 else False

"""