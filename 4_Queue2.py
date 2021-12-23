# 정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

# 명령은 총 여섯 가지이다.
# push X: 정수 X를 큐에 넣는 연산이다.
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 큐에 들어있는 정수의 개수를 출력한다.
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

num = (int)(input())
q_list = [input().split() for _ in range(num)]
myqueue = []

for i in range(num):
    if q_list[i][0] == "push" :
        myqueue.append(q_list[i][1])
    
    elif q_list[i][0] == "pop" :
        if len(myqueue) == 0:
            print(-1)
        else: 
            print(myqueue.pop(0)) 
    
    elif q_list[i][0] == "size" :
        print(len(myqueue))

    elif q_list[i][0] == "empty" :
        if len(myqueue) == 0:
            print(1)
        else:
            print(0)
    
    elif q_list[i][0] == "front" :
        if len(myqueue) == 0:
            print(-1)
        else: 
            print(myqueue[0])

    elif q_list[i][0] == "back" :
        if len(myqueue) == 0:
            print(-1)
        else: 
            print(myqueue[-1])