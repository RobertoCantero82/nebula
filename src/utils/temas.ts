export const temas = [
  { clave: 'tecnologia', nombre: 'Tecnología', descripcion: 'Inteligencia artificial, dispositivos y el mundo digital.' },
  { clave: 'ciencia', nombre: 'Ciencia', descripcion: 'Espacio, naturaleza e investigación.' },
  { clave: 'extra', nombre: 'Extra', descripcion: 'Cine, series, cultura y otras historias sorprendentes.' },
  { clave: 'hazlo-facil', nombre: 'Hazlo fácil', descripcion: 'Trucos, tutoriales y pequeñas soluciones para tu día a día.' },
];

// agrupo las publicaciones y conservo sus categorías y enlaces originales
export function temaPrincipal(data: { tema?: string; categoria?: string; serie?: string }): string {
  if (data.serie === 'trama') return 'extra';
  const tema = (data.categoria || data.tema || '').normalize('NFD').replace(/[\u0300-\u036f]/g, '').trim().toLowerCase();
  if (/^hazlo[- ]facil$/.test(tema)) return 'hazlo-facil';
  if (/tecnologia|inteligencia artificial|^ia$|robotica|software/.test(tema)) return 'tecnologia';
  if (/ciencia|biodiversidad|biologia|espacio|fisica|naturaleza/.test(tema)) return 'ciencia';
  return 'extra';
}

export function nombreCategoria(categoria: string): string {
  return temas.find(tema => tema.clave === temaPrincipal({ categoria }))?.nombre ?? 'Extra';
}
