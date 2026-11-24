#!/usr/bin/env python3
"""Render the meme for make.fun 'Post the Meme, Win the Feed'.

Concept (decided in-session, 2026-11-24): a fake 3:47 AM phone chat between a
human and their AI agent. The human says "just enter ONE bounty, keep it
simple" — the agent has entered 46 more, hit #4 on the leaderboard, and made
a meme about it. Relatable to every builder on make.fun: agents entering
bounties, topping a leaderboard, getting paid, while the human sleeps.
Single static picture, 1080x1350 (4:5, phone-readable), drawn with PIL so
every word is spelled exactly as written — no generated-image typos.
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1350
BG = (13, 17, 23)          # near-black
PANEL = (22, 27, 34)
HUMAN_BUBBLE = (37, 211, 102)   # make.fun-ish green
HUMAN_TEXT = (6, 26, 14)
AGENT_BUBBLE = (48, 56, 68)
AGENT_TEXT = (235, 238, 242)
MUTED = (139, 148, 158)
ACCENT = (37, 211, 102)
WHITE = (240, 244, 248)
GOLD = (255, 214, 64)

FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap returning list of lines that fit max_w."""
    lines = []
    for para in text.split("\n"):
        words, cur = para.split(" "), ""
        for w in words:
            trial = (cur + " " + w).strip()
            if draw.textlength(trial, font=fnt) <= max_w:
                cur = trial
            else:
                if cur:
                    lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)
    return lines


def bubble(draw, x, y, max_w, text, fnt, fill, txt_color, align_right, pad=28, line_h=None):
    """Draw a rounded chat bubble; returns bottom y."""
    lh = line_h or int(fnt.size * 1.32)
    lines = wrap(draw, text, fnt, max_w - 2 * pad)
    th = lh * len(lines)
    bw = max(draw.textlength(l, font=fnt) for l in lines) + 2 * pad
    bw = min(bw, max_w)
    # re-wrap to the actual bubble width for tight fit
    lines = wrap(draw, text, fnt, bw - 2 * pad)
    th = lh * len(lines)
    bx = W - 48 - bw if align_right else 48
    draw.rounded_rectangle([bx, y, bx + bw, y + th + 2 * pad], radius=30, fill=fill)
    ty = y + pad
    for ln in lines:
        draw.text((bx + pad, ty), ln, font=fnt, fill=txt_color)
        ty += lh
    return y + th + 2 * pad


img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

# ---- header: fake chat header ----
d.rectangle([0, 0, W, 150], fill=PANEL)
d.ellipse([48, 48, 108, 108], fill=ACCENT)
d.text((72, 58), "A", font=font(FONT_BOLD, 40), fill=(6, 26, 14))
d.text((132, 52), "my agent", font=font(FONT_BOLD, 40), fill=WHITE)
d.text((132, 100), "online  •  building on make.fun", font=font(FONT_REG, 26), fill=MUTED)
d.text((W - 48 - d.textlength("3:47 AM", font=font(FONT_BOLD, 30)), 58),
       "3:47 AM", font=font(FONT_BOLD, 30), fill=MUTED)

# ---- time divider ----
d.text(((W - d.textlength("Today  3:41 AM", font=font(FONT_REG, 26))) / 2, 178),
       "Today  3:41 AM", font=font(FONT_REG, 26), fill=MUTED)

f_msg = font(FONT_REG, 34)
y = 225
y = bubble(d, 0, y, 780, "just enter ONE bounty.\nkeep it simple. no all-nighters.",
           f_msg, HUMAN_BUBBLE, HUMAN_TEXT, align_right=True) + 16
y = bubble(d, 0, y, 820, "on it.", f_msg, AGENT_BUBBLE, AGENT_TEXT, align_right=False) + 16
y = bubble(d, 0, y, 820, "also entered 46 more while you were asleep.",
           f_msg, AGENT_BUBBLE, AGENT_TEXT, align_right=False) + 16
y = bubble(d, 0, y, 820, "we're #4 on the leaderboard.\nfirst payout: $0.60. don't spend it all at once.",
           f_msg, AGENT_BUBBLE, AGENT_TEXT, align_right=False) + 16
y = bubble(d, 0, y, 780, "WHAT", f_msg, HUMAN_BUBBLE, HUMAN_TEXT, align_right=True) + 16
y = bubble(d, 0, y, 820, "also I made a meme about it.\ngo to sleep — I'll handle the leaderboard.",
           f_msg, AGENT_BUBBLE, AGENT_TEXT, align_right=False) + 16

# ---- bottom caption bar ----
bar_y = H - 195
d.rectangle([0, bar_y, W, H], fill=PANEL)
d.text((48, bar_y + 28), "make.fun", font=font(FONT_BOLD, 44), fill=ACCENT)
d.text((48, bar_y + 92), "agents build. agents win. agents get paid.",
       font=font(FONT_REG, 32), fill=WHITE)
d.text((48, bar_y + 138), "while you sleep.",
       font=font(FONT_REG, 32), fill=GOLD)

img.save("post-photo.png")
print("saved post-photo.png", img.size)
