document.addEventListener('astro:before-swap', (evento: Event) => {
  const nueva = (evento as Event & { newDocument: Document }).newDocument;
  for (const script of nueva.querySelectorAll<HTMLScriptElement>('script:not([src])')) {
    if (script.type && !['text/javascript', 'application/javascript'].includes(script.type)) continue;
    if (!script.textContent?.trim()) continue;
    // conservo los gráficos antiguos sin modificar los artículos guardados.
    script.setAttribute('data-astro-rerun', '');
    const codigo = script.textContent.replace(/(?:document|window)\.addEventListener\(\s*(['"])DOMContentLoaded\1\s*,\s*/g, 'alContenidoListo(');
    script.textContent = `(() => { const alContenidoListo = (fn, opciones) => document.addEventListener('astro:page-load', fn, { once: true });\n${codigo}\n})();`;
  }
  const graficos = (window as any).Chart;
  if (graficos?.instances) Object.values(graficos.instances).forEach((grafico: any) => grafico.destroy());
});
