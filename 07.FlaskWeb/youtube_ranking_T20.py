from flask import Flask, render_template, request
import youtube_T20_util as yu20

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask'

@app.route('/youtube_ranking_Top20', methods=['GET', 'POST'])
def youtube_ranking_Top20():
    rank_list = yu20.crawling()
    return render_template('youtube_ranking_Top20.html', rank_list=rank_list)

if __name__ == '__main__':
    app.run(debug=True)

