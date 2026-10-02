import {Composition, Folder} from 'remotion';
import {SetupCheck} from './SetupCheck';
import {Reel as HFChamomileReel} from './reels/2026-10-01_healthfields_chamomile-9pm-cup/Reel';

// Register every reel here as its own <Composition>, inside the "Reels" folder.
// Each reel's code lives in src/reels/<YYYY-MM-DD>_<brand>_<slug>/ (see skills/remotion-reels/SKILL.md).
export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Folder name="Reels">
        <Composition
          id="reel-2026-10-01-healthfields-chamomile-9pm-cup"
          component={HFChamomileReel}
          width={1080}
          height={1920}
          fps={30}
          durationInFrames={738}
        />
      </Folder>
      <Folder name="Utilities">
        <Composition id="SetupCheck" component={SetupCheck} width={1080} height={1920} fps={30} durationInFrames={90} />
      </Folder>
    </>
  );
};
