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

# print(mainX)

mathExp = sum(mainX) / dotNumber

diffXpow2 = []
for i in range(dotNumber):
    diffXpow2.append(math.pow(mainX[i] - mathExp, 2))
# disp = sum(diffX) / (dotNumber - 1)
disp = sum(diffXpow2) / dotNumber

print(mathExp)
print(disp)

plt.xlabel("X")
plt.ylabel("T")
plt.plot(mainX)
plt.show()