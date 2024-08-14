def phrase_loves_me_not(n):
    phrases = []
    for i in range(1, n + 1):
        if i % 2 != 0:
            phrases.append("Loves me\n")
        else:
            phrases.append("Loves me not\n")
    return "".join(phrases)


print(phrase_loves_me_not(10))
