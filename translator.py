from translate import Translator

start_text = './Translation-Project/text-input.txt'
output_text = './Translation-Project/text-output.txt'
back_trans = './Translation-Project/text-back-input.txt'

initial_lang = 'en'
trans_lang = 'ar'

with open(start_text, mode='w') as input_file:
    text1 = input_file.write('Hello Sondos, I hope your day is wonderful.')

translator = Translator(to_lang=trans_lang, from_lang=initial_lang)

try:
    with open(start_text, mode='r', encoding='utf-8') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        with open(output_text, mode='w', encoding='utf-8') as my_file2:
            my_file2.write(translation)
except FileNotFoundError as e:
    print('Check your file path silly!')

back_translator = Translator(to_lang=initial_lang, from_lang=trans_lang)

try:
    with open(output_text, mode='r', encoding='utf-8') as my_file3:
        text2 = my_file3.read()
        translation2 = back_translator.translate(text2)
        with open(back_trans, mode='w', encoding='utf-8') as my_file4:
            my_file4.write(translation2)
except FileNotFoundError as e:
    print('Check your file path silly!')
