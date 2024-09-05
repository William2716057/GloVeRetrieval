import gensim.downloader as api

#model
model = api.load("glove-twitter-25")

#function to get vectors for word
def display_vector():
    word = input("Enter word to display vector: ")
    
    #check if word exists in model
    if word in model:
        vector = model[word]
        print("vector for ", word, "=", vector)
    else:
        print("word not found")
        
if __name__ == "__main__":
    display_vector()