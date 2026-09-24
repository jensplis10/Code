global index
global entry1
global entry2
global output
exit = False
index = 0
kg1 = -1
kg2 = 1.5
sw = 0.5
wanted_output = [[0,0,0],
 [0,1,0],
 [1,0,1],
 [1,1,1]]
entry1 = wanted_output[index][0]
entry2 = wanted_output[index][1]
output = wanted_output[index][2]
def next():
    global index
    global entry1
    global entry2
    global output
    index = index + 1 if index < len(wanted_output) - 1 else 0
    entry1 = wanted_output[index][0]
    entry2 = wanted_output[index][1]
    output = wanted_output[index][2]

while exit == False:
    line = entry1 * kg1 + entry2 * kg2 > sw
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
    next()
print("kg1 = " + str(kg1) + "\nkg2 = " + str(kg2) + "\nsw = " + str(sw))