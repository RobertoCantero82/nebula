export const familias = {'fantasmas':'fantasmas','asesinos':'asesinos','monstruos':'monstruos','psicologico':'terror psicológico','ciencia-ficcion':'ciencia ficción','zombis':'zombis','vampiros':'vampiros','ocultismo':'brujería y posesiones'};
export function filtrarPeliculas(peliculas, filtros) {
  return peliculas.filter(p =>
    (!filtros.familia || p.familias.split('|').includes(filtros.familia)) &&
    (!filtros.epoca || (filtros.epoca === 'clasica' ? p.anio < 2000 : p.anio >= 2000)) &&
    (!filtros.minutos || p.duracion <= Number(filtros.minutos)) &&
    (!filtros.intensidad || p.intensidad <= Number(filtros.intensidad)) &&
    (!filtros.tono || p.tono === filtros.tono) &&
    (!filtros.pais || p.paises.split('|').includes(filtros.pais))
  ).sort((a,b) => filtros.orden === 'votos'
    ? b.votos-a.votos || b.nota-a.nota || a.movie_id-b.movie_id
    : b.nota-a.nota || b.votos-a.votos || a.movie_id-b.movie_id);
}

export function explicar(p, f) {
  const razones = [];
  if (f.familia) razones.push(`incluye ${familias[f.familia]}`);
  if (f.epoca) razones.push(f.epoca === 'clasica' ? 'es anterior a 2000' : 'es de 2000 o posterior');
  if (f.minutos) razones.push(`sus ${p.duracion} minutos caben en tu límite de ${f.minutos}`);
  if (f.intensidad) razones.push(`su intensidad editorial (${p.intensidad}/3) no supera tu máximo`);
  if (f.tono) razones.push(f.tono === 'humor' ? 'incluye humor' : 'tiene tono serio');
  if (f.pais) razones.push(`incluye ${f.pais} entre sus países de producción`);
  return razones.length ? 'Encaja porque ' + razones.join('; ') + '.' : 'Sin filtros: aparece por su posición en el orden elegido.';
}

function iniciar() {
  const root = document.querySelector('#halloween-recomendador');
  if (!root) return;
  const form = root.querySelector('form');
  const salida = root.querySelector('#halloween-resultados');
  const estado = root.querySelector('#halloween-estado');
  const boton = root.querySelector('[type="submit"]');
  const mas = root.querySelector('#halloween-mas');
  const reiniciar = root.querySelector('[type="reset"]');
  let peliculas = null, coincidencias = [], limite = 3, actuales = {};
  const numero = new Intl.NumberFormat('es-ES');
  const nota = new Intl.NumberFormat('es-ES', {minimumFractionDigits:2, maximumFractionDigits:2});
  const escalones = {1:'1 · Amenaza sugerida',2:'2 · Tensión intermedia',3:'3 · Violencia o angustia intensa'};
  function elemento(tag, texto, clase) {
    const el=document.createElement(tag); if (texto) el.textContent=texto; if(clase) el.className=clase; return el;
  }
  function pintar() {
    salida.replaceChildren();
    estado.textContent = coincidencias.length
      ? `${coincidencias.length} de ${peliculas.length} películas cumplen todos los filtros. Muestro ${Math.min(limite,coincidencias.length)}, ordenadas por ${actuales.orden === 'votos' ? 'número de votos' : 'nota media'}.`
      : 'No hay películas que cumplan todos esos filtros. Prueba a ampliar el tiempo o cambiar una preferencia. No he relajado tus condiciones.';
    for (const p of coincidencias.slice(0,limite)) {
      const card=elemento('article',null,'halloween-tarjeta');
      card.append(elemento('h3',`${p.titulo} (${p.anio})`));
      card.append(elemento('p',`${p.duracion} min · ${nota.format(p.nota)}/5 · ${numero.format(p.votos)} votos`,'halloween-dato'));
      card.append(elemento('p',p.sinopsis));
      card.append(elemento('p',explicar(p,actuales),'halloween-porque'));
      card.append(elemento('p',`${p.familias.split('|').map(x=>familias[x]).join(' · ')}. ${p.tono==='humor'?'Con humor':'Tono serio'}.`,'halloween-detalle'));
      card.append(elemento('p',`${escalones[p.intensidad]}. Criterio editorial: ${p.criterio_intensidad}.`,'halloween-detalle'));
      if(p.votos<500) card.append(elemento('p','Menos de 500 votos: una referencia con menor participación.','halloween-aviso'));
      if(p.duraciones_ficha.includes('|')) card.append(elemento('p',`La ficha recoge ${p.duraciones_ficha.replaceAll('|',' y ')} minutos según versión. Filtro por el mayor valor.`,'halloween-detalle'));
      if(p.nota_anio) card.append(elemento('p',p.nota_anio,'halloween-detalle'));
      const links=elemento('p',null,'halloween-detalle');
      for (const [etiqueta,url] of [['Ficha y argumento',p.fuente_sinopsis],['Duración',p.fuente_duracion],['Países y géneros',p.wikidata]]) {
        const a=elemento('a',etiqueta); a.href=url; links.append(a,document.createTextNode(' · '));
      }
      card.append(links); salida.append(card);
    }
    mas.hidden=coincidencias.length<=limite;
  }
  async function cargar() {
    estado.textContent='Cargando las 120 películas…';
    try {
      const respuesta=await fetch('/nebula/analisis/halloween_cine/peliculas.json');
      if(!respuesta.ok) throw new Error('No se ha podido cargar el catálogo');
      peliculas=await respuesta.json();
      if(!Array.isArray(peliculas)||peliculas.length!==120) throw new Error('Catálogo incompleto');
      boton.disabled=false;
      estado.textContent='Elige tus preferencias y descubre las coincidencias. Votos históricos hasta octubre de 2023.';
    } catch(e) {
      estado.textContent='No se ha podido cargar el catálogo. Puedes volver a intentarlo o descargar los datos al final del artículo.';
      boton.disabled=false; boton.textContent='Reintentar carga'; peliculas=null;
    }
  }
  form.addEventListener('submit',async e=>{
    e.preventDefault();
    if(!peliculas) { boton.disabled=true; await cargar(); if(peliculas) boton.textContent='Encontrar mi película'; return; }
    actuales=Object.fromEntries(new FormData(form)); limite=3;
    coincidencias=filtrarPeliculas(peliculas,actuales); pintar(); estado.focus();
  });
  form.addEventListener('change',()=>{if(salida.children.length) estado.textContent='Has cambiado tus preferencias. Pulsa «Encontrar mi película» para actualizar los resultados.';});
  mas.addEventListener('click',()=>{limite+=3;pintar();});
  reiniciar.addEventListener('click',()=>{salida.replaceChildren();mas.hidden=true;estado.textContent='Preferencias reiniciadas. Elige de nuevo y pulsa «Encontrar mi película».';});
  cargar();
}
if (typeof document !== 'undefined') {
  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',iniciar,{once:true}); else iniciar();
}
