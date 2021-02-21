Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import JPype
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    import JPype
ModuleNotFoundError: No module named 'JPype'
>>> import JPype
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    import JPype
ModuleNotFoundError: No module named 'JPype'
>>> import JPype
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    import JPype
ModuleNotFoundError: No module named 'JPype'
>>> from konlpy.tag import Komoran
>>> import pickle
>>> class Preprocess:
	def__init__(self, word2index_dic='', userdic=None):
		
SyntaxError: invalid syntax
>>> class Preprocess:
	def__init(self, word2index_dic='', userdic=None):
		
SyntaxError: invalid syntax
>>> class Preprocess:
	def__init__(self, word2index_dic='', userdic=None):				if word2index_dic !='':
		
SyntaxError: invalid syntax
>>> class Preprocess:
	def __init__(self, word2index_dic='', userdic=Nonde):
		if word2index_dic !='':
			f = open(word2index_dic, "rb")
			self.word_index = pickle.load(f)
			f.close()
		else:
			self.word_index = None

		
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    class Preprocess:
  File "<pyshell#20>", line 2, in Preprocess
    def __init__(self, word2index_dic='', userdic=Nonde):
NameError: name 'Nonde' is not defined
>>> class Preprocess:
	def __init__(self, word2index_dic='', userdic=None):
		if word2index_dic !='':
			f = open(word2index_dic, "rb")
			self.word_index = pickle.load(f)
			f.close()
		else:
			self.word_index = None

			
>>> self.komoran = Komoran(userdic=userdic)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    self.komoran = Komoran(userdic=userdic)
NameError: name 'userdic' is not defined
>>> self.komoran = Komoran(userdic=userdic)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    self.komoran = Komoran(userdic=userdic)
NameError: name 'userdic' is not defined
>>> class Preprocess:
	def __init__(self, word2index_dic='', userid=None):
		if word2index_dic !='':
			f = open(word2index_dic, "rb")
			self.word_index = pickle.load(f)
			f.close()
		else:
			self.word_index = None
		self.komoran = Komoran(userdic=userdic)
		self.exclusion_tags = [
			'JKS', 'JKC', 'JKO', 'JKB', 'JKV', 'JKQ',
			'JX', 'JC'
			'SF', 'SP', 'SS', 'SE', 'SO',
			'EP', 'EF', 'EC', 'ETN', 'ETM',
			'XSN', 'XSV', 'XSA'
			]

	
>>> def pos(self, sentence):
	return self.komoran.pos(sentence)

>>> def get_keywords(self, pos, without_tag=False):
	f = lambda x: x in self.exclusion_tags
	word_list = []
	for p in pos:
		if f(p[1]) is False:
			word_list.append(p if without_tag is False else p[0])
		return word_list

	
>>> def get_wordidx_sequence(self, keywords):
	if self.word_index is None:
		return []
	w2i = []
	for word in keywords:
		try:
			w2i.append(self.word_index[word])
		except KeyError:
			w2i.append(self.word_index['OOV'])
	return w2i

>>> 