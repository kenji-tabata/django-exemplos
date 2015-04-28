from django.conf import settings
from django.template import Context, Template
import os

class Arquivo(object):
        
    def arquivo_existe(self,nome):
        try:
            arquivo = open("%s/%s" % (settings.DOCUMENTOS, nome), "r")
            if arquivo:
                msg = True
                
            arquivo.close()
            
        except FileNotFoundError as e:
            msg = False
            
        return msg
    
    def combobox_arquivos(self):
        list = os.listdir("%s" % (settings.DOCUMENTOS))
        
        h = Template('<option>{{msg}}</option>')
    
        context = Context({'msg': 'Selecione um arquivo'})

        html = h.render(context)

        for value in list:
            t = Template('<option value={{valor}}>{{valor}}</option>')
            con = Context({'valor': value})

            html += t.render(con)

        return html
        
    
    def criar_arquivo(self, nome, conteudo):
        if not self.arquivo_existe(nome):
            arquivo = open("%s/%s" % (settings.DOCUMENTOS, nome), "w")
            if arquivo:
                arquivo.write(conteudo)
                msg = "O arquivo %s foi criado com sucesso!" % nome
            else:
                msg = "Ocorreu um erro ao criar o arquivo."
                
            arquivo.close()
        
        else:
            msg = "O arquivo com o nome %s já existe na pasta." % nome
            
        return msg
    
    def salvar_arquivo(self, nome, conteudo):
        arquivo = open("%s/%s" % (settings.DOCUMENTOS, nome), "w")
        if arquivo:
            arquivo.write(conteudo)
            msg = "O arquivo %s foi salvo com sucesso!" % nome
        else:
            msg = "Ocorreu um erro ao criar o arquivo."

        arquivo.close()
        
        return msg
    
    def ler_arquivo(self, nome):
        if self.arquivo_existe(nome):
            arquivo = open("%s/%s" % (settings.DOCUMENTOS, nome), "r")
            msg = ""
            if arquivo:
                for linha in arquivo.readlines():
                    msg += linha
            else:
                msg = "Ocorreu um erro ao tentar ler o arquivo."
                
            arquivo.close()
        
        else:
            msg = "O arquivo %s não foi encontrado." % nome
            
        return msg
    
    def adicionar_conteudo(self, nome, conteudo):
        if self.arquivo_existe(nome):
            arquivo = self.ler_arquivo(nome) 
            if arquivo:
                escrever_arquivo = open("%s/%s" % (settings.DOCUMENTOS, nome), "w")
                escrever_arquivo.write(arquivo+conteudo)
                
                msg = "O arquivo %s foi alterado com sucesso!" % nome
            else:
                msg = "Ocorreu um erro ao adicionar o conteúdo no arquivo."
                
            escrever_arquivo.close()
        
        else:
            msg = "O arquivo %s não foi encontrado." % nome
            
        return msg
    
    def deletar_arquivo(self, nome):
        if self.arquivo_existe(nome):
            os.remove("%s/%s" % (settings.DOCUMENTOS, nome))
            msg = "Arquivo deletado com sucesso!"
        
        else:
            msg = "O arquivo %s não foi encontrado." % nome
            
        return msg