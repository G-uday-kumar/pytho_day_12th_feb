import time
from threading import Thread

class Movie(Thread):
    def run(self):
        if self.name == "Producer":
            self.produce()
        elif self.name == "Director":
            self.director()
        elif self.name == "Actor":
            self.actor()
        else:
            self.artists()

    def produce(self):
        for i in range(5):
            print("Produce is investing on the movie")
            time.sleep(5)
        print("Produce is done")
    def director(self):
        while True:
            print("Director is Directing in the movie")
            time.sleep(5)
    def actor(self):
        while True:
            print("Actor is Acting in the movie")
            time.sleep(5)
    def artists(self):
        while True:
            print("Artist is acting in the movie")
            time.sleep(5)
m1=Movie()
m2=Movie()
m3=Movie()
m4=Movie()

m1.name="Producer"
m2.name="Director"
m3.name="Actor"
m4.name="Artist"


m2.daemon=True
m3.daemon=True
m4.daemon=True
m1.start()
time.sleep(1)
m2.start()
time.sleep(1)
m3.start()
time.sleep(1)
m4.start()
