import keyboard, time, subprocess, yaml

def main():

    started = False

    with open("config.yaml", "r") as f:
        data = yaml.safe_load(f)

        shortcut = data["shortcut"]

        while True:
            if keyboard.is_pressed(shortcut):
                if not started:
                    subprocess.Popen("bin/app.exe")
                    started = True
            else:
                started = False
            
            time.sleep(0.1)

if __name__ == "__main__":
    main()
