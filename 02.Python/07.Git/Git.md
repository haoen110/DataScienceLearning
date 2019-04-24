
# Git 代码协同管理工具
- 代码管理工具作用
    * 防止代码丢失，做备份
    * 代码版本的管理，可以进行多个节点的备份，在多个版本之间跳跃
    * 可以方便的将代码在多人之间进行共享传输
    * 多人开发时有各种模式可以方便代码管理

### 分布式和集中式
- git是一个开源的分布式版本控制系统，可用于高效的管理大小项目。
    - 分布式(git)：每个节点都保存完成的代码，没有明确的中央服务器，节点之间项目推送下载代码完成代码共享
    - 集中式(svn)：代码集中管理，每次完成的代码上传到中央管理器，然后再统一从中央管理器下载代码使用

>### 工作区 -> 暂存区 -> 本地仓库 <-> 远程仓库

### Git特点
* git可以管理各种文件，特别是代码项目，多在*nix系统中使用
* 是分布式管理，不同于集中式，这是git和svn的核心区别
* git可以更好的支持分支，方便多人协同工作
* git分布式代码更安全，有全球唯一的commit版本号
* git是开源的系统
* 使用git可以脱网工作，且数据传输速度较快

### Git安装

    linux : 
    sudo apt-get install git

    windows : msysgit.github.io

    git  配置命令
    git config

### 配置级别  
1. 系统中所有的用户都可使用该配置
    - 命令：`git config  --system`   
    - 配置文件：`/etc/gitconfig`
2. 当前用户可使用该配置
    - 命令：`git config  --global`
    - 配置文件：`~/.gitconfig`
3. 当前项目可使用该配置
    - 命令：`git config`
    - 配置文件：`project/.git/config`

### 配置内容：
1. 配置用户名
   - 配置用户名为haoen110
   - `sudo git config --system user.name haoen110`
2. 配置用户邮箱
   - 配置邮箱
   - `git config --global user.email haoenwei@outlook.com`
3. 配置编译器
   - 配置编译器
   - `git config core.editor sublime`
4. 查看配置信息
   - `git config --list`

# Git基本命令

### 初始化仓库
- `git init` 
    - 在某个目录下初始化仓库后会自动产生.git目录，该目录下工作的所有文档即可以使用git进行管理

### 查看分支状态
- `git status`
    -  默认工作分支为master，可通过创建新的分支切换

### 文件提交和删除
- `git add [file]`
    - 将文件提交到**暂存区**
    - 提交内容可以是一个文件，多个文件用个空格分开
    - 如果是 * 表示所有文件，也可以是目录
- `git add .`
    - 监控工作区的状态树，使用它会把工作时的所有变化提交到暂存区，包括文件内容修改(modified)以及新文件(new)，但不包括被删除的文件。
- `git add -u`
    - 仅监控已经被add的文件（即tracked file），他会将被修改的文件提交到暂存区，add -u不会提交新文件（untracked file）--update的缩写）
- `git add -A`
    - 是上面两个功能的合集（git add --all的缩写）
- `git rm --cached Readme.txt`   
    - 删除暂存区某个文件提交记录
   
### 同步到本地仓库
- `git commit -m "some message"`
   - 同步时需要附加一些同步信息，在-m后添加
   - 所有对工作区的修改如果想同步到本地仓库，都需要add--->commit
   - `git commit -ma "some message"` == `git add .` + `git commit -m "some message"`

### 查看commit日志
    git log
    git log  --pretty=oneline

### 一些工作区命令
- `git diff file`
    - 查看本地文件和工作区差异
- `git checkout file`    
    - 从本地仓库恢复文件
- `git checkout -- file`    
    - 丢弃工作区修改
    
### 本地仓库文件的移动和删除
- `git mv file dir`
    - 移动文件
- `git rm file`     
    - 删除文件
* 用法和mv rm命令相同。操作后直接commit即可工作区和本地仓库同步

### 版本控制命令
- `git reset --hard HEAD^`
    - 回到之前版本
    - HEAD后的^数量决定了回到上几个版本
- `git reset --hard commit_id`
    - 使用commit前7位即可，回到指定的版本
- `git  reflog`
    - 查看所有历史版本号
    - 然后再用使用git reset去往指定版本
    - git reflog 会有所有的操作记录，最新的操作时钟在最上边
    
### 标签管理
- 即在当前工作位置添加快照，保存工作状态，一般用于版本的迭代。
- `git tag v1.0`
    - 默认在最新的commit_id处打标签
