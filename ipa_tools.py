cmudict = {}

def get_ipa(phrase):
  phrase = phrase.upper()
  if len(cmudict) > 0:
    if phrase in cmudict:
      return cmudict[phrase]
    else:
      return ""
  else:
    import os
    try:
      file = open('int3106/cmudict-0.7b-ipa.txt', 'r')
      while True:
        line = file.readline()
        if not line:
          break
        words = line.strip().split('\t')
        cmudict[words[0]] = words[1]
      file.close()
    except Exception:
      return "ERROR: file doesn't exist"
    
    if phrase in cmudict:
      return cmudict[phrase]
    else:
      return ""    