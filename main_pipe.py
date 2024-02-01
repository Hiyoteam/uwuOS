# -*- coding: UTF-8 -*-


# 地址列表:HackChat ZhangChat
hc="wss://hack.chat/chat-ws"
zhc="wss://chat.zhangsoft.cf/ws"

# 频道列表:yc ycl warma chat DHQZ
yc="your-channel"
ycl="your-channell"
warma="kt1j8rpc"
chat="chat"
DHQZ="DHQZ"

# 加入地址&频道
chatroom=[(hc,"114"),(hc,yc),(hc,"114514")]

# bot昵称:uwuOS
botnick="uwuOS"

# bot密码:——
botpass="rv4K/N|dtfD-P\\ud!7:19pw"

# 权限识别码:eYFDHl ejackX uwuu57
root=["eYFDHl","ejackX","uwuu57","Zhang+"]

# 三字母颜文字:uwu uvu ouo
emote=["uwu","uvu","ouo"]


'''
[主要代码]
若要修改请慎重(掀桌
'''

# 导入一堆库
from time import time,sleep,strftime,localtime
from json import dumps,loads
from random import choice,randint,shuffle
from os import execl
from threading import Thread
from websocket import WebSocket
from codecs import open
from sys import executable,argv,exit

# file:文件名 mode:模式 text:内容
def save(file,mode,text):
	with open(file,mode,"UTF-8-sig") as file_:
		file_.write(text)

# file:文件名
def load(file):
	return open(file,"r","UTF-8-sig").read()

# nick:昵称 state:状态
def chan(nick,state=False):
	data["state"][state].append(data["state"][not state].pop(data["state"][not state].index(nick)))
	data["core"][nick][3]=state

	if data["push"]["wolf"] and not state and nick in data["msg"]:
		sleep(1)
		send(False,f"这时 [{nick}]{choice(general[9])}的遗言被发现了\n[{nick}]：[{data['msg'][nick]}]")

# 随机取牌
def roll():
	return data["all"].pop(data["all"].index(choice([_ for _ in data["all"] if _])))

# game:游戏 state:状态
def end(game,state=False):
	global data

	for _ in list(set(data["trip"][1:])):
		notlife[1][_][0][2]+=randint(1,999)
		notlife[1][_][1][data["trip"][0]]+=1

	data={"push":{**data["push"],game:state}}

# name:变量名 nick:昵称
def var(name,nick):
	list_=globals()

	if name=="botpass":
		send(room,f"botpass:Never_Gonna_Give_You_Up",nick,False)

	else:
		for uwu_,_uwu in list(list_.items()):
			if uwu_==name:
				print(f"{uwu_}:{_uwu}\n")
				send(room,f"{uwu_}:{_uwu}",nick,False)

# nick:昵称 num:数量 state:状态
def add(nick,num=1,state=False):
	temp=str()

	for _ in range(num):
		if not data["all"]:
			sleep(1)
			send(False,f"Oops! 已经没有闲置牌了 添牌失败")
			break

		else:
			r=choice(data["all"])
			temp+=f"[{paper['sp']}] " if not r else f"[{paper['first'][r[0]]+paper['last'][r[1]]}] "
			data["core"][nick].append(data["all"].pop(data["all"].index(r)))

	if state and temp:
		sleep(1)
		send(False,f"·\n新增的牌：\n{temp}",nick)

# nick:昵称 card_:卡牌 state:状态
def rm(nick,card_,state=False):
	data["all"].append(data["core"][nick].pop(data["core"][nick].index(card_)))
	data["now"][0]=card_ if state else data["now"][0]

# nick:昵称
def next_(nick,state=True):
	note=data["temp"][(0 if data['temp'].index(nick)+1==len(data["temp"]) else data['temp'].index(nick)+1) if data["order"] else (-1 if not data['temp'].index(nick) else data['temp'].index(nick)-1)]
	data["now"][-1]=note if state else data["now"][-1]

	if not data["temp"].index(data["now"][-1]):
		data["round"]+=1
		send(False,f"回合[{data['round']}] 继续")

	if state:
		note_="["+"] [".join([(paper['first'][_[0]]+paper['last'][_[1]] if _ else paper["sp"]) for _ in data["core"][note]])+"]"
		send(False,f"·\n你的卡牌：\n{note_}",note)

	return note

# time_:等待时长
def rb(time_=30):
	sleep(time_)
	execl(executable,executable,*argv)

# mode:模式(0:存 1:读)
def life(mode=1):
	if mode:
		uwu_=load("notlife.txt").split("\n·\n")
		_uwu=[{},{}]

		try:
			for uwu in uwu_:
				for _ in uwu.split("\n"):
					note=_.split("  ")
					note_=note[0].split(" ")
					_uwu[uwu_.index(uwu)][note_[1] if uwu_.index(uwu) else note[1]]=[[*note_[:2],int(note_[2])],[int(_) for _ in note[1].split(" ")],note[2].split(" ")] if uwu_.index(uwu) else [*note[:3],int(note[3]),int(note[4])]

		except:
			print("data:error\n")

		return _uwu

	else:
		note=[]

		for uwu in notlife:
			for _ in uwu.values():
				note.append("  ".join([" ".join([str(___) for ___ in __]) if notlife.index(uwu) else str(__) for __ in _]))

			notlife.index(uwu) or note.append("·")

		save("notlife.txt","w","\n".join(note))

# trip:识别码
def pull(nick,trip,eb=0):
	if trip not in notlife[1]:
		notlife[1][trip]=[[nick,trip,eb],[0,0,0,0,0],[strftime("%Y.%m.%d",localtime())]]

	else:
		notlife[1][trip][0][0]=nick
		notlife[1][trip][0][2]+=randint(eb,eb+11)

# 主要数据库
data={"push":{"truth":False,"grass":False,"wolf":False,"uno":False,"guess":False}}

# root权限列表
rootlist=load("roottriplist.txt").split("\n")

# 真心话 提问
change=[False,["大","小"]]

# 生草机 词库
sbres=[_.split("\n") for _ in load("sbres.txt").split("\n·\n")]

# 狼人杀 卡牌列表
card={0:{True:"好人",False:"坏人"},
1:["平民","夜晚：注意旁白 安静等待\n白天：提出意见 跟随大家投票",True],
2:["预言家","夜晚：选择一位得知身份\n白天：领导大家投票",True],
3:["狼人","夜晚：选择一位杀死\n白天：隐藏身份 跟随大家投票",False],
4:["女巫","夜晚：选择一位使用药水 每种药只能使用一次\n白天：隐藏身份 跟随大家投票",True]}

# 狼人杀 药水列表
potion={True:["解药","救活"],False:["毒药","毒死"]}

# 狼人杀 初始牌组
group=[1,1,2,3,3,4]

# 狼人杀 剧情词组:通用
general=[["选择","决定","打算","想要"],
["断了气","没了动静","停了心跳","一命呜呼"],
["深夜","半夜三更","凌晨两点","午夜时分","公鸡打鸣","星云服务器降价"],
["失去理智","愤愤不平","闹腾","愤怒"],
["绿色","白色","翻折","皱巴巴","缺了角","不正经","整齐叠好","像23屎一样"],
["收回伸出纸片的手","不知如何抉择","有些迷茫","仔细思考"],
["来到","误入","闯入","跳进","飞进","滚进","骑着23闯入","踩着23走进","在地下吃出一条地道吃入"],
["欺负","诅咒","戏弄","鞭尸"],
["飘走了","被烧了","被偷走了","被捡走了","不翼而飞","被拼多多给骗了","被星云当服务器了","把23拿去擦屁股了"],
["家里","身上","背后","手中","肚子里","保险箱中","午餐盒中","马桶水箱里"],
["奇妙","危险","美丽","美好","23被揍","23被群殴"]]

