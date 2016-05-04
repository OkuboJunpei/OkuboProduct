from abc import ABCMeta, abstractmethod

class algorithm (metaclass=ABCMeta):
    @abstractmethod
    def visitLarge(large):
        pass
    @abstractmethod
    def visitSmall(small):
        pass

class quick(algorithm):
    def visitLarge(large):
        print("大きいデータをクイックソートします")
    def visitSmall(small):
        print("小さいデータをクイックソートします")

class bogo(algorithm):
    def visitLarge(large):
        print("大きいデータをボゴソートします")
    def visitSmall(small):
        print("小さいデータをボゴソートします")

class random(algorithm):
    def visitLarge(large):
        print("大きいデータをランダムソートします")
    def visitSmall(small):
        print("小さいデータをランダムソートします")


class item:
    def accept(algorithm):
        pass

class large(item):
    def accept(algorithm):
        algorithm.visitLarge(large)

class small(item):
    def accept(algorithm):
        algorithm.visitSmall(small)

class medium(item):
    def accept(selfalgorithm):
        algorithm.visitMedium(medium)

class sample:
    def decideAlgorythm(self, algorithmID, dataTypeID):
        if algorithmID == 1:
            if dataTypeID == 1:
                print("大きいデータをクイックソートします")
            else:
                print("小さいデータをクイックソートします")
        else:
            if dataTypeID == 2:
                print("大きいデータをボゴソートします")
            else:
                print("小さいデータをボゴソートします")

