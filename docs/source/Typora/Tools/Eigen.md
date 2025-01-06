# Eigen

## 安装配置

### 编译安装

默认安装目录

如何查看Eigen版本

Windows下安装

### CMake配置

## Matrix矩阵模块

### 初始化

Eigen::Matrix3d::Constant

### 矩阵的块操作

官方文档：[Eigen: Block operations](https://eigen.tuxfamily.org/dox/group__TutorialBlockOperations.html)

#### 行操作和列操作

| 块操作        | 方法             |
| :------------ | :--------------- |
| 矩阵的第 i 行 | `matrix.row(i);` |
| 矩阵的第 j 列 | `matrix.col(j);` |

```{note}
索引从0开始
```

colwise()

### Corner-related操作

| 块操作                                                       | 动态大小的块                     | 固定大小的块                       |
| :----------------------------------------------------------- | :------------------------------- | :--------------------------------- |
| Top-left p by q block [*](https://eigen.tuxfamily.org/dox/group__TutorialBlockOperations.html) | `matrix.topLeftCorner(p,q);`     | `matrix.topLeftCorner<p,q>();`     |
| Bottom-left p by q block [*](https://eigen.tuxfamily.org/dox/group__TutorialBlockOperations.html) | `matrix.bottomLeftCorner(p,q);`  | `matrix.bottomLeftCorner<p,q>();`  |
| Top-right p by q block [*](https://eigen.tuxfamily.org/dox/group__TutorialBlockOperations.html) | `matrix.topRightCorner(p,q);`    | `matrix.topRightCorner<p,q>();`    |
| Bottom-right p by q block [*](https://eigen.tuxfamily.org/dox/group__TutorialBlockOperations.html) | `matrix.bottomRightCorner(p,q);` | `matrix.bottomRightCorner<p,q>();` |
| Block containing the first q rows [*](https://eigen.tuxfamily.org/dox/group__TutorialBlockOperations.html) | `matrix.topRows(q);`             | `matrix.topRows<q>();`             |
| Block containing the last q rows [*](https://eigen.tuxfamily.org/dox/group__TutorialBlockOperations.html) | `matrix.bottomRows(q);`          | `matrix.bottomRows<q>();`          |
| Block containing the first p columns [*](https://eigen.tuxfamily.org/dox/group__TutorialBlockOperations.html) | `matrix.leftCols(p);`            | `matrix.leftCols<p>();`            |
| Block containing the last q columns [*](https://eigen.tuxfamily.org/dox/group__TutorialBlockOperations.html) | `matrix.rightCols(q);`           | `matrix.rightCols<q>();`           |
| Block containing the q columns starting from i [*](https://eigen.tuxfamily.org/dox/group__TutorialBlockOperations.html) | `matrix.middleCols(i,q);`        | `matrix.middleCols<q>(i);`         |
| Block containing the q rows starting from i [*](https://eigen.tuxfamily.org/dox/group__TutorialBlockOperations.html) | `matrix.middleRows(i,q);`        | `matrix.middleRows<q>(i);`         |

### block操作

| 块操作                                     | 动态大小的块             | 固定大小的块              |
| :----------------------------------------- | :----------------------- | :------------------------ |
| Block of size `(p,q)`, starting at `(i,j)` | `matrix.block(i,j,p,q);` | `matrix.block<p,q>(i,j);` |

### 向量的块操作

| 块操作                               | 动态大小的块           | 固定大小的块            |
| :----------------------------------- | :--------------------- | :---------------------- |
| 获取向量的前 n 个元素                | `vector.head(n);`      | `vector.head<n>();`     |
| 获取向量的后 n 个元素                | `vector.tail(n);`      | `vector.tail<n>();`     |
| 获取从向量第 i 个元素开始的 n 个元素 | `vector.segment(i,n);` | `vector.segment<n>(i);` |

### 向量与标量之间的四则运算

齐次坐标homogeneous

coeff方法是做什么的

## Geometry几何变换模块

### 头文件

```
#include <Eigen/Geometry>
```

### 四元数

```
Eigen::Quaterniond
```

