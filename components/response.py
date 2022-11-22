from components.masg_porb import mmassge_prob

def check_all_massage(massage):
    hight_porb_masg = {}

    def response(bot_res,list_word,single_response=False,require_word=[]):
        nonlocal hight_porb_masg
        hight_porb_masg[bot_res] = mmassge_prob(massage,list_word,single_response,require_word)
    
    #response ----------------------------------------
    #เพิ่มค่าข้อความได้ตามต้องการได้
    response("hello",['hello','hi','whaddub'],single_response=True)
    response("i\'m find",['how','are','you','doing'],require_word=['how'])
    response("hey i am lucy",['what','your','name'],require_word=['what','name'])

    best_match = max(hight_porb_masg, key=hight_porb_masg.get)

    return best_match