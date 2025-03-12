# DeepSeek_Desktop

#### 介绍

DeepSeek Desktop 是一个基于 PySide2 的桌面应用，用于快速访问 DeepSeek 的服务。
本软件基于 PySide2 构建，使用 PyInstaller 进行打包。
本软件是一个 Python 练习项目。
本软件是一个第三方项目，与 DeepSeek 官方服务无关，仅供学习参考。


#### 编译方法

##### 创建虚拟环境
```bash
python -m venv .venv
```
##### 安装依赖
```bash
pip install -r requirements.txt
```

##### 编译
```bash
pyinstaller --windowed --noconfirm --version-file=version_info.txt --icon=app/assets/favicon.ico --add-data 'app/assets;app/assets' --name "deepseek" main.py
```

