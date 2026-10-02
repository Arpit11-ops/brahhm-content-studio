import {useId} from 'react';

type Props = {
  readonly text: string;
  readonly cx: number;
  readonly cy: number;
  readonly r: number;
  readonly fontFamily: string;
  readonly fontSize: number;
  readonly fontWeight?: number;
  readonly color: string;
  readonly style?: React.CSSProperties;
};

// Text curved along the top of a circle, centred on the arc.
export const ArcText: React.FC<Props> = ({text, cx, cy, r, fontFamily, fontSize, fontWeight = 600, color, style}) => {
  const id = useId().replace(/:/g, '');
  const d = `M ${cx - r} ${cy} A ${r} ${r} 0 0 1 ${cx + r} ${cy}`;
  return (
    <svg width={1080} height={1920} style={{position: 'absolute', left: 0, top: 0, overflow: 'visible', ...style}}>
      <defs>
        <path id={id} d={d} />
      </defs>
      <text fontFamily={fontFamily} fontSize={fontSize} fontWeight={fontWeight} fill={color} letterSpacing={1}>
        <textPath href={`#${id}`} startOffset="50%" textAnchor="middle">
          {text}
        </textPath>
      </text>
    </svg>
  );
};
