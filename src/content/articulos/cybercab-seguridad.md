---
titulo: "¿El taxi sin conductor de Tesla conduce mejor o se enfrenta a menos dificultades?"
descripcion: "Los accidentes del Cybercab parecen ofrecer una respuesta. Al mirar dónde ocurren y a qué velocidad, la comparación se complica."
tema: "TECNOLOGÍA"
fecha: 2026-11-18T14:00:00+01:00
imagenPortada: "/nebula/imagenes/cybercab_seguridad_portada.png"
cifraDestacada: "8 accidentes"
etiquetaCifra: "del Cybercab, caso a caso"
textoContinuo: "¿El taxi de Tesla conduce mejor o se enfrenta a menos dificultades? Reviso 8 accidentes del Cybercab"
metodologia: "EDA de los CSV NHTSA publicados el 16 de noviembre de 2026, descargados el 17 y con informes recibidos hasta el 15 de octubre. Selecciono últimas versiones y activación verificada; agrupo por incidente y vehículo. Distingo ocho Cybercab, 43 casos Tesla autónomos y 2.407 con asistencia. Comparo velocidades, vías, datos ausentes y solapamiento descriptivo con bandas 0, 10 y 30 mph, además de otros cortes. No estimo tasas ni efectos causales: faltan exposición y gravedad comparable y los requisitos de notificación difieren. No genero predicciones propias."
---

**Si el taxi de Tesla circula despacio y por lugares más sencillos, ¿sus accidentes son menos graves porque conduce bien o porque se enfrenta a menos dificultades?** Imagina comparar a quien aparca frente a casa con quien pasa el día en carretera. Contar sus golpes puede ser fácil. Decidir quién conduce mejor exige bastante más.

La pregunta llega a tiempo. Electrek acaba de reunir ocho accidentes del Cybercab, el vehículo de Tesla concebido como taxi sin conductor. Cuatro aparecen bajo conducción autónoma y cuatro durante pruebas con asistencia al conductor. Es tentador convertir esa división en un examen de la máquina. Pero antes hay que mirar qué estaba haciendo en cada caso.

<div style="position:relative; aspect-ratio:16/9; margin:2rem 0;">
  <iframe
    src="https://www.youtube-nocookie.com/embed/Qfj4urMF8CU"
    title="Vídeo sobre el Cybercab de Tesla"
    style="position:absolute; inset:0; width:100%; height:100%; border:0;"
    loading="lazy"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    referrerpolicy="strict-origin-when-cross-origin"
    allowfullscreen
  ></iframe>
</div>

**He revisado los archivos originales de la agencia estadounidense de seguridad vial**, NHTSA. Tras eliminar actualizaciones repetidas, he confirmado esos ocho casos y ampliado la mirada a otros Tesla. Mi objetivo era comprobar si la menor gravedad observada podía confundirse con circular en circunstancias distintas. La primera sorpresa fue descubrir lo poco que se parecen las dos mitades del Cybercab.

## Ocho accidentes que no son el mismo examen

Los cuatro Cybercab registrados en conducción autónoma iban a **0, 0, 4,8 y 8 kilómetros por hora**. Tres incidentes ocurrieron en aparcamientos y uno en una calle. Ninguno declara lesiones. En dos, el vehículo estaba detenido cuando otro coche lo golpeó, según los relatos enviados por Tesla. Uno de los cuatro llevaba un supervisor a bordo: autónomo y sin supervisor no significan necesariamente lo mismo.

Los cuatro casos con asistencia dibujan otro escenario. Tres figuran en autopistas o autovías y uno en una intersección. Sus velocidades declaradas fueron **0, 8, 17,7 y 85,3 kilómetros por hora**. Aquí hay dos registros con lesiones leves, uno sin lesiones declaradas y otro con gravedad desconocida.

El gráfico coloca los ocho casos sobre la misma escala. Cada punto es un incidente y su posición indica la velocidad declarada. Permite ver las diferencias sin confundir un recuento con una probabilidad de accidente.

