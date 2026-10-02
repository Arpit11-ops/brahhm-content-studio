import {AbsoluteFill} from 'remotion';
import {C} from './theme';

// Zigzag band, Goli-style, peeking in at the top and bottom edges.
const Zigzag: React.FC<{top?: boolean}> = ({top}) => {
  const teeth = 9;
  const w = 1080 / teeth;
  let d = top ? 'M0 0 ' : 'M0 60 ';
  for (let i = 0; i < teeth; i++) {
    const x = i * w;
    d += top ? `L${x + w / 2} 46 L${x + w} 0 ` : `L${x + w / 2} 14 L${x + w} 60 `;
  }
  d += top ? 'Z' : 'L1080 60 Z';
  return (
    <svg
      width={1080}
      height={60}
      viewBox="0 0 1080 60"
      style={{position: 'absolute', left: 0, [top ? 'top' : 'bottom']: 0}}
    >
      <path d={d} fill={C.lilacMid} />
    </svg>
  );
};

export const Background: React.FC = () => {
  return (
    <AbsoluteFill
      style={{background: `radial-gradient(circle at 50% 52%, ${C.cream} 0%, ${C.lilac} 75%)`}}
    >
      <svg width={1080} height={1920} style={{position: 'absolute'}}>
        {[300, 430, 560, 690, 820, 950].map((r) => (
          <circle key={r} cx={540} cy={1000} r={r} fill="none" stroke={C.white} strokeWidth={2.5} opacity={0.7} />
        ))}
      </svg>
      <Zigzag top />
      <Zigzag />
    </AbsoluteFill>
  );
};
