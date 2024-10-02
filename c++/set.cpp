```c++
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

// 打印集合1
void PrintSet1(const vector<int>& A) {
    cout << "{";
    for (const int& a : A) {
        cout << a << ((a == A.back()) ? "" : ",");
    }
    cout << "}";
    cout << endl;
}

// 打印集合2
void PrintSet2(const vector<vector<int>>& A) {
    for (const vector<int>& row : A) {
        cout << "{";
        for (const int& a : row) {
            cout << a << ((a == row.back()) ? "" : ",");
        }
        cout << "}";
        cout << endl;
    }
}

// 并集
vector<int> Union(const vector<int>& A, const vector<int>& B) {
    vector<int> unionset(A);
    for (const int& b : B) {
        if (find(A.begin(), A.end(), b) == A.end()) {
            // 如果集合B中元素不在集合A中
            unionset.push_back(b);
        }
    }
    sort(unionset.begin(), unionset.end()); // 排序集合
    return unionset;
}

// 交集
vector<int> Intersection(const vector<int>& A, const vector<int>& B) {
    vector<int> interset;
    for (const int& b : B) {
        if (find(A.begin(), A.end(), b) != A.end()) {
            // 如果集合B中元素在集合A中
            interset.push_back(b);
        }
    }
    sort(interset.begin(), interset.end());
    return interset;
}

// 差集
vector<int> Difference(const vector<int>& A, const vector<int>& B) {
    vector<int> diffset;
    for (const int& a : A) {
        if (find(B.begin(), B.end(), a) == B.end()) {
            // 如果集合A中元素不在集合B中
            diffset.push_back(a);
        }
    }
    sort(diffset.begin(), diffset.end());
    return diffset;
}

// 补集
vector<int> Complement(const vector<int>& A, const vector<int>& U) {
    vector<int> comset;
    for (const int& u : U) {
        if (find(A.begin(), A.end(), u) == A.end()) {
            // 如果全集U中元素不在集合A中
            comset.push_back(u);
        }
    }
    sort(comset.begin(), comset.end());
    return comset;
}

// 对称差集
vector<int> Symmetric(const vector<int>& A, const vector<int>& B) {
    vector<int> set1 = Difference(A, B);     // A-B
    vector<int> set2 = Difference(B, A);     // B-A
    vector<int> symmset = Union(set1, set2); //(A-B)U(B-A)
    sort(symmset.begin(), symmset.end());
    return symmset;
}

vector<vector<int>>powerset;
vector<int>subset;

void backtracking(const vector<int>& nums,int stratIndex) {
    powerset.push_back(subset);
    for (int i = stratIndex; i < nums.size(); ++i) {
        subset.push_back(nums[i]);
        backtracking(nums, i + 1);
        subset.pop_back();
    }
}
// 幂集(时间复杂为O(n*2^n))
vector<vector<int>> PowerSet(const vector<int>& A) {
    powerset.clear();
    subset.clear();
    backtracking(A, 0);
    return powerset;
}

int main() {
    vector<int> A = { 1, 3, 4 };          // 集合A
    vector<int> B = { 1, 2, 5, 6 };       // 集合B
    vector<int> U = { 1, 2, 3, 4, 5, 6 }; // 全集U

    cout << "集合A：";
    PrintSet1(A);
    cout << "集合B：";
    PrintSet1(B);
    cout << "全集U：";
    PrintSet1(U);

    vector<int> unionSet = Union(A, B);
    cout << "集合A与集合B的并集为：" << endl;
    PrintSet1(unionSet);

    vector<int> intersectionSet = Intersection(A, B);
    cout << "集合A与集合B的交集为：" << endl;
    PrintSet1(intersectionSet);

    vector<int> diffSet = Difference(A, B);
    cout << "集合A与集合B的差集为：" << endl;
    PrintSet1(diffSet);

    vector<int> comSet = Complement(A, U);
    cout << "集合A的补集为：" << endl;
    PrintSet1(comSet);

    vector<int> symmSet = Symmetric(A, B);
    cout << "集合A与集合B的对称差集为：" << endl;
    PrintSet1(symmSet);

    vector<vector<int>> powerSet = PowerSet(A);
    cout << "集合A的幂集为："<< endl;
    PrintSet2(powerSet);

    system("Pause");
    return 0;
}
```
