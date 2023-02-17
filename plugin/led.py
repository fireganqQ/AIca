# by https://github.com/fireganqQ #

from . import boardBool, board, time, threading


class Led:
    def __init__(self) -> None:
        self.modeBool = False
        self.galatasaray_ = False
        self.fenerbahce_ = False
        self.entertainment_ = False

        self.entertainmentSleep = 0.4

    def entertainmentStart(self):
        self.entertainment_ = True
        self.modeBool = True
        t1 = threading.Thread(target=self.__entertainment__, daemon=True)
        t1.start()

    def stop(self):
        self.modeBool = False
        self.galatasaray_ = False
        self.fenerbahce_ = False
        self.entertainment_ = False
        
    def __entertainment__(self):
        while self.entertainment_:
            for i in range(3,7):
                board.digital[i].write(1)
                time.sleep(self.entertainmentSleep)
                board.digital[i].write(0)

            for i in range(5,3,-1):
                board.digital[i].write(1)
                time.sleep(self.entertainmentSleep)
                board.digital[i].write(0)

    def galatasarayStart(self):
        self.galatasaray_ = True
        self.modeBool = True
        t1 = threading.Thread(target=self.__galatasaray__, daemon=True)
        t1.start()
    def __galatasaray__(self):
        while self.galatasaray_:
            for i in range(3,5):
                board.digital[i].write(1)
                time.sleep(self.entertainmentSleep)
                board.digital[i].write(0)

    def fenerbahceStart(self):
        self.fenerbahce_ = True
        self.modeBool = True
        t1 = threading.Thread(target=self.__fenerbahce__, daemon=True)
        t1.start()

    def __fenerbahce__(self):
        while self.fenerbahce_:
            for i in range(4,6):
                board.digital[i].write(1)
                time.sleep(self.entertainmentSleep)
                board.digital[i].write(0)