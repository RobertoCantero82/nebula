---
titulo: 'Ningún lugar del cielo está a salvo de una explosión cósmica'
descripcion: 'Un análisis de 4.408 estallidos de rayos gamma muestra por qué cualquier dirección puede encender la próxima alarma.'
tema: 'CIENCIA'
fecha: 2026-10-30
imagenPortada: '/nebula/imagenes/estallidos_rayos_gamma_portada.png'
cifraDestacada: '238'
etiquetaCifra: 'estallidos detectados al año de media'
metodologia: 'EDA del catálogo FERMIGBRST de NASA HEASARC, actualizado el 28 de octubre de 2026. Analizo 4.408 estallidos registrados entre julio de 2008 y el 29 de octubre de 2026. Para la media anual utilizo los 17 años naturales completos de 2009 a 2025. Compruebo el reparto celeste con diez bandas de igual superficie y 20.000 simulaciones uniformes. Describo detecciones de Fermi, no todos los estallidos del universo, y no genero predicciones propias.'
---

**Imagina que el cielo pudiera encender una alarma sin avisar.** No sabrías cuándo sonará, cuánto durará ni hacia dónde mirar. Puede saltar sobre una constelación conocida o en un punto oscuro al que nunca habías prestado atención. Eso es, más o menos, lo que ocurre con los estallidos de rayos gamma.

Son fogonazos de la luz más energética que conocemos. Algunos duran menos que un parpadeo. Otros, varios minutos. Pueden nacer cuando muere una estrella enorme o cuando chocan dos objetos tan densos como las estrellas de neutrones. El reciente GRB 260310A llamó la atención porque su primer destello pareció modesto y su resplandor posterior acabó entre los más brillantes observados.

Sin embargo, ese caso extraordinario forma parte de una lluvia mucho mayor. He reunido **4.408 estallidos clasificados por el monitor GBM del telescopio espacial Fermi**, desde julio de 2008 hasta el 29 de octubre de 2026, para responder a una pregunta más sencilla: ¿con qué frecuencia los vemos y de qué parte del cielo llegan?

<figure class="video-rayos-gamma">
  <div class="video-rayos-gamma__marco">
    <iframe
      src="https://www.youtube-nocookie.com/embed/S1pa_G3Tz0A"
      title="Vídeo sobre los estallidos de rayos gamma"
      loading="lazy"
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
      allowfullscreen>
    </iframe>
  </div>

  <figcaption>
    Una explicación visual de cómo se producen los estallidos de rayos gamma.
  </figcaption>
</figure>

<style>
  .video-rayos-gamma {
    margin: 2rem 0;
  }

  .video-rayos-gamma__marco {
    position: relative;
    overflow: hidden;
    width: 100%;
    aspect-ratio: 16 / 9;
    border-radius: 14px;
    background: #111827;
  }

  .video-rayos-gamma__marco iframe {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    border: 0;
  }

  .video-rayos-gamma figcaption {
    margin-top: 0.65rem;
    color: #586174;
    font-size: 0.85em;
    line-height: 1.5;
  }
</style>

## Cientos de alarmas cada año

Para comparar periodos completos he apartado 2008, porque Fermi empezó a trabajar en julio, y 2026, que todavía no ha terminado. Entre los años 2009 y 2025, el satélite registró una media de **238 estallidos al año**. El mínimo fueron 218 y el máximo 271.

Eso equivale, aproximadamente, a una detección cada día y medio. Eso si, esto no significa que el universo solo produzca esa cantidad. La Tierra tapa parte del cielo, el instrumento no mantiene siempre la misma orientación y las señales más débiles pueden pasar inadvertidas. **Estamos contando lo que Fermi detecta y clasifica**, no todo lo que sucede.

<figure class="grb-figura">
  <figcaption><strong>Fermi detecta cientos de estallidos cada año</strong><br>Estallidos clasificados en años naturales completos. La línea marca la media de 238.</figcaption>
  <div id="grb-anios" class="grb-barras" role="img" aria-label="Gráfico de barras con entre 218 y 271 estallidos anuales desde 2009 hasta 2025"></div>
</figure>

