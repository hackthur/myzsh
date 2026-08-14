from libqtile.config import Screen
from libqtile import bar
from libqtile import qtile  # CORREGIDO: Se importa desde libqtile
from .widgets import primary_widgets, secondary_widgets

def status_bar(widgets):
    return bar.Bar(widgets, 16, opacity=0.60)

# Ruta de tu fondo de pantalla clásico
mi_fondo = "~/.config/qtile/images/hackthur2.png"

# Creamos la lista de pantallas vacía
screens = []

# Detectar número de monitores de forma segura para Wayland y X11
num_monitores = 1

if qtile:
    try:
        if qtile.core and hasattr(qtile.core, "outputs"):
            # Backend Wayland
            num_monitores = len(qtile.core.outputs)
        elif hasattr(qtile, "conn") and hasattr(qtile.conn, "pseudoscreens"):
            # Backend X11 (Fallback seguro)
            num_monitores = len(qtile.conn.pseudoscreens)
    except Exception:
        num_monitores = 1

# Configuramos la pantalla principal (Monitor 1)
screens.append(
    Screen(
        top=status_bar(primary_widgets),
        wallpaper=mi_fondo,
        wallpaper_mode="fill"
    )
)

# Si tienes más monitores conectados, les añade su barra secundaria
if num_monitores > 1:
    for _ in range(1, num_monitores):
        screens.append(
            Screen(
                top=status_bar(secondary_widgets),
                wallpaper=mi_fondo,
                wallpaper_mode="fill"
            )
        )



