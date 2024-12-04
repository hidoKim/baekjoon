import sys
input = sys.stdin.readline
# 계단 오르기 문제와 비슷한 문제
def main():
    N = int(input().strip())
    # 포도주의 양을 입력받음
    wine = [int(input().strip()) for _ in range(N)] 

    # 2개 이하일 때는 단순 계산
    if N == 1 :
        print(wine[0])
        return
    elif N == 2 :
        print(wine[0]+wine[1])
        return
    
    # 3개 이상일 때
    dp = [0] * N

    dp[0] = wine[0]
    dp[1] = dp[0] + wine[1]

    # N = 3 일때 [0]+[1] ,[1]+[2], [0]+[2] 중 가장 큰 수 저장
    dp[2] = max(wine[0] + wine[1] , wine[1] + wine[2], wine[0] + wine[2])

    # N = 4 이상일 때 
    # [i-1](현재잔을 안마심) , [i-2]+[i](전전잔, 현재잔), [i-3]+[i-1]+[i](전전전잔, 전잔, 현재잔) 중 가장 큰 수 저장
    for i in range(3, N) :
        dp[i] = max(dp[i-1],  dp[i-2] + wine[i], dp[i-3] + wine[i-1] + wine[i])  

    result = dp[N-1]
    print(result)

main()