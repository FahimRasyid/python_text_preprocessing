import re

# Fill text with desirable text
text = 'Your text here...'

# Replace ")" and store text into list
text_key = text.replace(")", " ")
text_key = text_key.split()
# remove digits, special characters and convert to lowercase
for k in range(len(text_key)):
    text_key[k] = text_key[k].lower()
    text_key[k] = text_key[k].replace("_", " ")
    text_key[k] = text_key[k].replace("-", " ")
# convert list to set, in order to remove duplicate tokens
text_tokens = set(text_key)  
# Remove Stop Words (You can add words which you want to remove into this list)
stopwords = ["ourselves", "hers", "between", "yourself", "but", "again",
            "there", "about", "once", "during", "out", "very", "having",
            "with", "they", "own", "an", "be", "some", "for", "do", "its",
            "yours", "such", "into", "of", "most", "itself", "other",
            'off', "is", "s", "am", "or", "who", "as", "from", "him", "each",
            "the", "themselves", "until", "below", "are", "we", "these", "your",
            "his", "through", "don", "nor", "me", "were", "her", "more",
            "himself", "this", "down", "should", "our", "their", "while",
            "above", "both", "up", "to", "ours", "had", "she", "all", "no",
            "when", "at", "any", "before", "them", "same", "and", "been",
            "have", "in", "will", "on", "does", "yourselves", "then", "that",
            "because", "what", "over", "why", "so", "can", "did", "not", "now",
            "under", "he", "you", "herself", "has", "just", "where", "too",
            "only", "myself", "which", "those", "i", "after", "few", "whom",
            "t", "being", "if", "theirs", "my", "against", "a", "by", "doing",
            "it", "how", "further", "was", "here", "than", "due", "", " "]
result = []
for word in text_tokens:
    if word not in stopwords:
        result.append(word) 

# Print result
print(result)
