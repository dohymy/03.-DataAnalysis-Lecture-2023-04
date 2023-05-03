from flask import Flask, render_template, request
import numpy as np
import matplotlib.pyplot as plt
import os
import map_util as mu
import interpark_util as iu

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask'

# carousel
@app.route('/carousel')
def carousel():
    return render_template('14.carousel.html')

# progress
@app.route('/progress')
def progress():
    return render_template('14.progress bar.html')

# scatter
@app.route('/scatter', methods = ['GET', 'POST'])
def scatter():
    if request.method == 'GET':
        return render_template('14.산점도.html')
    else:
        num = int(request.form['num'])
        mean = float(request.form['mean'])
        std = float(request.form['std'])
        min = float(request.form['min'])
        max = float(request.form['max'])
        xs = np.random.normal(loc=mean, scale=std, size=num)
        ys = np.random.uniform(min, max, num)
        plt.figure()
        plt.scatter(xs, ys)
        filename = os.path.join(app.static_folder,'img/scatter.png')
        plt.savefig(filename)
        return render_template('14.산점도_res.html')
    
# hotplace
@app.route('/hotPlaces', methods=['GET','POST'])
def hotPlaces():
    if request.method == 'GET':
        return render_template('14.HotPlaces.html')
    else:
        # client가 입력한 장소 알아내기
        place1 = request.form['place1']
        place2 = request.form['place2']
        place3 = request.form['place3']
        places = [place1, place2, place3]

        mu.hot_places(places, app)
        
        return render_template('14.hotPlaces_res.html')
    
# interpark
@app.route('/interpark', methods=['GET', 'POST'])
def interpark():
    book_list = iu.crawling()
    return render_template('14.interpark.html', book_list=book_list)

if __name__ == '__main__':
    app.run(debug=True)

