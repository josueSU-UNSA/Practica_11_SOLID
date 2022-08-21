import evento as evnt

class Lista:
    def __init__(self):
        self.cantidad = 0
        self.listaEvento = list()
    
    def muestraEventos(self):
        for evento in self.listaEvento: 
            evento.show()

    def agregaEvento(self, evento):
        self.listaEvento.append(evento)
        self.cantidad += 1
    
    def muestraEvento(self, nombre_evento):
        for evento in self.listaEvento:
            if evento.getNombre() == nombre_evento:
                evento.show()
                
    def buscaEvento(self, nombre_evento):
        for evento in self.listaEvento:
            if evento.getNombre() == nombre_evento:
                return True
        return False
