import json
import requests
from opencc import OpenCC

cc = OpenCC("t2s")
text = "習近平的政績？"
text = cc.convert(text)
sess = requests.get("https://api.ownthink.com/bot?spoken=" + text)

answer = sess.text

answer = json.loads(answer)

print(answer)