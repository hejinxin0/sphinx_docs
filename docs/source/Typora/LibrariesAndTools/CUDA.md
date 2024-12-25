

# CUDA和NVIDIA驱动

## NVIDIA驱动

```bash
nvidia-smi
nvidia-uninstall
```

## CUDA安装与卸载

cuda历史版本下载地址：[CUDA Toolkit Archive | NVIDIA Developer](https://developer.nvidia.com/cuda-toolkit-archive)

CMake项目中设置GPU架构：NVIDIA CUDA架构的问题，[CUDA_ARCHITECTURES — CMake 3.26.3 文档](https://cmake.org/cmake/help/latest/prop_tgt/CUDA_ARCHITECTURES.html)

cuDNN是什么？

### 安装cuda

[CUDA Toolkit 11.8 Downloads | NVIDIA Developer](https://developer.nvidia.com/cuda-11-8-0-download-archive?target_os=Linux&target_arch=x86_64&Distribution=Ubuntu&target_version=18.04&target_type=runfile_local)

```bash
#安装cuda
wget https://developer.download.nvidia.com/compute/cuda/11.8.0/local_installers/cuda_11.8.0_520.61.05_linux.run
sudo sh cuda_11.8.0_520.61.05_linux.run #可选是否安装配套的nvidia驱动

#将nvcc添加到环境变量，否则会找不到nvcc
vim ~/.bashrc
export PATH=$PATH:/usr/local/cuda-11.8/bin #cuda默认安装在/usr/local目录下
source ~/.bashrc
#/usr/local路径下如果有cuda目录软链接到cuda-11.8，可以使用export PATH=$PATH:/usr/local/cuda/bin

#查看cuda版本检查是否安装成功
nvcc -V | --version
```

### 卸载cuda

