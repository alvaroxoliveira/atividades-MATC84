import json
import unittest
import xml.etree.ElementTree as ET

class DesafiosJsonXml(unittest.TestCase):

	#Desafio 1
	#Vamos começar com um desafio de exemplo, que vamos resolver juntos.
	#Preencha a string abaixo com um JSON que, quando deserializado, se torne:
	#Um objeto com atributos nome e cargo, onde o nome é "Fred" e cargo é "Professor de Lab Web"
	def reposta_1(self):
		return '{ "nome": "Fred", "cargo": "Professor de Lab Web" }'

	#Desafio 2
	#Vamos agora com um desafio muito semelhante ao primeiro, mas com XML.
	#Preencha a string abaixo com um XML que, quando deserializado, contenha:
	#Um objeto com tag professor, e um atributo chamado nome com valor "Fred" 
	#e um atributo chamado cargo com valor "Professor de Lab Web"
	def reposta_2(self):
		return "\
<?xml version=\"1.0\"?>\
<dados>\
    <professor nome=\"Fred\" cargo=\"Professor de Lab Web\"/>\
</dados>\
"

	#Desafio 3
	#Dona Neya Matofino é uma senhora que sofre de Síndrome Jsônica, 
	#uma doença onde ela só consegue ler JSON.
	#Ela não sabe mexer em computadores, e pediu que você ajude ela 
	#a escrever a lista de compras dela.
	#Ela quer três listas, uma chamada frutas, uma chamada legumes e uma chamada vegetais.
	#Ela precisa que a lista de frutas contenha banana e manga.
	#Ela precisa que a lista de legumes contenha chuchu e abobrinha.
	#Ela precisa que a lista de vegetais contenha alface e couve.
	#Preencha a string abaixo com um JSON que, quando deserializado, se torne um objeto com as três listas da Dona Maria.	
	def reposta_3(self):
		return '{ "frutas": ["banana", "manga"], "legumes": ["chuchu", "abobrinha"], "vegetais": ["alface", "couve"] }'

	#Desafio 4
	#Seu primo Max Verstappen adora carros, e quando soube que você faz computação na UFBA,
	#não se aguentou e pediu sua ajuda.
	#Ele quer que você crie um XML cujos dados contenham 2 objetos com tag carro.
	#O primeiro deve ter nome "Golf", e um atributo chamado fabricante,
	#com nome "Volkswagen" e origem "Alemanha"
	#O segundo deve ter nome "Uno Mille", e um atributo chamado fabricante,
	#com nome "Fiat" e origem "Itália"
	def reposta_4(self):
		return "\
<?xml version=\"1.0\"?>\
<dados>\
    <carro nome=\"Golf\">\
		<aux/>\
		<fabricante nome=\"Volkswagen\" origem=\"Alemanha\"/>\
	</carro>\
    <carro nome=\"Uno Mille\">\
		<aux/>\
		<fabricante nome=\"Fiat\" origem=\"Itália\"/>\
	</carro>\
</dados>\
"

	#Desafio 5
	#Tony Soprano é um pizzaiolo muito ocupado, e te contratou para ajudá-lo a usar o
	#mais novo app de entregas, o iShoot.
	#O cardápio contém 3 pizzas, cada uma com 2 atributos: tamanho e coberturas
	#Uma pizza é a de tamanho "brotinho", com coberturas "parmesão" e "pepperoni"
	#Uma pizza é a de tamanho "médio", com coberturas "anchovas", "mussarela" e "champignon"
	#Uma pizza é a de tamanho "família", com coberturas "presunto" e "abacaxi"
	#Ele precisa que você tranforme o cardápio dele em um JSON, pra enviar ao app do iShoot, que só aceita esse formato.
	#O iShoot exige que o JSON seja desserializável para um dicionário, onde as chaves são o tamanho da pizza e os valores são listas chamadas coberturas!
	def reposta_5(self):
		return '{ "brotinho": {"coberturas": ["parmesão", "pepperoni"]}, "médio": {"coberturas": ["anchovas", "mussarela", "champignon"]}, "família": {"coberturas": ["presunto", "abacaxi"]}}'



	#ATENÇÃO! Qualquer manipulação do código abaixo resultará em nota zero para a equipe.
	#Ele está aqui para que vocês possam ver exatamente o que o desafio está pedindo.

	def test_desafio_1(self):
		resposta_do_aluno = self.reposta_1()
		python_obj = json.loads(resposta_do_aluno)
		self.assertEqual(python_obj["nome"], "Fred")
		self.assertEqual(python_obj["cargo"], "Professor de Lab Web")

	def test_desafio_2(self):
		resposta_do_aluno = self.reposta_2()
		root = ET.fromstring(resposta_do_aluno)
		self.assertEqual(root[0].attrib["nome"], "Fred")
		self.assertEqual(root[0].attrib["cargo"], "Professor de Lab Web")

	def test_desafio_3(self):
		resposta_do_aluno = self.reposta_3()
		python_obj = json.loads(resposta_do_aluno)
		self.assertTrue("banana" in python_obj["frutas"])
		self.assertTrue("manga" in python_obj["frutas"])
		self.assertTrue("chuchu" in python_obj["legumes"])
		self.assertTrue("abobrinha" in python_obj["legumes"])
		self.assertTrue("alface" in python_obj["vegetais"])
		self.assertTrue("couve" in python_obj["vegetais"])

	def test_desafio_4(self):
		resposta_do_aluno = self.reposta_4()
		root = ET.fromstring(resposta_do_aluno)
		for child in root:
			self.assertEqual(child.tag, "carro")
		self.assertEqual(root[0].attrib["nome"], "Golf")
		self.assertEqual(root[0][1].attrib["nome"], "Volkswagen")
		self.assertEqual(root[0][1].attrib["origem"], "Alemanha")
		self.assertEqual(root[1].attrib["nome"], "Uno Mille")
		self.assertEqual(root[1][1].attrib["nome"], "Fiat")
		self.assertEqual(root[1][1].attrib["origem"], "Itália")

	def test_desafio_5(self):
		resposta_do_aluno = self.reposta_5()
		python_obj = json.loads(resposta_do_aluno)
		self.assertTrue("parmesão" in python_obj["brotinho"]["coberturas"])
		self.assertTrue("pepperoni" in python_obj["brotinho"]["coberturas"])
		self.assertTrue("anchovas" in python_obj["médio"]["coberturas"])
		self.assertTrue("mussarela" in python_obj["médio"]["coberturas"])
		self.assertTrue("champignon" in python_obj["médio"]["coberturas"])
		self.assertTrue("presunto" in python_obj["família"]["coberturas"])
		self.assertTrue("abacaxi" in python_obj["família"]["coberturas"])

if __name__ == '__main__':
	print("\n\n\n\n\n")
	unittest.main()