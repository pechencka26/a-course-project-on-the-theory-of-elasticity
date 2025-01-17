from methods.streamline import StrLine
from methods.RungeKutta import RungeKutta
import matplotlib.pyplot as plt
import os

# Заданные параметры
lifetime = 1
num_points = 100  # Количество точек
h = 0.1  # Шаг метода Рунге-Кутты

# Создание папки для сохранения, если её нет
save_dir = 'C:/Users/Lenovo/Desktop/прога/PythonProject/plots'
os.makedirs(save_dir, exist_ok=True)

# Список временных моментов
time_values = [0, 0.5, 1, 2, 3, 5, 10]

# Построение и сохранение графиков линий тока
for t in time_values:
    grafik = StrLine(t)  # Объект для текущего времени
    grafik.graf(save_dir)  # Сохранение графиков линий тока

# Расчёт траекторий с помощью метода Рунге-Кутты
rk = RungeKutta(num_points, lifetime, h)

# Построение начальной и деформированной формы в каждый момент времени
for t_idx, t in enumerate(time_values):
    plt.figure(figsize=(10, 6))

    # Начальное состояние точек
    plt.scatter(rk.x_points, rk.y_points, color="green", label="Начальные точки", zorder=3)

    # Деформированное состояние точек в текущий момент времени
    if t_idx < rk.result_x.shape[1]:  # Проверка на доступность времени
        x_coords = rk.result_x[:, t_idx]
        y_coords = rk.result_y[:, t_idx]
        plt.scatter(x_coords, y_coords, color="red", label=f"Деформированная форма t={t} сек", zorder=3)

        # Траектории точек до текущего времени
        for i in range(len(rk.result_x)):
            plt.plot(rk.result_x[i, :t_idx + 1], rk.result_y[i, :t_idx + 1], linestyle="--", alpha=0.7, color="gray")

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
    plt.close()  # Закрываем текущую фигуру
