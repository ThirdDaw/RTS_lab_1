import random
import math
import matplotlib.pyplot as plt
from datetime import datetime
import time
import numpy

harmNumber = 14
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

alg_time = []
for i in range(500, 1500, 5):
    dotNumber = i
    # time_start = datetime.now()
    start = time.time()
    mainX = []
    for i in range(dotNumber):
        currentX = 0
        for j in range(harmNumber):
            currentX += ampls[j] * math.sin(omegaInterval * (j + 1) * i + phases[j])
        mainX.append(currentX)
    # time_finish = datetime.now()
    finish = time.time()
    alg_time.append(finish - start)
print(alg_time)
# for_schema = [i.microseconds for i in alg_time]

plt.xlabel("Dots")
plt.ylabel("Time")
plt.plot(range(500, 1500, 5), alg_time)
plt.show()

# print(mainX)

# mathExp = sum(mainX) / dotNumber
#
# diffXpow2 = []
# for i in range(dotNumber):
#     diffXpow2.append(math.pow(mainX[i] - mathExp, 2))
# # disp = sum(diffX) / (dotNumber - 1)
# disp = sum(diffXpow2) / dotNumber
#
# print(mathExp)
# print(disp)

# plt.xlabel("X")
# plt.ylabel("T")
# plt.plot(mainX)
# plt.show()
