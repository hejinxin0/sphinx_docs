[TOC]

# CMake

## CMake项目结构

CMakeLists.txt.user

cmake_install.cmake

CMakeCache.txt

Makefile

离线安装cmake（需要export或者source）

## 常用命令

### 脚本命令

#### cmake_minimum_required

```cmake
# 项目所需的最低 cmake 版本
cmake_minimum_required(VERSION <min>[...<policy_max>] [FATAL_ERROR])
cmake_minimum_required(VERSION 3.10)
```

#### find_package

```cmake
# 查找库文件
# [REQUIRED] 如果找不到包，该选项将停止处理并显示错误消息
find_package(<PackageName> [version] [EXACT] [QUIET] [MODULE] [REQUIRED]
             [OPTIONAL_COMPONENTS components...])
find_package(OpenCV 4.0 REQUIRED)
```

find_package的规则在哪提供，例如find_package(OpenCV)、find_package(Eigen)

#### include

#### list

#### option

#### set

### 项目命令

#### add_executable

```cmake
# 根据列出的源文件生成可执行文件
add_executable(<name> [source1] [source2 ...])
```

#### add_library

#### add_subdirectory

```cmake
# 添加并构建子目录（子项目）
#  source_dir 必选参数，
#  binary_dir 可选参数，
add_subdirectory(source_dir [binary_dir] [EXCLUDE_FROM_ALL])
```

#### install

#### target_link_libraries

**add_library、link_libraries、`target_link_libraries`三者的区别？？？？？？以及include_directories、link_directories的功能**

### 一个简单的CMakeLists.txt文件

```cmake
# cmake版本号
cmake_minimum_required(VERSION 3.10)
# 项目名称和版本号
project(calibration VERSION 1.0)
set(OpenCV_DIR C:/opencv-4.5.2/build/install)
# C++版本
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_BUILD_TYPE "Release")
find_package(OpenCV 4.0 REQUIRED)
add_executable(${PROJECT_NAME} calibration.cpp)
target_link_libraries(${PROJECT_NAME} ${OpenCV_LIBS})
```

**详细信息参考链接：**

https://cmake.org/cmake/help/latest/manual/cmake-commands.7.html

## CMake变量、set设定常用参数

https://cmake.org/cmake/help/latest/manual/cmake-variables.7.html

```cmake
CMAKE_INSTALL_PREFIX
INCLUDE_INSTALL_DIR
CMAKE_MODULE_PATH
```

## CMake语言

Directories (CMakeLists.txt),

Scripts (<script>.cmake), and

Modules (<module>.cmake).

https://cmake.org/cmake/help/latest/manual/cmake-language.7.html

## 命令行

### 构建CMake项目

```bash
cmake [<options>] <path-to-source>
cmake [<options>] <path-to-existing-build>
cmake [<options>] -S <path-to-source> -B <path-to-build>
# 指定的路径可以是绝对路径，也可以是相对于当前工作目录的路径。源代码树必须包含CMakeLists.txt文件，并且不能包含
# CMakeCache.txt文件，因为后者标识了一个现有的构建树
```

以上命令可以混用，`-S`或`-B`指定的路径总是分别为源文件目录或构建目录，如果只给出其中一种类型的路径，则另一类型的路径为当前工作目录 (cwd) 

| 命令行                   |         源文件目录         | 构建目录 |
| :----------------------- | :------------------------: | :------: |
| `cmake build` (existing) | 从`CMakeCache.txt`文件加载 | `build`  |
| `cmake src`              |           `src`            |   cwd    |
| `cmake -S src`           |           `src`            |   cwd    |
| `cmake -S src build`     |           `src`            | `build`  |
| `cmake -S src -B build`  |           `src`            | `build`  |
| `cmake -B build`         |           `cwd`            | `build`  |
| `cmake -B build src`     |           `src`            | `build`  |
| `cmake -B build -S src`  |           `src`            | `build`  |

## 常见问题

未定义的引用

CMake中没有添加相应的第三方库
