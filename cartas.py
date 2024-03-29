class cartas:
    def __init__(self, valor, pinta):
        self.valor=valor
        self.pinta=pinta
    def dar_valor(self):
        if self.valor in ['J','Q','K']:
            return 10
        if self.valor == 'A':
            return 1
        return int(self.valor)
    def mostrar(self):
        return self.valor + " de " + self.pinta
    
class Mazo:
    def __init__(self, jugador = False):
        if jugador:
            self.cartas = []
        else:
            self.cartas = [cartas(v,p)
                           for v in ['A','J','Q','K']+[str(x) for x in range(2,11)]
                           for p in ['picas','treboles','corazones','diamantes']]
    def dar_valor(self):
        valor = 0
        for c in self.cartas:
                valor+= c.dar_valor()
        return valor
    
    def dar_cartas(self):
        return self.cartas.pop()
    
    def agregar_cartas(self, cartas):
        self.cartas.append(cartas)
    
    
if __name__ == '__main__':
        m = Mazo()
        j = Mazo(True)
        j.agregar_cartas(m.dar_cartas())
        j.agregar_cartas(m.dar_cartas())
        for c in j.cartas:
            print(c.mostrar())
        print(m.dar_valor())