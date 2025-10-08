"""This class models an anonymous survey."""

class AnonymousSurvey:
    """Collect anonymous, single-response answers to a survey question."""

    def __init__(self, question):
        """Store a question and prepare to store responses."""
        # The question
        self.question = question
        
        # List to store each individual response
        self.responses = []

        # Dictionary to store each type of response (as keys) 
        #  and tallies for each response type (as values)
        self.tallied_responses = {}

    def list_results(self):
        """Print all the responses in a list going down the screen."""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")

    def show_question(self):
        """Show the survey question."""
        print(self.question)

    def store_response(self, response):
        """Store a single response to the survey."""
        # Add to list of responses.
        self.responses.append(response)

        # Store in dictionary.
        if response.lower().strip() not in self.tallied_responses:
            self.tallied_responses[f"{response.lower().strip()}"] = 1
        else:
            self.tallied_responses[f"{response.lower().strip()}"] += 1

    def tally_results(self):
        """Print the tallied results in order of popularity."""
        print("Survey results:")

        # Sort tallied responses by popularity.
        self.tallied_responses = {k: v for k, v in sorted(self.tallied_responses.items(), key=lambda response: response[1], reverse=True)}

        # Print the results.
        for response_type, response_quantity in self.tallied_responses.items():
            print(f"- {response_type}:\t{response_quantity}")
