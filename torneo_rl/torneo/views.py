from django.shortcuts import render, redirect
from inscripcion.models import Inscripcion
from .models import Enfrentamiento, Partida

# Create your views here.
def generar_torneo(request):
    enfrentamiento_cuartos = []
    if request.user.rol != "admin":
        return redirect("home")
    inscripciones = list(Inscripcion.objects.all())
    if len(inscripciones) != 8:
        return redirect("home")
    dict_nivel = {"LOW": 0, "MID": 1, "PRO": 2}
    inscripciones = sorted(inscripciones, key=lambda i: dict_nivel[i.nivel])
    for i in range(0, len(inscripciones), 2):
        enfrentamiento_cuartos.append(Enfrentamiento.objects.create(participante_1 = inscripciones[i], participante_2 = inscripciones[i + 1], ronda = Enfrentamiento.nivel_rondas.CUARTOS))
    semifinal_1 = Enfrentamiento.objects.create(ronda = Enfrentamiento.nivel_rondas.SEMIFINALES)
    semifinal_2 = Enfrentamiento.objects.create(ronda = Enfrentamiento.nivel_rondas.SEMIFINALES)
    enfrentamiento_cuartos[0].siguiente_enfrentamiento = semifinal_1
    enfrentamiento_cuartos[0].save()
    enfrentamiento_cuartos[1].siguiente_enfrentamiento = semifinal_1
    enfrentamiento_cuartos[1].save()
    enfrentamiento_cuartos[2].siguiente_enfrentamiento = semifinal_2
    enfrentamiento_cuartos[2].save()
    enfrentamiento_cuartos[3].siguiente_enfrentamiento = semifinal_2
    enfrentamiento_cuartos[3].save()
    final = Enfrentamiento.objects.create(ronda = Enfrentamiento.nivel_rondas.FINAL)
    semifinal_1.siguiente_enfrentamiento = final
    semifinal_1.save()
    semifinal_2.siguiente_enfrentamiento = final
    semifinal_2.save()
def encuentros(request, id):
    if request.user.rol != "admin":
        return redirect("home")
    enfrentamiento = Enfrentamiento.objects.get(id=id)
    if request.method == "POST":
        ganador = request.POST.get("ganador")
        if ganador == "1":
            ganador_partida = enfrentamiento.participante_1
        else:
            ganador_partida = enfrentamiento.participante_2
        numero_partida = Partida.objects.filter(enfrentamiento=enfrentamiento).count() + 1
        Partida.objects.create(enfrentamiento=enfrentamiento, numero_de_partidas=numero_partida, ganador_partida=ganador_partida)
        if ganador_partida == enfrentamiento.participante_1:
            enfrentamiento.victorias_participante_1 += 1
        elif ganador_partida == enfrentamiento.participante_2:
            enfrentamiento.victorias_participante_2 += 1
        enfrentamiento.save()
        if enfrentamiento.victorias_participante_1 == 2:
            enfrentamiento.ganador_enfrentamiento = enfrentamiento.participante_1
        elif enfrentamiento.victorias_participante_2 == 2:
            enfrentamiento.ganador_enfrentamiento = enfrentamiento.participante_2
        enfrentamiento.save()
        siguiente = enfrentamiento.siguiente_enfrentamiento
        if siguiente:
            if siguiente.participante_1 is None:
                siguiente.participante_1 = enfrentamiento.ganador_enfrentamiento
            else:
                siguiente.participante_2 = enfrentamiento.ganador_enfrentamiento
            siguiente.save()
        return redirect("home")
    return render(request, "torneo/construccion_torneo.html", {"enfrentamiento":enfrentamiento})
def ver_torneo(request):
    enfrentamientos = Enfrentamiento.objects.all()
    mi_inscripcion = Inscripcion.objects.filter(usuario=request.user).first()
    return render(request, "torneo/vista_torneo.html", {"enfrentamientos":enfrentamientos, "mi_inscripcion": mi_inscripcion})