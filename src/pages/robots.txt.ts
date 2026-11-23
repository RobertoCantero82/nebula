import type { APIRoute } from 'astro';

export const GET: APIRoute = ({ site }) => {
  const origen = site ?? new URL('https://diarionebula.es');
  const sitemap = new URL('/sitemap.xml', origen);

  return new Response(`User-agent: *\nAllow: /\n\nSitemap: ${sitemap.href}\n`, {
    headers: { 'Content-Type': 'text/plain; charset=utf-8' },
  });
};
