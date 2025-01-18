import numpy as np

class RungeKutta:
    def __init__(self, lifetime, h):
        self.lifetime = lifetime  # Временной интервал
        self.step = h  # Шаг времени
        self.result_x = None
        self.result_y = None
        self.result_t = None
        # Коэффициенты таблицы Бутчера
        self.a = np.array([
            [0, 0, 0],
            [0.5, 0, 0],
            [-1, 2, 0]
        ])
        self.b = np.array([1 / 6, 4 / 6, 1 / 6])
        self.c = np.array([0, 0.5, 1])

    def f(self, t, x, y):
        dx_dt = np.sin(t) * x
        dy_dt = np.exp(t) * y
        return np.array([dx_dt, dy_dt])

    def runge_kutta_step(self, t, x_r):
        h = self.step
        k1 = self.f(t, x_r[0], x_r[1])
        k2 = self.f(t + self.c[0] * h, x_r[0] + self.a[1, 0] * h * k1[0], x_r[1] + self.a[1, 0] * h * k1[1])
        k3 = self.f(t + self.c[1] * h,
                    x_r[0] + self.a[2, 0] * h * k1[0] + self.a[2, 1] * h * k2[0],
                    x_r[1] + self.a[2, 0] * h * k1[1] + self.a[2, 1] * h * k2[1])
        return x_r + h * np.dot(self.b, [k1, k2, k3])

    def solve(self, x_points, y_points):
        t_start, t_end = self.lifetime
        t_values = np.arange(t_start, t_end + self.step, self.step)
        self.result_t = t_values

        num_points = len(x_points)
        num_times = len(t_values)

        results_x = np.zeros((num_points, num_times))
        results_y = np.zeros((num_points, num_times))

        # Интеграция для каждой точки
        for idx, (x0, y0) in enumerate(zip(x_points, y_points)):
            x_values = np.zeros_like(t_values)
            y_values = np.zeros_like(t_values)

            # Установка начальных условий
            x_values[0] = x0
            y_values[0] = y0

            # Интеграция методом Рунге-Кутты
            current_position = np.array([x0, y0])
            for i in range(1, num_times):
                current_position = self.runge_kutta_step(t_values[i - 1], current_position)
                x_values[i], y_values[i] = current_position

            results_x[idx] = x_values
            results_y[idx] = y_values

        self.result_x = results_x
        self.result_y = results_y
        return results_x, results_y
