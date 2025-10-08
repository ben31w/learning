from survey import AnonymousSurvey

# Define a question, and make a survery.
question = "What language did you first learn to speak?"
survey = AnonymousSurvey(question)

# Show the question, and store responses to the question.
survey.show_question()
print("(enter 'q' when you are done entering responses.)\n")

while True:
    response = input("Language: ")
    if response.strip() == 'q':
        break
    survey.store_response(response)

# Once the user quits, display results
print("\nThank you for everyone who participated in this anonymous survey!")
survey.tally_results()