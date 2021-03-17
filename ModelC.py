class Record:
    def __init__(self, pruid, prname, prnameFr, date, numconf, numprob, numdeaths, numtotal, numtoday, ratetotal):
        """creates a new Record object with the following arguments:

        :param prid:
        :param pren:
        :param prfr:
        :param date:
        :param numconf:
        :param numprob:
        :param numdeaths:
        :param numtotal:
        :param numtoday:
        :param ratetotal:
        By Ahmed Albarghouti
        """
        self.pruid = pruid
        self.prname = prname
        self.prnameFr = prnameFr
        self.date = date
        self.numconf = numconf
        self.numprob = numprob
        self.numdeaths = numdeaths
        self.numtotal = numtotal
        self.numtoday = numtoday
        self.ratetotal = ratetotal

    # setters for the Object's attributes
    def set_pruid(self, pruid):
        self.pruid = pruid

    def set_prname(self, prname):
        self.prname = prname

    def set_prnameFr(self, prnameFr):
        self.prnameFr = prnameFr

    def set_date(self, date):
        self.date = date

    def set_numconf(self, numconf):
        self.numconf = numconf

    def set_numprob(self, numprob):
        self.numprob = numprob

    def set_numdeaths(self, numdeaths):
        self.numdeaths = numdeaths

    def set_numtotal(self, numtotal):
        self.numtotal = numtotal

    def set_numtoday(self, numtoday):
        self.numtoday = numtoday

    def set_ratetotal(self, ratetotal):
        self.ratetotal = ratetotal
