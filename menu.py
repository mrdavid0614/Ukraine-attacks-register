from ataque import AtaqueModel
from pathlib import Path
from folium import Map, Marker
import webbrowser

def agregarAtaque():
    print("-------- Información del Ataque --------\n")
    codigo = input("Ingrese el código del ataque: ")
    responsable = input("Ingrese el nombre del responsable del ataque: ")
    ciudad = input("Ingrese el nombre de la ciudad atacada: ")
    fecha = input("Ingrese la fecha en la que ocurrió el ataque: ")
    detalles = input("Ingrese los detalles sobre qué fue destruido durante el ataque: ")
    valor_monetario = input("Ingrese el valor monetario de este ataque: ")
    fallecidos = input("Ingrese la cantidad de fallecidos durante el ataque: ")
    heridos = input("Ingrese la cantidad de heridos durante el ataque: ")
    coordenadas = input("Ingrese las coordenadas del sitio donde ocurrió: ").split(",")
    latitud = coordenadas[0]
    longitud = coordenadas[1].strip()

    try:
        AtaqueModel.create(codigo=codigo, responsable=responsable, ciudad=ciudad, fecha=fecha, detalles=detalles, valor_monetario=valor_monetario, fallecidos=fallecidos, heridos=heridos, latitud=latitud, longitud=longitud)
        print("El ataque se ha añadido exitosamente...")
    except:
        print("Hubo un error mientras se creaba el ataque...")

def borrarAtaque():
    codigo = input("Ingrese el código del ataque que desea borrar: ")
    
    try:
        AtaqueModel.delete_by_id(codigo)
        print("El ataque se ha borrado exitosamente...")
    except:
        print("Hubo un error mientras se intentaba borrar el ataque...")

def exportarAtaque():
    codigo = input("Ingrese el código del ataque que desea exportar: ")

    try:
        ataque = AtaqueModel.get_by_id(codigo)
        cuerpo_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ataque a Ucrania</title>
</head>
<body>
    <h1>Ataque {ataque.codigo}</h1>

    <div class="info">
        <p>Responsable: {ataque.responsable}</p>
        <p>Ciudad: {ataque.ciudad}</p>
        <p>Fecha: {ataque.fecha}</p>
        <p>Detalles: {ataque.detalles}</p>
        <p>Valor Monetario: {ataque.valor_monetario}</p>
        <p>Fallecidos: {ataque.fallecidos}</p>
        <p>Heridos: {ataque.heridos}</p>
        <p>Coordenadas: {ataque.latitud}, {ataque.longitud}</p>
    </div>
</body>
</html>
        """
        html = open(f"./ataque{ataque.codigo}.html", "w", encoding="utf-8")
        html.write(cuerpo_html)
        html.close()

        webbrowser.open(f"file:///{Path().resolve()}/ataque{ataque.codigo}.html")

    except:
        print("Hubo un error al obtener el ataque...")

def exportarAtaques():
    ataques = AtaqueModel.select()

    mapa = Map(location=[50.418041, 30.514424], zoom_start=6)

    for ataque in ataques:
        Marker(location=[ataque.latitud, ataque.longitud], popup=f"<p><strong>Ataque:<strong> {ataque.codigo}</p><p><strong>Responsable:<strong> {ataque.responsable}</p><p><strong>Fecha:<strong> {ataque.fecha}</p>", tooltip=f"Ataque {ataque.codigo}").add_to(mapa)

    mapa.save("mapa.html")
    webbrowser.open(f"file:///{Path().resolve()}/mapa.html")