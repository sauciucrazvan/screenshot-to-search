import keyboard, time, subprocess, yaml

def main():

    started = False
    shortcut = "ctrl+shift+j" # Default shortcut to start de application

    try:
        with open("runner_config.yaml", "r") as f:
            data = yaml.safe_load(f)
            shortcut = data["shortcut"]
    except:
        print("Using the default configuration as runner_config.yaml was not found.")

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
