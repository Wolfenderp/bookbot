from stats import get_num_words
from stats import get_num_characters
from stats import characters_list_sorting

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    word_count = get_num_words(text)
    
    # Get character counts
    char_counts = get_num_characters(text)
    
    # Sort the character counts
    sorted_chars = characters_list_sorting(char_counts)
    
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    # Loop through each dictionary in the sorted list
    for char_dict in sorted_chars:
        char = char_dict["char"]  # Get the character
        count = char_dict["count"]  # Get the count
        
        # Only print alphabetical characters
        if char.isalpha():
            print(f"{char}: {count}")
    
    print("============= END ===============")

main()
