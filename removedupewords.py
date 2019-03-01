# Python 3 program to remove the
# duplicates words from a sentence 
#the boy and the boy

def removeDups(sentence):
    sentence = sentence.split()
    new_sentence = []
    for word in sentence:
        if word not in new_sentence:
            new_sentence.append(word)
    return ' '.join(new_sentence)
            

sentence = "the boy and the boy"
print(removeDups(sentence))
