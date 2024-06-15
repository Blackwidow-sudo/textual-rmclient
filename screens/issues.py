import requests
from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Footer, Pretty


class IssuesScreen(Screen):
    def compose(self) -> ComposeResult:
        issues = self.get_issues()

        yield Pretty(issues)
        yield Footer()

    def get_issues(self):
        response = requests.get("https://redmine.org/issues.json")

        return response.json()
