# enqueue - put() -> rear가 가리키는 위치에 데이터를 넣는 기능
# dequeue - get() -> front가 가리키는 위치에 데이터를 꺼내는 기능

# 1t -> 1 2 4 5 7 / 3
# 2t -> 7 1 2 4 5
# 3t -> 1 4 5
# 3 6 2 7 5 1 4
# 2번 뛰고 하나 제거 -> 제거 값 출력

# 입력 부분
read = input().strip()  # 입력된 줄의 양쪽 공백 제거
n, k = map(int, read.split())  # 공백을 기준으로 나누어 리스트를 만들고 정수로 변환

def rotate(lst, k): # 몇번째
    # 리스트를 오른쪽으로 k만큼 회전하는 함수
    return lst[-k:] + lst[:-k]

def josephus(n, k): # 총 몇명
    # 1부터 n까지의 숫자를 리스트로 생성
    lst = list(range(1, n + 1))
    result = []

    # 요세푸스 문제 해결
    index = 0  # 현재 인덱스

    while lst:
        # k번째 사람을 리스트에서 제거
        index = (index + k - 1) % len(lst)  # k-1은 인덱스 조정을 위한 것
        result.append(lst.pop(index))  # k번째 사람을 제거하고 결과에 추가

    return result



# 요세푸스 문제 해결
result = josephus_problem(n, k)

# 결과 출력7
print("<" + ", ".join(map(str, result)) + ">")




    

