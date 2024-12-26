# 3D Gaussian Splatting (3DGS)

## 正向渲染

**3DGS的属性：**${(\mu,\Sigma,c,\alpha)}$ , 位置中心$\mu$，不透明度$\alpha$，3D协方差矩阵$\Sigma$、颜色$c$ (可由球谐函数表示)

**Splatting泼溅：**三维空间中的3D高斯椭球投影到2D图像空间(椭圆)进行渲染



<img src="assets/NeRF_and_3DGS.png" alt="image-20241226211629702" style="zoom:80%;" />



<img src="assets/forward_process_of_3DGS.png" alt="image-20241226212736737" style="zoom:80%;" />

## 反向优化



<img src="assets/Algorithm1.png" alt="image-20241226213114411" style="zoom:80%;" />



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

