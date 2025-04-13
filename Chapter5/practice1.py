words = {
	"cat": "billy",
	"dog": "Kutta",
	"English" : "Angrezi",
}

word = input("Enter a word: ")



print(words.get(word, "Word not found")) # This will not raise an error if the word is not found

print(words[word])	# This will raise a KeyError if the word is not found