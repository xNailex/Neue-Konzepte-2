def reverse_words(sentence):
    """
    Reverses the order of words in a given sentence.

    Args:
        sentence (str): The input sentence to reverse.

    Returns:
        str: The sentence with the order of words reversed.
    """
    # Split the sentence into words
    words = sentence.split()
    
    # Reverse the list of words
    #reversed_words = words[::-1] <- Alternative method
    reversed_words = reversed(words)
    
    # Join the reversed list of words back into a string
    reversed_sentence = ' '.join(reversed_words)
    
    return reversed_sentence

sentence = "Hello world, Python is fun"

print(reverse_words(sentence))