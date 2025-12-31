def sort_on(items):
  return items["num"]

def count_words(text):
  word_count = 0
  words_from_text = text.split()
  word_count = len(words_from_text)
  return word_count

def count_characters(text):
  char_counter = []
  exists = False

  for char in text:
    if not char.isalpha():
      continue
    if len(char_counter) == 0:
      char_counter.append({ "char": char.lower(), "num": 1 })
    else:
      for counter in char_counter:
        if counter["char"] == char.lower():
          exists = True
          break
      if exists:
        for counter in char_counter:
          if counter["char"] == char.lower():
            counter["num"] += 1
      else:
        char_counter.append({ "char": char.lower(), "num": 1 })

  return char_counter

def sort_characters_count_desc(characters_list):
  characters_list.sort(reverse=True, key=sort_on)
  return characters_list
