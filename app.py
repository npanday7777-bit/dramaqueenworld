from flask import Flask, render_template, abort

app = Flask(__name__)

# =====================================================================
#  DRAMA QUEEN WORLD — main data file
#  Everything you want to personalize lives in the PEOPLE dict below.
#  Each person has their own secret "token" — that's what makes their
#  link private. Nobody can guess mom's page from dad's link.
# =====================================================================

# ---- Generic funny "buy me chocolate" reasons (edit freely) ----
CHOCOLATE_REASONS = [
    "Scientifically, chocolate = serotonin. You want me happy, right?",
    "I have supported you emotionally for years. This is a subscription renewal.",
    "It's not a want. It's basic human rights at this point.",
    "Cheaper than therapy. You're welcome.",
    "I said please. In my head. Very loudly.",
]
CHOCOLATE_STICKERS = ["🍫", "😋", "💅", "✨", "🙏"]

# ---- Generic "I love you, but make it weird" sticker carousel (edit freely) ----
LOVE_STICKERS = [
    "You're stuck with me. Forever. Sorry not sorry. 💗",
    "Consider this a permanent, unskippable hug. 🤗",
    "10/10 would choose you again in every timeline. 🌸",
    "Warning: contains unconditional love. Side effects include being adored.",
    "This is legally binding affection. No refunds.",
]

