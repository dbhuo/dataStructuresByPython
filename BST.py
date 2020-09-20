class Node:
    """
    定义二叉树的节点
    """
    __slots__ = '_item','_left','_right' #一个类中需要创建多个变量时可以用
    def __init__(self,item,left=None,right=None):
        self._item = item
        self._left = left
        self._right = right
class BinarySearchTree:
    """
    定义二叉搜索树的各种操作
    """
    def __init__(self,root=None):
        self._root = root
    def get(self,key):
        """
        params:
            key - 待查找的值
        Return:
            获取这个树中的对应节点
        """
        return self.__get(self._root,key)
    def __get(self,node,key):
        """
        helper - 确认数中是否右对应元素
        params:
            node - 树节点
            key - 待查找的值
        Return:
            若右对应值，则返回对应值
            若无则返回None
        """
        if(node is None):
            return None
        if(key == node._item):
            return node._item
        if(key < node._item):
            return self.__get(node._left,key)
        else:
            return self.__get(node._right,key)
    def add(self,value):
        """
        添加元素到树中
        Params:
            value - 待添加的值
        Return:
            无
        """
        self._root = self.__add(self._root,value)
    def __add(self,node,value):
        """
        helper - 添加元素到树中
        Params:
            node - 待添加值的树
            value - 待添加的值
        Returns:
            node - 添加完元素的新树
        """
        if node is None:
            return Node(value)
        if value == node._item:
            pass
        else:
            if value < node._item:
                node._left = self.__add(node._left,value)
            else:
                node._right = self.__add(node._right,value)
        return node    
    def get_max(self):
        """
        返回数中元素最大值
        """
        return self.__get_max(self._root)
    def __get_max(self,node):
        """
        helper - 获取树元素最的的值
        Params:
            node - 待查找子树
        """
    
        if node is Node:
            return None
        while node._right is not None: #因为树中的最大值出现在树的右下角
            node = node._right 
        return node._item
    def remove(self,key):
        """
        删除树中的对应元素
        Params:
            value - 待删除的值
        Return:
            无
        """
        self._root = self.__remove(self._root,key)       
    def __remove(self,node,key):
        """
        helper - 删除树种的对应元素
        Params:
            node - 待删除值的树
            value - 待删除的值
        Returns:
            node - 删除完元素的新树
        """
        if node is None:
            return None
        if key < node._item:
            node._left = self.__remove(node._left,key)
        elif key > node._item:
            node._right = self.__remove(node._right,key)
        else: #想删除的节点落在根节点上的时候
              #如果仅仅存在一颗子树，则返回对应子树即可
            if node._left is None:   
                node = node._right #仅存在右子树
            elif node._right is None:
                node = node_left #仅存在左子树
            else: 
              #左右节点都存在的情况下，交换根节点的值变成左子树最大值
                node._item = self.__get_max(node._left)
                node._left = self.__remove(node._left,node._item)
        return node
    def PreOrder(self):
        self.__PreOrder(self._root)
        print(' ')
    def __PreOrder(self,node):
        """
        先序遍历
        Params:
            node - 需要遍历的树
        return:
            无 
        """
        if node is None:
            return None
        print(node._item,end = " ")
        self.__PreOrder(node._left)
        self.__PreOrder(node._right)
    def InOrder(self):
        self.__InOrder(self._root)
        print(' ')
    def __InOrder(self,node):
        """
        中序遍历
        Params:
            node - 需要遍历的树
        return:
            无 
        """
        if node is None:
            return None
        self.__InOrder(node._left)
        print(node._item,end = " ")
        self.__InOrder(node._right)   
    def PostOrder(self):
        self.__PostOrder(self._root)
        print(' ')
    def __PostOrder(self,node):
        """
        后序遍历
        Params:
            node - 需要遍历的树
        return:
            无 
        """
        if node is None:
            return None
        self.__PostOrder(node._left)
        self.__PostOrder(node._right)
        print(node._item,end =" ")   