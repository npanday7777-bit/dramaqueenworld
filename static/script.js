// ============================================================
// Drama Queen World — front-end logic
// ============================================================

const unlockedSlug = window.UNLOCKED_SLUG;
const cheerLines = window.CHEER_LINES || [];
const gateLines = window.GATE_LINES || [];
const loveStickers = window.LOVE_STICKERS || [];

// ---------- Helpers ----------
function randomFrom(arr) {
  return arr[Math.floor(Math.random() * arr.length)];
}

function speak(text) {
  try {
    if (!("speechSynthesis" in window)) return;
    const utter = new SpeechSynthesisUtterance(text);
    utter.pitch = 1.3;
    utter.rate = 1.05;
    window.speechSynthesis.cancel(); // stop any previous line
    window.speechSynthesis.speak(utter);
  } catch (err) {
    // Some phone browsers (in-app browsers especially) don't support this.
    // Silently skip the voice — it's a bonus, not required for the page to work.
  }
}

// ---------- Menu tile clicks ----------
const cheerModal = document.getElementById("cheer-modal");
const cheerText = document.getElementById("cheer-text");
const cheerContinue = document.getElementById("cheer-continue");

const gateModal = document.getElementById("gate-modal");
const gateText = document.getElementById("gate-text");
const gateClose = document.getElementById("gate-close");

document.querySelectorAll(".menu-tile").forEach(tile => {
  tile.addEventListener("click", () => {
    const slug = tile.dataset.slug;

    if (slug === unlockedSlug) {
      const line = randomFrom(cheerLines);
      cheerText.textContent = line;
      cheerModal.classList.remove("hidden");
      speak(line);
    } else {
      gateText.textContent = randomFrom(gateLines);
      gateModal.classList.remove("hidden");
    }
  });
});

cheerContinue.addEventListener("click", () => {
  cheerModal.classList.add("hidden");

  // Some phone browsers (especially in-app browsers like WhatsApp/Instagram)
  // don't fully support speechSynthesis. Guard this so it can never block
  // the rest of the reveal below.
  try {
    if ("speechSynthesis" in window) {
      window.speechSynthesis.cancel();
    }
  } catch (err) {
    // ignore — not critical, the reveal must still happen
  }

  // Reveal the rest of the experience
  ["cards-section", "song-section", "final-section"].forEach(id => {
    const el = document.getElementById(id);
    if (el) el.classList.remove("hidden");
  });

  const cardsSection = document.getElementById("cards-section");
  if (cardsSection) cardsSection.scrollIntoView({ behavior: "smooth" });
});

gateClose.addEventListener("click", () => {
  gateModal.classList.add("hidden");
});

// ---------- Flip cards ----------
document.querySelectorAll(".flip-card").forEach(card => {
  card.addEventListener("click", () => {
    card.classList.toggle("flipped");
  });
});

// ---------- Sticker carousel ----------
let stickerIndex = 0;
const stickerDisplay = document.getElementById("sticker-display");
const prevBtn = document.getElementById("prev-sticker");
const nextBtn = document.getElementById("next-sticker");

function renderSticker() {
  if (!loveStickers.length) return;
  stickerDisplay.textContent = loveStickers[stickerIndex];
}

if (prevBtn && nextBtn) {
  prevBtn.addEventListener("click", () => {
    stickerIndex = (stickerIndex - 1 + loveStickers.length) % loveStickers.length;
    renderSticker();
  });

  nextBtn.addEventListener("click", () => {
    stickerIndex = (stickerIndex + 1) % loveStickers.length;
    renderSticker();
  });

  renderSticker();
}
