import numpy as np
import matplotlib
import matplotlib.pyplot as plt

drift = 0.1
vol = 0.3
time = 1
steps = 100
samples = 100

def gbm(S0, mu, sigma, t):
    return S0 * np.exp((mu - sigma ** 2 / 2) * t
                       + sigma * np.random.normal(0,np.sqrt(t)))

dtime = time / steps
for j in range(samples):
    current = 100
    x = [i for i in range(steps + 1)]
    y = [current]
    for i in range(steps):
        price = gbm(current, drift, vol, dtime)
        current = price
        y.append(price)
    plt.plot(x,y)
plt.show()
