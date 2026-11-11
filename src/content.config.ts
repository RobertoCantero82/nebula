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
    textoContinuo: z.string().min(1),
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
    descripcion: z.string(),
    categoria: z.enum(['tecnologia', 'ciencia', 'cine', 'cultura']),
    fecha: z.date(),
    hora: z.string().regex(/^([01]\d|2[0-3]):[0-5]\d$/).optional(),
    cifraDestacada: z.string().optional(),
    etiquetaCifra: z.string().optional(),
    fondoPortada: z.string().optional(),
    mostrarCifraInterior: z.boolean().optional(),
    pantallas: z.array(z.object({
      etiqueta: z.string(),
      titulo: z.string(),
      texto: z.array(z.string()).min(1),
      tipo: z.enum(['recorrido', 'linea', 'lista', 'hospital', 'contraste', 'cierre']),
      datos: z.array(z.string()).optional(),
    })).length(5),
    fuentes: z.array(z.object({
      nombre: z.string(),
      url: z.string().url(),
      detalle: z.string().optional(),
    })).min(1),
  }),
});

export const collections = { articulos, actualidad };
