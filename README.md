# Akyl — how to put it online

Akyl is a single file (`index.html`). There's no server and no accounts. The host's browser runs the game, and players' phones connect to it directly.

## 1. Put it on the web (free, about 2 minutes)

Phones need a real web address to scan, so the file has to be hosted. Either option works:

**Netlify Drop (easiest)**
1. Put `index.html` in a folder on your computer.
2. Go to https://app.netlify.com/drop and drag the folder onto the page.
3. You get a link like `https://something.netlify.app`. Create a free account to keep it permanently.

**GitHub Pages**
1. Create a public repository and upload `index.html`.
2. Go to Settings → Pages, choose the `main` branch, and save.
3. Your site will be at `https://<your-username>.github.io/<repo>/`.

## 2. Run a game

1. Open your link on the computer connected to the projector or TV.
2. Click **Open quiz editor**, write your questions, mark the correct answer, and set a time limit for each.
3. Click **Host this quiz ▶**. The screen shows a 6-digit PIN and a QR code.
4. Players scan the QR code, or open the same link and type the PIN. Then they choose a nickname.
5. Click **Start**. Each question shows on the big screen, and players tap a colored button on their phone.
6. After each question you'll see the answer chart, then the scoreboard. At the end, a podium appears and you can download the results as a CSV file.

## Good to know

- **Keep the host tab open and visible.** If it closes, the game ends. Players who briefly lose connection rejoin automatically and keep their score.
- **Scoring:** a correct answer earns up to 1000 points (faster answers earn more), plus a streak bonus of up to +500 for several correct answers in a row.
- **Your quizzes are saved in this browser.** Use **Export** to back them up or move them to another computer, and **Import** to load them.
- Tap a player's name in the lobby to remove them.
- Opening the file directly from your computer (`file://`) works for trying out the editor, but phones can't use the QR code until the file is hosted.
- Phones and the host connect through a free public message relay over a normal secure web connection, so it works on Wi-Fi, mobile data, and hotspots. An internet connection is required.
- The relay is public, so don't put private or sensitive information in quiz questions.

## Daily question sets

Every day gets a new set of 45 questions (23 logic, 9 general, 9 math, 4 science; 23 in Kyrgyz and 22 in Russian), named by its date, for example "November 6".

- The site loads new sets automatically. They appear at the top of the quiz editor's dropdown under **📅 Daily sets**, newest first, and the newest one is selected.
- To add a set, write `tools/sources/YYYY-MM-DD.json` (see `tools/sources/2026-11-06.json` for the format), then run `python3 tools/make_set.py tools/sources/YYYY-MM-DD.json`. The script checks the mix and that no question repeats an earlier set, shuffles the order and the answer positions, and writes `sets/YYYY-MM-DD.json` and `sets/index.json`. Push to `main` and the site updates.
