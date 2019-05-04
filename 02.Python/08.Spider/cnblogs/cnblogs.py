import urllib.request

url = "https://home.cnblogs.com/u/haoenwei/"
headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
'accept-language': 'zh-CN,zh;q=0.9',
'cache-control': 'max-age=0',
'cookie': '_ga=GA1.2.1949465555.1540625634; __gads=ID=953adc9bf2894fc4:T=1540625634:S=ALNI_MaE78JA-b20R5Gn2VWtuI0ECfxKVQ; UM_distinctid=167253848297ee-0749c0539596fc-35677407-13c680-1672538482b1044; __utmz=226521935.1555300815.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=226521935.1949465555.1540625634.1555300815.1555300814.1; .CNBlogsCookie=7DB75DE6417AA8E1B577445D662056E408ECAB2BC997E70F40FA5F1D17F0F86B623859E2CA98AC95F6AB41DEFB8536BAAC99BE9D6C09357D2053AEF5DC4B8B9AACF361657B24BA3D626A9632E85D41DE256D6E9A; .Cnblogs.AspNetCore.Cookies=CfDJ8JcopKY7yQlPr3eegllP76OxzUYdIv57u8kFIlVyiMda8XU4fciX_2hmaIN2Rm7W1VCENcn6Oodoexxt6J2VnAt6tfYUhWBrdG1RjzXZHP5U98Xgc5qxUmy_0MRS3McWZN6GiZAB0laOdaoaKVQyaOD9AZo1J9nFaR2yXmKpKPLOqHNIdbVkz7C7VE7y3J7qtBtu2rL1AgfnzadEBQEByKt6Iuijx-28gUAlZrJ4aaSHDv7ZweNHk03Lt_QHlnyAro6vKoAFmxRKCa8_XYFQiuz-y4qCtK8PPSSVFBenhUcVR_3qE8YyF2FRvRYSNirDJQ; _gid=GA1.2.2057231269.1556932274',
'referer': 'https://home.cnblogs.com/set/account/',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}

req = urllib.request.Request(url, headers=headers)
res = urllib.request.urlopen(req)
print(res.read().decode())
