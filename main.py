import sys
from stats import get_num_words
#from stats import character_count
from stats import frequency_report
def get_book_text(filepath):
	with open(filepath) as f:
		text = f.read()
		return text

def main():
	if len(sys.argv) == 2:
		book = sys.argv[1]
		text = get_book_text(book)
		counter = get_num_words(text)
	#print (f"{counter} words found in the document") 

	#counts = character_count(text)
		sorted_counts = frequency_report(text)

		print(f'''============ BOOKBOT ============
Analyzing book found at {book}...
----------- Word Count ----------
Found {counter} total words
--------- Character Count -------''')
		for item in sorted_counts:
			if item["char"].isalpha():
				print(f'{item["char"]}: {item["num"]}')
		print("============= END ===============")
	else:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)

main()
