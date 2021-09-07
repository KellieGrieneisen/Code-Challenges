def missingWords(s, t):
    # Write your code here
    missing=[]
    string_one_words = s.split()
    string_two_words=t.split()
    
    for i,word in enumerate(string_one_words):
        if not string_two_words:
            missing.append(word)
        elif word != string_two_words[0]:
            missing.append(word)
        elif word == string_two_words[0]:
            string_two_words.pop(0)
        
    
    return missing