<figure class="cybercab-figura"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 590" role="img" aria-labelledby="cybercab_velocidades-titulo cybercab_velocidades-descripcion"><title id="cybercab_velocidades-titulo">Ocho Cybercab, circunstancias distintas</title><desc id="cybercab_velocidades-descripcion">Velocidad declarada en km/h. Cuatro casos autónomos: 0, 0, 4,8 y 8,0. Cuatro con asistencia: 0, 8,0, 17,7 y 85,3. No representa riesgo.</desc><rect width="880" height="590" fill="#faf8f2"/><text x="24" y="33" font-family="Arial,sans-serif" font-size="24" fill="#172342">Ocho Cybercab, circunstancias distintas</text><text x="24" y="60" font-family="Arial,sans-serif" font-size="17" fill="#172342">Velocidad declarada en cada incidente (km/h)</text><path d="M380.0 82V510" stroke="#d6d9e2"/><text x="373.0" y="535" font-family="Arial,sans-serif" font-size="15" fill="#172342">0</text><path d="M468.0 82V510" stroke="#d6d9e2"/><text x="461.0" y="535" font-family="Arial,sans-serif" font-size="15" fill="#172342">20</text><path d="M556.0 82V510" stroke="#d6d9e2"/><text x="549.0" y="535" font-family="Arial,sans-serif" font-size="15" fill="#172342">40</text><path d="M644.0 82V510" stroke="#d6d9e2"/><text x="637.0" y="535" font-family="Arial,sans-serif" font-size="15" fill="#172342">60</text><path d="M732.0 82V510" stroke="#d6d9e2"/><text x="725.0" y="535" font-family="Arial,sans-serif" font-size="15" fill="#172342">80</text><path d="M820.0 82V510" stroke="#d6d9e2"/><text x="813.0" y="535" font-family="Arial,sans-serif" font-size="15" fill="#172342">100</text><text x="24" y="105" font-family="Arial,sans-serif" font-size="15" fill="#172342">Autónomo · Calle</text><circle cx="380.0" cy="100" r="7" fill="#446ddf"/><text x="391.0" y="105" font-family="Arial,sans-serif" font-size="15" fill="#446ddf">0.0</text><text x="24" y="158" font-family="Arial,sans-serif" font-size="15" fill="#172342">Autónomo · Aparcamiento</text><circle cx="380.0" cy="153" r="7" fill="#446ddf"/><text x="391.0" y="158" font-family="Arial,sans-serif" font-size="15" fill="#446ddf">0.0</text><text x="24" y="211" font-family="Arial,sans-serif" font-size="15" fill="#172342">Autónomo · Aparcamiento</text><circle cx="401.2433408" cy="206" r="7" fill="#446ddf"/><text x="412.2433408" y="211" font-family="Arial,sans-serif" font-size="15" fill="#446ddf">4.8</text><text x="24" y="264" font-family="Arial,sans-serif" font-size="15" fill="#172342">Autónomo · Aparcamiento</text><circle cx="415.405568" cy="259" r="7" fill="#446ddf"/><text x="426.405568" y="264" font-family="Arial,sans-serif" font-size="15" fill="#446ddf">8.0</text><text x="24" y="317" font-family="Arial,sans-serif" font-size="15" fill="#172342">Con asistencia · Autopista o autovía</text><circle cx="380.0" cy="312" r="7" fill="#785c34"/><text x="391.0" y="317" font-family="Arial,sans-serif" font-size="15" fill="#785c34">0.0</text><text x="24" y="370" font-family="Arial,sans-serif" font-size="15" fill="#172342">Con asistencia · Autopista o autovía</text><circle cx="415.405568" cy="365" r="7" fill="#785c34"/><text x="426.405568" y="370" font-family="Arial,sans-serif" font-size="15" fill="#785c34">8.0</text><text x="24" y="423" font-family="Arial,sans-serif" font-size="15" fill="#172342">Con asistencia · Intersección</text><circle cx="457.8922496" cy="418" r="7" fill="#785c34"/><text x="468.8922496" y="423" font-family="Arial,sans-serif" font-size="15" fill="#785c34">17.7</text><text x="24" y="476" font-family="Arial,sans-serif" font-size="15" fill="#172342">Con asistencia · Autopista o autovía</text><circle cx="755.2990208000001" cy="471" r="7" fill="#785c34"/><text x="766.2990208000001" y="476" font-family="Arial,sans-serif" font-size="15" fill="#785c34">85.3</text><text x="24" y="575" font-family="Arial,sans-serif" font-size="15" fill="#172342">Un punto por caso. La velocidad no atribuye la causa del choque.</text></svg><figcaption>Azul: conducción autónoma. Marrón: asistencia con conductor. Fuente: registros NHTSA revisados por Nebula.</figcaption><details><summary>Consultar los datos en una tabla</summary><div class="cybercab-tabla" role="region" aria-label="Tabla alternativa al gráfico" tabindex="0"><table><caption>Los ocho incidentes del Cybercab</caption><thead><tr><th scope="col">Informe</th><th scope="col">Sistema</th><th scope="col">km/h</th><th scope="col">Vía</th></tr></thead><tbody><tr><th scope="row">13781-17178</th><td>Autónomo</td><td>4,8</td><td>Aparcamiento</td></tr><tr><th scope="row">13781-16941</th><td>Autónomo</td><td>0,0</td><td>Calle</td></tr><tr><th scope="row">13781-16733</th><td>Autónomo</td><td>0,0</td><td>Aparcamiento</td></tr><tr><th scope="row">13781-16672</th><td>Autónomo</td><td>8,0</td><td>Aparcamiento</td></tr><tr><th scope="row">13781-16964</th><td>Asistencia</td><td>8,0</td><td>Autopista o autovía</td></tr><tr><th scope="row">13781-16881</th><td>Asistencia</td><td>85,3</td><td>Autopista o autovía</td></tr><tr><th scope="row">13781-16583</th><td>Asistencia</td><td>0,0</td><td>Autopista o autovía</td></tr><tr><th scope="row">13781-16524</th><td>Asistencia</td><td>17,7</td><td>Intersección</td></tr></tbody></table></div></details></figure>

