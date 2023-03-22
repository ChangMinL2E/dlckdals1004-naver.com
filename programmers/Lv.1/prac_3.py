# 둘만의 암호

'''
s	skip	index	result
"aukks"	"wbqd"	5	"happy"
'''


def solution(s, skip, index):
    answer = ''
    
    spellings = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    for spell in skip:
        spellings.remove(spell)
    
    def change(x):
        idx = spellings.index(x)
        x = spellings[(idx+index)% len(spellings)]
        return x
        
    s = ''.join(list(map(lambda x: change(x),s)))
    
    return s