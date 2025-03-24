

# CUDA 和 NVIDIA 驱动

## Linux 桌面环境

`X Server` : 一个**图形服务器**，提供了图形界面的底层支持，管理所有与图形显示相关的内容，包括绘制图形界面、处理输入事件（如键盘和鼠标），以及与显示硬件的交互。它是所有图形应用程序和桌面环境的基础。

`GNOME` : 一个完整的**桌面环境**，它构建在 `X Server`（或 `Wayland`）之上，提供了窗口管理、文件管理器、应用程序、系统设置等功能，为用户提供图形化的操作界面。

`GDM` : `GNOME`的显示管理器，它在系统启动时提供登录界面，并启动 `X Server` 和 `GNOME` 会话。`GDM` 是 `GNOME` 桌面环境的一部分，负责管理登录过程和会话启动。

```bash
操作系统（Linux）
   ├── 显示服务器（Display Server，处理显示和输入）
   │     ├── X Server（X11 协议）
   │     │     ├── Xorg（X Server 的实现）
   │     │
   │     ├── Wayland（现代显示协议，不需要 X Server）
   │           ├── XWayland（Xorg 兼容层，支持旧的 X11 应用）
   │
   ├── 显示管理器（Display Manager，管理登录）
   │     ├── GDM（GNOME Display Manager）
   │           ├── 选择并启动 Xorg 或 Wayland
   │           ├── 启动 GNOME 桌面
   │
   ├── 桌面环境（Desktop Environment，提供完整 GUI 体验）
         ├── GNOME（默认支持 Xorg 和 Wayland）
         │     ├── GNOME Shell（窗口管理器）
         │     ├── Nautilus（文件管理器）
         │     ├── GNOME Terminal（终端）
```

`GDM`：`GNOME`桌面环境的默认显示管理器。它是一个全功能的显示管理器，旨在与`GNOME`桌面环境紧密集成，提供图形化的登录界面。

`LightDM`：轻量级的显示管理器，它的目标是快速和节省资源，适用于多种桌面环境。

## NVIDIA 驱动

### 安装驱动

#### 从 NVIDIA 官方网站安装

