from badge import Badge
class SystemeValidation:
    def __init__(self):

    def interroger_badge(self):
        return Badge.isValide(self.badge)           

    def lancer_signal(self):