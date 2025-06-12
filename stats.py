def get_num_words(text):
	words_split = text.split()
	counter = len(words_split)
	return counter

def character_count(text):
	lowercase = text.lower()
	counts = {}
	for l in lowercase:
		if l in counts:
			counts[l] += 1
		else:
			counts[l] = 1
	print(counts)
	return counts

def frequency_report(text):
	lowercase = text.lower()
	counts = {}
	for l in lowercase:
		if l in counts:
			counts[l] += 1
		else:
			counts[l] = 1
	report = []
	for char, num in counts.items():
		report.append({"char": char, "num": num})

	report.sort(reverse=True, key=lambda d: d["num"])
	return report

