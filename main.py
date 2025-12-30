from stats import count_words, count_characters

def get_book_text(file_path):
  file_contents = None
  with open(file_path) as opened_file:
    file_contents = opened_file.read()
  return file_contents

def main():
  file_contents = get_book_text("books/frankenstein.txt")
  print(f"Found {count_words(file_contents)} total words")
  print(count_characters(file_contents))


main()
