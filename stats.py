def count_words(text):
  word_count = 0
  words_from_text = text.split()
  word_count = len(words_from_text)
  return word_count

def count_characters(text):
  char_counter = {}

  for char in text:
    if char.lower() in char_counter:
      char_counter[char.lower()] += 1
    else:
      char_counter[char.lower()] = 1

  return char_counter