# Real, personalized content. Each person's "nickname" shows up in their
# greeting so it feels like it's addressed to them specifically.
PEOPLE = {
    "mom": {
        "token": "mom-glow99",
        "display_name": "Mom",
        "nickname": "Billo Rani",
        "emoji": "👑",
        "cheer_lines": [
            "Billo Rani has entered the building — everyone bow!",
            "The queen mother approaches, make way!",
        ],
        "gate_title": "Welcome, Billo Rani 👑",
"song_url": "https://youtu.be/mfNnCKMx-tk",
        "cards": [
            {"title": "Why You Should Buy Me Chocolate", "emoji": "🍫",
             "type": "text", "stickers": CHOCOLATE_STICKERS,
             "content": "Billo Rani, you started this chocolate economy when I was still learning to walk. You'd hand me one after school like it was a salary. Now I've grown up, my sweet tooth hasn't — so technically, you owe me a lifetime subscription."},
            {"title": "Why You're Blessed To Have Me", "emoji": "🌟",
             "type": "text",
             "content": "Because before I had friends, I had you. Before I had \"everything figured out,\" I had you pretending like you did. You're not just my mother, you're my only best friend — and honestly, who else is going to argue with you and miss you in the same breath?"},
            {"title": "Why I Love You", "emoji": "💗",
             "type": "text",
             "content": "You used to kiss my forehead before waking me up, like it was the most normal thing in the world. It wasn't. I just didn't know that yet. That's why I love you — you made ordinary mornings feel safe."},
            {"title": "Top Secret Confession", "emoji": "🤫",
             "type": "text",
             "content": "I never told you I noticed when the forehead kisses stopped. I never asked you to bring them back either. But some mornings I still wait for them without meaning to."},
            {"title": "The Memory I Replay", "emoji": "🎞️",
             "type": "text",
             "content": "You, waking me up with a kiss on my forehead. Me, pretending to still be asleep for two more seconds just so it would last a little longer."},
        ],
    },
    "dad": {
        "token": "dad-legend77",
        "display_name": "Dad",
        "nickname": "Pitashree",
        "emoji": "🛡️",
        "cheer_lines": [
            "Pitashree in the house! Someone hide the receipts!",
            "The legend, the myth, the man who always finds a way — Pitashree!",
        ],
        "gate_title": "Welcome, Pitashree 🛡️",
 "song_url": "https://youtu.be/KhnVcAC5bIM",

        "cards": [
            {"title": "Why You Should Buy Me Chocolate", "emoji": "🍫",
             "type": "text", "stickers": CHOCOLATE_STICKERS,
             "content": "If he can, he will. That's it. That's the whole pitch. Pitashree, chocolate is cheaper than the fights we have now, just saying."},
            {"title": "Why You're Blessed To Have Me", "emoji": "🌟",
             "type": "text",
             "content": "Because I'm the only one who can rage-bait him and still come back for dosa afterward. Not everyone gets a daughter who fights AND forgives in the same evening."},
            {"title": "Why I Love You", "emoji": "💗",
             "type": "text",
             "content": "You took me to your office when I was small, just so I could sit around and feel important. You came to my karate match, watched me fight, and then had to leave right before I got my medal — because that's what showing up sometimes looks like, imperfect and real. And after all that, you still took me to my favourite restaurant for dosa with the ₹500 you had left. That's the whole story of you, honestly — always finding a way."},
            {"title": "Top Secret Confession", "emoji": "🤫",
             "type": "text",
             "content": "I wish our rage-baiting was still just baiting. I miss when it was funny and not real. I don't say that out loud, but I mean it."},
            {"title": "The Memory I Replay", "emoji": "🎞️",
             "type": "text",
             "content": "Sitting across from you at that dosa place, both of us pretending ₹500 was more money than it was."},
        ],
    },
    "brother": {
        "token": "bro-menace42",
        "display_name": "Brother",
        "nickname": "Duggu",
        "emoji": "🎮",
        "cheer_lines": [
            "DUGGU ALERT. The house just got ten times louder.",
            "It's the chaos gremlin himself — Duggu has logged in!",
        ],
       "gate_title": "Welcome, Duggu 🎮",
"song_url": "https://youtu.be/II2EO3Nw4m0",
        "cards": [
            {"title": "Why You Should Buy Me Chocolate", "emoji": "🍫",
             "type": "text", "stickers": CHOCOLATE_STICKERS,
             "content": "Because every playful hit I've given you deserves a chocolate as compensation, Duggu. Consider it a peace offering system."},
            {"title": "Why You're Blessed To Have Me", "emoji": "🌟",
             "type": "text",
             "content": "Because who else is going to fight you over the smallest things AND be the loudest when you walk through the door?"},
            {"title": "Why I Love You", "emoji": "💗",
             "type": "text",
             "content": "I remember how happy I'd get when you came home from Nani's ghar, even if it was just for a few days. That happiness hasn't changed, Duggu. It just doesn't show up as loudly anymore."},
            {"title": "Top Secret Confession", "emoji": "🤫",
             "type": "text",
             "content": "I miss the version of us that fought over toys instead of everything else. Some days I want to go back to that."},
            {"title": "The Memory I Replay", "emoji": "🎞️",
             "type": "text",
             "content": "You walking in after being at Nani's ghar, and me acting like the whole house got brighter — because it did."},
        ],
    },
    "special": {
        "token": "special-onlyone22",
        "display_name": "Best Friend",
        "nickname": "RED",
        "emoji": "💫",
        "cheer_lines": [
            "It's RED! My person, online and in real life!",
            "Camera's on, heart's fuller — RED has arrived!",
        ],
     "gate_title": "Welcome, RED 💫",
"song_url": "https://youtu.be/UDHklYvDkv8",
        "cards": [
            {"title": "Why You Should Buy Me Chocolate", "emoji": "🍫",
             "type": "text", "stickers": CHOCOLATE_STICKERS,
             "content": "You kept me waiting more times than I can count, RED. I'm billing you in chocolate, with interest."},
            {"title": "Why You're Blessed To Have Me", "emoji": "🌟",
             "type": "text",
             "content": "Because I'm the only person you can talk to about everything or nothing and somehow both feel like a full conversation."},
            {"title": "Why I Love You", "emoji": "💗",
             "type": "text",
             "content": "Long distance means I only get you through a screen, but you keep your camera on anyway. That's not a small thing. That's you choosing to actually be there."},
            {"title": "Top Secret Confession", "emoji": "🤫",
             "type": "text",
             "content": "You didn't tell me you got the job in Delhi. I found out some other way, and it stung more than I let on. I'm not over it, RED. Just saying."},
            {"title": "The Memory I Replay", "emoji": "🎞️",
             "type": "text",
             "content": "Video calls that were about nothing — just your face on screen and both of us talking till there was nothing left to say, and staying on the call anyway."},
        ],
    },
    "author_friends": {
        "token": "authors-quillsquad",
        "display_name": "Author Friend",
        "nickname": "Butterfly",
        "emoji": "🦋",
        "cheer_lines": [
            "BUTTERFLY is here — cancel whatever you were doing, we're talking for two hours now.",
            "The co-conspirator of every game night has arrived!",
        ],
        "gate_title": "Welcome, Butterfly 🦋",
"song_url": "https://youtu.be/AGsn2ycFRqI",
        "cards": [
            {"title": "Why You Should Buy Me Chocolate", "emoji": "🍫",
             "type": "text", "stickers": CHOCOLATE_STICKERS,
             "content": "Every time we say \"let's play a quick game,\" we end up talking for two hours instead. That's a chocolate tax, Butterfly."},
            {"title": "Why You're Blessed To Have Me", "emoji": "🌟",
             "type": "text",
             "content": "Because I'm the friend who'll derail game night into a three-hour conversation and somehow you never complain."},
            {"title": "Why I Love You", "emoji": "💗",
             "type": "text",
             "content": "You stay by my side even on the bad writing days, the bad everything days. You keep telling me to keep writing when I want to quit. That kind of support doesn't come easy, and you give it anyway."},
            {"title": "Top Secret Confession", "emoji": "🤫",
             "type": "text",
             "content": "Some days your encouragement is the only reason I open my draft at all. I don't say it enough."},
            {"title": "The Memory I Replay", "emoji": "🎞️",
             "type": "text",
             "content": "Us trying to start a game, failing immediately, and ending up in a two-hour conversation about something completely unrelated — again."},
        ],
    },
    "online_friends": {
        "token": "online-latenightcalls",
        "display_name": "Online Friend",
        "nickname": "Cupcakes",
        "emoji": "🧁",
        "cheer_lines": [
            "CUPCAKES in the chat — brace for chaos and flirting.",
            "The group chat's certified troublemaker has arrived!",
        ],
        "gate_title": "Welcome, Cupcakes 🧁",
"song_url": "https://youtu.be/jmpUP1MaQ9Q",
        "cards": [
            {"title": "Why You Should Buy Me Chocolate", "emoji": "🍫",
             "type": "text", "stickers": CHOCOLATE_STICKERS,
             "content": "For all the flirting you started in the group chat and then left me to deal with the consequences of, Cupcakes. Chocolate is the least you owe me."},
            {"title": "Why You're Blessed To Have Me", "emoji": "🌟",
             "type": "text",
             "content": "Because I'm the only one who flirts back in the group chat with zero shame and full commitment."},
            {"title": "Why I Love You", "emoji": "💗",
             "type": "text",
             "content": "You were there on the day I got my heart broken. Not with a speech, just there — and sometimes that's the only thing that actually helps."},
            {"title": "Top Secret Confession", "emoji": "🤫",
             "type": "text",
             "content": "Half our flirting in that group chat isn't even a joke to me anymore, Cupcakes."},
            {"title": "The Memory I Replay", "emoji": "🎞️",
             "type": "text",
             "content": "That heartbreak day, and you just... staying. No advice, no big words. Just present."},
        ],
    },
}

