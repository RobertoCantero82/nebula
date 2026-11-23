---
titulo: "¿Y si James Bond fuese un pésimo espía?"
descripcion: "Salvar el mundo no siempre significa controlar la situación. El historial de 007 deja una contradicción que sus victorias suelen ocultar."
tema: "CINE"
fecha: 2026-11-17
imagenPortada: "/imagenes/james_bond_pesimo_espia_portada.png"
cifraDestacada: "23 de 25"
etiquetaCifra: "películas con captura documentada"
textoContinuo: "¿Y si James Bond fuese un pésimo espía? En sus 25 películas, se pone a prueba la imagen de un héroe que lo controla todo"
metodologia: "EDA documental de las 25 películas oficiales estrenadas entre 1962 y 2021. Codificación manual de presencia de capturas en sinopsis, con corroboraciones oficiales y especializadas; consulta: 17 de noviembre de 2026. No se ha realizado un visionado completo. Son mínimos documentados por película, no un censo de escenas, tasas de fracaso ni una evaluación profesional. Una sola codificación, sin validación independiente. Comparo criterios que apartan Skyfall o incorporan el encierro-trampa de Sin tiempo para morir."
---

**Si tu trabajo consiste en pasar desapercibido, presentarte con nombre y apellido parece un comienzo discutible.** James Bond lo hace con una seguridad envidiable. Después llegan los coches destrozados, las explosiones y las cenas con personas que quieren matarlo. Pero ¿qué ocurre si dejamos de mirar al héroe y empezamos a revisar su historial como agente secreto?

La pregunta tiene trampa. Un espía puede ser descubierto y aun así conseguir información valiosa. También puede acercarse deliberadamente al enemigo. Para poner a prueba la sospecha sin inventarme nada, he buscado algo más concreto: **en cuántas películas queda Bond bajo control de sus adversarios**.

<div style="position:relative;width:100%;aspect-ratio:16/9;margin:2rem 0;">
  <iframe
    src="https://www.youtube.com/embed/K3elJwmxsRA"
    title="Vídeo de James Bond"
    style="position:absolute;inset:0;width:100%;height:100%;border:0;border-radius:12px;"
    loading="lazy"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    referrerpolicy="strict-origin-when-cross-origin"
    allowfullscreen
  ></iframe>
</div>

El resultado sorprende: he documentado al menos una captura en **23 de las 25 películas oficiales estrenadas entre 1962 y 2021**. Es el 92 % de la serie. No significa que fracase en el 92 % de sus misiones. Significa que terminar en manos del enemigo es una situación extraordinariamente habitual en sus historias.

## Una celda casi en cada aventura

