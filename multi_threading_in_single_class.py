import time
from threading import Thread

class MSWord(Thread):
    def run(self):
        if m1.name == "Typing":
            self.typing()
        elif self.name=="SpellCheck":
            self.spellCheck()
        else:
            self.autoSave()
    def typing(self):
        for i in range(2):
            print("Hello Uday")
            time.sleep(5)
    def spellCheck(self):
        for i in range(2):
            print("Spell Check is going on")
            time.sleep(5)
    def autoSave(self):
        for i in range(2):
            print("Autosave is going on")
            time.sleep(2)
m1=MSWord()
m2=MSWord()
m3=MSWord()
m1.name="Typing"
m2.name="SpellCheck"
m3.name="AutoSave"
m1.start()
m2.start()
m3.start()
