from textual.app import ComposeResult
from textual.containers import Grid
from textual.screen import ModalScreen
from textual.widgets import Button, Label, Input, Select


class IssueModal(ModalScreen):
    ACTIVITIES = (
        ("Development", 0),
    )

    def compose(self) -> ComposeResult:
        yield Grid(
            Label("Issue", id="issue"),
            Input("Date", id="date"),
            Input("Hours", id="hours"),
            Select(self.ACTIVITIES, id="activity"),
            Input("Comment", id="comment"),
            Button("Close", id="close", variant="primary"),
            Button("Start", id="start", variant="error"),
            id="dialog",
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.app.pop_screen()
