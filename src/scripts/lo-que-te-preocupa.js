const esc = (value = '') => String(value).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const clean = value => String(value).normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
const icon = (name) => {
  const shapes = {casa:'<path d="M3 15 16 4l13 11M7 12v17h18V12M13 29V19h6v10"/>',cartera:'<rect x="4" y="8" width="25" height="20" rx="2"/><path d="M5 8V5h20v3M21 15h8v8h-8zM24 19h1"/>',salud:'<path d="M12 4h8v8h8v8h-8v8h-8v-8H4v-8h8z"/>',manos:'<path d="m3 21 7-7 6 4 6-4 7 7M3 21l8 8 5-4 5 4 8-8M10 14V6h5l1 4 1-4h5v8"/>',reloj:'<circle cx="16" cy="16" r="12"/><path d="M16 8v9l6 4"/>',horizonte:'<path d="M3 25h26M7 20a9 9 0 0 1 18 0M16 2v4M3 9l4 3M29 9l-4 3"/>',pixel:'<rect x="7" y="7" width="18" height="18" rx="2"/><path d="M12 2v5M20 2v5M12 25v5M20 25v5M2 12h5M2 20h5M25 12h5M25 20h5M12 12h8v8h-8z"/>'};
  return `<svg class="lp-icon" viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">${shapes[name] || shapes.pixel}</svg>`;
};
export function iniciarPreocupa() {
  const root = document.getElementById('preocupa');
  const dataElement = document.getElementById('lp-data');
  if (!root || !dataElement || root.dataset.ready) return;
  root.dataset.ready = 'true';
  const data = JSON.parse(dataElement.textContent);
  const byParty = new Map(data.parties.map(p => [p.id,p]));
  const byProposal = new Map(data.proposals.map(p => [p.id,p]));
  const activeParties = data.parties.filter(p => p.status !== 'pending');
  const $ = id => root.querySelector(`#${id}`);
  const state = {view:'situations',topic:null,party:null,question:'all',query:'',parties:new Set(activeParties.map(p=>p.id)),saved:new Set(),compare:[],comparing:false};
  function announce(text){ $('lp-announcement').textContent=text; $('lp-visible-status').textContent=text; }
  function sourceUrl(row){ const p=byParty.get(row.party); return p.url+(row.page?`#page=${row.page}`:(p.url.includes('.pdf')&&row.search?`#search=${encodeURIComponent(row.search)}`:'')); }
  function sourceLink(row){return `<a href="${esc(sourceUrl(row))}" target="_blank" rel="noopener noreferrer" aria-label="Leer la fuente de ${esc(byParty.get(row.party).name)}: ${esc(row.reference)} (nueva pestaña)">Leer la fuente ↗</a>`;}
  function saveButton(row){const saved=state.saved.has(row.id);return `<button type="button" class="lp-save" data-save="${esc(row.id)}" aria-pressed="${saved}" aria-label="${saved?'Quitar de':'Guardar en'} mi selección: ${esc(byParty.get(row.party).name)}, ${esc(row.title)}"><svg viewBox="0 0 20 20" fill="${saved?'currentColor':'none'}" stroke="currentColor" stroke-width="1.4" aria-hidden="true"><path d="M5 3h10v14l-5-3-5 3z"/></svg></button>`;}
  function card(row){const p=byParty.get(row.party);return `<article class="lp-card" aria-labelledby="title-${esc(row.id)}"><div class="lp-card-header"><div><p class="lp-party-name">${esc(p.name)}</p><p class="lp-card-meta">${esc(data.topics.find(t=>t.id===row.topic).name)} · ${esc(p.scope)}</p></div>${saveButton(row)}</div><h3 id="title-${esc(row.id)}">${esc(row.title)}</h3><p class="lp-card-summary">${esc(row.summary)}</p><dl><dt>A quién se dirige</dt><dd>${esc(row.audience)}</dd><dt>Dónde comprobarlo</dt><dd>${esc(row.reference)}</dd></dl><details><summary>Plazos, financiación y alcance</summary><p><strong>Plazo:</strong> ${esc(row.deadline||'No he incorporado un plazo verificable en esta ficha.')}</p><p><strong>Financiación:</strong> ${esc(row.funding||'No he incorporado una financiación detallada en esta ficha.')}</p><p>Esto describe la revisión de esta ficha, no demuestra una ausencia en el documento completo.</p></details>${p.status==='partial'?'<p class="lp-source-note">Fuente parcial: resumen oficial del partido.</p>':''}<div class="lp-card-footer">${sourceLink(row)}<button type="button" data-compare="${esc(row.id)}" aria-pressed="${state.compare.includes(row.id)}">${state.compare.includes(row.id)?'En comparación':'Comparar'}</button></div></article>`;}
  function buildEntry(){
    root.querySelectorAll('[data-view]').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.view===state.view)));
    if(state.view==='situations'){
      $('lp-entry').innerHTML=`<div class="lp-section-head"><h2 id="lp-entry-title">¿Por dónde quieres empezar?</h2><p>Elige una situación. Puedes cambiar después.</p></div><div class="lp-situations">${data.topics.map((t,i)=>`<button type="button" class="lp-situation" data-topic="${t.id}" aria-pressed="${state.topic===t.id}">${icon(t.icon)}<span class="lp-topic-index">0${i+1} / ${esc(t.name)}</span><strong>${esc(t.situation)}</strong><small>${esc(t.hint)}</small><span class="lp-arrow" aria-hidden="true">↗</span></button>`).join('')}</div>`;
    } else if(state.view==='parties'){
      $('lp-entry').innerHTML=`<div class="lp-section-head"><h2 id="lp-entry-title">Entra por un partido.</h2><p>Orden alfabético. Consulta la cobertura al pie.</p></div><div class="lp-parties">${data.parties.map(p=>`<button type="button" data-party="${p.id}" aria-pressed="${state.party===p.id}">${esc(p.name)}${p.status==='pending'?' · pendiente':''}</button>`).join('')}</div><p class="lp-entry-note">La selección incluye documentos estatales y territoriales. No todas las formaciones concurren en todas las circunscripciones.</p>`;
    } else {
      $('lp-entry').innerHTML=`<div class="lp-section-head"><h2 id="lp-entry-title">Lo que quieres mirar con calma.</h2><p>${state.saved.size} fichas guardadas en esta pestaña.</p></div><p class="lp-entry-note">Se borran al recargar. Puedes imprimir o guardar esta vista como PDF desde tu navegador.</p><button type="button" class="lp-text-button" id="lp-clear-saved">Vaciar mi selección</button>`;
    }
  }
  function buildFilters(){ $('lp-filters').innerHTML=activeParties.map(p=>`<label><input type="checkbox" value="${p.id}" data-party-filter ${state.parties.has(p.id)?'checked':''}>${esc(p.name)}</label>`).join(''); }
  function renderResults(){
    const topic=data.topics.find(t=>t.id===state.topic);
    const party=byParty.get(state.party);
    const visible=state.view==='saved'||(state.view==='situations'&&topic)||(state.view==='parties'&&party);
    $('lp-results').hidden=!visible;
    if(!visible) return;
    $('lp-results-title').textContent=state.view==='saved'?'Mi selección':state.view==='parties'?party.name:topic.situation;
    $('lp-results-kicker').textContent=state.view==='saved'?'PARA VOLVER A LEER':state.view==='parties'?'SU DOCUMENTO, POR SITUACIONES':topic.name.toUpperCase();
    $('lp-context').textContent=state.view==='parties'?party.note:'Compara compromisos electorales. La selección es parcial y no evalúa si las medidas funcionarán. Las fuentes se abren en otra pestaña.';
    $('lp-share').hidden=state.view==='saved';
    $('lp-questions').innerHTML=state.view==='situations'?`<button type="button" data-question="all" aria-pressed="${state.question==='all'}">Ver todas</button>${topic.questions.map(([id,label])=>`<button type="button" data-question="${id}" aria-pressed="${state.question===id}">${esc(label)}</button>`).join('')}`:'';
    root.querySelector('.lp-party-filter').hidden=state.view==='parties';
    let selected=data.proposals.filter(r=>state.view==='saved'?state.saved.has(r.id):state.view==='parties'?r.party===state.party:r.topic===state.topic&&(state.question==='all'||r.tags.includes(state.question)));
    if(state.view!=='parties')selected=selected.filter(r=>state.parties.has(r.party));
    if(state.query)selected=selected.filter(r=>clean([r.title,r.summary,r.audience,r.reference,byParty.get(r.party).name].join(' ')).includes(clean(state.query)));
    selected.sort((a,b)=>byParty.get(a.party).name.localeCompare(byParty.get(b.party).name,'es')||data.topics.findIndex(t=>t.id===a.topic)-data.topics.findIndex(t=>t.id===b.topic));
    $('lp-counter').textContent=`${selected.length} ${selected.length===1?'ficha':'fichas'} · ${new Set(selected.map(p=>p.party)).size} ${new Set(selected.map(p=>p.party)).size===1?'partido':'partidos'} · última revisión: 27 nov 2026`;
    $('lp-cards').innerHTML=selected.map(card).join('')||`<p class="lp-empty">${state.view==='saved'&&!state.saved.size?'Todavía no has guardado propuestas. Pulsa el marcador de una ficha para añadirla aquí.':'No hay fichas con estos filtros. Prueba a limpiar la búsqueda o cambiar la selección.'}</p>`;
    const gaps=state.view==='situations'&&!state.query?activeParties.filter(p=>state.parties.has(p.id)&&!selected.some(r=>r.party===p.id)):[];
    $('lp-gaps').innerHTML=gaps.map(p=>`<div class="lp-gap"><strong>${esc(p.name)}</strong><p>Sin ficha revisada para esta pregunta. No significa que el programa carezca de propuesta.</p></div>`).join('')+(state.view==='parties'&&party.status==='pending'?`<div class="lp-gap"><strong>Documento pendiente de revisión</strong><p>${esc(party.note)}</p><a href="${esc(party.url)}" target="_blank" rel="noopener noreferrer">Consultar la web de la formación ↗</a></div>`:'');
    updateCompare();
  }
  function updateCompare(){
    $('lp-tray').hidden=!state.compare.length;
    $('lp-tray-count').textContent=`${state.compare.length} de 3 propuestas`;
    $('lp-do-compare').disabled=state.compare.length<2;
    $('lp-compare').hidden=!state.comparing||state.compare.length<2;
    if(!$('lp-compare').hidden)$('lp-compare-grid').innerHTML=state.compare.map(id=>{const row=byProposal.get(id);return `<article class="lp-compare-card"><p class="lp-party-name">${esc(byParty.get(row.party).name)}</p><h3>${esc(row.title)}</h3><dl><dt>Qué propone</dt><dd>${esc(row.summary)}</dd><dt>A quién se dirige</dt><dd>${esc(row.audience)}</dd><dt>Plazo recogido en la ficha</dt><dd>${esc(row.deadline||'No incorporado en esta revisión.')}</dd><dt>Financiación recogida</dt><dd>${esc(row.funding||'No incorporada en esta revisión.')}</dd><dt>Referencia</dt><dd>${esc(row.reference)}</dd></dl><p>${sourceLink(row)}</p><button class="lp-text-button" type="button" data-compare="${esc(id)}">Quitar de la comparación</button></article>`;}).join('');
  }
  function urlState(){
    const params=new URLSearchParams();
    if(state.view==='parties'){params.set('vista','partidos');if(state.party)params.set('partido',state.party);}
    else if(state.topic){params.set('tema',state.topic);if(state.question!=='all')params.set('pregunta',state.question);}
    if(state.parties.size!==activeParties.length)params.set('partidos',[...state.parties].sort().join(','));
    if(state.query)params.set('buscar',state.query);
    return params.toString();
  }
  function remember(){const params=urlState();history.replaceState(null,'',`${location.pathname}${params?'?'+params:''}${location.hash}`);}
  function refresh(){buildEntry();buildFilters();renderResults();$('lp-saved-count').textContent=state.saved.size;}
  function resultFocus(){ $('lp-results-title').focus({preventScroll:true});$('lp-results').scrollIntoView({behavior:matchMedia('(prefers-reduced-motion: reduce)').matches?'auto':'smooth',block:'start'}); }
  root.addEventListener('click',async event=>{
    const btn=event.target.closest('button');if(!btn)return;
    if(btn.dataset.view){state.view=btn.dataset.view;state.query='';$('lp-search').value='';refresh();remember();root.querySelector(`[data-view="${state.view}"]`).focus();}
    if(btn.dataset.topic){state.topic=btn.dataset.topic;state.question='all';state.query='';$('lp-search').value='';refresh();remember();resultFocus();}
    if(btn.dataset.party){state.party=btn.dataset.party;state.query='';$('lp-search').value='';refresh();remember();resultFocus();}
    if(btn.dataset.question){state.question=btn.dataset.question;renderResults();remember();root.querySelector(`[data-question="${state.question}"]`)?.focus();}
    if(btn.dataset.save){const id=btn.dataset.save;state.saved.has(id)?state.saved.delete(id):state.saved.add(id);const isSaved=state.saved.has(id);$('lp-saved-count').textContent=state.saved.size;if(state.view==='saved'){refresh();$('lp-results-title').focus({preventScroll:true});}else{renderResults();root.querySelector(`[data-save="${id}"]`)?.focus({preventScroll:true});}announce(isSaved?'Propuesta guardada en esta pestaña.':'Propuesta retirada de mi selección.');}
    if(btn.dataset.compare){const id=btn.dataset.compare;const row=byProposal.get(id);if(state.compare.includes(id)){state.compare=state.compare.filter(x=>x!==id);}else{if(state.compare.length&&byProposal.get(state.compare[0]).topic!==row.topic){announce('Compara propuestas de la misma situación. Vacía la comparación para cambiar de tema.');return;}if(state.compare.length===3){announce('Puedes comparar hasta tres propuestas. Retira una para añadir otra.');return;}state.compare.push(id);}renderResults();updateCompare();root.querySelector(`[data-compare="${id}"]`)?.focus({preventScroll:true});announce(`${state.compare.length} propuestas en comparación.`);}
    if(btn.id==='lp-do-compare'){state.comparing=true;updateCompare();$('lp-compare-title').focus({preventScroll:true});$('lp-compare').scrollIntoView({behavior:matchMedia('(prefers-reduced-motion: reduce)').matches?'auto':'smooth'});}
    if(btn.id==='lp-clear-compare'){state.comparing=false;updateCompare();$('lp-do-compare').focus();}
    if(btn.id==='lp-empty-compare'){state.compare=[];state.comparing=false;renderResults();updateCompare();$('lp-results-title').focus({preventScroll:true});announce('Comparación vaciada.');}
    if(btn.id==='lp-clear-saved'){state.saved.clear();refresh();$('lp-results-title').focus({preventScroll:true});announce('Selección vaciada.');}
    if(btn.id==='lp-reset'){state.question='all';state.query='';state.parties=new Set(activeParties.map(p=>p.id));$('lp-search').value='';buildFilters();renderResults();remember();}
    if(btn.id==='lp-all-parties'){state.parties=new Set(activeParties.map(p=>p.id));buildFilters();renderResults();remember();}
    if(btn.id==='lp-share'){
      const url=new URL(location.href);url.search=urlState();url.hash='';
      try{if(!navigator.clipboard)throw Error('clipboard');await navigator.clipboard.writeText(url.href);btn.textContent='Enlace copiado';announce('Enlace a esta consulta copiado.');setTimeout(()=>{if(btn.isConnected)btn.textContent='Copiar enlace a esta consulta';},2500);}catch{announce('No se pudo copiar automáticamente. Puedes copiar la dirección de la barra del navegador.');btn.textContent='Copia la dirección del navegador';}
    }
  });
  $('lp-search').addEventListener('input',event=>{state.query=event.target.value;renderResults();remember();});
  $('lp-filters').addEventListener('change',event=>{const input=event.target.closest('[data-party-filter]');if(!input)return;input.checked?state.parties.add(input.value):state.parties.delete(input.value);renderResults();remember();});
  const params=new URLSearchParams(location.search);
  if(params.get('vista')==='partidos')state.view='parties';
  if(byParty.has(params.get('partido')))state.party=params.get('partido');
  if(data.topics.some(t=>t.id===params.get('tema')))state.topic=params.get('tema');
  if(state.topic&&data.topics.find(t=>t.id===state.topic).questions.some(([q])=>q===params.get('pregunta')))state.question=params.get('pregunta');
  if(params.has('partidos'))state.parties=new Set(params.get('partidos').split(',').filter(id=>activeParties.some(p=>p.id===id)));
  state.query=(params.get('buscar')||'').slice(0,200);$('lp-search').value=state.query;
  $('lp-total').textContent=`${data.proposals.length} fichas de ${activeParties.length} formaciones, repartidas en ${data.topics.length} situaciones`;
  $('lp-source-list').innerHTML=data.parties.map(p=>`<div class="lp-source-item"><strong>${esc(p.name)}</strong><div><p>${esc(p.document)} · ${p.status==='pending'?'Sin fichas':`${data.proposals.filter(r=>r.party===p.id).length} fichas`}</p><p>${esc(p.note)}</p><a href="${esc(p.url)}" target="_blank" rel="noopener noreferrer">${p.status==='pending'?'Consultar referencia localizada':'Abrir documento consultado'} ↗</a></div></div>`).join('');
  refresh();
}
