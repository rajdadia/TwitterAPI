import nltk

class Analyzer():


    def __init__(self, positives, negatives):

        self.pos=set()
        posfile=open(positives,"r")
        for line in posfile:
            if line.startswith(';') == False:
                self.pos.add(line.rstrip("\n"))

        self.neg=set()
        negfile=open(negatives,"r")
        for line in negfile:
            if line.startswith(';') == False:
                self.neg.add(line.rstrip("\n"))




    def analyze(self, text):
        self.text=text
        counter=0
        tokenizer = nltk.tokenize.TweetTokenizer()
        tokens = tokenizer.tokenize(self.text)
        for s in tokens:
            s=s.lower()
            if s in self.neg:
                counter=counter-1
            elif s in self.pos:
                counter=counter+1
        return counter



#nltk.tokenize.api.TokenizerI   nltk.tokenize.TweetTokenizer