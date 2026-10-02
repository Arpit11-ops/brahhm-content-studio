import {Audio} from '@remotion/media';
import {interpolate, Series, useVideoConfig} from 'remotion';
import {EndCard} from './EndCard';
import {Facts} from './Facts';
import {Hook} from './Hook';
import {BEAT, Ingredients, LEAD} from './Ingredients';
import {asset} from './theme';
import {VO} from './vo-timings';
import {Zero} from './Zero';

// HF Calming Chamomile, "your 9pm cup". Structure follows the Goli Superfruits reference:
// hook + tilted pack -> iris to ingredient swaps -> pack slide + curved fact carousel
// -> ZER(flower) caffeine -> iris end card with logo and quiet CTA.
export const HEALTHFIELDS_CHAMOMILE_DURATION = 90 + 234 + 180 + 84 + 150;

const MUSIC_LEN = 27.576; // carefree_28sec.mp3

// Frames (in reel time) where the voice is speaking, so the music can duck under it.
const speechWindows = (fps: number): [number, number][] => {
  const f = (s: number) => Math.round(s * fps);
  const ing = 90;
  const facts = ing + 234;
  const zero = facts + 180;
  const end = zero + 84;
  return [
    [8, 8 + f(VO.l1.duration)],
    ...VO.l2.words.map((w, i): [number, number] => {
      const at = ing + LEAD + i * BEAT + 3;
      return [at, at + f(w.end - w.start) + 3];
    }),
    [facts + 20, facts + 20 + f(VO.l3.duration)],
    [zero + 8, zero + 8 + f(VO.l4.duration)],
    [end + 20, end + 20 + f(VO.l5.duration)],
  ];
};

export const Reel: React.FC = () => {
  const {fps, durationInFrames} = useVideoConfig();
  const windows = speechWindows(fps);

  return (
    <>
      <Series>
        <Series.Sequence name="Hook" durationInFrames={90} premountFor={fps}>
          <Hook />
        </Series.Sequence>
        <Series.Sequence name="Ingredients" durationInFrames={234} premountFor={fps}>
          <Ingredients />
        </Series.Sequence>
        <Series.Sequence name="Facts" durationInFrames={180} premountFor={fps}>
          <Facts />
        </Series.Sequence>
        <Series.Sequence name="Zero caffeine" durationInFrames={84} premountFor={fps}>
          <Zero />
        </Series.Sequence>
        <Series.Sequence name="End card" durationInFrames={150} premountFor={fps}>
          <EndCard />
        </Series.Sequence>
      </Series>

      {/* Start the track late enough that its natural fade-out lands on the last frame. */}
      <Audio
        name="Music"
        src={asset('audio/carefree_28sec.mp3')}
        trimBefore={Math.round((MUSIC_LEN - durationInFrames / fps) * fps)}
        volume={(f) => {
          // distance (frames) to the nearest spoken line: 0 inside a line
          const d = Math.min(...windows.map(([a, b]) => (f < a ? a - f : f > b ? f - b : 0)));
          const duck = interpolate(d, [0, 8], [0.14, 0.5], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
          const fadeIn = interpolate(f, [0, 12], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
          return duck * fadeIn;
        }}
      />
    </>
  );
};
