def my_decorator(func):

    def wrapper():
        print("데코레이터 추가")
        func()
        print("데코레이터 추가")
    return wrapper

@ my_decorator

def hello():
	    print("안녕하세요")

hello()