from flask import Flask , render_template , request, redirect, url_for, send_file
from main import (
  YouTubeInfo ,extract_watch_url,convert_to_embed_url, YouTubeDownloadUseingRequest)
from pytube import YouTube
app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@app.route('/',methods=['GET','POST'])
def home():
  if request.method == 'POST':
    url = request.form.get('text')
    if url == '' or url == None:
      return redirect(url_for('home'))
      url = None
    else:
      url = request.form.get('text')
    R_request= YouTubeInfo(extract_watch_url(url))
    Title =R_request['Title']
    Duration =R_request['Duration']
    Views =R_request['Views']
    Rating =R_request['Rating']
    Description =R_request['Description']
    return render_template('index.html',Title=Title,emurl=convert_to_embed_url(url),Rmode=True,Duration=Duration,Views=Views,Rating=Rating,Description=Description,url=extract_watch_url(url))
  if request.method == 'GET':
    return render_template('index.html')

@app.route('/download_video', methods=['POST','GET'])
def download_video():
  if request.method == 'GET':
    return redirect(url_for('home'))
  if request.method.lower() == "post":
      video_url = request.form.get('downloadURL')
      download_url = YouTubeDownloadUseingRequest(video_url)
      return redirect(download_url)
  

@app.route('/download_url', methods=['POST','GET'])
def download_video():
  if request.method == 'GET':
    return redirect(url_for('home'))
  if request.method.lower() == "post":
      video_url = request.form.get('downloadURL')
      download_url = YouTubeDownloadUseingRequest(video_url)
      return download_url





if __name__ == '__main__':
  app.run(host='0.0.0.0',port='5000')
# Obj ={
#   'Title':yt.title,
#   'Duration':yt.length,
#   'Views':yt.views,
#   'Rating':yt.rating,
#   'Description':yt.description
#   }