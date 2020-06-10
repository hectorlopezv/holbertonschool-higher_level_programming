"""Square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """constructor for square class"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """string representation of object"""
        return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                             self.id, self.x, self.y,
                                             self.width)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def update_(self, id=None, size=None, x=None, y=None):
        """update aux method"""

        if id is not None:
            self.id = id

        if size is not None:
            self.size = size

        if x is not None:
            self.x = x

        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """update args of instance"""

        if args and len(args) != 0:
            self.update_(*args)
        else:
            self.update_(**kwargs)

    def to_dictionary(self):
        """to to_dictionary"""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}