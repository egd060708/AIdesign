## 智能备忘录prompt工程

部署需要安装

调用大模型api以及prompt工程的langChain

openai

简单的可视化界面gradio

```shell
pip install langchain
pip install openai
pip install gradio
```

运行demo之前需要先改一下proxy

在终端分别输入

```shell
export ALL_PROXY=''
export all_proxy=''
```

在准备完成后运行以下demo，如果有报错没依赖的，就安装相关库

```shell
python AIreminder_test.py
```

![](/home/lu/Git_Project/github/AIdesign/cache/2024-05-11_12-27.png)

成功运行过后复制输出的网络端口在浏览器打开

即可得到ui界面并且测试智能备忘录

输入要生成备忘录的语句，点击submit即可输出相应备忘录

![](/home/lu/Git_Project/github/AIdesign/cache/2024-05-11_12-26.png)

