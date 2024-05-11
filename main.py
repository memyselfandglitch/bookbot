def count_words(msg):
    words=msg.split()
    return words

def count_chars(words):
    lowercase_dict = {chr(i): 0 for i in range(ord('a'), ord('z')+1)}
    for word in words:
        for ch in word:
            if(ch.isalpha()):
                lowercase_dict[ch.lower()]+=1
    return (lowercase_dict)

def sortOn(dict):
    return dict["frequency"]

if __name__ == "__main__":
    with open('./books/frankenstein.txt') as f:
        file_contents=f.read()
        words=count_words(file_contents)
        lowercase_dict=count_chars(words)
        new_list = [{'alphabet': key, 'frequency': value} for key, value in lowercase_dict.items()]
        new_list.sort(reverse=True,key=sortOn)
        print("Report of book is as follows")
        print("Number of words is ", len(words))
        for item in new_list:
            ch=item["alphabet"]
            freq=item["frequency"]
            print('The',ch,'character was found ', freq,'times' )

        


