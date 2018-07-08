

lex=[('direction','north'),
            ('direction','south'),
            ('direction','east'),
            ('verb','go'),
            ('verb','eat'),
            ('verb','kill'),
            ('stop','the'),
            ('stop','in'),
            ('stop','of'),
            ('noun','princess'),
            ('noun','bear')]

#returns the tuple of the given direction
def scan(string):
    word_list=string.split()
    print('word_list',word_list)
    result=[]
    not_found=[]
    appended=False
    for word in word_list:
        for t in lex:
                if word in t and appended==False:
                    result.append(t)
                    appended=True
        #word is not in lex so it is a number or an error
        if appended==False:
            try:
                num=int(word)
                result.append(('number',num))
            except ValueError as e:
                result.append(('error',word))
        appended=False


    print("result",result)
    return result
