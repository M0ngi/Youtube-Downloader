import sys, pafy, os, time, requests
from bs4 import BeautifulSoup
import json
from urllib.parse import urlparse, parse_qs


def get_streams(pafy_obj):
    return [stream for stream in pafy_obj.streams]


def get_audiostreams(pafy_obj):
    return [s for s in pafy_obj.audiostreams]


def getFirstVideoUrl(list_id):
    resp = requests.get('https://www.youtube.com/playlist?list='+list_id)
    soup = BeautifulSoup(resp.text, "html.parser")

    res = soup.find_all('script')
    ytInitialData = [x for x in res if "ytInitialData =" in x.text]
    assert len(ytInitialData) == 1, "Expected only one script"

    jsonData = ytInitialData[0].text.replace("var ytInitialData = ", "")[:-1] # remove ;
    ytInitialData = json.loads(jsonData)
    # print(ytInitialData)

    data = ytInitialData['contents']['twoColumnBrowseResultsRenderer']['tabs'][0]['tabRenderer']['content']['sectionListRenderer']
    videosData = data['contents'][0]['itemSectionRenderer']['contents'][0]['playlistVideoListRenderer']['contents']

    # print(data)
    # print(len(videosData))

    # Get the url to scrap the ids from.
    firstVid = videosData[0]
    firstVidUrl = firstVid['playlistVideoRenderer']['navigationEndpoint']['commandMetadata']['webCommandMetadata']['url']
    return "https://www.youtube.com"+firstVidUrl


def GetIds(url):
    """
        Due to the lazy loading at endpoint /playlist?list=
        we cannot scrap all video ids therefore,
        We get the first video url for the given playlist.
        The endpoint /watch?v=X&list=Y gives us a full list without lazy loading.
        We scrap the ids from that endpoint.
    """

    parsedUrl = urlparse(url)
    parsedQueries = parse_qs(parsedUrl.query)

    firstVidUrl = url
    if parsedUrl.path == "/watch":
        pass
    elif parsedUrl.path == "/playlist":
        firstVidUrl = getFirstVideoUrl(parsedQueries['list'][0])
    else:
        raise "Unknown"
    

    # print(firstVidUrl)

    resp = requests.get(firstVidUrl)
    soup = BeautifulSoup(resp.text, "html.parser")

    res = soup.find_all('script')
    ytInitialData = [x for x in res if "ytInitialData =" in x.text]

    assert len(ytInitialData) == 1, "Expected only one script"

    jsonData = ytInitialData[0].text.replace("var ytInitialData = ", "")[:-1] # remove ;
    ytInitialData = json.loads(jsonData)

    playlist = ytInitialData['contents']['twoColumnWatchNextResults']['playlist']['playlist']
    playlistTitle = playlist['title']
    playlistContent = playlist['contents']

    print(playlistTitle)
    # print(playlistContent[0])

    for videoData in playlistContent:
        vidTitle = videoData['playlistPanelVideoRenderer']['title']['simpleText']
        vidId = videoData['playlistPanelVideoRenderer']['navigationEndpoint']['watchEndpoint']['videoId']
        yield playlistTitle, vidTitle, vidId


def downloadAudio(playlistTitle, vidTitle, vidId):
    if not os.path.exists(f"./{playlistTitle}"):
        os.mkdir(f"./{playlistTitle}")
    while True:
        try:
            v = pafy.new('https://www.youtube.com/watch?v='+vidId)
            stream = v.audiostreams[-1]
            stream.download(f"./{playlistTitle}/{vidTitle}.mp3")
            # print(v.audiostreams)
            break
        except Exception as e:
            print("Error occured, sleeping for 5 seconds before trying again.")
            print(f"Error: {e}")
            time.sleep(5)
            
    return

URL = ""
for playlistTitle, vidTitle, vidId in GetIds(URL):
    downloadAudio(playlistTitle, vidTitle, vidId)
