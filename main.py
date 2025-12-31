import sys

from stats import count_words, count_characters, sort_characters_count_desc

def get_book_text(file_path):
  file_contents = None
  with open(file_path) as opened_file:
    file_contents = opened_file.read()
  return file_contents

def main():
  book_file_path = None
  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  else:
    book_file_path = sys.argv[1]

  file_contents = get_book_text(book_file_path)
  char_counter_sorted = sort_characters_count_desc(count_characters(file_contents))
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {book_file_path}...")
  print("----------- Word Count ----------")
  print(f"Found {count_words(file_contents)} total words")
  print("--------- Character Count -------")
  for counter in char_counter_sorted:
    print(f"{counter["char"]}: {counter["num"]}")
  print("============= END ===============")


main()
