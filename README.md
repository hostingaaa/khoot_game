# Brightpin — how to put it online

Brightpin is a single file (`index.html`). There's no server and no accounts. The host's browser runs the game, and players' phones connect to it directly.

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
- Connections go through the free PeerJS service, and the internet is required. On very strict networks (some corporate or school Wi-Fi), a phone may fail to connect. Switching that phone to mobile data usually fixes it.
