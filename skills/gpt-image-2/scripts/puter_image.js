#!/usr/bin/env node
/**
 * puter_image.js — GPT Image 2 via Puter.js (free, no OpenAI key needed)
 *
 * Usage:
 *   node puter_image.js "your prompt" output.png
 *   node puter_image.js --model gpt-image-2 "your prompt" output.png
 *   node puter_image.js --size 1024x1792 "your prompt" output.png
 *
 * Auth:
 *   Set PUTER_AUTH_TOKEN env var (get from puter.com/dashboard → Copy)
 *
 * Models: gpt-image-2, gpt-image-1.5, gpt-image-1-mini, gpt-image-1, dall-e-3
 * Sizes:  1024x1024 (square) | 1024x1792 (story/reel 9:16) | 1792x1024 (landscape)
 */

import { init } from '@heyputer/puter.js/src/init.cjs';
import fs from 'fs';
import path from 'path';

// ── Auth check ──────────────────────────────────────────────────────────────
const token = process.env.PUTER_AUTH_TOKEN;
if (!token) {
  console.error('❌ PUTER_AUTH_TOKEN not set.');
  console.error('   Get your token from puter.com/dashboard → Copy');
  console.error('   Then add it to .claude/settings.local.json under env');
  process.exit(1);
}

// ── Parse CLI args ──────────────────────────────────────────────────────────
const args = process.argv.slice(2);
let model  = 'gpt-image-2';
let size   = '1024x1792'; // story / reel format by default
let prompt = null;
let outputPath = null;

for (let i = 0; i < args.length; i++) {
  if (args[i] === '--model' && args[i + 1]) { model = args[++i]; continue; }
  if (args[i] === '--size'  && args[i + 1]) { size  = args[++i]; continue; }
  if (!prompt)     { prompt     = args[i]; continue; }
  if (!outputPath) { outputPath = args[i]; continue; }
}

if (!prompt || !outputPath) {
  console.error('Usage: node puter_image.js [--model gpt-image-2] [--size 1024x1792] "prompt" output.png');
  process.exit(1);
}

// Ensure output directory exists
const outDir = path.dirname(path.resolve(outputPath));
if (!fs.existsSync(outDir)) fs.mkdirSync(outDir, { recursive: true });

// ── Init Puter ──────────────────────────────────────────────────────────────
const puter = init(token);

// ── Generate ────────────────────────────────────────────────────────────────
console.log(`\n🎨 Generating image...`);
console.log(`   Model:  ${model}`);
console.log(`   Size:   ${size}`);
console.log(`   Output: ${outputPath}`);
console.log(`   Prompt: ${prompt.substring(0, 100)}${prompt.length > 100 ? '...' : ''}\n`);

try {
  const result = await puter.ai.txt2img(prompt, { model, size });

  // Extract base64 from data URL or handle direct buffer
  const src = result?.src ?? result;

  let buffer;
  if (typeof src === 'string' && src.startsWith('data:')) {
    buffer = Buffer.from(src.split(',')[1], 'base64');
  } else if (typeof src === 'string') {
    buffer = Buffer.from(src, 'base64');
  } else if (Buffer.isBuffer(src)) {
    buffer = src;
  } else {
    console.error('Unexpected result format:', JSON.stringify(result, null, 2));
    process.exit(1);
  }

  fs.writeFileSync(outputPath, buffer);
  const kb = (buffer.length / 1024).toFixed(1);
  console.log(`✅ Done — saved to ${outputPath} (${kb} KB)`);

} catch (err) {
  console.error('❌ Generation failed:', err.message || err);
  process.exit(1);
}
