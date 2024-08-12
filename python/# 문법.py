# 문법

"""
함수 선언 : def {함수이름} (미지수) : 끝

* 함수정의
def f(x): - parameter
    return x + 3

* 함수호출
f(1) - argument

    age = 96
    print("저는 {}년생 입니다.".format(age)) - python 객체지향 함수 찾아보기 
    print(f"저는 {age}년생 입니다.")
    
    출력값 = 저는 96년생 입니다.
    
    seq -> " " / end -> \n
    ex. print(1,2,3,4,5, seq="-")
    출력값 = 1-2-3-4-5
    
    a = input()
    
    print(a) -> 기본 type str
    
    형변환 -> 뭐..str넣거나 int 넣..기
    
    ** 산술 연산자 **
    print(A % B) -- 나눈 값의 나머지
    print(A // B) -- 나눈 값의 몫
    print(A ** B) -- 제곱
    
    ** 논리 연산자 **
   and or not
   
   ** 조건문 **
   if A < B : 
    pass
   elif b == 0:
    pass
   else:
    pass
   
    x,y = map(int, input().split()) 
    # split = 각자 구분자로 나뉜 입력된 값을 대입해서 넣어준다
    
   ** 반복문 **
   for i in range(0, 10, 1) -> 0부터 10까지 1step
   출력값 = [0,1,2,3,4,5,6,7,8,9]
   
   arr = [1,2,3,4,5,6, "안녕", True, 2.5] 
   for i in arr
   
   for i in range(1, 10):
    print(f"{i}단 입니다")
    for j in range(1, 10):
    print(f"{j}단 입니다")
    print(f"{i} x {j} = {i * j}") -> 구구단
   
  

    ** 리스트 **
    arr = [1,2,3,4,5,6] 
    
    ** 인덱싱 **
    print(arr[2])
    출력값 = 3
    
    ** 슬라이싱 **
    print(arr[1:4]) = 1이상 4미만
    출력값 = [2,3,4]
    
    print(arr[1:6:2]) = 2칸씩 띄어서 출력 
    출력값 = [2,4,6]
    
    arr.append -> 다른 자료형들끼리 묶어서 리스트로 출력 가능
    # 7을 출력하고 싶을 경우,
    arr.append([1,2,3,4,5] [3,4,5,8,6,4] [12,3,4,7])
    print(arr[-1][3]) //  출력값 = 7

    # 안만 출력하고싶을 경우    
    arr.append("안녕")
    print(arr[-1][0]) -> 맨뒤 리스트는 -1로 출력 가능
    출력값 = 안
    
    
    # 백준 14681
x,y = map(int,input().split())
    
if x > y:
    print(1)
elif x < y:
    print(4)
    
    """

for i in range(2, 10):
    print(f"{i}단 입니다")
    for j in range(1, 10): # 들여쓰기에 따라 결과가 달라짐
        print(f"{i} x {j} = {i * j}")

a = 0
while a < 10 :
    print(a)
    a += 1
    break # 멈챠~
    continue # 다음 반복으로 스킵~

 # sorted = 오름차순 / reverse=True = 내림차순
 
def check_tri():
  pass

while True():
    a,b,c = map(int, input().split()) 

    if a == 0 and b == 0 and c == 0:
        break

if check_tri(sorted([a,b,c])):
    print("right")
else: 
    print("worng")
    
    