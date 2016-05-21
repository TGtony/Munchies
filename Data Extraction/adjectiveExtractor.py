import nltk
import os, sys, time

def main():

	filename = "the_review_data.txt"
	read_file = open(filename, "r")

	write_file = open("review_data_output.txt", "w")

	count = 0


	size = os.stat("C:/Users/Jaber/Documents/Capstone/Munchies/review_data_output.txt")

	for lines in read_file:
		write_file.write(lines)
		reviewText = read_file.readline()
		listOfAdjectives = performNLTK(reviewText)

		write_file.write("%s\n" %listOfAdjectives)








def performNLTK(sentence):
	tokens = nltk.word_tokenize(sentence)

	tagged = nltk.pos_tag(tokens)

	listOfAdjectives = []

	for words in tagged:
		if words[1] == 'JJ': #adjective
			listOfAdjectives.append(words[0])

	return listOfAdjectives





main()


