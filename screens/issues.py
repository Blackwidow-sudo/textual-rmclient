import requests
from modals.issue import IssueModal
from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import DataTable, Footer, Header


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
        yield Header()
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
        table.cursor_type = "row"

        for issue in issues:
            table.add_row(
                issue["id"],
                issue["project"]["name"],
                issue["tracker"]["name"],
                issue["status"]["name"],
                issue["priority"]["name"],
                issue["subject"],
            )

    def on_data_table_row_selected(self, event: DataTable.RowSelected) -> None:
        self.app.push_screen(IssueModal())
