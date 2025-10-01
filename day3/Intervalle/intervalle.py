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
        borne_inf = self.__borne_inf if self.__borne_inf > other.__borne_inf else other.__borne_inf
        borne_sup = self.__borne_sup if self.__borne_sup < other.__borne_sup else other.__borne_sup
        return Intervalle(borne_inf, borne_sup) if borne_inf <= borne_sup else None

if __name__ == '__main__':
    try:
        Intervalle("toto", "tata")
    except IntervalError as ie:
        print(f"Intervalle(toto, tata): {ie}")

    try:
        Intervalle(-1, 10)
    except IntervalError as ie:
        print(f"Intervalle(-1, 10): {ie}")

    try:
        Intervalle(11, 10)
    except IntervalError as ie:
        print(f"Intervalle(11, 10): {ie}")

    int1 = Intervalle(3, 7)
    print(f"{int1} borne inférieure: {int1.lire_inf()}")
    print(f"{int1} borne supérieure: {int1.lire_sup()}")

    print(f"5 in {int1}: {5 in int1}")
    print(f"7 in {int1}: {7 in int1}")
    print(f"3 in {int1}: {3 in int1}")
    print(f"9 in {int1}: {9 in int1}")

    int2 = Intervalle(2,4)
    print(f"{int1} + {int2}: {(int1+int2)}")
    print(f"{int1} - {int2}: {(int1-int2)}")
    try:
        int2-int1
    except IntervalError as ie:
        print(f"{int2} - {int1}: {ie}")
    
    print(f"{int1} * {int2}: {(int1*int2)}")
    print(f"{int1} & {int2}: {(int1&int2)}")

    int3 = Intervalle(1,2)
    print(f"{int1} & {int3}: {(int1&int3)}")

