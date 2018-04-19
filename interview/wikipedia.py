"""
Utilities for processing Wikipedia text.
"""

import textblob


class NormalizedAnswer(str):
    """
    An answer whose hash is based on the normalized words.
    """

    def __init__(self, answer):
        """
        An answer whose hash is based on the normalized words.
        """
        super(NormalizedAnswer, self).__init__()

        self.original = answer

        answer_words = tuple(answer.words)
        # Normalize punctuation using spaces
        self.normalized = ' '.join(answer_words).lower()

    def __hash__(self):
        """
        Use the nomalized answer as a hash, e.g. the key in a dictionary.
        """
        return hash(self.normalized)


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
                normalized_answer = NormalizedAnswer(answer)
                if normalized_answer.normalized in ' '.join(
                        sentence.words).lower():
                    self.answer_sentence_words[
                        normalized_answer] = set(sentence.words)
                    break
        # TODO Again, the above could be changed to be processed
        # lazily on first access to avoid the processing time if ever
        # there was significant use where `answer_sentence_words`
        # isn't used

    def match_question_answers(self):
        """
        Match answers to their questions based on the paragraph sentences.
        """
        question_answers = []
        for question in self.questions:
            word_intersection_max = 0
            words = set(word.lower() for word in question.words)
            best_answer = NormalizedAnswer(textblob.TextBlob(''))
            for answer, sentence_words in self.answer_sentence_words.items():
                sentence_intersection_len = len(
                    words.intersection(sentence_words))
                if sentence_intersection_len > word_intersection_max:
                    word_intersection_max = sentence_intersection_len
                    best_answer = answer

            question_answers.append(best_answer.original)

        return question_answers


def match_question_answers(input_text):
    """
    Match answers to their questions based on the input paragraph.
    """
    parsed = InputText(input_text)
    return '\n'.join(
        str(answer) for answer in parsed.match_question_answers()) + '\n'