# Reverse lookup: token -> slug
TOKEN_TO_SLUG = {info["token"]: slug for slug, info in PEOPLE.items()}
def to_embed_url(url):
    """Turn a normal YouTube link into an embeddable one."""
    if not url:
        return None
    if "embed/" in url:
        return url
    video_id = None
    if "watch?v=" in url:
        video_id = url.split("watch?v=")[1].split("&")[0]
    elif "youtu.be/" in url:
        video_id = url.split("youtu.be/")[1].split("?")[0]
    if not video_id:
        return None
    return f"https://www.youtube.com/embed/{video_id}"

# Public-safe menu info (name + emoji only — no personal content)
MENU_ITEMS = [
    {"slug": slug, "display_name": info["display_name"], "emoji": info["emoji"]}
    for slug, info in PEOPLE.items()
]

# Funny-but-meaningful gatekeeper lines shown when someone clicks a tile
# that isn't theirs. Feel free to add more.
GATEKEEPER_LINES = [
    "Whoa there, detective. This diary has someone else's name on it. Privacy is a love language too. 🕵️",
    "Nice try. This one's locked with a heart-shaped key that isn't yours. 🔒",
    "This mailbox belongs to someone else. Some love notes are meant for one person only. 💌",
    "You found a door, not a key. Ask nicely for your own link instead. 😄",
]


@app.route("/")
def home():
    return render_template("locked.html", reason="home")


@app.route("/world/<token>")
def world(token):
    slug = TOKEN_TO_SLUG.get(token)
    if not slug:
        return render_template("locked.html", reason="invalid")

   person = PEOPLE[slug]
    song_embed_url = to_embed_url(person.get("song_url", ""))
    return render_template(
        "world.html",
        unlocked_slug=slug,
        person=person,
        song_embed_url=song_embed_url,
        menu_items=MENU_ITEMS,
        love_stickers=LOVE_STICKERS,
        gatekeeper_lines=GATEKEEPER_LINES,
    )


if __name__ == "__main__":
    print("\n💌 Drama Queen World — personal links:\n")
    for slug, info in PEOPLE.items():
        print(f"  {info['display_name']:<15} http://127.0.0.1:5000/world/{info['token']}")
    print("\nSend each person ONLY their own link.\n")
    app.run(debug=True)
