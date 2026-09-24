from PIL import Image
from collections import defaultdict

class Neuron:
    def __init__(self,r,g,b):
        self.entries = [r,g,b]
        self.w = [0,0,0]
        self.sw = 0

    def train(self):
        line = self.entries[0] * self.w[0] + self.entries[1] * self.w[1] + self.entries[2] * self.w[2] > 0
        if line:
            self.kg1 -= 0.5 if self.r != 0 else 0
            self.kg2 -= 0.5 if self.g != 0 else 0
            self.kg3 -= 0.5 if self.b != 0 else 0
        else:
            self.kg1 += 0.5 if self.r != 0 else 0
            self.kg2 += 0.5 if self.g != 0 else 0
            self.kg3 += 0.5 if self.b != 0 else 0
        print("kg1 = " + str(self.kg1) + "\nkg2 = " + str(self.kg2) + "\nkg3 = " + str(self.kg3))
        print(self.r * self.kg1 + self.g * self.kg2 + self.b * self.kg3 if line else 0)

# Open an image file
img = Image.open('AIDATA/Test-Pictures/Apple1.jpg').convert("RGB")

width, height = img.size

pixels = {}
pixels = defaultdict(list)
notwhitepixels = []

for y in range(height):
    for x in range(width):
        r, g, b = img.getpixel((x, y))
        pixels[r, g, b]= x,y

for i in list(pixels.items()):
    if i[0][0] <= 240 and i[0][1] <= 240 and i[0][2] <= 240:
        notwhitepixels.append(i)

print(notwhitepixels)
for i in notwhitepixels:
    clone = Neuron(i[0][0],i[0][1],i[0][2])
    clone.train()
    