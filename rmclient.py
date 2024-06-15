from screens.issues import IssuesScreen
from textual.app import App


class RMClient(App):
    BINDINGS = [
        ("i", "switch_mode('issues')", "Issues")
    ]
    MODES = {
        "issues": IssuesScreen
    }

    def on_mount(self) -> None:
        self.switch_mode("issues")


if __name__ == "__main__":
    app = RMClient()

    app.run()
