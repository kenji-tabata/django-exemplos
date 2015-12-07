from django.test import TestCase
from checkbox.models import Transportes

from django.test import Client

class TransportesTest(TestCase):
    def setUp(self):
        self.transporte1 = {
            'id': 1,
            'carro': 'Sim',
            'moto': 'Não',
            'onibus': 'Não',
            'bicicleta': 'Sim',
        }
                
    def test_inserir_transporte(self):
        transporte = Transportes.objects.create(**self.transporte1)
        self.assertEqual(transporte.id, 1)
        
        
    def test_carregar_alternativas(self):
        transporte = Transportes.objects.create(**self.transporte1)
        
        get_transporte = Transportes.objects.get(id=1)
        
        
        

    def test_enviar_checkbox_selecionados(self):
        client = Client()
        check1 = client.post('/checkbox/enviar/', {'carro':'Sim','moto':'Não','onibus':'Sim','bicicleta':'Sim'})
        check2 = client.post('/checkbox/enviar/', {'carro':'Sim','onibus':'Sim','bicicleta':'Sim'})
        check3 = client.post('/checkbox/enviar/', {'moto':'Não','onibus':'Sim'})
        check4 = client.post('/checkbox/enviar/', {'onibus':'Sim'})
        check5 = client.post('/checkbox/enviar/', {})
        check6 = client.post('/checkbox/enviar', {})
        check7 = client.get('/checkbox/enviar/')
        
        self.assertEqual(check1.status_code, 200)
        self.assertEqual(check2.status_code, 200)
        self.assertEqual(check3.status_code, 200)
        self.assertEqual(check4.status_code, 200)
        self.assertEqual(check5.status_code, 200)
        self.assertEqual(check6.status_code, 301)
        self.assertEqual(check7.status_code, 200)
        
