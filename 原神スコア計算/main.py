import sys
import tkinter
from PIL import Image, ImageTk, ImageGrab
import pyocr
import pyocr.builders
import re
import os
import tkinter as ttk
import tkinter.ttk as tk
#
# GUI設定
#
root = tkinter.Tk()
root.title(u"原神SCORE計算")
# root.resizable(width=False, height=False)

canvasX = 1280
canvasY = 720 + 70
root.geometry(str(canvasX) + "x" + str(canvasY))
canvas = tkinter.Canvas(root, width=canvasX, height=canvasY, bg="#1F1F23")

# キャンバスバインド
canvas.place(x=0, y=0)

# 最初の画像表示

# imgWitdh = getimg.width / 2 + 2
# imgHeight = getimg.height / 2 + 2
# canvas.create_image(imgWitdh, imgHeight, image=img, tag="icon")


# def displayImg(event):
#     value = combobox.get()
#     if value == "元素熟知" or value == "HP" or value == "防御力" or value == "攻撃力%" or value == "元素チャージ効率":
#         global decide_value
#         decide_value = combobox.get()
#         print(decide_value)
#     getimg = ImageGrab.grabclipboard().resize((1280, 720))
#     img = ImageTk.PhotoImage(getimg)
#     imgWitdh = getimg.width / 2 + 2
#     imgHeight = getimg.height / 2 + 2
#     canvas.create_image(imgWitdh, imgHeight, image=img, tag="icon")
#     reload()


# def deleteImg(event):
#     canvas.delete("icon")


