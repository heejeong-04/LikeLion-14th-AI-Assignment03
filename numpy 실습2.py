# numpy를 np라는 이름으로 불러오기
import numpy as np

# 7x7 크기의 2차원 배열을 만들고 전부 0으로 채우기
arr = np.zeros((7, 7), dtype=int)

# 짝수행의 홀수열을 1로 채우기
arr[::2, 1::2] = 1
# 홀수행의 짝수열을 1로 채우기
arr[1::2, ::2] = 1

# for문을 통해 2차원 배열의 각 요소를 순차적으로 출력하기
for row in range(7): # 0행부터 6행까지 반복하기
    for col in range(7): # 0열부터 6열까지 반복하기
        print(arr[row, col], end=" ") # 행,열 원소 출력 후 띄어쓰기
    print()