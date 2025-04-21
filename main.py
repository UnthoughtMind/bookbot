import sys
from stats import word_count, char_count, character_counts_dict_to_list

def main():
	try:
		print(sys.argv[1])
	except Exception:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)

	path = sys.argv[1]
	text = get_text(path)
	count = word_count(text)
	chars = char_count(text)
	sort = character_counts_dict_to_list(chars)

	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {path}...")
	print("----------- Word Count ----------")
	print(f"Found {count} total words")
	print("--------- Character Count -------")
	for item in sort:
		if item["char"].isalpha():
			print(f"{item['char']}: {item['num']}")
	print("============= END ===============")

def get_text(path):
        with open(path) as f:
                return f.read()
main()
