from IPython.display import display, Markdown
from pathlib import Path


def show_ihf():
    thisfolder = Path(__file__).parent
    # thisfolder = Path("./")
    with open(thisfolder / "innholdsfortegnelse.md") as mdfile:
        mdtxt = mdfile.read()
        display(Markdown(mdtxt))
