import abc


class LecteurBadge(abc.ABC):

    @abc.abstractmethod
    def verifier_badge(self) -> int | None:
        pass

