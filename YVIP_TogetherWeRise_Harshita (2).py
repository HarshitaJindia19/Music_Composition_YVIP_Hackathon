# script_name: TOGETHER we RISE 
# authour: Harshita Jindia 
# description:  I wanted to construct a song which encapsulates the journey of the Indigenous people and black communities through peace, challenges, and resilience

from earsketch import *

#tempo set
setTempo(100)
setTempo(120, 14.5) #I accelerated the tempo for the Challenges part to reflect the escalating difficulties the Indigenous and black communities faced
setTempo(100, 24) #the tempo is restored to a slower speed, as a moment of reflection and resilience of the communities, from the challenges
#Altogether, the tempo changes serve to highlight the Indigenous & black communities' journey to strength through peace, challenges, and resilience 

# music section 
#SOUNDBANK

#keyboard
keyboard1 = COMMON_LOVE_THEME_PIANO_4
keyboard2 = TFLAMES_OC_PIANO_VRS_4

#beats/bass
beat1 = SAMIAN_PEUP_BEAT_FULL
beat2 = DKBEAR_FREE_PERC_KICK
beat3 = CIARA_HWR_DRUM_BASS_1

bass1 = MILKNSIZZ_SENTIMIENTO_808_BASS
bass2 = SAMIAN_PEUP_PERC_CRASH
bass3 = HIPHOP_DUSTYGROOVEPART_002

#drums
drum1 = YG_ALT_POP_SNARE_1
drum2 = KHALID_NORM_DRUMBEAT

#flute
flute1 = TFLAMES_OMEN_FLUTE_1_VRS_2

#strings
strings1 = TFLAMES_OMEN_STRINGS_CHOR_1
strings2 = TFLAMES_OMEN_STRINGS_CHOR_2
strings3 = ENTREP_THEME_ORCH

#vocals
vocals1 = AK_UNDOG_PERC_VOCALS_2
vocals2 = AK_UNDOG_OOHS_AHHS_3
vocals3 = TFLAMES_OC_VOX_VRS_1
vocals4 = TFLAMES_OC_VOX_VRS_2
vocals5 = ENTREP_VOX_PHARRELL_WHSP_2
vocals6 = JWOLF_COTG_VOX_LEAD_INTRO_2
vocals7 = JWOLF_COTG_VOX_LEAD_VERSE_1
vocals9 = ENTREP_VOX_PHARRELL_WHSP_5
vocals8 = ENTREP_VOX_PHARRELL_WHSP_6
vocals10 = TFLAMES_OMEN_VOX_CHOR_1
vocals11 = AK_UNDOG_VOCAL_BKUP_5 #rise up
vocals12 = AK_UNDOG_OOHS_AHHS_4
vocals13 = DKBEAR_FREE_TALK_MUST_DO
vocals14 = DKBEAR_FREE_TALK_NEED_TO
vocals15 = AK_UNDOG_VOCAL_BELT_1

choir1 = Y33_CHOIR_1
choir2 = Y33_CHOIR_2

#sfx
sfx1 = DKBEAR_FREE_PERC_AUX
sfx2 = EIGHT_BIT_ATARI_SFX_013
sfx3 = RD_RNB_SFX_SPACETAP_1
sfx4 = Y20_CLAP_1


#part 1 - together
#intro function
def introTOGETHER (start, end):

    fitMedia(vocals1, 1, start, end) 
    fitMedia(vocals2, 2, start+1, end)

    for measure in range(start+2,end):
        makeBeat(bass1, 4, measure, "0--0--0---------")
        setEffect(4, VOLUME, GAIN, 0, measure, 2, measure)
           
    for measure in range(start+1, end-2):
        if measure != start+2:
             fitMedia(bass2, 6, measure, measure+2)

    setEffect(2, VOLUME, GAIN, 0, start+1, 12, end-3)
    setEffect(2, VOLUME, GAIN, 12, start+3, -50, end-0.5)

#bridge to challenges 
fitMedia(keyboard2, 3, 5, 7) 
setEffect(3,VOLUME,GAIN, -60, 5.8, -10, 6.5)

print('Part 1 - Together: For the introduction I aimed to set themes of peace and unity, to symbolize the togetherness of Indigenous peoples before multiple hardships encountered by them. It is to highlight their cultural heritage and collective identity. To fit all of these themes I used softer tones through vocals and bass to sound the heartbeat of these thriving communities.')

#part 2 - challenges 
#verse 1 function 

