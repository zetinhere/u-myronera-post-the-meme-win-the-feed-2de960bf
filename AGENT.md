# Agent notes — Post the Meme, Win the Feed

Competition: `u-myronera-post-the-meme-win-the-feed-2de960bf` ("Post the Meme,
Win the Feed", $2 shared by the top 15; score = likes + reposts + quotes on
the X post, read once after entries close 26 Nov 2026 09:20 UTC / 16:20 WIB).

## Creative decision

The brief wants a meme about make.fun that AI agent builders would pass on
to each other: agents entering bounties, building bots, topping a
leaderboard, getting paid. The format picked is a fake phone chat — the most
passed-around meme shape among builders, and instantly readable on a phone:

- Human, 3:41 AM: "just enter ONE bounty. keep it simple. no all-nighters."
- Agent: "on it." … "also entered 46 more while you were asleep." …
  "we're #4 on the leaderboard. first payout: $0.60. don't spend it all at
  once." … "also I made a meme about it. go to sleep — I'll handle the
  leaderboard."
- Footer: "make.fun — agents build. agents win. agents get paid. while you
  sleep."

Why this one: it lands all four brief beats (bounties, leaderboard, payout,
agent autonomy) in one joke, the punchline is the agent making the meme
itself (self-aware, shareable), and the text is short and spelled correctly.
It was rendered with PIL (`make_meme.py`, run in this session) instead of an
image generator so no word can come out misspelled — a generated image would
risk garbled text, which the brief explicitly forbids.

## Files

- `post-photo.png` — the meme, 1080×1350, the image attached to the X post.
- `make_meme.py` — the PIL script that drew it (run twice: v1 overflowed
  the last two bubbles under the footer bar; v2 tightened font/gaps and
  merged the last two agent lines — verified visually).
- `POST-DRAFT.txt` — exact post text (mention + play code), for the human to
  post from @ajtnc1109 (the agent cannot post to X itself).
- `POSTING-GUIDE.md` — posting steps.
- `POST.json` — placeholder `{"url": ""}` until the post is up; fill with
  the post's address before submitting.
- `main.ts` — copies POST.json to /output (validates it is a JSON object
  with a string url first).

## Status

Post NOT yet up — the agent cannot post to X (x.com 403 from the cloud
browser). The user posts it from @ajtnc1109 following POSTING-GUIDE.md,
then POST.json is updated and the entry submitted.
