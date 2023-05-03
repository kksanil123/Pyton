sentence = "My name is Michele"
words = sentence.split(' ')
mod_sentence =""
for i in range(0,len(words)):
    mod_sentence = mod_sentence +' '+str(words[-i-1])

print(mod_sentence)

