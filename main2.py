from youtube_statistics import YTstats

API_KEY = "AIzaSyBvp2BdZow7o9DWssirx_QgZzjFH2--pNw"
channel_id = "Randy Santel"

yt = YTstats(API_KEY, channel_id)
yt.get_channel_statistics()