

# CUDA和NVIDIA驱动

## NVIDIA驱动

### 从NVIDIA官方网站安装

NVIDIA Driver下载地址：https://www.nvidia.com/en-us/drivers/

① 检查gcc版本是否与要安装的驱动匹配，删除可能存在的旧Nvidia驱动

```bash
sudo apt-get remove --purge nvidia*
```

② 禁用开源Nouveau驱动

```bash
#Nouveau是开源的nvidia驱动，会与官方的nvidia驱动发生冲突
sudo vim /etc/modprobe.d/blacklist-nouveau.conf
#添加以下内容
blacklist nouveau
options nouveau modeset=0
#更新initramfs并重启
sudo update-initramfs -u
sudo reboot
#检查是否已禁用Nouveau驱动，执行以下命令应没有输出才对
lsmod | grep nouveau
```

③ 切换至tty控制台

按下 `Ctrl+Alt+F1~F6`任一切换到tty控制台

④ 关闭`X Server`

```bash
sudo service lightdm stop
sudo service gdm stop
```

⑤ 安装Nvidia驱动并重启系统

```bash
sudo sh NVIDIA-Linux-x86_64-550.127.05.run
sudo reboot
```

⑥ 检查是否安装成功

```bash
#查看版本
nvidia-smi
#卸载nvidia驱动
nvidia-uninstall
```



### 通过Ubuntu官方包管理器安装

① 禁用开源Nouveau驱动，参考上一节

② 安装Nvidia驱动并重启系统

```bash
sudo apt install nvidia-driver-550
sudo reboot
#若指定版本不可用，可尝试使用ubuntu-drivers工具自动选择适合的版本
#sudo ubuntu-drivers autoinstall 
```

③ 检查是否安装成功，参考上一节

### 

ubuntu22.04更新Nvidia驱动导致掉网卡驱动的解决办法：更改内核版本

```bash
#1.查看已安装内核版本
dpkg --list | grep linux-image
#2.查看当前内核版本
uname -r
#3.删除不需要的内核版本
sudo apt-get purge linux-image-5.4.0-74-generic
#4.清理不再需要的内核包
sudo apt-get autoremove --purge
#5.更新GRUB配置
sudo update-grub
#6.重启后dpkg --list重新查看内核版本
```

如何进入tty命令行，ctrl+f3?

开机如何切换内核版本，开机时按住shift?

什么是Ubuntu内核？grub是什么？

### 

## CUDA安装与卸载

cuda历史版本下载地址：[CUDA Toolkit Archive | NVIDIA Developer](https://developer.nvidia.com/cuda-toolkit-archive)

CMake项目中设置GPU架构：NVIDIA CUDA架构的问题，[CUDA_ARCHITECTURES — CMake 3.26.3 文档](https://cmake.org/cmake/help/latest/prop_tgt/CUDA_ARCHITECTURES.html)

cuDNN是什么？

### 安装cuda

[CUDA Toolkit 11.8 Downloads | NVIDIA Developer](https://developer.nvidia.com/cuda-11-8-0-download-archive?target_os=Linux&target_arch=x86_64&Distribution=Ubuntu&target_version=18.04&target_type=runfile_local)

```bash
#1.安装前检查cuda对应的gcc版本是否符合要求

#2.安装cuda，可选是否安装配套的nvidia驱动
wget https://developer.download.nvidia.com/compute/cuda/11.8.0/local_installers/cuda_11.8.0_520.61.05_linux.run
sudo sh cuda_11.8.0_520.61.05_linux.run

#3.添加环境变量
#将nvcc添加到环境变量，否则会找不到nvcc，cuda默认安装在/usr/local目录下，注意:
#/usr/local/cuda为软链接
#root用户添加环境变量的配置文件为/root/.bashrc
vim ~/.bashrc
export PATH=$PATH:/usr/local/cuda/bin
source ~/.bashrc

#4.查看cuda版本，检查是否安装成功
nvcc -V | --version

#5.cuda多版本切换
sudo rm /usr/local/cuda
sudo ln -s /usr/local/cuda-11.8 /usr/local/cuda
```

### 卸载cuda

