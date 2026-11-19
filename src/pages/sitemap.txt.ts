import type { APIRoute } from 'astro';
import { GET as generarSitemapXml } from './sitemap.xml';

export const prerender = true;

// reutilizo el sitemap principal para conservar las mismas rutas y fechas de publicación
export const GET: APIRoute = async (contexto) => {
  const respuesta = await generarSitemapXml(contexto);
  if (!respuesta.ok) throw new Error('No he podido generar el sitemap principal.');

  const xml = await respuesta.text();
  const entidades: Record<string, string> = {
    amp: '&', lt: '<', gt: '>', quot: '"', apos: "'",
  };
  const urls = Array.from(xml.matchAll(/<loc>([^<]+)<\/loc>/g), ([, url]) =>
    url.replace(/&(amp|lt|gt|quot|apos);/g, (_, entidad: string) => entidades[entidad])
  );
  if (urls.length === 0) throw new Error('El sitemap principal no contiene direcciones.');

  return new Response(`${urls.join('\n')}\n`, {
    headers: { 'Content-Type': 'text/plain; charset=utf-8' },
  });
};
