# COLMAP配置运行与算法框架

## 配置运行

### 安装配置

````{error}
```bash
Could not find `LZ4`
```
```{figure} assets/Install-Colmap-Error.png
```
````

**解决方法：** 安装相应的包 `sudo apt-get install liblz4-dev`

````{error}
```bash
Cannot specify include directories for imported target "CUDA::cudart"
Cannot specify include directories for imported target "CUDA::curand"
```
````

**解决方法：** 安装新版CMake `sudo snap install cmake --classic`

````{error}
```bash
CMake Error at CMakeLists.txt:255 (message):
  You must set CMAKE_CUDA_ARCHITECTURES to e.g.  'native', 'all-major', '70',
  etc.  More information at
  https://cmake.org/cmake/help/latest/prop_tgt/CUDA_ARCHITECTURES.html
```
````



错误原因：[CUDA_ARCHITECTURES — CMake 3.26.3 文档](https://cmake.org/cmake/help/latest/prop_tgt/CUDA_ARCHITECTURES.html)
