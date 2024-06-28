def count_words(phrase):
    def normalize(word):
        word = word.lower()
        word = ''.join(c for c in word if c.isalnum())
        return word

    words = phrase.split()
    
    normalized_words = [
        normalize(word)
        for word in words
    ]
    
    total_words = len(normalized_words)
    
    unique_words = set(normalized_words)
    total_unique_words = len(unique_words)
    
    return total_words, total_unique_words

phrase = """Modern information and communication systems are based on the reliable and efficient
transmission of information. Channels encountered in practical applications are usually
disturbed regardless of whether they correspond to information transmission over noisy
and time-variant mobile radio channels or to information transmission on optical discs that
might be damaged by scratches. Owing to these disturbances, appropriate channel coding
schemes have to be employed such that errors within the transmitted information can be
detected or even corrected. To this end, channel coding theory provides suitable coding
schemes for error detection and error correction. Besides good code characteristics with
respect to the number of errors that can be detected or corrected, the complexity of the
architectures used for implementing the encoding and decoding algorithms is important for
practical applications."""

total_words, total_unique_words = count_words(phrase)
print("Total words:", total_words)
print("Total unique words:", total_unique_words)
