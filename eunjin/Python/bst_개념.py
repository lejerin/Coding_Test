class Node(object):
  def __init__(self, data):
    # data: 부모노드
    self.data = data
    # left, right: 자식 노드
    self.left = self.right = None

class BinarySearhTree(object):

  #1. 초기화
  def __init__(self):
    #최상위 노드
    self.root = None

  #2. 삽입
  def insert(self, data):
    # data를 1개의 노드씩 받아서 insert_value 함수 실행
    self.root = self._insert_value(self.root, data)
    # 값을 넣었으면 True 반환
    return self.root is not None 

  def _insert_value(self, node, data):
    # 부모 노드가 비워져있다면 부모 노드에 추가
    if node is None:
      node = Node(data)
    # 부모 노드에 값이 있다면 자식 노드에 추가
    else:
    # 부모 노드보다 작으면 left에 추가
      if data < node.data:
        node.left = self._insert_value(node.left, data)
      # 부모 노드보다 크다면 right에 추가
      else:
        node.right = self._insert_value(node.right, data)
    return node

  def find(self, key)
