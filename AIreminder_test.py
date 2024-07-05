'''
Author: lu 2231625449@qq.com
Date: 2024-05-11 11:18:37
LastEditors: lu 2231625449@qq.com
LastEditTime: 2024-07-03 21:58:53
FilePath: /AIdesign/AIreminder_test.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
# 创建基本的对话模型
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import datetime
import gradio as gr

def AIreminder(input_text):
    llm = ChatOpenAI(
                    api_key="sk-KlPk9mmRi2hrh4WWdW6V5Mlw84JuWOfsJeeExpTNT0xrbYde",
                    base_url="https://api.chatanywhere.tech/v1")

    # 使用提示模版进行prompt
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "你是一个智能备忘录。需要解析输入句子中的任务和对应的时间，返回一个结构化的数据格式，其中包含任务描述和确切时间。"),
        ("user", "{input_template}"),
        ("ai", "{output_template}"),
        ("system", "你需要根据上述内容和模版，根据现在的时间输出备忘录。无论输入语句有多短都要输出有效内容。现在的时间是 {now_time}。"),
        ("system", "记得备忘录每一项都要另起一行，并且不要有其他输出！"),
        ("user","{input}")
    ])
    # print(prompt.format(input="再过半小时我要去补办学生卡，然后明天下午我要去找 A 老师，星期三上午还要去看医生",output="[{‘补办学生卡’, (2024, 3, 4, 10, 32)}],{‘ 去 找 A 老 师 ’, (2024, 3, 5, 15, 0)},{‘去体检’, (2024, 3, 6, 8, 0)}]",now_time=datetime.datetime.now()))
    # 添加一个解析器，让聊天信息转换为字符串
    output_parser = StrOutputParser()
    # 把对话ai和提示模版进行结合，这样可以引导ai以提示模版的方式进行输出
    chain = prompt | llm | output_parser
    time = str(datetime.datetime.now())
    input_template = "今天再过半小时我要去补办学生卡，然后明天下午我要去找 A 老师，星期三上午还要去体检\n"
    # 智能备忘录
    output_template = "[{‘补办学生卡’, (2024, 3, 4, 10, 32)},\n {‘ 去 找 A 老 师 ’, (2024, 3, 5, 15, 0)},\n {‘去体检’, (2024, 3, 6, 8, 0)}]"
    # 智能工程管理
    # output_template = "```mermaid\ngantt\n    title 我的<br>项目\n    dateFormat  YYYY-MM-DD HH:mm\n    section 项目\n    补办学生卡 :des1, 2024-03-04 10:30, 2024-03-04 11:30\n    section 去找A老师 :des2, 2024-03-05 15:00, 2024-03-05 17:00\n    section 去体检 :des3, 2024-03-06 08:00, 2024-03-06 11:00\n```\n"
    # output_template += "| 任务       | 开始时间              | 结束时间              |\n| ---------- | ------------------- | ------------------- |\n| 补办学生卡 | 2024-03-04 10:30 | 2024-03-04 11:30 |\n| 去找A老师   | 2024-03-05 15:00 | 2024-03-05 17:00 |\n| 去体检       | 2024-03-06 08:00 | 2024-03-06 11:00 |"
    input = input_text
    output = chain.invoke({"input_template": input_template,"now_time":time,"output_template":output_template,"input":input})
    return output

def main():
    demo = gr.Interface(
        fn=AIreminder,
        inputs=["text"],
        outputs=["text"],
    )

    demo.launch()

if __name__ == '__main__':
    main()

# print(AIreminder("今天下午去五山，明天中午吃酸菜鱼，明天晚上开全员大会"))


# from langchain.prompts.example_selector import PromptTemplate, FewShotPromptTemplate
# # These are a lot of examples of a pretend task of creating antonyms.
# examples = [
#     {"input": "再过半小时我要去补办学生卡，然后明天下午我要去找 A 老师，星期三上午还要去", 
#      "output": "[{‘补办学生卡’, (2024, 3, 4, 10, 32)}],{‘ 去 找 A 老 师 ’, (2024, 3, 5, 15, 0)},{‘去体检’, (2024, 3, 6, 8, 0)}]"},
# ]

# example_formatter_template = """
# User: {input}
# AI: {output}\n
# """
# example_prompt = PromptTemplate(
#     input_variables=["word", "antonym"],
#     template=example_formatter_template,
# )