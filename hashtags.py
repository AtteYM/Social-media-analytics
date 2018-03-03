

#Goes through string and makes a list containing all tags which start with '#'
def get_hashtagslist(string):
    ret = []
    s=''
    hashtag = False
    for char in string:
        if char=='#':
            hashtag = True
            if s:
                ret.append(s)
                s=''
#            continue
#remove previous commentmark if you want to exclude # from words

        #define characters that aren´t included in tags
        #in other words which characters define end of tag
        if hashtag and char in [' ',"'",'’','!','|','\n','.',',','(',')',':','{','}, '] and s:
            ret.append(s)
            s=''
            hashtag=False
        #save tag in to list
        if hashtag:
            s+=char

    #save last tag in to list
    if s:
        ret.append(s)

    #return list of tags used in tweet
    return list(set([word for word in ret if len(ret)>1 and len(ret)<20]))
