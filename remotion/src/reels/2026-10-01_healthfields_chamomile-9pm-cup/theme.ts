import {loadFont as loadFraunces} from '@remotion/google-fonts/Fraunces';
import {loadFont as loadManrope} from '@remotion/google-fonts/Manrope';
import {loadFont as loadCaveat} from '@remotion/google-fonts/Caveat';
import {loadFont as loadAmatic} from '@remotion/google-fonts/AmaticSC';
import {staticFile} from 'remotion';

export const FOLDER = 'reels/2026-10-01_healthfields_chamomile-9pm-cup';
export const asset = (p: string) => staticFile(`${FOLDER}/${p}`);

export const serif = loadFraunces('normal', {weights: ['600', '700', '900'], subsets: ['latin']}).fontFamily;
export const sans = loadManrope('normal', {weights: ['500', '600'], subsets: ['latin']}).fontFamily;
export const hand = loadCaveat('normal', {weights: ['700'], subsets: ['latin']}).fontFamily;
export const label = loadAmatic('normal', {weights: ['700'], subsets: ['latin']}).fontFamily;

// Colour world: soft lilac + cream (matches the pack), HF Teal Green for type and CTA.
export const C = {
  cream: '#F7F2FA',
  lilac: '#E9DEF4',
  lilacMid: '#C9B3E3',
  lilacDeep: '#8E6CB8',
  teal: '#1A6B5A',
  white: '#FFFFFF',
};

// Pack cut-out is 1431x2660.
export const PACK_RATIO = 1431 / 2660;
