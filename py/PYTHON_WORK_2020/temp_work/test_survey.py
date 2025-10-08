import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey"""

    # the unittest.TestCase class has a setUp() method that allows you to create
    #  objects that can be used in each test_ method. When you define a setUp()
    #  method in a TestCase class, Python runs the setUp() method before running
    #  each test_ method.
    def setUp(self):
        """
        Create a survey and a set of responses for use in all test methods.
        """
        question = "What language did you first learn to speak?"
        self.survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin', 'English', 'Arabic',
            'Mandarin', 'English']

    def test_store_single_response(self):
        """Test that a single response question is stored properly."""
        self.survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.survey.responses)

    def test_store_three_responses(self):
        """Tests that three individual responses are stored properly."""
        for response in self.responses:
            self.survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.survey.responses)

    def test_delete_last_response(self):
        """
        Tests that the last/most recently added response can be deleted using
        delete_response().
        """
        last_response = self.responses[len(self.responses) - 1]
        self.survey.delete_response(last_response)
        self.assertEqual(self.survey.tallied_responses[f"{last_response.lower().strip()}"], 2)

if __name__ == '__main__':
    unittest.main()