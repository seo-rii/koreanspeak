gyeop_consonant = {'ㄳ': ('ㄱ', 'ㅅ'), 'ㄵ': ('ㄴ', 'ㅈ'), 'ㄶ': ('ㄴ', 'ㅎ'), 'ㄺ': ('ㄹ', 'ㄱ'), 'ㄻ': ('ㄹ', 'ㅁ'), 'ㄼ': ('ㄹ', 'ㅂ'),
                   'ㄽ': ('ㄹ', 'ㅅ'), 'ㄾ': ('ㄹ', 'ㅌ'), 'ㄿ': ('ㄹ', 'ㅍ'), 'ㅀ': ('ㄹ', 'ㅎ'), 'ㅄ': ('ㅂ', 'ㅅ')}


def isTypeOfㄱ(c):
    if c == 'ㄱ' or c == 'ㄲ' or c == 'ㅋ' or c == 'ㄳ' or c == 'ㄺ':
        return True
    return False

def isTypeOfㄷ(c):
    if c == 'ㄷ' or c == 'ㅅ' or c == 'ㅆ' or c == 'ㅈ' or c == 'ㅊ' or c == 'ㅌ':
        return True
    return False

def isTypeOfㅂ(c):
    if c == 'ㅂ' or c == 'ㅍ' or c == 'ㄼ' or c == 'ㄿ' or c == 'ㅄ':
        return True
    return False
