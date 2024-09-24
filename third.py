import math

epsilon = 1e-4


def f(x):
    return x ** 3 - 4 * x ** 2 - 4 * x + 13

def phi(x):
    return  -math.sqrt(x**3 -4*x + 13)/2
def df(x):
    return 3 * x ** 2 - 8 * x - 4

def apriori_estimation_iteration(q):
    return round(math.log(abs( (phi(-1.8) + 1.8) / (1 - q) / epsilon))/ math.log(1/q)) + 1

def newton_method_with_table(x0, max_iter=100):
    iter_count = 0
    table = []

    while iter_count < max_iter:
        f_x0 = f(x0)
        df_x0 = df(x0)

        if df_x0 == 0:
            print("Похідна дорівнює нулю. Метод не може продовжуватися.")
            break

        x1 = x0 - f_x0 / df_x0
        error = abs(x1 - x0)

        table.append((iter_count, x0, error))

        if error < epsilon:
            break

        x0 = x1
        iter_count += 1

    return x1, table, iter_count


def simple_iteration_method_with_table(x0, q, max_iter=100):
    iter_count = 0
    table = []

    while iter_count < max_iter:
        x1 = phi(x0)
        error = abs(x1 - x0)


        table.append((iter_count, x0, error))

        if error < ((1-q)/q)*epsilon:
            break

        x0 = x1
        iter_count += 1

    return x1, table, iter_count

def print_table(table):
    print("{:<10}  {:<20} {:<20}".format("Ітерація", "x_n", "f(x_n)"))
    print("-" * 60)
    for row in table:
        iter_count, xn, error = row
        print("{:<10}  {:<20} {:<20}".format(iter_count, f"{xn:.10f}",
                                                          f"{error:.10e}"))



def apriori_estimation_relaxation_n(q):
    return math.log(round((math.log(0.12/epsilon))/(math.log(1/q)) + 1), 2) + 1


x0 = -1.87
q = 0.05


root, result_table, iterations = newton_method_with_table(x0)


print("Метод Ньютона")
apriori_iters = apriori_estimation_relaxation_n(0.05)
print(f"Апріорна кількість ітерацій: {apriori_iters}")
print(f"Знайдений корінь: {root:.10f}")
print(f"Фактична кількість ітерацій:: {iterations}")
print("Апостеріорна оцінка кількості кроків:")
print_table(result_table)

print("Метод простої ітерації")
print(f"Апріорна кількість ітерацій: {apriori_estimation_iteration(q)}")
root, result_table, iterations = simple_iteration_method_with_table(-1.8, q)
print(f"Знайдений корінь: {root:.10f}")
print(f"Фактична кількість ітерацій: {iterations}")
print("Апостеріорна оцінка кількості кроків:")
print_table(result_table)
