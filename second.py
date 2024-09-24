import math


epsilon = 1e-4


def f(x):
    return 3 * x + math.cos(x) + 1


def df(x):
    return 3 - math.sin(x)

def apriori_estimation_bisection(a, b):
    return round(math.log2(abs((b - a) / epsilon)))
def bisection_method_with_table(a, b, max_iter=100):
    iter_count = 0
    table = []
    while iter_count < max_iter:
        x0 = (a + b) / 2
        error = abs(b - a) / 2

        table.append((iter_count, x0, error))

        if error < epsilon:
            break

        if f(x0) == 0:
            break
        elif f(a) * f(x0) < 0:
            b = x0
        else:
            a = x0

        iter_count += 1

    return x0, table, iter_count


def apriori_estimation_relaxation(a, b):
    return round(math.log(0.25 / epsilon) / math.log((b+a)/(b-a))) + 1


def relaxation_method_with_table(x0, tau, max_iter=100):
    iter_count = 0
    table = []

    while iter_count < max_iter:
        x1 = x0 - tau * f(x0)
        error = abs(x1 - x0)

        table.append((iter_count, x0, error))

        if error < epsilon:
            break

        x0 = x1
        iter_count += 1

    return x1, table, iter_count

def print_table(table):
    print("{:<10} {:<20} {:<20}".format("Ітерація", "x_n", "f(x_n)"))
    print("-" * 60)
    for row in table:
        iter_count, xn, error = row
        print("{:<10} {:<20} {:<20}".format(iter_count, f"{xn:.10f}", f"{error:.10e}"))

a = -1
b = -0.5
x0 = -0.75
m1 = 2
M1 = 4
tau_opt = 2 / (m1 + M1)


root, result_table1, iterations1 = relaxation_method_with_table(x0, tau_opt)
print("Метод дихотомії")
root, result_table, iterations = bisection_method_with_table(a, b)
print(f"Знайдений корінь: {root:.10f}")
print(f"Фактична кількість ітерацій: {iterations}")
apriori_iters = apriori_estimation_bisection(a, b)
print(f"Апріорна кількість ітерацій: {apriori_iters}")
print(f"Апостеріорна оцінка кількості кроків:")
print_table(result_table)
print("Метод релаксації")
apriori_iters = apriori_estimation_relaxation(m1, M1)
print(f"Апріорна кількість ітерацій: {apriori_iters}")
print(f"Знайдений корінь: {root:.10f}")
print(f"Фактична кількість ітерацій: {iterations1}")
print("Апостеріорна оцінка кількості кроків:")
print_table(result_table1)