def verse1CHALLENGES():

    #looped beats 
    for measure in range(7, 15):
        if measure != 10:
            fitMedia(beat1, 7, measure, measure+1)

    for measure in range(5+2,11):
        if measure != 8 and measure != 10:
            fitMedia(flute1, 8, measure, measure+2)

    for measure in range(12, 15):
        if measure != 13:
            makeBeat(vocals5, 10, measure, "0++++++++++++++++--") #whisphers indicating the inner voice showing them being aware of them loosing there voice

    #added sounds 
    fitMedia(vocals3, 9, 10.95, 12.5)
    fitMedia(vocals4, 9, 12.6, 14.6)
    fitMedia(vocals6, 11, 15, 16.7)  
    fitMedia(vocals6, 12, 10.11, 18)  
    fitMedia(vocals7, 11, 18, 21.8)
    fitMedia(sfx3, 26, 21.3, 23.3)
    fitMedia(sfx1, 13, 18, 26)
    fitMedia(beat3, 14, 15, 16.8)
    fitMedia(vocals8, 10, 19.5, 20.7)
    fitMedia(vocals9, 10, 18.5, 19.5)

    #makeBeats 
    makeBeat(beat2, 13, 16.8, "0-0-0-0-0-00000")
    makeBeat(bass3, 16, 20.5, "0000000000000")

    #setEffects 
    setEffect(7, VOLUME, GAIN, 0, 7, 3, 14)
    setEffect(9, PITCHSHIFT, PITCHSHIFT_SHIFT, -10) #I used PITCHSHIFT effect to symbolize identity loss faced by the communities during challenging times
    setEffect(10, PITCHSHIFT, PITCHSHIFT_SHIFT, 5) 
    setEffect(11, REVERB, REVERB_TIME, 1500, 20, 4000, 22)
    setEffect(13, VOLUME, GAIN, 12, 21.5, -50, 26)
    setEffect(14, VOLUME, GAIN, 0, 16, -10, 17)
    setEffect(12,VOLUME,GAIN, -60, 16.7, 0, 16.7)
    setEffect(10, VOLUME, GAIN, 5, 18.5, 0, 22)
    setEffect(11, VOLUME, GAIN, -5)
    setEffect(16, VOLUME, GAIN, 4, 12.7, 12, 23.3)
    setEffect(26, VOLUME, GAIN, 3)

    #function for sfx to repeat with a louder volume
    def sfxEffect(startMeasure, endMeasure, loudVolume):
        fitMedia(sfx2, 15, startMeasure , endMeasure)
        setEffect(15, VOLUME, GAIN, -20, startMeasure, loudVolume, endMeasure)
    
    sfxEffect(17.7, 18.1, -10)
    sfxEffect(21.3, 21.8, -5)

print('Part 2 - Challenges: This section delves into the course of challenges and adversities faced by the Indigenous and Black communities. I focused on the stems of Jayli Wolf from "Child of the Government", to indicate the deep loss of cultural identity and the persisting legacies of trauma from such actions pursued by the Canadian government and the Catholic Church against Indigenous peoples. I wanted to include specific contexts including adoption into white homes, and separation of Indigenous families. I also worked to incorporate stems from Pharrell Williams in his song "Entrepreneur" to reflect the racial injustices created by the white populations in their society against Black communities. To combine all elements and emphasize the deep emotions I incorporated more intense and faster beats, paired with different pitches to the vocals as a symbolization of identity loss.')

#transition from intro together, to more resilience and unity
def bridge():

    #added sounds
    fitMedia(drum1, 17, 30, 35)
    fitMedia(sfx4, 18, 30, 35)
    fitMedia(choir1, 19, 29, 33) #used choir vocals to show unity in voices after the hardships
    fitMedia(drum2, 20, 30, 33)

    #set VOLUME effects 
    setEffect(17, VOLUME, GAIN, -20, 30, -10, 35)
    setEffect(18, VOLUME, GAIN, -20, 30, -10, 35)
    setEffect(19, VOLUME, GAIN, -10, 29, -30, 33)
    setEffect(20, VOLUME, GAIN, -20)

print('Part 3 - Resilience: In this section, I use the introduction which demonstrates unity and peace, but now I place it after the challenges part. This is to highlight the growing resilience of the Indigenous and Black communities after identity loss, and how they work to find a voice through unity and self-discovery once again. However now, I use choir vocals and powerful beats as a bridge to illustrate the unwavering spirit and determination amongst the communities to rise above all challenges. My main message through this portion is to show how the Black and Indigenous communities have worked resiliently with strength and unity to find a voice, grow their identity, and emerge in the face of adversity. ')

#part 3 - rise 
#verse 2 function

def verse2RISE():

    #added sounds 
    fitMedia(choir1, 19, 35.5, 39.5)
    fitMedia(choir2, 19, 39.5, 43.7)
    fitMedia(vocals15, 21, 43.8, 44.8)
    fitMedia(vocals12, 22, 35.5, 43.8)
    fitMedia(vocals13, 23, 40.5, 42.1)
    fitMedia(vocals14, 23, 42.3, 44.25)
    fitMedia(strings1, 24, 44.4, 48.4)
    fitMedia(strings2, 24, 48.4, 50.2)
    fitMedia(strings3, 25, 44.2, 50.2)

    #loops
    for measure in range(31,36):
        makeBeat(bass1, 4, measure, "0--0--0---------")
        setEffect(4, VOLUME, GAIN, 0, measure, 2, measure)

    #repeats vocals "rise up" - as a sign of growth and strength 
    for measure in range(33, 37):
        fitMedia(vocals11, 21, measure, measure+0.7)

    #setEffects for VOLUME changes
    setEffect(19, VOLUME, GAIN, -30, 35.5, -25, 39.5)
    setEffect(19, VOLUME, GAIN, -25, 41, -35, 43.7)
    setEffect(21, VOLUME, GAIN, -30, 32.8, -5, 36)
    setEffect(21, VOLUME, GAIN, -5, 36, -8 ,37)
    setEffect(22, VOLUME, GAIN, -30, 35, 1, 37)
    setEffect(23, VOLUME, GAIN, -5)
    setEffect(25, VOLUME, GAIN, -30, 44.2, 0, 46)
    setEffect(25, VOLUME, GAIN, 0, 48, -30, 50.8)
    setEffect(24, VOLUME, GAIN, 0, 48.6, -30, 50.7)
    setEffect(24, VOLUME, GAIN, -30, 44.4, 0, 45)

print('Part 4 - Rising Together: The final part, I worked to create a crescendo, celebrating the unity and triumph of Indigenous and Black communities. Knowing the ongoing challenges faced by these communities, this part is to evoke togetherness amongst everyone and a collective effort to rise together, stronger, and more united than ever. I use vocals including "Rise up" to encourage all communities to build a more unified society without racial injustices. I also wanted to reflect the communities'' awareness of the past, and them taking a step forward.')

#function calls 
introTOGETHER(1, 7)
verse1CHALLENGES()
introTOGETHER(25, 31)
bridge()
verse2RISE()



