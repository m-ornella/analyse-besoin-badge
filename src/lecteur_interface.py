import abc


class LecteurBadge(abc.ABC):

    @abc.abstractmethod
    def simuler_detection_badge_valide(self) -> int | None:
        pass

