from random import randint


class weight:
    def __init__(self, x:float=0.0, y:float=0.0, z:float=0.0):
        self.x = x
        self.y = y
class firstLayerNeuron:
    def __init__(self, weight:weight):
        self.weight = weight




neuronsFirst = [firstLayerNeuron(weight((randint(-100,100))/100, (randint(-100,100))/100)) for _ in range(100)]
print(neuronsFirst[3].weight.x, neuronsFirst[3].weight.y)
