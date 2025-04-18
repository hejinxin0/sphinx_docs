[TOC]

**官方文档：https://git-scm.com/docs**

**菜鸟教程：https://www.runoob.com/git/git-tutorial.html**

# Git

## git配置

### 设置用户信息

```bash
git config --global user.name "username"
git config --global user.email xxx@example.com
```

### 设置密钥

```bash
# 1.生成SSH密钥, 一直Enter默认选项
ssh-keygen -t rsa -C "xxx@example.com" # 或者 ssh-keygen -t rsa

# 2.添加公钥到GitHub
cat ~/.ssh/id_rsa.pub
# 复制输出的内容, 然后去GitHub网页：
# 点右上角头像 --> Settings --> SSH and GPG keys --> 点「New SSH key」,Title随便填, Key粘贴进去, 保存

# 3.测试SSH是否连通
ssh -T git@github.com
```

SSH 连接时，**服务器** 会使用存储在它上的公钥（`id_rsa.pub`）来生成一个 **加密挑战**，然后你使用 **私钥**（`id_rsa`）来解密挑战并回应

| **文件名**   | **类型** | **用途**                                         | **是否公开** | **默认路径**        | **通常存储位置**       |
| ------------ | -------- | ------------------------------------------------ | ------------ | ------------------- | ---------------------- |
| `id_rsa`     | 私钥     | 用于本地身份验证，配合公钥解密服务器验证挑战     | ❌ 不可公开   | `~/.ssh/id_rsa`     | 本地（客户端）         |
| `id_rsa.pub` | 公钥     | 提供给服务器进行身份验证，授权连接或操作远程资源 | ✅ 可以公开   | `~/.ssh/id_rsa.pub` | 远程服务器、GitHub 等` |

## 工作区、暂存区和版本库

<img src="assets/git_command.jpg" alt="git-command" style="zoom: 100%; display: block; margin-left: auto; margin-right: auto;"/>

[**菜鸟教程：Git 工作区、暂存区和版本库**](https://www.runoob.com/git/git-workspace-index-repo.html)

[**菜鸟教程：Git 基本操作**](https://www.runoob.com/git/git-basic-operations.html)

## 获取和创建项目

### git init

```bash
git init    # 创建一个空的git仓库或重新初始化现有的git仓库
git clone   # 将仓库克隆到新目录
```

### git add

[git add .，git add -A，git add -u，git add * 的区别与联系 - 掘金 (juejin.cn)](https://juejin.cn/post/7053831273277554696)

将工作区的内容提交到暂存区

```bash
git add [file1] [file2] ...  # 将指定文件添加到暂存区
git add [dir] ...            # 将指定文件夹添加到暂存区
git add .                    # 将当前目录的所有文件添加到暂存区
```

### git status



### git commit

```bash
git commit -m [message]                      # 将暂存区内容添加到本地仓库中
git commit [file1] [file2] ... -m [message]  # 提交暂存区的指定文件到仓库区
git commit -a ?????????????????
```

## 共享和更新远程项目

### git remote

```bash
git remote [-v | --verbose]         # [-v | --verbose] 显示远程仓库的详细信息
git remote add <name> <URL>         # 为 <URL> 地址的远程仓库添加一个名为 <name> 的本地仓库，建立链接
git remote rename <old> <new>       # 将名为 <old> 的远程仓库重命名为 <new>
git remote remove <name>            # 删除名为 <name> 的远程仓库
git remote [-v | --verbose] show    # 显示所有远程仓库的信息
git remote [-v | --verbose] show [-n] <name>  # 显示名为 <name> 的远程仓库的信息
```

### git pull

将来自远程仓库的更改合并到当前本地分支中

```bash
git pull origin master
```

### git push

从本地仓库上传文件更新远程仓库

```bash
git push <远程主机名> <本地分支名>:<远程分支名>
git push origin master # 将本地的 master 分支推送到 origin 主机的 master 分支
```

### 总体流程举例

```bash
echo "# DenseORB_SLAM2" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:hejinxin0/DenseORB_SLAM2.git
git push -u origin main
```



## git分支管理和git标签

### git branch

官方文档：https://git-scm.com/docs/git-branch

```bash
git branch (-m | -M) [<oldbranch>] <newbranch>
git branch (-c | -C) [<oldbranch>] <newbranch>
git branch (-d | -D) [-r] <branchname>…       # 删除 git分支 ([-r]远程git分支)     
git branch (-r | --remotes)   # 查看远程 git 分支 ？？？？？？？？？？？？？？？
git branch --edit-description [<branchname>]
```

### git checkout

如何更新版本1.0，1.1，1.2 ？

branch和tags

-f强制切换分支？？

## git log

## git代理

[开启了代理，但是git仍然连接拒绝的解决方法_git设置代理不起作用-CSDN博客](https://wtl4it.blog.csdn.net/article/details/131743283?spm=1001.2101.3001.6661.1&utm_medium=distribute.pc_relevant_t0.none-task-blog-2~default~BlogCommendFromBaidu~PaidSort-1-131743283-blog-135921678.235^v43^pc_blog_bottom_relevance_base5&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-2~default~BlogCommendFromBaidu~PaidSort-1-131743283-blog-135921678.235^v43^pc_blog_bottom_relevance_base5&utm_relevant_index=1)
