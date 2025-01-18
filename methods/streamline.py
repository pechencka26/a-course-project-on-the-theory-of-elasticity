
import math
import os
import numpy as np
import matplotlib.pyplot as plt

class StrLine:
    def __init__(self, time):
        self.time = time
        self.x, self.y = np.meshgrid(
            np.linspace(-5, 5, 1000), np.linspace(-5, 5, 1000)
        )
        # Поле скоростей
        self.v_x = self.x * math.sin(self.time)
        self.v_y = self.y * math.exp(self.time)

    def graf(self, save_dir):
        fig, axes = plt.subplots(1, 2, figsize=(16, 6))

        # Линии тока (streamplot использует поле скоростей для вычисления)
        colormass = np.sqrt(self.v_x**2 + self.v_y**2)
        axes[0].streamplot(
            self.x,
            self.y,
            self.v_x,
            self.v_y,
            color=colormass,
            density=2,
            linewidth=0.5,
            cmap="viridis",
        )
        axes[0].set_title(f"Линии тока, t = {self.time:.2f}")
        axes[0].set_xlabel("x")
        axes[0].set_ylabel("y")
        axes[0].grid()

        # Поле скоростей
        axes[1].quiver(
            self.x[::30, ::30],
            self.y[::30, ::30],
            self.v_x[::30, ::30],
            self.v_y[::30, ::30],
            color="blue",
        )
        axes[1].set_title(f"Поле скоростей, t = {self.time:.2f}")
        axes[1].set_xlabel("x")
        axes[1].set_ylabel("y")
        axes[1].grid()

        # Сохранение попарного графика
        save_path = os.path.join(
            save_dir, f"streamline_and_velocity_time_{round(self.time, 1)}_second.jpeg"
        )
        plt.savefig(save_path, format="jpeg", dpi=500)
        plt.close()
