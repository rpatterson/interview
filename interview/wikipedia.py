"""
Utilities for processing Wikipedia text.
"""

import textblob


class InputText(str):
    """
    Parse the input format into a paragraph, questions and answers.
    """

    def __init__(self, input_text=''):
        """
        Parse the input format into a paragraph, questions and answers.
        """
        super(InputText, self).__init__()

        lines = input_text.strip().split('\n')
        # "The first line contains a short paragraph of text from
        # Wikipedia."
        self.paragraph = textblob.TextBlob(lines[0])
        # "Lines 2 to 6 contain a total of 5 questions."
        # NOTE Because we can assume the last line contains the
        # answers, we can support an arbitrary number of questions
        self.questions = [
            textblob.TextBlob(question) for question in lines[1:-1]]
        # "Line 7 contains all the five answers, which are jumbled up."
        self.answers = [
            textblob.TextBlob(answer.strip())
            for answer in lines[-1].split(';')]
        # TODO the above could be changed to be processed lazily on
        # first access to avoid the TextBlob processing time if ever
        # there was significant use where only some of the attributes
        # are referenced.  Before doing so, confirm that TextBlob
        # doesn't already to lazy processing

        # Map answers to their sentences so we can compare questions
        # to prospective sentences
        self.answer_sentence_words = {}
        for sentence in self.paragraph.sentences:
            for answer in self.answers:
                answer_words = tuple(answer.words)
                # Normalize punctuation using spaces
                if ' '.join(answer_words) in ' '.join(sentence.words):
                    self.answer_sentence_words[answer] = set(sentence.words)
                    break
        # TODO Again, the above could be changed to be processed
        # lazily on first access to avoid the processing time if ever
        # there was significant use where `answer_sentence_words`
        # isn't used


def match_question_answers(input_text):
    """
    Match answers to their questions based on the input paragraph.
    """
    parsed = InputText(input_text)
    return '\n'.join(str(answer) for answer in parsed.answers) + '\n'
