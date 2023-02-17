# by https://github.com/fireganqQ #

from playsound import playsound
from gtts import gTTS
import speech_recognition as sr, random, time, os
from plugin import board, boardBool
from plugin.led import Led
from plugin.openai import Ai

r=sr.Recognizer()
led = Led()

class SesliAsistan():
    def dubbing(self,metin):
        xtts=gTTS(text=metin,lang="tr")
        dosya="./ses/dosya"+str(random.randint(0,1242312412312))+".mp3"
        xtts.save(dosya)
        time.sleep(1)
        playsound(dosya)
        os.remove(dosya)
    def voiceRecord(self):
        with sr.Microphone() as kaynak:
            print("Sizi dinliyorum...")
            listen=r.listen(kaynak)
            voice=" "

            try:
                voice=r.recognize_google(listen,language="tr-TR")
            except sr.UnknownValueError:
                self.dubbing("Ne söylediğinizi anlayamadım.Lutfen tekrar ediniz")

            return voice
    def editAudioText(self, text) -> str:
        return text.lower().replace('i', 'ı')

    def brain(self, text, wakeFunction: bool=False):
            if "selam" in self.editAudioText(text):
                self.dubbing("Selamm, Nasılsın?")
            elif "merhaba" in self.editAudioText(text):
                self.dubbing("Merhabalar efendim!")
            elif "nasılsın" in self.editAudioText(text):
                self.dubbing("iyim siz nasılsınız")
            elif "nasıl gıdıyor" in self.editAudioText(text):
                self.dubbing("iyi sizin?")
            elif "ışık" in self.editAudioText(text) and "aç" in self.editAudioText(text) and "beyaz" in self.editAudioText(text):
                if boardBool != True:
                    self.dubbing('Bir hata oluştu daha sonra tekrar deneyiniz!')
                    return
                self.dubbing('Işıklar açılıyor..')
                led.stop()
                board.digital[2].write(1)
                board.digital[3].write(0)
                board.digital[4].write(0)
                board.digital[5].write(0)
                board.digital[6].write(0)
                board.digital[7].write(1)
            elif "ışık" in self.editAudioText(text) and "aç" in self.editAudioText(text):
                if boardBool != True:
                    self.dubbing('Bir hata oluştu daha sonra tekrar deneyiniz!')
                    return
                self.dubbing('Işıklar açılıyor..')
                led.stop()
                board.digital[2].write(1)
                board.digital[3].write(1)
                board.digital[4].write(1)
                board.digital[5].write(1)
                board.digital[6].write(1)
                board.digital[7].write(1)
            elif "eğlence" in self.editAudioText(text) and ("aç" in self.editAudioText(text) or "başlat" in self.editAudioText(text)):
                if boardBool != True:
                    self.dubbing('Bir hata oluştu daha sonra tekrar deneyiniz!')
                    return

                if led.modeBool == True:
                    self.dubbing('Çalışan bir mod var!')
                    return

                self.dubbing('Mod başlatılıyor..')
                led.entertainmentStart()
            elif "eğlence" in self.editAudioText(text) and "kapat" in self.editAudioText(text):
                if boardBool != True:
                    self.dubbing('Bir hata oluştu daha sonra tekrar deneyiniz!')
                    return

                if led.modeBool != True:
                    self.dubbing('Çalışan bir mod yok!')
                    return

                self.dubbing('Mod kapatılıyor..')
                led.stop()
            elif "ışık" in self.editAudioText(text) and "kapat" in self.editAudioText(text):
                if boardBool != True:
                    self.dubbing('Bir hata oluştu daha sonra tekrar deneyiniz!')
                    return
                self.dubbing('Işıklar kapatılıyor..')
                led.stop()
                board.digital[2].write(0)
                board.digital[3].write(0)
                board.digital[4].write(0)
                board.digital[5].write(0)
                board.digital[6].write(0)
                board.digital[7].write(0)
            elif ("eğlence" in self.editAudioText(text) or "led" in self.editAudioText(text)) and "hız" in self.editAudioText(text) and ("arttır" in self.editAudioText(text) or "yükselt" in self.editAudioText(text) or "hızlandır" in self.editAudioText(text)):
                self.dubbing('Led hızı arttırılıyor..')
                led.entertainmentSleep-=0.2
                if led.entertainmentSleep < 0:
                    led.entertainmentSleep = 0.1
            elif ("eğlence" in self.editAudioText(text) or "led" in self.editAudioText(text)) and (("hız" in self.editAudioText(text) and ("azalt" in self.editAudioText(text) or "düşür" in self.editAudioText(text))) or "yavaşlat" in self.editAudioText(text)):
                self.dubbing('Led hızı azaltılıyor..')
                led.entertainmentSleep+=0.2
            elif "galatasaray" in self.editAudioText(text):
                if boardBool != True:
                    self.dubbing('Bir hata oluştu daha sonra tekrar deneyiniz!')
                    return
                led.stop()
                self.dubbing(random.choice(['En büyük cimbom!!', 'en büyük galatasaray!!']))
                led.galatasarayStart()
            elif "fenerbahçe" in self.editAudioText(text):
                if boardBool != True:
                    self.dubbing('Bir hata oluştu daha sonra tekrar deneyiniz!')
                    return
                led.stop()
                self.dubbing(random.choice(['En büyük fenerbahçe!!']))
                led.fenerbahceStart()

            else:
                if wakeFunction or 'ayça' in self.editAudioText(text):
                    pass
                else:
                    return
                print(text)
                self.dubbing(Ai().ai(text))