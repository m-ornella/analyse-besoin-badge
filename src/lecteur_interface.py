import abc


class LecteurBadge(abc.ABC):

    def simuler_detection_badge(self):
        abc.abstractmethod
        pass
     
    def verifier_badge(self) -> int | None:
        abc.abstractmethod
        pass
