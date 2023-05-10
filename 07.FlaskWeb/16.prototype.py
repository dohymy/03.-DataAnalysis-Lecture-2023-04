from flask import Flask, render_template, request
from weather_util import get_weather
import interpark_util as iu
import chart_util as cu
import siksin_util as su

app = Flask(__name__)

@app.route('/')
def home():
    menu = {'ho':1, 'us':0, 'cr':0, 'sc':0}
    return render_template('prototype/home.html', menu=menu, weather=get_weather(app))

@app.route('/pr')
def pr():
    menu = {'ho':0, 'us':1, 'cr':0, 'sc':0}
    return render_template('prototype/pr.html', menu=menu, weather=get_weather(app))

@app.route('/interpark')
def interpark():
    book_list = iu.crawling()
    menu = {'ho':0, 'us':0, 'cr':1, 'sc':0}
    return render_template('prototype/interpark.html', menu=menu, weather=get_weather(app), book_list=book_list)

@app.route('/chart')
def chart():
    chart_list = cu.chart()
    menu = {'ho':0, 'us':0, 'cr':1, 'sc':0}
    return render_template('prototype/chart.html', menu=menu, weather=get_weather(app), chart_list=chart_list)

@app.route('/siksin', methods=['GET', 'POST'])
def siksin():
    menu = {'ho':0, 'us':0, 'cr':1, 'sc':0}
    if request.method == 'GET':
        return render_template('prototype/siksin.html', menu=menu, weather=get_weather(app))
    else:
        place = request.form['place']
        siksin_list = su.siksin(place)
        return render_template('prototype/siksin_res.html', menu=menu, weather=get_weather(app), siksin_list=siksin_list, place=place)

@app.route('/schedule')
def schedule():
    menu = {'ho':0, 'us':0, 'cr':0, 'sc':1}
    return render_template('prototype/schedule.html', menu=menu, weather=get_weather(app))


if __name__ == '__main__':
    app.run(debug=True)
