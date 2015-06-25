import re

class Validar:
    
    def returnNumero(self):
        print (self)
        num = re.sub("[-\. ]", "", self)
        return num
    
    def verificaCPF(self):
        print (self)
        if len(self) < 11:
            return True
        return False
    
    def numeroRepetidos(self):
        print (self)
        rep = 0
                
        for digito in range(len(self)-2):
            if self[digito] == self[digito + 1]:
                # print(self[digito])
                rep = rep+1
                
        # print(rep)
        
        return rep
    
    
    def verificarDdd(self):
        print (self)
        if re.match(r'\d{2}', self):
            return True
        return False
    
    def verificarTelefone(self):
        print (self)
        if re.match(r'\d{4,5}-\d{4}', self):
            return True
        return False
    
    def verificarCep(self):
        print (self)
        if re.match(r'\d{5}-\d{3}', self):
            return True
        return False
        