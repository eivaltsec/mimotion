import time
import requests
import random
 
 
def main_ip():
    """
    yao_code为邀请码
    56352159
 
    :return: ""
    :rtype: ""
    """
    yao_code = "56352159"  # 邀请码
    diz = requests.get(
        "http://api.xdaili.cn/xdaili-api//greatRecharge/getGreatIp?spiderId=xxxx&orderno=xxxx&returnType=2&count=1").json()
 
    if diz['ERRORCODE'] == "0":
        if yao_code == "":
            yao_code = input("邀请码空，输入8位邀请码")
        ip = f"{diz['RESULT'][0]['ip']}:{diz['RESULT'][0]['port']}"
        print(ip)
        proxies = {
            "http": f"http://{ip}",
            "https": f"http://{ip}",
        }
        a = 0
        while a < 10:
            a += 1
            print(a)
            img = """https://img2.woyaogexing.com/2020/07/17/33836d83f33a45c4922395b2a1328a74!400x400.jpeg
            https://img2.woyaogexing.com/2020/07/17/232d32bca50e441889ab2fc012e6854f!400x400.jpeg
            https://img2.woyaogexing.com/2020/07/17/9c47541838704532a5a0fba58d51b1b8!400x400.jpeg
            https://img2.woyaogexing.com/2020/07/17/df6c46b20ecb47419f5e9290dc7a84d1!400x400.jpeg
            [img]https://img2.woyaogexing.com/2020/07/17/ef8a229447a3479b96142f473e1becc2!400x400.jpg[/img]
            https://img2.woyaogexing.com/2020/07/17/a94d318d174342bc8cecffe9b8496757!400x400.jpeg
            https://img2.woyaogexing.com/2020/07/17/4a442eb21e664d2aa71184f08fbcae3a!400x400.jpeg
            https://img2.woyaogexing.com/2020/07/17/722760e3266940f1bcda96f0605dae6b!400x400.jpeg
            https://img2.woyaogexing.com/2020/07/17/d99207cae158434c811730a9a2024015!400x400.jpeg
            https://img2.woyaogexing.com/2020/07/17/e36af362da314f9b9e544da59445512b!400x400.jpeg
            https://img2.woyaogexing.com/2020/07/17/174e88464d51400dbeb09c382d3f2b43!400x400.jpeg
            https://img2.woyaogexing.com/2020/07/17/1f0df540930547628f79e6832ba0e6ce!400x400.jpeg
            https://img2.woyaogexing.com/2020/07/17/e489a709c65747a38336b730d3bde654!400x400.jpeg
            https://img2.woyaogexing.com/2020/07/17/e489a709c65747a38336b730d3bde654!400x400.jpeg
            https://img2.woyaogexing.com/2020/07/17/0b2bcf055a7e48a78d5b31e89006c13a!400x400.jpeg
            https://img2.woyaogexing.com/2020/07/17/808c143a5c97404ba23d3b84b2f01394!400x400.jpeg
            https://img2.woyaogexing.com/2020/07/17/18d6ffad92994a95957136ebc3ae76ed!400x400.jpeg
            https://img2.woyaogexing.com/2020/07/17/a9a0d71ae4fa450189745e1e44af9dfa!400x400.jpeg
            https://img2.woyaogexing.com/2020/07/17/b2ad2b5a1c2240c6b23bcddc0e43fbab!400x400.jpeg
            https://img2.woyaogexing.com/2020/07/17/d955f45f3b3b4e52a1c4b722152bfa0d!400x400.jpeg
            https://img2.woyaogexing.com/2020/07/17/d955f45f3b3b4e52a1c4b722152bfa0d!400x400.jpeg
            https://img2.woyaogexing.com/2020/07/17/0a49d821c9de4eea8f2b858d022840d7!400x400.jpeg
            [img]https://img2.woyaogexing.com/2020/07/17/361ccbf2b9624e4daafaf9f18029b6b1!400x400.jpg[/img]
            https://img2.woyaogexing.com/2020/07/17/ea3d312f8868425aafb9f80a6a5ff161!400x400.jpeg
            https://img2.woyaogexing.com/2020/07/17/61863ed94c494e9fa699647a67bc925a!400x400.jpeg
            https://img2.woyaogexing.com/2020/07/17/c04199ada2404650bfe5674f9aeb341c!400x400.jpeg
            https://img2.woyaogexing.com/2020/07/17/4fd060ba790541d0a4ff7ca1d7dd31f2!400x400.jpeg
            https://img2.woyaogexing.com/2020/07/17/f7b7954e7e1542068314bf001cac3220!400x400.jpeg
            https://img2.woyaogexing.com/2020/07/16/a47482e8560a4509bcbc093a9ecafb89!400x400.jpeg
            https://img2.woyaogexing.com/2020/07/17/0e89362854e84d949af38bbf672ee3e1!400x400.jpeg
            https://img2.woyaogexing.com/2020/07/16/52d0326b2a394ab389b65bfe30efdcdc!400x400.jpeg
            https://img2.woyaogexing.com/2020/07/16/45a40d1e319347d8b382dd9ce257ea70!400x400.jpeg
            https://img2.woyaogexing.com/2020/07/16/47c69b92ff3b43209cb40e7bc6749aa5!400x400.jpeg
            https://img2.woyaogexing.com/2020/07/16/2d02ff482fc94b1dac75d68e760dd0b9!400x400.jpeg
            https://img2.woyaogexing.com/2020/07/16/04beaa621ece474a8eb8262997f253f0!400x400.jpeg
            [img]https://img2.woyaogexing.com/2020/07/16/9b72789144d045be8a826d7dea371280!400x400.jpg[/img]
            https://img2.woyaogexing.com/2020/07/16/660f06a4b5544505a0c5451757b62917!400x400.jpeg
            https://img2.woyaogexing.com/2020/07/16/37603af7c7f74dbb90ee90e2f1e21a43!400x400.jpeg""".split("\n")
            name = """忄青深⌒缘?
 
            蜂窝实验室
            Οo茪輝歲冄оΟ
            拼命捂着心脏不让它碎╮
            心交朋友钱交狗ゞ
            说你是2B都对不起人家铅笔
            空人空心空世界
            ぃ 流年
            ζ、三分愛，七分醒。
            眉梢゛那片情ゝ
            ╰︶墨兮〤
            安於現狀°づ
            蜂窝
            ㄑ 流年.4ツ水 .
            〆 ﹏为 你 伏笔。
            能力就是实力.
            事在人为
            成绩单是一份微凉的遗书
            独孤求败◇
            时光不染,回忆不淡
            萌系大白
            生只爱你人
            西海情謌
            不要迷戀哥，嫂子會生氣
            ヾ幸福的感情メ」
            ヾ溕耆A
            画皮易，画心难
            余生请你指教
            像雾像雨又像风
            醒着做梦
            天佑爱人
            风继续吹
            凡人多烦事
            痴心错付
            累世情深
            谁能温暖我的心
            ζ凉风习卷人心
            蜂窝实验室
            你困住我，年深月久
            小妞让爷(づ￣3￣)づ╭个
            坐在坟前调戏鬼
            ^劳资终有一天会炸学校*
            谁喷了榴莲味的香水
            扛起拖把扫天下
            半聋半哑半糊涂
            樱花⌒识盈
            涟漪浅漾
            海在阳光下⌒
            凉月流沐@
            ╰◇木槿花
            花色长裙姑娘好美i
            唯美似夏花
            喇叭婲、
            一个人的天空`
            草莓味的风
            雨落弦断
            巴黎街角上空飘着的气球っ
            带花旳蘑菇°
            樱花下的浪漫
            心素如简
            、浅 笑 ζ
            盛夏光年
            唇齿微凉薄荷糖.
            靜待花開
            紫色`薰衣草
            绿袖子
            彼岸雨露
            蓝色的海洋
            じ初晴夜雨
            森林小巷少女与狐@
            我有我的小思念
            历经繁华才知平淡是真
            巫女养的猫.
            别忘了那杯水起初也是热的
            因为看透人心所以百毒不侵
            柔情演绎
            且行且珍惜
            我喜欢你用了整整一个曾经
            天然淡雅香
            泪倾斜的海
            森系女孩
            向鈤葵の微笑。
            南幕影歇
            浅草带疏烟
            ╭萢ㄣ沫oοО
            5个半柠檬c
            ~_樱花草.
            _素手浣椛⌒
            樱莎美子°
            花堪渡
            暖南绿倾i
            浅浅玫瑰淡淡香°
            巷尾的梧桐
            苏陌染。
            湛蓝玫瑰
            海单纯洁白°
            芳草碧色
            花、￣很美
            花岩伴飞花°
            佳蜜桃妞
            冬天开出牵牛花ヽ
            小清新范
            向阳小草，暖暖好
            @薄荷冰i
            ら花一样的年龄
            柠檬草。
            风过无痕
            红玫瑰々
            陨落星辰
            打酱油的先生
            厭世為王
            离吥开忧伤
            清風与我
            澎湃小青年
            木伊蓅年
            杀尽天下叛我者
            傲气一世
            决战风云
            炼狱死神
            本尊，无赖
            霸天绝地
            夏风如歌
            血染的风
            沧海行云
            魔龙★祭天
            狙神之说
            棱枫★绝影
            箭指天阙
            落雨流殤
            月下鹰翔
            狂傲゛俯视世界
            雪夜伤雨痕
            死神无惧
            晨曦骄阳
            霸气拽少
            恣意踏江山
            魅影狂杀
            殘月殺手
            霜色メ幻想
            风掠幽蓝
            狂灵在世
            幻°一世凡尘
            幽冥灬紫瞳
            影猎灭世
            亂世年間
            凌晨交界
            紫翼魔王
            寒气震四方
            雄霸罕世
            暗世メ骑
            楠木清晨
            飞鹰荣耀
            超鬼般被杀
            柠萌味的西瓜
            风、扬起思念
            花儿开在雨季
            雨后的告白
            夏的哭声
            夜未央゛樱花落
            有范儿的女人
            该死的心动
            够范°旳气质女人
            别两难
            凉城听暖
            林尽处听雨眠
            沉醉花海
            泼墨山水
            南风向北
            山后别相逢
            岁月静好
            微笑向暖
            半字浅眉-
            如花的旋律
            山水温柔不回头
            几程山水
            清风秀雅
            怀抱清风
            微笑面对每一天
            花与时光同眠
            陈酒幽梦
            筱蓝芷韵
            请远离我i
            ヽ如冰
            浅蓝色
            冷月飘霜
            正宗傻白甜
            不爱请闪开
            图图是个好孩纸
            低声细语
            桔味美人
            風光
            青色发尾
            石榴薄荷
            清风耳畔拂
            你笑在眉眼.
            再可爱一点好了
            老死不相往来
            海上明月共潮生
            清风入梦
            森林屿麓
            看海听风""".split("\n")
            nu = random.randint(1000, 99999)
            headers = {
                "Accept-Encoding": "gzip,deflate,br",
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Content Type": "application/json",
                "Cookie": f"UM_distinctid={str(nu)}2b8ea750-0d47632c92aba5-3f176f50-3d10d-17352b8ea76d8",
                "Host": "biz.caiyunapp.com",
                "User-Agent": "ColorfulClouds/6.0.1(iPhone;iOS13.2.2;Scale/2.00)"
            }
            data = {
                "avatar": f"{img[random.randint(0, len(img) - 1)]}",
                "uid": f"B{str(nu)}Z",
                "gender": "0",
                "device_id": f"358EE7E0-396F-412A-{nu}Z-B{nu}",
                "platform_name": "weixin",
                "platform_id": f"BB{nu}YZ",
                "app_name": "weather",
                "name": f"{str(random.randint(1, 9999999999))+name[random.randint(0, len(name) - 1)]}"
            }
 
            try:
                res = requests.post("https://biz.caiyunapp.com/v2/third_party_login", headers=headers, json=data,
                                    proxies=proxies, timeout=6).json()
                token = res['result']['token']
            except Exception as e:
                print(e)
                a -= 1
                continue
            yao_headers = {
                "Accept": "application/json",
                "Accept-Encoding": "gzip,deflate,br",
                "Accept-Language": "zh-Hans-CN;q=1",
                "Connection": "keep-alive",
                "Content-Type": "application/json",
                "Cookie": f"UM_distinctid=17352b8ea750-0d47632c92aba5-3f176f50-3d10d-{str(nu)}",
                "Cy-User-Id": token,
                "Host": "biz.caiyunapp.com",
                "User-Agent": "ColorfulClouds/6.0.1(iPhone;iOS13.2.2;Scale/2.00)"
            }
            yao_data = {
                "os_type": "ios",
                "app_name": "wt",
                "invitation_code": yao_code
            }
            try:
                resp = requests.post("https://biz.caiyunapp.com/v3/user/invitation_code/redeem", proxies=proxies,
                                     headers=yao_headers,
                                     json=yao_data, timeout=6).text
                print(resp)
            except Exception as e:
                print(e)
                a -= 1
                continue
            time.sleep(5)
    else:
        main()
 
 
