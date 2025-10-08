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
        self.responses = ['English', 'Spanish', 'Mandarin', 'English', 'Arabic']

    def test_store_single_response(self):
        """Test that a single response question is stored properly."""
        self.survey.store_response(self.responses[0])

        # Test that the response is stored in the list.
        self.assertIn(self.responses[0], self.survey.responses)

        # Test that the response is stored in the dictionary.
        self.assertEqual(self.survey.tallied_responses[
            f"{self.responses[0].lower()}"], 1)

    def test_store_three_responses(self):
        """Tests that three individual responses are stored properly."""
        # Store the responses in the survey.
        for response in self.responses:
            self.survey.store_response(response)

        # Test that responses are stored in the list.
        for response in self.responses:
            self.assertIn(response, self.survey.responses)

        # Test that reponses are stored in the dictionary.
            #  Create a copy of the responses in lower case.
        responses = [response.lower() for response in self.responses]

            # Keep count of similar responses and check if they match the
            #  tallied response count.
        while responses:
            current_response = responses.pop(0)
            current_response_count = 1
            for response in responses:
                if current_response == response:
                    responses.remove(response)
                    current_response_count += 1

            self.assertEqual(self.survey.tallied_responses[f"{current_response}"], current_response_count)


if __name__ == '__main__':
    unittest.main()