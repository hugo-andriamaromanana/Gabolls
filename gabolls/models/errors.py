class NoDecisionsTaken(NotImplementedError):
    pass


class EnvVarNotFound(ValueError):
    pass


class RoundEndNotImplemented(NotImplementedError):
    pass


class CardNotInPlayerHand(IndexError):
    pass


class NoTypeError(ValueError):
    pass


class CannotDrawFromEmptyDeck(ValueError):
    pass
