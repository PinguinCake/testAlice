from requests import post

# print(post("http://localhost:5000/post",
#            json={
#                "request": {
#                    "command": "закажи пиццу на улицу льва толстого, 16 на завтра",
#                    "original_utterance": "закажи пиццу на улицу льва толстого, 16 на завтра"
#                },
#                "session": {
#                    "new": True,
#                    "message_id": 0,
#                    "session_id": "2eac4854-fce721f3-b845abba-20d60",
#                    "skill_id": "3ad36498-f5rd-4079-a14b-788652932056",
#                    "user_id": "AC9WC3DF6FCE052E45A4566A48E6B7193774B84814CE49A922E163B8B29881DC"
#                },
#                "version": "1.0"}).json())

# {'session': {'new': True, 'message_id': 0, 'session_id': '2eac4854-fce721f3-b845abba-20d60',
#              'skill_id': '3ad36498-f5rd-4079-a14b-788652932056',
#              'user_id': 'AC9WC3DF6FCE052E45A4566A48E6B7193774B84814CE49A922E163B8B29881DC'}, 'version': '1.0',
#  'response': {'end_session': False, 'text': 'Привет! Купи слона!',
#               'buttons': [{'title': 'Не хочу.', 'hide': True}, {'title': 'Не буду.', 'hide': True}]}}

# print(post("http://localhost:5000/post",
#            json={
#                "request": {
#                    "command": "не хочу",
#                    "original_utterance": "не хочу"
#                },
#                "session": {
#                    "new": False,
#                    "message_id": 1,
#                    "session_id": "2eac4854-fce721f3-b845abba-20d60",
#                    "skill_id": "3ad36498-f5rd-4079-a14b-788652932056",
#                    "user_id": "AC9WC3DF6FCE052E45A4566A48E6B7193774B84814CE49A922E163B8B29881DC"
#                },
#                "version": "1.0"}).json())

# {'session': {'new': False, 'message_id': 1, 'session_id': '2eac4854-fce721f3-b845abba-20d60',
#              'skill_id': '3ad36498-f5rd-4079-a14b-788652932056',
#              'user_id': 'AC9WC3DF6FCE052E45A4566A48E6B7193774B84814CE49A922E163B8B29881DC'}, 'version': '1.0',
#  'response': {'end_session': False, 'text': "Все говорят 'не хочу', а ты купи слона!",
#               'buttons': [{'title': 'Не буду.', 'hide': True}, {'title': 'Отстань!', 'hide': True}]}}

# print(post("http://localhost:5000/post",
#            json={
#                "request": {
#                    "command": "Не буду.",
#                    "original_utterance": "Не буду."
#                },
#                "session": {
#                    "new": False,
#                    "message_id": 1,
#                    "session_id": "2eac4854-fce721f3-b845abba-20d60",
#                    "skill_id": "3ad36498-f5rd-4079-a14b-788652932056",
#                    "user_id": "AC9WC3DF6FCE052E45A4566A48E6B7193774B84814CE49A922E163B8B29881DC"
#                },
#                "version": "1.0"}).json())

# {'session': {'new': False, 'message_id': 1, 'session_id': '2eac4854-fce721f3-b845abba-20d60',
#              'skill_id': '3ad36498-f5rd-4079-a14b-788652932056',
#              'user_id': 'AC9WC3DF6FCE052E45A4566A48E6B7193774B84814CE49A922E163B8B29881DC'}, 'version': '1.0',
#  'response': {'end_session': False, 'text': "Все говорят 'Не буду.', а ты купи слона!",
#               'buttons': [{'title': 'Отстань!', 'hide': True},
#                           {'title': 'Ладно', 'url': 'https://market.yandex.ru/search?text=слон', 'hide': True}]}}

# print(post("http://localhost:5000/post",
#            json={
#                "request": {
#                    "command": "Ни за что",
#                    "original_utterance": "Ни за что"
#                },
#                "session": {
#                    "new": False,
#                    "message_id": 1,
#                    "session_id": "2eac4854-fce721f3-b845abba-20d60",
#                    "skill_id": "3ad36498-f5rd-4079-a14b-788652932056",
#                    "user_id": "AC9WC3DF6FCE052E45A4566A48E6B7193774B84814CE49A922E163B8B29881DC"
#                },
#                "version": "1.0"}).json())

# {'session': {'new': False, 'message_id': 1, 'session_id': '2eac4854-fce721f3-b845abba-20d60',
#              'skill_id': '3ad36498-f5rd-4079-a14b-788652932056',
#              'user_id': 'AC9WC3DF6FCE052E45A4566A48E6B7193774B84814CE49A922E163B8B29881DC'}, 'version': '1.0',
#  'response': {'end_session': False, 'text': "Все говорят 'Ни за что', а ты купи слона!",
#               'buttons': [{'title': 'Ладно', 'url': 'https://market.yandex.ru/search?text=слон', 'hide': True}]}}

print(post("http://localhost:5000/post",
           json={
               "request": {
                   "command": "Ладно",
                   "original_utterance": "Ладно"
               },
               "session": {
                   "new": False,
                   "message_id": 1,
                   "session_id": "2eac4854-fce721f3-b845abba-20d60",
                   "skill_id": "3ad36498-f5rd-4079-a14b-788652932056",
                   "user_id": "AC9WC3DF6FCE052E45A4566A48E6B7193774B84814CE49A922E163B8B29881DC"
               },
               "version": "1.0"}).json())

# {'session': {'new': False, 'message_id': 1, 'session_id': '2eac4854-fce721f3-b845abba-20d60',
#              'skill_id': '3ad36498-f5rd-4079-a14b-788652932056',
#              'user_id': 'AC9WC3DF6FCE052E45A4566A48E6B7193774B84814CE49A922E163B8B29881DC'}, 'version': '1.0',
#  'response': {'end_session': True, 'text': 'Слона можно найти на Яндекс.Маркете!'}}
