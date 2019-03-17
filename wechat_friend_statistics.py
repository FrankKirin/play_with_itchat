#coding=utf8
import re
import os
import itchat
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from pyecharts import Bar
import logging
logging.basicConfig(level=logging.DEBUG)

itchat.auto_login(hotReload=True)
friends = itchat.get_friends()

user_signature = []

male = female = other = 0
# friends 是一个字典
for user in friends:
    # signature = re.sub('<[^<]+?>', '',user["Signature"])
    signature = re.sub('<.*?>', '', user['Signature'])

    if signature:
        user_signature.append(signature.strip())

    if user["Sex"] == 1:
        male += 1
    elif user["Sex"] == 2:
        female += 1
    else:
        other += 1

total = len(friends)

print("{} are male, {} are female, {} are other".format(male, female, other))
print("{:.2%} are male, {:.2%} are female, {:.2%} are other".format(male/total, female/total, other/total))

with open('user_signature.txt', 'w+') as file:
    for _ in user_signature:
        file.write("{}\n".format(_))

# Generate word cloud
def generate_wordcloud_figure():
    with open('user_signature.txt', 'r') as file:
        text = file.read()
        wordcloud = WordCloud(font_path='/Users/frank/Library/Fonts/simhei.ttf').generate(text)
        plt.imshow(wordcloud, interpolation='nearest')
        plt.xlabel(u'董萌宇')
        # plt.axis("off") 
        plt.figure(dpi=300)
        plt.show()
        # plt.savefig('signature.png', dpi=300)

if __name__ == '__main__':
    generate_wordcloud_figure()


# 作图
# bar = Bar(user_name, "男女好友分布")
# bar.add("好友", ["男", "女", "其他"], [male, female, other])
# # bar.print_echarts_options() # 该行只为了打印配置项，方便调试时使用
# bar.render()    # 生成本地 HTML 文件