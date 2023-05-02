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



**错误原因：**NVIDIA GPU架构的问题，[CUDA_ARCHITECTURES — CMake 3.26.3 文档](https://cmake.org/cmake/help/latest/prop_tgt/CUDA_ARCHITECTURES.html)

**解决方法：**在colmap的`CMakeLists.txt:255`处前面添加对`CMAKE_CUDA_ARCHITECTURES`的定义：`set(CMAKE_CUDA_ARCHITECTURES all-major)`



````{error}
```bash
[ 34%] Built target vlfeat
[ 34%] Building CUDA object src/CMakeFiles/colmap_cuda.dir/mvs/gpu_mat_prng.cu.o
nvcc fatal   : Unknown option 'fPIC'
src/CMakeFiles/colmap_cuda.dir/build.make:75: recipe for target 'src/CMakeFiles/colmap_cuda.dir/mvs/gpu_mat_prng.cu.o' failed
make[2]: *** [src/CMakeFiles/colmap_cuda.dir/mvs/gpu_mat_prng.cu.o] Error 1
CMakeFiles/Makefile2:633: recipe for target 'src/CMakeFiles/colmap_cuda.dir/all' failed
make[1]: *** [src/CMakeFiles/colmap_cuda.dir/all] Error 2
Makefile:135: recipe for target 'all' failed
make: *** [all] Error 2
```
````

[https://github.com/colmap/colmap/issues/1753](https://github.com/colmap/colmap/issues/1753)

