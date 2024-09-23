import gensim.downloader as api

# Load the GloVe Twitter-25 embedding model
model = api.load("glove-twitter-25")

# Function to compute and display the difference between two word vectors
def display_vector_difference():
    word1 = input("Enter the first word: ")
    word2 = input("Enter the second word: ")
    
    # Check if both words exist in the model's vocabulary
    if word1 in model.key_to_index and word2 in model.key_to_index:
        vector1 = model.get_vector(word1)
        vector2 = model.get_vector(word2)
        
        # Compute the difference between the two vectors
        difference = vector1 - vector2
        
        print(f"Vector for '{word1}' = {vector1}")
        print(f"Vector for '{word2}' = {vector2}")
        print(f"Difference between '{word1}' and '{word2}' = {difference}")
    else:
        missing_words = [word for word in [word1, word2] if word not in model.key_to_index]
        print(f"Word(s) not found in the model's vocabulary: {', '.join(missing_words)}")

if __name__ == "__main__":
    display_vector_difference()