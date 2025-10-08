from survey import AnonymousSurvey


question = "What language did you first learn to speak?"
language_survey = AnonymousSurvey(question)

responses = ['English', 'Spanish', 'Mandarin', 'English', 'Arabic',
            'Mandarin', 'English']

for reponse in responses:
    language_survey.store_response(reponse)

language_survey.delete_response('English')
print(language_survey.responses)
print(language_survey.tally_results())

print()
language_survey.delete_response('Arabic')
print(language_survey.responses)
print(language_survey.tally_results())