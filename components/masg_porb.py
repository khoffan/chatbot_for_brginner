def mmassge_prob(user_masg,recognised_word,single_response=False,required_word=[]):
    massage_cer = 0
    has_require_word = True

    for word in user_masg:
        if word in recognised_word:
            massage_cer += 1

    percentage = float(massage_cer) / float(len(recognised_word))

    for word in required_word:
        if word not in user_masg:
            has_require_word = False
            break
    
    if has_require_word or single_response:
        return int(percentage*100)
    else:
        return 0