from zeep import Client
class Controller_docente:
	wsdl = 'http://localhost:8080/servidor-clase/crud_docente_ws?WSDL'
	client = Client(wsdl)

	def guardar_docentes(self, docente):
		return self.client.service.guardar_docente(docente)

	def actualizar_docentes(self, docente):
		return self.client.service.actualizar_docente(docente)

	def listar_mostrar_docentes(self, docente):
		return self.client.service.listar_mostrar_docente(docente)

	def eliminar_docentes(self, docente):
		return self.client.service.eliminar_docente(docente)

	def listar_docentes(self):
		return self.client.service.listar_docente()

class Controller_salon:
	wsdl = 'http://localhost:8080/servidor-clase/crud_salon_ws?WSDL'
	client = Client(wsdl)

	def guardar_salones(self, salones):
		return self.client.service.guardar_salon(salones)

	def actualizar_salones(self, salon):
		return self.client.service.actualizar_salon(salon)

	def listar_mostrar_salones(self, salon):
		return self.client.service.listar_mostrar_salon(salon)

	def eliminar_salones(self, salon):
		return self.client.service.eliminar_salon(salon)

	def listar_salones(self):
		return self.client.service.listar_salon()

class Controller_registro:
	wsdl = 'http://localhost:8080/servidor-clase/crud_registro_ws?WSDL'
	client = Client(wsdl)

	def guardar_registros(self, registro):
		return self.client.service.guardar_registro(registro)

	def actualizar_registros(self, registro):
		return self.client.service.actualizar_registro(registro)

	def listar_mostrar_registros(self, registro):
		return self.client.service.listar_mostrar_registro(registro)

	def eliminar_registros(self, registro):
		return self.client.service.eliminar_registro(registro)

	def listar_registros(self):
		return self.client.service.listar_registro()

	def listar_docentes2(self):
		return self.client.service.listar_docente2()

	def listar_salones2(self):
		return self.client.service.listar_salon2()

	def filtrar_registro(self, registro):
		return self.client.service.filtrar_registro(registro)

	def filtrar_registro2(self, registro):
		return self.client.service.filtrar_registro2(registro)