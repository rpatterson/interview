"""
Utilities for processing Wikipedia text.
"""


def match_question_answers(input_text):
    """
    Match answers to their questions based on the input paragraph.
    """
    lines = input_text.strip().split('\n')
    paragraph = lines[0]
    questions = lines[1:-1]
    answers = [answer.strip() for answer in lines[-1].split(';')]
    return '\n'.join(answers)
