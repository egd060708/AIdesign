'''
Author: lu 2231625449@qq.com
Date: 2024-05-13 10:45:33
LastEditors: lu 2231625449@qq.com
LastEditTime: 2024-05-13 10:52:18
FilePath: /AIdesign/localUI.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
import AIreminder_test as re

import tkinter as tk

extracted_text = ""

def submit_schedule():
    # 获取输入文本
    global extracted_text
    input_text = input_textbox.get("1.0", tk.END)
    # 这里可以加入处理输入文本并生成备忘录内容的逻辑
    output_text = re.AIreminder(input_text)  # 假设输出文本暂时与输入文本相同
    output_textbox.delete("1.0", tk.END)  # 清空输出文本框
    output_textbox.insert(tk.END, output_text)  # 显示处理后的备忘录内容
    # 获取处理后的输出文本并执行额外的逻辑
    extracted_text = output_textbox.get("1.0", tk.END).strip()
    print("提取的备忘录内容:\n", extracted_text)
    
    with open('output.md', 'w', encoding='utf-8') as file:
        file.write(extracted_text)
    

# 创建主窗口
root = tk.Tk()
root.title("智能备忘录")

# 设置窗口大小
root.geometry("500x400")

# 创建输入文本框，用于输入日程描述
input_textbox = tk.Text(root, height=10)
input_textbox.pack(pady=10, fill='both', expand=True)

# 创建提交按钮
submit_button = tk.Button(root, text="提交", command=submit_schedule)
submit_button.pack(pady=5)

# 创建输出文本框，用于显示备忘录内容
output_textbox = tk.Text(root, height=10)
output_textbox.pack(pady=10, fill='both', expand=True)

# 启动事件循环
root.mainloop()
