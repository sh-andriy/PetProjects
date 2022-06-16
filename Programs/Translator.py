from googletrans import Translator, LANGUAGES

print('Available languages: \n')
for key, value in LANGUAGES.items():
    print(f'{key}: {value}')

text = str(input('Enter your text: '))
lan = str(input('Enter language you want to translate to: '))
translator = Translator()
output = translator.translate(text, dest=lan)
print(output.text)
