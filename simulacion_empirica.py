import matplotlib.pyplot as plt
import numpy as np
import time
from turingmachine import TuringMachine

sizes = list(range(12))
times = []

tm = TuringMachine("maquina.txt")

for n in sizes:
    input_string = "1" * n
    start = time.time()
    tm.run(input_string, show_steps=False)
    end = time.time()
    times.append(end - start)

plt.scatter(sizes, times)
plt.xlabel("Tamaño de entrada (n)")
plt.ylabel("Tiempo (s)")
plt.title("Tiempo de ejecución MT Fibonacci")
plt.show()

# Regresión polinomial
coeff = np.polyfit(sizes, times, 2)
poly = np.poly1d(coeff)

x = np.linspace(min(sizes), max(sizes), 100)
plt.scatter(sizes, times)
plt.plot(x, poly(x))
plt.show()
