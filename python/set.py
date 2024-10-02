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
