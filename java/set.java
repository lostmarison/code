```java
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

public class Main {
    //并集
    public static ArrayList<Integer> Union(ArrayList<Integer> A, ArrayList<Integer> B) {
        ArrayList<Integer> result = new ArrayList<>(A);
        for (int b : B) {
            if (!A.contains(b)) {//如果集合B中元素不在集合A中
                result.add(b);
            }
        }
        Collections.sort(result);//排序
        return result;
    }

    //交集
    public static ArrayList<Integer> Intersection(ArrayList<Integer> A, ArrayList<Integer> B) {
        ArrayList<Integer> result = new ArrayList<>();
        for (int a : A) {
            if (B.contains(a)) {//如果集合A中元素在集合B中
                result.add(a);
            }
        }
        return result;
    }

    //差集A-B
    public static ArrayList<Integer> Difference(ArrayList<Integer> A, ArrayList<Integer> B) {
        ArrayList<Integer> result = new ArrayList<>();
        for (int a : A) {
            if (!B.contains(a)) {//如果集合A中元素不在在集合B中
                result.add(a);
            }
        }
        return result;
    }

    //补集
    public static ArrayList<Integer> Complement(ArrayList<Integer> A, ArrayList<Integer> U) {
        ArrayList<Integer> result = new ArrayList<>();
        for (int u : U) {
            if (!A.contains(u)) {//如果全集U中元素不在集合A中
                result.add(u);
            }
        }
        return result;
    }

    //对称差集
    public static ArrayList<Integer> Symmetric(ArrayList<Integer> A, ArrayList<Integer> B) {
        ArrayList<Integer> set1 = Difference(A, B);//A-B
        ArrayList<Integer> set2 = Difference(B, A);//B-A
        ArrayList<Integer> result = Union(set1, set2);//(A-B)U(B-A)
        Collections.sort(result);//排序
        return result;
    }

    public static void main(String[] args) {
        ArrayList<Integer> A = new ArrayList<>(Arrays.asList(1, 3, 4));
        ArrayList<Integer> B = new ArrayList<>(Arrays.asList(1, 2, 5, 6));
        ArrayList<Integer> U = new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5, 6));

        ArrayList<Integer> union = Union(A, B);
        System.out.printf("集合A与集合B的并集：%s\n", union);

        ArrayList<Integer> intersection = Intersection(A, B);
        System.out.printf("集合A与集合B的交集：%s\n", intersection);

        ArrayList<Integer> difference = Difference(A, B);
        System.out.printf("集合A与集合B的差集：%s\n", difference);

        ArrayList<Integer> symmetric = Symmetric(A, B);
        System.out.printf("集合A与集合B的对称差集：%s\n", symmetric);

        ArrayList<Integer> complement = Complement(A, U);
        System.out.printf("集合A在全集U中的补集：%s\n", complement);
    }
}
```
