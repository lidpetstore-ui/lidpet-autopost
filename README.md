# Lidpet Auto Post

2 dial l'merrat f nhar (14:00 w 00:00 UTC) katakhod l'post jay men `posts/`, kat9ad les creatives, w katposti:

| Plateforme | Chno katposti |
|---|---|
| Instagram | Carousel (ga3 les tsawer) + Reel (vidéo) |
| Facebook | Post b les tsawer + vidéo |
| Pinterest | Pin (2:3) b lien l'produit |
| TikTok | Vidéo (k **draft** f TikTok: nta tclicki Post men l'app) |

## Kifach tzid post jdid
1. Dir dossier jdid f `posts/` (masalan `posts/11/`) w 7et fih les tsawer.
2. Copier `post.json` men chi post a5or w beddel: smiya, prix, lien, text dyal vidéo, captions.
3. Push l GitHub. L'automation kat9ad `ready/11/` bou7dha w katposti fih f nobto.

## post.json
- `product`, `short_name`, `price`, `url` – dyal l'produit f store
- `headline` – 2 dial ster l Pinterest
- `mockups` – tsawer dyal les couleurs (l Pinterest w vidéo)
- `video.scenes` – kol scene: `image`, `top` (text fo9), `bottom` (text lta7t), `highlight` (kelmat b gold), `seconds`
- `caption` – Instagram + Facebook
- `tiktok_caption`, `pin_title`, `pin_description`
- `skip_images` – tsawer ma khasshomch ytposṭaw (masalan ila fihom brand a5or)

## Secrets (GitHub > Settings > Secrets and variables > Actions)
Kol plateforme katkhdem ghir ila zedti les secrets dyalha:

| Plateforme | Secrets |
|---|---|
| Instagram + Facebook | `PAGE_ACCESS_TOKEN`, `FB_PAGE_ID`, `IG_USER_ID` (nefs li f automation l9dima) |
| Pinterest | `PINTEREST_APP_ID`, `PINTEREST_APP_SECRET`, `PINTEREST_REFRESH_TOKEN`, `PINTEREST_BOARD_ID` |
| TikTok | `TIKTOK_CLIENT_KEY`, `TIKTOK_CLIENT_SECRET`, `TIKTOK_REFRESH_TOKEN` |

## Tjriba
Actions > Lidpet Auto Post > Run workflow > dry_run = 1 (walo ma kaytposta).

## Mla7adat
- Repo khasso ykoun **Public** (Instagram/Facebook/Pinterest kayjbdo les tsawer men raw.githubusercontent.com).
- TikTok: bla app mvalidiya men TikTok, l'vidéo katwsel k draft (inbox). Mli TikTok yvalidi l'app, beddel `TIKTOK_MODE` l `direct`.
- Ila plateforme fshlat, run jay kay3awed ghir hiya (status f `posts/<n>/status.json`).
- Mli kaykmlo ga3 les posts, kayrj3o men `done/` w kaybdaw men l'awal.
- Fonts: Poppins (OFL, `assets/fonts/OFL.txt`).
