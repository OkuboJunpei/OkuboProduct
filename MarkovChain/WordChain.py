import Node


def Chain(NodeList):
    NewNodeList = []
    beforeNode = None
    for addNode in NodeList:
        presence = False
        presenceNode = Node.stringTreeNode
        targetNode = Node.stringTreeNode
        #これまでに同じ単語が出てきているかを調べる
        for node in NewNodeList:
            if(node.Word == addNode.Word):
                presence = True
                targetNode = node
        #出てきていないのであれば管理用のリストに追加する
        if(presence == False):
            NewNodeList.append(addNode)
            targetNode = addNode
        #一つ前の単語のノードに自身を登録する

        if (beforeNode is not None):

            nextWordPresence = False
            for node in beforeNode.nextNodesList:
                #既に、その単語の次の単語として自身が登録されているなら、カウントを追加する
                if (node.Word == targetNode.Word):
                    beforeNode.nextNodesCountList[ beforeNode.nextNodesList.index(node)] += 1
                    nextWordPresence = True
            #未だにその単語が次の単語として登録されていないのであれば、それを登録する
            if(nextWordPresence == False):
                beforeNode.nextNodesList.append(targetNode)
                beforeNode.nextNodesCountList.append(1)
        #自身を一つ前の単語として設定する
        beforeNode =targetNode

    return NewNodeList








