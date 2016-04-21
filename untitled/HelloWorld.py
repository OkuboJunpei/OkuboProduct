print("モジュールのロード")

def test():
    print ("テストの呼び出し")

if __name__ == "__main__":

    print("test")


number = 4

if number <=10:
    print("aa          ")

import testClass

obj =  testClass.quick
item = testClass.large

item.accept(obj)
