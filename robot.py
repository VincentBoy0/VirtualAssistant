from listen import audioToText
from speak import textToAudio
from AppOpener import open, close
import webbrowser

myLang = "vi"
def print_speak(text):
    print(text)
    textToAudio(text, myLang)

def main_menu():
    print("-----------------------------------------")
    print("|Main menu                              |")
    print("-----------------------------------------")
    print("|Chế độ:                                |")
    print("|         1.   Mở/Đóng app              |")
    print("|         2.   Tìm kiếm                 |")
    print("-----------------------------------------")

def open_app(app):
    text = "mở " + app
    print(text)
    textToAudio(text, myLang)
    open(app, match_closest=True, output=False)
    
def close_app(app):
    text = "đóng " + app
    print(text)
    textToAudio(text, myLang)
    close(app, match_closest=True, output=False)    


App = ["word", "excel", "powerpoint", "notepad", "google", "discord", 
       "zalo", "unikey", "codeblocks", "keyboard", "nitro", "zoom"]

def choose_mode(text):
    for app in App: 
        if app in text:
            if "mở" in text:
                open_app(app)
            elif "đóng" in text:
                close_app(app)


print("Robot: Chào anh Long, chúc anh một ngày vui")
textToAudio("Chào anh Long, chúc anh một ngày vui", myLang)
main_menu()
while True:
    text = audioToText(myLang)
    text = text.lower()
    if ("mở" in text) or ("đóng" in text): 
        choose_mode(text)
    elif "tìm kiếm" in text:
        textToAudio(text, myLang)
        if "facebook" in text:
            link = "https://facebook.com"
        elif "youtube" in text:
            link = "https://youtube.com"
        elif "gmail" in text:
            link = "https://gmail.com"
        else:
            link = "https://google.com/search?q="
            for i in range(9, len(text)):
                link = link + text[i]

        webbrowser.open(link)
    elif "menu" in text:
        main_menu()
    elif "ngắt kết nối" in text:
        print_speak("Tạm biệt và hẹn gặp lại anh Long")
        break

