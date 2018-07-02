
class LPIDManager:

    def __init__(self):
        self._max_id = LPID(0)

    def next(self):
        self._max_id += 1
        return self._max_id

    def __repr__(self):
        return str("Max id: %s" % (self._max_id,))


class LPID:

    def __init__(self, id):
        self._id = id

    def __eq__(self, other):
        return self._id == other._id

    def __repr__(self):
        return str(self._id)

    def __add__(self, other):
        return LPID(self._id + other)

    def __hash__(self):
        return self._id