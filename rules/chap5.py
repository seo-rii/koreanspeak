def rule17(a, b, c, p, q, r):
    if p=='ㅇ' and q=='ㅣ':
        if c=='ㄷ':
            c=''
            p='ㅈ'
        elif c=='ㅌ' or c=='ㄾ':
            c=''
            p='ㅊ'
    return (a, b, c, p, q, r)

def rule18(a, b, c, p, q, r):
    if p=='ㄴ' or p=='ㅁ':
        if c=='ㄱ' or c=='ㄲ' or c=='ㅋ' or c=='ㄳ' or c=='ㄺ':
            c='ㅇ'
        elif c=='ㄷ' or c=='ㅅ' or c=='ㅆ' or c=='ㅈ' or c=='ㅊ' or c=='ㅌ' or c=='ㅎ':
            c='ㄴ'
        elif c=='ㅂ' or c=='ㅍ' or c=='ㄼ' or c=='ㄿ' or c=='ㅄ':
            c='ㅁ'
    return (a, b, c, p, q, r)

def rule19(a, b, c, p, q, r):
    if c=='ㅁ' or c=='ㅇ':
        if p=='ㄹ':
            p='ㄴ'
    return (a, b, c, p, q, r)



def rule20(a, b, c, p, q, r):
    if c=='ㄴ' and p=='ㄹ':
        c='ㄹ'
    elif (c=='ㄹ' or c=='ㄾ' or c=='ㅀ') and p=='ㄴ':
        p='ㄹ'
    return (a, b, c, p, q, r)

