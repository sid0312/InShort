import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

def naive_summarize(text="Nothing was entered"):

  stop_words = set(stopwords.words("english")) 
  words = word_tokenize(text) 
  word_count = {}
  for word in words:
    word = word.lower()
    if word in stop_words:
      continue
    if word in word_count:
      word_count[word] +=1
    else:
      word_count[word] = 1
  sentences = sent_tokenize(text)
  sentence_score = {}
  for sentence in sentences:
    for word,frequency in word_count.items():
      if word in sentence.lower():
        if sentence in sentence_score:
          sentence_score[sentence] += frequency
        else:
          sentence_score[sentence] = frequency
  total_score = 0
  for sentence in sentence_score:
    total_score +=sentence_score[sentence]
  average_score = total_score // len(sentence_score)
  summary = """ """
  for sentence in sentences:
    if (sentence in sentence_score) and (sentence_score[sentence] > (1.2 * average_score)):
      summary += " " + sentence
  return summary
