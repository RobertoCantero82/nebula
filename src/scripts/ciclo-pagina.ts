export function alCargarPagina(preparar: (escuchar: Function, alSalir: Function) => void) {
  let limpiar = () => {};
  document.addEventListener('astro:before-swap', () => limpiar());
  document.addEventListener('astro:page-load', () => {
    limpiar();
    const controlador = new AbortController();
    const tareas: Array<() => void> = [];
    const escuchar = (destino: EventTarget, nombre: string, funcion: EventListener, opciones: AddEventListenerOptions = {}) => {
      destino.addEventListener(nombre, funcion, { ...opciones, signal: controlador.signal });
    };
    limpiar = () => { controlador.abort(); tareas.splice(0).forEach(tarea => tarea()); };
    preparar(escuchar, (tarea: () => void) => tareas.push(tarea));
  });
}
