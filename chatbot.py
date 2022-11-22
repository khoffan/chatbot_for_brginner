import re
from components.response import check_all_massage

# def mmassge_prob(user_masg,recognised_word,single_response=False,required_word=[]):
#     massage_cer = 0
#     has_require_word = True

#     for word in user_masg:
#         if word in recognised_word:
#             massage_cer += 1

#     percentage = float(massage_cer) / float(len(recognised_word))

#     for word in required_word:
#         if word not in user_masg:
#             has_require_word = False
#             break
    
#     if has_require_word or single_response:
#         return int(percentage*100)
#     else:
#         return 0

# def check_all_massage(massage):
#     hight_porb_masg = {}

#     def response(bot_res,list_word,single_response=False,require_word=[]):
#         nonlocal hight_porb_masg
#         hight_porb_masg[bot_res] = mmassge_prob(massage,list_word,single_response,require_word)
    
#     #response ----------------------------------------
#     #เพิ่มค่าข้อความได้ตามต้องการได้
#     response("hello",['hello','hi','whaddub'],single_response=True)
#     response("i\'m find",['how','are','you','doing'],require_word=['how'])
#     response("hey i am lucy",['what','your','name'],require_word=['what','name'])

#     best_match = max(hight_porb_masg, key=hight_porb_masg.get)

#     return best_match
def get_response(user_input):
    splite_msg = re.split(r'\s+|[,.!@$^%&_?]\s',user_input.lower())
    response = check_all_massage(splite_msg)
    return response

def chatbot():
    while True:
        text = input("You: ")
        if text.lower() == 'quit':
            break
        print("Bot: "+ get_response(text.lower()))
chatbot()