#coding=utf8
import itchat
from pyecharts import Bar

itchat.auto_login(hotReload=True)
friends = itchat.get_friends()
# user_name = friends[0]["NickName"]
# print(user_name)

male = female = other = 0
# friends 是一个字典
for user in friends:
    user_name = user["NickName"]
    user_signature = user["Signature"]
    print("{} : {}\n".format(user_name, user_signature))
    if user["Sex"] == 1:
        male += 1
    elif user["Sex"] == 2:
        female += 1
    else:
        other += 1

total = len(friends)

print("{} are male, {} are female, {} are other".format(male, female, other))
print("{:.2%} are male, {:.2%} are female, {:.2%} are other".format(male/total, female/total, other/total))


# 作图
bar = Bar(user_name, "男女好友分布")
bar.add("好友", ["男", "女", "其他"], [male, female, other])
# bar.print_echarts_options() # 该行只为了打印配置项，方便调试时使用
bar.render()    # 生成本地 HTML 文件