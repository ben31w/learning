favorite_languages = {
    'jen': ['python', 'java'],
    'claire': ['c'],
    'robert': ['ruby', 'go'],
    'phil': ['python', 'pascal', 'haskell'],
    'courtney': ['java', 'pascal'],
    'eric': ['python'],
    'kyle': ['python', 'javascript'],
}

for name, languages in favorite_languages.items():
    # If a person only has one favorite language, use singular wording.
    if len(languages) == 1:
        print(f"\n{name.title()}'s favorite language is:")
    #  If a person has multiple favorite languages, use plural wording.
    else:
        print(f"\n{name.title()}'s favorite languages are:")
    # Print their favorite languages.
    for language in languages:
        print(f"\t{language.title()}")

#Print all the languages collected.
collected_languages = []

print("\nThe following languages were collected:")
for languages in favorite_languages.values():
    for language in languages:
        collected_languages.append(language)

for language in sorted(set(collected_languages)):
    print(language.title())