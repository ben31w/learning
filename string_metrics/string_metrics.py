def lev(a: str, b: str) -> int:
    """
    Return Levenshtein (edit) distance between two strings. This is the number
    of insertions, deletions, and substitutions separating the two strings.
    :param a:
    :param b:
    :return:
    """
    if len(b) == 0:
        return len(a)
    if len(a) == 0:
        return len(b)

    if a[0] == b[0]:
        return lev(a[1:], b[1:])

    else:
        return 1 + min(
            lev(a[1:], b),
            lev(a, b[1:]),
            lev(a[1:], b[1:])
        )

exercises = [
    ("bb squats", "squat"),
    ("rdls", "romanian deadlifts"),
    ("dls", "rdls")
]

for pair in exercises:
    exercise1, exercise2 = pair



    print(lev(exercise1, exercise2), exercise1, exercise2, sep="\t")