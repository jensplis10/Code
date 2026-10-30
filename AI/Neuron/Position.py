from random import randint


class weight:
    def __init__(self, x:float=0.0, y:float=0.0, z:float=0.0):
        self.x = x
        self.y = y
class firstLayerNeuron:
    def __init__(self, weight:weight):
        self.weight = weight


auto = firstLayerNeuron(weight((randint(-100,100))/100, (randint(-100,100))/100))
print(auto.weight.x)

neuronsFirst = firstLayerNeuron
