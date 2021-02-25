n = int(input())  # n : 입력받을 정수의 개수

# n_lst >(push)> temp_lst >(pop)> result_lst
n_lst = [i for i in range(1, n+1)]  # n_lst : 1 ~ n 까지의 수를 저장한 리스트. push연산에 의해 temp_lst로 데이터 전달.
temp_lst = []  # temp_lst : push연산에 의해 n_lst로부터 데이터를 수신. pop연산에 의해 result_lst로 데이터 전달.
result_lst = []  # result_lst : pop연산에 의해 temp_lst로부터 데이터를 수신.

result = []  # result : 결과로 출력할 +,- 를 저장하기 위한 공간

idx = 0  # idx : 어떤 숫자까지 push하였는지 확인하기 위한 변수. push/pop 동작 중 수행할 동작 선택에 필요.

for i in range(n):  # n번 반복
    num = int(input())  # num : 입력받은 숫자

    # push와 pop으로 만들지 못하는 경우는 순서때문에 못만드는 경우이고, 그 경우에는 IndexError가 날 것이다.
    try:

        # push 동작 수행
        # n_lst에서 temp_lst로 전달, push한 숫자까지 idx를 옮겨줌, push동작과 pop동작만큼 result에 추가.
        if num > idx:
            for j in range(num-idx):
                temp_lst.append(n_lst.pop(0))
                result.append('+')
            idx = num
            result_lst.append(temp_lst.pop())
            result.append('-')

        # pop 동작 수행
        # temp_lst에서 result_lst로 전달, pop동작만큼 result에 추가.
        else:
            for j in range(temp_lst[-1]-num+1):
                result_lst.append(temp_lst.pop())
                result.append('-')
    
    # 에러가 난 경우는 push/pop 연산으로 표현이 불가능한 경우이고, NO를 출력한다.
    except:
        print("NO")
        exit(0)

for val in result:
    print(val)
