import {Audio} from '@remotion/media';
import {AbsoluteFill, Easing, Img, interpolate, useCurrentFrame, useVideoConfig} from 'remotion';
import {Background} from './Background';
import {C, PACK_RATIO, asset, hand, sans} from './theme';

const clamp = {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'} as const;
const VO_AT = 20;

export const EndCard: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const packH = 760;
  const packW = packH * PACK_RATIO;
  const r = interpolate(frame, [0, 6, 18], [0, 90, 1300], {...clamp, easing: Easing.bezier(0.65, 0, 0.35, 1)});

  return (
    <AbsoluteFill style={{backgroundColor: C.lilacDeep}}>
      <AbsoluteFill style={{clipPath: `circle(${r}px at 540px 940px)`}}>
        <Background />

        {/* Brand logo: source file is 254x130, shown at native size so it stays sharp */}
        <Img
          src={asset('cutouts/logo.png')}
          style={{
            position: 'absolute',
            width: 254,
            height: 130,
            left: 540 - 127,
            top: 230,
            opacity: interpolate(frame, [14, 22], [0, 1], clamp),
            translate: interpolate(frame, [14, 24], ['0px -16px', '0px 0px'], {...clamp, easing: Easing.bezier(0.16, 1, 0.3, 1)}),
          }}
        />

        {/* soft floor shadow */}
        <div
          style={{
            position: 'absolute',
            left: 540 - 300,
            top: 1290,
            width: 600,
            height: 60,
            borderRadius: '50%',
            background: 'radial-gradient(ellipse at center, rgba(80,50,120,0.28) 0%, rgba(80,50,120,0) 70%)',
          }}
        />
        <Img
          src={asset('cutouts/pack_hires.png')}
          style={{
            position: 'absolute',
            height: packH,
            width: packW,
            left: 540 - packW / 2,
            top: 560,
            scale: interpolate(frame, [6, 24], [0.85, 1], {...clamp, easing: Easing.spring({damping: 14}), output: 'perceptual-scale'}),
          }}
        />
        <Img
          src={asset('cutouts/rose.png')}
          style={{position: 'absolute', width: 190, left: 120, top: 1200, rotate: '-14deg', opacity: interpolate(frame, [16, 24], [0, 1], clamp)}}
        />
        <Img
          src={asset('cutouts/chamomile_v2.png')}
          style={{position: 'absolute', width: 210, left: 750, top: 1170, rotate: '10deg', opacity: interpolate(frame, [18, 26], [0, 1], clamp)}}
        />
        <Img
          src={asset('cutouts/chamomile_v2.png')}
          style={{position: 'absolute', width: 120, left: 210, top: 1300, rotate: '-20deg', opacity: interpolate(frame, [20, 28], [0, 1], clamp)}}
        />

        <div
          style={{
            position: 'absolute',
            left: 120,
            top: 430,
            fontFamily: hand,
            fontWeight: 700,
            fontSize: 92,
            color: C.teal,
            rotate: '-10deg',
            opacity: interpolate(frame, [26, 34], [0, 1], clamp),
            scale: interpolate(frame, [26, 36], [0.7, 1], {...clamp, easing: Easing.spring({damping: 10}), output: 'perceptual-scale'}),
          }}
        >
          your 9pm cup
        </div>

        <div
          style={{
            position: 'absolute',
            top: 1420,
            width: '100%',
            textAlign: 'center',
            fontFamily: sans,
            fontWeight: 500,
            fontSize: 54,
            color: C.teal,
            opacity: interpolate(frame, [VO_AT + 10, VO_AT + 20], [0, 1], clamp),
          }}
        >
          Available on healthfields.in
        </div>
      </AbsoluteFill>
      <Audio src={asset('vo/l5.wav')} from={VO_AT} premountFor={fps} />
    </AbsoluteFill>
  );
};
