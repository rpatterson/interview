"""
Test the wikipedia question answering implementation.
"""

import os
import unittest

from interview import wikipedia


class TestWikipedia(unittest.TestCase):
    """
    Test the wikipedia question answering implementation.
    """

    SAMPLE = 'zebras'

    def test_sample(self):
        """
        Test the sample input against the sample output.
        """
        with open(os.path.join(
                os.path.dirname(__file__), self.SAMPLE + '.input.txt'
        )) as input_file:
            input_text = input_file.read()
        with open(os.path.join(
                os.path.dirname(__file__), self.SAMPLE + '.output.txt'
        )) as output_file:
            expected_output_text = output_file.read()
        output_text = wikipedia.match_question_answers(input_text)
        self.assertEqual(
            output_text, expected_output_text,
            'Did not match expected output')
