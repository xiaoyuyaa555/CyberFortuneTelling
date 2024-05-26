from find_lose import find_lose
from fortune_forecast import fortune_forecast
from weather_forecast import weather_forecast
from tkinter import Tk, Button, Label, Entry, END


# 定义模式切换函数
# 找失物的gui界面
def gui_find_lose_mode():
    # 更新各栏的文本描述
    date_label.config(text="现在的日期")
    time_label.config(text="现在的时间")
    result_label.config(text="寻物结果是")
    run_button.config(command=lambda: find_lose(in_date_entry=date_entry,
                                                in_time_entry=time_entry,
                                                in_name_print=name_print,
                                                in_result_print=result_print))
    # 每次切换模式都刷新输出栏
    clean_print()

# 测运势的gui界面
def gui_fortune_forecast_mode():
    # 更新各栏的文本描述
    date_label.config(text="现在的日期")
    time_label.config(text="现在的时间")
    result_label.config(text="运势结果是")
    run_button.config(command=lambda: fortune_forecast(in_date_entry=date_entry,
                                                       in_time_entry=time_entry,
                                                       in_name_print=name_print,
                                                       in_result_print=result_print))
    # 每次切换模式都刷新输出栏
    clean_print()

# 测天气的gui界面
def gui_weather_forecast_mode():
    # 更新各栏的文本描述
    date_label.config(text="今天的日期")
    time_label.config(text="今天的时间")
    result_label.config(text="天气结果是")
    run_button.config(command=lambda: weather_forecast(in_date_entry=date_entry,
                                                       in_time_entry=time_entry,
                                                       in_name_print=name_print,
                                                       in_result_print=result_print))
    # 每次切换模式都刷新输出栏
    clean_print()

# 刷新输出栏
def clean_print():
    result_print.delete(0, END)     # 刷新解卦栏
    name_print.delete(0, END)       # 刷新掌决栏


# GUI界面设计
root = Tk()
root.title("赛博算命")

# 各栏的行号
title_row = 0
model_change_row = 2
first_entry_row = 3
second_entry_row = 4
name_row = 5
print_row = 6
run_row = 7

# 宽度设置
entry_width = 30    # 所有输入、输出的框宽度
label_width = 10

# 添加title
title_label = Label(root, text="欢迎使用赛博算命！")
title_label.grid(row=title_row, columnspan=3)
Label(root).grid(row=1, column=0)

# 模式切换按钮
model_change_label = Label(root, text="模式切换",width=label_width)
model_change_label.grid(row=model_change_row, column=0)
Button(root, text="寻物", command=gui_find_lose_mode,width=10,borderwidth=1).grid(row=model_change_row, column=1, sticky="w")
Button(root, text="运势", command=gui_fortune_forecast_mode,width=10,borderwidth=1).grid(row=model_change_row, column=1, sticky="s")
Button(root, text="天气", command=gui_weather_forecast_mode,width=10,borderwidth=1).grid(row=model_change_row, column=1, sticky="e")

# 输入栏1
date_label = Label(root, text="现在的日期",width=label_width)
date_label.grid(row=first_entry_row, column=0)
date_entry = Entry(root, width=entry_width)  # 调整输入框宽度
date_entry.grid(row=first_entry_row, column=1)
date_entry.insert(0, '10.21')

# 输入栏2
time_label = Label(root, text="现在的时间",width=label_width)
time_label.grid(row=second_entry_row, column=0)
time_entry = Entry(root, width=entry_width)  # 调整输入框宽度
time_entry.grid(row=second_entry_row, column=1)
time_entry.insert(0, '11:14')

# 掌决栏
name_label = Label(root, text="掌决结果是",width=label_width)
name_label.grid(row=name_row, column=0)
name_print = Entry(root, width=entry_width)  # 调整输入框宽度
name_print.grid(row=name_row, column=1)

# 解卦栏
result_label = Label(root, text="寻物结果是",width=label_width)
result_label.grid(row=print_row, column=0)
result_print = Entry(root, width=entry_width)  # 调整输入框宽度
result_print.grid(row=print_row, column=1)

# 运行按钮
Label(root).grid(row=run_row, column=0)
run_button = Button(root, text="开始算卦", command=lambda: find_lose(date_entry, time_entry, name_print, result_print))
run_button.grid(row=run_row + 1, column=0, columnspan=2, sticky='s')

# 设置网格布局列居中
# root.grid_columnconfigure(0, weight=1)
# root.grid_columnconfigure(1, weight=1)

# 调整窗口大小
root.geometry("300x250")  # 设置窗口大小

root.mainloop()
