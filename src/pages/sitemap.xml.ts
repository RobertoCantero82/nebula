import type { APIRoute } from 'astro';
import { getCollection } from 'astro:content';

const escaparXml = (valor: string) =>
  valor.replace(/[<>&'\"]/g, (caracter) => ({
    '<': '&lt;',
    '>': '&gt;',
    '&': '&amp;',
    "'": '&apos;',
    '"': '&quot;',
  })[caracter] ?? caracter);

export const GET: APIRoute = async ({ site }) => {
  const origen = site ?? new URL('https://robertocantero82.github.io');
  const base = new URL('/nebula/', origen);
  const articulos = await getCollection('articulos');
  const paginas = [
    { url: base.href },
    { url: new URL('trabaja-conmigo/', base).href },
    ...articulos.map((articulo) => ({
      url: new URL(`articulos/${articulo.id}/`, base).href,
      fecha: articulo.data.fecha.toISOString().slice(0, 10),
    })),
  ];

  const urls = paginas.map(({ url, fecha }) => `
  <url>
    <loc>${escaparXml(url)}</loc>${fecha ? `\n    <lastmod>${fecha}</lastmod>` : ''}
  </url>`).join('');

  return new Response(
    `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">${urls}\n</urlset>\n`,
    { headers: { 'Content-Type': 'application/xml; charset=utf-8' } },
  );
};
