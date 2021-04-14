from pyrogram import Client, Filters, filters, emoji

app = Client("Hi", bot_token="1604118007:AAF_w0_1qLOVQMArR1DrC567k8TZ7VSNPDc")


@app.on_message(Filters.command('hello'))
def startmsg(client, message):
    message.reply("هاي أنا بوت اللي عبدالله اللي عبدالله عمله")


# @app.on_message(Filters.command('photoUrl'))
# def photoUrl(client, message):
#     chatID = message.chat.id
#     photoUrl = "https://telegra.ph/file/aa59c3024666f7bc9f712.jpg"
#     client.send_photo(chatID, photoUrl)


# @app.on_message(Filters.command('photo'))
# def photoId(client, message):
#     chatID = message.chat.id
#     photoUrl = "https://telegra.ph/file/aa59c3024666f7bc9f712.jpg"
#     caption = "__عالم البرمجة__"
#     style = "Md"
#     # https://core.telegram.org/bots/api#markdown-style
#     client.send_photo(chatID, photoUrl, caption, style)


# @app.on_message(Filters.command('videoUrl'))
# def videoUrl(client, message):
#     chatID = message.chat.id
#     videoUrl = "https://telegra.ph/file/8e6865cd51fb051ab8812.mp4"
#     client.send_video(chatID, videoUrl)


app.run()