def main():
    """
    yao_code为邀请码
    56352159
 
    :return: ""
    :rtype: ""
    """
    yao_code = "56352159"  # 邀请码
 
    if yao_code == "":
        yao_code = input("邀请码空，输入8位邀请码")
    a = 0
    while a < 10:
        a += 1
        print(a)
        img = """https://img2.woyaogexing.com/2020/07/17/33836d83f33a45c4922395b2a1328a74!400x400.jpeg
        https://img2.woyaogexing.com/2020/07/17/232d32bca50e441889ab2fc012e6854f!400x400.jpeg
        https://img2.woyaogexing.com/2020/07/17/9c47541838704532a5a0fba58d51b1b8!400x400.jpeg
        https://img2.woyaogexing.com/2020/07/17/df6c46b20ecb47419f5e9290dc7a84d1!400x400.jpeg
        [img]https://img2.woyaogexing.com/2020/07/17/ef8a229447a3479b96142f473e1becc2!400x400.jpg[/img]
        https://img2.woyaogexing.com/2020/07/17/a94d318d174342bc8cecffe9b8496757!400x400.jpeg
        https://img2.woyaogexing.com/2020/07/17/4a442eb21e664d2aa71184f08fbcae3a!400x400.jpeg
        https://img2.woyaogexing.com/2020/07/17/722760e3266940f1bcda96f0605dae6b!400x400.jpeg
        https://img2.woyaogexing.com/2020/07/17/d99207cae158434c811730a9a2024015!400x400.jpeg
        https://img2.woyaogexing.com/2020/07/17/e36af362da314f9b9e544da59445512b!400x400.jpeg
        https://img2.woyaogexing.com/2020/07/17/174e88464d51400dbeb09c382d3f2b43!400x400.jpeg
        https://img2.woyaogexing.com/2020/07/17/1f0df540930547628f79e6832ba0e6ce!400x400.jpeg
        https://img2.woyaogexing.com/2020/07/17/e489a709c65747a38336b730d3bde654!400x400.jpeg
        https://img2.woyaogexing.com/2020/07/17/e489a709c65747a38336b730d3bde654!400x400.jpeg
        https://img2.woyaogexing.com/2020/07/17/0b2bcf055a7e48a78d5b31e89006c13a!400x400.jpeg
        https://img2.woyaogexing.com/2020/07/17/808c143a5c97404ba23d3b84b2f01394!400x400.jpeg
        https://img2.woyaogexing.com/2020/07/17/18d6ffad92994a95957136ebc3ae76ed!400x400.jpeg
        https://img2.woyaogexing.com/2020/07/17/a9a0d71ae4fa450189745e1e44af9dfa!400x400.jpeg
        https://img2.woyaogexing.com/2020/07/17/b2ad2b5a1c2240c6b23bcddc0e43fbab!400x400.jpeg
        https://img2.woyaogexing.com/2020/07/17/d955f45f3b3b4e52a1c4b722152bfa0d!400x400.jpeg
        https://img2.woyaogexing.com/2020/07/17/d955f45f3b3b4e52a1c4b722152bfa0d!400x400.jpeg
        https://img2.woyaogexing.com/2020/07/17/0a49d821c9de4eea8f2b858d022840d7!400x400.jpeg
        [img]https://img2.woyaogexing.com/2020/07/17/361ccbf2b9624e4daafaf9f18029b6b1!400x400.jpg[/img]
        https://img2.woyaogexing.com/2020/07/17/ea3d312f8868425aafb9f80a6a5ff161!400x400.jpeg
        https://img2.woyaogexing.com/2020/07/17/61863ed94c494e9fa699647a67bc925a!400x400.jpeg
        https://img2.woyaogexing.com/2020/07/17/c04199ada2404650bfe5674f9aeb341c!400x400.jpeg
        https://img2.woyaogexing.com/2020/07/17/4fd060ba790541d0a4ff7ca1d7dd31f2!400x400.jpeg
        https://img2.woyaogexing.com/2020/07/17/f7b7954e7e1542068314bf001cac3220!400x400.jpeg
        https://img2.woyaogexing.com/2020/07/16/a47482e8560a4509bcbc093a9ecafb89!400x400.jpeg
        https://img2.woyaogexing.com/2020/07/17/0e89362854e84d949af38bbf672ee3e1!400x400.jpeg
        https://img2.woyaogexing.com/2020/07/16/52d0326b2a394ab389b65bfe30efdcdc!400x400.jpeg
        https://img2.woyaogexing.com/2020/07/16/45a40d1e319347d8b382dd9ce257ea70!400x400.jpeg
        https://img2.woyaogexing.com/2020/07/16/47c69b92ff3b43209cb40e7bc6749aa5!400x400.jpeg
        https://img2.woyaogexing.com/2020/07/16/2d02ff482fc94b1dac75d68e760dd0b9!400x400.jpeg
        https://img2.woyaogexing.com/2020/07/16/04beaa621ece474a8eb8262997f253f0!400x400.jpeg
        [img]https://img2.woyaogexing.com/2020/07/16/9b72789144d045be8a826d7dea371280!400x400.jpg[/img]
        https://img2.woyaogexing.com/2020/07/16/660f06a4b5544505a0c5451757b62917!400x400.jpeg
        https://img2.woyaogexing.com/2020/07/16/37603af7c7f74dbb90ee90e2f1e21a43!400x400.jpeg""".split("\n")
        name = """忄青深⌒缘?
        蜂窝实验室
        Οo茪輝歲冄оΟ
        拼命捂着心脏不让它碎╮
        心交朋友钱交狗ゞ
        说你是2B都对不起人家铅笔
        空人空心空世界
        ぃ 流年
        ζ、三分愛，七分醒。
        眉梢゛那片情ゝ
        ╰︶墨兮〤
        安於現狀°づ
        蜂窝
        ㄑ 流年.4ツ水 .
        〆 ﹏为 你 伏笔。
        能力就是实力.
        事在人为
        成绩单是一份微凉的遗书
        独孤求败◇
        时光不染,回忆不淡
        萌系大白
        生只爱你人
        西海情謌
        不要迷戀哥，嫂子會生氣
        ヾ幸福的感情メ」
        ヾ溕耆A
        画皮易，画心难
        余生请你指教
        像雾像雨又像风
        醒着做梦
        天佑爱人
        风继续吹
        凡人多烦事
        痴心错付
        累世情深
        谁能温暖我的心
        ζ凉风习卷人心
        蜂窝实验室
        你困住我，年深月久
        小妞让爷(づ￣3￣)づ╭个
        坐在坟前调戏鬼
        ^劳资终有一天会炸学校*
        谁喷了榴莲味的香水
        扛起拖把扫天下
        半聋半哑半糊涂
        樱花⌒识盈
        涟漪浅漾
        海在阳光下⌒
        凉月流沐@
        ╰◇木槿花
        花色长裙姑娘好美i
        唯美似夏花
        喇叭婲、
        一个人的天空`
        草莓味的风
        雨落弦断
        巴黎街角上空飘着的气球っ
        带花旳蘑菇°
        樱花下的浪漫
        心素如简
        、浅 笑 ζ
        盛夏光年
        唇齿微凉薄荷糖.
        靜待花開
        紫色`薰衣草
        绿袖子
        彼岸雨露
        蓝色的海洋
        じ初晴夜雨
        森林小巷少女与狐@
        我有我的小思念
        历经繁华才知平淡是真
        巫女养的猫.
        别忘了那杯水起初也是热的
        因为看透人心所以百毒不侵
        柔情演绎
        且行且珍惜
        我喜欢你用了整整一个曾经
        天然淡雅香
        泪倾斜的海
        森系女孩
        向鈤葵の微笑。
        南幕影歇
        浅草带疏烟
        ╭萢ㄣ沫oοО
        5个半柠檬c
        ~_樱花草.
        _素手浣椛⌒
        樱莎美子°
        花堪渡
        暖南绿倾i
        浅浅玫瑰淡淡香°
        巷尾的梧桐
        苏陌染。
        湛蓝玫瑰
        海单纯洁白°
        芳草碧色
        花、￣很美
        花岩伴飞花°
        佳蜜桃妞
        冬天开出牵牛花ヽ
        小清新范
        向阳小草，暖暖好
        @薄荷冰i
        ら花一样的年龄
        柠檬草。
        风过无痕
        红玫瑰々
        陨落星辰
        打酱油的先生
        厭世為王
        离吥开忧伤
        清風与我
        澎湃小青年
        木伊蓅年
        杀尽天下叛我者
        傲气一世
        决战风云
        炼狱死神
        本尊，无赖
        霸天绝地
        夏风如歌
        血染的风
        沧海行云
        魔龙★祭天
        狙神之说
        棱枫★绝影
        箭指天阙
        落雨流殤
        月下鹰翔
        狂傲゛俯视世界
        雪夜伤雨痕
        死神无惧
        晨曦骄阳
        霸气拽少
        恣意踏江山
        魅影狂杀
        殘月殺手
        霜色メ幻想
        风掠幽蓝
        狂灵在世
        幻°一世凡尘
        幽冥灬紫瞳
        影猎灭世
        亂世年間
        凌晨交界
        紫翼魔王
        寒气震四方
        雄霸罕世
        暗世メ骑
        楠木清晨
        飞鹰荣耀
        超鬼般被杀
        柠萌味的西瓜
        风、扬起思念
        花儿开在雨季
        雨后的告白
        夏的哭声
        夜未央゛樱花落
        有范儿的女人
        该死的心动
        够范°旳气质女人
        别两难
        凉城听暖
        林尽处听雨眠
        沉醉花海
        泼墨山水
        南风向北
        山后别相逢
        岁月静好
        微笑向暖
        半字浅眉-
        如花的旋律
        山水温柔不回头
        几程山水
        清风秀雅
        怀抱清风
        微笑面对每一天
        花与时光同眠
        陈酒幽梦
        筱蓝芷韵
        请远离我i
        ヽ如冰
        浅蓝色
        冷月飘霜
        正宗傻白甜
        不爱请闪开
        图图是个好孩纸
        低声细语
        桔味美人
        風光
        青色发尾
        石榴薄荷
        清风耳畔拂
        你笑在眉眼.
        再可爱一点好了
        老死不相往来
        海上明月共潮生
        清风入梦
        森林屿麓
        看海听风""".split("\n")
        nu = random.randint(1000, 99999)
        headers = {
            "Accept-Encoding": "gzip,deflate,br",
            "Accept": "*/*",
            "Connection": "keep-alive",
            "Content Type": "application/json",
            "Cookie": f"UM_distinctid={str(nu)}2b8ea750-0d47632c92aba5-3f176f50-3d10d-17352b8ea76d8",
            "Host": "biz.caiyunapp.com",
            "User-Agent": "ColorfulClouds/6.0.1(iPhone;iOS13.2.2;Scale/2.00)"
        }
        data = {
            "avatar": f"{img[random.randint(0, len(img) - 1)]}",
            "uid": f"B{str(nu)}Z",
            "gender": "0",
            "device_id": f"358EE7E0-396F-412A-{nu}Z-B{nu}",
            "platform_name": "weixin",
            "platform_id": f"BB{nu}YZ",
            "app_name": "weather",
            #"name": f"{name[random.randint(0, len(name) - 1)]}"
            "name": f"{str(random.randint(1, 9999999999))+name[random.randint(0, len(name) - 1)]}"

        }
 
        try:
            res = requests.post("https://biz.caiyunapp.com/v2/third_party_login", headers=headers, json=data,
                                timeout=6).json()
            token = res['result']['token']
        except Exception as e:
            print(e)
            a -= 1
            continue
        yao_headers = {
            "Accept": "application/json",
            "Accept-Encoding": "gzip,deflate,br",
            "Accept-Language": "zh-Hans-CN;q=1",
            "Connection": "keep-alive",
            "Content-Type": "application/json",
            "Cookie": f"UM_distinctid=17352b8ea750-0d47632c92aba5-3f176f50-3d10d-{str(nu)}",
            "Cy-User-Id": token,
            "Host": "biz.caiyunapp.com",
            "User-Agent": "ColorfulClouds/6.0.1(iPhone;iOS13.2.2;Scale/2.00)"
        }
        yao_data = {
            "os_type": "ios",
            "app_name": "wt",
            "invitation_code": yao_code
        }
        try:
            resp = requests.post("https://biz.caiyunapp.com/v3/user/invitation_code/redeem", headers=yao_headers,
                                 json=yao_data, timeout=6).text
            print(resp)
        except Exception as e:
            print(e)
            a -= 1
            continue
        time.sleep(5)
 
 
if __name__ == '__main__':
    main_ip()