La estabilidad resulta llamativa. Hay altibajos, pero ningún año multiplica por dos al anterior ni deja el contador cerca de cero. El cielo de rayos gamma no es una fiesta anual con fecha marcada: es un **goteo continuo** de explosiones lejanas.

## Haz tu apuesta antes de mirar

**¿Dónde colocarías la mayoría?** ¿Quizás cerca del plano de la Vía Láctea, la franja donde se concentran tantas estrellas de nuestra galaxia o hacia una mitad concreta del cielo?

<fieldset id="grb-apuesta" class="grb-bloque">
  <legend>¿Dónde esperas encontrar más estallidos?</legend>
  <div class="grb-opciones">
    <button type="button" data-grb="plano">Cerca del plano de la Vía Láctea</button>
    <button type="button" data-grb="norte">En una mitad del cielo</button>
    <button type="button" data-grb="todas">Repartidos en todas direcciones</button>
  </div>
  <p id="grb-respuesta" role="status" aria-live="polite">Elige una opción para descubrir qué muestran los datos.</p>
</fieldset>

<figure class="grb-figura">
  <figcaption><strong>Los fogonazos aparecen por todo el cielo</strong><br>Cada punto representa una detección. El centro corresponde a la dirección del centro de la Vía Láctea.</figcaption>
  <canvas id="grb-cielo" width="900" height="450" role="img" aria-label="Mapa ovalado con estallidos de rayos gamma distribuidos por todo el cielo"></canvas>
  <p class="grb-nota">La proyección deforma las distancias, como cualquier mapamundi. Las posiciones individuales también tienen incertidumbre.</p>
</figure>

## La franja que no apareció

El mapa permite intuir el resultado, pero los puntos se pisan y nuestros ojos encuentran dibujos incluso donde solo hay azar. Para comprobarlo **dividí el cielo en diez bandas con la misma superficie**. No usé franjas con los mismos grados, porque cerca de los polos hay menos cielo disponible, igual que en un mapamundi hay menos superficie cerca de los extremos.

Las bandas contienen entre 413 y 490 estallidos. Después fabriqué 20.000 cielos imaginarios, todos uniformes y con el mismo número de puntos. En el **23,3 %** de esas simulaciones aparecieron diferencias entre bandas tan grandes o mayores que las reales.

Eso no prueba que el reparto sea perfectamente uniforme. Significa que **los datos son compatibles con que las diferencias se deban al azar**. Tampoco aparece un desequilibrio entre mitades. El 50,4 % de los estallidos cae al norte del plano galáctico y el 49,6 %, al sur.

Este reparto fue una pista histórica importante. Si los estallidos pertenecieran principalmente a nuestra galaxia, esperaríamos reconocer su forma: una concentración hacia el disco de la Vía Láctea. En cambio, **llegan desde todas partes** porque están repartidos por el universo lejano.

## Un universo sin rincón tranquilo

Fermi no ve todas las explosiones y su sensibilidad no es idéntica en cualquier circunstancia. Además, este análisis no calcula la distancia de cada estallido. La ausencia de una franja galáctica describe la población completa, pero no funciona como certificado de origen para cada punto individual.

<figure class="video-rayos-gamma">
  <div class="video-rayos-gamma__marco">
    <iframe
      src="https://www.youtube-nocookie.com/embed/zLchqzpFF5c"
      title="Vídeo sobre los estallidos de rayos gamma"
      loading="lazy"
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
      allowfullscreen>
    </iframe>
  </div>

  <figcaption>
    Otra mirada visual a los fenómenos más energéticos del universo.
  </figcaption>
</figure>

Aun así, la imagen conjunta resulta poderosa. **GRB 260310A** puede destacar por la extraña evolución de su brillo, pero no apareció en un escenario vacío. Forma **parte de una colección que crece unas 238 veces por año**.

El universo no reserva sus mayores fogonazos para un solo rincón del cielo. Desde la Tierra, cualquier dirección puede ser la próxima.

## Fuentes y análisis

