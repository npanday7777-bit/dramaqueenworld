# Drama Queen World 👑

A private, personalized "why you should love/tolerate me" website — one
secret link per person, soft pastel aesthetic, flip cards, a talking
character, and a sticker carousel at the end.

## How to run this in VS Code

1. Open this folder in VS Code (`File > Open Folder`).
2. Open a terminal (`` Ctrl + ` ``).
3. (Optional) create a virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # Mac/Linux
   ```
4. Install Flask:
   ```
   pip install -r requirements.txt
   ```
5. Run the app:
   ```
   python app.py
   ```
6. Look at your terminal — it prints a **personal link for every person**, like:
   ```
   Mom             http://127.0.0.1:5000/world/mom-glow99
   Dad             http://127.0.0.1:5000/world/dad-legend77
   ```

Right now these only work on your own laptop (`127.0.0.1` = your machine).
To actually send links to people, you'll need to deploy it — ask me when
you're ready and I'll walk you through a free option (Render, Railway, etc.).

## How the privacy actually works

- Every person in `PEOPLE` (inside `app.py`) has a unique `token`.
- Their link is `/world/<their-token>`.
- The page only ever sends **that person's own card content** from the
  server — other people's cards are never included in the page source,
  so there's nothing to "peek" at even by opening dev tools.
- If someone clicks a menu tile that isn't theirs, the funny gatekeeper
  character pops up. If someone tries a random/wrong link entirely, they
  land on the generic locked page.

## How to personalize everything

Open `app.py` and edit the `PEOPLE` dictionary:

- `display_name`, `emoji`, `cheer_lines` — what shows/plays when they click their own tile (uses the browser's built-in voice, so no audio files needed).
- `gate_title` — the header shown once they're "in."
- `cards` — each card has a `title`, `emoji`, and `content`.
  - Cards with `"type": "list"` show a bullet list + stickers on the flip side (already pre-written with generic humor — tweak if you want).
  - Cards with `"type": "text"` are the emotional ones. Look for **[bracketed prompts]** — replace those with the real thing, in your own words. I'm happy to help you write these anytime — just tell me who it's for and I'll draft it in your POV.

To add or remove a relationship (e.g. best friend, cousin), copy one of the
existing blocks in `PEOPLE` and give it a new key + a new unique token.

## Deploying it so phones can open it (Android + iPhone both work the same way — it's just a website)

Right now the links only work on your own laptop. To get a real link you can send
in WhatsApp/Instagram, you need to put the code online. Free option: **Render**.

1. **Put your code on GitHub** (if you haven't already):
   - Go to github.com, make a free account if needed.
   - Create a new repository (e.g. `drama-queen-world`).
   - Upload this whole folder to it (GitHub's website lets you drag-and-drop files,
     or use `git` from the VS Code terminal if you're comfortable with that).

2. **Go to render.com** → sign up free → **New + → Web Service**.

3. Connect your GitHub repo when it asks.

4. Render will auto-detect it's a Python app. Set:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app` (already in the `Procfile`, Render usually picks it up automatically)

5. Click **Deploy**. Wait a couple minutes. You'll get a link like:
   ```
   https://drama-queen-world.onrender.com
   ```

6. Your personal links now become:
   ```
   https://drama-queen-world.onrender.com/world/mom-glow99
   https://drama-queen-world.onrender.com/world/dad-legend77
   ```
   Same tokens, just a real domain instead of `127.0.0.1:5000`.

7. Send each person **only their own link**. Any phone, any browser, works instantly.

**Note:** Render's free tier "sleeps" the app after inactivity — the first person to
open a link after a while might wait ~30 seconds for it to wake up. That's normal
and just a free-tier thing, not a bug.

## Adding the song

Open `templates/world.html`, find the `song-embed-box` div, and paste a
YouTube (or other) embed iframe where the comment tells you to. Example:
```html
<iframe width="100%" height="200" src="https://www.youtube.com/embed/VIDEO_ID"
        frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
```

## Editing the sticker carousel

Also in `app.py` — the `LOVE_STICKERS` list. Add as many "I love you, but
make it weird" lines as you want; they'll cycle through automatically.
