
import os
import pyttsx3

def speak(msg):
    try:
        engine = pyttsx3.init()
        engine.say(msg)
        engine.runAndWait()
    except:
        print("Voice module not working.")

def command_center():
    speak("Phantom Bot online.")
    print("Phantom V2 > Type !help for commands.")
    while True:
        cmd = input("Phantom > ").strip().lower()
        if cmd == "!help":
            print("""
!help              → Show help menu
!speak <msg>       → Phantom speaks message
!deploy <target>   → Launch QR clone (discord, paypal, whatsapp, amazon)
!dashboard         → Open web dashboard
!exit              → Exit Phantom
""")
        elif cmd.startswith("!speak "):
            speak(cmd[7:])
        elif cmd.startswith("!deploy"):
            parts = cmd.split()
            if len(parts) >= 2:
                target = parts[1]
                speak(f"Launching {target} clone.")
                os.system(f"start http://127.0.0.1:5000/{target}")
            else:
                print("Specify a target to deploy.")
        elif cmd == "!dashboard":
            os.system("start dashboard/index.html")
        elif cmd == "!exit":
            speak("Shutting down.")
            break
        else:
            print("Unknown command.")

if __name__ == "__main__":
    command_center()
