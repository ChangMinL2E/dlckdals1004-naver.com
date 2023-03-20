# 로그인 성공?

'''
id_pw	db	result
["meosseugi", "1234"]	[["rardss", "123"], ["yyoom", "1234"], ["meosseugi", "1234"]]	"login"
["programmer01", "15789"]	[["programmer02", "111111"], ["programmer00", "134"], ["programmer01", "1145"]]	"wrong pw"
["rabbit04", "98761"]	[["jaja11", "98761"], ["krong0313", "29440"], ["rabbit00", "111333"]]	"fail"
'''

def solution(id_pw, db):
    answer = 'fail'
    
    for data in db:
        if data == id_pw:
            answer = 'login'
            break
        elif data[0] == id_pw[0]:
            answer = 'wrong pw'
    
    return answer