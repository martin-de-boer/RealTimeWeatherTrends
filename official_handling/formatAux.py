import datetime as dt
import string

#find the next date and time, the given time occurs at
def next_datetime(current: dt.datetime, hour: int, **kwargs) -> dt.datetime:
    repl = current.replace(hour=hour, **kwargs)
    while repl <= current:
        repl = repl + dt.timedelta(days=1)
    return repl


#extract a list of tags from a text (starts at a "#" ends at first " " or punctuation)
def extract_tags(text):
    tags = []
    #split the list based on "#"
    for i in range(1,len(text.split('#'))):
        result = []
        
        #find the first " " or punctuation
        for char in text.split('#')[i]:
            if char in string.punctuation + ' ':
                break
            result.append(char)
        ''.join(result)
        
        tags.append(''.join(result))
    
    return tags