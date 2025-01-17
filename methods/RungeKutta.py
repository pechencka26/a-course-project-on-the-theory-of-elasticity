import numpy as np
from models.body import CirclePoints

class RungeKutta(CirclePoints):
    def __init__(self, num_points, lifetime, h):
        super().__init__(num_points, lifetime)
        self.result_points = None  # Массив результатов для каждой точки
        self.step = h
        self.result_x = None # для траектории
        self.result_y = None # для траектории
        self.result_t = None # для траектории
        # Коэффициенты таблицы Бутчера (для метода с 4 стадиями)
        #Серединные коэффициенты таблицы Бутчера
        self.a = np.array([
            [0, 0, 0],
            [0.5, 0, 0],
            [-1, 2, 0]
        ])
        #Нижние кф таблицы Бутчера
        self.b = np.array([1/6, 4/6, 1/6])
        #Левые кф таблицы Бутчера
        self.c = np.array([0, 0.5, 1])
        self.solve()

    def f(self, t, x, y):
        dx_dt = np.sin(t) * x
        dy_dt = np.exp(t) * y
        return dx_dt, dy_dt

    def solve(self):
        self.generate_points() # Вызывает родительский метод который генерирует точки
        t_start, t_end = self.lifetime
        t_values = np.arange(t_start, t_end + self.step, self.step)
        self.result_t = t_values
        u = 0      # счетчик
        results = []  # Для хранения решений для всех начальных точек
        results_x = np.zeros((len(self.x_points), len(t_values)))   # двумерный массив иксов и игриков
        results_y = np.zeros((len(self.x_points), len(t_values))) # где номер строки это номер точки, а строка - координаты для траектории
        for x0, y0 in zip(self.x_points, self.y_points):
            x_values = np.zeros_like(t_values)
            y_values = np.zeros_like(t_values)

            # Установка начальных условий для текущей точки
            x_values[0] = x0
            y_values[0] = y0

            for i in range(1, len(t_values)):
                t = t_values[i - 1]
                x = x_values[i - 1]
                y = y_values[i - 1]

                # Вычисление стадий
                kx = np.zeros(len(self.c))
                ky = np.zeros(len(self.c))
                for j in range(len(self.c)):
                    t_stage = t + self.c[j] * self.step
                    x_stage = x + self.step * np.dot(self.a[j, :j], kx[:j])
                    y_stage = y + self.step * np.dot(self.a[j, :j], ky[:j])
                    kx[j], ky[j] = self.f(t_stage, x_stage, y_stage)

                # Вычисление следующего значения x и y
                x_values[i] = x + self.step * np.dot(self.b, kx)
                y_values[i] = y + self.step * np.dot(self.b, ky)

            results.append((x_values, y_values))
            results_x[u] = x_values
            results_y[u] = y_values
            u += 1
        self.result_x = results_x
        self.result_y = results_y
        self.result_points = results
        return results
