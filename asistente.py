import speech_recognition as sr
import subprocess as sub
import pyautogui as auto
import pyttsx3 as voz
from time import sleep


def interpretar(comando_de_audio):
    comando_de_audio = comando_de_audio.split(' ')
    #print(type(dato))
    ver_video = ('vídeo' or 'video') in comando_de_audio
    escribir = ('escribir' or 'texto') in comando_de_audio

    #print(type(vd))
    if ver_video is True:
        abrir_youtube()
    elif escribir is True:
        abrir_blocNotas()


def abrir_blocNotas():
    sub.call('start notepad.exe', shell=True)
    sleep(1.5)
    auto.write('Estoy lista para escribir tu texto Jordi')
    lupita = voz.init()
    velocidad = lupita.getProperty('rate')
    lupita.setProperty('rate', velocidad-25)
    lupita.setProperty('voice', 'TTS_MS_ES-MX_SABINA_11.0') # voz con acento mexicano
    lupita.say('Estoy lista para escribir tu texto Jordi')
    lupita.runAndWait()


def abrir_youtube():
    sub.call([r'C:/Users/gcjor\Desktop/codisprogramar/codisprogramats_enmarxa/repos_integrats_vsc_github/voiceassist_apli_jgc/navegar.bat'])
    return None


# escuchar el audio con el micrófono de mi computadora
r = sr.Recognizer()
with sr.Microphone() as source:
    print("¡Dime!")
    audio = r.listen(source)


try:
    # Si se entendió el audio
    comando = r.recognize_google(audio, language='es-MX')
    print("Creo que dijiste: " + comando)
    interpretar(comando) # lo que se debe hacer con el comando de audio

except sr.UnknownValueError:
    # si no se entendió
    print("No te pude entender")
except sr.RequestError as e:
    # si no se tiene conexión a internet o al servicio de google
    print("No pude obtener respuesta del servicio de Google Speech Recognition; {0}".format(e))