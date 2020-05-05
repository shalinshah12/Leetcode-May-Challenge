def can(ransomNote,magazine):
    ransom_freq = {} 
    magazine_freq = {}  
    for i in ransomNote: 
        if i in ransom_freq: 
            ransom_freq[i] += 1
        else: 
            ransom_freq[i] = 1
    for i in magazine: 
        if i in magazine_freq: 
            magazine_freq[i] += 1
        else: 
            magazine_freq[i] = 1
    print(ransom_freq['a'])
    print(magazine_freq['a'])
    return all(ransom_freq[key] <= magazine_freq[key] for key in ransom_freq)

ransomNote = "a"
magazine = "b"
print(can(ransomNote,magazine))
