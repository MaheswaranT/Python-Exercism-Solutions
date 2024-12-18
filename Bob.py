def response(hey_bob):
    stripped_input = hey_bob.strip()
    if not stripped_input:
        return "Fine. Be that way!"
    if stripped_input.isupper() and stripped_input.endswith('?'):
        return "Calm down, I know what I'm doing!"
    if stripped_input.isupper():
        return "Whoa, chill out!"
    if stripped_input.endswith('?'):
        return "Sure."
    return "Whatever."
