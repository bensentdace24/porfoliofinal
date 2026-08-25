from html.parser import HTMLParser
from pathlib import Path
import unittest


class PortfolioParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text_parts = []
        self.project_images = []
        self.in_project_image = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        classes = set(attrs.get("class", "").split())
        if tag == "div" and "project-img-wrap" in classes:
            self.in_project_image = True
        if tag == "img" and self.in_project_image:
            self.project_images.append(attrs.get("src", ""))

    def handle_endtag(self, tag):
        if tag == "div" and self.in_project_image:
            self.in_project_image = False

    def handle_data(self, data):
        text = " ".join(data.split())
        if text:
            self.text_parts.append(text)


class PortfolioContentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = Path("index.html").read_text(encoding="utf-8")
        cls.parser = PortfolioParser()
        cls.parser.feed(cls.source)
        cls.text = " ".join(cls.parser.text_parts)

    def test_new_project_titles_are_rendered(self):
        for title in (
            "Resort Website",
            "Accounting & Budget Management System",
            "Job Tracking Platform",
        ):
            self.assertIn(title, self.text)

    def test_project_technology_stack_is_rendered(self):
        for technology in (
            "React",
            "TypeScript",
            "Laravel Sanctum",
            "REST APIs",
            "SQLite",
            "Vitest",
            "Laravel Blade",
            "Chart.js",
            "Axios",
            "PHPUnit",
        ):
            self.assertIn(technology, self.text)

    def test_ai_assisted_workflow_is_described_honestly(self):
        self.assertIn("AI-Assisted Development", self.text)
        for activity in ("planning", "debugging", "learning", "testing"):
            self.assertIn(activity, self.text.lower())

    def test_new_project_screenshots_start_blank(self):
        for filename in ("resort", "accounting-budget", "job-tracker"):
            self.assertNotIn(f"images/{filename}.", " ".join(self.parser.project_images))

    def test_reduced_motion_has_an_intentional_fallback(self):
        self.assertIn("@media (prefers-reduced-motion: reduce)", self.source)
        self.assertIn("animation-duration: 0.01ms", self.source)


if __name__ == "__main__":
    unittest.main()
