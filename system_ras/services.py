from datetime import datetime

from asgiref.sync import sync_to_async
from .models import *
from .serializers import *
import json
from django.conf import settings
import openpyxl
from openpyxl.styles import Font
from collections import defaultdict

from operator import itemgetter


def calculate_result(koef1, koef2, value):
    return koef1 + (((koef2 - koef1) / 1000) * abs(value))


def get_data_block(data):
    va_params = []
    vd_params = []
    block = json.loads(data.GET['params'])[0][:7]
    for param in json.loads(data.GET['params']):
        if param[8:][:2] == "VA":
            va_params.append(param[8:])
        else:
            vd_params.append(param[8:])
    if block == "block_1":
        va_signals = L110KvaB1.objects.filter(timepoint__gte=data.GET['date_time_start'],
                                              timepoint__lte=data.GET['date_time_finish'])
        vd_signals_start = L110KvdB1.objects.get(timepoint=data.GET['date_time_start'])
        vd_signals = B1SigstateChange.objects.filter(timepoint__gte=data.GET['date_time_start'],
                                                     timepoint__lte=data.GET['date_time_finish'],
                                                     sig_name__in=vd_params)
        if datetime.strptime(data.GET['date_time_finish'], "%Y-%m-%dT%H:%M") > datetime.now():
            vd_signals_finish = L110KvdB1.objects.last()
        else:
            vd_signals_finish = L110KvdB1.objects.get(timepoint=data.GET['date_time_finish'])

    elif block == "block_2":
        va_signals = L110KvaB2.objects.filter(timepoint__gte=data.GET['date_time_start'],
                                              timepoint__lte=data.GET['date_time_finish'])
        vd_signals_start = L110KvdB2.objects.get(timepoint=data.GET['date_time_start'])
        vd_signals = B2SigstateChange.objects.filter(timepoint__gte=data.GET['date_time_start'],
                                                     timepoint__lte=data.GET['date_time_finish'],
                                                     sig_name__in=vd_params)
        if datetime.strptime(data.GET['date_time_finish'], "%Y-%m-%dT%H:%M") > datetime.now():
            vd_signals_finish = L110KvdB2.objects.last()
        else:
            vd_signals_finish = L110KvdB2.objects.get(timepoint=data.GET['date_time_finish'])
    else:
        va_signals = L110KvaB3.objects.filter(timepoint__gte=data.GET['date_time_start'],
                                              timepoint__lte=data.GET['date_time_finish'])
        vd_signals_start = L110KvdB3.objects.get(timepoint=data.GET['date_time_start'])
        vd_signals = B3SigstateChange.objects.filter(timepoint__gte=data.GET['date_time_start'],
                                                     timepoint__lte=data.GET['date_time_finish'],
                                                     sig_name__in=vd_params)
        if datetime.strptime(data.GET['date_time_finish'], "%Y-%m-%dT%H:%M") > datetime.now():
            vd_signals_finish = L110KvdB3.objects.last()
        else:
            vd_signals_finish = L110KvdB3.objects.get(timepoint=data.GET['date_time_finish'])
    block_num = 1 if block == "block_1" else 2 if block == "block_2" else 3
    return va_signals, vd_signals_start, vd_signals, block_num, va_params, vd_params, vd_signals_finish


def create_title_va(block_num, va_params):
    str = ""
    if va_params != []:
        str = """АНАЛОГОВЫЕ СИГНАЛЫ
================================================
Дата/Время\t"""
        for va_param in va_params:
            str += f"{getattr(settings, f'DATA_BLOCK_{block_num}')['VA_SIGNALS'][f'{va_param}']['name']}\t"
    return str


def create_data_va(block_num, va_signals, va_params):
    str = ''
    if va_params != []:
        for va_signal in va_signals:
            str += f"{va_signal.timepoint.strftime('%d.%m.%Y %H:%M:%S')}\t"
            for va_param in va_params:
                str += f"{calculate_result(getattr(settings, f'DATA_BLOCK_{block_num}')['VA_SIGNALS'][f'{va_param}']['Koef_1'], getattr(settings, f'DATA_BLOCK_{block_num}')['VA_SIGNALS'][f'{va_param}']['Koef_2'], getattr(va_signal, va_param.lower())):.2f}\t"
            str += '\n'
    return str


def create_title_vd(block_num, vd_params, vd_signals_start):
    str = ""
    if vd_params != []:
        str = """ДИСКРЕТНЫЕ СИГНАЛЫ
Дата/Время	Наименование	Значение
================================================
**************ИСХОДНЫЕ**************\n"""
        for vd_param in vd_params:
            str += f"{vd_signals_start.timepoint.strftime('%d.%m.%Y')}\t{getattr(settings, f'DATA_BLOCK_{block_num}')['VD_SIGNALS'][f'{vd_param}']['name']}\t{getattr(vd_signals_start, vd_param.lower())}\n"
        str += '************************************'
    return str


def create_data_vd(block_num, vd_params, vd_signals):
    str = ""
    if vd_params != []:
        for vd_signal in vd_signals:
            str += f"{vd_signal.timepoint.strftime('%d.%m.%Y %H:%M:%S')}\t{getattr(settings, f'DATA_BLOCK_{block_num}')['VD_SIGNALS'][f'{vd_signal.sig_name.strip()}']['name']}\t{vd_signal.sig_state}\n"
    return str


