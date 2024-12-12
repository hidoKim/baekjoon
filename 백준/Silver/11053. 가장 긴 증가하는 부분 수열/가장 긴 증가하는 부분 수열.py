import sys
input = sys.stdin.readline

def main():
    N = int(input().strip())
    sequence = list(map(int, input().split()))
    
    # N은 1이상, N이 1이면 길이는 무조건 1
    if N==1:
        print(1)
        return

    # 수열의 길이 저장
    # dp[i]는 sequence[i]를 마지막으로 하는 가장 긴 증가 부분 수열의 길이
    dp = [1] * N 
    # 자기 자신 만으로 길이가 1인 부분 수열이기 때문에 1로 초기화
    
    # 현재 수 i와 i이전의 모든 수 j를 비교
    for i in range(N) :
        for j in range(i) :
            if sequence[j] < sequence[i] :
                dp[i] = max(dp[i], dp[j] + 1) 
                # 증가 부분 수열이 성립하면 수열 길이를 1 증가 시키고, i와 j중 더 큰 길이를 저장
       
    print(max(dp))

main()        