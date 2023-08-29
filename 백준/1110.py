N = int(input())
check = N

cnt = 0

A = 987654321

while N != A:
    x = check // 10      # 앞자리 구분
    y = check % 10       # 뒷자리 구분
    z = (x+y) % 10       # 합산 숫자의 뒷자리
    check = (y*10) + z   # 더하기 사이클 계산
    A = check            # N과 A 가 같은지 판별
    cnt += 1

print(cnt)