# 023deco.py
# 银行业务：
# 	存钱：savemoney
# 	取钱：withdraw
# 1.添加一个余额变动提醒功能
def message_send(fn):
	def fx(name, x):
		print('发送消息:', name, '来银行办理业务...')
		fn(name, x)
		print('发送消息', name, '办理了', x, '元的业务')
	return fx
# 2.加一个权限验证功能的装饰器

def privileged_check(fn):
	def fx(name, x):
		print("Checking...")
		if True:
			fn(name, x)
	return fx

@privileged_check
@message_send
def savemoney(name, x):
	print(name, '存钱', x, '元')

def withdraw(name, x):
	print(name, '取钱', x, '元')

savemoney('小李', 200)
