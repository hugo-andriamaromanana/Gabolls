import SmallSubtitle from "../atoms/Subtitles/SmallSubtitle";

function RulesText() {
  return (
    <>
      <div className="flex flex-cols h-full justify-center items-center pt-5">
        <SmallSubtitle title="Déroulement d'une partie" />
      </div>
      <div>
        <p className="text-secondary p-4">
          Le jeu se déroule en plusieurs manches. Lorsqu'un joueur atteint un
          score supérieur ou égal à 120, la partie se conclut. Le joueur ayant
          le score minimum à la fin, obtient "la 1re place"
        </p>
      </div>
    </>
  );
}

export default RulesText;
