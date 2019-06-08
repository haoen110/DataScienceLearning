import urllib.request

url = "https://ban-fang.jiyoujia.com/category.htm?"
headers = {
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
'accept-language': 'zh-CN,zh;q=0.9',
'cache-control': 'max-age=0',
'cookie': 'hng=CN%7Czh-CN%7CCNY%7C156; dnk=haoen110; uc1=cookie16=V32FPkk%2FxXMk5UvIbNtImtMfJQ%3D%3D&cookie21=URm48syIZJwTkNGk7euL6g%3D%3D&cookie15=W5iHLLyFOGW7aA%3D%3D&existShop=false&pas=0&cookie14=UoTZ7Yt2DGXeKQ%3D%3D&tag=8&lng=zh_CN; tracknick=haoen110; lid=haoen110; _l_g_=Ug%3D%3D; unb=739405758; cookie1=ACO%2F0E4AcXJMP0GSGoTa6igaASEQhEJKBlKjlXBt974%3D; login=true; cookie17=VAKEwuppvz3m; cookie2=13e9e81854e72c7686cf874ba147a4bc; _nk_=haoen110; t=d51a5ba7a02f8a1f94cfe5fa70c779cf; sg=084; csg=d72981ff; _tb_token_=3b31ea01e1b4e; cna=/dFbFR5ZewwCAXr2kjvQI2ni; pnm_cku822=098%23E1hvMvvUvbpvUpCkvvvvvjiPRLchsjY8RsLWzj3mPmPv0j3CR2FZgjt8n2SOAjEVnfyCvm9vvvmbphvvvvvv9DCvpvFqvvmmZhCv2CUvvUEpphvWrpvv9DCvpvAluphvmvvv9bx2TiIfkphvC99vvOHzpQyCvhQWWwhvClsUlj7Q%2BulApjc6D76XVB60kUkQD46XaoF6fc7Q%2BulAB5c6Qbm655H2znsU%2B2Kz8Z0vQRAn%2BbyDCwsIAXZTKFEw9Exr1CKKvphvC9vhvvCvpvGCvvpvvvvvRphvCvvvvvm5vpvhvvmv99%3D%3D; l=bBjyC6g7vtllI0VyKOCg5uI8Us79sIRAIuPRwd0Xi_5IM6L1kAQOlHrH8Fp62j5RsqYB4V0hhnv9-etXi; isg=BD4-RgoZ7gdFwDojadrz6Kb9j1JA1wCR0kfIDehHqQF8i95lUA2WCdlpBhfikvoR',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}

req = urllib.request.Request(url, headers=headers)
res = urllib.request.urlopen(req)
print(res.read().decode('gb18130'))
