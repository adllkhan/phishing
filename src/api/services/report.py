from weasyprint import HTML
from jinja2 import Environment, FileSystemLoader

from .phishing import get_data
from api.core.config import Config

__environment = Environment(loader=FileSystemLoader("src/templates"))
__template = __environment.get_template("report.html")


def generate_report(domain: str) -> str:
    path = f"{Config.reports_path}/report.pdf"

    data = get_data()
    print(data)
    template = __template.render(data=data)
    print("template")
    HTML(string=template).write_pdf(target=path)
    print("pdf")
    return path
