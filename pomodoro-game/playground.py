import time
import winsound
from pygame import mixer

mixer.init()
mixer.music.load("ring_sound.mp3")

for i in range(10, 0, -1):
    print(f"remain: {i}")
    # winsound.Beep(frequency=3000, duration=500)
    # winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
    mixer.music.play()
    time.sleep(5)