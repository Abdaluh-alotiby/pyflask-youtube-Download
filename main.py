import re
import requests
from bs4 import BeautifulSoup


def YouTubeDownloadUseingRequest(CleanWatchUrl):
  r = requests.get(f"https://10downloader.com/download?v={CleanWatchUrl}&utm_source=000tube")
  res = r.text
  soup = BeautifulSoup(res,"html.parser")
  download_link = soup.find("a",class_="downloadBtn")
  if download_link:
    download_url = download_link.get("href")
    return download_url
  

try:
  from pytube import YouTube

  def YouTubed(Yurl):
    
    video_url = Yurl
    
    yt = YouTube(video_url)
    
    stream = yt.streams.get_highest_resolution()
    stream.download()




  def YouTubeInfo(Yurl):
    video_url = Yurl
    
    yt = YouTube(video_url)
    
    Obj ={
    'Title':yt.title,
    'Duration':yt.length,
    'Views':yt.views,
    'Rating':yt.rating,
    'Description':yt.description
    }
    return Obj
except ModuleNotFoundError:
  print(
    """
    The model Pytube is not install
    Therefor the functions:
    (YouTubeInfo)
    (YouTubeD)
    is not cofig
    To install type :
    # pip install pytube
    """
  )
  pass

def extract_video_id(url):
    # Define a regular expression pattern to match YouTube video URLs
    pattern = r'(?<=v=)[a-zA-Z0-9_-]+(?=&|\b)'
    # Search for the video ID using the pattern
    match = re.search(pattern, url)
    if match:
        return match.group(0)
    else:
        return None

# Example usage:
# search_url = "https://www.google.com/search?q=nmap&source=lmns&tbm=vid&bih=739&biw=430&client=safari&prmd=ivn&hl=ar&sa=X&ved=2ahUKEwjzhc_xxNWEAxWBTKQEHcsIB_cQ_AUoAnoECAAQDg#"
# video_id = extract_video_id(search_url)
# if video_id:
#     # Construct the YouTube watch URL using the extracted video ID
#     watch_url = f"https://www.youtube.com/watch?v={video_id}"
#     print(watch_url)
# else:
#     print("No YouTube video ID found in the URL.")
def extract_video(url):
  video_id = extract_video_id(url)
  if video_id:
      watch_url = f"https://www.youtube.com/watch?v={video_id}"
      return watch_url
  else:
      return "No YouTube video ID found in the URL."





def extract_watch_url(shared_url):
    if 'watch' in shared_url:
      return shared_url
    elif "shorts" in shared_url:
      return convert_shorts_url_to_watch_url(shared_url)
    elif "embed" in shared_url:
      return 
    else:
      pattern = r'https://youtu\.be/([^\?]+)'
      match = re.search(pattern, shared_url)
      if match:
          return "https://www.youtube.com/watch?v=" + match.group(1)
      else:
          return "Invalid YouTube URL"

#sys 1 : conver watch url to embed url
def convert_watch_url_to_embed_url(url):
    # Split the URL by '=' and '&', and find the part containing the video ID
    video_id = url.split('v=')[-1].split('&')[0]
    # Construct the embed URL
    embed_url = f'https://www.youtube.com/embed/{video_id}'
    return embed_url


def convert_to_embed_url(shared_url):
  if 'watch' in shared_url:
    embed_url = convert_watch_url_to_embed_url(shared_url)
    return embed_url
  elif "shorts" in shared_url:
    videoId =  shared_url.split("/shorts/")[1].split("?")[0]
    return f"http://youtube.com/embed/{videoId}"

  else:
    # Remove the query string in get method
    if '?' in shared_url:
        shared_url = shared_url.split('?')[0]

    # Append '/embed/' to the domain
    embed_url = shared_url.replace('youtu.be', 'youtube.com/embed')

    return embed_url

#https://www.youtube.com/shorts/v0h3wWXI7H4
def convert_shorts_url_to_watch_url(url):
  # url = 'https://www.youtube.com/shorts/v0h3wWXI7H4'
  if "shorts" in url and "youtube" in url :
    videoId =  url.split("/shorts/")[1].split("?")[0]
    watch_url = f"https://www.youtube.com/watch?v={videoId}"
    return watch_url


















