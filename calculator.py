class Credit:

    def __init__(self, suma_imp, ani_imp, r_lun, suma_totala, dobanda_an, salar, optiune):
        self.suma_imp = suma_imp
        self.ani_imp = ani_imp
        self.r_lun = r_lun
        self.suma_totala = suma_totala
        self.dobanda_an = dobanda_an
        self.salar = salar
        self.optiune = optiune

    def venit(self):
        self.salar = input("Care este venitul lunar curent? ")

    def tip_credit(self):
        tip = {1: "Nevoi Personale", 2: "Ipotecar", 3: "Auto"}
        print(tip)
        self.optiune = input("Alegeti tipul de credit: ")
        if self.optiune == str(1):
            print("Ati ales Creditul pentru Nevoi Personale cu dobanda de 12% ")
            self.dobanda_an = 0.12
            self.optiune = "Nevoi personale"
        elif self.optiune == str(2):
            print("Ati ales Creditul Ipotecar cu dobanda de 4% ")
            self.dobanda_an = 0.04
            self.optiune = "Ipotecar"
        elif self.optiune == str(3):
            print("Ati ales Creditul Auto cu dobanda de 7% ")
            self.dobanda_an = 0.07
            self.optiune = "Auto"
        else:
            print("Optiunea aleasa nu este valida")
            calculator.tip_credit()

    def suma(self):
        try:
            self.suma_imp = float(input("Introduceti suma de imprumutat: "))
        except ValueError:
            print("Introduceti o suma reala")
            calculator.suma()

    def ani(self):
        try:
            self.ani_imp = float(input("Introduceti durata creditului, intre 1 si 5 ani: "))
            while self.ani_imp < 1 or self.ani_imp > 5:
                print("Numarul de ani nu este in intervalul 1-5\n")
                self.ani_imp = int(input("Introduceti durata creditului, intre 1 si 5 ani: "))
        except ValueError:
            print("Introduceti o cifra intre 1 si 5 ")
            calculator.ani()

    def rata(self):
        self.r_lun = self.suma_imp * self.dobanda_an / (12 * (1 - (1 + (self.dobanda_an / 12)) **
                                                              (-1 * self.ani_imp * 12)))
        print("Rata lunara este: ", round(self.r_lun, 2))
        self.suma_totala = self.r_lun * (self.ani_imp * 12)
        print("Suma totala de rambursat este: ", round(self.suma_totala, 2))

    def venit_mic(self):
        while True:
            while int(self.salar) / 2 <= self.r_lun:
                print("Venitul lunar este prea mic pentru a obtine acest credit, reincercati cu o suma mai mica ")
                self.salar = input("Care este venitul lunar curent? ")
                calculator.tip_credit()
                calculator.suma()
                calculator.ani()
                calculator.rata()
                calculator.venit_mic()
            else:
                break

    def __str__(self):
        return "Ati obtinut un credit de {0} in valoare de {1} cu dobanda anuala {2}% si rata lunara {3}"\
            .format(self.optiune, int(self.suma_imp),  self.dobanda_an*100, round(self.r_lun, 2))

calculator = Credit(0, 0, 0, 0, 0, 0, 0)
calculator.venit()
calculator.tip_credit()
calculator.suma()
calculator.ani()
calculator.rata()
calculator.venit_mic()
print(calculator)
input("Apasa ENTER pentru a iesi ")