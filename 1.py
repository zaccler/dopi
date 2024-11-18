MOD = 10**9 + 7

def summa(n):
    result = 0
    power_of_two = 1
    while power_of_two <= n:
        # Количество чисел, у которых этот бит установлен
        count = (n + 1) // (power_of_two * 2) * power_of_two + max(0, (n + 1) % (power_of_two * 2) - power_of_two)
        result = (result + count * power_of_two) % MOD
        power_of_two *= 2
    return result


t = int(input())
for _ in range(t):
    n = int(input())
    print(summa(n))
