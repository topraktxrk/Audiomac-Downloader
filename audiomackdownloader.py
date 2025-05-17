import json
import pyfiglet
import os
import requests
import platform
import webbrowser


def agreement1(): #me and chatgpt mostly me
    print("1. as this is your first time using AUMC Downloader here is a tutorial how to use AUMC Downloader\n")
    print("2. firstly go to audiomack and choose a title (NO PLAYLIST) after choosing a song title press f12 on your keyboard \n or press left click and press on inspect if you got a diffrent browser then chromium browsers \n")
    print("3. after pressing f12 or pressing inspect website press on the network tab, above right it should say clear network log press on it\n")
    print("4. after clearing your network log you should see the logs being free sometimes there comes random files but that doesnt matter\n")
    print("5. press play on your music title, after pressing the play button there should pop up a section with containing your musics name\n")
    print("6. if not just check if the type is media, after confirming its your music title left click on it and copy the url\n")
    print("7. after copying the url paste it in the script after agreeing\n")
    print("8. after pasting the link and downloading the audio file it will show up in the folder where you put the script i recommend to make a folder for this script, still if you can find where you put it just choose option 2")
    print("9. this was the tutorial of using AUMC Downloader if you dindt understand it read it again or show it to chatgpt for help ig\n")
    print("but if you did understand it type 1 to start this script")
    while True:
        agree = input()
        try:
            agree = int(agree)
            if agree == 1:

                fn = "options.json"
                data = {"option": 1}
                with open(fn, 'w') as myfile:
                    json.dump(data,myfile)
                print("please wait Updating agreement file")
                break
            else:
                print("Please type 1 to proceed.")
        except ValueError:
            print("Invalid input, please enter 1.")


def agreement2(): #me and chatgpt mostly chatgpt
    fn = "options.json"
    if not os.path.exists(fn):  # Check if file exists
        return 0
    with open(fn,"r") as myfile:
        datavalue = json.load(myfile)
    return datavalue.get("option")
def windowsorlinuxmac(): #me
    asd = platform.system().lower()
    term = os.environ.get("TERM")

    if asd == "windows":
        os.system("cls")
    elif term:
        os.system("clear")

def download_audiomack_track(): #chatgpt
    url = input("send the link here\n")
    filename = input("Name the mp3 file\n")

    response = requests.get(url, allow_redirects=True)

    print("Status:", response.status_code)
    print("Content-Type:", response.headers.get("Content-Type"))
    print("Content-Length:", response.headers.get("Content-Length"))

    if "audio" in response.headers.get("Content-Type", ""):
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded: {filename}")
    else:
        print("This is not an audio file. Check the URL.")

def whereami(): #chatgpt
    folder_path = os.path.dirname(os.path.abspath(__file__))
    if platform.system() == "Windows":
        os.startfile(folder_path)
    elif platform.system() == "Darwin":  # macOS
        os.system(f"open \"{folder_path}\"")
    else:  # Linux and others
        os.system(f"xdg-open \"{folder_path}\"")

while True: #me
    print(pyfiglet.figlet_format("AUMC Downloader", font="slant"))
    print("        any bugs send to sssoprak on discord \n")
    print("                       V 1.0\n")
    print(f"[1]Download Audiomack Songs\n[2]Open Folder\n[3]exit")
    print("select your option")
    selection1 = input()
    selection1 = int(selection1)
    if selection1 == 1:
        value = agreement2()
        if value == 1:
            download_audiomack_track()
        else:
            agreement1()
            windowsorlinuxmac()
            download_audiomack_track()

    if selection1 == 2:
        whereami()
    if selection1 == 3:
        webbrowser.open("")
    if selection1 == 4:
        exit()