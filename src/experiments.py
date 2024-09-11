from drama import oscar
import matplotlib.pyplot as plt
from tqdm import tqdm

initial_altitude = []
lifetime_results = []
r_earth = 6378 

for i in tqdm(range(100, 700, 10)):
    results = oscar.run(sma=r_earth + i, parallel=False)
    initial_altitude.append(r_earth + i)
    lifetime_results.append(results["results"][0]["lifetime"])

print(results["results"][0]["lifetime"])


plt.plot(initial_altitude, lifetime_results)
plt.yscale("log")
plt.grid()
plt.savefig("test.jpg")