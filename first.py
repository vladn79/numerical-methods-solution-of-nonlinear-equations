import math

e = 1e-4


def f(x):
    return x**3 - 3*x**2 - 14*x - 8

def phi(x):
    return  math.sqrt(3*x + 8/x + 14)


def apriori_estimation_bisection(a, b):
    return round(math.log2(abs((b - a) / e)))
def bisection_method_with_table(a, b, max_iter=100):
    iter_count = 0
    table = []
    while iter_count < max_iter:
        x0 = (a + b) / 2
        error = abs(b - a) / 2

        table.append((iter_count, x0, error))

        if error < e:
            break

        if f(x0) == 0:
            break
        elif f(a) * f(x0) < 0:
            b = x0
        else:
            a = x0

        iter_count += 1

    return x0, table, iter_count


def simple_iteration_method_with_table(x0, q, max_iter=100):
    iter_count = 0
    table = []

    while iter_count < max_iter:
        x1 = phi(x0)
        error = abs(x1 - x0)


        table.append((iter_count, x0, error))

        if error < ((1-q)/q)*e:
            break

        x0 = x1
        iter_count += 1

    return x1, table, iter_count

def apriori_estimation_iteration(q):
    return round(math.log(abs( (phi(5.75) - 5.75) / (1 - q) / e))/ math.log(1/q)) + 1

def print_table(table):

    print("{:<10} {:<20} {:<20}".format("Ітерація", "x_n", "f(x_n)"))
    print("-" * 60)
    for row in table:
        iter_count, xn, error = row
        print("{:<10} {:<20} {:<20}".format(iter_count, f"{xn:.10f}", f"{error:.10e}"))


a = 5.5
b = 6
q = 0.25
print("Метод дихотомії")
root, result_table, iterations = bisection_method_with_table(a, b)
print(f"Знайдений корінь: {root:.10f}")
print(f"Фактична кількість ітерацій: {iterations}")
apriori_iters = apriori_estimation_bisection(a, b)
print(f"Апріорна кількість ітерацій: {apriori_iters}")
print(f"Апостеріорна оцінка кількості кроків:")
print_table(result_table)

print("Метод простої ітерації")
print(f"Апріорна кількість ітерацій: {apriori_estimation_iteration(q)}")
root, result_table, iterations = simple_iteration_method_with_table(5.75, q)
print(f"Знайдений корінь: {root:.10f}")
print(f"Фактична кількість ітерацій: {iterations}")
print("Апостеріорна оцінка кількості кроків:")
print_table(result_table)

