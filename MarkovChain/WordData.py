import Node
import WordChain

Node1 = Node.stringTreeNode()
Node2 = Node.stringTreeNode()
Node3 = Node.stringTreeNode()
Node4 = Node.stringTreeNode()
Node5 = Node.stringTreeNode()
Node6 = Node.stringTreeNode()
Node7= Node.stringTreeNode()
Node1.Word = "今日は"
Node2.Word = "いい天気"
Node3.Word = "ですね"
Node4.Word = "いい天気"
Node5.Word = "今日は"
Node6.Word = "いい天気"
Node7.Word = "今日は"

NodeList = []
NodeList.append(Node1)
NodeList.append(Node2)
NodeList.append(Node3)
NodeList.append(Node4)
NodeList.append(Node5)
NodeList.append(Node6)
NodeList.append(Node7)
NewNodeList = WordChain.Chain(NodeList)

for node in NewNodeList:
    print(node.Word)

