'''
Author: lu 2231625449@qq.com
Date: 2024-05-11 11:18:37
LastEditors: lu 2231625449@qq.com
LastEditTime: 2024-05-13 11:01:07
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
        ("system", "记得备忘录每一项都要另起一行！"),
        ("user","{input}")
    ])
    # print(prompt.format(input="再过半小时我要去补办学生卡，然后明天下午我要去找 A 老师，星期三上午还要去看医生",output="[{‘补办学生卡’, (2024, 3, 4, 10, 32)}],{‘ 去 找 A 老 师 ’, (2024, 3, 5, 15, 0)},{‘去体检’, (2024, 3, 6, 8, 0)}]",now_time=datetime.datetime.now()))
    # 添加一个解析器，让聊天信息转换为字符串
    output_parser = StrOutputParser()
    # 把对话ai和提示模版进行结合，这样可以引导ai以提示模版的方式进行输出
    chain = prompt | llm | output_parser
    time = str(datetime.datetime.now())
    input_template = "今天再过半小时我要去补办学生卡，然后明天下午我要去找 A 老师，星期三上午还要去体检\n"
    # input_template = "项目名称：自动化辅助机器人开发\n时间线与活动安排（增强并行任务）\n项目启动与团队建设\n\n日期：2023年6月1日\n内容：项目启动会议，明确项目目标、团队职责、初步时间表。同时组建各子团队。\n参与者：项目经理、各子团队负责人、关键技术人员。\n需求分析与市场调研（完全并行任务）\n\n需求分析\n开始日期：2023年6月2日\n结束日期：2023年6月15日\n市场调研\n开始日期：2023年6月2日\n结束日期：2023年6月15日\n设计与原型开发（增强并行多任务）\n\n硬件设计\n开始日期：2023年6月16日\n结束日期：2023年7月15日\n软件开发\n开始日期：2023年6月16日\n结束日期：2023年7月15日\n用户界面设计\n开始日期：2023年6月16日\n结束日期：2023年7月15日\n初步原型制作\n开始日期：2023年7月16日\n结束日期：2023年7月31日\n综合测试与优化（完全并行多任务）\n\n原型测试\n开始日期：2023年8月1日\n结束日期：2023年8月20日\n设计优化\n开始日期：2023年8月1日\n结束日期：2023年8月20日\n第二版原型开发\n开始日期：2023年8月21日\n结束日期：2023年8月31日\n产品完善与市场准备（完全并行多任务）\n\n最终测试与调整\n开始日期：2023年9月1日\n结束日期：2023年9月15日\n市场与销售策略制定\n开始日期：2023年9月1日\n结束日期：2023年9月15日\n生产准备\n开始日期：2023年9月16日\n结束日期：2023年9月30日\n产品发布与后续支持\n\n日期：2023年10月1日起\n内容：正式发布产品，开展市场推广活动，提供技术支持和客户服务。\n参与者：销售团队、市场团队、客户服务部门。"
    # output_template = "[{‘补办学生卡’, (2024, 3, 4, 10, 32)},\n {‘ 去 找 A 老 师 ’, (2024, 3, 5, 15, 0)},\n {‘去体检’, (2024, 3, 6, 8, 0)}]"
    output_template = "```mermaid\ngantt\n    title 我的<br>项目\n    dateFormat  YYYY-MM-DD HH:mm\n    section 项目\n    补办学生卡 :des1, 2024-03-04 10:30, 2024-03-04 11:30\n    section 去找A老师 :des2, 2024-03-05 15:00, 2024-03-05 17:00\n    section 去体检 :des3, 2024-03-06 08:00, 2024-03-06 11:00\n```\n"
    # output_template = "```\ngantt\n    title 自动化辅助机器人开发项目时间线\n    dateFormat YYYY-MM-DD\n    axisFormat %m/%d\n\n    section 项目启动与团队建设\n    项目启动会议 :milestone, 2023-06-01, 1d\n\n    section 需求分析与市场调研\n    需求分析 :2023-06-02, 2023-06-15\n    市场调研 :2023-06-02, 2023-06-15\n\n    section 设计与原型开发\n    硬件设计 :2023-06-16, 2023-07-15\n    软件开发 :2023-06-16, 2023-07-15\n    用户界面设计 :2023-06-16, 2023-07-15\n    初步原型制作 :2023-07-16, 2023-07-31\n\n    section 综合测试与优化\n    原型测试 :2023-08-01, 2023-08-20\n    设计优化 :2023-08-01, 2023-08-20\n    第二版原型开发 :2023-08-21, 2023-08-31\n\n    section 产品完善与市场准备\n    最终测试与调整 :2023-09-01, 2023-09-15\n    市场与销售策略制定 :2023-09-01, 2023-09-15\n    生产准备 :2023-09-16, 2023-09-30\n\n    section 产品发布与后续支持\n    产品发布 :milestone, 2023-10-01, 1d\n```\n"
    output_template += "| 任务       | 开始时间              | 结束时间              |\n| ---------- | ------------------- | ------------------- |\n| 补办学生卡 | 2024-03-04 10:30 | 2024-03-04 11:30 |\n| 去找A老师   | 2024-03-05 15:00 | 2024-03-05 17:00 |\n| 去体检       | 2024-03-06 08:00 | 2024-03-06 11:00 |"
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