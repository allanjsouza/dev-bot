class ShouldideployMessage:
    """Message indicating if it is a good time to deploy"""

    def __init__(self, text: str):
        if not text:
            raise ValueError("Shouldideploy message must not be empty")
        self.text = str(text)
        self.thumb_url = ""
        self.footer_icon = ""
        self.footer = ""
        self._color = 0

    @property
    def color(self) -> int:
        return self._color

    @color.setter
    def color(self, color):
        str_color = str(color).replace("#", "0x")
        self._color = int(str_color, 0)
