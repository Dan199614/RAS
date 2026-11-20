// Инициализация пустого графика
var chart_system_ras = new Chart($('#chart'), {
    type: 'scatter',
    data: {
        datasets: [],
    },
});


// Функции подбора цвета для параметров
function color_class_param_block_1(value_block, el, date_block) {
    date_hour_1 = moment(new Date()).subtract(1, 'hour')
    date_block = moment(date_block)
    if (date_hour_1.isAfter(date_block)) {
        return 'text-body-tertiary'
    } else {
        if ((DATA_BLOCK_1_param[el].LowLimit >= value_block) || (DATA_BLOCK_1_param[el].HighLimit <= value_block)) {
            return 'text-danger'
        } else if (((DATA_BLOCK_1_param[el].LowLimit < value_block) && (value_block > DATA_BLOCK_1_param[el].LowGran)) || ((DATA_BLOCK_1_param[el].HighGran < value_block) && (DATA_BLOCK_1_param[el].HighLimit > value_block))) {
            return 'text-success'
        } else return 'text-warning'
    }


}

function color_class_param_block_2(value_block, el, date_block) {
    date_hour_1 = moment(new Date()).subtract(1, 'hour')
    date_block = moment(date_block)
    if (date_hour_1.isAfter(date_block)) {
        return 'text-body-tertiary'
    } else {
        if ((DATA_BLOCK_2_param[el].LowLimit >= value_block) || (DATA_BLOCK_2_param[el].HighLimit <= value_block)) {
            return 'text-danger'
        } else if (((DATA_BLOCK_2_param[el].LowLimit < value_block) && (value_block > DATA_BLOCK_2_param[el].LowGran)) || ((DATA_BLOCK_2_param[el].HighGran < value_block) && (DATA_BLOCK_2_param[el].HighLimit > value_block))) {
            return 'text-success'
        } else return 'text-warning'
    }


}

function color_class_param_block_3(value_block, el, date_block) {
    date_hour_1 = moment(new Date()).subtract(1, 'hour')
    date_block = moment(date_block)
    if (date_hour_1.isAfter(date_block)) {
        return 'text-body-tertiary'
    } else {
        if ((DATA_BLOCK_3_param[el].LowLimit >= value_block) || (DATA_BLOCK_3_param[el].HighLimit <= value_block)) {
            return 'text-danger'
        } else if (((DATA_BLOCK_3_param[el].LowLimit < value_block) && (value_block > DATA_BLOCK_3_param[el].LowGran)) || ((DATA_BLOCK_3_param[el].HighGran < value_block) && (DATA_BLOCK_3_param[el].HighLimit > value_block))) {
            return 'text-success'
        } else return 'text-warning'
    }


}

// Стриминг данных на экран
$(function () {
    let eventSource = new EventSource('/stream/')
    eventSource.onmessage = (event) => {
        data_ras = JSON.parse(event.data)
        date_hour_1 = moment(new Date()).subtract(1, 'hour')

        for (var el in data_ras.L110KvaB1) {
            $('#table_BLOCK_1').find(`#param_block_1_${el}`).text(data_ras.L110KvaB1[el].toFixed(2))
                .removeClass('text-success text-warning text-danger text-body-tertiary')
                .addClass(`${color_class_param_block_1(data_ras.L110KvaB1[el], el, data_ras.date_block_1)}`)
        }
        for (var el in data_ras.L110KvdB1) {
            $('#table_BLOCK_1').find(`#param_block_1_${el}`)
                .addClass(`${date_hour_1.isAfter(moment(data_ras.date_block_1))
                    ? 'text-body-tertiary' :
                    data_ras.L110KvdB1[el] === 'ДА'
                        ? 'text-success'
                        : 'text-danger'}`)
                .removeClass(`${date_hour_1.isBefore(moment(data_ras.date_block_1))
                    ? 'text-body-tertiary' :
                    data_ras.L110KvdB1[el] === 'ДА'
                        ? 'text-danger'
                        : 'text-success'}`).text(data_ras.L110KvdB1[el])
        }
        for (var el in data_ras.L110KvaB2) {
            $('#table_BLOCK_2').find(`#param_block_2_${el}`).text(data_ras.L110KvaB2[el].toFixed(2))
                .removeClass('text-success text-warning text-danger text-body-tertiary')
                .addClass(`${color_class_param_block_2(data_ras.L110KvaB2[el], el, data_ras.date_block_2)}`)
        }
        for (var el in data_ras.L110KvdB2) {
            $('#table_BLOCK_2').find(`#param_block_2_${el}`)
                .addClass(`${date_hour_1.isAfter(moment(data_ras.date_block_2))
                    ? 'text-body-tertiary' :
                    data_ras.L110KvdB2[el] === 'ДА'
                        ? 'text-success'
                        : 'text-danger'}`)
                .removeClass(`${date_hour_1.isBefore(moment(data_ras.date_block_2))
                    ? 'text-body-tertiary' :
                    data_ras.L110KvdB2[el] === 'ДА'
                        ? 'text-danger'
                        : 'text-success'}`).text(data_ras.L110KvdB2[el])
        }
        for (var el in data_ras.L110KvaB3) {
            $('#table_BLOCK_3').find(`#param_block_3_${el}`).text(data_ras.L110KvaB3[el].toFixed(2))
                .removeClass('text-success text-warning text-danger text-body-tertiary')
                .addClass(`${color_class_param_block_3(data_ras.L110KvaB3[el], el, data_ras.date_block_3)}`)
        }
        for (var el in data_ras.L110KvdB3) {
            $('#table_BLOCK_3').find(`#param_block_3_${el}`)
                .addClass(`${date_hour_1.isAfter(moment(data_ras.date_block_3))
                    ? 'text-body-tertiary' :
                    data_ras.L110KvdB3[el] === 'ДА'
                        ? 'text-success'
                        : 'text-danger'}`)
                .removeClass(`${date_hour_1.isBefore(moment(data_ras.date_block_3))
                    ? 'text-body-tertiary' :
                    data_ras.L110KvdB3[el] === 'ДА'
                        ? 'text-danger'
                        : 'text-success'}`).text(data_ras.L110KvdB3[el])
        }
    }
});

