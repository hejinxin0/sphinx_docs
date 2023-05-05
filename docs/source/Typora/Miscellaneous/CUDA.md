

# CUDA

## 安装配置与卸载

下载地址：[CUDA Toolkit Archive | NVIDIA Developer](https://developer.nvidia.com/cuda-toolkit-archive)

```bash
nvcc -V | --version # 查看cuda版本
```

CMake项目中设置GPU架构：NVIDIA CUDA架构的问题，[CUDA_ARCHITECTURES — CMake 3.26.3 文档](https://cmake.org/cmake/help/latest/prop_tgt/CUDA_ARCHITECTURES.html)

cuDNN是什么？？

### Ubuntu安装cuda10.1

```bash
sudo dpkg -i cuda-repo-ubuntu1804-10-1-local-10.1.105-418.39_1.0-1_amd64.deb
sudo apt-key add /var/cuda-repo-<version>/7fa2af80.pub
sudo apt-get update
sudo apt-get install cuda
```

```{note}
第二步`apt-key`时需要在`/var`目录下找到相应的`cuda-repo`目录，将`/var/cuda-repo-<version>/7fa2af80.pub`替换为该目录下的`.pub`文件绝对路径
```





~~~{error}
```bash
下列软件包有未满足的依赖关系：
 cuda-libraries-dev-10-1 : 依赖: libcublas-dev (>= 10.1.0.105) 但是它将不会被安装
 cuda-samples-10-1 : 依赖: libcublas-dev (>= 10.1.0.105) 但是它将不会被安装
 cuda-visual-tools-10-1 : 依赖: libcublas-dev (>= 10.1.0.105) 但是它将不会被安装
E: 有未能满足的依赖关系。请尝试不指明软件包的名字来运行“apt --fix-broken install”(也可以指定一个解决办法)。
```

按照上面提示执行`sudo apt --fix-broken install`后遇到以下问题
```bash
dpkg: 处理归档 /var/cuda-repo-10-1-local-10.1.105-418.39/./libcublas-dev_10.1.0.105-1_amd64.deb (--unpack)时出错：
 正试图覆盖 /usr/include/cublas_v2.h，它同时被包含于软件包 nvidia-cuda-dev 9.1.85-3ubuntu1
dpkg-deb: 错误: 粘贴 subprocess was killed by signal (断开的管道)
在处理时有错误发生：
 /var/cuda-repo-10-1-local-10.1.105-418.39/./libcublas-dev_10.1.0.105-1_amd64.deb
E: Sub-process /usr/bin/dpkg returned an error code (1)
```
**解决方法**：先强制覆盖再执行相应命令
```bash
sudo dpkg -i --force-overwrite /var/cuda-repo-10-1-local-10.1.105-418.39/./libcublas-dev_10.1.0.105-1_amd64.deb
sudo apt --fix-broken install
```
~~~



````{admonition} 安装 cuda 后找不到 nvcc
```bash
locate nvcc #查看nvcc是否存在，找到nvcc位置
vim ~/.bashrc
export PATH=$PATH:/usr/local/cuda-10.1/bin
source ~/.bashrc
```
````

