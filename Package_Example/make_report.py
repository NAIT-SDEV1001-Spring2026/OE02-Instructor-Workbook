from yattag import Doc
from report_config import get_config

def build_report(data):
    doc, tag, text = Doc().tagtext()
    cfg = get_config()

    with tag('html'):
        with tag('body'):
            with tag('h1'):
                text(cfg["title"])

    return doc.getvalue()

if __name__ == "__main__":
    sample = ["Point A: Install venv", "Point B: Use dotenv"]
    print(build_report(sample))