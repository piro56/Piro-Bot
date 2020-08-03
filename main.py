import DiscordExtension
import threading

if __name__ == '__main__':
    t = threading.Thread(name='DiscordExtension', target=DiscordExtension.PiroBot_Run)
    t.start()
