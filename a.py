def greeting():
    print('a.py')
    print(__name__)
    
if __name__ == "__main__":
    print(__name__)
    greeting()
    print('직접 실행 됨.')
else:
    print("a.py가 import 되어 실행됨.")