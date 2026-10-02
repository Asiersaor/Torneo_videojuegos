from inscripcion.models import Inscripcion

def inscripcion_context(request):
    if request.user.is_authenticated:
        mi_inscripcion = Inscripcion.objects.filter(usuario=request.user).first()
    else:
        mi_inscripcion = None
    return {"mi_inscripcion": mi_inscripcion}