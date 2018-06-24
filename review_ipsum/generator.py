import random
from .sentence import Sentence

class Generator:

    def __init__(self):
        self.sentence = Sentence()
    
    def create_review(self, number_of_sentences):
        review = ''
        for _ in range(number_of_sentences):
            review += '{}'.format(
                self.sentence.sentences[
                    random.randint(0, self.sentence.total_sentences - 1)
                ]
            )
            if _ != number_of_sentences:
                review += ' '
        return review