Hay un detalle que rompe la explicación rápida: **los dos casos con lesiones declaradas iban a 8 y 17,7 kilómetros por hora**. En el de 85,3, la gravedad es desconocida. La velocidad más alta no identifica automáticamente el accidente con lesiones. Tampoco una velocidad baja descarta que alguien resulte herido.

## Intenté ponerlos en condiciones parecidas

Para comparar con algo más de sentido, agrupé los casos por tipo de vía y tramos de velocidad. La idea era sencilla: enfrentar situaciones más parecidas, en vez de comparar una maniobra de aparcamiento con un recorrido de autopista. **Entre los ocho Cybercab no apareció ningún caso que compartiera ambas características con el grupo contrario**, usando esos tramos.

Eso no demuestra que sus recorridos nunca se parezcan. Demuestra que esta pequeña muestra no ofrece la comparación que necesitábamos. Además, una calle con peatones puede plantear problemas muy distintos de una autopista despejada. El nombre de la vía tampoco mide por sí solo su dificultad.

Prueba a filtrar los incidentes por entorno y velocidad. Verás qué casos quedan y qué sabemos de sus consecuencias. Si desaparece un grupo, no significa que conduzca sin accidentes: significa que no hay registros de ese grupo dentro de tu selección.

<section class="cybercab-explora" aria-labelledby="cybercab-titulo">
  <h3 id="cybercab-titulo">¿Estamos comparando situaciones parecidas?</h3>
  <p>Filtra los ocho Cybercab. Cada tarjeta es un caso, con su velocidad declarada y las consecuencias que constan en el registro.</p>
  <div class="cybercab-filtros">
    <label for="cybercab-sistema">Funcionamiento<select id="cybercab-sistema"><option value="todos">Ambos grupos</option><option value="ADS">Conducción autónoma</option><option value="ADAS">Asistencia con conductor</option></select></label>
    <label for="cybercab-via">Entorno<select id="cybercab-via"><option value="todos">Todos los entornos</option><option>Aparcamiento</option><option>Calle</option><option>Intersección</option><option>Autopista o autovía</option></select></label>
    <label for="cybercab-velocidad">Velocidad<select id="cybercab-velocidad"><option value="todos">Todas las velocidades</option><option value="parado">Parado: 0 km/h</option><option value="lento">Más de 0 y hasta 16,1 km/h</option><option value="medio">Más de 16,1 y hasta 48,3 km/h</option><option value="rapido">Más de 48,3 km/h</option></select></label>
  </div>
  <p id="cybercab-recuento" role="status" aria-live="polite" aria-atomic="true">8 casos: 4 autónomos y 4 con asistencia.</p>
  <ol class="cybercab-casos"><li data-caso data-sistema="ADS" data-via="Calle" data-velocidad="0.0"><strong>Conducción autónoma · 0.0 km/h</strong><span>Calle · Sin lesiones declaradas</span><small>Informe 13781-16941</small></li><li data-caso data-sistema="ADS" data-via="Aparcamiento" data-velocidad="0.0"><strong>Conducción autónoma · 0.0 km/h</strong><span>Aparcamiento · Sin lesiones declaradas</span><small>Informe 13781-16733</small></li><li data-caso data-sistema="ADS" data-via="Aparcamiento" data-velocidad="3.0"><strong>Conducción autónoma · 4.8 km/h</strong><span>Aparcamiento · Sin lesiones declaradas</span><small>Informe 13781-17178</small></li><li data-caso data-sistema="ADS" data-via="Aparcamiento" data-velocidad="5.0"><strong>Conducción autónoma · 8.0 km/h</strong><span>Aparcamiento · Sin lesiones declaradas</span><small>Informe 13781-16672 · Supervisor a bordo declarado</small></li><li data-caso data-sistema="ADAS" data-via="Autopista o autovía" data-velocidad="0.0"><strong>Asistencia con conductor · 0.0 km/h</strong><span>Autopista o autovía · Sin lesiones declaradas</span><small>Informe 13781-16583</small></li><li data-caso data-sistema="ADAS" data-via="Autopista o autovía" data-velocidad="5.0"><strong>Asistencia con conductor · 8.0 km/h</strong><span>Autopista o autovía · Lesiones leves; atención hospitalaria declarada</span><small>Informe 13781-16964</small></li><li data-caso data-sistema="ADAS" data-via="Intersección" data-velocidad="11.0"><strong>Asistencia con conductor · 17.7 km/h</strong><span>Intersección · Lesiones leves sin hospitalización declarada</span><small>Informe 13781-16524</small></li><li data-caso data-sistema="ADAS" data-via="Autopista o autovía" data-velocidad="53.0"><strong>Asistencia con conductor · 85.3 km/h</strong><span>Autopista o autovía · Gravedad desconocida</span><small>Informe 13781-16881</small></li></ol>
  <p class="cybercab-nota">No hay kilómetros recorridos para calcular riesgos. La selección no atribuye responsabilidad y los dos grupos tienen requisitos de notificación distintos.</p>
  <noscript><p>Para usar los filtros necesitas JavaScript. Los ocho casos permanecen visibles y puedes descargar su tabla al final.</p></noscript>
