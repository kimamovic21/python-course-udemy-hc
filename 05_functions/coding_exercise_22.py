counter = 0


def pure_add(a, b):
    return a + b


def impure_increment():
    global counter
    counter += 1
    return counter


def factorial_recursive(n):
    if n == 0:
        return 1
    return n * factorial_recursive(n - 1)


def square_list(nums):
    return list(map(lambda number: number**2, nums))
