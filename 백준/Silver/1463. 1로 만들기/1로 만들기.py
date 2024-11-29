import sys
input = sys.stdin.readline

def main():
    N = int(input().strip()) 

    dp = [0] * (N + 1) #연산횟수를 저장할 리스트 생성

    for i in range(2, N + 1): # N이 1이면 0이기 때문에 2부터 N까지 계산
        # 기본 규칙 : 1을 뺀다
        dp[i] = dp[i - 1] + 1 # 연산을 수행했으니 1을 더한다
        
        # 2로 나눴을때 나머지가 없으면 2로 나눈다
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1) 
        # 연산 횟수가 더 적은걸 dp[i]에 저장한다.

        # 3으로 나눴을때 나며지가 없으면 3으로 나눈다
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)
        # 연산 횟수가 더 적은걸 dp[i]에 저장한다.
    print(dp[N])

main()
