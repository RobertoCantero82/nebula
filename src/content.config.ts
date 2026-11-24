import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const articulos = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/articulos' }),
  schema: z.object({
    titulo: z.string(),
    descripcion: z.string(),
    tema: z.string(),
    fecha: z.date(),
    serie: z.enum(['trama']).optional(),
    cifraDestacada: z.string().optional(),
    etiquetaCifra: z.string().optional(),
    metodologia: z.string().optional(),
    imagenPortada: z.string().optional(),
    reconocimiento: z.object({
      etiqueta: z.string(),
      detalle: z.string(),
    }).optional(),
  }),
});

const actualidad = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/actualidad' }),
  schema: z.object({
    titulo: z.string(),
    palabraDestacada: z.string().trim().optional(),
    descripcion: z.string(),
    categoria: z.enum(['tecnologia', 'ciencia', 'cine', 'cultura', 'extra']),
    fecha: z.date(),
    hora: z.string().regex(/^([01]\d|2[0-3]):[0-5]\d$/).optional(),
    cifraDestacada: z.string().optional(),
    etiquetaCifra: z.string().optional(),
    fondoPortada: z.string().optional(),
    mostrarCifraInterior: z.boolean().optional(),
    formato: z.enum(['base', 'visual']).optional(),
    pantallas: z.array(z.object({
      etiqueta: z.string(),
      titulo: z.string(),
      texto: z.array(z.string()).min(1),
      tipo: z.enum(['recorrido', 'linea', 'lista', 'hospital', 'contraste', 'cierre', 'secuencia-iconos', 'secuencia-xpeng', 'secuencia-hueso', 'secuencia-gameboy', 'imagen-cine', 'video-youtube', 'video-x', 'interactivo-cine', 'interactivo-xpeng', 'interactivo-datos', 'grafico-tiempo', 'grafico-alcance', 'grafico-comparacion']),
      datos: z.array(z.string()).optional(),
      respuestas: z.array(z.string()).optional(),
      imagen: z.string().optional(),
      altImagen: z.string().optional(),
      pieImagen: z.string().optional(),
      videoXId: z.string().regex(/^\d{15,22}$/).optional(),
      videoId: z.string().regex(/^[A-Za-z0-9_-]{11}$/).optional(),
      videoIdiomaSubtitulos: z.string().regex(/^[a-z]{2}$/).optional(),
    })).length(5),
    fuentes: z.array(z.object({
      nombre: z.string(),
      url: z.string().url(),
      detalle: z.string().optional(),
    })).min(1),
  }),
});

export const collections = { articulos, actualidad };
