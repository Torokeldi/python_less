# import requests
#
# url = 'htt://www.w3schools.com/howto/howto_js_topnav_responsive.asp'
#
# res = requests.get(url)
#
# if res.status_code == 200:
#     print("работает")
# else:
#     print("не работает")

import pyjokes

for i in range(0, 6):
    joke = pyjokes.get_joke(language="ru", category="all")
    print(joke)
    print(f"Шутка №{i}:")
    print(joke)

