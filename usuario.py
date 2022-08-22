import evento as evnt
import lista as lista_eventos

class Usuario:
    def __init__(self, _ID, _correo, _nombre, _Port1, _apellidos):
        self.ID = _ID
        self.correo = _correo
        self.nombre = _nombre
        self.Port1 = _Port1
        self.apellidos = _apellidos
        self.lista = lista_eventos
 
    def get_Tuple_Data(self):
        tuple=(self.id,self.nombre,self.correo)
        return tuple
    
    def accedeEvento(self, nombre_evento):
        if self.buscaEvento(nombre_evento):
            self.lista.muestraEvento(nombre_evento)
        else:
            print("Evento no guardado en su lista")
 
    def buscaEvento(self, nombre_evento):
        if self.lista.buscaEvento(nombre_evento):
            return True
        return False        
    
    def registraEvento(self, evento):
        self.lista.agregaEvento(evento)
 
    def setCorreo(self, _correo):
        self.correo = _correo
 
    def getCorreo(self):
        return self.correo
 
    def setID(self, _ID ):
        self.ID = _ID
 
    def getID(self):
        return self.ID
 
    def setNombre(self, _nombre):
        self.nombre = _nombre
 
    def getNombre(self):
        return self.nombre
 
    def setApellido(self, _apellido):
        self.apellidos = _apellido
 
    def getApellido(self):
        return self.apellidos
