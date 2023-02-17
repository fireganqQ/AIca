# by https://github.com/fireganqQ #

from utils import SesliAsistan
import random

asistan=SesliAsistan()

def uyanma_fonksiyonu(metin):
    if(metin.replace('ç', 'c')=="hey ayca" or metin.replace('ç', 'c')=="ayca"):
        asistan.dubbing(random.choice(["Efendim..", "Efendim canım..", "Dinliyorum."]))
        cevap=asistan.voiceRecord()
        if(cevap!=""):
            asistan.brain(cevap, True)
    else: # deneme
        asistan.brain(metin, False) # deneme

if __name__ == "__main__":
    while True:
        ses=asistan.voiceRecord()
        if(ses!=" "):
            ses=ses.lower()
            uyanma_fonksiyonu(ses)