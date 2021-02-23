from Scripts.chatbot.utils.Preprocess import Preprocess

sent = input()

p = Preprocess(userdic='../utils/user_dic.tsv')
pos = p.pos(sent)
ret = p.get_keywords(pos, without_tag=False)
print(ret)

ret = p.get_keywords(pos, without_tag=True)
print(ret)



