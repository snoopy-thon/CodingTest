# 구현 알고리즘
# 4-2. 시각
# 00 00 00 ~ N 59 59
# 내 풀이 : 수학계산으로 품.
# 전체 - 3이 아예 안들어갈때 = (n+1) * 60 * 60 - 네모(n에 따라 달라짐) * 5*9 * 5*9

# 정수 N을 입력 받기
n = int(input())
except3 = 0
if n == 3 :
    except3 = 3 * 5*9 * 5*9
elif n == 13 :
    except3 = 12 * 5*9 * 5*9
elif n == 23 :
    except3 = 21 * 5*9 * 5*9
elif n < 3:
    except3 = (n+1) * 5*9 * 5*9
elif n < 13:
    except3 = n * 5*9 * 5*9
elif n < 23:
    except3 = (n-1) * 5*9 * 5*9

result = (n+1) * 60 * 60 - except3
print(result)

# 책 풀이 : 내 풀이보다 훨씬 쉽고 간결함.
# 문자열에서 특정 문자가 있는지 확인할때 if '문자' in "문자열"을 사용하면 됨.

# H를 입력받기
h = int(input())

count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1
print(count)

