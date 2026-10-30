class Vector2:
    def __init__(self, x:float=0.0, y:float=0.0):
        self.x = x
        self.y = y
class firstLayerNeuron:
    def __init__(self, position:Vector2):
        self.position = position
auto = firstLayerNeuron(Vector2(1, 2))
print(auto.position.x)
