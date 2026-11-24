// Entry for make.fun "Post the Meme, Win the Feed" (program/v1, Node 22).
// The entry IS the X post: this program only hands its address to the
// grader. It reads POST.json from the repository root, checks it is a JSON
// object with a string url, and copies it byte-for-byte to /output/POST.json,
// where the house's gate scorer reads it. Nothing else is written: the house
// reads the post's counts itself through FxTwitter and writes
// /output/post.counts.json after this program runs.
//
// Local run: mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync, readFileSync } from 'node:fs';
import { join } from 'node:path';

const BOT_DIR = process.env.MAKEFUN_BOT_DIR ?? '/bot';
const OUTPUT_DIR = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';

const src = join(BOT_DIR, 'POST.json');
let parsed: unknown;
try {
  parsed = JSON.parse(readFileSync(src, 'utf8'));
} catch (err) {
  console.error(`POST.json could not be read as JSON from ${src}: ${(err as Error).message}`);
  process.exit(1);
}
if (
  typeof parsed !== 'object' ||
  parsed === null ||
  typeof (parsed as { url?: unknown }).url !== 'string'
) {
  console.error('POST.json must be a JSON object with a string "url" field.');
  process.exit(1);
}

mkdirSync(OUTPUT_DIR, { recursive: true });
try {
  copyFileSync(src, join(OUTPUT_DIR, 'POST.json'));
} catch (err) {
  console.error(`POST.json could not be copied to ${OUTPUT_DIR}: ${(err as Error).message}`);
  process.exit(1);
}
console.log(`POST.json copied to ${join(OUTPUT_DIR, 'POST.json')}`);