@sync_to_async
def get_data_ras():
    va_b1 = L110KvaB1.objects.last()
    va_b2 = L110KvaB2.objects.last()
    va_b3 = L110KvaB3.objects.last()
    vd_b1 = L110KvdB1.objects.last()
    vd_b2 = L110KvdB2.objects.last()
    vd_b3 = L110KvdB3.objects.last()

    va_signals_b1 = {
        name_va: calculate_result(
            signal_va['Koef_1'],
            signal_va['Koef_2'],
            getattr(va_b1, name_va.lower())
        )
        for name_va, signal_va in settings.DATA_BLOCK_1['VA_SIGNALS'].items()
    }

    vd_signals_b1 = {
        name_vd: "ДА" if getattr(vd_b1, name_vd.lower()) == 1 else "НЕТ"
        for name_vd, signal_vd in settings.DATA_BLOCK_1['VD_SIGNALS'].items()
    }

    va_signals_b2 = {
        name_va: calculate_result(
            signal_va['Koef_1'],
            signal_va['Koef_2'],
            getattr(va_b2, name_va.lower())
        )
        for name_va, signal_va in settings.DATA_BLOCK_2['VA_SIGNALS'].items()
    }

    vd_signals_b2 = {
        name_vd: "ДА" if getattr(vd_b2, name_vd.lower()) == 1 else "НЕТ"
        for name_vd, signal_vd in settings.DATA_BLOCK_2['VD_SIGNALS'].items()
    }

    va_signals_b3 = {
        name_va: calculate_result(
            signal_va['Koef_1'],
            signal_va['Koef_2'],
            getattr(va_b3, name_va.lower())
        )
        for name_va, signal_va in settings.DATA_BLOCK_3['VA_SIGNALS'].items()
    }

    vd_signals_b3 = {
        name_vd: "ДА" if getattr(vd_b3, name_vd.lower()) == 1 else "НЕТ"
        for name_vd, signal_vd in settings.DATA_BLOCK_3['VD_SIGNALS'].items()
    }
    dict_ras = {
        'date_block_1': str(va_b1.timepoint),
        'date_block_2': str(va_b2.timepoint),
        'date_block_3': str(va_b3.timepoint),
        'L110KvaB1': va_signals_b1, 'L110KvdB1': vd_signals_b1,
        'L110KvaB2': va_signals_b2, 'L110KvdB2': vd_signals_b2,
        'L110KvaB3': va_signals_b3, 'L110KvdB3': vd_signals_b3
    }

    return json.dumps(dict_ras)


def create_report(data):
    va_signals, vd_signals_start, vd_signals, block_num, va_params, vd_params = itemgetter(0, 1, 2, 3, 4, 5)(
        get_data_block(data))
    if data.GET['type'] == 'text_report':
        str = f"""
Отчет по параметрам работы энергоблока № {block_num}

{create_title_va(block_num, va_params)}  
{create_data_va(block_num, va_signals, va_params)}
{create_title_vd(block_num, vd_params, vd_signals_start)}   
{create_data_vd(block_num, vd_params, vd_signals)}     
        """

        my_file = open("media/files/text_report.txt", "w+")
        my_file.write(str)
        my_file.close()
        return "/media/files/text_report.txt"
    else:
        ft = Font(bold=True)
        excel_file = openpyxl.Workbook()
        list_of_excel = excel_file.active
        list_of_excel.title = 'Система регистрации аварийных ситуаций'
        for i in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                  'U', 'V', 'W', 'X', 'Y', 'Z']:
            list_of_excel.column_dimensions[i].width = 30
        list_of_excel.append(('Заголовок', ''))
        list_of_excel.append((f'Отчет по параметрам работы энергоблока № {block_num}', ''))
        list_of_excel['A1'].font = ft
        list_of_excel['A2'].font = ft
        if va_params != []:
            list_of_excel.append(('', ''))
            title = ['Дата/Время']
            list_of_excel.append(('АНАЛОГОВЫЕ СИГНАЛЫ', ''))
            list_of_excel.append(('', ''))
            for va_param in va_params:
                title.append(getattr(settings, f'DATA_BLOCK_{block_num}')['VA_SIGNALS'][f'{va_param}']['name'])
            list_of_excel.append(title)
            for va_signal in va_signals:
                data_row = [va_signal.timepoint.strftime('%d.%m.%Y %H:%M:%S')]
                for va_param in va_params:
                    data_row.append(
                        f"{calculate_result(getattr(settings, f'DATA_BLOCK_{block_num}')['VA_SIGNALS'][f'{va_param}']['Koef_1'], getattr(settings, f'DATA_BLOCK_{block_num}')['VA_SIGNALS'][f'{va_param}']['Koef_2'], getattr(va_signal, va_param.lower())):.2f}")
                list_of_excel.append(data_row)
        if vd_params != []:
            list_of_excel.append(('', ''))
            list_of_excel.append(('', ''))
            list_of_excel.append(('ДИСКРЕТНЫЕ СИГНАЛЫ', ''))
            list_of_excel.append(['Дата/Время', 'Наименование', 'Значение'])
            list_of_excel.append(('', ''))
            list_of_excel.append(('ИСХОДНЫЕ', ''))
            for vd_param in vd_params:
                list_of_excel.append([vd_signals_start.timepoint.strftime('%d.%m.%Y'),
                                      getattr(settings, f'DATA_BLOCK_{block_num}')['VD_SIGNALS'][f'{vd_param}']['name'],
                                      getattr(vd_signals_start, vd_param.lower())])
            list_of_excel.append(('', ''))
            for vd_signal in vd_signals:
                list_of_excel.append([vd_signal.timepoint.strftime('%d.%m.%Y %H:%M:%S'),
                                      getattr(settings, f'DATA_BLOCK_{block_num}')['VD_SIGNALS'][
                                          f'{vd_signal.sig_name.strip()}']['name'], vd_signal.sig_state])
        excel_file.save('media/files/xlsx_report.xlsx')
        return "/media/files/xlsx_report.xlsx"


