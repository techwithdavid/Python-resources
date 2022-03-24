from gtts import gTTS
from playsound import playsound
text_val = 'Sharon es hermosa y peshosha.'
language = 'es'
obj = gTTS(text=text_val, lang=language, slow=False)
obj.save("exam.mp3")
playsound("exam.mp3")
