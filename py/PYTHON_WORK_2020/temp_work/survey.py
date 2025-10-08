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

    def delete_response(self, response):
        """Deletes a single response."""
        if response in self.responses:
            # Remove from list.
            self.responses.remove(response)

            # Subtract from dictionary.
            if self.tallied_responses[f"{response.lower().strip()}"] == 1:
                del self.tallied_responses[f"{response.lower().strip()}"]
            elif self.tallied_responses[f"{response.lower().strip()}"] > 1:
                self.tallied_responses[f"{response.lower().strip()}"] -= 1
        else:
            pass

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
        """Print the tallied results."""
        print("Survey results:")
        print(self.tallied_responses)
