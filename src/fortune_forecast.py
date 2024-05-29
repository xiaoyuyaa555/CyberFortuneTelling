from base_function import *
from result_lib import result_of_fortune


def fortune_forecast(in_date_entry, in_time_entry, in_name_print, in_result_print):
    if chick_input(in_date_entry, in_time_entry) == 'form error':  # 格式出错
        in_result_print.delete(0, END)
        return

    # 获取输入框输入
    date, time = get_input(in_date_entry, in_time_entry)
    # print(date, time)

    # 根据输入得到三个数字
    first_num, second_num = solar_to_lunar(date)
    third_num = time_to_serial_number_of_zodiac(time)
    # print(first_num, second_num, third_num)

    # 根据数字得到结果
    fortune_forecast_imp(first_num, second_num, third_num, in_result_print, in_name_print)


def fortune_forecast_imp(first_num, second_num, third_num, result_print, name_print):
    # 根据数字得到三个掌决
    first_name, second_name, third_name = get_name(first_num, second_num, third_num)
    # print(first_index, first_name, second_index, second_name, third_index, third_name)

    # 根据掌决获得结果
    result = get_result(second_name, third_name, result_dirt=result_of_fortune)

    # 在输出框输出对应信息
    print_name(first_name, second_name, third_name, name_print)  # 输出掌决结果
    print_result(result_print, result)  # 输出解卦结果

    return
