def duplicate_count(text):
    
    lText = list(text)
    chars = []
    dupChars = [] 
    
    for i in lText:
        if i.lower() in chars and i.lower() not in dupChars:
            dupChars.append(i.lower())
        else:
            chars.append(i.lower())
           
    return len(dupChars)