# Importing of the Modules for creating Custom Announcement files

import os
import pandas as pd   # for reading CSV
from pydub import AudioSegment   # for generating the Audio segments from mp3 file
from gtts import gTTS   # Google text to  speech


def text_to_speech(text , filename):
    '''This function converts text to the audio file
    this function takes the text and converts the text into the system voice and gives the file output'''
    mytext = str(text)
    language = 'hi'
    myobj = gTTS(text=mytext , lang=language)
    myobj.save(filename)





def merge_audios(audios):
    '''This function returns pydub Audio segments
       Merging of the audio segments for making the main audio files'''
    combined = AudioSegment.empty()
    for audio in audios:
        combined += AudioSegment.from_mp3(audio)


    return combined



def generate_skeletons ():
    '''joining of the Audio Segments for making the Audio Files'''
    audio = AudioSegment.from_mp3("railway.mp3")

    # 1.  generating "Kripiya DHyan Dijiye"    from audio file of the Railway mp3
    start = 88000
    finish = 90200
    audioProcessed = audio[start:finish]
    audioProcessed.export("1_announce.mp3" , format = "mp3")
    
    # 2. generating is from city 


    # 3 . generating se Chalkar
    start = 91000
    finish = 92200
    audioProcessed = audio[start:finish]
    audioProcessed.export("3_announce.mp3" , format = "mp3")


    # 4. is VIA-City




    # 5. generating "KE RAASTE" 
    start = 94000
    finish = 95000
    audioProcessed = audio[start:finish]
    audioProcessed.export("5_announce.mp3" , format = "mp3")


    # 6. generating to City




    #7. Generate "KO JANE WALI GAADI SANKYA"
    start = 96000
    finish = 98900
    audioProcessed = audio[start:finish]
    audioProcessed.export("7_announce.mp3" , format = "mp3")

    #8. generating Train number and name


    #9. generating   "KUCH HI SAMAY ME PLATFORM SANKHYA"
    start = 105500
    finish = 108200
    audioProcessed = audio[start:finish]
    audioProcessed.export("9_announce.mp3" , format = "mp3")
    
    # 10 generating platform number



    #11 generating "PER AA RAHI HAI"
    start = 109000
    finish = 112250
    audioProcessed = audio[start:finish]
    audioProcessed.export("11_announce.mp3" , format = "mp3")





def generate_announcement (filename):
    """reading of the EXCEL FIle and generating from the file and generating the audio files and forming of the 
       main Announments using the merge audios funtion """
    df = pd.read_excel(filename)
    print(df)
    for index , item in df.iterrows():
        #2.  generating from city
        text_to_speech(item['from'] , '2_announce.mp3')

        # 4 VIA CITY 
        text_to_speech(item['via'] , '4_announce.mp3')

        # 6 to-City
        text_to_speech(item['to'] , '6_announce.mp3')

        # 8 TRain NUMBER  NAMe
        text_to_speech(item['train_no'] + " " + item['train_name'] , '8_announce.mp3')

        # 10 Platform number
        text_to_speech(item['platform'] , '10_announce.mp3')

        audios = [ f"{i}_announce.mp3" for i in range(1,12)]


        # making the main Files for the announcements
        annnouncement = merge_audios(audios)
        annnouncement.export(f'main_announcement_{index+1}.mp3', format="mp3")

        






if __name__ == "__main__":
    print("Generating Skeletons ......")
    generate_skeletons()
    print("Now Generating Announcements")
    generate_announcement("announce_hindi.xlsx")
    
