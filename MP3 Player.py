from replit import audio
import os, time

def play():
    source = audio.play_file('audio.wav')
    source.paused = False
    while True:
      stop = int(input("Please Press 2 to stop playback: "))
      if stop == 2:
        source.paused = True
        return
      else:
          continue


while True:
    os.system("clear")
    print("Welcome to Joshua's MP3 Player 🎵")
    time.sleep(2)
    userInput = int(input("Press 1 to PLAY and 2 to STOP: "))
    if userInput == 1:
        play()
    elif userInput == 2:
        continue