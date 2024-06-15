import requests
from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import DataTable, Footer


class IssuesScreen(Screen):
    COLUMNS = (
        "ID",
        "Project",
        "Tracker",
        "Status",
        "Priority",
        "Subject",
    )

    def compose(self) -> ComposeResult:
        yield DataTable()
        yield Footer()

    def get_issues(self):
        response = requests.get("https://redmine.org/issues.json")

        if response.status_code == 200:
            return response.json()["issues"]

        return []

    def on_mount(self) -> None:
        issues = self.get_issues()
        table = self.query_one(DataTable)
        table.add_columns(*self.COLUMNS)

        for issue in issues:
            table.add_row(
                issue["id"],
                issue["project"]["name"],
                issue["tracker"]["name"],
                issue["status"]["name"],
                issue["priority"]["name"],
                issue["subject"],
            )
