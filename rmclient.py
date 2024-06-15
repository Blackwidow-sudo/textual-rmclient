from modals.quit import QuitModal
from screens.issues import IssuesScreen
from textual.app import App


class RMClient(App):
    BINDINGS = [
        ("i", "switch_mode('issues')", "Issues"),
        ("q", "request_quit", "Quit"),
    ]
    MODES = {
        "issues": IssuesScreen,
        "quit": QuitModal,
    }

    def action_request_quit(self) -> None:
        self.push_screen(QuitModal())

    def on_mount(self) -> None:
        self.switch_mode("issues")


if __name__ == "__main__":
    app = RMClient()

    app.run()
