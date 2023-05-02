[TOC]

# CMake

## Ubuntu安装CMake

- **apt-get安装CMake**

```bash
sudo apt-get install cmake
```

默认安装目录：`/usr/bin/cmake`

- **snap安装新版CMake**

```bash
sudo snap install cmake --classic
```

默认安装目录：`/snap/bin/cmake`

- **离线安装cmake（需要export或者source）**

## CMake项目结构

CMakeLists.txt.user

cmake_install.cmake

CMakeCache.txt

Makefile

## 常用命令

### 版本、编译选项

#### cmake_minimum_required

```cmake
# 项目所需的最低 cmake 版本
cmake_minimum_required(VERSION <min>[...<policy_max>] [FATAL_ERROR])
cmake_minimum_required(VERSION 3.10)
```

设置release模式和debug模式

### 设置和选项

#### set

#### option

### 包文件

#### find_package

```cmake
# 查找库文件
# [REQUIRED] 如果找不到包，该选项将停止处理并显示错误消息
find_package(<PackageName> [version] [EXACT] [QUIET] [MODULE] [REQUIRED]
             [OPTIONAL_COMPONENTS components...])
find_package(OpenCV 4.0 REQUIRED)
```

find_package的规则在哪提供，例如find_package(OpenCV)、find_package(Eigen)

### 链接库

链接库一般需要include头文件，然后link

#### add_library

#### link_directories

#### target_link_libraries

#### include_directories和target_include_directories

**add_library、link_libraries、`target_link_libraries`三者的区别？？？？？？以及include_directories、link_directories的功能**

### 可执行文件

#### add_executable

```cmake
# 根据列出的源文件生成可执行文件
add_executable(<name> [source1] [source2 ...])
```

### 子项目

#### add_subdirectory

```cmake
# 添加并构建子目录（子项目）
#  source_dir 必选参数，
#  binary_dir 可选参数，
add_subdirectory(source_dir [binary_dir] [EXCLUDE_FROM_ALL])
```

#### include

#### list

#### install

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

##太简单了，没有add_library和add_subdirectory的过程！！！！！！！！！！！！
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
CMAKE_ARCHIVE_OUTPUT_DIRECTORY
CMAKE_LIBRARY_OUTPUT_DIRECTORY和LIBRARY_OUTPUT_PATH
CMAKE_RUNTIME_OUTPUT_DIRECTORY
EXECUTABLE_OUTPUT_PATH

${PROJECT_NAME}
${PROJECT_SOURCE_DIR}
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

| 命令行                          |         源文件目录         | 构建目录 |
| :------------------------------ | :------------------------: | :------: |
| `cmake build` (existing)        | 从`CMakeCache.txt`文件加载 | `build`  |
| `cmake src`<br />`cmake -S src` |           `src`            |  `cwd`   |
|                                 |           `src`            |   cwd    |
| `cmake -S src build`            |           `src`            | `build`  |
| `cmake -S src -B build`         |           `src`            | `build`  |
| `cmake -B build`                |           `cwd`            | `build`  |
| `cmake -B build src`            |           `src`            | `build`  |
| `cmake -B build -S src`         |           `src`            | `build`  |

## 常见问题

未定义的引用

CMake中没有添加相应的第三方库

target_link相应的lib后需要include相应的头文件路径吗
