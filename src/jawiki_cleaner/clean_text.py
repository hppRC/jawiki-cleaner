import re
import unicodedata
from xml.sax.saxutils import unescape


def replace_characters(text):
    text = re.sub(r'、+', '、', text)
    text = re.sub(r"\s*\[\[(.*?)\|(.*?)\]\]\s*", r"\2", text)
    text = re.sub(r"\s*\[\[(.*?)\]\]\s*", r"\1", text)
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'\s*\(\s*', '(', text)
    text = re.sub(r'\s*\)\s*', ')', text)
    text = re.sub(r'(,\s)+', ',', text)
    text = re.sub(r'(\s*、\s*)+', '、', text)
    text = re.sub(r'\s*\+\s*', '+', text)
    text = re.sub(r'\s*-\s*', '-', text)
    text = re.sub(r'\s*%\s*', '%', text)
    text = re.sub(r'\s*""\s*', '', text)
    text = re.sub(r'^[、。,\.\s]*', '', text)
    text = text.replace('(、', '(')
    text = text.replace('、)', ')')
    text = text.replace('()', '')
    text = text.replace('「」', '')
    text = text.replace("(,", "(")
    text = text.replace(",)", ")")
    text = text.replace(";)", ")")
    text = text.replace(" ' ", "")
    text = text.replace("『』", "")
    text = text.replace("・)", ")")
    text = text.replace(":)", ")")
    text = text.replace("、。", "。")
    text = text.replace("“”", "")
    text = text.replace("、,", "、")
    text = text.replace('[[', '')
    text = text.replace(']]', '')
    return text.strip().lstrip()


def preprocess(text):
    text = unicodedata.normalize('NFKC', text).lstrip().strip()
    text = unescape(text).lstrip().strip()
    text = replace_characters(text).lstrip().strip()
    return text


def clean_text(text):
    new = preprocess(text)
    while text != new:
        text = new
        new = preprocess(text).strip()
    return text
