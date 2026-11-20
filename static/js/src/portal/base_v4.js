$(document).ready(function () {
    create_calendar_base()
});

function refreshTime() {
    const timeDisplay = document.getElementById("portal_time_2");
    const dateString = new Date().toLocaleString("ru", {
        hour: 'numeric',
        minute: 'numeric',
        second: 'numeric'
    });
    const formattedString = dateString.replace(", ", " - ");
    timeDisplay.textContent = formattedString;
}

setInterval(refreshTime, 1000);


function create_calendar_base() {
    let day_calendar_base = new Date()
    let day_week_calendar_base = new Date(day_calendar_base.getFullYear(), day_calendar_base.getMonth(), 1).getDay()
    if (day_week_calendar_base == 0) {
        day_week_calendar_base = 6
    } else {
        day_week_calendar_base -= 1
    }
    let days_in_month_calendar_base = new Date(day_calendar_base.getFullYear(), day_calendar_base.getMonth() + 1, 0).getDate()
    let now_day_calendar_base = day_calendar_base.getDate()
    let count_day_calendar_base = 1
    div_calendar_base = ""
    for (let row = 0; row <= 5; row++) {
        div_calendar_base += '<div style="display: flex; gap: 1rem;"> \n'
        for (let col = 0; col <= 6; col++) {
            if ((row == 0) && (col < day_week_calendar_base)) {
                div_calendar_base += '<div style="width: 100%; font-weight: bold; "></div> \n'
            } else {
                if (count_day_calendar_base <= days_in_month_calendar_base) {
                    if (now_day_calendar_base == count_day_calendar_base) {
                        div_calendar_base += '<div style="border-radius: 15%; width: 100%; font-weight: bold; text-align: center; color: white; background: linear-gradient(to top, black, #005D9F);">' + count_day_calendar_base + '</div> \n'

                    } else {
                        div_calendar_base += '<div style="width: 100%; font-weight: bold; text-align: center;">' + count_day_calendar_base + '</div> \n'

                    }
                    count_day_calendar_base++;
                } else {
                    div_calendar_base += '<div style="width: 100%; font-weight: bold; "></div> \n'
                }
            }
        }
        div_calendar_base += '</div> \n'
    }
    document.getElementById('calendar_base').innerHTML = div_calendar_base
}



setInterval(function () {
    $.ajax({
        type: 'get',
        dataType: 'json',
        url: '/update_temper_and_date/',
        data: {},
        success: function (data) {
            $('.span_now_date_portal').each(function () {
                console.log(data['date_now'])
                $(this).text(data['date_now'])
            });
            $('.span_temper_neryngri').each(function () {
                $(this).text(data['temper_neryngri'] + ' °C')
            });
            $('.span_temper_chulman').each(function () {
                $(this).text(data['temper_chulman'] + ' °C')
            });
            let day_calendar_base = new Date()
            if ((day_calendar_base.getDate()).toString() != $('.div_calendar_base').text()) {
                create_calendar_base()
            }
        }
    })
}, 600000);


function GetResultCalendarFooter() {
    let temp_json
    let day_calendar_base = new Date()
    let temp_array = []

    $.get({
        url: "/static/json/" + day_calendar_base.getFullYear() + ".json",
        async: false,
    })
        .done(function (data) {
            temp_json = JSON.stringify(data['holidays'])
            let temp_month = day_calendar_base.getMonth() + 1 < 10 ? "0" + (day_calendar_base.getMonth() + 1).toString() : (day_calendar_base.getMonth() + 1).toString()
            JSON.parse(temp_json).forEach((value) => {
                if (value.includes('-' + temp_month + '-')) {
                    temp_array.push(parseInt(value.split('-')[2]))
                }
            });
        })
        .fail(function () {
        });
    return temp_array
}