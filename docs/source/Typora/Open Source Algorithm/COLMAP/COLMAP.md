# COLMAP

## Review of Structure-from-Motion

```{figure} assets/pipline.png
---
alt: pipline
---
Incremental Structure-from-Motion pipeline
```

### Correspondence Search（检索匹配）

#### Feature Extraction

#### Matching

#### Geometric Verification

### Incremental Reconstruction

#### Image Registration

#### Triangulation

#### Bundle Adjustment

## 主要贡献

1、 提出了提高初始化和三角化鲁棒性的几何验证策略。

2、 一种最大化鲁棒性和准确性的下一最佳匹配图像选择策略

3、 一种可以获得更为完整的场景结构且计算代价更小的鲁棒三角化方法

4、 一种迭代BA、重三角化、外点滤除策略，显著提升重建完整性和精度，减轻漂移影响

5、 一种用于挖掘密集图像集间的冗余视图的高效BA参数化方法

### 场景图增强

### 下一最佳视图的选择

```{figure} assets/Scores.png
---
alt: Scores
---
Scores for different number of points (left and right) with different distributions (top and bottom) in the image for L = 3
```

一种流行的策略是选择看到最多三角点的图

### 鲁棒高效的三角化

## 参考资料

官方文档

[COLMAP - Structure-From-Motion and Multi-View Stereo (demuc.de)](https://demuc.de/colmap/#tutorial)

[COLMAP — COLMAP 3.8-dev documentation](https://colmap.github.io/index.html)

[https://github.com/colmap/colmap](https://github.com/colmap/colmap)

[Structure-from-Motion Revisited](./papers/Structure-from-Motion.pdf)