// Обработка чекбоксов заголовка
$('.group_check_VA_block_1').change(function () {
    $(`.${$(this).prop('id').replace("block_1_VA_group_", "")}_VA_check_block_1`).prop('checked', this.checked);
})
$('.group_check_VD_block_1').change(function () {
    $(`.${$(this).prop('id').replace("block_1_VD_group_", "")}_VD_check_block_1`).prop('checked', this.checked);
})
$('.group_check_VA_block_2').change(function () {
    $(`.${$(this).prop('id').replace("block_2_VA_group_", "")}_VA_check_block_2`).prop('checked', this.checked);
})
$('.group_check_VD_block_2').change(function () {
    $(`.${$(this).prop('id').replace("block_2_VD_group_", "")}_VD_check_block_2`).prop('checked', this.checked);
})
$('.group_check_VA_block_3').change(function () {
    $(`.${$(this).prop('id').replace("block_3_VA_group_", "")}_VA_check_block_3`).prop('checked', this.checked);
})
$('.group_check_VD_block_3').change(function () {
    $(`.${$(this).prop('id').replace("block_3_VD_group_", "")}_VD_check_block_3`).prop('checked', this.checked);
})


// Обработка открытия модального окна для отчета
$('#report_block_1, #report_block_2, #report_block_3').click(function () {
    $('#modal_create_report').modal('show');
    $('#modal_create_report_title').text(`${$(this).prop('id') === 'report_block_1'
        ? 'Отчет по параметрам энергоблока №1'
        : $(this).prop('id') === 'report_block_2'
            ? 'Отчет по параметрам энергоблока №2'
            : 'Отчет по параметрам энергоблока №3'}`)
    date_now = new Date();
    $('#date_start').val(new Date(date_now.getFullYear(), date_now.getUTCMonth(), date_now.getDate(), 0, 0, 0).toLocaleString("sv-SE", {
        year: "numeric",
        month: "2-digit",
        day: "2-digit",
        hour: "2-digit",
        minute: "2-digit",
    }).replace(" ", "T"));
    $('#date_finish').val(new Date(date_now.getFullYear(), date_now.getMonth(), date_now.getDate(), 23, 59, 0).toLocaleString("sv-SE", {
        year: "numeric",
        month: "2-digit",
        day: "2-digit",
        hour: "2-digit",
        minute: "2-digit",
    }).replace(" ", "T"));
})


// Обработка открытия модального окна для графика
$('#chart_block_1, #chart_block_2, #chart_block_3').click(function () {
    chart_system_ras.destroy();
    $('#save_chart').prop('disabled', true);
    $('#modal_create_chart').modal('show');
    $('#modal_create_chart_title').text(`${$(this).prop('id') === 'chart_block_1'
        ? 'График по параметрам энергоблока №1'
        : $(this).prop('id') === 'chart_block_2'
            ? 'График по параметрам энергоблока №2'
            : 'График по параметрам энергоблока №3'}`)
    date_now = new Date();
    $('#date_start_chart').val(new Date(date_now.getFullYear(), date_now.getMonth(), date_now.getDate(), 0, 0, 0).toLocaleString("sv-SE", {
        year: "numeric",
        month: "2-digit",
        day: "2-digit",
        hour: "2-digit",
        minute: "2-digit",
    }).replace(" ", "T"));
    $('#date_finish_chart').val(new Date(date_now.getFullYear(), date_now.getMonth(), date_now.getDate(), 23, 59, 0).toLocaleString("sv-SE", {
        year: "numeric",
        month: "2-digit",
        day: "2-digit",
        hour: "2-digit",
        minute: "2-digit",
    }).replace(" ", "T"));
})

