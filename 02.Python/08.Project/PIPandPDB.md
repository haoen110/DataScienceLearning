# PIP
- 作用：管理Python的标准第三方库中第三方软件包
- 安装：`sudo apt-get install python3-pip`
- 常用命令：
    - 安装软件：`pip3 install [name]`
    - 查看当前包：`pip3 list`
    - 搜索某个名字的包：`pip search [name]`
    - 查看软件包信息：`pip show [name]`
    - 升级软件包：`pip install --upgrade [name]`
    - 卸载软件包：`pip uninstall [name]`
    - 导出软件包环境：`pip freeze > requirments.txt`
    - 根据文档自动安装：`pip install -r requirments.txt`

# PDB调试方法
`import pdb`
- 功能：断点设置、单步执行、查看代码、查看函数、追踪变量
- 命令：
    - 设置断点：`b break`
    - 继续执行：`c continue`
    - 单步执行：`n next`
    - 单步执行，可以进入函数内部：`s step`
    - 查看代码段：`l list`
    - 查看某个变量值：`pp`
    - 帮助：`help`
- 方法：
    - 在代码中加入：`pdb.set_trace()`
    - 在运行程序时：`python -m pdb debug.py`
    
    
    
