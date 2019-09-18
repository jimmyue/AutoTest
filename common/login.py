import requests
import lxml.html
import json

class login:
	def __init__(self,username,password):
		self.username=username
		self.password=password

	def SGM_Cookie(self,module):
		#需输入账号、密码、模块名称（每个模块Cookie是单独的）
		headers = {
		"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
		"Accept-Encoding": "gzip, deflate",
		"Accept-Language": "zh-CN,zh;q=0.9",
		"Cache-Control": "no-cache",
		"Connection": "keep-alive",
		"Cookie": "",
		"Upgrade-Insecure-Requests": "1",
		"User-Agent": "Mozilla/5.0"
		}

		url_login ='http://telecom.thinktanksgmmd.com/login?service=http%3A%2F%2Fweb.thinktanksgmmd.com%2F{}%2Fj_spring_cas_security_check'.format(module)
		response = requests.session()
		req = response.get(url_login)
		html_content = req.text
		login_html = lxml.html.fromstring(html_content)
		#获取表单form，并加入账号密码
		hidden_inputs=login_html.xpath(r'//*[@id="loginForm"]/input[@type="hidden"]')
		user_form = {x.attrib["name"] : x.attrib["value"] for x in hidden_inputs}
		user_form["username"]=self.username
		user_form["password"]=self.password
		headers['Cookie'] = req.headers['Set-cookie']
		#cas登录认证，获取ticket
		responseRes=response.post(req.url, data=user_form, headers=headers, allow_redirects=False)
		service_url=responseRes.headers['Location']
		#获取带ticket的模块URL
		module=response.get(service_url,headers=headers, allow_redirects=False)
		module_url=module.headers['Location']
		#通过票据获取模块Cookie
		endall=response.get(module_url,headers=headers, allow_redirects=False)
		return endall.headers['Set-Cookie']

	def IWAY_Token(self):
		url='http://i.way-s.cn/api/cas-server/doLogin'
		data=json.dumps({"data":{"username":self.username,"password":self.password}})
		headers={"Content-Type":"application/json"}
		response = requests.request("POST",url,data=data,headers=headers)
		r=response.json()
		return r["data"]["token"]

	def GTIDS_Token(self):
		url='http://ids.waysdata.com/api/auth/login'
		parameter={"userName":self.username,"password":self.password}
		response = requests.request("POST", url, params=parameter)
		r=json.loads(response.text)
		return r['data'][0]['token']

if __name__ == "__main__":
	#SGM验证
	cookies=login('sgmm','1').SGM_Cookie('economic')
	sgm_headers={'Cookie':cookies}
	economic_url='http://web.thinktanksgmmd.com/economic/marketPopularity/getMarketPopularityEchartData.do?level=2&levelId=1&levelPid=1&year=2019&month=8&week=1&areaId=-1&type=4&popularityType=0'
	response = requests.get(url=economic_url, headers=sgm_headers)
	print('SGM接口：',response.text)

	#IWAYS验证
	token=login('itways','itways.abc').IWAY_Token()
	iway_headers={'token':token}
	iway_url='http://i.way-s.cn/api/segment-forecast/forecast-overview/get-attention-segment-list'
	iways_Params={"sourceType":"segment_xiaoliang","ymId":"201906"}
	response = requests.get(url=iway_url,params=iways_Params,headers=iway_headers)
	print('\nIWAY接口：',response.text)

	# #GTIDS验证
	token=login('888888@11A90','119024').GTIDS_Token()
	print('\nGTIDS登录:',token)