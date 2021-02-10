import requests

host = 'localhost'


def getRaw(URL):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    while True:
        try:
            res = requests.get(URL, headers=headers)
        except:
            continue
        return res.json()


def onlyHangul(word):
    res = ""
    for i in word:
        if '가' <= i <= '힣':
            res += i
    return res


def crawlWord(word):
    st = ""
    for i in range(1, 5):
        obj = getRaw(
            'https://ko.dict.naver.com/api3/koko/search?query=%s&m=pc&range=word&page=%d&shouldSearchOpen=false' % (
                word, i))
        for w in obj['searchResultMap']['searchResultListMap']['WORD']['items']:
            try:
                if w['handleEntry'] != onlyHangul(w['handleEntry']):
                    continue
                st += w['handleEntry'] + ',' + onlyHangul(
                    w['searchPhoneticSymbolList'][0]['phoneticSymbol'].split('/')[0].split(',')[0].split(']')[0]) + '\n'
            except:
                pass
            try:
                detail = getRaw('https://ko.dict.naver.com/api/platform/koko/entry.nhn?entryId=' + w['entryId'])
                for wi in detail['entry']['conjs']:
                    try:
                        if wi['conj_content'] != onlyHangul(wi['conj_content']) or wi['pron'] == '':
                            continue
                        st += wi['conj_content'] + ',' + onlyHangul(
                            wi['pron'].split('/')[0].split(',')[0].split(']')[0]) + '\n'
                    except:
                        pass
            except:
                pass
    return st


li = []
while True:
    print('Input > ', end='')
    wd = input()
    if wd == '':
        break
    li.append(wd)

print('처리 중...')

for wd in li:
    csv = open('test.csv', 'a', encoding='utf-8')
    csv.write(crawlWord(wd))
    csv.close()
