from pdfminer.high_level import extract_text
import io


def MinePDF(file):
    try:
        return extract_text(io.BytesIO(file.read()))
    except Exception as e:
        return False
