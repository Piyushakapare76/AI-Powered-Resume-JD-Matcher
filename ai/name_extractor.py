import re

def extract_name(resume_text):
    lines = resume_text.strip().split("\n")[:5]

    for line in lines:
        line = line.strip()

        if (
            re.match(r"^[A-Z][a-z]+(\s[A-Z][a-z]+){1,3}$", line)
            and "@" not in line
            and not any(char.isdigit() for char in line)
        ):
            return line.title()

    return None
