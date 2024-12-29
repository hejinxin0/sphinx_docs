# 3D Gaussian Splatting (3DGS)

<img src="assets/3DGS_pipeline.png" alt="3DGS_pipeline" style="zoom: 80%; display: block; margin-left: auto; margin-right: auto;" />

## 正向渲染

基于点的渲染

新视角合成

### NeRF与3DGS

NeRF和3DGS的渲染可看作是彼此的逆过程

NeRF: 后向映射 (backward mapping)，沿射线采样，然后查询MLP以获得相应的颜色和不透明度

3DGS: 前向映射 (forward mapping)，将所有3D高斯投影到图像空间 (即splatting)，然后并行渲染

<img src="assets/NeRF_and_3DGS.png" alt="NeRF_and_3DGS" style="zoom: 80%; display: block; margin-left: auto; margin-right: auto;" />

<figure style="text-align: center;">
  <figcaption>NeRF与3DGS</figcaption>
</figure>

### 3DGS的属性

 ${(\boldsymbol{\mu},\boldsymbol{\Sigma},\boldsymbol{c},\alpha)}$

- 中心位置$\boldsymbol{\mu}$

- 3D协方差矩阵$\boldsymbol{\Sigma}$

- 颜色$\boldsymbol{c}$ (可由球谐函数表示)
- 不透明度$\alpha$

### 

### Splatting泼溅

 三维空间中的3D高斯椭球投影到2D图像空间 (椭圆) 进行渲染




$$
G(\boldsymbol{x}) = \exp \left( { - \frac{1}{2}{{(\boldsymbol{x} - \boldsymbol{\mu} )}^T}{\boldsymbol{\Sigma} ^{ - 1}}(\boldsymbol{x} - \boldsymbol{\mu} )} \right)
$$


$$
\boldsymbol{\Sigma}  = \boldsymbol{RS}{\boldsymbol{S}^{\rm{T}}}{\boldsymbol{R}^{\rm{T}}}
$$

$$
\boldsymbol{\Sigma}' = \boldsymbol{JW\Sigma} {\boldsymbol{W}^{\rm{T}}}{\boldsymbol{J}^{\rm{T}}}
$$

$$
\boldsymbol{C} = \sum\limits_{i \in {\cal N}} {{\boldsymbol{c}_i}{\alpha _i}\prod\limits_{j = 1}^{i - 1} {(1 - {\alpha _i})} }
$$

### 像素渲染

给定像素点$\boldsymbol x$，通过与其到所有重叠高斯函数的距离，即这些高斯函数的深度。这些可以通过观察变换 $\boldsymbol W$ 计算出来，形成高斯函数的排序列表$\cal N$。然后进行𝛼-blending混合，计算该像素的最终颜色

### 并行渲染

**Tiles (Patches)**：为避免逐像素计算的成本，3DGS改为patch级别的渲染。首先将图像分割为多个不重叠的`patch`，称为`tile`，每个图块包含 16×16 像素，然后确定`tile`与投影高斯的相交情况，由于投影高斯可能会与多个`tile`相交，需要进行复制，并为每个复制体分配相关`tile`的标识符。

<img src="assets/forward_process_of_3DGS.png" alt="forward_process_of_3DGS" style="zoom: 80%; display: block; margin-left: auto; margin-right: auto;" />

<figure style="text-align: center;">
  <figcaption>3DGS的前向过程</figcaption>
</figure>


## 反向优化

<img src="assets/algorithm1.png" alt="algorithm1" style="zoom: 80%; display: block; margin-left: auto; margin-right: auto;" />



>**Web Pages：**
>
>[3DGS综述以及对3DGS的理解：A Survey on 3D Gaussian Splatting - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/679809915)
>
>**Project Pages:**
>
>[3D Gaussian Splatting for Real-Time Radiance Field Rendering (inria.fr)](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/)
>
>**Papers:**
>
>[1] [3D Gaussian Splatting for Real-Time Radiance Field Rendering (2023)](https://arxiv.org/abs/2308.04079) ([pdf](./papers/3DGS.pdf))
>
>[2] [A Survey on 3D Gaussian Splatting (2024)](https://arxiv.org/abs/2401.03890) ([pdf](./papers/A_Survey_on_3D_Gaussian_Splatting.pdf))
>
>

