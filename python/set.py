# python
```py
from typing import List  
  
class SetOperations:  
      
    # 并集  
    def union(self, A: List[int], B: List[int]) -> List[int]:  
        result = A.copy()  
        for b in B:  
            if b not in A:  
                result.append(b)  
        result.sort()  
        return result  
      
    # 交集  
    def intersection(self, A: List[int], B: List[int]) -> List[int]:  
        result = []  
        for a in A:  
            if a in B:  
                result.append(a)  
        return result  
      
    # 差集 A-B  
    def difference(self, A: List[int], B: List[int]) -> List[int]:  
        result = []  
        for a in A:  
            if a not in B:  
                result.append(a)  
        return result  
      
    # 补集  
    def complement(self, A: List[int], U: List[int]) -> List[int]:  
        result = []  
        for u in U:  
            if u not in A:  
                result.append(u)  
        return result  
      
    # 对称差集  
    def symmetric(self, A: List[int], B: List[int]) -> List[int]:  
        set1 = self.difference(A, B)  # A-B  
        set2 = self.difference(B, A)  # B-A  
        result = self.union(set1, set2)  # (A-B)U(B-A)  
        result.sort()  
        return result  
  
# 示例用法  
if __name__ == "__main__":  
    set_ops = SetOperations()  
    A = [1, 2, 3, 4]  
    B = [3, 4, 5, 6]  
    U = [1, 2, 3, 4, 5, 6, 7, 8]  
  
    print("Union:", set_ops.union(A, B))  
    print("Intersection:", set_ops.intersection(A, B))  
    print("Difference A-B:", set_ops.difference(A, B))  
    print("Complement:", set_ops.complement(A, U))  
    print("Symmetric Difference:", set_ops.symmetric(A, B))
```
# python function
```py
class SetOperations:
    # 并集
    @staticmethod
    def union(A, B):
        result = list(set(A) | set(B))  # 使用集合的并集操作，然后转换回列表
        result.sort()  # 排序
        return result

    # 交集
    @staticmethod
    def intersection(A, B):
        result = list(set(A) & set(B))  # 使用集合的交集操作，然后转换回列表
        return result

    # 差集 A-B
    @staticmethod
    def difference(A, B):
        result = list(set(A) - set(B))  # 使用集合的差集操作，然后转换回列表
        return result

    # 补集
    @staticmethod
    def complement(A, U):
        result = list(set(U) - set(A))  # 全集U中不在A中的元素
        return result

    # 对称差集
    @staticmethod
    def symmetric_difference(A, B):
        set1 = SetOperations.difference(A, B)  # A-B
        set2 = SetOperations.difference(B, A)  # B-A
        result = SetOperations.union(set1, set2)  # (A-B)U(B-A)
        result.sort()  # 排序
        return result


# 测试代码
if __name__ == "__main__":
    A = [1, 3, 4]
    B = [1, 2, 5, 6]
    U = [1, 2, 3, 4, 5, 6]

    union = SetOperations.union(A, B)
    print(f"集合A与集合B的并集：{union}")

    intersection = SetOperations.intersection(A, B)
    print(f"集合A与集合B的交集：{intersection}")

    difference = SetOperations.difference(A, B)
    print(f"集合A与集合B的差集：{difference}")

    symmetric = SetOperations.symmetric_difference(A, B)
    print(f"集合A与集合B的对称差集：{symmetric}")

    complement = SetOperations.complement(A, U)
    print(f"集合A在全集U中的补集：{complement}")
  ```
