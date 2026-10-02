import {AbsoluteFill, Easing, Img, interpolate, staticFile, useCurrentFrame} from 'remotion';

// Pipeline smoke test: a real pack image, frame-driven motion, text. Not a reel template.
export const SetupCheck: React.FC = () => {
  const frame = useCurrentFrame();
  const ease = Easing.bezier(0.16, 1, 0.3, 1);

  return (
    <AbsoluteFill style={{backgroundColor: '#F5F2E8', alignItems: 'center', justifyContent: 'center', gap: 80}}>
      <Img
        src={staticFile('setup-check/pack.webp')}
        style={{
          width: 720,
          opacity: interpolate(frame, [0, 15], [0, 1], {extrapolateRight: 'clamp'}),
          scale: interpolate(frame, [0, 90], [0.92, 1], {extrapolateRight: 'clamp', easing: ease}),
        }}
      />
      <div style={{fontFamily: 'sans-serif', fontSize: 64, fontWeight: 700, color: '#003C32'}}>Remotion is ready</div>
    </AbsoluteFill>
  );
};
