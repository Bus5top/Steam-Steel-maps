# Hosting on Vercel — notes

If you saw a 404 from Vercel (like the screenshot you provided), it usually means Vercel had no `index.html` or build output to serve at the site root. I added a minimal `index.html` and `vercel.json` to make the repo deployable as a static site.

Quick deploy (CLI):

```bash
npm i -g vercel
vercel login
vercel --prod
```

Notes and troubleshooting:
- Ensure `index.html` is in the repository root (the file we added).
- `vercel.json` in the repo root configures routing; it maps `/data/*` to the `data/` files and everything else to `index.html`.
- Make sure `data/steam_steel_maps.json` is present and not ignored; Vercel will deploy files committed to the repo.
- If you use the Vercel dashboard, connect this repo and trigger a deploy. Check the deployment logs for errors.

If you want, I can set up a simple GitHub Action that auto-deploys to Vercel or help push the changes and walk through the dashboard deploy.