En *Agente 007 contra el Dr. No*, los guardias de la isla capturan a Bond y Honey Ryder. En *007: Alta tensión*, [Bond](https://diarionebula.es/actualidad/2026-11-17/robert-pattinson-nuevo-james-bond/) termina drogado y encarcelado en una base soviética. En *GoldenEye*, lo sedan y lo dejan retenido dentro de un helicóptero. Cambian las décadas y los protagonistas, pero el riesgo de perder la libertad permanece.

Para contar una captura exijo que la fuente describa una retención, un traslado forzado, un encierro o una reducción bajo control del adversario. Una pelea o una persecución no bastan. Tampoco cuento como enemigo a cualquier superior que le ordene volver a Londres.

No he vuelto a ver y cronometrar las 25 películas. Este EDA, también conocido como análisis exploratorio de datos, parte de sinopsis y contrasta episodios concretos con materiales oficiales. Cada registro conserva su explicación y su enlace. Por eso hablo de **mínimos documentados**, no de un recuento completo de escenas.

Antes de seguir, prueba a cambiar el criterio. Cada círculo representa una película, por ejemplo, el azul señala un caso incluido en el recuento. Puedes apartar *Skyfall*, añadir el encierro-trampa de *Sin tiempo para morir* y consultar la prueba de cada título. **El explorador contiene spoilers.**

<section class="bond-expediente" aria-labelledby="bond-titulo">
  <h3 id="bond-titulo">Abre el expediente de 007</h3>
  <p>Un círculo por película, en orden de estreno de izquierda a derecha y de arriba abajo. Azul: caso incluido. Contorno vacío: caso fuera del criterio o sin prueba; no significa ausencia.</p>
  <fieldset>
    <legend>Decide qué situaciones cuentas</legend>
    <label><input id="bond-skyfall" type="checkbox" checked> Incluir la captura de Skyfall, donde acepta acercarse al enemigo</label>
    <label><input id="bond-trampa" type="checkbox"> Añadir el encierro-trampa de Sin tiempo para morir</label>
  </fieldset>
  <div id="bond-resumen" role="status" aria-live="polite" aria-atomic="true"><strong>23 de 25 películas · 92 %</strong><span>Mínimo documentado con capturas; no es una tasa de fracaso.</span></div>
  <figure><svg id="bond-mapa" viewBox="0 0 200 200" role="img" aria-labelledby="bond-mapa-titulo bond-mapa-desc"><title id="bond-mapa-titulo">Capturas documentadas en 23 de 25 películas</title><desc id="bond-mapa-desc">Una cuadrícula cronológica de 25 círculos. Los primeros 21, Skyfall y Spectre aparecen en azul. Quantum of Solace queda sin prueba; Sin tiempo para morir es un encierro-trampa separado.</desc><circle cx="24" cy="24" r="12" fill="#446ddf" stroke="#1d3157" stroke-width="1.5"><title>Agente 007 contra el Dr. No: captura</title></circle><circle cx="62" cy="24" r="12" fill="#446ddf" stroke="#1d3157" stroke-width="1.5"><title>Desde Rusia con amor: captura</title></circle><circle cx="100" cy="24" r="12" fill="#446ddf" stroke="#1d3157" stroke-width="1.5"><title>James Bond contra Goldfinger: captura</title></circle><circle cx="138" cy="24" r="12" fill="#446ddf" stroke="#1d3157" stroke-width="1.5"><title>Operación Trueno: captura</title></circle><circle cx="176" cy="24" r="12" fill="#446ddf" stroke="#1d3157" stroke-width="1.5"><title>Sólo se vive dos veces: captura</title></circle><circle cx="24" cy="62" r="12" fill="#446ddf" stroke="#1d3157" stroke-width="1.5"><title>007 al servicio secreto de su Majestad: captura</title></circle><circle cx="62" cy="62" r="12" fill="#446ddf" stroke="#1d3157" stroke-width="1.5"><title>Diamantes para la eternidad: captura</title></circle><circle cx="100" cy="62" r="12" fill="#446ddf" stroke="#1d3157" stroke-width="1.5"><title>Vive y deja morir: captura</title></circle><circle cx="138" cy="62" r="12" fill="#446ddf" stroke="#1d3157" stroke-width="1.5"><title>El hombre de la pistola de oro: captura</title></circle><circle cx="176" cy="62" r="12" fill="#446ddf" stroke="#1d3157" stroke-width="1.5"><title>La espía que me amó: captura</title></circle><circle cx="24" cy="100" r="12" fill="#446ddf" stroke="#1d3157" stroke-width="1.5"><title>Moonraker: captura</title></circle><circle cx="62" cy="100" r="12" fill="#446ddf" stroke="#1d3157" stroke-width="1.5"><title>Sólo para sus ojos: captura</title></circle><circle cx="100" cy="100" r="12" fill="#446ddf" stroke="#1d3157" stroke-width="1.5"><title>Octopussy: captura</title></circle><circle cx="138" cy="100" r="12" fill="#446ddf" stroke="#1d3157" stroke-width="1.5"><title>Panorama para matar: captura</title></circle><circle cx="176" cy="100" r="12" fill="#446ddf" stroke="#1d3157" stroke-width="1.5"><title>007: Alta tensión: captura</title></circle><circle cx="24" cy="138" r="12" fill="#446ddf" stroke="#1d3157" stroke-width="1.5"><title>Licencia para matar: captura</title></circle><circle cx="62" cy="138" r="12" fill="#446ddf" stroke="#1d3157" stroke-width="1.5"><title>GoldenEye: captura</title></circle><circle cx="100" cy="138" r="12" fill="#446ddf" stroke="#1d3157" stroke-width="1.5"><title>El mañana nunca muere: captura</title></circle><circle cx="138" cy="138" r="12" fill="#446ddf" stroke="#1d3157" stroke-width="1.5"><title>El mundo nunca es suficiente: captura</title></circle><circle cx="176" cy="138" r="12" fill="#446ddf" stroke="#1d3157" stroke-width="1.5"><title>Muere otro día: captura</title></circle><circle cx="24" cy="176" r="12" fill="#446ddf" stroke="#1d3157" stroke-width="1.5"><title>Casino Royale: captura</title></circle><circle cx="62" cy="176" r="12" fill="#faf8f2" stroke="#1d3157" stroke-width="1.5"><title>Quantum of Solace: no_documentada</title></circle><circle cx="100" cy="176" r="12" fill="#446ddf" stroke="#1d3157" stroke-width="1.5"><title>Skyfall: captura</title></circle><circle cx="138" cy="176" r="12" fill="#446ddf" stroke="#1d3157" stroke-width="1.5"><title>Spectre: captura</title></circle><circle cx="176" cy="176" r="12" fill="#faf8f2" stroke="#1d3157" stroke-width="1.5"><title>Sin tiempo para morir: encierro_trampa</title></circle></svg></figure>
  <label for="bond-pelicula">Consulta una película y su prueba documental</label>
  <select id="bond-pelicula"><option value="bond_01">Agente 007 contra el Dr. No (1962)</option><option value="bond_02">Desde Rusia con amor (1963)</option><option value="bond_03">James Bond contra Goldfinger (1964)</option><option value="bond_04">Operación Trueno (1965)</option><option value="bond_05">Sólo se vive dos veces (1967)</option><option value="bond_06">007 al servicio secreto de su Majestad (1969)</option><option value="bond_07">Diamantes para la eternidad (1971)</option><option value="bond_08">Vive y deja morir (1973)</option><option value="bond_09">El hombre de la pistola de oro (1974)</option><option value="bond_10">La espía que me amó (1977)</option><option value="bond_11">Moonraker (1979)</option><option value="bond_12">Sólo para sus ojos (1981)</option><option value="bond_13">Octopussy (1983)</option><option value="bond_14">Panorama para matar (1985)</option><option value="bond_15">007: Alta tensión (1987)</option><option value="bond_16">Licencia para matar (1989)</option><option value="bond_17">GoldenEye (1995)</option><option value="bond_18">El mañana nunca muere (1997)</option><option value="bond_19">El mundo nunca es suficiente (1999)</option><option value="bond_20">Muere otro día (2002)</option><option value="bond_21">Casino Royale (2006)</option><option value="bond_22">Quantum of Solace (2008)</option><option value="bond_23">Skyfall (2012)</option><option value="bond_24">Spectre (2015)</option><option value="bond_25">Sin tiempo para morir (2021)</option></select>
  <div id="bond-detalle" aria-live="polite" aria-atomic="true"><h4>Agente 007 contra el Dr. No (1962)</h4><p>Captura documentada. Los guardias de Crab Key capturan a Bond y Honey; después Bond queda encerrado y escapa por un conducto.</p><p><a href="https://en.wikipedia.org/wiki/Dr._No_(film)">Consultar fuente de esta película</a></p></div>
  <noscript><p>Los controles necesitan JavaScript. El gráfico y el recuento inicial muestran 23 películas; la tabla siguiente permite consultar todas las pruebas sin JavaScript.</p></noscript>
  <details><summary>Ver las 25 películas, los casos y las fuentes</summary><div class="bond-tabla-scroll" tabindex="0" role="region" aria-label="Tabla de 25 películas desplazable horizontalmente"><table><caption>Registro documental: una fila por película, no un censo de todas las escenas</caption><thead><tr><th scope="col">Película</th><th scope="col">Clasificación</th><th scope="col">Prueba parafraseada y fuente</th></tr></thead><tbody><tr><th scope="row">Agente 007 contra el Dr. No (1962)</th><td>Captura documentada</td><td>Los guardias de Crab Key capturan a Bond y Honey; después Bond queda encerrado y escapa por un conducto. <a href="https://en.wikipedia.org/wiki/Dr._No_(film)">Fuente de Agente 007 contra el Dr. No</a></td></tr><tr><th scope="row">Desde Rusia con amor (1963)</th><td>Captura documentada</td><td>Grant suplanta a Nash, reduce a Bond y lo mantiene bajo amenaza de muerte en el tren. Bond revierte la situación con el maletín. <a href="https://en.wikipedia.org/wiki/From_Russia_with_Love_(film)">Fuente de Desde Rusia con amor</a></td></tr><tr><th scope="row">James Bond contra Goldfinger (1964)</th><td>Captura documentada</td><td>Tras saltar la alarma de la refinería, Bond queda cautivo ante un láser. Lo trasladan sedado a Kentucky. <a href="https://en.wikipedia.org/wiki/Goldfinger_(film)">Fuente de James Bond contra Goldfinger</a></td></tr><tr><th scope="row">Operación Trueno (1965)</th><td>Captura documentada</td><td>Fiona Volpe y los hombres de Largo retienen a Bond a punta de pistola y lo trasladan en coche; escapa durante el desfile. <a href="https://en.wikipedia.org/wiki/Thunderball_(film)">Fuente de Operación Trueno</a></td></tr><tr><th scope="row">Sólo se vive dos veces (1967)</th><td>Captura documentada</td><td>Bond es capturado en el carguero Ning-Po y despierta en el camarote de Helga Brandt. <a href="https://en.wikipedia.org/wiki/You_Only_Live_Twice_(film)">Fuente de Sólo se vive dos veces</a></td></tr><tr><th scope="row">007 al servicio secreto de su Majestad (1969)</th><td>Captura documentada</td><td>Blofeld descubre la suplantación de Hilary Bray y ordena encarcelar a Bond en Piz Gloria. <a href="https://en.wikipedia.org/wiki/On_Her_Majesty%27s_Secret_Service_(film)">Fuente de 007 al servicio secreto de su Majestad</a></td></tr><tr><th scope="row">Diamantes para la eternidad (1971)</th><td>Captura documentada</td><td>Blofeld incapacita a Bond con gas; Wint y Kidd lo trasladan y abandonan dentro de una tubería. <a href="https://en.wikipedia.org/wiki/Diamonds_Are_Forever_(film)">Fuente de Diamantes para la eternidad</a></td></tr><tr><th scope="row">Vive y deja morir (1973)</th><td>Captura documentada</td><td>Kananga captura a Bond y Solitaire y los ata a una plataforma que desciende hacia los tiburones. <a href="https://en.wikipedia.org/wiki/Live_and_Let_Die_(film)">Fuente de Vive y deja morir</a></td></tr><tr><th scope="row">El hombre de la pistola de oro (1974)</th><td>Captura documentada</td><td>La suplantación de Scaramanga fracasa en la residencia de Hai Fat. Bond es capturado y llevado a la academia de artes marciales. <a href="https://en.wikipedia.org/wiki/The_Man_with_the_Golden_Gun_(film)">Fuente de El hombre de la pistola de oro</a></td></tr><tr><th scope="row">La espía que me amó (1977)</th><td>Captura documentada</td><td>La tripulación del Liparus captura el submarino donde viajan Bond y Anya. Bond se libra de sus guardias y libera a los marineros. <a href="https://en.wikipedia.org/wiki/The_Spy_Who_Loved_Me_(film)">Fuente de La espía que me amó</a></td></tr><tr><th scope="row">Moonraker (1979)</th><td>Captura documentada</td><td>Jaws captura a Bond en la Amazonia. Drax encierra a Bond y Goodhead bajo la plataforma de lanzamiento. <a href="https://en.wikipedia.org/wiki/Moonraker_(film)">Fuente de Moonraker</a></td></tr><tr><th scope="row">Sólo para sus ojos (1981)</th><td>Captura documentada</td><td>Los hombres de Gonzales capturan a Bond cuando espía la villa; logra escapar cuando Melina mata a Gonzales. <a href="https://en.wikipedia.org/wiki/For_Your_Eyes_Only_(film)">Fuente de Sólo para sus ojos</a></td></tr><tr><th scope="row">Octopussy (1983)</th><td>Captura documentada</td><td>Gobinda deja inconsciente a Bond y lo lleva al palacio de Kamal Khan, de donde escapa. <a href="https://en.wikipedia.org/wiki/Octopussy">Fuente de Octopussy</a></td></tr><tr><th scope="row">Panorama para matar (1985)</th><td>Captura documentada</td><td>Zorin retiene a Bond y lo introduce en el Rolls-Royce junto al cadáver de Tibbett. May Day empuja el coche al lago. <a href="https://en.wikipedia.org/wiki/A_View_to_a_Kill">Fuente de Panorama para matar</a></td></tr><tr><th scope="row">007: Alta tensión (1987)</th><td>Captura documentada</td><td>Tras ser drogado, Bond es trasladado con Kara a una base soviética en Afganistán y ambos son encarcelados. <a href="https://en.wikipedia.org/wiki/The_Living_Daylights">Fuente de 007: Alta tensión</a></td></tr><tr><th scope="row">Licencia para matar (1989)</th><td>Captura documentada</td><td>Dario reconoce a Bond en la planta de cocaína. Bond es capturado y colocado en la cinta que conduce a una trituradora. <a href="https://en.wikipedia.org/wiki/Licence_to_Kill">Fuente de Licencia para matar</a></td></tr><tr><th scope="row">GoldenEye (1995)</th><td>Captura documentada</td><td>Bond es sedado con un dardo y despierta retenido junto a Natalya dentro del helicóptero Tiger. <a href="https://en.wikipedia.org/wiki/GoldenEye">Fuente de GoldenEye</a></td></tr><tr><th scope="row">El mañana nunca muere (1997)</th><td>Captura documentada</td><td>Stamper captura a Bond y Wai Lin tras salir del barco hundido; ambos son conducidos a la torre de Carver. <a href="https://en.wikipedia.org/wiki/Tomorrow_Never_Dies">Fuente de El mañana nunca muere</a></td></tr><tr><th scope="row">El mundo nunca es suficiente (1999)</th><td>Captura documentada</td><td>Los hombres de Elektra capturan a Bond. Ella lo inmoviliza y tortura con un garrote en la Torre de la Doncella. <a href="https://en.wikipedia.org/wiki/The_World_Is_Not_Enough">Fuente de El mundo nunca es suficiente</a></td></tr><tr><th scope="row">Muere otro día (2002)</th><td>Captura documentada</td><td>Los soldados norcoreanos capturan a Bond; tras catorce meses de cautiverio lo liberan mediante un intercambio de prisioneros. <a href="https://en.wikipedia.org/wiki/Die_Another_Day">Fuente de Muere otro día</a></td></tr><tr><th scope="row">Casino Royale (2006)</th><td>Captura documentada</td><td>Le Chiffre captura y tortura a Bond para obtener la contraseña del dinero del torneo. La irrupción de Mr. White evita su ejecución. <a href="https://en.wikipedia.org/wiki/Casino_Royale_(2006_film)">Fuente de Casino Royale</a></td></tr><tr><th scope="row">Quantum of Solace (2008)</th><td>Sin prueba registrada</td><td>No he identificado en las fuentes consultadas una captura enemiga equiparable. Las órdenes de sus superiores y los intentos de detenerlo no acreditan por sí solos ese episodio. <a href="https://en.wikipedia.org/wiki/Quantum_of_Solace">Fuente de Quantum of Solace</a></td></tr><tr><th scope="row">Skyfall (2012)</th><td>Captura documentada</td><td>Bond viaja voluntariamente con Sévérine para conocer a su empleador. La tripulación los captura y los entrega a Silva; después llegan refuerzos llamados por Bond. <a href="https://en.wikipedia.org/wiki/Skyfall">Fuente de Skyfall</a></td></tr><tr><th scope="row">Spectre (2015)</th><td>Captura documentada</td><td>En Londres, los agentes de Spectre secuestran por separado a Bond y Madeleine y trasladan a Bond al antiguo edificio del servicio secreto. <a href="https://en.wikipedia.org/wiki/Spectre_(2015_film)">Fuente de Spectre</a></td></tr><tr><th scope="row">Sin tiempo para morir (2021)</th><td>Encierro-trampa</td><td>Ash dispara a Leiter, encierra a Bond con él bajo cubierta y activa explosivos para hundir el barco. <a href="https://en.wikipedia.org/wiki/No_Time_to_Die">Fuente de Sin tiempo para morir</a></td></tr></tbody></table></div></details>
</section>


## No todas las trampas son iguales

*Skyfall* obliga a introducir un matiz. Bond acepta viajar con Sévérine para conocer a su empleador y termina capturado por los hombres de Silva. Acercarse voluntariamente al peligro no demuestra que quisiera ser detenido, pero tampoco permite tratar el episodio como un descuido cualquiera.

Si aparto ese caso, todavía documento capturas en **22 de 25 películas**, es decir, el **88 %**. El resultado apenas cambia: el cautiverio sigue apareciendo en casi toda la saga. Esta comprobación permite ver cuánto pesa una decisión discutible sin esconderla detrás de una cifra.

Hay otra frontera en *Sin tiempo para morir*. Ash encierra a Bond y a Leiter bajo la de un barco y busca hundirlo. Lo separo como encierro-trampa porque no mantiene después una custodia sobre ellos. Si lo incorporamos al criterio principal, el mínimo sube a **24 películas**.

*Quantum of Solace* queda sin una captura enemiga acreditada en mi registro. Eso no la convierte automáticamente en una misión impecable. Que una sinopsis no documente algo tampoco demuestra que no suceda.

<figure class="bond-criterios">
  <h3>¿Cambia mucho si cambiamos las reglas?</h3>
  <p>Películas con al menos un caso documentado, sobre las 25 analizadas.</p>

  <div class="bond-criterios-fila">
    <div class="bond-criterios-etiqueta">
      <strong>Sin Skyfall</strong>
      <span>22 de 25 · 88 %</span>
    </div>
    <div class="bond-criterios-pista" aria-hidden="true">
      <div style="width:88%"></div>
    </div>
    <p>Excluyo el caso en el que Bond acepta acercarse al enemigo.</p>
  </div>

  <div class="bond-criterios-fila">
    <div class="bond-criterios-etiqueta">
      <strong>Criterio principal</strong>
      <span>23 de 25 · 92 %</span>
    </div>
    <div class="bond-criterios-pista" aria-hidden="true">
      <div style="width:92%"></div>
    </div>
    <p>Incluyo Skyfall y mantengo separado el encierro-trampa.</p>
  </div>

  <div class="bond-criterios-fila">
    <div class="bond-criterios-etiqueta">
      <strong>Con el encierro-trampa</strong>
      <span>24 de 25 · 96 %</span>
    </div>
    <div class="bond-criterios-pista" aria-hidden="true">
      <div style="width:96%"></div>
    </div>
    <p>Añado el encierro de Sin tiempo para morir al criterio principal.</p>
  </div>

  <figcaption>
    Incluso con el criterio más restrictivo, documento casos en 22 películas.
    Son mínimos documentados, no tasas de fracaso.
    La falta de una captura registrada no demuestra su ausencia.
    Fuente: registro documental del análisis.
  </figcaption>
</figure>

<style>
  .bond-criterios {
    box-sizing: border-box;
    margin: 2rem 0;
    padding: clamp(18px, 4vw, 32px);
    background: #faf8f2;
    color: #1d3157;
    border: 1px solid #aab5ce;
    border-radius: 16px;
  }

  .bond-criterios h3 {
    margin: 0 0 12px;
    font-size: clamp(1.2rem, 4vw, 1.6rem);
    line-height: 1.3;
  }

  .bond-criterios > p {
    margin: 0 0 24px;
    line-height: 1.6;
  }

  .bond-criterios-fila {
    margin: 0 0 24px;
  }

  .bond-criterios-etiqueta {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    gap: 6px 16px;
    margin-bottom: 8px;
    line-height: 1.5;
  }

  .bond-criterios-etiqueta span {
    font-weight: 700;
    font-variant-numeric: tabular-nums;
  }

  .bond-criterios-pista {
    height: 20px;
    overflow: hidden;
    background: #e1e5ef;
    border-radius: 4px;
  }

  .bond-criterios-pista > div {
    height: 100%;
    background: #446ddf;
    border-radius: 4px;
  }

  .bond-criterios-fila > p {
    margin: 8px 0 0;
    font-size: .9rem;
    line-height: 1.5;
  }

  .bond-criterios figcaption {
    padding-top: 16px;
    border-top: 1px solid #aab5ce;
    font-size: .85rem;
    line-height: 1.6;
  }
</style>

## El hombre que también necesita ayuda

**Perder la libertad y salir de ella son cuestiones diferentes**. Bond puede quedar atrapado y después escapar con ingenio. En *Goldfinger*, por ejemplo, consigue que su captor interrumpa la ejecución con el láser al convencerlo de que matarlo perjudicaría sus planes.

Otras veces interviene alguien más. Tatiana dispara a Rosa Klebb en *Desde Rusia con amor*. Domino detiene a Largo cuando está a punto de matar a Bond en *Operación Trueno*. En *El mundo nunca es suficiente*, Zukovsky utiliza su arma oculta para liberarlo. Son ejemplos documentados, no una estadística completa de rescates.

<figure class="bond-balance">
  <h3>El expediente de 007, en 25 películas</h3>

  <div class="bond-balance-barra" aria-hidden="true">
    <span class="bond-balance-capturas"></span>
    <span class="bond-balance-trampa"></span>
    <span class="bond-balance-sin-prueba"></span>
  </div>

  <ul class="bond-balance-leyenda">
    <li>
      <span class="bond-balance-muestra bond-balance-capturas" aria-hidden="true"></span>
      <span><strong>23</strong> con captura documentada</span>
    </li>
    <li>
      <span class="bond-balance-muestra bond-balance-trampa" aria-hidden="true"></span>
      <span><strong>1</strong> encierro-trampa, separado del recuento principal</span>
    </li>
    <li>
      <span class="bond-balance-muestra bond-balance-sin-prueba" aria-hidden="true"></span>
      <span><strong>1</strong> sin captura acreditada en el registro</span>
    </li>
  </ul>

  <figcaption>
    El registro documenta cautiverios, no incompetencia.
    No mide el éxito de las misiones ni permite comparar a Bond con agentes
    reales. La falta de una captura acreditada tampoco demuestra su ausencia.
    Fuente: registro documental del análisis.
  </figcaption>
</figure>

<style>
  .bond-balance {
    box-sizing: border-box;
    margin: 2rem 0;
    padding: clamp(18px, 4vw, 32px);
    background: #faf8f2;
    color: #1d3157;
    border: 1px solid #aab5ce;
    border-radius: 16px;
  }

  .bond-balance h3 {
    margin: 0 0 24px;
    font-size: clamp(1.2rem, 4vw, 1.6rem);
    line-height: 1.35;
  }

  .bond-balance-barra {
    display: flex;
    height: 40px;
    gap: 3px;
    margin-bottom: 22px;
  }

  .bond-balance-barra > span {
    min-width: 0;
    border-radius: 3px;
  }

  .bond-balance-barra > .bond-balance-capturas {
    flex: 23;
  }

  .bond-balance-barra > .bond-balance-trampa,
  .bond-balance-barra > .bond-balance-sin-prueba {
    flex: 1;
  }

  .bond-balance-capturas {
    background: #446ddf;
  }

  .bond-balance-trampa {
    background: repeating-linear-gradient(
      135deg,
      #1d3157 0,
      #1d3157 3px,
      #faf8f2 3px,
      #faf8f2 7px
    );
  }

  .bond-balance-sin-prueba {
    background: #faf8f2;
    box-shadow: inset 0 0 0 2px #697a9a;
  }

  .bond-balance-leyenda {
    display: grid;
    gap: 12px;
    margin: 0 0 24px;
    padding: 0;
    list-style: none;
  }

  .bond-balance-leyenda li {
    display: flex;
    align-items: flex-start;
    gap: 10px;
    line-height: 1.5;
  }

  .bond-balance-muestra {
    flex: 0 0 18px;
    height: 18px;
    margin-top: 3px;
    border-radius: 3px;
  }

  .bond-balance figcaption {
    padding-top: 16px;
    border-top: 1px solid #aab5ce;
    font-size: .9rem;
    line-height: 1.65;
  }
</style>

*Casino Royale* lleva esa dependencia al primer plano: Vesper evita que Bond muera envenenado y Mr. White interrumpe su tortura al matar a Le Chiffre. Que alguien lo salve no implica que actúe por bondad. Tampoco borra lo que Bond consigue por sus propios medios.

Así que el expediente no permite despedir a 007. **He encontrado un patrón de cautiverio, no una prueba de incompetencia.** Para evaluar lo segundo harían falta los objetivos, las alternativas y las consecuencias de cada decisión. Lo interesante es la contradicción que dejan estas historias: recordamos a un agente que controla la situación, aunque una y otra vez tenga que recuperarla.
## Fuentes y cómo comprobarlo

Las pruebas de las 25 películas y sus enlaces figuran en el explorador y en el [registro documental](/analisis/james-bond-pesimo-espia/data/raw/peliculas_codificadas.csv). Son sinopsis secundarias de Wikipedia en inglés, complementadas con los materiales identificados en el [archivo de corroboraciones y ejemplos](/analisis/james-bond-pesimo-espia/data/raw/corroboraciones_y_ejemplos.csv). Algunos textos oficiales sólo estuvieron disponibles en los resultados de búsqueda, circunstancia que queda indicada en ese archivo.

Puedes descargar el [cuaderno de preparación](/analisis/james-bond-pesimo-espia/01_preparacion_datos.ipynb), el [notebook del EDA ejecutado](/analisis/james-bond-pesimo-espia/02_eda.ipynb), la [tabla preparada](/analisis/james-bond-pesimo-espia/data/processed/peliculas_analisis.csv) y el [libro de códigos y limitaciones](/analisis/james-bond-pesimo-espia/LIBRO_DE_CODIGOS.md). La falta de un caso registrado no acredita su ausencia. El análisis no evalúa agentes reales ni demuestra que Bond sea incompetente.

<script type="application/json" id="bond-datos">[{"id": "bond_01", "anio": "1962", "titulo_original": "Dr. No", "titulo_es": "Agente 007 contra el Dr. No", "actor": "Sean Connery", "tipo": "captura", "acceso_voluntario": "no", "evidencia": "Los guardias de Crab Key capturan a Bond y Honey; después Bond queda encerrado y escapa por un conducto.", "localizador": "Plot: llegada a Crab Key y cautiverio en la base.", "fuente_url": "https://en.wikipedia.org/wiki/Dr._No_(film)", "consulta": "2026-11-17", "metodo": "codificacion_manual_de_fuentes_documentales_sin_visionado", "captura_documentada": "1", "criterio_conservador": "1", "criterio_ampliado": "1"}, {"id": "bond_02", "anio": "1963", "titulo_original": "From Russia with Love", "titulo_es": "Desde Rusia con amor", "actor": "Sean Connery", "tipo": "captura", "acceso_voluntario": "no", "evidencia": "Grant suplanta a Nash, reduce a Bond y lo mantiene bajo amenaza de muerte en el tren. Bond revierte la situación con el maletín.", "localizador": "Plot: Grant sustituye a Nash en el Orient Express.", "fuente_url": "https://en.wikipedia.org/wiki/From_Russia_with_Love_(film)", "consulta": "2026-11-17", "metodo": "codificacion_manual_de_fuentes_documentales_sin_visionado", "captura_documentada": "1", "criterio_conservador": "1", "criterio_ampliado": "1"}, {"id": "bond_03", "anio": "1964", "titulo_original": "Goldfinger", "titulo_es": "James Bond contra Goldfinger", "actor": "Sean Connery", "tipo": "captura", "acceso_voluntario": "no", "evidencia": "Tras saltar la alarma de la refinería, Bond queda cautivo ante un láser. Lo trasladan sedado a Kentucky.", "localizador": "Plot: refinería suiza y traslado a la granja.", "fuente_url": "https://en.wikipedia.org/wiki/Goldfinger_(film)", "consulta": "2026-11-17", "metodo": "codificacion_manual_de_fuentes_documentales_sin_visionado", "captura_documentada": "1", "criterio_conservador": "1", "criterio_ampliado": "1"}, {"id": "bond_04", "anio": "1965", "titulo_original": "Thunderball", "titulo_es": "Operación Trueno", "actor": "Sean Connery", "tipo": "captura", "acceso_voluntario": "no", "evidencia": "Fiona Volpe y los hombres de Largo retienen a Bond a punta de pistola y lo trasladan en coche; escapa durante el desfile.", "localizador": "La sinopsis abrevia este episodio: corroboración oficial sobre Fiona Volpe.", "fuente_url": "https://en.wikipedia.org/wiki/Thunderball_(film)", "consulta": "2026-11-17", "metodo": "codificacion_manual_de_fuentes_documentales_sin_visionado", "captura_documentada": "1", "criterio_conservador": "1", "criterio_ampliado": "1"}, {"id": "bond_05", "anio": "1967", "titulo_original": "You Only Live Twice", "titulo_es": "Sólo se vive dos veces", "actor": "Sean Connery", "tipo": "captura", "acceso_voluntario": "no", "evidencia": "Bond es capturado en el carguero Ning-Po y despierta en el camarote de Helga Brandt.", "localizador": "Plot: investigación del Ning-Po.", "fuente_url": "https://en.wikipedia.org/wiki/You_Only_Live_Twice_(film)", "consulta": "2026-11-17", "metodo": "codificacion_manual_de_fuentes_documentales_sin_visionado", "captura_documentada": "1", "criterio_conservador": "1", "criterio_ampliado": "1"}, {"id": "bond_06", "anio": "1969", "titulo_original": "On Her Majesty’s Secret Service", "titulo_es": "007 al servicio secreto de su Majestad", "actor": "George Lazenby", "tipo": "captura", "acceso_voluntario": "no", "evidencia": "Blofeld descubre la suplantación de Hilary Bray y ordena encarcelar a Bond en Piz Gloria.", "localizador": "Plot: descubrimiento de la identidad en el instituto.", "fuente_url": "https://en.wikipedia.org/wiki/On_Her_Majesty%27s_Secret_Service_(film)", "consulta": "2026-11-17", "metodo": "codificacion_manual_de_fuentes_documentales_sin_visionado", "captura_documentada": "1", "criterio_conservador": "1", "criterio_ampliado": "1"}, {"id": "bond_07", "anio": "1971", "titulo_original": "Diamonds Are Forever", "titulo_es": "Diamantes para la eternidad", "actor": "Sean Connery", "tipo": "captura", "acceso_voluntario": "no", "evidencia": "Blofeld incapacita a Bond con gas; Wint y Kidd lo trasladan y abandonan dentro de una tubería.", "localizador": "Plot: encuentro en la planta superior del Whyte House.", "fuente_url": "https://en.wikipedia.org/wiki/Diamonds_Are_Forever_(film)", "consulta": "2026-11-17", "metodo": "codificacion_manual_de_fuentes_documentales_sin_visionado", "captura_documentada": "1", "criterio_conservador": "1", "criterio_ampliado": "1"}, {"id": "bond_08", "anio": "1973", "titulo_original": "Live and Let Die", "titulo_es": "Vive y deja morir", "actor": "Roger Moore", "tipo": "captura", "acceso_voluntario": "no", "evidencia": "Kananga captura a Bond y Solitaire y los ata a una plataforma que desciende hacia los tiburones.", "localizador": "Plot: desenlace en la guarida de Kananga.", "fuente_url": "https://en.wikipedia.org/wiki/Live_and_Let_Die_(film)", "consulta": "2026-11-17", "metodo": "codificacion_manual_de_fuentes_documentales_sin_visionado", "captura_documentada": "1", "criterio_conservador": "1", "criterio_ampliado": "1"}, {"id": "bond_09", "anio": "1974", "titulo_original": "The Man with the Golden Gun", "titulo_es": "El hombre de la pistola de oro", "actor": "Roger Moore", "tipo": "captura", "acceso_voluntario": "no", "evidencia": "La suplantación de Scaramanga fracasa en la residencia de Hai Fat. Bond es capturado y llevado a la academia de artes marciales.", "localizador": "Plot: residencia de Hai Fat y academia.", "fuente_url": "https://en.wikipedia.org/wiki/The_Man_with_the_Golden_Gun_(film)", "consulta": "2026-11-17", "metodo": "codificacion_manual_de_fuentes_documentales_sin_visionado", "captura_documentada": "1", "criterio_conservador": "1", "criterio_ampliado": "1"}, {"id": "bond_10", "anio": "1977", "titulo_original": "The Spy Who Loved Me", "titulo_es": "La espía que me amó", "actor": "Roger Moore", "tipo": "captura", "acceso_voluntario": "no", "evidencia": "La tripulación del Liparus captura el submarino donde viajan Bond y Anya. Bond se libra de sus guardias y libera a los marineros.", "localizador": "Plot: captura del USS Wayne. Corroboración adicional en Forbes y James Bond Wiki.", "fuente_url": "https://en.wikipedia.org/wiki/The_Spy_Who_Loved_Me_(film)", "consulta": "2026-11-17", "metodo": "codificacion_manual_de_fuentes_documentales_sin_visionado", "captura_documentada": "1", "criterio_conservador": "1", "criterio_ampliado": "1"}, {"id": "bond_11", "anio": "1979", "titulo_original": "Moonraker", "titulo_es": "Moonraker", "actor": "Roger Moore", "tipo": "captura", "acceso_voluntario": "no", "evidencia": "Jaws captura a Bond en la Amazonia. Drax encierra a Bond y Goodhead bajo la plataforma de lanzamiento.", "localizador": "Plot: base de Drax en la Amazonia.", "fuente_url": "https://en.wikipedia.org/wiki/Moonraker_(film)", "consulta": "2026-11-17", "metodo": "codificacion_manual_de_fuentes_documentales_sin_visionado", "captura_documentada": "1", "criterio_conservador": "1", "criterio_ampliado": "1"}, {"id": "bond_12", "anio": "1981", "titulo_original": "For Your Eyes Only", "titulo_es": "Sólo para sus ojos", "actor": "Roger Moore", "tipo": "captura", "acceso_voluntario": "no", "evidencia": "Los hombres de Gonzales capturan a Bond cuando espía la villa; logra escapar cuando Melina mata a Gonzales.", "localizador": "Plot: investigación en la villa española. No cuento la posterior custodia de Columbo como captura enemiga.", "fuente_url": "https://en.wikipedia.org/wiki/For_Your_Eyes_Only_(film)", "consulta": "2026-11-17", "metodo": "codificacion_manual_de_fuentes_documentales_sin_visionado", "captura_documentada": "1", "criterio_conservador": "1", "criterio_ampliado": "1"}, {"id": "bond_13", "anio": "1983", "titulo_original": "Octopussy", "titulo_es": "Octopussy", "actor": "Roger Moore", "tipo": "captura", "acceso_voluntario": "no", "evidencia": "Gobinda deja inconsciente a Bond y lo lleva al palacio de Kamal Khan, de donde escapa.", "localizador": "Plot: robo del huevo con localizador y traslado al palacio.", "fuente_url": "https://en.wikipedia.org/wiki/Octopussy", "consulta": "2026-11-17", "metodo": "codificacion_manual_de_fuentes_documentales_sin_visionado", "captura_documentada": "1", "criterio_conservador": "1", "criterio_ampliado": "1"}, {"id": "bond_14", "anio": "1985", "titulo_original": "A View to a Kill", "titulo_es": "Panorama para matar", "actor": "Roger Moore", "tipo": "captura", "acceso_voluntario": "no", "evidencia": "Zorin retiene a Bond y lo introduce en el Rolls-Royce junto al cadáver de Tibbett. May Day empuja el coche al lago.", "localizador": "La sinopsis de Wikipedia abrevia el episodio: corroboración en la descripción oficial y MI6-HQ.", "fuente_url": "https://en.wikipedia.org/wiki/A_View_to_a_Kill", "consulta": "2026-11-17", "metodo": "codificacion_manual_de_fuentes_documentales_sin_visionado", "captura_documentada": "1", "criterio_conservador": "1", "criterio_ampliado": "1"}, {"id": "bond_15", "anio": "1987", "titulo_original": "The Living Daylights", "titulo_es": "007: Alta tensión", "actor": "Timothy Dalton", "tipo": "captura", "acceso_voluntario": "no", "evidencia": "Tras ser drogado, Bond es trasladado con Kara a una base soviética en Afganistán y ambos son encarcelados.", "localizador": "Plot: captura, vuelo a Afganistán y prisión.", "fuente_url": "https://en.wikipedia.org/wiki/The_Living_Daylights", "consulta": "2026-11-17", "metodo": "codificacion_manual_de_fuentes_documentales_sin_visionado", "captura_documentada": "1", "criterio_conservador": "1", "criterio_ampliado": "1"}, {"id": "bond_16", "anio": "1989", "titulo_original": "Licence to Kill", "titulo_es": "Licencia para matar", "actor": "Timothy Dalton", "tipo": "captura", "acceso_voluntario": "no", "evidencia": "Dario reconoce a Bond en la planta de cocaína. Bond es capturado y colocado en la cinta que conduce a una trituradora.", "localizador": "Plot: visita a la planta y reconocimiento por Dario.", "fuente_url": "https://en.wikipedia.org/wiki/Licence_to_Kill", "consulta": "2026-11-17", "metodo": "codificacion_manual_de_fuentes_documentales_sin_visionado", "captura_documentada": "1", "criterio_conservador": "1", "criterio_ampliado": "1"}, {"id": "bond_17", "anio": "1995", "titulo_original": "GoldenEye", "titulo_es": "GoldenEye", "actor": "Pierce Brosnan", "tipo": "captura", "acceso_voluntario": "no", "evidencia": "Bond es sedado con un dardo y despierta retenido junto a Natalya dentro del helicóptero Tiger.", "localizador": "Plot: encuentro con Janus. No cuento el interrogatorio posterior de las autoridades rusas.", "fuente_url": "https://en.wikipedia.org/wiki/GoldenEye", "consulta": "2026-11-17", "metodo": "codificacion_manual_de_fuentes_documentales_sin_visionado", "captura_documentada": "1", "criterio_conservador": "1", "criterio_ampliado": "1"}, {"id": "bond_18", "anio": "1997", "titulo_original": "Tomorrow Never Dies", "titulo_es": "El mañana nunca muere", "actor": "Pierce Brosnan", "tipo": "captura", "acceso_voluntario": "no", "evidencia": "Stamper captura a Bond y Wai Lin tras salir del barco hundido; ambos son conducidos a la torre de Carver.", "localizador": "Plot: captura tras la inmersión y traslado a Saigón.", "fuente_url": "https://en.wikipedia.org/wiki/Tomorrow_Never_Dies", "consulta": "2026-11-17", "metodo": "codificacion_manual_de_fuentes_documentales_sin_visionado", "captura_documentada": "1", "criterio_conservador": "1", "criterio_ampliado": "1"}, {"id": "bond_19", "anio": "1999", "titulo_original": "The World Is Not Enough", "titulo_es": "El mundo nunca es suficiente", "actor": "Pierce Brosnan", "tipo": "captura", "acceso_voluntario": "no", "evidencia": "Los hombres de Elektra capturan a Bond. Ella lo inmoviliza y tortura con un garrote en la Torre de la Doncella.", "localizador": "Plot: captura y tortura en la torre.", "fuente_url": "https://en.wikipedia.org/wiki/The_World_Is_Not_Enough", "consulta": "2026-11-17", "metodo": "codificacion_manual_de_fuentes_documentales_sin_visionado", "captura_documentada": "1", "criterio_conservador": "1", "criterio_ampliado": "1"}, {"id": "bond_20", "anio": "2002", "titulo_original": "Die Another Day", "titulo_es": "Muere otro día", "actor": "Pierce Brosnan", "tipo": "captura", "acceso_voluntario": "no", "evidencia": "Los soldados norcoreanos capturan a Bond; tras catorce meses de cautiverio lo liberan mediante un intercambio de prisioneros.", "localizador": "Plot: misión inicial en Corea del Norte e intercambio.", "fuente_url": "https://en.wikipedia.org/wiki/Die_Another_Day", "consulta": "2026-11-17", "metodo": "codificacion_manual_de_fuentes_documentales_sin_visionado", "captura_documentada": "1", "criterio_conservador": "1", "criterio_ampliado": "1"}, {"id": "bond_21", "anio": "2006", "titulo_original": "Casino Royale", "titulo_es": "Casino Royale", "actor": "Daniel Craig", "tipo": "captura", "acceso_voluntario": "no", "evidencia": "Le Chiffre captura y tortura a Bond para obtener la contraseña del dinero del torneo. La irrupción de Mr. White evita su ejecución.", "localizador": "Plot: secuestro de Vesper y tortura en el barco.", "fuente_url": "https://en.wikipedia.org/wiki/Casino_Royale_(2006_film)", "consulta": "2026-11-17", "metodo": "codificacion_manual_de_fuentes_documentales_sin_visionado", "captura_documentada": "1", "criterio_conservador": "1", "criterio_ampliado": "1"}, {"id": "bond_22", "anio": "2008", "titulo_original": "Quantum of Solace", "titulo_es": "Quantum of Solace", "actor": "Daniel Craig", "tipo": "no_documentada", "acceso_voluntario": "no", "evidencia": "No he identificado en las fuentes consultadas una captura enemiga equiparable. Las órdenes de sus superiores y los intentos de detenerlo no acreditan por sí solos ese episodio.", "localizador": "No documento no equivale a demostrar ausencia; falta un visionado sistemático. No codifico un cero.", "fuente_url": "https://en.wikipedia.org/wiki/Quantum_of_Solace", "consulta": "2026-11-17", "metodo": "codificacion_manual_de_fuentes_documentales_sin_visionado", "captura_documentada": "", "criterio_conservador": "", "criterio_ampliado": ""}, {"id": "bond_23", "anio": "2012", "titulo_original": "Skyfall", "titulo_es": "Skyfall", "actor": "Daniel Craig", "tipo": "captura", "acceso_voluntario": "si", "evidencia": "Bond viaja voluntariamente con Sévérine para conocer a su empleador. La tripulación los captura y los entrega a Silva; después llegan refuerzos llamados por Bond.", "localizador": "Caso contextual: el acceso es voluntario. No afirmo que pretendiera ser capturado. Lo excluyo en la comprobación conservadora.", "fuente_url": "https://en.wikipedia.org/wiki/Skyfall", "consulta": "2026-11-17", "metodo": "codificacion_manual_de_fuentes_documentales_sin_visionado", "captura_documentada": "1", "criterio_conservador": "", "criterio_ampliado": "1"}, {"id": "bond_24", "anio": "2015", "titulo_original": "Spectre", "titulo_es": "Spectre", "actor": "Daniel Craig", "tipo": "captura", "acceso_voluntario": "no", "evidencia": "En Londres, los agentes de Spectre secuestran por separado a Bond y Madeleine y trasladan a Bond al antiguo edificio del servicio secreto.", "localizador": "Uso el secuestro de Londres, no la visita voluntaria a la base del Sahara, para comprobar la captura.", "fuente_url": "https://en.wikipedia.org/wiki/Spectre_(2015_film)", "consulta": "2026-11-17", "metodo": "codificacion_manual_de_fuentes_documentales_sin_visionado", "captura_documentada": "1", "criterio_conservador": "1", "criterio_ampliado": "1"}, {"id": "bond_25", "anio": "2021", "titulo_original": "No Time to Die", "titulo_es": "Sin tiempo para morir", "actor": "Daniel Craig", "tipo": "encierro_trampa", "acceso_voluntario": "no", "evidencia": "Ash dispara a Leiter, encierra a Bond con él bajo cubierta y activa explosivos para hundir el barco.", "localizador": "Trampa con encierro físico; la separo de una captura con custodia continuada. Sólo entra en el criterio ampliado.", "fuente_url": "https://en.wikipedia.org/wiki/No_Time_to_Die", "consulta": "2026-11-17", "metodo": "codificacion_manual_de_fuentes_documentales_sin_visionado", "captura_documentada": "", "criterio_conservador": "", "criterio_ampliado": "1"}]</script>
<script>
(() => {
  const fuente = document.getElementById('bond-datos');
  if (!fuente) return;
  const datos = JSON.parse(fuente.textContent);
  const skyfall = document.getElementById('bond-skyfall');
  const trampa = document.getElementById('bond-trampa');
  const selector = document.getElementById('bond-pelicula');
  const resumen = document.getElementById('bond-resumen');
  const mapa = document.getElementById('bond-mapa');
  const detalle = document.getElementById('bond-detalle');
  if (!skyfall || !trampa || !selector || !resumen || !mapa || !detalle) return;
  const etiquetas = {captura:'Captura documentada',encierro_trampa:'Encierro-trampa',no_documentada:'Sin prueba registrada: no equivale a ausencia'};
  const incluido = d => (d.tipo === 'captura' && (skyfall.checked || d.acceso_voluntario !== 'si')) || (trampa.checked && d.tipo === 'encierro_trampa');
  const elemento = (tipo,texto) => { const e=document.createElement(tipo);e.textContent=texto;return e; };
  const actualizar = () => {
    const cantidad=datos.filter(incluido).length;
    resumen.replaceChildren(elemento('strong',cantidad+' de 25 películas · '+(cantidad*4)+' %'),elemento('span','Mínimo documentado con el criterio elegido; no es una tasa de fracaso.'));
    mapa.querySelector('title').textContent='Casos documentados en '+cantidad+' de 25 películas';
    mapa.querySelector('desc').textContent='Cuadrícula cronológica. '+cantidad+' círculos azules indican películas incluidas. Los contornos vacíos no acreditan ausencia.';
    mapa.querySelectorAll('circle').forEach((c,i)=>{c.setAttribute('fill',incluido(datos[i])?'#446ddf':'#faf8f2');c.setAttribute('stroke-width',datos[i].id===selector.value?'3.5':'1.5');});
    const d=datos.find(f=>f.id===selector.value);
    const enlace=elemento('a','Consultar fuente de esta película');enlace.href=d.fuente_url;
    const origen=elemento('p','');origen.append(enlace);
    detalle.replaceChildren(elemento('h4',d.titulo_es+' ('+d.anio+')'),elemento('p',etiquetas[d.tipo]+'. '+d.evidencia),elemento('p',d.localizador),origen);
  };
  skyfall.addEventListener('change',actualizar);
  trampa.addEventListener('change',actualizar);
  selector.addEventListener('change',actualizar);
  actualizar();
})();
</script>
<style>
.bond-expediente{background:#faf8f2;border:1px solid #aab5ce;border-radius:16px;padding:clamp(16px,4vw,30px);margin:2rem 0;color:#1d3157;max-width:100%;box-sizing:border-box}
.bond-expediente fieldset{border:1px solid #8d9ab5;padding:12px;margin:1rem 0;min-width:0}
.bond-expediente label{display:block;margin:.65rem 0;line-height:1.55}
.bond-expediente input{width:20px;height:20px;accent-color:#314a87;vertical-align:middle;margin-right:8px;flex-shrink:0}
.bond-expediente select{display:block;width:100%;max-width:100%;min-width:0;font:inherit;color:#1d3157;background:#fff;border:1px solid #697a9a;border-radius:6px;padding:12px;box-sizing:border-box}
.bond-expediente :focus-visible{outline:3px solid #243f84;outline-offset:4px}
#bond-resumen{display:grid;gap:6px;margin:18px 0}#bond-resumen strong{font-size:clamp(21px,5vw,30px)}
.bond-expediente figure{max-width:270px;margin:1rem auto}.bond-expediente svg{display:block;width:100%;height:auto}
#bond-detalle{border-top:1px solid #b0bad0;margin-top:1rem;padding-top:1rem;overflow-wrap:anywhere}
.bond-expediente h4{font-size:1.12rem;margin:.5rem 0}.bond-expediente a{color:#243f84;text-decoration:underline}
.bond-expediente summary{cursor:pointer;font-weight:700;padding:14px 0;min-height:44px;box-sizing:border-box}
.bond-tabla-scroll{overflow-x:auto;max-width:100%}.bond-expediente table{border-collapse:collapse;min-width:580px;width:100%;font-size:.9rem}
.bond-expediente td,.bond-expediente th{padding:12px;text-align:left;vertical-align:top;border-bottom:1px solid #b0bad0}
.bond-expediente caption{text-align:left;padding:12px 0}.bond-expediente th:first-child{width:25%}
</style>
