def translate_en_zh(phrase):
  import googletrans
  from googletrans import Translator
  translator = Translator()
  return translator.translate(phrase, src='en', dest='zh-tw').text
  
def translate_zh_en(phrase):
  import googletrans
  from googletrans import Translator
  translator = Translator()
  return translator.translate(phrase, src='zh-tw', dest='en').text