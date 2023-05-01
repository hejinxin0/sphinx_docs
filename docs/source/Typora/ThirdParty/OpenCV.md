# OpenCV



Opencv命令行参数cv::CommandLineParser：

https://blog.csdn.net/kasteluo/article/details/86621951

https://docs.opencv.org/4.5.2/d0/d2e/classcv_1_1CommandLineParser.html

## 安装配置与卸载

### 安装和查看版本

默认安装目录：

[CSDN：Ubuntu18.04安装Opencv4.5.2](https://blog.csdn.net/qq_17769915/article/details/124087687)

```bash
pkg-config  --libs opencv  # 查看libs库
pkg-config  --modversion  opencv   # 查看版本号
```

### 安装过程中的问题

~~~{error} 
构建`libopencv_imgcodecs.so`报错：没有规则可制作目标“`/usr/lib/libjpeg.so`”
```{figure} assets/OpenCV安装报错.png
```
~~~

- **错误原因：** 缺少或者未在指定的路径找到 `libjpeg.so`

- **解决方法：** `locate`查找`libjpeg.so`位置，如果存在但没有位于指定的路径`/usr/lib/libjpeg.so`，例如位于`/usr/lib/x86_64-linux-gnu/libjpeg.so` ，则建立软链接

```bash
sudo ln -s /usr/lib/x86_64-linux-gnu/libjpeg.so /usr/lib/libjpeg.so
```

### 卸载

[CSDN：wsl+opencv——清除旧版并安装新版，实测有效](https://blog.csdn.net/m0_51984869/article/details/127538531)

## cv::Mat

```{note}
`cv::Mat::Size(cols,rows)`的格式，列数在前，行数在后
```

https://blog.csdn.net/weixin_47156401/article/details/120023261

图片转换cvtColor、图片的通道数、BGR和RGB、RGBA，灰度图可以三通道吗

### 初始化

### 访问元素

### 矩阵块操作

colRange

block

### 矩阵运算

加减乘除、数乘、向量和标量的加减

#### 

## 浅拷贝与深拷贝

## 图片读取、显示、调整大小resize、与转换

cv::imread

cv::imwrite

imshow

resize

cv::cvtColor



通道处理BRG2RGB，BGRA等等

## 特征提取与匹配

cv::keypoint类的成员变量包括哪些：位置、方向、角度、金字塔层数？？

KeyPoint类及其内部结构

DMatch类及其内部结构

Mat Descriptor类及其内部结构（行数表示描述子的数目，列数表示描述子的维数）

**不同于brief描述子的uchar类型，sift和surf均采用float型。所以ORB(brief)描述子8维，32bytes（256bits）,CV_8UC1。SIFT描述子128维，512bytes，CV_32UC4（512*8/32 = 32*4，第一个32表示描述子Mat是32列，第二个32表示float类型）。SURF描述子64维，256bytes，CV_32UC2。（OpenCV里compute的描述子的列数都是32）**
————————————————
版权声明：本文为CSDN博主「cc_sunny」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/aptx704610875/article/details/51503149

## 多视图几何与位姿估计

## 图像滤波

## 
