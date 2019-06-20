from django.shortcuts import render
from django.http import HttpResponse
from .controller import *
import json

# def index(request):
# 	return render( request, 'main/index.html' )

def toJSON(self):
		return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

def guardar_do(request):
	return render(request, 'guardar_docente.html')

def actualizar_do(request):
	return render(request, 'actualizar_docente.html')

def listar_do(request):
	controller = Controller_docente()
	resul = controller.listar_docentes()
	dic = {'resul':resul}
	print(resul)

	return render(request, 'listar_docente.html', {'dic':dic})

def salones(request):
	return render(request, 'listar_salon.html')

def index(request):
	return render(request, 'index.html')

def listar_docente(request):
	controller = Controller_docente()
	resul = controller.listar_docentes()
	dic = {'resul':resul }

	return HttpResponse(toJSON(dic), content_type='application/json')

def actualizar_docente(request):
	controller = Controller_docente()
	idd = request.POST.get('id')
	docente = {'id':idd}
	for key in docente:
		print key, ":", docente[key]
	resul = controller.listar_mostrar_docentes(docente)
	dic = {'resul':resul }

	return HttpResponse(toJSON(dic), content_type='application/json')

def actualizar_guardar_docente(request):
	controller = Controller_docente()
	idd = request.POST.get('id')
	docente1 = request.POST.get('nombre')
	docente2 = request.POST.get('apellido')
	docente3 = request.POST.get('cedula')
	docente = {'id':idd, 'nombre':docente1, 'apellido':docente2, 'cedula':docente3}
	for key in docente:
		print key, ":", docente[key]
	resul = controller.actualizar_docentes(docente)
	dic = {'resul':resul }

	return HttpResponse(toJSON(dic), content_type='application/json')

def guardar_docente(request):
	controller = Controller_docente()
	docente1 = request.POST.get('nombre')
	docente2 = request.POST.get('apellido')
	docente3 = request.POST.get('cedula')
	docente = {'nombre':docente1, 'apellido':docente2, 'cedula':docente3}
	for key in docente:
		print key, ":", docente[key]
	resul = controller.guardar_docentes(docente)
	print(resul)

	return HttpResponse(json.dumps(resul), content_type='application/json')

def eliminar_docente(request):
	controller = Controller_docente()
	idd = request.POST.get('id')
	docente = {'id':idd}
	for key in docente:
		print key, ":", docente[key]
	resul = controller.eliminar_docentes(docente)
	dic = {'resul':resul }

	return HttpResponse(toJSON(dic), content_type='application/json')

def listar_salones(request):
	controller = Controller_salon()
	resul = controller.listar_salones()
	dic = {'resul':resul }

	return HttpResponse(toJSON(dic), content_type='application/json')

def actualizar_salon(request):
	controller = Controller_salon()
	idd = request.POST.get('id')
	salon = {'id':idd}
	for key in salon:
		print key, ":", salon[key]
	resul = controller.listar_mostrar_salones(salon)
	dic = {'resul':resul }

	return HttpResponse(toJSON(dic), content_type='application/json')

def actualizar_guardar_salon(request):
	controller = Controller_salon()
	idd = request.POST.get('id')
	salon1 = request.POST.get('detalle')
	salon = {'id':idd, 'detalle':salon1}
	for key in salon:
		print key, ":", salon[key]
	resul = controller.actualizar_salones(salon)
	dic = {'resul':resul }

	return HttpResponse(toJSON(dic), content_type='application/json')

def guardar_salon(request):
	controller = Controller_salon()
	salon1 = request.POST.get('detalle')
	salon = {'detalle':salon1}
	for key in salon:
		print key, ":", salon[key]
	resul = controller.guardar_salones(salon)
	print(resul)

	return HttpResponse(json.dumps(resul), content_type='application/json')

def eliminar_salon(request):
	controller = Controller_salon()
	idd = request.POST.get('id')
	salon = {'id':idd}
	for key in salon:
		print key, ":", salon[key]
	resul = controller.eliminar_salones(salon)
	dic = {'resul':resul }

	return HttpResponse(toJSON(dic), content_type='application/json')

def listar_registro(request):
	controller = Controller_registro()
	resul = controller.listar_registros()
	dic = {'resul':resul }

	return HttpResponse(toJSON(dic), content_type='application/json')

def actualizar_registro(request):
	controller = Controller_registro()
	idd = request.POST.get('id')
	registro = {'id':idd}
	for key in registro:
		print key, ":", registro[key]
	resul = controller.listar_mostrar_registros(registro)
	dic = {'resul':resul }
	print(dic)

	return HttpResponse(toJSON(dic), content_type='application/json')

def actualizar_guardar_registro(request):
	controller = Controller_registro()
	idd = request.POST.get('id')
	registro1 = request.POST.get('docente_id')
	registro2 = request.POST.get('salon_id')
	registro3 = request.POST.get('fecha')
	registro4 = request.POST.get('hora_inicio')
	registro5 = request.POST.get('hora_fin')
	registro6 = request.POST.get('objetivo')
	registro = {'id':idd, 'docente_id':registro1, 'salon_id':registro2, 'fecha':registro3, 'hora_inicio':registro4, 'hora_fin':registro5, 'objetivo':registro6}
	for key in registro:
		print key, ":", registro[key]
	resul = controller.actualizar_registros(registro)
	dic = {'resul':resul }

	return HttpResponse(toJSON(dic), content_type='application/json')

def guardar_registro(request):
	controller = Controller_registro()
	registro1 = request.POST.get('docente_id')
	registro2 = request.POST.get('salon_id')
	registro3 = request.POST.get('fecha')
	registro4 = request.POST.get('hora_inicio')
	registro5 = request.POST.get('hora_fin')
	registro6 = request.POST.get('objetivo')
	registro = {'docente_id':registro1, 'salon_id':registro2, 'fecha':registro3, 'hora_inicio':registro4, 'hora_fin':registro5, 'objetivo':registro6}
	for key in registro:
		print key, ":", registro[key]
	resul = controller.guardar_registros(registro)
	print(resul)

	return HttpResponse(json.dumps(resul), content_type='application/json')

def eliminar_registro(request):
	controller = Controller_registro()
	idd = request.POST.get('id')
	registro = {'id':idd}
	for key in registro:
		print key, ":", registro[key]
	resul = controller.eliminar_registros(registro)
	dic = {'resul':resul }

	return HttpResponse(toJSON(dic), content_type='application/json')

def listar_docentes2(request):
	controller = Controller_registro()
	resul = controller.listar_docentes2()
	dic = {'resul':resul }

	return HttpResponse(toJSON(dic), content_type='application/json')

def listar_salones2(request):
	controller = Controller_registro()
	resul = controller.listar_salones2()
	dic = {'resul':resul }

	return HttpResponse(toJSON(dic), content_type='application/json')

def filtrar_registro(request):
	controller = Controller_registro()
	fecha = request.POST.get('fecha')
	registro = {'fecha':fecha}
	for key in registro:
		print key, ":", registro[key]
	resul = controller.filtrar_registro(registro)
	dic = {'resul':resul }
	print(dic)

	return HttpResponse(toJSON(dic), content_type='application/json')

def filtrar_registro2(request):
	controller = Controller_registro()
	docente_id = request.POST.get('nombre')
	registro = {'docente_id':docente_id}
	for key in registro:
		print key, ":", registro[key]
	resul = controller.filtrar_registro2(registro)
	print(resul);
	dic = {'resul':resul }
	print(dic)

	return HttpResponse(toJSON(dic), content_type='application/json')
