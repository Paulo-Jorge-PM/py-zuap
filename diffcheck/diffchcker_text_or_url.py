import requests
from difflib import Differ, SequenceMatcher
from pprint import pformat, pprint


class Diffchecker:
    """
    Utils class for diffchecking two docs from URL (HTML source-code) or text
    """
    def __init__(self, doc1: str, doc2: str, source: str = "url"):
        """
        :param doc1: origin content to comapre, can be text or url
        :param doc2: content to comapre to doc1, can be text or url
        :param source: doc1 and doc2 content type: url will (fetch source-code) or text 
        """
        self.doc1 = self.content_from_url(doc1) if source=="url" else doc1
        self.doc2 = self.content_from_url(doc2) if source=="url" else doc2

        self.doc1 = self.doc1.splitlines(keepends=True)
        self.doc2 = self.doc2.splitlines(keepends=True)

    def diff(self):
        """
        Diffcheck per lines

        Meaning of the symbols:
        Lines only present on the second file: +
        Lines not present on the second file: -
        """
        diff = Differ()
        difference = list(diff.compare(self.doc1, self.doc2))
        return difference

    def diff_ratio(self):
        """
        Match ratio of two contents

        Result meaning (range: 0 to 1):
        0: totally differ
        1: exactly the same 
        """

        match = SequenceMatcher(a=self.doc1, b=self.doc2)
        return match.ratio()

    def content_from_url(sefl, url):
        """
        Get content from URL source-code
        """
        source = requests.get(url)
        return source.text

if __name__ == "__main__":
    args = ["a", "b", "c"]

    report = ""

    for arg in args:
        url1 = "xx?name="+arg
        url2 = "xx2?name="+arg

        diff = Diffchecker(url1, url2)
        diff_result = diff.diff()

        report += f"===== Dfiffcheck for product {arg} ====="
        report += pformat(diff_result)
        report += "\n"
        repot += f"Diff Ratio: {diff.diff_ratio()}"
        report += "\n\n"

    with open("report.txt", "w") as f:
        f.write(report)
