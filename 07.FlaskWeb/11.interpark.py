from flask import Flask, render_template, request
import interpark_util as iu

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask'

@app.route('/interpark', methods=['GET', 'POST'])
def interpark():
    book_list = iu.crawling()
    return render_template('11.interpark.html', book_list=book_list)

if __name__ == '__main__':
    app.run(debug=True)

