

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

