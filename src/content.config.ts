import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const articulos = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/articulos' }),
  schema: z.object({
    titulo: z.string(),
    descripcion: z.string(),
    tema: z.string(),
    fecha: z.date(),
    cifraDestacada: z.string().optional(),
    etiquetaCifra: z.string().optional(),
    metodologia: z.string().optional(),
    imagenPortada: z.string().optional(),
  }),
});

export const collections = { articulos };
