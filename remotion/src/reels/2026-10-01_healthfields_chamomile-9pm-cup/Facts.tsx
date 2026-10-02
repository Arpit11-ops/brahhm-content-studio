import {Audio} from '@remotion/media';
import {AbsoluteFill, Easing, Img, interpolate, useCurrentFrame, useVideoConfig} from 'remotion';
import {ArcText} from './ArcText';
import {Background} from './Background';
import {C, PACK_RATIO, asset, serif} from './theme';
import {VO} from './vo-timings';

const clamp = {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'} as const;
const VO_AT = 20;

const HEADLINES = [
  {text: 'Unbleached paper bags', word: 0},
  {text: 'No added colours', word: 3},
  {text: 'Certified organic', word: 6},
];

// Ingredients drifting in the corners, like Goli's floating gummies.
const Floater: React.FC<{file: string; x: number; y: number; w: number; phase: number; delay: number}> = ({
  file,
  x,
  y,
  w,
  phase,
  delay,
}) => {
  const frame = useCurrentFrame();
  return (
    <Img
      src={asset(file)}
      style={{
        position: 'absolute',
        left: x,
        top: y,
        width: w,
        opacity: interpolate(frame, [delay, delay + 10], [0, 1], clamp),
        translate: `0px ${Math.sin((frame + phase) / 18) * 14}px`,
        rotate: `${Math.sin((frame + phase) / 30) * 8}deg`,
        filter: 'drop-shadow(0 14px 18px rgba(80,50,120,0.18))',
      }}
    />
  );
};

export const Facts: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const w = VO.l3.words;
  const starts = HEADLINES.map((h) => VO_AT + Math.round(w[h.word].start * fps) - 2);
  const packH = 740;

  return (
    <AbsoluteFill>
      <Background />
      <Audio src={asset('vo/l3.wav')} from={VO_AT} premountFor={fps} />

      <Floater file="cutouts/licorice.png" x={40} y={300} w={240} phase={0} delay={8} />
      <Floater file="cutouts/rose.png" x={790} y={290} w={230} phase={40} delay={12} />
      <Floater file="cutouts/fennel.png" x={40} y={1420} w={250} phase={80} delay={16} />
      <Floater file="cutouts/chamomile_v2.png" x={780} y={1400} w={220} phase={120} delay={20} />

      {HEADLINES.map((h, i) => {
        const start = starts[i];
        const end = i < HEADLINES.length - 1 ? starts[i + 1] : 10_000;
        const reveal = interpolate(frame, [start, start + 9], [100, 0], {...clamp, easing: Easing.bezier(0.65, 0, 0.35, 1)});
        const hide = interpolate(frame, [end, end + 7], [0, 100], {...clamp, easing: Easing.bezier(0.65, 0, 0.35, 1)});
        return (
          <ArcText
            key={h.text}
            text={h.text}
            cx={540}
            cy={1180}
            r={560}
            fontFamily={serif}
            fontSize={72}
            fontWeight={700}
            color={C.teal}
            style={{clipPath: `inset(0 ${reveal}% 0 ${hide}%)`}}
          />
        );
      })}

      <Img
        src={asset('cutouts/pack_hires.png')}
        style={{
          position: 'absolute',
          height: packH,
          width: packH * PACK_RATIO,
          left: 540 - (packH * PACK_RATIO) / 2,
          top: 730,
          translate: interpolate(frame, [0, 18], ['900px 0px', '0px 0px'], {...clamp, easing: Easing.bezier(0.16, 1, 0.3, 1)}),
          rotate: interpolate(frame, [0, 18, 26], ['12deg', '-3deg', '0deg'], {...clamp, easing: Easing.bezier(0.33, 1, 0.68, 1)}),
          filter: 'drop-shadow(0 30px 40px rgba(80,50,120,0.25))',
        }}
      />
    </AbsoluteFill>
  );
};