def create_chart(data):
    va_signals, vd_signals_start, vd_signals, block_num, va_params, vd_params, vd_signals_finish = get_data_block(data)
    colors = ["red", "green", "blue", "yellow", "cyan", "magenta", "orange", "brown", "purple", "pink", "gray", "black",
              "white", "olive", "maroon", "navy"]

    dict_chart = defaultdict(list)
    if va_params != []:
        if data.GET['type'] == "real_value":
            param_data = {}
            data_block = getattr(settings, f'DATA_BLOCK_{block_num}')
            for va_param in va_params:
                va_info = data_block['VA_SIGNALS'][va_param]
                param_data[va_param] = {
                    'name': va_info['name'],
                    'Koef_1': va_info['Koef_1'],
                    'Koef_2': va_info['Koef_2']
                }

            for va_signal in va_signals:
                for va_param in va_params:
                    # Получаем данные из предвычисленного словаря
                    name = param_data[va_param]['name']
                    k1 = param_data[va_param]['Koef_1']
                    k2 = param_data[va_param]['Koef_2']

                    # Вычисляем результат (один раз для каждой пары (сигнал, параметр))
                    result = calculate_result(k1, k2, getattr(va_signal, va_param.lower()))
                    value = f"{result:.2f}"

                    # Добавляем в список для ключа
                    time_str = va_signal.timepoint.strftime('%Y-%m-%d %H:%M:%S')
                    dict_chart[name].append({'x': time_str, 'y': value})


        elif data.GET['type'] == "clean_value":
            key_map = {
                va_param: getattr(settings, f'DATA_BLOCK_{block_num}')['VA_SIGNALS'][va_param]['name']
                for va_param in va_params
            }
            for va_signal in va_signals:
                for va_param in va_params:
                    key = key_map[va_param]
                    time_str = va_signal.timepoint.strftime('%Y-%m-%d %H:%M:%S')
                    value = getattr(va_signal, va_param.lower())
                    dict_chart[key].append({'x': time_str, 'y': value})
        else:
            key_map = {
                va_param: getattr(settings, f'DATA_BLOCK_{block_num}')['VA_SIGNALS'][va_param]['name']
                for va_param in va_params
            }
            for va_signal in va_signals:
                for va_param in va_params:
                    key = key_map[va_param]
                    value = {'x': va_signal.timepoint.strftime('%Y-%m-%d %H:%M:%S'),
                             'y': abs(getattr(va_signal, va_param.lower()) / 10)}
                    dict_chart[key].append(value)
    if vd_params != []:
        key_map = {
            vd_param: getattr(settings, f'DATA_BLOCK_{block_num}')['VD_SIGNALS'][f'{vd_param}']['name']
            for vd_param in vd_params
        }

        for vd_param in vd_params:
            key = key_map[vd_param.upper()]
            time_str = vd_signals_start.timepoint.strftime('%Y-%m-%d %H:%M:%S')
            value = getattr(vd_signals_start, vd_param.lower())
            dict_chart[key].append({'x': time_str, 'y': value})

        for vd_signal in vd_signals:
            for vd_param in vd_params:
                key = key_map[vd_param.upper()]
                time_str = vd_signal.timepoint.strftime('%Y-%m-%d %H:%M:%S')
                value = vd_signal.sig_state
                dict_chart[key].append({'x': time_str, 'y': value})

        for vd_param in vd_params:
            key = key_map[vd_param.upper()]
            time_str = vd_signals_finish.timepoint.strftime('%Y-%m-%d %H:%M:%S')
            value = getattr(vd_signals_finish, vd_param.lower())
            dict_chart[key].append({'x': time_str, 'y': value})

    dict_chart_color = {
        key: [colors[index if index < 16 else index % 16], value]
        for index, (key, value) in enumerate(dict_chart.items())
    }
    dict_chart_out = {}
    for key, value in dict_chart_color.items():
        dict_chart_out[key] = {
            'borderColor': value[0],
            'label': key,
            'data': value[1],
            'borderWidth': 1,
        }
    return dict_chart_out
