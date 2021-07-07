

class Individu():
    def __init__(self, nom, prenom, age, PMA, LTHR, FTP, duree):
        self.FTP = FTP
        self.LTHR = LTHR
        self.PMA = PMA
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.duree = duree

    def __repr__(self):
        return f'{self.nom} {self.prenom}, {self.age} ans , LTHR = {self.LTHR}, PMA = {self.PMA}, FTP = {self.FTP}, durée du cycle = {self.duree} jours '
        
class Seuil :
    def __init__(self, individu):
        self.FTPmoins = 0.91*individu.FTP
        self.FTPplus = 1.05*individu.FTP
        self.PMAmoins = 0.75*individu.PMA
        self.PMAplus = 0.85*individu.PMA
        self.LTHRmoins = 0.95*individu.LTHR
        self.LTHRplus = 1.05*individu.LTHR
        self.ITVmoins =  8
        self.ITVplus = 8
        self.cadenceMoins  = None
        self.cadencePlus = None
        
    def __repr__(self):
        return f"Seuil (FTP compris entre {int(self.FTPmoins)} et {int(self.FTPplus)}, PMA comprise entre {int(self.PMAmoins)} et {int(self.PMAplus)} , LTHR compris entre {int(self.LTHRmoins)} et {int(self.LTHRplus)}) "


class Capacite_anaerobie :
    def __init__(self, individu):
        self.FTPmoins = 1.21*individu.FTP
        self.FTPplus = 1.50*individu.FTP
        self.PMAmoins = 1.0*individu.PMA
        self.PMAplus = 1.80*individu.PMA
        self.LTHRmoins = False
        self.LTHRplus = False
        self.ITVmoins =  10
        self.ITVplus = 10
        self.cadenceMoins  = None
        self.cadencePlus = None
        
    def __repr__(self):
        return f"Capacité anaerobie (FTP compris entre {int(self.FTPmoins)} et {int(self.FTPplus)}, PMA comprise entre {int(self.PMAmoins)} et {int(self.PMAplus)} , LTHR compris entre {int(self.LTHRmoins)} et {int(self.LTHRplus)}) "
        

class Tempo :
    def __init__(self, individu):
        self.FTPmoins = 0.76*individu.FTP
        self.FTPplus = 0.9*individu.FTP
        self.PMAmoins = 0.6*individu.PMA
        self.PMAplus = 0.75*individu.PMA
        self.LTHRmoins = 0.84*individu.LTHR
        self.LTHRplus = 0.94*individu.LTHR
        self.ITVmoins =  5
        self.ITVplus = 5
        self.cadenceMoins  = None
        self.cadencePlus = None
        
    def __repr__(self):
        return f"Tempo (FTP compris entre {int(self.FTPmoins)} et {int(self.FTPplus)}, PMA comprise entre {int(self.PMAmoins)} et {int(self.PMAplus)} , LTHR compris entre {int(self.LTHRmoins)} et {int(self.LTHRplus)}) "

class Endurance :
    def __init__(self, individu):
        self.FTPmoins = 0.56*individu.FTP
        self.FTPplus = 0.75*individu.FTP
        self.PMAmoins = 0.6*individu.PMA
        self.PMAplus = 0.6*individu.PMA
        self.LTHRmoins = 0.69*individu.LTHR
        self.LTHRplus = 0.83*individu.LTHR
        self.ITVmoins =  3
        self.ITVplus = 4
        self.cadenceMoins  = None
        self.cadencePlus = None
        
    def __repr__(self):
        return f"Endurance (FTP compris entre {int(self.FTPmoins)} et {int(self.FTPplus)}, PMA comprise entre {int(self.PMAmoins)} et {int(self.PMAplus)} , LTHR compris entre {int(self.LTHRmoins)} et {int(self.LTHRplus)}) "


class Sweet_spot :
    def __init__(self, individu):
        self.FTPmoins = 0.88*individu.FTP
        self.FTPplus = 0.93*individu.FTP
        self.PMAmoins = False #demander à Clara pq pas de données
        self.PMAplus = False #*individu.PMA
        self.LTHRmoins = 0.92*individu.LTHR
        self.LTHRplus = 0.98*individu.LTHR
        self.ITVmoins =  6
        self.ITVplus = 7
        self.cadenceMoins  = None
        self.cadencePlus = None
    
    def __repr__(self):
        return f"Sweet spot (FTP compris entre {int(self.FTPmoins)} et {int(self.FTPplus)}, PMA comprise entre {int(self.PMAmoins)} et {int(self.PMAplus)} , LTHR compris entre {int(self.LTHRmoins)} et {int(self.LTHRplus)})"


class Capacite_aerobie :
    def __init__(self, individu):
        self.FTPmoins = 1.06*individu.FTP
        self.FTPplus = 1.20*individu.FTP
        self.PMAmoins = 0.85*individu.PMA
        self.PMAplus = 1.0*individu.PMA
        self.LTHRmoins = 1.05*individu.LTHR
        self.LTHRplus = 1.06*individu.LTHR
        self.ITVmoins =  9
        self.ITVplus = 9
        self.cadenceMoins  = None
        self.cadencePlus = None
        
    def __repr__(self):
        return f"Capacité anaérobie (FTP compris entre {int(self.FTPmoins)} et {int(self.FTPplus)}, PMA comprise entre {int(self.PMAmoins)} et {int(self.PMAplus)} , LTHR compris entre {int(self.LTHRmoins)} et {int(self.LTHRplus)})"


class Recup_active :
    def __init__(self, individu):
        self.FTPmoins = 0*individu.FTP
        self.FTPplus = 0.55*individu.FTP
        self.PMAmoins = 0.3*individu.PMA
        self.PMAplus = 0.5*individu.PMA
        self.LTHRmoins = 0*individu.LTHR
        self.LTHRplus = 0.68*individu.LTHR
        self.ITVmoins =  1
        self.ITVplus = 2
        
    def __repr__(self):
        return f"Récupération active (FTP compris entre {int(self.FTPmoins)} et {int(self.FTPplus)}, PMA comprise entre {int(self.PMAmoins)} et {int(self.PMAplus)} , LTHR compris entre {int(self.LTHRmoins)} et {int(self.LTHRplus)})"


class Sprint :
    def __init__(self, individu):
        self.FTPmoins = 1.50*individu.FTP
        self.FTPplus = 2.*individu.FTP
        self.PMAmoins = 1.8*individu.PMA
        self.PMAplus = 2.0*individu.PMA
        self.LTHRmoins = False
        self.LTHRplus = False
        self.ITVmoins =  10
        self.ITVplus = 10
        self.cadenceMoins  = None
        self.cadencePlus = None
        
    def __repr__(self):
        return f"Sprint (FTP compris entre {int(self.FTPmoins)} et {int(self.FTPplus)}, PMA comprise entre {int(self.PMAmoins)} et {int(self.PMAplus)} , LTHR compris entre {int(self.LTHRmoins)} et {int(self.LTHRplus)})"
