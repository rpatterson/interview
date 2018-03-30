"""
Test the wikipedia question answering implementation.
"""

import os
import unittest

import textblob

from interview import wikipedia


class TestWikipedia(unittest.TestCase):
    """
    Test the wikipedia question answering implementation.
    """

    SAMPLE = 'zebras'

    def setUp(self):
        """
        Load the samples for testing against.
        """
        super(TestWikipedia, self).setUp()

        with open(os.path.join(
                os.path.dirname(__file__), self.SAMPLE + '.input.txt'
        )) as input_file:
            self.input_text = input_file.read()
        with open(os.path.join(
                os.path.dirname(__file__), self.SAMPLE + '.output.txt'
        )) as output_file:
            self.expected_output_text = output_file.read()

    def test_input_format(self):
        """
        Test parsing the input format.
        """
        input_text = wikipedia.InputText(self.input_text)

        self.assertIn(
            'paragraph', dir(input_text), 'Missing parsed paragraph')
        self.assertIsInstance(
            input_text.paragraph, textblob.TextBlob,
            'Wrong parsed paragraph type')
        self.assertTrue(
            input_text.paragraph,
            'Missing parsed paragraph content')

        self.assertIn(
            'questions', dir(input_text), 'Missing parsed questions')
        self.assertIsInstance(
            input_text.questions, list,
            'Wrong parsed questions type')
        self.assertTrue(
            input_text.questions,
            'Missing parsed questions content')
        self.assertIsInstance(
            input_text.questions[0], textblob.TextBlob,
            'Wrong parsed question type')
        self.assertTrue(
            input_text.questions[0],
            'Missing parsed question content')

        self.assertIn(
            'answers', dir(input_text), 'Missing parsed answers')
        self.assertIsInstance(
            input_text.answers, list,
            'Wrong parsed answers type')
        self.assertTrue(
            input_text.answers,
            'Missing parsed answers content')
        self.assertIsInstance(
            input_text.answers[0], textblob.TextBlob,
            'Wrong parsed answer type')
        self.assertTrue(
            input_text.answers[0],
            'Missing parsed answer content')

    def test_answer_sentence_words(self):
        """
        Test mapping answers to sentences in the paragraph.
        """
        input_text = wikipedia.InputText(self.input_text)

        self.assertIn(
            'answer_sentence_words', dir(input_text),
            'Missing mapping of answers to sentences')
        self.assertIsInstance(
            input_text.answer_sentence_words, dict,
            'Wrong mapping of answers to sentences type')
        self.assertTrue(
            input_text.answer_sentence_words,
            'Missing mapping of answers to sentences content')
        self.assertIsInstance(
            input_text.answer_sentence_words[wikipedia.NormalizedAnswer(
                input_text.answers[0])],
            set,
            'Wrong mapping of answer to sentence type')
        self.assertTrue(
            input_text.answer_sentence_words[wikipedia.NormalizedAnswer(
                input_text.answers[0])],
            'Missing mapping of answer to sentence content')

    def test_sample(self):
        """
        Test the sample input against the sample output.
        """
        output_text = wikipedia.match_question_answers(self.input_text)
        self.assertEqual(
            output_text, self.expected_output_text,
            'Did not match expected output')
