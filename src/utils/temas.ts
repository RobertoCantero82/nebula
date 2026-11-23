export const temas = [
  { clave: 'tecnologia', nombre: 'Tecnología', descripcion: 'Inteligencia artificial, dispositivos y el mundo digital.' },
  { clave: 'ciencia', nombre: 'Ciencia', descripcion: 'Espacio, naturaleza e investigación.' },
  { clave: 'cine', nombre: 'Cine', descripcion: 'Películas, series e historias de la pantalla.' },
  { clave: 'extra', nombre: 'Extra', descripcion: 'Cultura, deporte y otras historias.' },
];

// agrupo los temas existentes sin modificar las etiquetas originales
export function temaPrincipal(data: { tema?: string; categoria?: string; serie?: string }): string {
  if (data.serie === 'trama') return 'cine';
  const tema = (data.categoria || data.tema || '').normalize('NFD').replace(/[\u0300-\u036f]/g, '').trim().toLowerCase();
  if (/tecnologia|inteligencia artificial|^ia$|robotica|software/.test(tema)) return 'tecnologia';
  if (/ciencia|biodiversidad|biologia|espacio|fisica|naturaleza/.test(tema)) return 'ciencia';
  if (/cine|series|audiovisual/.test(tema)) return 'cine';
  return 'extra';
}
