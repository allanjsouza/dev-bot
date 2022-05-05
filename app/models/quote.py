class Quote:
    """Carries words of inspiration from influential figures throughout history"""

    def __init__(self, text, author):
        if not text:
            raise ValueError("Quote must not be empty")
        if not author:
            raise ValueError("Quote author must be specified")
        self.text = text
        self.author = author
