

if __name__ == '__main__':
  wordstring = 'it was the best of times it was the worst of times '
  wordstring += 'it was the age of wisdom it was the age of foolishness'

  wordlist= wordstring.split()
  freq = []
  for w in wordlist:
    freq.append(wordlist.count(w))

  dictionary = {}
  for word, freq in zip ( wordlist, freq):
    dictionary[word] = freq


  print(sorted(dictionary.items(), key = lambda x: x[1], reverse = True))

  #print(dictionary)