参考：[Ubuntu安装Nvidia英伟达显卡驱动，安装Cuda和Cudnn配置机器学习环境](https://qii404.me/2021/07/03/ubuntu-install-nvidia-driver.html)

NVIDIA Driver下载地址：https://www.nvidia.com/en-us/drivers/

(1) 检查gcc版本是否与要安装的驱动匹配，删除可能存在的旧Nvidia驱动

```bash
sudo apt-get remove --purge nvidia*
```

(2) 禁用开源Nouveau驱动

```bash
# Nouveau是开源的nvidia驱动，会与官方的nvidia驱动发生冲突
sudo vim /etc/modprobe.d/blacklist-nouveau.conf
# 添加以下内容
blacklist nouveau
options nouveau modeset=0
# 更新initramfs并重启
sudo update-initramfs -u
sudo reboot
# 检查是否已禁用Nouveau驱动，执行以下命令应没有输出才对
lsmod | grep nouveau
```

(3) 切换至`tty`控制台

按下 `Ctrl+Alt+F1~F6`任一切换到`tty`控制台

(4) 关闭`X Server`

```bash
sudo service lightdm stop
sudo service gdm stop
```

(5) 安装Nvidia驱动并重启系统

```bash
sudo sh NVIDIA-Linux-x86_64-550.127.05.run
sudo reboot
```

(6) 检查是否安装成功

```bash
# 查看版本和卸载nvidia驱动
nvidia-smi
nvidia-uninstall
```

#### 通过 Ubuntu 官方包管理器安装

(1) 禁用开源Nouveau驱动，参考上一节

(2) 安装Nvidia驱动并重启系统

```bash
sudo apt install nvidia-driver-550
sudo reboot
# 若指定版本不可用，可尝试使用ubuntu-drivers工具自动选择适合的版本
# sudo ubuntu-drivers autoinstall 
```

(3) 检查是否安装成功，参考上一节

### 显卡切换

`prime-select` 基于 **NVIDIA Optimus** 技术，它可以让系统在集成显卡和独立显卡之间切换，以提高电池续航和图形性能

```bash
# 查看当前显卡状态
prime-select query

# 切换到intel集成显卡
sudo prime-select intel

# 切换到nvidia独立显卡
sudo prime-select nvidia

#切换到on-demand模式
sudo prime-select on-demand
```

**注意**：

切换显卡后，需要重启计算机才能生效

### Xorg 配置

 `Xorg` 配置文件通常位于 `/etc/X11/xorg.conf` 或 `/etc/X11/xorg.conf.d/` 目录中

使用 `intel` 集成显卡显示，编辑 `/etc/X11/xorg.conf` 文件如下：

```bash
Section "Device"
    Identifier "Intel"
    Driver "modesetting"
    BusID "PCI:0:2:0"  # 集成显卡的总线地址，具体可以通过 lspci 命令查找
EndSection

Section "Screen"
    Identifier "IntelScreen"
    Device "Intel"
EndSection

Section "ServerLayout"
    Identifier "Layout0"
    Screen 0 "IntelScreen"
EndSection
```

### Linux 内核

ubuntu22.04更新Nvidia驱动导致掉网卡驱动的解决办法：更改内核版本

```bash
# 1.查看已安装内核版本
dpkg --list | grep linux-image

# 2.查看当前内核版本
uname -r

# 3.删除不需要的内核版本
sudo apt-get purge linux-image-5.4.0-74-generic

# 4.清理不再需要的内核包
sudo apt-get autoremove --purge

# 5.更新GRUB配置
sudo update-grub

# 6.重启后dpkg --list重新查看内核版本
```

如何进入tty命令行，ctrl+f3?

tmux命令行使用鼠标？？？

开机如何切换内核版本，开机时按住shift?

什么是Ubuntu内核？grub是什么？

### 

## CUDA安装与卸载

cuda历史版本下载地址：[CUDA Toolkit Archive | NVIDIA Developer](https://developer.nvidia.com/cuda-toolkit-archive)

CMake项目中设置GPU架构：NVIDIA CUDA架构的问题，[CUDA_ARCHITECTURES — CMake 3.26.3 文档](https://cmake.org/cmake/help/latest/prop_tgt/CUDA_ARCHITECTURES.html)

cuDNN是什么？

### 安装cuda

[CUDA Toolkit 11.8 Downloads | NVIDIA Developer](https://developer.nvidia.com/cuda-11-8-0-download-archive?target_os=Linux&target_arch=x86_64&Distribution=Ubuntu&target_version=18.04&target_type=runfile_local)

详细安装和卸载教程可参考NVIDIA官方网站提供的相应版本cuda的Versioned Online Documentation文档：[CUDA Toolkit Documentation](https://docs.nvidia.com/cuda/archive/11.8.0/)

```bash
# 1.安装前检查cuda对应的gcc版本是否符合要求

# 2.安装cuda，可选是否安装配套的nvidia驱动
wget https://developer.download.nvidia.com/compute/cuda/11.8.0/local_installers/cuda_11.8.0_520.61.05_linux.run
sudo sh cuda_11.8.0_520.61.05_linux.run

# 3.添加环境变量
# 将nvcc添加到环境变量，否则会找不到nvcc，cuda默认安装在/usr/local目录下，注意:
# /usr/local/cuda为软链接
# root用户添加环境变量的配置文件为/root/.bashrc
vim ~/.bashrc
export PATH=$PATH:/usr/local/cuda/bin
source ~/.bashrc

# 4.查看cuda版本，检查是否安装成功
nvcc -V | --version

# 5.cuda多版本切换
sudo rm /usr/local/cuda
sudo ln -s /usr/local/cuda-11.8 /usr/local/cuda
```

### 卸载cuda

```bash
# 卸载cuda，不同版本cuda可能有出入，具体参考相应版本cuda的官方Versioned Online Documentation文档
sudo apt-get --purge remove "*cuda*" "*cublas*" "*cufft*" "*cufile*" "*curand*" \
 "*cusolver*" "*cusparse*" "*gds-tools*" "*npp*" "*nvjpeg*" "nsight*"

# 卸载nvidia驱动
sudo apt-get --purge remove "*nvidia*" "libxnvctrl*"

# 清理卸载
sudo apt-get autoremove
```

