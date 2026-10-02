import {Audio} from '@remotion/media';
import {AbsoluteFill, Easing, Img, interpolate, Sequence, useCurrentFrame, useVideoConfig} from 'remotion';
import {ArcText} from './ArcText';
import {Background} from './Background';
import {C, asset, label, sans} from './theme';
import {VO} from './vo-timings';

const clamp = {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'} as const;

export const LEAD = 24; // iris opening
export const BEAT = 54; // frames per ingredient

const ITEMS = [
  {name: 'CHAMOMILE', file: 'cutouts/chamomile_v2.png', width: 600},
  {name: 'FENNEL', file: 'cutouts/fennel.png', width: 620},
  {name: 'ROSE', file: 'cutouts/rose.png', width: 580},
  {name: 'LICORICE', file: 'cutouts/licorice.png', width: 620},
];

// Circle iris: deep lilac field, the scene opens through a growing circle ringed with sunburst ticks.
const Iris: React.FC<{children: React.ReactNode}> = ({children}) => {
  const frame = useCurrentFrame();
  const r = interpolate(frame, [0, 10, 14, LEAD], [0, 230, 240, 1300], {
    ...clamp,
    easing: Easing.bezier(0.65, 0, 0.35, 1),
  });
  const ticks = interpolate(frame, [4, 10, 15, 19], [0, 1, 1, 0], clamp);
  return (
    <AbsoluteFill style={{backgroundColor: C.lilacDeep}}>
      <AbsoluteFill style={{clipPath: `circle(${r}px at 540px 1000px)`}}>{children}</AbsoluteFill>
      <svg width={1080} height={1920} style={{position: 'absolute', opacity: ticks}}>
        {Array.from({length: 12}).map((_, i) => {
          const a = (i / 12) * Math.PI * 2;
          return (
            <line
              key={i}
              x1={540 + Math.cos(a) * 270}
              y1={1000 + Math.sin(a) * 270}
              x2={540 + Math.cos(a) * 330}
              y2={1000 + Math.sin(a) * 330}
              stroke={C.white}
              strokeWidth={8}
              strokeLinecap="round"
            />
          );
        })}
      </svg>
    </AbsoluteFill>
  );
};

const Ingredient: React.FC<{i: number}> = ({i}) => {
  const frame = useCurrentFrame(); // local to this beat
  const item = ITEMS[i];
  const last = i === ITEMS.length - 1;
  const left = i % 2 === 0;
  const out = last ? 1 : interpolate(frame, [BEAT - 6, BEAT], [1, 0], clamp);

  return (
    <AbsoluteFill style={{opacity: out}}>
      <Img
        src={asset(item.file)}
        style={{
          position: 'absolute',
          width: item.width,
          left: 540 - item.width / 2,
          top: 1040,
          translate: '0 -50%',
          scale: interpolate(frame, [0, 14], [0.6, 1], {...clamp, easing: Easing.spring({damping: 11}), output: 'perceptual-scale'}),
          rotate: interpolate(frame, [0, BEAT], ['-6deg', '4deg'], clamp),
          opacity: interpolate(frame, [0, 5], [0, 1], clamp),
          filter: 'drop-shadow(0 24px 30px rgba(80,50,120,0.22))',
        }}
      />
      <div
        style={{
          position: 'absolute',
          top: 640,
          left: left ? 110 : undefined,
          right: left ? undefined : 150,
          fontFamily: label,
          fontWeight: 700,
          fontSize: 120,
          color: C.teal,
          letterSpacing: 2,
          opacity: interpolate(frame, [2, 8], [0, 1], clamp),
          translate: interpolate(frame, [2, 10], ['0px -20px', '0px 0px'], {...clamp, easing: Easing.bezier(0.16, 1, 0.3, 1)}),
        }}
      >
        {item.name}
      </div>
      <svg width={1080} height={1920} style={{position: 'absolute'}}>
        <path
          d={left ? 'M 200 790 C 160 850, 190 910, 290 940' : 'M 880 790 C 920 850, 890 910, 790 940'}
          fill="none"
          stroke={C.teal}
          strokeWidth={6}
          strokeLinecap="round"
          strokeDasharray={240}
          strokeDashoffset={interpolate(frame, [6, 18], [240, 0], clamp)}
        />
        <path
          d={left ? 'M 262 918 L 292 941 L 262 958' : 'M 818 918 L 788 941 L 818 958'}
          fill="none"
          stroke={C.teal}
          strokeWidth={6}
          strokeLinecap="round"
          strokeLinejoin="round"
          opacity={interpolate(frame, [17, 19], [0, 1], clamp)}
        />
      </svg>
    </AbsoluteFill>
  );
};

export const Ingredients: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const words = VO.l2.words;
  const durFrames = Math.floor(VO.l2.duration * fps);

  return (
    <Iris>
      <Background />
      <ArcText
        text="Steeped from"
        cx={540}
        cy={1040}
        r={470}
        fontFamily={sans}
        fontSize={62}
        color={C.teal}
        style={{opacity: interpolate(frame, [LEAD - 6, LEAD + 4], [0, 1], clamp)}}
      />
      <div
        style={{
          position: 'absolute',
          top: 1350,
          width: '100%',
          textAlign: 'center',
          fontFamily: sans,
          fontWeight: 600,
          fontSize: 52,
          color: C.teal,
          opacity: interpolate(frame, [LEAD + 8, LEAD + 16], [0, 1], clamp),
        }}
      >
        in every bag
      </div>

      <Sequence name="Chamomile" from={LEAD} durationInFrames={BEAT} premountFor={fps}>
        <Ingredient i={0} />
      </Sequence>
      <Sequence name="Fennel" from={LEAD + BEAT} durationInFrames={BEAT} premountFor={fps}>
        <Ingredient i={1} />
      </Sequence>
      <Sequence name="Rose" from={LEAD + 2 * BEAT} durationInFrames={BEAT} premountFor={fps}>
        <Ingredient i={2} />
      </Sequence>
      <Sequence name="Licorice" from={LEAD + 3 * BEAT} premountFor={fps}>
        <Ingredient i={3} />
      </Sequence>

      {/* Each ingredient is voiced by slicing its word out of line 2, so the voice lands with the swap. */}
      {words.map((wd, i) => (
        <Audio
          key={wd.text}
          src={asset('vo/l2.wav')}
          from={LEAD + i * BEAT + 3}
          trimBefore={Math.round(wd.start * fps)}
          trimAfter={Math.min(durFrames, Math.ceil(wd.end * fps))}
          premountFor={fps}
        />
      ))}
    </Iris>
  );
};