// Обработка кнопки построить график
$('#create_chart').click(function () {
    let date_time_start = $('#date_start_chart').val();
    let date_time_finish = $('#date_finish_chart').val();
    if ((date_time_start !== '') && (date_time_finish !== '')) {
        if ((new Date(date_time_start) < new Date(date_time_finish)) && (((new Date(date_time_finish) - new Date(date_time_start)) / (1000 * 3600 * 24)) <= 2)) {
            let params = $(`#table_BLOCK_${$('#modal_create_chart_title').text() === 'График по параметрам энергоблока №1'
                    ? '1'
                    : $('#modal_create_chart_title').text() === 'График по параметрам энергоблока №2'
                            ? '2'
                            : '3'}`).find('.param_checkbox:checked').map(function () {
                return this.id
            }).get();
            if (params.length !== 0) {
                $('#create_chart').html('<span class="spinner-border spinner-border-sm" id="load_chart"></span> Получение данных...');
                $.ajax({
                    url: '{% ' / ' %}',
                    data: {
                        create: "create_chart",
                        date_time_start: date_time_start,
                        date_time_finish: date_time_finish,
                        params: JSON.stringify(params),
                        type: $('input[name="chart"]:checked').prop('id')
                    }
                }).done(function (response) {
                    if (chart_system_ras.id) {
                        chart_system_ras.destroy();
                    }
                    const plugin = {
                        id: 'customCanvasBackgroundColor',
                        beforeDraw: (chart, args, options) => {
                            const {ctx} = chart;
                            ctx.save();
                            ctx.globalCompositeOperation = 'destination-over';
                            ctx.fillStyle = options.color || '#99ffff';
                            ctx.fillRect(0, 0, chart.width, chart.height);
                            ctx.restore();
                        }
                    };
                    try {
                        chart_system_ras = new Chart($('#chart'), {
                            responsive: true,
                            type: 'line',
                            data: {
                                label: [date_time_start, date_time_finish],
                                datasets: Object.values(response)
                            },
                            options: {
                                scales: {
                                    x: {
                                        type: 'time',
                                        time: {
                                            unit: 'second',
                                            tooltipFormat: 'YYYY.MM.DD HH:mm:ss',
                                            displayFormats: {
                                                second: 'HH:mm:ss'
                                            },
                                        }
                                    },
                                    y: {
                                        beginAtZero: true,
                                    }
                                },

                                plugins: {
                                    decimation: {
                                        enabled: true,
                                        algorithm: 'min-max',
                                    },
                                    customCanvasBackgroundColor: {
                                        color: 'white',
                                    },
                                    zoom: {
                                        zoom: {
                                            wheel: {
                                                enabled: true,
                                            },
                                            pinch: {
                                                enabled: true
                                            },
                                            mode: 'xy',
                                        }
                                    },
                                },
                                elements: {
                                    point: {
                                        radius: 0
                                    },

                                },
                            },

                            plugins: [plugin],
                        });
                        $('#save_chart').prop('disabled', false);
                    } catch (e) {
                        alert('Что-то пошло не так! Попробуйте изменить временной диапазон.');
                        $('#chart').remove();
                        $('#modal_create_chart').find('.modal-body').append(`<canvas id="chart" class="w-100"></canvas>`);
                    } finally {
                        $('#create_chart').text('Построить');
                    }

                })
            } else {
                alert('Не выбраны параметры, для которых нужно построить отчет!')
            }
        } else {
            alert('Временные промежутки выбраны неверно!')
        }
    } else {
        alert('Не заполнены временные промежутки!')
    }

})


// Обработка кнопки создать отчет
$('#create_report').click(function () {
    let date_time_start = $('#date_start').val();
    let date_time_finish = $('#date_finish').val();
    if ((date_time_start !== '') && (date_time_finish !== '')) {
        if ((new Date(date_time_start) < new Date(date_time_finish)) && (((new Date(date_time_finish) - new Date(date_time_start)) / (1000 * 3600 * 24)) <= 2)) {
            let params = $(`#table_BLOCK_${$('#modal_create_report_title').text() === 'Отчет по параметрам энергоблока №1'
                    ? '1'
                    : $('#modal_create_report_title').text() === 'Отчет по параметрам энергоблока №2'
                            ? '2'
                            : '3'}`).find('.param_checkbox:checked').map(function () {
                return this.id
            }).get();
            if (params.length !== 0) {
                $('#load_report').removeClass('d-none');
                $.ajax({
                    url: '{% ' / ' %}',
                    data: {
                        create: "create_report",
                        date_time_start: date_time_start,
                        date_time_finish: date_time_finish,
                        params: JSON.stringify(params),
                        type: $('input[name="report"]:checked').prop('id')
                    }
                }).done(function (response) {
                    let a = document.createElement('a');
                    a.href = response;
                    a.download = "report";
                    document.body.appendChild(a);
                    a.click();
                    document.body.removeChild(a);
                    $('#load_report').addClass('d-none')
                })
            } else {
                alert('Не выбраны параметры, для которых нужно построить отчет!')
            }
        } else {
            alert('Временные промежутки выбраны неверно!')
        }
    } else {
        alert('Не заполнены временные промежутки!')
    }
})


// Обработка сохранения графика
$('#save_chart').click(function () {
    var url_base64jp = chart_system_ras.toBase64Image("image/jpeg", 1.0)
    let a = document.createElement('a');
    a.href = url_base64jp;
    a.download = "chart";
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
})