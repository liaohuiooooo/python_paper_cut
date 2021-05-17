[TOC]

# git相关

## 远程仓库地址修改后，本地仓库该如何更新？

| https://blog.csdn.net/asdfsfsdgdfgh/article/details/54981823


### 直接修改远程地址
- git remote 查看所有远程仓库
- giit remote set-url origin [新仓库地址]

### 先删除远程地址，再添加远程仓库
- git remote rm origin
- git remote add origin [新仓库地址]