# 狼人杀 剧情词组:预言家
prophet=[["犯了心肌梗塞","脑子不太清醒","撞到了头","被水晶球反噬","摔了一跤"],
["叹了口气","沉默不语","喃喃自语","摇了摇头"],
["陷入沉思","不敢置信","瞪大了双眼","惊掉了下巴","大喊一声woc","大喊一声mb"],
["熟","甜","香","舒服"],
["没有回应","没有行动","家里没人","不在家中","去保养水晶球了"]]

# 狼人杀 剧情词组:狼人
werewolf=[["惨叫","哀嚎","悲鸣","呜咽"],
["被撕咬过","不成样","四分五裂","难以辨认","像23死亡时惨状"],
["呼唤同伴","追赶","奔走","嬉闹"],
["迷路","走丢","离群","去找对象"],
["或许是想赌一把","真有心机呢","这样好吗","这样可以吗"],
["做可以吗","真的好吗","是在协助吗","有没有好处"],
["伤心欲绝","重情重义","讲义气","悲伤"],
["沉思中","略显憔悴","望向远方","不太坚定"]]

# 狼人杀 剧情词组:女巫
witch=[["压缩纸片","让自己变性","让星云降价","让鱼变好吃","自动写代码","让预言家的水晶球出现rickroll"],
["死一般的寂静","看似一派祥和","已经没有人影了","偶有远处的呼喊","播放着rickroll"],
["无声","安静","静悄悄","悄无声息"],
["大声","开心","神秘","诡异"],
["想要休息","不知所踪","的纸片丢失了","的小屋无人打扫","的家中只有一台循环rickroll的电脑"]]

# UNO 卡牌列表
paper={"first":["黄","绿","蓝"],"last":["禁","转","+1","+2",*[str(_) for _ in range(9)][::2]],"sp":"变色"}

# 猜数字 范围
guess=[1,9]

# 不是生活 数据
notlife=life()

# 欢迎语
welcome=["每天都要开开心心！","勇敢面对生活吧！","征途的前方是星辰大海","欢迎来到温暖的聊天室","愿你能被温柔以待"]

# bot实际名
botname=f"{botnick}_{str(randint(1,999)).zfill(3)}"

# 互通管子
pipe={"chatroom":[],"data":[]}

# text:内容
def send(room,text,nick=None,light=True):
	text=str(text).replace("]","](https://)") if light else f"`{text}`"
	text_=text if text in [*emote,"success","failure"] else f">\n{text}"

	data_=dumps({"cmd":"whisper","nick":nick,"text":text_} if nick else {"cmd":"emote","text":text_})

	if isinstance(room,int):
		pipe["chatroom"][room].send(data_)

	else:
		for uwu in pipe["chatroom"]:
			uwu.send(data_)

# socket:地址 channel:频道
def join(socket,channel):
	try:
		ws=WebSocket()
		ws.connect(socket)
		print(f"{socket}/{channel}\n")

		id_=pipe["chatroom"]
		pipe["chatroom"].append(ws)

		sleep(0.5)
		ws.send(dumps({"cmd":"join","channel":channel,"nick":botname,"password":botpass,"client":"papereescomputer","murmur":"/bi5lWkmPbUMF96kWJXoBsIU9opk36B2zK6xUtg87cWJavnaxRrKMhxwzVf6eAxG"}))

	except:
		rb()

	while True:
		try:
			temp_=loads(ws.recv())
			temp_["room"]=id_
			pipe["data"].append(temp_)
		
		except:
			rb()

		sleep(0.5)

for data_ in chatroom:
	
	Thread(target=join,args=data_).start()
	sleep(60)

