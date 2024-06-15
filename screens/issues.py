from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Footer, Placeholder


class IssuesScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Placeholder("Issues Screen")
        yield Footer()
