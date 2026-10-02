import {Audio} from '@remotion/media';
import {AbsoluteFill, Easing, Img, interpolate, useCurrentFrame, useVideoConfig} from 'remotion';
import {Background} from './Background';
import {C, asset, sans, serif} from './theme';
import {VO} from './vo-timings';

const clamp = {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'} as const;
const VO_AT = 8;

export const Zero: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const w = VO.l4.words;
  const at = (i: number) => VO_AT + Math.round(w[i].start * fps);
  const zero = at(1);

  return (
    <AbsoluteFill>
      <Background />
      <Audio src={asset('vo/l4.wav')} from={VO_AT} premountFor={fps} />

      <div
        style={{
          position: 'absolute',
          top: 560,
          width: '100%',
          textAlign: 'center',
          fontFamily: sans,
          fontWeight: 600,
          fontSize: 70,
          color: C.teal,
          opacity: interpolate(frame, [at(0), at(0) + 5], [0, 1], clamp),
        }}
      >
        And
      </div>

      <div
        style={{
          position: 'absolute',
          top: 660,
          width: '100%',
          display: 'flex',
          justifyContent: 'center',
          alignItems: 'center',
          fontFamily: serif,
          fontWeight: 900,
          fontSize: 250,
          color: C.teal,
          lineHeight: 1,
        }}
      >
        {['Z', 'E', 'R'].map((ch, i) => (
          <span
            key={ch}
            style={{
              display: 'inline-block',
              opacity: interpolate(frame, [zero + i * 2, zero + i * 2 + 4], [0, 1], clamp),
              scale: interpolate(frame, [zero + i * 2, zero + i * 2 + 10], [0.4, 1], {
                ...clamp,
                easing: Easing.spring({damping: 10}),
                output: 'perceptual-scale',
              }),
            }}
          >
            {ch}
          </span>
        ))}
        <Img
          src={asset('cutouts/chamomile_v2.png')}
          style={{
            width: 230,
            marginLeft: 6,
            translate: interpolate(frame, [zero + 2, zero + 16], ['800px 0px', '0px 0px'], {
              ...clamp,
              easing: Easing.bezier(0.16, 1, 0.3, 1),
            }),
            rotate: interpolate(frame, [zero + 2, zero + 20], ['540deg', '0deg'], {
              ...clamp,
              easing: Easing.bezier(0.16, 1, 0.3, 1),
            }),
          }}
        />
      </div>

      <div
        style={{
          position: 'absolute',
          top: 940,
          width: '100%',
          textAlign: 'center',
          fontFamily: serif,
          fontWeight: 700,
          fontSize: 130,
          color: C.teal,
          opacity: interpolate(frame, [at(2), at(2) + 6], [0, 1], clamp),
          translate: interpolate(frame, [at(2), at(2) + 10], ['0px 30px', '0px 0px'], {
            ...clamp,
            easing: Easing.bezier(0.16, 1, 0.3, 1),
          }),
        }}
      >
        caffeine
      </div>
    </AbsoluteFill>
  );
};
