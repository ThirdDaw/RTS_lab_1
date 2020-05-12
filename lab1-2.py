import random
import math
import matplotlib.pyplot as plt
import numpy

harmNumber = 14
dotNumber = 64
omegaMax = 2500
omegaInterval = omegaMax / harmNumber

ampl = random.randint(1, 10)
ampls = []
for i in range(harmNumber):
    ampls.append(random.randint(1, 10))

# print(ampl)

phase = 0
phases = []
for i in range(harmNumber):
    phases.append(random.uniform(0, math.pi))
# print(phase)

mainX = []
for i in range(dotNumber):
    currentX = 0
    for j in range(harmNumber):
        currentX += ampls[j] * math.sin(omegaInterval * (j + 1) * i + phases[j])
    mainX.append(currentX)

mathExp = sum(mainX) / dotNumber

diffXpow2 = []
for i in range(dotNumber):
    diffXpow2.append(math.pow(mainX[i] - mathExp, 2))
# disp = sum(diffX) / (dotNumber - 1)
disp = sum(diffXpow2) / dotNumber

covXX = sum(diffXpow2) / dotNumber
rXX = covXX / disp
print(rXX)

newPhase = [i + math.pi * 2 for i in phases]
newMainX = []
for i in range(dotNumber):
    currentX = 0
    for j in range(harmNumber):
        currentX += ampls[j] * math.sin(omegaInterval * (j + 1) * i + newPhase[j])
    newMainX.append(currentX)

newMathExp = sum(newMainX) / dotNumber

diffX = []
for i in range(dotNumber):
    diffX.append(mainX[i] - mathExp)

diffNewX = []
for i in range(dotNumber):
    diffNewX.append(newMainX[i] - newMathExp)

composition = []
for i in range(dotNumber):
    composition.append(diffX[i] * diffNewX[i])

covXnewX = sum(composition) / dotNumber

diffNewXpow2 = []
for i in range(dotNumber):
    diffNewXpow2.append(math.pow(newMainX[i] - newMathExp, 2))
# disp = sum(diffX) / (dotNumber - 1)
newDisp = sum(diffNewXpow2) / dotNumber

rXnewX = covXnewX / (math.sqrt(disp) * math.sqrt(newDisp))
print(rXnewX)

plt.xlabel("X")
plt.ylabel("T")
plt.plot(newMainX)
plt.show()
