class RectangleShape:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
       
        return iter([
            {'length': self.length},
            {'width': self.width}
        ])


rectangle = RectangleShape(5, 6)

for item in rectangle:
    print(item)
