import pandas as pd
from py2neo import Graph, Node, Relationship
from py2neo.matching import *

def Py2Neo(graph):
    df = pd.read_excel("Invoice_data_Demo.xls")  # 使用 pandas 读取表格内容
    column_data1 = df["销售方名称"]
    column_data2 = df["购买方名称"]
    column_data3 = df["金额"]

    # 将 pandas 读取的数据转为列表方便后续处理
    sell = column_data1.values.tolist()
    buy = column_data2.values.tolist()
    trade = column_data3.values.tolist()

    # 使用 set 集合去重后，再转为 list
    sell_distinct = list(set(sell))
    buy_distinct = list(set(buy))

    # 删除数据库中原有的节点
    graph.run("match (n) detach delete n")

    # 在数据库中建立销售方节点
    for s in sell_distinct:
        sell_node = Node("sell", name=s)
        graph.create(sell_node)

    # 在数据库中建立购买方节点
    for b in buy_distinct:
        buy_node = Node("buy", name=b)
        graph.create(buy_node)

    # 构建关系指向
    nodes = NodeMatcher(graph)
    for s, b, t in zip(sell, buy, trade):
        node1 = nodes.match("sell", name=s).first()  # 找到对应的销售方节点
        node2 = nodes.match("buy", name=b).first()  # 找到对应的购买方节点
        re = Relationship(node1, t, node2)  # 确定节点间指向关系
        graph.create(re)
    print("关系创建成功！")

if __name__ == "__main__":
    graph = Graph("http://localhost:7474/", auth=("neo4j", "123456"))
    Py2Neo(graph)