- `git  tag v1.0  -m  "message"`    
    - 添加标签信息
- `git tag v0.9 [commit_id]`    
    - 指定某个commit_id打标签
- `git tag`    
    - 查看标签
- `git show v1.0`
    - 显示标签具体信息
- `git tag -d v1.0`
    - 删除标签
- `git reset --hard v0.9`    
    - 去往某个标签版本

### 临时工作区操作
- `git stash`
    - 创建保存临时工作区
- `git stash list`   
    - 查看保存的工作区
- `git stash apply stash@{1}`
    - 应用哪个工作区
- `git stash pop`   
    - 应用上一个工作区并且删除
- `git stash drop stash@{0}`   
    - 删除某一个工作区
- `git stash clear`
    - 删除所有工作区

# 分支操作
- 概念
    - 分支即每个人获取原有代码，在此基础上创建自己的工作环境，单独开发，不会影响其他分支的操作。开发完成后再统一合并到主线分支中。
- 优点
    - 安全，不影响其他人工作，自己控制进度
---
- `git branch`
    - 查看当前分支
    - 前面有 * 号的分支表示当前正在工作的分支
- `git branch [branch_name]`
    - 创建分支
- `git checkout [branch]`    
    - 切换工作分支
- `git checkout -b [branch_name]`    
    - 创建并切换到新的分支
- `git merge [branch]`    
    - 将某个分支合并到当前分支
- `git branch -d [branch_name]`    
    - 删除分支
- `git branch -D [branch_name]`
    - 强制删除没有合并的分支
---
* 合并过程中如果没有冲突则直接合并后当前分支即为**干净**的状态
* 如果产生冲突则需要人为选择然后在进行add,commit等操作
* 在创建分支前尽量保证当前分支是干净点，以减少冲突的发生

# 远程仓库
- 概念
    - 远程主机上的仓库。实际上git是分布式的，每一台主机的git结构都相似，只是把其他主机的git仓库叫做远程而已

### 创建共享仓库
1. 创建文件夹
   - `mkdir gitrepo`
2. 设置文件夹属主
   - `chown haoen110:haoen110 gitrepo`
3. 将该文件夹设置为可共享的git仓库，设置名字
   - `git init --bare fly.git`
4. 设置本地仓库属组
   - `chown -R haoen110:haoen110 fly.git`

### 添加远程仓库
- `git remote add origin haoen110@127.0.0.1:/gitrepo/fly.git`
    - 默认使用SSH作为传输手段
    - 必须在本地的某个git仓库下执行才能使本地仓库和远程仓库关联
- `git remote rm [origin]`
    - 删除远程主机
- `git push -u origin master`
    - 将本地分支推送到远程
    - 在第一次向远程仓库推送时需要加 -u选项，以后就不需要了
- `git clone tarena@127.0.0.1:/gitrepo/fly.git`
    - 从远程仓库获取项目
- `git pull origin dev_Tom` 
    - 直接拉取远程分支和当前工作分支合并
- `git pull origin dev_Tom:dev_Tom`
    - 拉取远程分支到本地，不合并，远程分支:本地分支名
- `git push`
    - 将本地代码推送到连接的远程仓库
- `git push --force origin`
    - 当本地版本比远程版本旧时用本地旧版本覆盖远程新版本
- `git fetch`
    - 如果有新的分支拉取到本地不会和本地分支合并

# GitHub
- 概念
    - GitHub是一个开源项目社区网站。拥有全球最多的开源项目。开发者可以注册这个网站建立自己的GitHub仓库。然后就可以在本地通过git像操作远程仓库一样操作GitHub仓库。
- git是GitHub唯一指定的代码管理工具
- 网址：https://github.com/
---
- 添加ssh秘钥
    1. 在本地主机生成ssh密钥对`ssh-keygen`
        * 默认密钥对存放在 ~/.ssh/ 下
        * 生成过程会提示设置密码，如果直接回车则表示不设置密码
    2. 进入 ~/.ssh 目录，复制id_rsa.pub公钥内容
    3. 登录github账号  
        - settings --> SSH and GPG keys --> new ssh key --> add
---
- 创建新的GitHub仓库
- 操作github仓库
    1. `git remote`连接远程GitHub仓库 如果需要输入密码输入github密码即可
    2. 使用`git push`等操作远程仓库的方法操作即可
