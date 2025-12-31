from stats import count_words, count_characters, sort_characters_count_desc

def get_book_text(file_path):
  file_contents = None
  with open(file_path) as opened_file:
    file_contents = opened_file.read()
  return file_contents

def main():
  file_contents = get_book_text("books/frankenstein.txt")
  char_counter_sorted = sort_characters_count_desc(count_characters(file_contents))
  print("============ BOOKBOT ============")
  print("Analyzing book found at books/frankenstein.txt...")
  print("----------- Word Count ----------")
  print(f"Found {count_words(file_contents)} total words")
  print("--------- Character Count -------")
  for counter in char_counter_sorted:
    print(f"{counter["char"]}: {counter["num"]}")
  print("============= END ===============")


main()
