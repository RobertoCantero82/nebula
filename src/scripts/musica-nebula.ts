let raiz = document.querySelector<HTMLElement>('[data-musica-nebula]');
if (raiz) {
  let boton = raiz.querySelector<HTMLButtonElement>('button')!;
  let aviso = raiz.querySelector<HTMLParagraphElement>('p')!;
  const pistas: string[] = JSON.parse(raiz.dataset.pistas || '[]');
  const audio = new Audio();
  (window as any).__nebulaMusica = { audio }; 
  audio.preload = 'none';
  audio.volume = 0.35;
  const clave = 'nebula-musica-v1';
  let cola: string[] = [];
  let actual = '';
  let ocupado = false;
  let fallos = 0;
  let reanudar = false;
  const guardar = () => {
    try { sessionStorage.setItem(clave, JSON.stringify({ actual, cola, tiempo: audio.currentTime, sonando: !audio.paused })); } catch {}
  };
  const estado = (texto?: string) => {
    if (!raiz) return;
    const sonando = !audio.paused && !audio.ended;
    raiz.toggleAttribute('data-sonando', sonando);
    boton.setAttribute('aria-pressed', String(sonando));
    boton.setAttribute('aria-label', sonando ? 'Pausar música de Nebula' : 'Reproducir música de Nebula');
    aviso.textContent = texto || 'Pulsa en el logo para encender o apagar la música';
  };
  const siguiente = () => {
    if (!cola.length) {
      cola = [...pistas];
      for (let i = cola.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [cola[i], cola[j]] = [cola[j], cola[i]];
      }
      if (cola.length > 1 && cola[cola.length - 1] === actual) [cola[0], cola[cola.length - 1]] = [cola[cola.length - 1], cola[0]];
    }
    actual = cola.pop() || '';
    if (actual) audio.src = actual;
  };
  const reproducir = async () => {
    if (ocupado) return;
    ocupado = true;
    try {
      if (!actual) siguiente();
      if (!actual) { estado('Todavía no hay música disponible'); return; }
      await audio.play();
      fallos = 0;
      estado();
      guardar();
    } catch { estado('Pulsa el logo para continuar la música'); }
    finally { ocupado = false; }
  };
  try {
    const previo = JSON.parse(sessionStorage.getItem(clave) || 'null');
    if (previo && pistas.includes(previo.actual)) {
      actual = previo.actual;
      cola = Array.isArray(previo.cola) ? [...new Set<string>(previo.cola.filter((p: string) => pistas.includes(p)))] : [];
      const tiempo = Number.isFinite(previo.tiempo) ? Math.max(0, previo.tiempo) : 0;
      reanudar = previo.sonando === true;
      audio.src = actual;
      audio.addEventListener('loadedmetadata', () => {
        if (Number.isFinite(audio.duration) && tiempo < audio.duration) audio.currentTime = tiempo;
      }, { once: true });
    }
  } catch {}
  document.addEventListener('click', (evento) => {
    if (!(evento.target instanceof Element) || !evento.target.closest('[data-musica-nebula] button')) return;
    if (!audio.paused) { audio.pause(); guardar(); }
    else void reproducir();
  });
  document.addEventListener('astro:page-load', () => {
    raiz = document.querySelector<HTMLElement>('[data-musica-nebula]');
    if (!raiz) return;
    boton = raiz.querySelector<HTMLButtonElement>('button')!;
    aviso = raiz.querySelector<HTMLParagraphElement>('p')!;
    estado();
  });
  audio.addEventListener('play', () => estado());
  audio.addEventListener('pause', () => estado());
  audio.addEventListener('ended', () => { siguiente(); void reproducir(); });
  audio.addEventListener('error', () => {
    fallos++;
    estado('No se pudo cargar la pista. Pulsa para probar otra');
    if (fallos < pistas.length) { siguiente(); }
    else { actual = ''; cola = []; }
    guardar();
  });
  let ultimoGuardado = 0;
  audio.addEventListener('timeupdate', () => {
    if (Date.now() - ultimoGuardado > 3000) { guardar(); ultimoGuardado = Date.now(); }
  });
  window.addEventListener('pagehide', guardar);
  document.addEventListener('visibilitychange', () => { if (document.hidden) guardar(); });
  estado();
  if (reanudar) void reproducir();
}
