
def fibonacci(n):
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(str(a))
        a, b = b, a + b
    return ','.join(series)

if __name__ == "__main__":
    n = 10
    print(fibonacci(n))
