from nicegui import ui
import speech_recognition as sr
from gtts import gTTS
import pandas as pd
import plotly.figure_factory as ff
import os

recognizer = sr.Recognizer()

# 获取桌面路径
# desktop_path = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
desktop_path = '/home/lu/Git_Project/github/AIdesign/audio_assets'
file_path = os.path.join(desktop_path, '1.mp3')



def speech_to_text():
    with sr.Microphone() as source:
        ui.notify("正在聆听...")
        audio_data = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio_data, language='zh-CN')
            ui.notify(f"识别的文字: {text}")
            output_text.set_value(text)
        except sr.UnknownValueError:
            ui.notify("无法识别音频")
        except sr.RequestError as e:
            ui.notify(f"请求识别结果失败: {e}")


def text_to_speech(text, voice_model):
    language_map = {
        '小新': 'zh-CN',
        '小芳': 'zh-TW',
        '小明': 'zh'
    }
    lang = language_map.get(voice_model, 'zh-CN')
    tts = gTTS(text=text, lang=lang)

    # 保存语音文件到桌面并命名为1.mp3
    tts.save(file_path)
    # audio_player.set_source(f'/static/{os.path.basename(file_path)}')
    audio_player.set_source('C:/Users/ts/Desktop/1.mp3')
    audio_player.visible = True
    ui.notify(f"语音文件已保存到: {file_path}")


# 添加全局样式
ui.add_head_html(
    '<style>body { font-family: Arial, sans-serif; background-color: #f5f5f5; } .card { max-width: 1000px; margin: 20px auto; padding: 20px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); } .btn { width: 100%; margin-top: 10px; } .card1 { max-width: 3000px; margin: 20px auto; padding: 20px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }</style>')

with ui.grid(columns=2):
# with ui.element('div').style('margin-top: 50px;'):
    with ui.card().classes('card'):
        ui.markdown("## 语音转文字")
        ui.button("开始聆听", on_click=speech_to_text).classes('btn')
        output_text = ui.textarea(label="输出文字").style('width: 100%;')

    with ui.card().classes('card'):
        ui.markdown("## 文字转语音")
        input_text = ui.input(label="输入文字").style('width: 100%; margin-bottom: 10px;')
        voice_model = ui.select(['丁真', '黑天鹅', '流萤','自己'], label='选择语音模型').style(
            'width: 100%; margin-bottom: 10px;')
        ui.button("转换为语音", on_click=lambda: text_to_speech(input_text.value, voice_model.value)).classes('btn')
        audio_player = ui.audio(src='').style('width: 100%; margin-top: 10px;').classes('audio_player')
with ui.element('div').style('margin-right: 1000px;'):
    with ui.card():
        ui.markdown("## 甘特图")
        content = """
            gantt
        title 无人机项目时间管理
        dateFormat  YYYY-MM-DD
        section 项目启动
        项目规划         :done,    p1, 2024-01-01, 2024-01-07
        团队组建         :done,    p2, 2024-01-08, 2024-01-14
        section 研发阶段
        设计             :active,  d1, 2024-01-15, 2024-02-12
        原型制造         :         d2, after d1, 20d
        软件开发         :         d3, after d1, 30d
        section 测试阶段
        功能测试         :         t1, after d2, 15d
        性能测试         :         t2, after t1, 15d
        section 生产阶段
        量产准备         :         pd1, after t2, 10d
        section 市场推广
        市场营销         :         m1, after pd1, 20d
        销售             :         m2, after m1, 30d
            """
        ui.mermaid(content)
    ui.chat_message('Hello NiceGUI!',
                    name='Robot',
                    stamp='now',
                    avatar='https://robohash.org/ui')



# 为静态文件提供服务
@ui.page('/static/<file_name>')
def serve_static_file(file_name):
    return ui.send_file(os.path.join(desktop_path, file_name))



ui.run()
