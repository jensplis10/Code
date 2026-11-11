from random import randint
from collections import defaultdict

neurons = []
with open("AIDATA/config.json", "w", encoding="utf-8") as f:
    neuralWeights = f
    neuralWeights = defaultdict(list)

class Neuron:
    def __init__(self, x:float,y:float):
        self.x = x
        self.y = y
    def activate(self, entry1:float, entry2:float, sw:float):
        return entry1 * self.x + entry2 * self.x> sw



for i in range(100):
    x = randint(-100,100)/100
    y = randint(-100,100)/100
    neuralWeights[f"neuron{i}"] = (x, y)
    neurons.append(Neuron(x,y))

for i in range(5):
    print(neurons[i].x, neurons[i].y)


print(neurons[2].activate(50, 50, 50))

#f = (neuralWeights)






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