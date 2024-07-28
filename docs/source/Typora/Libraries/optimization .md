# Non-linear Optimization

## g2o

参考：[g2o：非线性优化与图论的结合 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/600012824)

### 代价函数



### 求解器

1. Gauss-Newton Solver：高斯-牛顿法求解器，通过求解线性方程组来更新优化变量。
2. Levenberg-Marquardt Solver：Levenberg-Marquardt算法求解器，可以在高斯-牛顿法和梯度下降法之间平衡，适用于非线性问题。
3. Dogleg Solver：狗腿法求解器，既可以使用高斯-牛顿法，也可以使用梯度下降法，可以在两者之间平衡。
4. Powell's Dogleg Solver：Powell's狗腿法求解器，与普通狗腿法求解器相比，使用了更高级的算法来计算步长。
5. GN Var Solver：高斯-牛顿法求解器，使用变量增量来更新优化变量。
6. LM Var Solver：Levenberg-Marquardt算法求解器，使用变量增量来更新优化变量。
7. Block Solver：块求解器，可以处理大型稀疏矩阵，支持多线程求解。
8. Linear Solver Cholmod：基于Cholmod库的线性求解器，使用超松弛法来求解线性方程组。
9. Linear Solver CSparse：基于CSparse库的线性求解器，使用共轭梯度法来求解线性方程组。
10. Linear Solver Eigen：基于Eigen库的线性求解器，使用LU分解或QR分解来求解线性方程组。
11. Linear Solver PCG：预处理共轭梯度法求解器，使用预处理技术加速共轭梯度法的收敛速度。

#### 线性求解器类型（位于g2o/solvers文件夹下）

[g2o不同线性方程求解器（LinearSolver）的区别](https://blog.csdn.net/ziliwangmoe/article/details/89399540)

g2o支持多种线性求解器类型，以下是其中的几种：

1. Linear Solver Cholmod：基于Cholmod库的线性求解器，使用超松弛法来求解线性方程组。

2. Linear Solver CSparse：基于CSparse库的线性求解器，使用共轭梯度法来求解线性方程组。

3. Linear Solver Eigen：基于Eigen库的线性求解器，使用LU分解或QR分解来求解线性方程组。

用户可以根据自己的需求选择合适的线性求解器来求解非线性最小二乘问题。

#### 非线性求解器类型



## Ceres

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

### 构造代价函数

### 构建优化问题

### 配置并运行求解器

## gtsam

[(13条消息) SLAM中姿态估计的图优化方法比较（g2o/Ceres/GTSAM/SE-Sync）_自动驾驶之心的博客-CSDN博客](https://blog.csdn.net/CV_Autobot/article/details/127456573)