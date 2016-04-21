class algorythm :
    def visitLarge(large):
        print("")
    def visitSmall(small):
        print("")


class quick(algorythm):
    def visitLarge(large):
        print("大きいデータをクイックソートします")
    def visitSmall(small):
        print("小さいデータをクイックソートします")

class bogo(algorythm):
    def visitLarge(large):
        print("大きいデータをボゴソートします")
    def visitSmall(small):
        print("小さいデータをボゴソートします")

class item:
    def accept(algorythm):
        print("")


class large(item):
    def accept(algorythm):
        algorythm.visitLarge(large)


class small(item):
    def accept(algorythom):
       algorythm.visitSmall(small)




