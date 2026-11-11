from random import randint


class weight:
    def __init__(self, x:float=randint(-100,100)/100, y:float=randint(-100,100)/100):
        self.x = x
        self.y = y
class Neuron:
    def __init__(self, weight:weight):
        self.weight = weight




neuronsFirst = [Neuron(weight()) for _ in range(100)]
print(neuronsFirst[3].weight.x, neuronsFirst[3].weight.y)
