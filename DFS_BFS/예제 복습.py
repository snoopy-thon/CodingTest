# 4/19/금
# 126p stack 연습
# stack 선입후출(First In Last Out)

stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack)
print(stack[::-1])

# 129p queue 연습
# queue 선입선출(FIFO; First In First Out)

from collections import deque

# 큐 구현을 위해 deque 라이브러리 사용
queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()
print(queue)

# deque 객체를 list로 변경하고자 할 때 list() 사용 
list(queue)

# 130p 재귀함수
# 컴퓨터 내부에서 재귀함수의 수행은 스택 자료구조를 이용함
# 함수를 계속 호출했을 때 가장 마지막에 호출한 함수가 먼저 수행을 끝내야 그 앞의 함수 호출이 종료되기 때문
def recursive_function(i):
    if i == 100 :
        return
    
    print(i,'번째 재귀함수에서',i+1,'번째 재귀함수를 출력합니다.')
    recursive_function(i+1)
    print(i,'번째 재귀함수를 종료합니다.')

recursive_function(1)

# 팩토리얼 예제
# 반복적으로 구현한 n!
def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
# 재귀적으로 구현한 n!
def factorial_recursive(n):
    if n <= 1 :
        return 1
    return n * factorial_iterative(n-1)

print('반복적으로 구현:', factorial_iterative(5))
print('재귀적으로 구현:',factorial_recursive(5))

# 그래프 : 인접 행렬(2차원배열) / 인접 리스트(리스트)
# 인접 행렬 예제
# 특징 : 모든 관계를 저장하므로 메모리가 불필요하게 낭비됨
INF = 999999999 # 무한의 비용 선언

graph = [
    [0,7,5],
    [7,0,INF],
    [5,INF,0]
]

print(graph)

# 인접 리스트 예제
# 특징 : 특정한 두 노드가 연결되어 있는지에 대한 정보를 얻는 속도가 느림
graph = [[] for _ in range(3)]

graph[0].append((1, 7))
graph[0].append((2, 5))

graph[1].append((0, 7))

graph[2].append((0, 5))

print(graph)