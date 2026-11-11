from random import randint
from collections import defaultdict

neurons = []
wantedOutput = True
with open("AIDATA/config.json", "w", encoding="utf-8") as f:
    neuralWeights = f
    neuralWeights = defaultdict(list)

class Neuron:
    def __init__(self, x:float,y:float):
        self.x = x
        self.y = y
    def activate(self, entry1:float, entry2:float, sw:float):
        return entry1 * self.x + entry2 * self.x > sw



for i in range(100):
    x = randint(-100,100)/100
    y = randint(-100,100)/100
    neuralWeights[f"neuron{i}"] = (x, y)
    neurons.append(Neuron(x,y))

for i in range(5):
    print(neurons[i].x, neurons[i].y)


for i in range(100):
    for j in range(100):
        fire = neurons[j].activate(50, 50, 50)
        print(neurons[j].activate(50, 50, 50))



        if fire == False and wantedOutput == True or fire == True and wantedOutput == 0:
            if fire == True:
                neurons[j].x -= 0.01
                neurons[j].y += 0.01
            else:
                neurons[j].x += 0.01
                neurons[j].y -= 0.01

for i in range(100):
    neurons.activate(50,50,50)