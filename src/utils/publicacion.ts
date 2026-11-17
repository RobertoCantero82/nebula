const zona = 'Europe/Madrid';
const reloj = new Intl.DateTimeFormat('en-GB', {
  timeZone: zona, year: 'numeric', month: '2-digit', day: '2-digit',
  hour: '2-digit', minute: '2-digit', second: '2-digit', hourCycle: 'h23',
});

export function fechaPublicacion(datos: { fecha: Date; hora?: string }): Date {
  if (!datos.hora) return datos.fecha;
  const dia = datos.fecha.toISOString().slice(0, 10);
  const destino = new Date(`${dia}T${datos.hora}:00Z`).getTime();
  let instante = destino;
  for (let intento = 0; intento < 3; intento++) {
    const partes = Object.fromEntries(reloj.formatToParts(instante).map(p => [p.type, p.value]));
    const local = Date.UTC(+partes.year, +partes.month - 1, +partes.day,
      +partes.hour, +partes.minute, +partes.second);
    const diferencia = local - destino;
    if (diferencia === 0) return new Date(instante);
    instante -= diferencia;
  }
  throw new Error(`Hora de publicación no válida en ${zona}: ${dia} ${datos.hora}`);
}

export function estaPublicada(datos: { fecha: Date; hora?: string }, ahora = new Date()): boolean {
  return fechaPublicacion(datos).getTime() <= ahora.getTime();
}
