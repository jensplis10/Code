from random import randint


class weight:
    def __init__(self, x:float=0.0, y:float=0.0, z:float=0.0):
        self.x = x
        self.y = y
        self.z = z
class firstLayerNeuron:
    def __init__(self, position:weight):
        self.position = position


auto = firstLayerNeuron(weight((randint(-100,100))/100, (randint(-100,100))/100, (randint(-100,100))/100))
print(auto.position.x)

neuronsFirst = firstLayerNeuron
