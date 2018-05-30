import requests
import wxpy
from bs4 import BeautifulSoup
import time

bot = wxpy.Bot(console_qr=2, cache_path='botoo.pkl')


def get_msg(nmb):
    url = 'http://www.59xihuan.cn/index_' + str(nmb) + '.html'
    header = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                            'Chrome/66.0.3359.181 Safari/537.36'}
    h = requests.get(url, headers=header)
    html = h.text
    news_bf = BeautifulSoup(html, "html.parser")
    msgs = news_bf.find_all('div', class_='pic_text1')

    news = []
    pic_url = []
    for msg in msgs:
        news.append(msg.text)
        pic_src = msg.find('img').get('src')
        pic_url.append('http://www.59xihuan.cn' + pic_src)

    return news


def send_msg(nub):
    nub = nub
    try:
        friend = bot.friends().search(u'dianmei3')[0]
        msgs = get_msg(nub)
        for i in range(len(msgs[0])):
            friend.send(msgs[i])

    except:
        pass


if __name__ == '__main__':
    for i in range(10):
        send_msg(i)
        time.sleep(10)
