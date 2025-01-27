import numpy as np

def coordinate_descent(f, x0, tol=1e-6, max_iter=1000):
    """
    Покоординатный метод оптимизации (метод циклического покоординатного спуска)
    
    Параметры:
    f : callable
        Целевая функция для минимизации
    x0 : numpy array
        Начальная точка
    tol : float
        Точность для критерия остановки
    max_iter : int
        Максимальное количество итераций
    
    Возвращает:
    x : numpy array
        Точка минимума
    f_min : float
        Значение функции в точке минимума
    iterations : int
        Количество выполненных итераций
    """
    x = np.array(x0, dtype=float)
    n = len(x)
    iteration = 0
    
    while iteration < max_iter:
        x_old = x.copy()
        
        # Цикл по каждой координате
        for i in range(n):
            # Создаем функцию одной переменной, фиксируя остальные координаты
            def f_coordinate(t):
                x_temp = x.copy()
                x_temp[i] = t
                return f(x_temp)
            
            # Находим минимум по i-й координате методом золотого сечения
            x[i] = golden_section_search(f_coordinate, x[i]-1, x[i]+1, tol)
        
        # Проверяем условие остановки
        if np.linalg.norm(x - x_old) < tol:
            break
            
        iteration += 1
    
    return x, f(x), iteration

def golden_section_search(f, a, b, tol=1e-6):
    """
    Метод золотого сечения для поиска минимума функции одной переменной
    
    Параметры:
    f : callable
        Целевая функция
    a, b : float
        Границы интервала поиска
    tol : float
        Точность
        
    Возвращает:
    x : float
        Точка минимума
    """
    golden_ratio = (1 + np.sqrt(5)) / 2
    
    c = b - (b - a) / golden_ratio
    d = a + (b - a) / golden_ratio
    
    while abs(b - a) > tol:
        if f(c) < f(d):
            b = d
        else:
            a = c
            
        c = b - (b - a) / golden_ratio
        d = a + (b - a) / golden_ratio
    
    return (a + b) / 2

# Пример использования
if __name__ == "__main__":
    # Тестовая функция (например, функция Розенброка)
    def rosenbrock(x):
        return 100 * (x[1] - x[0]**2)**2 + (1 - x[0])**2
    
    # Начальная точка
    x0 = np.array([-1.0, 1.0])
    
    # Запуск оптимизации
    x_min, f_min, iterations = coordinate_descent(rosenbrock, x0)
    
    print(f"Минимум найден в точке: {x_min}")
    print(f"Значение функции в минимуме: {f_min}")
    print(f"Количество итераций: {iterations}")
