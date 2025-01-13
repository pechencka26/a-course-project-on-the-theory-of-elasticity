import math
import numpy as np
import matplotlib.pyplot as plt
class StrLine:
    def __init__(self, time):
        self.time = time
        self.x, self.y = np.meshgrid(np.linspace(-5, 5, 1000), np.linspace(-5, 5, 1000))
        self.v_x = self.x * (math.sin(self.time))  # уравнения задающие поле скоростей в момент времени t
        self.v_y = self.y * math.exp(self.time)
    def graf(self):
        # Построение линий тока
        colormass = np.sqrt(self.v_y**2+self.v_x**2)
        plt.figure(figsize=(8, 6))
        plt.streamplot(self.x, self.y, self.v_x, self.v_y, color=colormass, density=3, linewidth=0.5)
        plt.title(f"Линии тока в момент времени t = {self.time:.2f}")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.grid()

