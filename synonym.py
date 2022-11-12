def synonym_antonym_extractor(phrase):
     from nltk.corpus import wordnet
     synonyms = []
     antonyms = []

     for syn in wordnet.synsets(phrase):
          for l in syn.lemmas():
               synonyms.append(l.name())
               if l.antonyms():
                    antonyms.append(l.antonyms()[0].name())

     return (set(synonyms), set(antonyms))

def get_synonym(phrase):
  result = []
  synonyms, antonyms = synonym_antonym_extractor(phrase)
  for synonym in synonyms:
    result.append(synonym)

  return result
  
def get_antonym(phrase):
  result = []
  synonyms, antonyms = synonym_antonym_extractor(phrase)
  for antonym in antonyms:
    result.append(antonym)

  return result