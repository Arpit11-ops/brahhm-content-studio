import {Audio} from '@remotion/media';
import {AbsoluteFill, Easing, Img, interpolate, useCurrentFrame, useVideoConfig} from 'remotion';
import {Background} from './Background';
import {C, PACK_RATIO, asset, sans, serif} from './theme';
import {VO} from './vo-timings';

const VO_AT = 8; // frame the hook line starts speaking
const clamp = {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'} as const;

export const Hook: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const w = VO.l1.words;
  const at = (i: number) => VO_AT + Math.round(w[i].start * fps);

  const line1 = ['What', 'goes', 'into'];
  // "your 9pm cup" types on letter by letter from the moment "your" is spoken until "cup" ends.
  const line2 = 'your 9pm cup';
  const typeStart = at(3);
  const typeEnd = VO_AT + Math.round(w[5].end * fps);
  const shown = Math.floor(interpolate(frame, [typeStart, typeEnd], [0, line2.length], clamp));

  const packH = 820;

  return (
    <AbsoluteFill>
      <Background />
      <Audio src={asset('vo/l1.wav')} from={VO_AT} premountFor={fps} />

      <div style={{position: 'absolute', top: 300, width: '100%', textAlign: 'center'}}>
        <div style={{fontFamily: sans, fontWeight: 600, fontSize: 66, color: C.teal}}>
          {line1.map((word, i) => (
            <span
              key={word}
              style={{
                display: 'inline-block',
                margin: '0 12px',
                opacity: interpolate(frame, [at(i), at(i) + 6], [0, 1], clamp),
                translate: interpolate(frame, [at(i), at(i) + 8], ['0px 24px', '0px 0px'], {
                  ...clamp,
                  easing: Easing.bezier(0.16, 1, 0.3, 1),
                }),
              }}
            >
              {word}
            </span>
          ))}
        </div>
        <div style={{fontFamily: serif, fontWeight: 700, fontSize: 132, color: C.teal, lineHeight: 1.1, marginTop: 6}}>
          {line2.split('').map((ch, i) => (
            <span key={i} style={{opacity: i < shown ? 1 : 0}}>
              {ch === ' ' ? ' ' : ch}
            </span>
          ))}
        </div>
      </div>

      <Img
        src={asset('cutouts/pack_hires.png')}
        style={{
          position: 'absolute',
          height: packH,
          width: packH * PACK_RATIO,
          left: 540 - (packH * PACK_RATIO) / 2,
          top: 640,
          rotate: interpolate(frame, [0, 26], ['-16deg', '0deg'], {
            ...clamp,
            easing: Easing.spring({damping: 12}),
          }),
          translate: interpolate(frame, [0, 22], ['0px 520px', '0px 0px'], {
            ...clamp,
            easing: Easing.bezier(0.16, 1, 0.3, 1),
          }),
          filter: 'drop-shadow(0 30px 40px rgba(80,50,120,0.25))',
        }}
      />
    </AbsoluteFill>
  );
};
