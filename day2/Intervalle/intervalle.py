class IntervalError(Exception):
    pass

class Intervalle:

    @staticmethod
    def __check_borne(borne:int) -> int:
        try:
            checked_borne = int(borne)
        except:
            raise IntervalError("Erreur : bornes invalides")
        return checked_borne
    
    def __check_bornes(self):
        if self.__borne_inf <= 0 or self.__borne_sup < self.__borne_inf:
            raise IntervalError("Erreur : bornes invalides")
        
    def __init__(self, borne_inf:int, borne_sup:int):
        self.__borne_inf = Intervalle.__check_borne(borne_inf)
        self.__borne_sup = Intervalle.__check_borne(borne_sup)
        self.__check_bornes()

    def modif_borne_sup(self, borne_sup:int):
        self.__borne_sup = Intervalle.__check_borne(borne_sup)
        self.__check_bornes()
        
    def modif_borne_inf(self, borne_inf:int):
        self.__borne_inf = Intervalle.__check_borne(borne_inf)
        self.__check_bornes()

    def lire_inf(self):
        return self.__borne_inf
    
    def lire_sup(self):
        return self.__borne_sup
    
    def __str__(self):
        return f"[{self.__borne_inf};{self.__borne_sup}]"
    
    def __contains__(self, val:int):
        return val >= self.__borne_inf and val <= self.__borne_sup
    
    def __add__(self, other):
        return Intervalle(self.__borne_inf+other.__borne_inf, self.__borne_sup+other.__borne_sup)

    def __sub__(self, other):
        # peut échouer en fonction des bornes de self et other
        return Intervalle(self.__borne_inf-other.__borne_inf, self.__borne_sup-other.__borne_sup)

    def __mul__(self, other):
        return Intervalle(self.__borne_inf*other.__borne_inf, self.__borne_sup*other.__borne_sup)
    
    def __and__(self, other):
        if self.__borne_inf > other.__borne_inf:
            borne_inf = self.__borne_inf
        else:
            borne_inf = other.__borne_inf
        if self.__borne_sup < other.__borne_sup:
            borne_sup = self.__borne_sup
        else:
            borne_sup = other.__borne_sup
        if borne_inf <= borne_sup:
            return Intervalle(borne_inf, borne_sup)
        return None

if __name__ == '__main__':
    try:
        Intervalle("toto", "tata")
    except IntervalError as ie:
        print(ie)

    try:
        Intervalle(-1, 10)
    except IntervalError as ie:
        print(ie)

    try:
        Intervalle(11, 10)
    except IntervalError as ie:
        print(ie)

    int1 = Intervalle(3, 7)
    print(int1.lire_inf())
    print(int1.lire_sup())
    print(int1)

    print(int1.__contains__(5))
    print(int1.__contains__(7))
    print(int1.__contains__(3))
    print(int1.__contains__(9))

    int2 = Intervalle(2,4)
    print(int1+int2)
    print(int1-int2)
    print(int1*int2)
    print(int1 & int2)