def reload(event):
    value = combobox.get()
    if value == "元素熟知" or value == "HP%" or value == "防御力%" or value == "攻撃力%" or value == "元素チャージ効率%":
        global decide_value
        decide_value = combobox.get()
        print(decide_value)
    getimg = ImageGrab.grabclipboard().resize((1280, 720))
    img = ImageTk.PhotoImage(getimg)
    imgWitdh = getimg.width / 2 + 2
    imgHeight = getimg.height / 2 + 2
    canvas.create_image(imgWitdh, imgHeight, image=img, tag="icon")

    getimg_original = ImageGrab.grabclipboard()
    imgcut = getimg_original.crop((1355, 470, 1655, 630))

    #################################################################################################################
    #################################################################################################################
    #################################################################################################################

    # 1.インストール済みのTesseractのパスを通す
    path_tesseract = "C:\Program Files\Tesseract-OCR"
    if path_tesseract not in os.environ["PATH"].split(os.pathsep):
        os.environ["PATH"] += os.pathsep + path_tesseract

    # 2.OCRエンジンの取得
    tools = pyocr.get_available_tools()

    tool = tools[0]

    # 3.原稿画像の読み込み
    # img_org = Image.open("sscrop.png")

    # 4.ＯＣＲ実行
    builder = pyocr.builders.TextBuilder()
    # result = tool.image_to_string(img_org, lang="jpn", builder=builder)
    result = tool.image_to_string(imgcut, lang="jpn", builder=builder)
    result = re.split('\n', result)
    last_result = list(filter(None, result))

    option1 = last_result[0].split('+')
    option2 = last_result[1].split('+')
    option3 = last_result[2].split('+')
    option4 = last_result[3].split('+')

    print(option1 + option2 + option3 + option4)

    # option1 の処理
    offensive_power01 = 0  # 初期値設定
    critical_damage01 = 0  # 初期値設定
    affinity_rate01 = 0    # 初期値設定
    select_value01 = 0     # 初期値設定

    option_name = option1[0]
    option_value = option1[1]
    option_value = option_value[:-1]
    if option_name == "防御力" and option_value[-2:-1] == ".":
        if decide_value == "防御力%":
            select_value01 = float(option_value)
    elif option_name == "HP" and option_value[-2:-1] == ".":
        if decide_value == "HP%":
            select_value01 = float(option_value)
    elif option_name == "攻撃力" and option_value[-2:-1] == ".":
        if decide_value == "攻撃力%":
            select_value01 = float(option_value)
    elif option_name == "元素チャージ効率" and option_value[-2:-1] == ".":
        if decide_value == "元素チャージ効率%":
            select_value01 = float(option_value)
    elif option_name == "元素熟知":
        if decide_value == "元素熟知":
            select_value01 = float(option1[1]) * 0.25
    elif option_name == "会心率":
        affinity_rate01 = float(option_value) * 2
    elif option_name == "会心ダメージ":
        critical_damage01 = float(option_value)
    calc01 = offensive_power01 + critical_damage01 + affinity_rate01 + select_value01
    print(calc01)

    # option2 の処理
    offensive_power02 = 0  # 初期値設定
    critical_damage02 = 0  # 初期値設定
    affinity_rate02 = 0    # 初期値設定
    select_value02 = 0     # 初期値設定

    option_name = option2[0]
    option_value = option2[1]
    option_value = option_value[:-1]
    if option_name == "防御力" and option_value[-2:-1] == ".":
        if decide_value == "防御力%":
            select_value02 = float(option_value)
    elif option_name == "HP" and option_value[-2:-1] == ".":
        if decide_value == "HP%":
            select_value02 = float(option_value)
    elif option_name == "攻撃力" and option_value[-2:-1] == ".":
        if decide_value == "攻撃力%":
            select_value02 = float(option_value)
    elif option_name == "元素チャージ効率" and option_value[-2:-1] == ".":
        if decide_value == "元素チャージ効率%":
            select_value02 = float(option_value)
    elif option_name == "元素熟知":
        if decide_value == "元素熟知":
            select_value02 = float(option2[1]) * 0.25
    elif option_name == "会心率":
        affinity_rate02 = float(option_value) * 2
    elif option_name == "会心ダメージ":
        critical_damage02 = float(option_value)
    calc02 = offensive_power02 + critical_damage02 + affinity_rate02 + select_value02
    print(calc02)

    # option3 の処理
    offensive_power03 = 0  # 初期値設定
    critical_damage03 = 0  # 初期値設定
    affinity_rate03 = 0    # 初期値設定
    select_value03 = 0     # 初期値設定

    option_name = option3[0]
    option_value = option3[1]
    option_value = option_value[:-1]
    if option_name == "防御力" and option_value[-2:-1] == ".":
        if decide_value == "防御力%":
            select_value03 = float(option_value)
    elif option_name == "HP" and option_value[-2:-1] == ".":
        if decide_value == "HP%":
            select_value03 = float(option_value)
    elif option_name == "攻撃力" and option_value[-2:-1] == ".":
        if decide_value == "攻撃力%":
            select_value03 = float(option_value)
    elif option_name == "元素チャージ効率" and option_value[-2:-1] == ".":
        if decide_value == "元素チャージ効率%":
            select_value03 = float(option_value)
    elif option_name == "元素熟知":
        if decide_value == "元素熟知":
            select_value03 = float(option3[1]) * 0.25
    elif option_name == "会心率":
        affinity_rate03 = float(option_value) * 2
    elif option_name == "会心ダメージ":
        critical_damage03 = float(option_value)
    calc03 = offensive_power03 + critical_damage03 + affinity_rate03 + select_value03
    print(calc03)

    # option4 の処理
    offensive_power04 = 0  # 初期値設定
    critical_damage04 = 0  # 初期値設定
    affinity_rate04 = 0    # 初期値設定
    select_value04 = 0     # 初期値設定

    option_name = option4[0]
    option_value = option4[1]
    option_value = option_value[:-1]
    if option_name == "防御力" and option_value[-2:-1] == ".":
        if decide_value == "防御力%":
            select_value04 = float(option_value)
    elif option_name == "HP" and option_value[-2:-1] == ".":
        if decide_value == "HP%":
            select_value04 = float(option_value)
    elif option_name == "攻撃力" and option_value[-2:-1] == ".":
        if decide_value == "攻撃力%":
            select_value04 = float(option_value)
    elif option_name == "元素チャージ効率" and option_value[-2:-1] == ".":
        if decide_value == "元素チャージ効率%":
            select_value04 = float(option_value)
    elif option_name == "元素熟知":
        if decide_value == "元素熟知":
            select_value04 = float(option4[1]) * 0.25
    elif option_name == "会心率":
        affinity_rate04 = float(option_value) * 2
    elif option_name == "会心ダメージ":
        critical_damage04 = float(option_value)
    calc04 = offensive_power04 + critical_damage04 + affinity_rate04 + select_value04
    print(calc04)

    calc_all = calc01 + calc02 + calc03 + calc04
    print(calc_all)

    score = calc_all
    # option01 title
    score_option01 = tkinter.Label(text=option1[0], width=12, height=1)
    score_option01.place(x=300, y=720 + 14)
    # option02 title
    score_option02 = tkinter.Label(text=option2[0], width=12, height=1)
    score_option02.place(x=400, y=720 + 14)
    # option03 title
    score_option03 = tkinter.Label(text=option3[0], width=12, height=1)
    score_option03.place(x=500, y=720 + 14)
    # option04 title
    score_option04 = tkinter.Label(text=option4[0], width=12, height=1)
    score_option04.place(x=600, y=720 + 14)

    # option01
    score_option01 = tkinter.Label(text=calc01, width=12, height=1)
    score_option01.place(x=300, y=720 + 37)
    # option02
    score_option02 = tkinter.Label(text=calc02, width=12, height=1)
    score_option02.place(x=400, y=720 + 37)
    # option03
    score_option03 = tkinter.Label(text=calc03, width=12, height=1)
    score_option03.place(x=500, y=720 + 37)
    # option04
    score_option04 = tkinter.Label(text=calc04, width=12, height=1)
    score_option04.place(x=600, y=720 + 37)

    # score title
    score_option04 = tkinter.Label(
        text="合計", width=12, height=1, foreground='red')
    score_option04.place(x=700, y=720 + 14)
    # score
    score_display = tkinter.Label(
        text=score, width=12, height=1, foreground='red')
    score_display.place(x=700, y=720 + 37)

    score_displayfalse = tkinter.Label(text=score, width=10, height=1.1)
    score_displayfalse.place(x=700, y=720 + 23)
    #################################################################################################################
    #################################################################################################################
    #################################################################################################################


