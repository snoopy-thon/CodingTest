# 그리디 알고리즘
# 3-4. 1이 될 때까지
# 내 풀이 : 연산 횟수 = 몫+나머지+몫+나머지+...+ (n-1)(만약 n이 K보다 작다면 n-1 더하고 반복문 탈출)
# < 연산 >
# 1. N에서 1을 뺀다.
# 2. N을 K로 나눈다.

# n, k 를 공백으로 구분하여 입력받기
n, k = map(int,input().split())
count = 0

while True :
    if n >= k :
        # n을 k로 나눈 나머지 만큼 1번 연산을 수행한다.
        # 나머지 : n이 k로 나누어 떨어질 때까지 빼야하는 횟수
        r = n % k
        count += r
        # (n-r)을 k로 나눌 때, 2번 연산을 수행한다.
        q = (n-r) // k
        count += 1
        n = q
    else:
        # n이 k보다 작을 때, n에서 1씩 뺀만큼 1번 연산 수행 후 반복문 탈출
        count += n-1
        break
    
print(count)


# 책 풀이1 : n을 k의 배수로 만들고 target에 저장하고, result에 1번 연산을 수행하는 횟수를 저장함.

n, k = map(int,input().split())
result = 0

while True :
    # (N == K로 나누어떨어지는 수)가 될 때까지 1씩 빼기
    target = (n // k) * k
    result += (n - target)
    n = target
    # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # K로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)


# 책 풀이2 : 이중 while문 사용함. 문제 그대로 n이 k의 배수가 아닌 경우 1번 연산을 하고,
# n이 k의 배수인 경우 k로 나눴다.
n, k = map(int,input().split())
result = 0

# N이 K이상이라면 K로 계속 나누기
while n >= k:
    # N이 K로 나누어 떨어지지 않는다면 N에서 1씩 빼기
    while n % k != 0:
        n -= 1
        result += 1
    # K로 나누기 
    n //= k
    result += 1

# 마지막으로 남은 수에 대하여 1씩 빼기
while n > 1 :
    n -= 1
    result += 1
    
print(result)






