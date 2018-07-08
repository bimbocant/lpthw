class ParserError(Exception):
    pass

class Sentence(object):
    def __init__(self,subject,verb,obj):
        self.subject=subject[1]
        self.verb=verb[1]
        self.obj=obj[1]

class SentenceParser(object):
    def __init__(self):
        pass

    def peek(self,word_list):
        if word_list:
            word=word_list[0]
            return word[0]
        else:
            return None

    def match(self,word_list,expecting):
        if word_list:
            word=word_list.pop(0)
            if word[0]==expecting:
                return word
            else:
                return None
        else:
            return None

    def skip(self,word_list,word_type):

        while self.peek(word_list)==word_type:
            self.match(word_list,word_type)

    def parse_verb(self,word_list):
        self.skip(word_list,'stop')

        if self.peek(word_list)=='verb':
            return self.match(word_list,'verb')
        else:
            raise ParserError("Expected a verb next")

    def parse_obj(self,word_list):

        self.skip(word_list,'stop')
        next_word=self.peek(word_list)

        if next_word=='noun':
            return self.match(word_list,'noun')
        elif next_word=='direction':
            return self.match(word_list,'direction')
        else:
            raise ParserError("Expected a noun next")

    def parse_subject(self,word_list):
        self.skip(word_list,'stop')
        next_word=self.peek(word_list)
        print('next_word',next_word)

        if next_word=='noun':
            return self.match(word_list,'noun')
        elif next_word=='verb':
            return ('noun','player')
        else:
            raise ParserError('Expected a verb next')

    def parse_sentence(self,word_list):
        subj=self.parse_subject(word_list)
        verb=self.parse_verb(word_list)
        obj=self.parse_obj(word_list)

        return Sentence(subj,verb,obj)
