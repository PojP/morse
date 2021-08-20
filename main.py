morse = {
'а':'.-',
'б':'-...',
'в':'.--',
'г':'--.',
'д':'-..',
'е':'.',
'ё':'.',
'ж':'...-',
'з':'--..',
'и':'..',
'й':'.---',
'к':'-.-',
'л':'.-..',
'м':'--',
'н':'-.',
'о':'---',
'п':'.--.',
'р':'.-.',
'с':'...',
'т':'-',
'у':'..-',
'ф':'..-.',
'х':'....',
'ц':'-.-.',
'ч':'---.',
'ш':'----',
'щ':'--.-',
'ъ':'.--.-.',
'ы':'-.--',
'ь':'-..-',
'э':'..-..',
'ю':'..--',
'я':'.-.-',
}

def translate(natural_lang):
    morse_lang=''
    for i in range(len(natural_lang)):
        try:
            morse_lang+=morse[natural_lang[i]]
        except:
            morse_lang+=natural_lang[i]
            
    print(morse_lang)

text = input("Enter the text:\n")
translate(text)