- [Catálogo Fermi GBM Burst de NASA HEASARC](https://heasarc.gsfc.nasa.gov/W3Browse/fermi/fermigbrst.html) y [portal de datos de Fermi](https://fermi.gsfc.nasa.gov/ssc/data/access/).
- [Estudio de GRB 260310A](https://arxiv.org/abs/2605.23818).
- [Notebook del análisis](/nebula/analisis/estallidos-rayos-gamma/analisis_estallidos_rayos_gamma.ipynb), [datos utilizados](/nebula/analisis/estallidos-rayos-gamma/fermi_gbm_estallidos.csv), [respuesta original de NASA](/nebula/analisis/estallidos-rayos-gamma/fermi_gbm_catalogo_raw.xml) y [guía de reproducción](/nebula/analisis/estallidos-rayos-gamma/README.md).

<style>
.grb-figura{margin:2rem 0}.grb-figura figcaption{font-size:.95em;line-height:1.5;margin-bottom:.8rem}.grb-barras{display:flex;align-items:flex-end;gap:clamp(2px,.55vw,7px);height:230px;padding:16px 8px 28px;border-left:1px solid #cbd3e5;border-bottom:1px solid #cbd3e5}.grb-barra{flex:1;min-width:4px;background:#446ddf;border-radius:3px 3px 0 0;position:relative}.grb-barra span{position:absolute;top:100%;left:50%;transform:translate(-50%,7px) rotate(-55deg);font-size:10px;color:#586174}.grb-bloque{border:1px solid #becbec;border-radius:14px;padding:1.2rem;margin:1.8rem 0;background:#f5f7fd}.grb-bloque legend{font-weight:700;padding:0 .5rem}.grb-opciones{display:flex;gap:.65rem;flex-wrap:wrap}.grb-opciones button{font:inherit;padding:.65rem .8rem;border:1px solid #446ddf;border-radius:8px;background:white;color:#23439b}.grb-opciones button[aria-pressed="true"]{background:#446ddf;color:white}.grb-bloque :focus-visible{outline:3px solid #a76d3c;outline-offset:3px}#grb-cielo{display:block;width:100%;height:auto;background:#faf7ef;border-radius:50%;border:1px solid #d9d1bf}.grb-nota{font-size:.82em;color:#586174}
</style>

<script>
document.addEventListener('DOMContentLoaded',()=>{
 const anios={2009:250,2010:242,2011:218,2012:220,2013:232,2014:242,2015:237,2016:218,2017:251,2018:243,2019:230,2020:260,2021:235,2022:225,2023:250,2024:228,2025:271};
 const barras=document.getElementById('grb-anios');
 if(barras) Object.entries(anios).forEach(([anio,n])=>{const b=document.createElement('div');b.className='grb-barra';b.style.height=`${n/271*100}%`;b.title=`${anio}: ${n} estallidos`;b.innerHTML=`<span>${anio}</span>`;barras.appendChild(b);});
 document.querySelectorAll('[data-grb]').forEach(b=>b.addEventListener('click',()=>{document.querySelectorAll('[data-grb]').forEach(x=>x.setAttribute('aria-pressed',String(x===b)));const r=document.getElementById('grb-respuesta');r.textContent=b.dataset.grb==='todas'?'Exacto. El catálogo no muestra una dirección privilegiada.':b.dataset.grb==='plano'?'La intuición galáctica falla: no aparece una franja dominante junto a la Vía Láctea.':'Las dos mitades están casi empatadas: 50,4 % frente a 49,6 %.';}));
 const canvas=document.getElementById('grb-cielo');
 if(canvas) fetch('/nebula/analisis/estallidos-rayos-gamma/fermi_gbm_estallidos.csv').then(r=>r.text()).then(texto=>{const ctx=canvas.getContext('2d');ctx.fillStyle='#446ddf';ctx.globalAlpha=.35;texto.trim().split('\n').slice(1).forEach(linea=>{const c=linea.split(',');const lon=Number(c[4]),lat=Number(c[5]);if(!Number.isFinite(lon)||!Number.isFinite(lat))return;const l=((lon+180)%360)-180;const x=canvas.width/2-l/180*canvas.width*.46;const y=canvas.height/2-lat/90*canvas.height*.43;ctx.beginPath();ctx.arc(x,y,1.45,0,Math.PI*2);ctx.fill();});}).catch(()=>{});
});
</script>
