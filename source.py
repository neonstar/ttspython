from gtts import gTTS
import random
from colored import fg, bg, attr
color = bg('indian_red_1a') + fg('white')
reset = attr('reset')

print('Print something you want to tts')
def main():
	a = input()
	b = a
	print(color + "You have printed: " + a + reset)
	tts = gTTS(a, lang = 'ru')
	if len(a) > 25:
		print('Saving...')
		tts.save(str(len(a))+str("@")+str(random.randint(1,9999))+'.ogg')
		print('Saving complete, name of file is: '+ str(len(a))+str("@")+str(random.randint(1,9999))+'.ogg')
	else:
		print('Saving...')
		tts.save((str(a)) +'.ogg')
		print('Saving complete, name of file is: ' + (str(a)) +'.ogg')
	main()

main()