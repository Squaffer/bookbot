import sys
from stats import word_count, count_characters_in_file, sort_on



def get_book_text(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()
    return text

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]

    text_excerpt = get_book_text(filepath)
    num_words = word_count(text_excerpt)
    characters = count_characters_in_file(text_excerpt)


    sorted_character_list = [{'char': k, 'num': v} for k, v in sorted(characters.items())]
    sorted_character_list.sort(reverse=True, key=sort_on)
    
    print(f"""============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------\nFound {num_words} total words\n--------- Character Count -------""") 
    for item in sorted_character_list:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['num']}")
          
    print("============= END ===============")
    
          
          
          
            

main()