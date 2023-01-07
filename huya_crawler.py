import requests
import  re
import  json
# #EXTINF:-1 tvg-logo="https://huyaimg.msstatic.com/avatar/1037/07/de445ffea2560634bc51cd203be6ac_180_135.jpg?1615362899" group-title="天龙八部手游", 聚悦、啵啵
# https://epg.112114.xyz/huya/597461
def get_real_url(gameid,range_list):
    try:

        header = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/75.0.3770.100 Mobile Safari/537.36 ',
            'Accept-Encoding' : 'deflate',
        }
        for page_id in range(1,range_list+1):
            cache = requests.get("https://www.huya.com/cache.php?m=LiveList&do=getLiveListByPage&gameId={}&tagAll=0&callback=getLiveListJsonpCallback&page={}".format(str(gameid),str(page_id)),headers=header)
            cache_content=cache.content.decode('utf-8','ignore')
            real_content= re.findall("({.*})", cache_content)[0]
            json_content = json.loads(real_content)


            for person_json in  json_content['data']["datas"]:
                nick=person_json['nick']
                group_title=person_json['gameFullName']
                id=person_json['profileRoom']
                jpg=person_json['avatar180']

                m3u_content = "#EXTINF:-1 tvg-logo=\"{}\" group-title=\"{}\", {}".format(jpg,group_title,nick)
                m3u_url = "https://epg.112114.xyz/huya/{}".format(id)
                print(m3u_content)
                print(m3u_url)
    except Exception as e:

        print(e)
get_real_url(gameid="4079",range_list=6)