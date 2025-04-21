def word_count(text):
        words = text.split()
        return len(words)

def char_count(text):
        character_counts = {}
        for letters in text:
                l_case = letters.lower()
                if l_case in character_counts:
                        character_counts[l_case] += 1
                else:
                        character_counts[l_case] = 1
        return character_counts

def sort_on(c_counts):
	return c_counts["num"]

def character_counts_dict_to_list(character_counts_dict):
	sorted_list = []
	for character in character_counts_dict:
		sorted_list.append({"char": character, "num": character_counts_dict[character]})
	sorted_list.sort(reverse=True, key=sort_on)
	return sorted_list
