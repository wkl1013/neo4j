from py2neo import Graph, Node, Relationship

"""新版 py2neo 建立连接的方式"""
graph = Graph("http://localhost:7474/", auth=("neo4j", "123456"))
graph.run("create (wang: Person {name: 'wangKaiLiang', born: 1995})")
print("连接成功！")

"""创建一个节点使用 Node 类，其中 (节点标签, 其它参数)."""
movie_node = Node("Movie", name="The Matrix", released="1999", tagline="Welcome to The Real World!")  # 新建一个节点
graph.create(movie_node)  # 将节点添加到图中
print("节点创建成功！")

"""创建一个关系使用 Relationship 类，其中 (节点1, 关系类型, 节点2)."""
person1 = Node("Person", name="Alice", age=30)
person2 = Node("Person", name="Bob", age=25)
friend1 = Relationship(person1, "FRIEND_WITH", person2)  # 关系指向默认，第一个节点指向第二个节点
graph.create(friend1)
print("关系创建成功！")