# 表示ボタン
# button_draw = ttk.Button(root, text=u"計算開始", width=10, default="normal")
# button_draw.bind("<Button-1>", displayImg)
# button_draw.place(x=20, y=720 + 20)

# 非表示ボタン
# button_draw = ttk.Button(root, text=u"画像非表示", width=10, default="normal")
# button_draw.bind("<Button-1>", deleteImg)
# button_draw.place(x=120, y=720 + 20)

# ただのラベル
lbl = tkinter.Label(text="スクショ画像")
lbl.place(x=0, y=0)

# 基準ステータスSelectBox


# def decide():
#     value = combobox.get()
#     if value == "元素熟知" or value == "HP" or value == "防御力" or value == "攻撃力%" or value == "元素チャージ効率":
#         global decide_value
#         decide_value = combobox.get()
#         print(decide_value)


opnamelist = ("元素熟知", "HP%", "防御力%", "攻撃力%", "元素チャージ効率%")
combobox = tk.Combobox(root, values=opnamelist, width=20, height=5)
combobox.place(x=800, y=720 + 22)
decidebutton = ttk.Button(root, text=u"計算する", default="normal")
decidebutton.bind("<Button-1>", reload)
decidebutton.place(x=950, y=720 + 20)
root.mainloop()


# HP
# 攻撃力
# 防御
# チャージ
# 元素熟知

# if option_name == "攻撃力" or option_name == "会心率" or option_name == "会心ダメージ" or option_name == decide_value:
