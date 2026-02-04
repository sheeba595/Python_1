# Objective: 
# Create a program that counts the frequency of each word in a given sentence and 
# displays the result in a neat format. 

sentence=input("Enter a sentence: ").lower().split(" ")
word_count={}
for word in sentence:
    if word in word_count:
        word_count[word]+=1
        
    else:
        word_count[word]=1
for word,count in word_count.items():
    print(f"{word}=>{count}")
    