while True:
	if pipe["data"]:
		ouo=pipe["data"][0]

		if "cmd" in ouo:
			cmd=ouo["cmd"]
			room=ouo.get("room")

			if cmd=="onlineAdd":
				sleep(0.5)
				nick=ouo["nick"]
				trip=ouo.get("trip")
				date_=strftime("%Y.%m.%d",localtime())

				try:
					if trip and trip!="null" and date_ not in notlife[1][trip][2][1:]:
						send(room,f"hi yo [{nick}]\n今天是[{date_}] 使用`|sign`签到吧\n更多使用方法 请发送：`|help`",nick)

					else:
						send(room,f"hi yo [{nick}]\n{choice(welcome)} {choice(emote)}",nick)

				except:
					pass

			if cmd=="chat":
				sleep(0.5)
				nick=ouo["nick"]
				text=ouo["text"]
				trip=ouo.get("trip")

				if trip and trip!="null":
					slices=text.split()
					pull(nick,trip)

					if slices[0]=="|data":
						date_=" ".join(notlife[1][trip][2][1:]) or "未签到过"
						send(room,f"·\n游戏次数({sum(notlife[1][trip][1])})：\n真心话：{str(notlife[1][trip][1][0]).zfill(3)}\n生草机：{str(notlife[1][trip][1][1]).zfill(3)}\n狼人杀：{str(notlife[1][trip][1][2]).zfill(3)}\nUNO：{str(notlife[1][trip][1][3]).zfill(3)}\n猜数字：{str(notlife[1][trip][1][4]).zfill(3)}\n·\n签到状况({len(notlife[1][trip][2][1:])})：\n{date_}",nick)

					elif slices[0]=="|pack":
						if slices[-1]=="list":
							send(room," ".join(notlife[1]))

						elif slices[-1] not in notlife[1] and slices[-1]!="|pack":
							send(room,choice(emote))

						else:
							trip_=slices[-1] if slices[-1] in notlife[1] else trip
							note=[f"[{uwu[1]}]：[{uwu[2]}] 价值|[{uwu[3] or 'Null'}]eb" for uwu in notlife[0].values() if uwu[0]==trip_ and not uwu[4]]
							note_="\n".join(note) or ("无 你可以选择买入或制作物品" if trip_==trip else "TA的背包空空如也")
							send(room,f"·\n识别码：[{trip_}]\n昵称：[{notlife[1][trip_][0][0]}]\n纸币：[{notlife[1][trip_][0][2]}]eb\n加入日期：{notlife[1][trip_][2][0]}\n·\n物品列表({len(note)})：\n{note_}"+(f"\n·\n背包操作：\n制作：`/w {botname} make(换行)物品名 说明 价值`\n给予：`/w {botname} give(换行)物品名 识别码`\n上架：`/w {botname} sell(换行)物品名 价值`\n丢弃：`/w {botname} del(换行)物品名`" if trip_==trip else ""),nick)

					elif slices[0]=="|shop":
						note=[f"[{uwu[1]}]：[{uwu[2]}] 来自|[{notlife[1][uwu[0]][0][0]}] 价值|[{uwu[3] or 'Null'}]eb" for uwu in notlife[0].values() if uwu[4]]
						note_="\n".join(note) or "这里什么都没有 要不要卖点东西？\n查看背包物品请用`|pack`"
						send(False,f"·\n物品列表({len(note)})：\n{note_}\n·\n商店操作：\n买入：`/w {botname} buy(换行)物品名`")

					elif slices[0]=="|sign":
						date_=strftime("%Y.%m.%d",localtime())

						if date_ in notlife[1][trip][2][1:]:
							send(room,choice(emote))

						else:
							weekday=int(date(int(strftime("%Y")),int(strftime("%m")),int(strftime("%d"))).weekday())+1
							plus=weekday*100
							notlife[1][trip][2].append(date_)
							notlife[1][trip][0][2]+=plus
							dker=[_ for _ in notlife[1].values() if date_ in _[2][1:]]

							send(False,f"[{nick}]是今天第[{len(dker)}]个签到的\n今天是星期[{weekday}] 获得[{plus}]eb")

					life(0)

				if f"@{botnick}" in text:
					send(room,choice(emote))

				elif text[:5]=="|root":
					if trip in root+rootlist:
						try:
							slices=[_.split() for _ in text.split("\n")]
							order=slices[0][1 if len(slices[0])>1 else 0]

							if order=="-rl":
								var(slices[0][-1],nick)

							elif order=="-rb":
								print("reboot:success\n")
								rb(1)

							elif order=="-cl":
								print("close:success\n")

								sleep(1)
								ws.close()
								break

							elif order=="-ad":
								for _ in slices[1]:
									if len(_)==6:
										rootlist.append(_)

							elif order=="-dl":
								for _ in slices[1]:
									rootlist.pop(rootlist.index(_))

							elif order=="-cr":
								rootlist=[]

							elif order=="-T":
								order_=slices[0][-1]

								if order_=="-ch":
									change=[bool(int(slices[1][0])),["小","大"] if slices[1][0] else ["大","小"]]

								else:
									send(room,f"·\n可变更项：\n规则(-ch)\n·\n变更说明：\n规则：调换顺序(1/0) *最小→最大/最大→最小",nick)

							elif order=="-W":
								order_=slices[0][-1]

								if order_=="-cd":
									for _ in slices[1:]:
										if 0<int(_[0])<=4:
											card[int(_[0])]=[_[1],card[int(_[0])][1],bool(int(_[2]))]

								elif order_=="-cp":
									card[0]={True:slices[1][0],False:slices[1][1]}

								elif order_=="-po":
									for _ in slices[1:]:
										potion[bool(int(_[0]))]=[*_[1:]]

								elif order_=="-gp":
									group=sorted([int(_) for _ in slices[1] if _ in list("1234")])
									note="下轮"

									if data["push"]["wolf"] and not data["core"] and len(group)>=len(data["temp"]):
										data["group"]=group
										note="本局"

									send(room,f"{note}卡牌设置({len(group)}人局)：\n1.[{card[1][0]}]x{group.count(1)}\n2.[{card[2][0]}]x{group.count(2)}\n3.[{card[3][0]}]x{group.count(3)}\n4.[{card[4][0]}]x{group.count(4)}")

								else:
									send(room,"·\n可变更项：\n卡牌(-cd) 阵营(-cp) 药水(-po) 牌组(-gp)\n·\n变更说明：\n卡牌：牌序(1~4) 牌名(str) 阵营(1/0)\n阵营：正方阵营名(str) 反方阵营名(str)\n药水：好坏(1/0) 药名(str) 状态(str)\n牌组：牌序(1~4)",nick)

							elif order=="-U":
								order_=slices[0][-1]

								if order_=="-ft":
									if len(slices[1][0])==4:
										paper["first"]=list(slices[1][0])

								elif order_=="-lt":
									if len(slices[1])==2:
										for _ in len(slices[1]):
											paper["last"][_]=slices[1][_]

								else:
									send(room,"·\n可变更项：\n前置名(-ft) 后置名(-lt)\n·\n变更说明：\n前置名：颜色(x4) 后置名(禁&转)",nick)

							elif order=="-L":
								order_=slices[0][-1]

								if order_=="-pk":
									for _ in slices[1:]:
										notlife[0][_[1]]=[*_[:3],int(_[3]),int(_[4])]

								elif order_=="-eb":
									for _ in slices[1:]:
										pull(_[0],_[1],int(_[2]))

								else:
									send(room,"·\n可变更项：\n物品(-pk) 纸币(-eb)\n·\n变更说明：\n物品：识别码(str) 物品名(str) 说明(str) 价值(int) 是否上架(1/0)\n纸币：昵称(str) 识别码(str) 纸币(int)",nick)

							elif order=="-N":
								order_=slices[0][-1]

								if order_=="-rg":
									guess=[int(slices[1][0]),int(slices[1][1])]

								else:
									send(room,"·\n可变更项：\n范围(-rg)\n·\n变更说明：\n范围：最小(int) 最大(int)",nick)

							else:
								note="·\n可操作项：\n查看数据(-rl) 重启(-rb) 关机(-cl)\n·\n权限相关：\n添加root(-ad) 移除root(-dl) 清空root(-cr)\n·\n游戏相关：\n真心话(-T) 狼人杀(-W) UNO(-U) 不是生活(-L) 猜数字(-N)"
								send(room,note,nick)

							rootlist=list(set(rootlist))
							save("roottriplist.txt","w","\n".join(rootlist))
							send(room,f"success")

						except:
							send(room,f"failure")

					else:
						send(room,choice(emote))

				elif text[:5]=="|help":
					slices=text.split()

					if slices[-1]=="truth":
						send(room,f"·\n使用方法：\n获取随机数：`r`\n结算数据：`|ctrl`\n结束游戏：`|over`\n·\n注意事项：\n由数字最{change[1][0]}的向数字最{change[1][1]}的提问\n尊重隐私 请勿提问过分露骨的问题\n愿赌服输 请说真心话(有权拒绝回答隐私问题)")

					elif slices[-1]=="grass":
						send(room,f"·\n限制时长：\n[开头]1分钟\n[续写]2分钟\n超时由{botnick}代写\n·\n使用方法：\n报数加入：`1`\n查看进度：`|info`")

					elif slices[-1]=="wolf":
						true="".join([f" [{card[_][0]}]" for _ in card if _ and card[_][-1]])
						false="".join([f" [{card[_][0]}]" for _ in card if _ and not card[_][-1]])
						send(room,f"·\n主要卡牌：\n{true}/[{card[0][True]}]\n{false}/[{card[0][False]}]\n·\n卡牌设置({len(data.get('group',group))}人局)：\n[{card[1][0]}]x{data.get('group',group).count(1)}\n[{card[2][0]}]x{data.get('group',group).count(2)}\n[{card[3][0]}]x{data.get('group',group).count(3)}\n[{card[4][0]}]x{data.get('group',group).count(4)}\n·\n限制时长：\n[{card[2][0]}]1分钟\n[{card[3][0]}]2分钟\n[{card[4][0]}]1分钟\n白天投票共3分钟\n超时则踢出村子\n·\n使用方法：\n报数加入：`1`\n查看卡牌：`|info`")

					elif slices[-1]=="uno":
						send(room,f"·\n限制时长：\n每人1分钟\n·\n使用方法：\n报数加入：`1`\n打出卡牌：`u 卡牌`\n跳过出牌：`u .`\n查看卡牌：`|info`")

					else:
						send(room,f"·\n机器人：[{botnick}]\n开发者：[paperee]([ee]) [jiangmuran]([jmr])\n适用地：[HackChat] [ZhangChat]\n·\n使用手册：\n个人数据：`|data`\n打开背包：`|pack 识别码`\n打开商店：`|shop`\n获取权限：`|root`\n查看帮助：`|help 游戏`\n开始游戏：`|play 游戏`\n·\n可选游戏：\n真心话(truth) 生草机(grass) 狼人杀(wolf) UNO(uno)")

				elif text[:5]=="|play":
					slices=text.split()

					if any(data["push"].values()):
						send(room,choice(emote))

					else:
						if slices[-1]=="truth":
							data={**data,"round":1,"core":[],"num":[],"trip":[0]}
							send(False,f"[真心话]开始 请用`r`获取随机数")

						elif slices[-1]=="grass":
							data={**data,"temp":[],"core":False,"msg":[],"trip":[1]}
							send(False,f"开始清点[生草机]人数 请用`1`报数")

						elif slices[-1]=="wolf":
							data={**data,"owner":nick,"group":group,"round":0,"temp":[],"core":{},"state":{True:[],False:[]},"sudden":[],"prophet":[],"werewolf":{"skip":False,"core":[],"wait":[],"kill":[],"dead":[]},"witch":{"med":{True:[True,True],False:[False,True]},"temp":[],"allow":[]},"day":{"wait":[],"kill":[],"dead":[]},"msg":{},"now":[],"trip":[2]}
							send(False,f"新的[村长]诞生了 {choice(general[10])}的夜晚要开始了")

							sleep(1)
							note=" ".join([str(_) for _ in group])
							send(False,f"·\n[村长][{nick}]\n现在你可以选择改变牌组 否则为默认\n·\n卡牌详情：\n1.[{card[1][0]}]\n2.[{card[2][0]}]\n3.[{card[3][0]}]\n4.[{card[4][0]}]\n·\n默认牌组({len(group)}人局)：\n{note}\n·\n设置方法：\n`/w {botname} 牌组`",nick)

							sleep(0.5)
							send(False,f"[村长]开始清点村里人数 请用1报数")

							# 主循环
							def loop():
								while True:
									if data["push"]["wolf"] and len(data["temp"])==len(data["group"]):
										data["notice"]="@"+" @".join(data["temp"])+" "
										data["time"]=round(time())
										send(False,f"{data['notice']}\n人数到齐 开始抽牌 请注意查看私聊")

										try:
											shuffle(data["temp"])

											for _ in data["temp"]:
												note=data["group"][data["temp"].index(_)]
												data["core"][_]=[_,note,card[note][2],True]

												sleep(1)
												send(False,f"·\n你的卡牌：\n[{card[note][0]}]/[{card[0][card[note][2]]}]\n·\n你的任务：\n{card[note][1]}\n·\n获胜条件：\n[{card[0][not card[note][2]]}]全员阵亡\n·\n设置遗言(死亡前有效)：\n`/w {botname} msg(换行)遗言`",_)

										except:
											for _ in data["temp"][len(data["group"])-1:]:
												data["temp"].pop(data["temp"].index(_))

										sleep(2)
										send(False,f"发牌完毕 [狼人杀]正式开始")
										break

									else:
										sleep(2)

								while True:
									data["round"]+=1
									data["werewolf"]["skip"]=False
									data["witch"]["temp"]=[]
									data["day"]={**data["day"],"wait":[],"kill":[]}

									note=list(data["core"].values())
									data["state"]={True:[_[0] for _ in note if _[3]],
									False:[_[0] for _ in note if not _[3]]}

									sleep(4)
									send(False,f"回合[{data['round']}] 天黑请闭眼")

									for uwu in note:
										if uwu[1]==2:
											if uwu[3]:
												sleep(2)
												send(False,f"[{card[2][0]}]No.{str(randint(1,999)).zfill(3)}请睁眼")

												alive=[_ for _ in data["state"][True] if _!=uwu[0]]
												shuffle(alive)
												uwu_="["+"] [".join(alive)+"]"
												_uwu="\n"+"\n".join([f"[{card[data['core'][_][1]][0]}]/[{card[0][data['core'][_][2]]}] [{_}]" for _ in data["prophet"]])

												data["now"]=[*uwu[:2][::-1]]

												sleep(1)
												send(False,f"·\n[{card[2][0]}]/[{card[0][True]}] [{uwu[0]}]\n现在你可以选择一位对象得知身份\n请在1分钟内做出选择\n·\n已知身份：\n你自己{_uwu}\n·\n选择方法：\n`/w {botname} 对象`\n·\n可选对象：\n{uwu_}",uwu[0])

												for _ in range(60):
													sleep(1)

													if data["now"][0]!=uwu[1]:
														break

												else:
													chan(uwu[0])
													data["sudden"].append(uwu[0])

													sleep(1)
													send(False,f"[{card[2][0]}][{uwu[0]}]在今晚{choice(general[1])} 突然猝死")

											else:
												sleep(randint(10,20))
												send(False,f"[{card[2][0]}]{choice(prophet[4])}")

										elif uwu[1]==3 and not data["werewolf"]["skip"]:
											if uwu[3]:
												sleep(2)
												send(False,f"[{card[3][0]}]们请睁眼")

												alive=data["state"][True][:]
												shuffle(alive)
												uwu_="["+"] [".join(alive)+"]"

												note=[_ for _ in data["core"] if data["core"][_][1]==3 and data["core"][_][3]]
												data["werewolf"]={"skip":True,"core":note,"wait":note,"kill":[],"dead":data["werewolf"]["dead"]}
												data["now"]=[uwu[1],data["werewolf"]["core"]]

												for _ in data["werewolf"]["core"]:
													_uwu=" ".join([f"[{__}]" for __ in data["werewolf"]["core"] if __!=_])

													if _uwu:
														_uwu=f"\n·\n你的同伴：\n{_uwu}"

													sleep(1)
													send(False,f"·\n[{card[3][0]}]/[{card[0][False]}] [{_}]\n现在你可以选择一位对象杀死\n狼群只有意见统一才会行动\n请在2分钟内做出选择{_uwu}\n·\n选择方法：\n`/w {botname} 对象`\n·\n可选对象：\n{uwu_}",_)

												for _ in range(120):
													sleep(1)

													if data["now"][0]!=uwu[1]:
														break

												else:
													for _ in data["werewolf"]["core"]:
														if _ not in data["werewolf"]["wait"]:
															sleep(1)
															send(False,f"今晚你的同伴猝死了\n{choice(werewolf[6])}的狼群忙于为TA送葬 没有行动",_)

													for _ in data["werewolf"]["wait"]:
														chan(_)
														data["sudden"].append(_)

														sleep(1)
														send(False,f"[{card[3][0]}][{_}]在今晚{choice(general[1])} 突然猝死")

											else:
												sleep(randint(10,20))
												send(False,f"狼群中的狼{choice(werewolf[7])}")

										elif uwu[1]==4:
											if uwu[3]:
												sleep(2)
												send(False,f"[{card[4][0]}]No.{str(randint(1,999)).zfill(3)}请睁眼")

												data["witch"]={"med":data["witch"]["med"],"temp":[],"allow":[]}
												med=[_ for _ in data["witch"]["med"] if data["witch"]["med"][_][1]]

												if med:
													data["now"]=[*uwu[:2][::-1]]
													dead=[_ for _ in data["state"][False] if _ not in data["sudden"]]
													alive=[_ for _ in data["state"][True] if _!=uwu[0]]

													uwu_=" ".join([f"[{potion[data['witch']['med'][_][0]][0]}]" for _ in med if data['witch']['med'][_][1]])
													_uwu=str()

													if dead and True in med:
														data["witch"]["allow"].extend(dead)
														shuffle(dead)
														_uwu+="\n可救：["+"] [".join(dead)+"]"

													if alive and False in med:
														data["witch"]["allow"].extend(alive)
														shuffle(alive)
														_uwu+="\n可杀：["+"] [".join(alive)+"]"

													if not _uwu:
														_uwu="\n无 你可以等待回合跳过 或输入假对象名"

													sleep(1)
													send(False,f"·\n[{card[4][0]}]/[{card[0][False]}] [{uwu[0]}]\n现在你可以选择一位对象使用药水\n请在1分钟内做出选择\n·\n选择方法：\n`/w {botname} 对象`\n·\n所剩药水：\n{uwu_}\n·\n可选对象：{_uwu}",uwu[0])

													for _ in range(60):
														sleep(1)

														if data["now"][0]!=uwu[1]:
															break

													else:
														sleep(1)
														send(False,f"黑夜里 只剩[{card[4][0]}]四处飞行的身影")

												else:
													sleep(1)
													send(False,f"·\n[{card[4][0]}][{uwu[0]}]\n虽然轮到你行动 但你已经用完了药水",uwu[0])

													sleep(2)
													send(False,f"[{card[4][0]}]在研究能{choice(witch[0])}的药水")

											else:
												sleep(15)
												send(False,f"[{card[4][0]}]{choice(witch[4])}")

									sleep(4)
									send(False,f"回合[{data['round']}] 天亮了")

									alive=data["state"][True][:]
									shuffle(alive)
									uwu_="["+"] [".join(alive)+"]"
									_uwu=str()

									if not data["witch"]["temp"] or data["witch"]["temp"][-1]:
										_uwu="是一个平安夜\n"

									if isinstance(data["werewolf"]["kill"],str):
										_uwu=f"[{data['werewolf']['kill']}]被[{card[3][0]}]杀死了\n"

									if data["witch"]["temp"]:
										_uwu+=f"[{data['witch']['temp'][0]}]被使用[{potion[data['witch']['temp'][-1]][0]}]的[{card[4][0]}][{potion[data['witch']['temp'][-1]][1]}]了\n"

									sleep(2)
									send(False,f"[公告] 昨晚{_uwu}")

									data["stats"]=[[_ for _ in data["core"] if data["core"][_][2] and data["core"][_][3]],
									[_ for _ in data["core"] if not data["core"][_][2] and data["core"][_][3]]]

									if not all(data["stats"]):
										break

									data["now"]=[0,data["state"][True]]
									data["day"]={"wait":data["state"][True][:],"kill":[],"dead":data["day"]["dead"]}

									sleep(2)
									send(False,f"·\n投票环节：\n每人一票 得票数最高的[村民]会被处死\n请在3分钟内做出选择\n·\n选择方法：\n`/w {botname} 对象`\n·\n可选对象：\n{uwu_}\n*以上[村民]未死亡 且有票权")

									for _ in range(180):
										sleep(1)

										if not data["day"]["wait"]:
											break

										elif _==120:
											send(False,"白天仅剩1分钟了")

									else:
										for _ in data["day"]["wait"]:
											if data["core"][_][1]!=4:
												chan(_)
												data["sudden"].append(_)

												sleep(2)
												send(False,f"[{card[data['core'][_][1]][0]}][{_}]在白天{choice(general[1])} 突然猝死")

									if data["day"]["kill"]:
										sleep(2)
										note=max(set(data["day"]["kill"]),key=data["day"]["kill"].count)

										try:
											chan(note)
											data["day"]["dead"].append(note)
											send(False,f"[公告] 投票结果统计完成\n{choice(general[3])}的[村民]们处死了[{note}]")

										except:
											send(False,f"[公告] 投票结果统计完成\n{choice(general[3])}的[村民]们{choice(general[0])}处死[{note}]\n但当发现时 [{note}]已经猝死在家中了")

										alive=data["state"][True][:]
										shuffle(alive)
										uwu_="["+"] [".join(alive)+"]"

										sleep(2)
										send(False,f"目前留在村子里的人有：\n{uwu_}")

									data["stats"]=[[_ for _ in data["core"] if data["core"][_][2] and data["core"][_][3]],
									[_ for _ in data["core"] if not data["core"][_][2] and data["core"][_][3]]]
				
									if not all(data["stats"]):
										break

								sleep(4)
								winner=data["stats"].index([])

								if winner:
									send(False,f"不知什么时候 天气变得晴朗\n大家清楚地感受到 邪恶从村子里消失了")

								else:
									send(False,f"这个村子正在发生异变\n血色笼罩村庄 时不时传来邪恶的声音")

								uwu=[[f"[{_}]" for _ in data["stats"][not int(winner)]],
								[f"[{_}]" for _ in data["core"] if data["core"][_][2]==winner and not data["core"][_][3]],
								[f"[{_}]" for _ in data["core"] if data["core"][_][2]==(not winner)],
								[f"[{_}]" for _ in data["day"]["dead"]],
								[f"[{_}]" for _ in data["prophet"]],
								[f"[{_}]" for _ in data["werewolf"]["dead"]],
								[f"\n[{card[4][0]}][{potion[data['witch']['med'][_][0]][1]}]了：[{data['witch']['med'][_][-1]}]" for _ in data["witch"]["med"] if not data["witch"]["med"][_][1]]]

								note=[str() for _ in range(3)]
								test=[f"\n存活({len(data['stats'][not winner])})：",f"\n死亡({len(uwu[1])})：",f"\n死亡({len(uwu[2])})：",f"\n投票处死了：",f"\n[{card[2][0]}]知道了：",f"\n[{card[3][0]}]杀死了：",""]

								for _ in range(len(uwu)):
									if uwu[_]:
										note[0 if not _ else _-1 if _ in [1,2] else 2]+=test[0 if not _ else _ if _ in [1,2] else _]+" ".join(uwu[_])

								if note[2]:
									note[2]=f"\n·\n特殊数据：{note[2]}"

								minutes=divmod(round(time()-data["time"]),60)
								date_=strftime("日期：%Y.%m.%d",localtime())

								sleep(2)
								send(False,f"[{card[0][not winner]}]阵亡 [{card[0][winner]}]胜利")

								sleep(1)
								note_=f"·\n统计数据：\n{date_}\n时长：{minutes[0]}:{minutes[1]}\n回合数：{str(data['round']).zfill(3)}\n参与人数：{str(len(data['core'])).zfill(3)}\n·\n[{card[0][winner]}](胜){note[0]}\n·\n[{card[0][not winner]}](败){note[1]}{note[2]}"
								save("wolf.log","a+",note_.replace("·","")+"\n\n\n")
								end("wolf")
								send(False,note_)

								exit(0)

							# 开启多线程
							Thread(target=loop).start()

						elif slices[-1]=="uno":
							data={**data,"round":0,"temp":[],"core":{},"all":[],"now":[],"order":True,"trip":[3]}
							send(False,f"开始清点发牌人数 请用`1`报数")

						elif slices[-1]=="guess":
							data={**data,"round":1,"range":guess[:],"num":randint(guess[0]+1,guess[1]-1),"core":[],"trip":[4]}
							send(False,f"本局猜测范围是：[{guess[0]}]~[{guess[1]}] 请用`n 数字`猜数字")

						else:
							send(False,"·\n可选游戏：\n真心话(truth) 生草机(grass) 狼人杀(wolf) UNO(uno) 猜数字(guess)")

						if slices[-1] in data["push"]:
							data["push"][slices[-1]]=True

				elif text=="|ctrl":
					if data["push"]["truth"]:
						if len(data["core"])<2:
							send(False,"至少要2人才能互相提问")

						else:
							uwu_=max(data['num'])
							_uwu=min(data['num'])
							date_=strftime("日期：%Y.%m.%d",localtime())

							if change[0]:
								uwu_,_uwu=_uwu,uwu_

							send(False,f"·\n统计数据：\n{date_}\n参与人数：{str(len(data['core'])).zfill(3)}\n·\n最{change[1][0]}：[{uwu_}]([{data['core'][data['num'].index(uwu_)]}])\n最{change[1][1]}：[{_uwu}]([{data['core'][data['num'].index(_uwu)]}])")

							sleep(1)
							send(False,f"由[{data['core'][data['num'].index(uwu_)]}]向[{data['core'][data['num'].index(_uwu)]}]提问")

							data={**data,"round":data["round"]+1,"core":[],"num":[]}

					elif data["push"]["grass"]:
						if len(data["temp"])<3:
							send(False,"至少要3人才能生草")

						else:
							send(False,"[生草机]开始生草故事")

							sleep(1)
							shuffle(data["temp"])
							data["core"]=True
							data["notice"]="@"+" @".join(data["temp"])+" "
							send(False,f"{data['notice']}\n请注意查看私聊 由于是按顺序来 部分用户的场合需要等待")

							# 主循环
							def loop():
								temp=data["temp"]
								list_=["人物","地点/时间","事件","续写"]

								for uwu in range(len(temp)):
									sleep(1)
									send(False,f"·\n[{'开头' if uwu<3 else '续写'}]\n现在请你输入生草{list_[uwu if uwu<3 else 3]}\n·\n输入方法：\n`/w {botname} {list_[uwu if uwu<3 else 3]}`",temp[uwu])

									if uwu>=3:
										sleep(0.5)
										note="".join(data["msg"][:3])+" "+" ".join(data["msg"][3:])
										send(False,f"·\n前文内容：\n{note}",temp[uwu])

									for _ in range(60 if uwu<3 else 120):
										sleep(1)

										if uwu!=len(data["msg"]):
											break

									else:
										note=choice(temp if not uwu else sbres[uwu-1 if uwu<3 else 2]).replace("你们",choice(temp)).replace("我们",choice(temp)).replace("你",choice(temp)).replace("我",botnick)
										temp[uwu]=f"替[{temp[uwu]}]写的[{botnick}]"
										data["msg"].append(f"在{note}" if uwu==2 else note)
										send(False,f"{temp[uwu]}卡住了？那就让[{botnick}]帮你写吧",temp[uwu])

								try:
									sleep(2)
									send(False,"".join(data["msg"][:3])+" "+" ".join(data["msg"][3:]))

									sleep(0.5)
									date_=strftime("日期：%Y.%m.%d",localtime())
									note=f"·\n统计数据：\n{date_}\n参与人数：{str(len(temp)).zfill(3)}\n·\n开头："

									for uwu in range(len(temp)):
										if uwu==3:
											note+="\n·\n续写："

										note+=f"\n{data['msg'][uwu]}([{temp[uwu]}])"

									save("grass.log","a+",note.replace("·","")+"\n\n\n")
									end("grass")
									send(False,note)

								except:
									send(False,"Oops! 在处理文本的时候抛出一条错误")

								exit(0)

							# 开启多线程
							Thread(target=loop).start()

					elif data["push"]["uno"]:
						if len(data["temp"])<2:
							send(False,"至少要2人才能打牌")

						else:
							shuffle(data["temp"])
							data["notice"]="@"+" @".join(data["temp"])+" "
							data["time"]=round(time())
							send(False,f"{data['notice']}\n人数到齐 开始发牌 请注意查看私聊")

							for uwu_ in range(len(paper["first"])):
								for _uwu in range(len(paper["last"])):
									data["all"].extend([[uwu_,_uwu]]*2)

							data["all"].extend([None]*4)

							for uwu in data["temp"]:
								sleep(1)
								data["core"][uwu]=[]

								add(uwu,6)
								note="["+"] [".join([(paper['first'][_[0]]+paper['last'][_[1]] if _ else paper["sp"]) for _ in data["core"][uwu]])+"]"
								send(False,f"·\n你的卡牌：\n{note}",uwu)

							sleep(1)
							send(False,f"发牌完毕 回合[1] 开始")

							sleep(1)
							data["now"]=[roll(),data["temp"][0]]
							send(False,f"初始牌是[{paper['first'][data['now'][0][0]]+paper['last'][data['now'][0][1]]}] 由[{data['temp'][0]}]先出")

							# 计时器
							def loop():
								oops=0

								while True:
									try:
										now=data["now"][-1]

										for _ in range(120):
											sleep(1)

											if data["now"][-1]!=now:
												break

										else:
											oops+=1
											send(False,f"Oops! [{now}]超时了 错过了自己的回合")

											sleep(1)

											if oops==10:
												send(False,f"回合被跳过10次 不玩了 {choice(['恼','悲','气','卑'])}")
												break

											else:
												send(False,f"现在的牌还是[{paper['first'][data['now'][0][0]]+paper['last'][data['now'][0][1]]}] 轮到[{next_(now)}]")

									except:
										break

								exit(0)

							# 开启多线程
							Thread(target=loop).start()

				elif text=="|info":
					if data["push"]["grass"] and data["core"]:
						uwu=len(data["msg"])
						note=["·\n已完成：\n"+(" ".join([f"[{_}]" for _ in data["temp"][:uwu]]) or "无"),f"进行中：\n[{data['temp'][uwu]}]",f"等待中：\n"+('无' if len(data['temp'])==len(data['msg'])+1 else "["+"] [".join(data["temp"][uwu+1:])+"]")]
						send(False,"\n·\n".join(note),nick)

					elif data["push"]["wolf"] and data["core"]:
						if nick in data["core"]:
							note="[存活] 喜" if data["core"][nick][3] else "[猝死] 恼" if nick in data["sudden"] else "[被杀] 悲"
							send(False,f"·\n你的卡牌：\n[{card[data['core'][nick][1]][0]}]/[{card[0][data['core'][nick][2]]}]\n·\n你的任务：\n{card[data['core'][nick][1]][1]}\n·\n你的状态：\n{note}\n·\n获胜条件：\n[{card[0][not data['core'][nick][2]]}]全员阵亡",nick)

						else:
							send(False,f"[{nick}]不在村子中")

					elif data["push"]["uno"] and data["core"]:
						if nick in data["core"]:
							note="["+"] [".join([(paper['first'][_[0]]+paper['last'][_[1]] if _ else paper["sp"]) for _ in data["core"][nick]])+"]"
							send(False,f"·\n你的卡牌：\n{note}\n·\n现在的牌：\n[{paper['first'][data['now'][0][0]]+paper['last'][data['now'][0][1]]}]",nick)

						else:
							send(False,f"[{nick}]没有参与本局游戏")

				elif text=="|over":
					for uwu in ["truth","guess"]:
						if data["push"][uwu]:
							send(False,f"Ahh! 游戏在连续进行了[{data['round']}]回后结束了")
							end(uwu)

				elif text=="1":
					try:
						if not data["push"]["truth"] and not data.get("core"):
							if nick in data["temp"]:
								send(False,f"[{nick}]已经在花名册中了 现有[{len(data['temp'])}]人")

							elif data["push"]["uno"] and len(data["temp"])>=8:
								send(False,f"已经到[UNO]的人数上限了")

							else:
								data["temp"].append(nick)

								if data["push"]["wolf"]:
									send(False,f"[{nick}]{choice(general[6])}了村子 村里有{len(data['temp'])}人了")

								else:
									send(False,f"[{nick}]成功加入 现有{len(data['temp'])}人")

								not trip or data["trip"].append(ouo["trip"])

					except:
						pass

				elif text=="r":
					if data["push"]["truth"]:
						if nick in data["core"]:
							send(False,f"[{nick}]已经r出了[{data['num'][data['core'].index(nick)]}]")

						else:
							r=randint(1,999)
							note="本局的主角" if r in [1,999] else choice(["什么鬼","离谱","神奇","wow","nb","6"]) if r in [11,13,23,27,49,57,154,365,666] else ""
							data["core"].append(nick)
							data["num"].append(r)
							not trip or data["trip"].append(ouo["trip"])
							send(False,f"[{nick}]r出了[{r}] {note}")

				elif text[0]=="u":
					if data["push"]["uno"] and nick in data.get("now"):
						slices=text.split()[-1]
						note=str()

						if slices==".":
							if randint(1,3)==3:
								data["now"][0]=roll()
								note=f"[{nick}]将牌补到[{paper['first'][data['now'][0][0]]+paper['last'][data['now'][0][1]]}]并将其打出 轮到[{next_(nick)}]"

							else:
								add(nick,1,True)
								note=f"[{nick}]新增1张牌 轮到[{next_(nick)}]"

						elif slices[:2]==paper["sp"] and None in data["core"][nick]:
							if slices[2:] in paper["first"]:
								note=f"[{nick}]出了[{slices}] "
								rm(nick,None)

								if paper["first"].index(slices[2:])==data["now"][0][0]:
									note+=f"牌和颜色不变 [{nick}]继续出牌"

								else:
									data["now"][0][0]=paper["first"].index(slices[2:])
									note+=f"将牌的颜色变为[{slices[2:]}] [{nick}]继续出牌"

							else:
								note=f"只能为[变色"+"] [变色".join(paper["first"])+"]"

						else:
							try:
								first=paper["first"].index(slices[0])
								last=paper["last"].index(slices[1:])

								if [first,last] in data["core"][nick]:
									if first==data["now"][0][0] or last==data["now"][0][1]:
										note=f"[{nick}]出了[{slices}] "
										rm(nick,[first,last],True)

										if not last:
											nick_=next_(nick)
											note+=f"[{nick_}]跳过了本回合 现在轮到[{next_(nick_)}]"

										elif last==1:
											data["order"]=not data["order"]
											note+=f"顺序调换 现在轮到[{next_(nick)}]"

										elif last in [2,3]:
											num=int(slices[-1])
											nick_=next_(nick,False)
											add(nick_,num,True)
											note+=f"[{nick_}]加{num}张牌 [{nick}]继续出牌"

										else:
											note+=f"现在轮到[{next_(nick)}]"

									else:
										note=f"出牌失败"

								else:
									note=f"[{nick}]没有[{slices}]这张牌"

							except:
								note=f"牌组里没有[{slices}]这张牌"

						if len(data["core"][nick])==1:
							sleep(1)
							send(False,f"[{nick}]：{choice(emote)} UNO!!!")

						if not data["core"][nick]:
							sleep(1)
							send(False,f"Wow! [{nick}]出完了全部的牌 [{nick}]获胜")

							sleep(1)
							minutes=divmod(round(time()-data["time"]),60)
							date_=strftime("日期：%Y.%m.%d",localtime())
							note=f"·\n统计数据：\n{date_}\n时长：{minutes[0]}:{minutes[1]}\n回合数：{str(data['round']).zfill(3)}\n参与人数：{str(len(data['temp'])).zfill(3)}\n·\n剩余牌数：\n"+"\n".join([f"[{_}]：{len(data['core'][_])}" for _ in data["core"]])

							save("uno.log","a+",note.replace("·","")+"\n\n\n")
							end("uno")
							send(False,note)

						else:
							send(False,f"{note} 现在的牌是[{paper['first'][data['now'][0][0]]+paper['last'][data['now'][0][1]]}]")

				elif text[0]=="n":
					if data["push"]["guess"]:
						slices=text.split()[-1]

						try:
							num=round(float(slices))

							if num not in range(data["range"][0]+1,data["range"][1]):
								send(room,f"已经超出当前范围了 请在[{data['range'][0]}]~[{data['range'][1]}]之间")

							else:
								data["core"].append(nick)
								not trip or data["trip"].append(ouo["trip"])

								if num==data["num"]:
									send(False,f"Wow! [{nick}]猜中了数字 {choice(['毫无疑问','的的确确','确实','果真'])}是[{num}]")

									sleep(1)
									date_=strftime("日期：%Y.%m.%d",localtime())
									send(False,f"·\n统计数据：\n{date_}\n参与人数：{str(len(set(data['core']))).zfill(3)}\n猜测次数：{str(len(data['core'])).zfill(3)}\n末尾玩家：[{data['core'][-1]}]")

									data={**data,"round":data["round"]+1,"range":guess[:],"num":randint(guess[0]+1,guess[1]-1),"core":[]}

									sleep(1)
									send(False,f"下轮游戏开始 范围在[{data['range'][0]}]~[{data['range'][1]}]间")

								else:
									note=["小","大"]
									note_=int(num>data["num"])
									data["range"][note_]=num
									send(False,f"[{nick}]猜{note[note_]}了 但把范围缩到了[{data['range'][0]}]~[{data['range'][1]}] {choice(['再来','再猜','继续','再接再厉'])}")

						except:
							send(room,"这不是一个数字 请猜数字")

			elif cmd=="info" and ouo.get("type")=="whisper" and "from" in ouo:
				sleep(0.5)
				nick=str(ouo["from"])
				text=ouo["text"]
				trip=ouo.get("trip",choice(root))
				uwu=ouo.get("msg") if ouo.get("msg") else text[text.find(":")+2:]
				msg=uwu.split("\n",1)
				slices=msg[-1].split()
				pull(nick,trip)

				if msg[0]=="buy" and trip:
					if len(slices)!=1:
						send(room,f"参数错误 应该是：`/w {botname} buy(换行)物品名`",nick)

					elif slices[0] not in notlife[0] or not notlife[0][slices[0]][4]:
						send(room,f"商店里没有[{slices[0]}]",nick)

					elif notlife[1][trip][0][2]<notlife[0][slices[0]][3]:
						send(room,f"[{nick}]没有足够的eb-",nick)

					else:
						old=notlife[0][slices[0]][0]
						notlife[1][old][0][2]+=notlife[0][slices[0]][3]
						notlife[1][trip][0][2]-=notlife[0][slices[0]][3]
						notlife[0][slices[0]][4]=0
						notlife[0][slices[0]][0]=trip
						send(False,f"[{nick}]{'赎回' if old==trip else '买下'}了[{slices[0]}] 并放入了背包\n[{nick}]花了[{notlife[0][slices[0]][3] or 'Null'}]eb {'但是' if old==trip else ''}[{notlife[1][old][0][0]}]{'又' if old==trip else ''}得到[{notlife[0][slices[0]][3] or 'Null'}]eb")

				elif msg[0]=="make" and trip:
					if len(slices)!=3:
						send(room,f"参数错误 应该是：`/w {botname} make(换行)物品名 说明 价值`",nick)

					else:
						name="".join([_ for _ in slices[0] if _.isalpha() or _.isnumeric() or _ in ["_","~","*","@","|"]])

						if name in notlife[0]:
							send(room,f"世界里已经存在[{name}]了",nick)

						elif 0<len(name)<=12 and 0<len(slices[1])<=48:
							if slices[2].isnumeric() and 0<=int(slices[2])<=1919810:
								note=int(slices[2])

								if notlife[1][trip][0][2]<note:
									send(room,f"[{nick}]没有足够的eb-",nick)

								else:
									notlife[0][name]=[trip,name,slices[1],note,0]
									notlife[1][trip][0][2]-=note
									send(False,f"Wow! [{nick}]做出了[{name}]\n说明|[{slices[1]}] 价值|[{int(slices[2]) or 'Null'}]eb")

							else:
								send(room,"价值只能为整数 且在0~1919810间",nick)

						else:
							send(room,"物品名在1~12字间 说明在1~48字间",nick)

				elif msg[0]=="give" and trip:
					if len(slices)!=2:
						send(room,f"参数错误 应该是：`/w {botname} give(换行)物品名 识别码`",nick)

					elif slices[0] not in notlife[0] or notlife[0][slices[0]][4] or notlife[0][slices[0]][0]!=trip:
						send(room,f"背包里没有[{slices[0]}]",nick)

					elif slices[1] not in notlife[1]:
						send(room,"查无此人 请检查识别码",nick)

					else:
						note="自己" if slices[1]==trip else f"[{notlife[1][slices[1]][0][0]}]"
						notlife[0][slices[0]][0]=slices[1]
						send(False,f"[{nick}]把[{slices[0]}]给了{note}")

				elif msg[0]=="sell" and trip:
					if len(slices)!=2:
						send(room,f"参数错误 应该是：`/w {botname} sell(换行)物品名 价值`",nick)

					elif slices[0] not in notlife[0] or notlife[0][slices[0]][4] or notlife[0][slices[0]][0]!=trip:
						send(room,f"背包里没有[{slices[0]}]",nick)

					elif (slices[1].isnumeric() and 0<=int(slices[1])<=1919810) or (trip in root):
						send(False,f"[{nick}]将[{slices[0]}]上架到了商店\n原价|[{notlife[0][slices[0]][3] or 'Null'}]eb 现价|[{int(slices[1]) or 'Null'}]eb")
						notlife[0][slices[0]]=[*notlife[0][slices[0]][:3],int(slices[1]),1]

					else:
						send(room,"价值只能为整数 且在0~1919810间",nick)

				elif msg[0]=="del" and trip:
					if len(slices)!=1:
						send(room,f"参数错误 应该是：`/w {botname} del(换行)物品名`",nick)

					elif slices[0] not in notlife[0] or notlife[0][slices[0]][4] or notlife[0][slices[0]][0]!=trip:
						send(room,f"背包里没有[{slices[0]}]",nick)

					else:
						send(False,f"Oops! [{nick}]丢掉了[{notlife[0].pop(slices[0])[1]}]")

				elif data["push"]["grass"]:
					if nick==data["temp"][len(data["msg"])]:
						if len(data["msg"])==1 and uwu[0]!="在":
							uwu=f"在{uwu}"

						data["msg"].append(uwu.replace("$","").replace("，"," ").replace("。"," "))
						send(room,f"[{nick}]的生草成功",nick)

						if len(data["msg"])<=3 and not len(data["msg"])==len(data["temp"])==3:
							note="".join(data["msg"])
							send(room,f"·\n目前内容：\n{note}",nick)

				elif data["push"]["wolf"]:
					if not data["core"] and nick==data["owner"]:
						allow=sorted([int(_) for _ in uwu.split() if _ in list("1234")])

						if allow==data["group"]:
							send(room,"牌组和原先相同 不变更",nick)

						elif len(allow)<len(data["temp"]):
							send(room,"花名册的人数已经超过牌数了",nick)

						else:
							data["group"]=allow
							send(False,f"[村长]更改了[村民]身份牌数目")

							sleep(1)
							send(False,f"本局卡牌设置({len(allow)}人局)：\n1.[{card[1][0]}]x{allow.count(1)}\n2.[{card[2][0]}]x{allow.count(2)}\n3.[{card[3][0]}]x{allow.count(3)}\n4.[{card[4][0]}]x{allow.count(4)}")

					elif msg[0]=="msg" and nick in data["state"][True]:
						if len(msg)<2 or not msg[1].strip():
							send(room,"请写下你的遗言",nick)

						else:
							send(room,"遗言更新成功" if nick in data["msg"] else "遗言添加成功",nick)
							data["msg"][nick]=msg[1].replace("$","")

					elif data["now"]:
						if nick in data["day"]["wait"]:
							if uwu in data["state"][True]:
								data["day"]["wait"].pop(data["day"]["wait"].index(nick))
								data["day"]["kill"].append(uwu)
								note="你自己" if uwu==nick else f"[{uwu}]"
								send(room,f"你将写有{note}名字的纸片塞进投票箱",nick)

								sleep(2)
								send(False,f"投票箱中多了一张{choice(general[4])}的纸片")

							elif uwu in data["state"][False]:
								send(room,f"你必要{choice(general[7])}死者",nick)

							else:
								data["day"]["wait"].pop(data["day"]["wait"].index(nick))
								send(room,f"你{choice(general[5])} 放弃了投票",nick)

								sleep(2)
								send(False,f"有一张纸片{choice(general[8])}")

						elif nick==data["now"][1] or isinstance(data["now"][1],list) and nick in data["werewolf"]["wait"]:
							if data["now"][0]==2:
								if uwu==nick:
									send(room,f"不允许[{card[2][0]}]选择自己",nick)

								else:
									if uwu in data["state"][True]:
										if uwu in data["prophet"]:
											send(room,f"你已经预言过[{uwu}]的身份了\nTA是[{card[data['core'][uwu][1]][0]}] 属于[{card[0][data['core'][uwu][2]]}]",nick)

											sleep(2)
											send(False,f"不幸的[{card[2][0]}]{choice(prophet[0])}")

										else:
											data["prophet"].append(uwu)
											send(room,f"[{uwu}]是[{card[data['core'][uwu][1]][0]}] 属于[{card[0][data['core'][uwu][2]]}]",nick)

											sleep(2)
											note=choice(prophet[1]) if data["core"][uwu][2] else choice(prophet[2])
											send(False,f"盯着水晶球的[{card[2][0]}]{note}")

									elif uwu in data["state"][False]:
										send(room,f"你没必要{choice(general[7])}死者",nick)

									else:
										send(room,f"你{choice(general[0])}今晚放弃预言 睡个好觉",nick)

										sleep(2)
										send(False,f"[{card[2][0]}]睡得很{choice(prophet[3])}")

									data["now"]=[0,None]

							elif data["now"][0]==3:
								if uwu in data["state"][True]:
									data["werewolf"]["wait"].pop(data["werewolf"]["wait"].index(nick))
									data["werewolf"]["kill"].append(uwu)

									note=f"自己 {choice(werewolf[4])}" if uwu==nick else f"同伴[{uwu}] 这样{choice(werewolf[5])}" if uwu in data["werewolf"]["core"] else f"[{uwu}]"
									send(room,f"你{choice(general[0])}杀{note}",nick)

									for _ in data["werewolf"]["wait"]:
										sleep(1)
										send(False,f"你的同伴[{nick}]{choice(general[0])}杀{'你' if _==uwu else note}",_)

								elif uwu in data["state"][False]:
									send(room,f"你没必要{choice(general[7])}死者",nick)

								else:
									data["werewolf"]["wait"].pop(data["werewolf"]["wait"].index(nick))
									send(room,f"你{choice(general[0])}今晚做件好事 放过人类",nick)

									for _ in data["werewolf"]["wait"]:
										sleep(1)
										send(False,f"你的同伴[{nick}]{choice(general[3])}了",_)

								if not data["werewolf"]["wait"]:
									note="你们意见不相同 因此没有杀人"

									if data["werewolf"]["kill"] and data["werewolf"]["kill"].count(uwu)==len(data["werewolf"]["kill"]):
										chan(uwu)
										data["werewolf"]["dead"].append(uwu)
										data["werewolf"]["kill"]=uwu
										note=f"你们杀死了同伴[{uwu}]" if uwu in data["werewolf"]["core"] else f"你们杀死了[{uwu}]\nTA是[{data['core'][uwu][1]}] 属于[{data['core'][uwu][2]}]"

									for _ in data["werewolf"]["core"]:
										sleep(1)
										send(False,"今晚 你被杀死了" if _==uwu else f"今晚 {note}",_)

									sleep(2)

									if uwu in data["core"] and not data["core"][uwu][3]:
										send(False,f"[公告] {choice(general[2])} 只听见[{uwu}]的{choice(werewolf[0])}和几声狼嚎\n当[{choice(data['state'][True])}]跑去查看情况的时候 只发现[{uwu}]{choice(werewolf[1])}的尸体")

									else:
										send(False,f"能听见远处狼群{choice(werewolf[2])}的声音")

									data["now"]=[0,None]

							elif data["now"][0]==4:
								if uwu==nick:
									send(room,f"不允许[{card[4][0]}]自己喝下药水",nick)

								elif uwu in data["sudden"]:
									send(room,f"你没必要{choice(general[7])}猝死的人",nick)

								else:
									if uwu in data["witch"]["allow"]:
										state=not data["core"][uwu][3]
										note=data["witch"]["med"][state]
										note_=f"获得了新生" if state else f"陷入了永眠"

										chan(uwu,state)
										data["witch"]["temp"]=[uwu,state]
										data["witch"]["med"][state]=[state,False,uwu]
										send(room,f"你使用{potion[note[0]][0]}成功{potion[note[0]][1]}了[{uwu}]",nick)

										sleep(2)
										send(False,f"[公告] {choice(general[2])} 村子里{choice(witch[1])}\n[{choice(data['state'][True])}]挨家挨户地传话道 [{uwu}]{choice(witch[2])}地{note_}")

										data["now"]=[0,None]
										
									elif uwu in data["core"]:
										send(room,f"你没有能给[{uwu}]使用的药",nick)

									else:
										send(room,f"你{choice(general[0])}今晚放弃投药 等待机会",nick)

										sleep(2)
										send(False,f"[{card[4][0]}]笑得很{choice(witch[3])}")

										data["now"]=[0,None]

						elif nick in data["state"][True]:
							send(room,"现在不是你的场合 快去睡觉——",nick)

						elif nick in data["state"][False]:
							send(room,"你已经死了",nick)

				life(0)

		pipe["data"].pop(0)

	else:
		sleep(0.5)
