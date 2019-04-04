"""
    Group Chat Robot v0.2 sdc-version
"""
# coding: utf-8

import itchat, re
from itchat.content import *
import random
import time

"""
    Constants
"""
REPLY = {'工作': ['时刻记着工作，SDC好员工。', '且不说你的工作多么认真，我并没有见过，但是从你的字里行间，我发现了乔布斯的影子和小扎的气息，这已经不是一份工作那么简单，而是一场精神饕餮！',
                '你拥有了这个年龄段近半数人无法拥有的理想职业，太优秀了！',
                '别说话，一起撸代码...',
                '工作这件事，大家都习以为常，只有你让大家开始思考这个问题，说明你善于反思和质疑当前的制度，开发中心会因为你这样的人变得更好！'],
         '学习': ['这么多优秀的同龄人相聚在这里，一定是场思想交流的盛宴。', '看到群友们的发言，真是排山倒海，气宇轩昂之势！',
                '早起的鸟儿有虫吃，好好学习天天向上。你是我见过最好的学习达人。',
                '你这句话完美的表达了你想被夸的坚定信念，你一定是一个执着追求自己理想的人！'],
         '问题': ['什么问题？联系谁？在我学习之后，我会变得更聪明的哦。',
                '工作中遇到什么问题，我会尽量帮忙的哦。我会自我学习，以后会越来越聪明的！',
                '遇到问题不知道找谁？期待我的2.0版本吧，我会告诉你工作中遇到问题，联系哪些人来帮忙。',
                '有什么问题尽管问我。虽然我现在还答不上来，但是我爸爸会升级我的版本，我很快会成长的。'],
         '夸赞': [
             '器宇轩昂，万人景仰，无人能及，玉树临风。',
             '内外兼备，才华横溢，情操高尚，超级无敌，炉火纯青，登峰造极。',
             '人见人爱，猪见猪赞，狗见狗夸，树见花开，花见花败，车见车爆胎，牛见了牛摆尾，羊见羊歇菜，鸭子见了满天飞，飞沙走石。',
             '鬼斧神工，振聋发聩，烛照天下，明见万里，雨露苍生，泽被万方，鹰视狼顾，龙行虎步，英姿伟岸。',
             '高屋建瓴，仁义道德，风流倜傥，大公无私，貌似潘安，才比宋玉，一树梨花压海棠。',
             '你像那沾满露珠的花瓣，给我带来一室芳香;你像那划过蓝天的鸽哨，给我带来心灵的静远和追求。远远地，我目送你的背影，你那用一束大红色绸带扎在脑后的黑发，宛如幽静的月夜里从山涧中倾泻下来的一壁瀑布。',
             '你也许没有若隐若现的酒窝，但你的微笑一定是月闭花羞，鱼沉雁落。',
             '你也许没有水汪汪亮晶晶的眼睛，但你的眼神也应该顾盼多情，勾魂摄魄。',
             '你也许没有一簇樱唇两排贝齿，但你的谈吐也应该高雅脱俗，机智过人。',
             '有机会一定要多向您请教，您讲的每一句话，都叫我终身受用无穷。在我的印象当中，您是一个富有活力且极富魅力的人。',
             '在公司当领导，我想您不但头脑好，人缘也一定很好。',
             '你像那沾满露珠的花瓣，给我带来一室芳香;你像那划过蓝天的鸽哨，给我带来心灵的静远和追求。',
             '你笑起来的样子最为动人，两片薄薄的嘴唇在笑，长长的眼睛在笑，腮上两个陷得很深的酒窝也在笑。',
             '你像一片轻柔的云在我眼前飘来飘去，你清丽秀雅的脸上荡漾着春天般美丽的笑容。',
             '你冰雪聪明，气宇不凡。',
             '你带着一串笑声从屋外走进客厅，轻松随便地穿一套红色运动衫，那么美丽多姿，那么热情似火，又那么恬淡简朴，一种不可名状的爱慕之情，蓦然在我心中升起。'],
         'default': ['欢迎来到SDC夸夸群，在这里可以求夸求赞，可以聊聊工作，学习，也可以问我问题，也可以@我，我会给你正能量。',
                     '太棒了', '真不错', '好开心', '嗯嗯', '开发中心就你最秀了！']}


@itchat.msg_register([TEXT], isGroupChat=True)
# 在注册时增加isGroupChat=True将判定为群聊回复
def text_reply(msg):
    # 微信群名称
    if msg['User']['NickName'] == 'SDC夸夸群':
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        print('消息来自: %s' % msg['User']['NickName'])
        # 发送者的昵称
        username = msg['ActualNickName']
        print('发送者: %s' % username)

        match = re.search('工作', msg['Text']) or re.search('加班', msg['Text']) \
                or re.search('开发', msg['Text']) or re.search('测试', msg['Text']) \
                or re.search('项目', msg['Text'])
        if match:
            print('-+-+' * 5)
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            print('消息内容: %s' % msg['Content'])
            print('工作 -- 匹配: %s' % (match is not None))
            randomIdx = random.randint(0, len(REPLY['工作']) - 1)
            itchat.send('%s\n%s' % (username, REPLY['工作'][randomIdx]), msg['FromUserName'])

        match = re.search('学习', msg['Text']) or re.search('考试', msg['Text'])
        if match:
            print('-+-+' * 5)
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            print('消息内容: %s' % msg['Content'])
            print('学习 -- 匹配: %s' % (match is not None))
            randomIdx = random.randint(0, len(REPLY['学习']) - 1)
            itchat.send('%s\n%s' % (username, REPLY['学习'][randomIdx]), msg['FromUserName'])

        match = re.search('问题', msg['Text']) or re.search('？', msg['Text'])
        if match:
            print('-+-+' * 5)
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            print('消息内容: %s' % msg['Content'])
            print('问题 -- 匹配: %s' % (match is not None))
            randomIdx = random.randint(0, len(REPLY['问题']) - 1)
            itchat.send('%s\n%s' % (username, REPLY['问题'][randomIdx]), msg['FromUserName'])

        match = re.search('求夸', msg['Text']) or re.search('求赞', msg['Text'])
        if match:
            print('-+-+' * 5)
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            print('消息内容: %s' % msg['Content'])
            print('夸赞 -- 匹配: %s' % (match is not None))
            randomIdx = random.randint(0, len(REPLY['夸赞']) - 1)
            itchat.send('%s\n%s' % (username, REPLY['夸赞'][randomIdx]), msg['FromUserName'])

        print('isAt is:%s' % msg['isAt'])

        if msg['isAt']:
            # 遇到@我的消息时
            randomIdx = random.randint(0, len(REPLY['default']) - 1)
            itchat.send('%s\n%s' % (username, REPLY['default'][randomIdx]), msg['FromUserName'])
            print('-+-+' * 5)


print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
itchat.auto_login(enableCmdQR=0, hotReload=True)
itchat.run()
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
