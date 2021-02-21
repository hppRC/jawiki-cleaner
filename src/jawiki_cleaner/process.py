from .clean_text import clean_text
from .break_line import break_line


def process(text):
    text = text.lstrip().strip()
    text = clean_text(text).lstrip().strip()
    text = break_line(text).lstrip().strip()
    return text
