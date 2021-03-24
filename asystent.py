import speech_recognition as sr
import pyttsx3 as tts
import os, sys, time
import random
import webbrowser


# r - recognizing speech
r = sr.Recognizer()
# engine - text to speech
engine = tts.init()
engine.setProperty('rate', 150)

# programs and aplications
lol = '"D:\Riot Games\Riot Client\RiotClientServices.exe" --launch-product=league_of_legends --launch-patchline=live'

# lists of keywords for our assistant
startCommands = ['siema', 'mordeczko', 'potrzebuję pomocy', 'włącz się']
karinaCommands = ['karina', 'karyna', 'karino', 'karyno', 'karinka']
endCommands = ['żegnaj', 'bywaj', 'nara', 'na razie', 'spadam', 'spierdalaj', 'goń się', 'żegnam']
browserCommands = ['włącz przeglądarkę', 'przeglądarka', 'opera', 'włącza operę', 'przeglądarkę']
lolCommands = ['włącz lola', 'liga legend', 'lola', 'ligę legend', 'league of legends', 'lol']
searchYtCommands = ['szukaj na youtube', 'wyszukaj na youtube', 'znajdż na youtube', 'znajdź na youtubie', 'włącz na youtube',
                    'włącz na youtubie', 'wyszukaj na youtubie']
ytCommands = ['youtube', 'youtuba']
searchCommands = ['szukaj', 'wyszukaj', 'google', 'googluj', 'gogle', 'znajdź'] 

# answers:
startAnswers = ['masz jakiś problem, mordo?', 'no co tam byczku?', 'no elo mordeczko, w czym ci pomóc?', 
                'potrzebujesz czegoś ode mnie byczku?']
karynaAnswers = ['karyna zgłasza się', 'karyna w gotowości, w czym pomóc?']
lolAnswers = ['czas na grę mordo, powodzenia!', 'daj z siebie wszystko byczku', 'rozpierdzielisz ich, mordeczko']
ytAnswers = ['miłego oglądania mordo', 'już włączam youtube ziomuś', 'oki doki mordo, youtube włączony']
googleAnswers = ['coś tam znalazłam', 'zoba co Ci wyszukałam', 'w sumie to coś znalazłam', 'sam se szukaj ha ha. nie no żartowałam']

def talkToMe(text):
    engine.say(text)
    engine.runAndWait()

# get text from microphone and check if it isnt None
def getText():
    with sr.Microphone() as source:
        try:
            print("Słucham...")
            audio = r.listen(source)
            text = r.recognize_google(audio, language = 'pl-PL')
            if text != '':
                return text.lower()
            else:
                return None
        except:
            return None

def checkWords(text, words):
        return [element for element in words if element in text]

def openBrowser(url):
    webbrowser.get().open(url)

def main():
    while True:
        os.system("cls")
        time.sleep(0.5)
        newCommand = getText()
        if newCommand != None:
            os.system("cls")
            print(newCommand)
            if len(checkWords(newCommand, startCommands)): # greetings
                talkToMe(random.choice(startAnswers))
            elif len(checkWords(newCommand, browserCommands)): # browser
                talkToMe("luźno byczku, już włączam przeglądarkę")
                openBrowser("www.google.com")
            elif len(checkWords(newCommand, lolCommands)): # league of legends
                talkToMe(random.choice(lolAnswers))
                os.system(lol)
            elif len(checkWords(newCommand, searchYtCommands)): # search in youtube
                talkToMe(random.choice(googleAnswers))
                askYoutube = newCommand.split(checkWords(newCommand, searchYtCommands)[0])[1] 
                newLinkYt = ("https://www.youtube.com/results?search_query=" + askYoutube.replace(" ", "+").replace("?", "%3F")) # create a link 
                openBrowser(newLinkYt)
            elif len(checkWords(newCommand, ytCommands)): # open youtube
                talkToMe(random.choice(ytAnswers))
                openBrowser("www.youtube.com")
            elif len(checkWords(newCommand, searchCommands)): # search in google
                askGoogle = newCommand.split(checkWords(newCommand, searchCommands)[0])[1]  # get text after search command
                newLink = ("https://www.google.com/search?q=" + askGoogle.replace(" ", "+").replace("?", "%3F")) # create a link  
                openBrowser(newLink)
                talkToMe(random.choice(googleAnswers))

            elif len(checkWords(newCommand, karinaCommands)): # greetings with karina name
                talkToMe(random.choice(karynaAnswers))
            elif len(checkWords(newCommand, endCommands)): # end of program
                talkToMe("No to spierdalam...")
                sys.exit()


if __name__ == '__main__':
    main()