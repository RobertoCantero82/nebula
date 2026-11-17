---
titulo: "Querían espiar correos de la OTAN y la UE: el programa se escondía en un servidor rumano"
descripcion: "ESET atribuye a Turla una herramienta que seleccionaba correspondencia institucional. Rumanía afirma que frenó el ataque y no identificó extracción de datos sensibles."
categoria: tecnologia
fecha: 2026-11-17
cifraDestacada: "2025"
etiquetaCifra: "el año del ataque"
fondoPortada: "Cereal"
mostrarCifraInterior: false
formato: visual
pantallas:
  - etiqueta: "01 | El objetivo"
    titulo: "Para buscar correos de la OTAN y la UE, entraron en una institución rumana."
    tipo: recorrido
    datos: ["Institución rumana", "Servidor de correo", "Selección de mensajes", "OTAN y UE"]
    texto:
      - "ESET ha descubierto Cereal, un conjunto de programas maliciosos preparado para seleccionar correos enviados a instituciones de la OTAN y la Unión Europea, o recibidos de ellas. Lo encontró en un organismo gubernamental de Rumanía."
  - etiqueta: "02 | Las fechas"
    titulo: "La noticia es de noviembre. El ataque ocurrió en diciembre de 2025."
    tipo: video-youtube
    videoId: "b7kEr04BjxM"
    pieImagen: "Vídeo seleccionado para acompañar esta noticia. Enlace directo disponible en las fuentes."
    texto:
      - "La fecha importa: el Servicio Rumano de Información afirma que detectó la intrusión en diciembre de 2025 y tomó medidas para frenarla y reparar sus efectos. Su comunicado del 11 de noviembre de 2026 describe una actuación pasada, no un ataque recién descubierto."
  - etiqueta: "03 | El escondite"
    titulo: "El servidor de la víctima también servía para recibir órdenes."
    tipo: interactivo-datos
    datos: ["Dónde se ocultaba", "Qué buscaba", "Cómo recibía órdenes"]
    respuestas:
      - "En Microsoft Exchange, el sistema que gestionaba el correo de la organización. El código se integraba en procesos legítimos."
      - "Una de sus piezas, CerealBox, filtraba la correspondencia para apartar copias de mensajes de interés."
      - "Los investigadores no observaron servidores externos de control: el propio Exchange comprometido recibía las instrucciones."
    texto:
      - "Pulsa cada opción para entender el mecanismo descrito por ESET. El programa aprovechaba el sistema de correo que la organización ya utilizaba."
  - etiqueta: "04 | La atribución"
    titulo: "ESET señala a Turla, un grupo vinculado a los servicios de inteligencia rusos."
    tipo: contraste
    datos: ["ESET: atribución con alta confianza", "Rumanía: identifica a Turla"]
    texto:
      - "La empresa basa su atribución en herramientas coincidentes y semejanzas con programas anteriores. Su informe vincula a Turla con el Servicio Federal de Seguridad ruso. Es una conclusión de los investigadores."
      - "El comunicado rumano también atribuye el ataque a Turla y afirma que el caso se abordó con socios europeos, de la UE y de la OTAN."
  - etiqueta: "05 | El alcance"
    titulo: "Buscar correos sensibles no demuestra que consiguieran sacarlos."
    tipo: cierre
    texto:
      - "Rumanía afirma que detuvo el ataque, reparó el servicio de correo y no identificó extracción de datos sensibles. Esa es la versión oficial sobre sus consecuencias."
      - "El objetivo descrito por ESET y el balance de las autoridades responden a preguntas distintas: qué buscaba el programa y qué daño se pudo confirmar. No hay una cifra pública verificada de correos robados."
fuentes:
  - nombre: "ESET · Investigación original"
    detalle: "Informe de Matías Porolli publicado el 10 de noviembre de 2026: funcionamiento de Cereal, objetivo de la selección y atribución a Turla"
    url: "https://www.welivesecurity.com/en/eset-research/exchange-for-breakfast-turlas-cereal-tricks-are-not-for-kids/"
  - nombre: "Servicio Rumano de Información"
    detalle: "Comunicado del 11 de noviembre de 2026: ataque detenido, servicio reparado y ausencia de extracción de datos sensibles identificada"
    url: "https://www.sri.ro/articole/comunicat-de-presa-11-11-2026.html"
  - nombre: "TechRadar · Noticia de partida"
    detalle: "Publicada el 17 de noviembre de 2026; contrastada con la investigación y el comunicado oficial"
    url: "https://www.techradar.com/pro/security/russian-hackers-target-romanian-servers-to-steal-nato-eu-emails"
  - nombre: "YouTube · Vídeo seleccionado"
    detalle: "Vídeo facilitado para acompañar la pieza; la comprobación de los hechos se apoya en ESET y el comunicado rumano"
    url: "https://www.youtube.com/watch?v=b7kEr04BjxM"
---
