def get_gcd(num1: int, num2: int) -> int:
    if num1 == 0:
        return num2
    return get_gcd(num2 % num1, num1)


if __name__ == '__main__':
    print(get_gcd(8, 12))

    arr = [2, 4, 6, 8, 16]
    gcd = None
    for i in range(0, len(arr) - 1):
        if gcd is None:
            gcd = get_gcd(arr[i], arr[i + 1])
        else:
            gcd = get_gcd(gcd, arr[i + 1])

    print(gcd)
