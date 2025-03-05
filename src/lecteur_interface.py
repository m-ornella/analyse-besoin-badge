import abc


class LecteurBadge(abc.ABC):
        
    def verifier_badge(self) -> int | None:
        abc.abstractmethod
        pass
