from datetime import datetime, timedelta, date

# Classe permettant de gérer les dates utilisée dans l'app
# Format yy/mm/dd car pas de quêtes horaires
class Date:

    def __init__(self, pdate : date = None):
        if pdate is None:
            self.date = datetime.now().date()
        else:
            self.date = pdate

    @classmethod
    def from_timestamp(cls, timestamp):
        return cls(datetime.fromtimestamp(timestamp).date())

    def add_days(self,nbDays):
        self.date = self.date + timedelta(days=nbDays)

    def to_timestamp(self):
        return datetime(self.date.year, self.date.month, self.date.day).timestamp()

    # Surchage de conversion en string
    def __str__(self):
        return self.date.strftime("%d/%m/%Y")

    def __eq__(self, other):
        """Permet de comparer Objet Date == datetime.date ou Objet Date == Objet Date"""
        if isinstance(other, Date):
            return self.date == other.date
        if isinstance(other, date):
            return self.date == other
        return False

    def __ne__(self, other):
        return not self.__eq__(other)