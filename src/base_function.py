from tkinter import END
from result_lib import name_list


def chick_input(date_entry, time_entry):
    import re

    date_form_error = True
    time_form_error = True

    date_regex = r'^\d{1,2}\.\d{1,2}$'  # 日期格式，包含两个数字和一个.号
    time_regex = r'^\d{1,2}:\d{1,2}$'  # 时间格式，包含两个数字和一个:号
    date = date_entry.get()
    # print(type(date))
    if re.match(date_regex, date) is None:  # 日期格式错误
        date_entry.delete(0, END)
        date_entry.insert(0, '请输入如 10.10 的格式')
    else:
        date_form_error = False

    time = time_entry.get()
    if re.match(time_regex, time) is None:  # 时间格式错误
        time_entry.delete(0, END)
        time_entry.insert(0, '请输入如 13:14 的格式')
    else:
        time_form_error = False

    if date_form_error or time_form_error:
        return 'form error'
    return 'form true'


# 获得输入信息
def get_input(date_entry, time_entry):
    return date_entry.get().split('.'), time_entry.get().split(':')


# 将日期转为农历日期
def solar_to_lunar(date):
    from lunarcalendar import Converter, Solar
    from datetime import datetime

    # 获取年月日
    current_year = datetime.now().year
    current_month = int(date[0])
    current_date = int(date[1])

    # 公历日期
    solar_date = Solar(current_year, current_month, current_date)

    # 转换为农历日期
    lunar_date = Converter.Solar2Lunar(solar_date)

    return lunar_date.month, lunar_date.day


# 将时间转换成对应的时辰的序号
def time_to_serial_number_of_zodiac(time):
    time = int(time[0])
    if time == 0 or time == 23:
        period_index = 1
    else:
        period_index = int((time + 1) * 60 // 120) + 1

    return period_index


# 根据数字获得对应掌决
def get_name(first_num, second_num, third_num):
    first_index = (first_num - 1) % 6
    first_name = name_list[first_index]     # 第一个掌决

    second_index = (first_index + second_num - 1) % 6
    second_name = name_list[second_index]   # 第二个掌决

    third_index = (second_index + third_num - 1) % 6
    third_name = name_list[third_index]     # 第三个掌决
    return first_name, second_name, third_name


# 在result_dirt字典中找到对应结果
def get_result(second_name, third_name, result_dirt):
    index = (second_name, third_name)
    result = result_dirt[index]
    return result


# 输出掌决结果
def print_name(first_name, second_name, third_name, name_print):
    name_print.delete(0, END)
    name_print.insert(0, first_name + '->' + second_name + '->' + third_name)


# 输出寻物结果
def print_result(result_print, result):
    result_print.delete(0, END)
    result_print.insert(0, result)
