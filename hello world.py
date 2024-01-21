num=int(input())#get a number
sentences =[] #hold the sentences

for i in range(num): #get the sentences
    phrase = input()
    sentences.append(phrase)
    
for i in range(len(sentences)):
    print(sentences[i])