</section>
<style>
.cybercab-explora{background:#faf8f2;border:1px solid #c6ccdc;border-radius:12px;padding:clamp(16px,3vw,28px);margin:32px 0;color:#172342}.cybercab-explora h3{margin-top:0}.cybercab-explora strong{color:#172342}.cybercab-filtros{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}.cybercab-filtros label{font:600 15px/1.5 system-ui}.cybercab-filtros select{display:block;width:100%;min-height:48px;margin-top:7px;padding:8px;background:white;color:#172342;border:1px solid #65708b;border-radius:5px;font:15px system-ui}.cybercab-filtros select:focus-visible{outline:3px solid #294da7;outline-offset:3px}.cybercab-casos{list-style:none;margin:16px 0;padding:0;display:grid;gap:10px}.cybercab-casos li{border-left:4px solid #446ddf;background:white;padding:13px;display:grid;gap:5px}.cybercab-casos li[data-sistema="ADAS"]{border-left-color:#785c34}.cybercab-casos li[hidden]{display:none}.cybercab-casos span,.cybercab-casos small{display:block}.cybercab-casos small,.cybercab-nota{font:14px/1.6 system-ui;color:#46506a}.cybercab-figura{margin:32px 0;padding:16px;background:#faf8f2;border-radius:8px}.cybercab-figura svg{width:100%;height:auto;display:block}.cybercab-figura figcaption{font:15px/1.6 system-ui;color:#172342}.cybercab-figura details{margin-top:15px}.cybercab-figura summary{cursor:pointer;color:#294da7;min-height:44px;padding:8px}.cybercab-figura summary:focus-visible{outline:3px solid #294da7}.cybercab-tabla{overflow-x:auto}.cybercab-tabla table{width:100%;border-collapse:collapse;font:14px/1.5 system-ui}.cybercab-tabla td,.cybercab-tabla th{padding:9px;text-align:left;border-bottom:1px solid #bbc2d2}@media(max-width:650px){.cybercab-filtros{grid-template-columns:1fr}.cybercab-figura{padding:7px}.cybercab-casos strong{font-size:16px}}
</style>
<script>
(() => {
 const sistema = document.getElementById('cybercab-sistema');
 const via = document.getElementById('cybercab-via');
 const velocidad = document.getElementById('cybercab-velocidad');
 const estado = document.getElementById('cybercab-recuento');
 const casos = Array.from(document.querySelectorAll('[data-caso]'));
 if (!sistema || !via || !velocidad || !estado) return;
 function actualizar() {
   let autonomos = 0, asistencia = 0;
   for (const caso of casos) {
     const v = Number(caso.dataset.velocidad);
     const coincide_velocidad = velocidad.value === 'todos' || (velocidad.value === 'parado' && v === 0) || (velocidad.value === 'lento' && v > 0 && v <= 10) || (velocidad.value === 'medio' && v > 10 && v <= 30) || (velocidad.value === 'rapido' && v > 30);
     const visible = (sistema.value === 'todos' || caso.dataset.sistema === sistema.value) && (via.value === 'todos' || caso.dataset.via === via.value) && coincide_velocidad;
     caso.hidden = !visible;
     if (visible) { if (caso.dataset.sistema === 'ADS') autonomos++; else asistencia++; }
   }
   const total = autonomos + asistencia;
   estado.textContent = total ? `${total} casos: ${autonomos} autónomos y ${asistencia} con asistencia. ${!autonomos || !asistencia ? 'Esta selección no contiene casos de ambos grupos.' : 'Compartir un filtro no garantiza condiciones idénticas.'}` : 'No hay casos registrados con estos filtros. Eso no significa que el riesgo sea cero.';
 }
 for (const control of [sistema, via, velocidad]) control.addEventListener('change', actualizar);
 actualizar();
})();
</script>

## El dato que falta cambia la historia

Ampliar la mirada ayuda, pero también revela otro problema. Los archivos contienen **43 casos Tesla con conducción autónoma**, sumando Cybercab y Model Y. Ninguno figura en autopista o autovía y la mediana de velocidad es de 1,6 kilómetros por hora: la mitad de los registros queda por debajo o igual a esa cifra. Describe los incidentes, no todos sus viajes.

En los **2.407 casos con asistencia al conductor**, de distintos modelos Tesla, hay una barrera mayor: **2.319 tienen gravedad desconocida, el 96,3 %**. Incluso al quedarme con tipos de vía y tramos de velocidad presentes en ambos grupos, sigue faltando ese dato en 330 de los 355 casos con asistencia. Desconocido no significa que nadie resultara herido.

<figure class="cybercab-figura"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 330" role="img" aria-labelledby="lesiones_desconocidas-titulo lesiones_desconocidas-descripcion"><title id="lesiones_desconocidas-titulo">Faltan datos para comparar las lesiones</title><desc id="lesiones_desconocidas-descripcion">Porcentajes de casos Tesla por gravedad declarada. Se muestran lesiones, ausencia declarada y desconocidos por separado. No son tasas de accidente.</desc><rect width="880" height="330" fill="#faf8f2"/><text x="24" y="34" font-family="Arial,sans-serif" font-size="24" fill="#172342">Faltan datos para comparar las lesiones</text><text x="24" y="109" font-family="Arial,sans-serif" font-size="16" fill="#172342">Autónomos (n=43)</text><rect x="245" y="85" width="41.86046511627907" height="36" fill="#446ddf"/><rect x="286.8604651162791" y="85" width="558.1395348837209" height="36" fill="#657654"/><rect x="845.0" y="85" width="0.0" height="36" fill="#785c34"/><text x="245" y="144" font-family="Arial,sans-serif" font-size="16" fill="#172342">Gravedad desconocida: 0/43 (0.0 %)</text><text x="24" y="191" font-family="Arial,sans-serif" font-size="16" fill="#172342">Con asistencia (n=2407)</text><rect x="245" y="167" width="15.205650186954715" height="36" fill="#446ddf"/><rect x="260.2056501869547" y="167" width="6.730369754881595" height="36" fill="#657654"/><rect x="266.9360199418363" y="167" width="578.0639800581637" height="36" fill="#785c34"/><text x="245" y="226" font-family="Arial,sans-serif" font-size="16" fill="#172342">Gravedad desconocida: 2319/2407 (96.3 %)</text><rect x="24" y="258" width="12" height="12" fill="#446ddf"/><text x="43" y="269" font-family="Arial,sans-serif" font-size="15" fill="#172342">Lesiones declaradas</text><rect x="24" y="280" width="12" height="12" fill="#657654"/><text x="43" y="291" font-family="Arial,sans-serif" font-size="15" fill="#172342">Sin lesiones declaradas</text><rect x="24" y="302" width="12" height="12" fill="#785c34"/><text x="43" y="313" font-family="Arial,sans-serif" font-size="15" fill="#172342">Desconocidas</text></svg><figcaption>Datos de todos los modelos Tesla de este corte. Las lesiones pueden ser confirmadas o alegadas y afectar a cualquier implicado. Las reglas de notificación difieren entre grupos.</figcaption><details><summary>Consultar los datos en una tabla</summary><div class="cybercab-tabla" role="region" aria-label="Tabla alternativa al gráfico" tabindex="0"><table><caption>Casos Tesla de todos los modelos; no son tasas de riesgo</caption><thead><tr><th scope="col">Funcionamiento</th><th scope="col">Lesiones declaradas</th><th scope="col">Sin lesiones declaradas</th><th scope="col">Desconocidas</th><th scope="col">Total</th></tr></thead><tbody><tr><th scope="row">Autónomo</th><td>3</td><td>40</td><td>0</td><td>43</td></tr><tr><th scope="row">Asistencia</th><td>61</td><td>27</td><td>2319</td><td>2407</td></tr></tbody></table></div></details></figure>

Además, las reglas para notificar accidentes no son iguales entre ambos sistemas. Y faltan kilómetros recorridos en condiciones comparables. Saber cuántos choques hay sin saber cuánto se conduce se parece a contar paraguas rotos sin preguntar cuánto llueve.

La respuesta, por tanto, sigue abierta. Los registros muestran circunstancias distintas, compatibles con nuestra sospecha, pero **no permiten separar cuánto depende de conducir bien y cuánto de las dificultades del recorrido**. Los accidentes leves no bastan para aprobar al taxi de Tesla. Estos datos tampoco bastan para suspenderlo.


## Fuentes y datos

- [Registros originales y limitaciones de la NHTSA](https://www.nhtsa.gov/laws-regulations/standing-general-order-crash-reporting).
- [Diccionario oficial de los campos](https://static.nhtsa.gov/odi/ffdd/sgo-2021-01/SGO-2021-01_Data_Element_Definitions.pdf).
- [Metodología del informe de seguridad de Tesla](https://www.tesla.com/robotaxi/safety). Tiene una selección distinta; sus kilómetros no se utilizan para calcular tasas con estos incidentes.
- [Noticia de Electrek que motivó la pregunta](https://electrek.co/2026/11/16/tesla-cybercab-crashes-speed-problem/).
- [Descargar notebook reproducible](/nebula/analisis/cybercab-seguridad/analisis_cybercab_seguridad.ipynb) · [Leer cuaderno ejecutado](/nebula/analisis/cybercab-seguridad/analisis_cybercab_seguridad.html).
- [Los ocho casos del Cybercab en CSV](/nebula/analisis/cybercab-seguridad/resultados/cybercab_ocho_casos.csv) · [Resultados y auditoría](/nebula/analisis/cybercab-seguridad/resultados/resultados.json).
