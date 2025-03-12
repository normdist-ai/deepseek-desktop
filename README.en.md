# DeepSeek_Desktop

#### Introduction

DeepSeek Desktop is a desktop application based on PySide2 for quick access to DeepSeek's services.
This software is built based on PySide2 and packaged with PyInstaller.
This software is a Python practice project.
This software is a third-party project and has nothing to do with DeepSeek official services, it is only for learning and reference.

![ScreenShot](https://raw.githubusercontent.com/normdist-ai/deepseek-desktop/refs/heads/main/screenshot.png)

#### Download

[https://github.com/normdist-ai/deepseek-desktop/releases/download/DeepSeek/deepseek-desktop-1.0.1.sfx.exe](https://github.com/normdist-ai/deepseek-desktop/releases/download/DeepSeek/deepseek-desktop-1.0.1.sfx.exe)


#### Building Method

##### Create Virtual Environment
```bash
python -m venv .venv
```
##### Install Dependencies
```bash
pip install -r requirements.txt
```

##### Compile
```bash
pyinstaller --windowed --noconfirm --version-file=version_info.txt --icon=app/assets/favicon.ico --add-data 'app/assets;app/assets' --name "deepseek" main.py
```