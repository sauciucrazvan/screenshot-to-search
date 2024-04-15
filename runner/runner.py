import keyboard, time, subprocess

def main():

    started = False

    while True:
        if keyboard.is_pressed("ctrl+shift+j"):
            if not started:
                subprocess.Popen("bin/app.exe")
                started = True
        else:
            started = False
        
        time.sleep(0.1)

if __name__ == "__main__":
    main()
