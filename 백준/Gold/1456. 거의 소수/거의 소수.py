def Prime(sqrt_B):
    prime_list = set()
    is_prime = [True] * (sqrt_B + 1)
    is_prime[0] = is_prime[1] = False

    for num in range(2, sqrt_B+1):
        if is_prime[num]:
            for i in range(num*num, sqrt_B+1, num):
                is_prime[i] = False

    for num in range(2, sqrt_B+1):
        if(is_prime[num]):
            prime_list.add(num)

    return prime_list

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    
    A, B = map(int, input().split())
    count = 0
    
    visited = set()
    prime_list = Prime(int(B**0.5) + 1) #B의 제곱근까지만 소수를 확인하면 됨 => 초과 시 거듭제곱 확인 불가능
    # print(prime_list)
    for prime in prime_list:
        power = prime
        while power <= B:
            if power >= A and power != prime and power not in visited:
                count += 1
                # print("power", power)
                visited.add(power)

            if power > B // prime:
                break
            
            power *= prime
    
    print(count)