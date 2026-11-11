from random import randint
from collections import defaultdict

neurons = []
wantedOutput = False
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
    x = randint(0,100)/100
    y = randint(0,100)/100
    neuralWeights[f"neuron{i}"] = (x, y)
    neurons.append(Neuron(x,y))

for i in range(5):
    print(neurons[i].x, neurons[i].y)


for i in range(500):
    points = 0
    minuspoints = 0
    for j in range(100):
        fire = neurons[j].activate(50, 50, 50)
        if fire == wantedOutput:
            points += 1
        else:
            minuspoints += 1
        



        if fire == False and wantedOutput == True or fire == True and wantedOutput == 0:
            if fire == True:
                if neurons[j].x > 0:
                    neurons[j].x -= 0.01
                if neurons[j].y > 0:
                    neurons[j].y -= 0.01
            else:
                if neurons[j].x < 1:
                    neurons[j].x += 0.01
                if neurons[j].y < 1:
                    neurons[j].y += 0.01
        neuralWeights[f"neuron{j}"] = (neurons[j].x, neurons[j].y)

    print(points,minuspoints)
    if minuspoints == 0:
        break


print("-------------------------------------\n\n\n")
points = 0
minuspoints = 0
for i in range(100):
    if neurons[i].activate(50,50,50) == True:
        points += 1
    else:
        minuspoints += 1

print(points,minuspoints)


for i in range(100):
    print(round(neuralWeights[f"neuron{i}"][0]*100)/100 , round(neuralWeights[f"neuron{i}"][1]*100)/100)

print(50 * 0.03 + 50 * 0.92 > 50)