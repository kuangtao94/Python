import yagmail

# ----------1.跟发件相关的参数------
yag = yagmail.SMTP(user="1512500241@qq.com",password="wmqtqbtnmyamhfjd",host="smtp.qq.com")

#邮箱正文
contents = ['雪里已知春信至，寒梅点缀琼枝腻。\
            香脸半开娇旖旎，当庭际，玉人浴出新妆洗。\
            造化可能偏有意，故教明月玲珑地。'\
            '共赏金尊沈绿蚁，莫辞醉，此花不与群花比。']

#邮件发送
# yag.send("1512500241@qq.com","yagmail邮件发送",contents)

#给多个接受者发送邮件
# yag.send(["1512500241@qq.com","2376416151@qq.com","1554908427@qq.com"],"yagmail邮件发送测试",contents)

#给多个接受者发送邮件附件 --多份附件用列表表示
yag.send(["1512500241@qq.com","2376416151@qq.com","1554908427@qq.com"],"yagmail附件发送测试",contents,["Test_Report.html","app测试点.png"])
