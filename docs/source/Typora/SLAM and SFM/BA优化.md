# BA优化

## 线性方程组

线性方程组的几种分解方法：svd，QR、LU、

## 非线性优化问题的数学模型

## 非线性优化库

### Ceres

```C++
ceres::Problem 
ceres::Solver::Options
ceres::Solver::Summary
ceres::CostFunction
    
// 求解器类ceres::Solver中的Solve函数来求解非线性优化问题，引用的三个参数中包含三个重要的类ceres::Problem 、ceres::Solver::Options、 ceres::Solver::Summary
CERES_EXPORT void Solve(const Solver::Options& options,
                        Problem* problem,
                        Solver::Summary* summary);
```

#### 构造代价函数

#### 构建优化问题

#### 配置并运行求解器

### g2o非线性优化

线性求解器类型（位于g2o/solvers文件夹下）

[g2o不同线性方程求解器（LinearSolver）的区别](https://blog.csdn.net/ziliwangmoe/article/details/89399540)

### gtsam

[CSDN：SLAM中姿态估计的图优化方法比较（g2o/Ceres/GTSAM/SE-Sync）](