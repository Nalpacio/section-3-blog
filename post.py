class Post:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __repr__(self):
        return '{}'.format(self.title)

    def json(self):
        return {
            'Title':self.title,
            'Content':self.content,
        }
