from methods.streamline import StrLine
from methods.trajectory import Trajectory
from models.body import MaterialCircle
from methods.RungeKutta import RungeKutta

import matplotlib.pyplot as plt
import os


# Создание папки для сохранения, если её нет
save_dir = 'C:/Users/Lenovo/Desktop/прога/PythonProject/plots'


# Список временных моментов
time_values = [0, 0.5, 1, 2, 3, 5, 10]

# Построение и сохранение графиков линий тока и поля скоростей
for t in time_values:
    grafik = StrLine(t)  # Объект для текущего времени
    grafik.graf(save_dir)  # Сохранение графиков линий тока и поля скоростей

# Расчёт траекторий с помощью метода Рунге-Кутты
circle = MaterialCircle(radius=3, center=(4, 4))
circle.generate_points(num_points=100)
x_points, y_points = zip(*circle.get_points())

# Инициализация Рунге-Кутты
rk = RungeKutta(lifetime=(0, 1), h=0.1)
result_x, result_y = rk.solve(x_points, y_points)

selected_index = 0  # Индекс первой точки
selected_x = result_x[selected_index]
selected_y = result_y[selected_index]
# Создание объекта Trajectory для выбранной точки
trajectory = Trajectory(selected_x, selected_y)
# Визуализация траектории
save_path = os.path.join(save_dir, 'trajectory_of_selected_point.jpeg')
trajectory.plot_trajectory(save_path=save_path)

# Вывод координат траектории
trajectory_points = [(round(float(x), 2), round(float(y), 2)) for x, y in trajectory.get_trajectory()]
print(f"Траектория точки {circle.get_points()[selected_index]}:")
print(trajectory_points)

# Построение начальной и деформированной формы в каждый момент времени
for t_idx, t in enumerate(time_values):
    plt.figure(figsize=(10, 6))

    # Начальное состояние точек
    plt.scatter(x_points, y_points, color="green", label="Начальные точки", zorder=3)

    # Деформированное состояние точек в текущий момент времени
    if t_idx < result_x.shape[1]:  # Проверка на доступность времени
        x_coords = result_x[:, t_idx]
        y_coords = result_y[:, t_idx]
        plt.scatter(x_coords, y_coords, color="red", label=f"Деформированная форма t={t} сек", zorder=3)

        # Траектории точек до текущего времени
        for i in range(len(result_x)):
            plt.plot(result_x[i, :t_idx + 1], result_y[i, :t_idx + 1], linestyle="--", alpha=0.7, color="gray")

    # Оформление графика
    plt.title(f"Начальная и деформированная форма окружности (время = {t} секунд)")
    plt.xlabel("X координаты")
    plt.ylabel("Y координаты")
    plt.axis("equal")  # Сохранение пропорций для корректного отображения круга
    plt.legend(loc="best")
    plt.grid()

    # Сохранение графика начальной и деформированной формы
    save_path = os.path.join(save_dir, f'deformation_time_{round(t, 1)}_second.jpeg')
    plt.savefig(save_path, format='jpeg', dpi=500)
    plt.close()