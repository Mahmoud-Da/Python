#play with janom
!pip install janome

#
from janome.tokenizer import Tokenizer
t = Tokenizer()
m_list = t.tokenize("グローバル化した社会で求められる幅広い教養とモラルを身に\
つけ、商学の基礎となる専門的知識・技能を修得している。")
for n in m_list:
  print(n)

#
#名詞のみ取り出す
import numpy as np
wakati_list = []
wakati = ''
for token in t.tokenize("グローバル化した社会で求められる幅広い教養とモラルを\
身につけ、商学の基礎となる専門的知識・技能を修得している。"):
 hinshi = (token.part_of_speech).split(',')[0]
 if hinshi in ['名詞']:
  word = str(token).split()[0]
  wakati = wakati + word +' '
wakati_list.append(wakati)

wakati_list
