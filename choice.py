# import random# randrange(0. 4) : 0 ~ 3까지 무작위 수 만듦
# trip = random.randrange(0, 4)
# if trip == 0:
#     print('제주도로 출발')
# elif trip == 1:
#     print('사이판으로 출발')
# else:
#     print('하와이로 출발')

# import random


# gnum = 0
# while True:
#     com = random.randrange(3)
#     user = int(input('가위0 바위1 보2 선택: '))
#     if user == 0 or user == 1 or user == 2:
#         print('user = %d, com = %d' %(user, com))
#         if user == com :
#             print('비겼습니다.')
#         elif(user == 0 and com == 2) or (user == 1 and com == 0) or (user == 2 and com == 1) :
#             print('user 승!')
#         else:
#             print('com 승!')
#     else:
#         print('%d회 가위바위보 == End of game ===' % gnum)
#         break
#     gnum += 1

# print("===1부터 n까지의 짝수의 합 구하기===")
# digit = 2
# sum = 0
# n = int(input("어디까지의 합? "))
# while(digit <= n):
#     sum = sum + digit
#     digit = digit + 2
# print("1부터", n, "까지의 합= ", sum)  

# print("===1부터 n까지의 짝수의 합 구하기===")
# sum = 0
# n = int(input("어디까지의 합? "))
# for digit in range(2, n+1, 2):
#     sum = sum + digit
# print("1부터", n, "까지의 합= ", sum)   
# import sys

# # 명령행 인자(argument) 개수가 1개 이상이면 첫번째 인자(argument)를 출력합니다.
# if len(sys.argv) > 1:
#     print("입력한 인자(argument)는:", sys.argv[1])
# else:
#     print("인자(argument)를 입력해주세요.")   
# select = int(input('1, 입력한 수식 계산 2. 두 수 num1부터 num2 까지의 합계 : '))

# if select == 1:
#     nexp = input(" ***수식을 입력하세요: ")
#     answer = eval(nexp)
#     print(" %s 결과는 %5.1f입니다. " %(nexp, answer))

# elif select == 2:
#      num1 = int(input(" ***첫번째 숫자를 입력하세요: " ))
#      num2 = int(input(" ***두번째 숫자를 입력하세요: " ))
#      answer = 0
#      for i in range(n1, n2 + 1):
#           answer = answer + i
#           print('%d+...+%d는 %d입니다' % (n1,n2,answer))
#      else:
#           print('1,2만 입력하세요.')

for dan in range(2, 10):
    print('\n%d단: ' %dan, end = '')
    for num in range(1, 10):
        print('%d x %d =%d' %(dan, num, dan * num), end =' ')
    



