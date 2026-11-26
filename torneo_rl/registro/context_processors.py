from inscripcion.models import Inscripcion

# Archivo creado para usar variables sin necesidad de pasarlos por una vista.

def inscripcion_context(request): # Metodo para guardar las inscripciones sin necesidad de vista.
    if request.user.is_authenticated:
        mi_inscripcion = Inscripcion.objects.filter(usuario=request.user).first()
    else:
        mi_inscripcion = None
    return {"mi_inscripcion": mi_inscripcion}