from random import randint
from collections import defaultdict
import json

#Defining variables
neurons = []
wantedOutput = True
limit = 80
entry1 = 50
entry2 = 30.01
points = 0
minuspoints = 0
x = 0
y = 0
maxTrainingSteps = 500
allNeurons = 500
newConfig = True

#Import old Neuron config if wanted
with open("AIDATA/config.json", "r", encoding="utf-8") as f:
    if newConfig == True:
        neuralWeights = defaultdict(list)
    else:
        neuralWeights = json.load(f)
    


#Make a Neuron
class Neuron:
    def __init__(self, x:float,y:float):
        self.x = x
        self.y = y
    def activate(self, entry1:float, entry2:float, limit:float):
        return entry1 * self.x + entry2 * self.y > limit


#Give every Neuron its weights
for neuronInCreation in range(allNeurons):
    if len(neuralWeights) > neuronInCreation:
        x = neuralWeights[f"neuron{neuronInCreation}"][0]
        y = neuralWeights[f"neuron{neuronInCreation}"][1]
    else:
        x = randint(0,100)/100
        y = randint(0,100)/100
    neuralWeights[f"neuron{neuronInCreation}"] = (x, y)
    neurons.append(Neuron(x,y))


#Configurate the weights of the Neurons to get the wanted Output (Training process)
for trainingStep in range(maxTrainingSteps): 
    points = 0
    minuspoints = 0

    for neuronInConfig in range(len(neuralWeights)):
        #Output of Neuron
        fire = neurons[neuronInConfig].activate(entry1, entry2, limit) 

        #Checking if the output is right
        if fire == wantedOutput:
            points += 1
        else:
            minuspoints += 1

            #Adjusting the Weights
            if fire == True:
                if neurons[neuronInConfig].x > 0:
                    neurons[neuronInConfig].x = round(neurons[neuronInConfig].x - 0.01 , 2)
                if neurons[neuronInConfig].y > 0:
                    neurons[neuronInConfig].y = round(neurons[neuronInConfig].y - 0.01 , 2)
            else:
                if neurons[neuronInConfig].x < 1:
                    neurons[neuronInConfig].x = round(neurons[neuronInConfig].x + 0.01 , 2)
                if neurons[neuronInConfig].y < 1:
                    neurons[neuronInConfig].y = round(neurons[neuronInConfig].y + 0.01 , 2)
                
                    

    #Partial results of training
    print(f"{points} right, {minuspoints} wrong")


    if minuspoints == 0:
        break #End of training

#Returning entirety of Trainings
print(f"\n{trainingStep} Trainings done\n")

#Saving Config
for neuronInSaving in range(len(neuralWeights)):
    neuralWeights[f"neuron{neuronInSaving}"] = (neurons[neuronInSaving].x, neurons[neuronInSaving].y)

#Uploading Config
with open("AIDATA/config.json", "w", encoding="utf-8") as f:
    neuralWeights = json.dump(neuralWeights,f)

