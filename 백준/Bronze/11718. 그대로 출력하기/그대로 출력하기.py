while True:
    try:
        print(input())
    except EOFError:
        break
# print(sys.stdin.readline().rstrip())는 EOF를 받을 때 빈 문자열을 리턴해서 에러처리가 되지 않음