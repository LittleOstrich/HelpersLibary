def cleanString(s: str, removees=None):
    if removees is None:
        removees = ",;[](){}\n"

    for r in removees:
        s = s.replace(r, "")
    return s
