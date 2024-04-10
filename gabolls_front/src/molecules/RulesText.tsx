import SmallSubtitle from "../atoms/Subtitles/SmallSubtitle";
import MiniCard from "../atoms/MiniCard";

function RulesText() {
  return (
    <div className="pb-4">
      <div className="flex flex-cols justify-center items-center pt-10 pb-4">
        <SmallSubtitle title="Déroulement d'une partie" />
      </div>
      <div>
        <p className="text-quinary pt-4 pl-4 pr-4">
          Le jeu se déroule en plusieurs manches. Lorsqu'un joueur atteint un
          score supérieur ou égal à 120, la partie se conclut. Le joueur ayant
          le score minimum à la fin, obtient "la 1re place"
        </p>
        <p className="text-quinary pt-4 pl-4 pr-4">
          Le reste sera classé par ordre croissant. Le décompte des points de
          chacun se fait à la fin de chaque manche et s'additionne pour donner
          le score final à la fin du nombre de manches décidé pour la partie.
        </p>
        <p className="text-quinary pt-4 pl-4 pr-4">
          Le but du jeu est d'avoir le moins de points possibles a la fin de la
          partie.
        </p>
      </div>
      <div className="flex flex-cols justify-center items-center pt-10 pb-4">
        <SmallSubtitle title="Déroulement d'une manche" />
      </div>
      <div>
        <p className="text-quinary pt-4 pl-4 pr-4">
          Un joueur mélange les cartes à distribuer et en donne quatre à chaques
          joueur.
        </p>
        <p className="text-quinary pt-4 pl-4 pr-4">
          Il pose la pioche au centre, face cachée. Chaque joueur dispose ses 4
          cartes devant lui en carré. Chaque joueur doit prendre connaissance
          uniquement des deux premières cartes devant lui et doit les retenir
          avant de les reposer face cachée au même endroit, avant que le jeu ne
          commence.
        </p>
        <p className="text-quinary pt-4 pl-4 pr-4">
          Les cartes ne peuvent pas être interchangées de places! sauf avec le
          pouvoir des cartes.
        </p>
        <p className="text-quinary pt-4 pl-4 pr-4">
          Le joueur situé à la droite (ou gauche, à définir en début de partie)
          du donneur commence le tour.
        </p>
        <p className="text-quinary pt-4 pl-4 pr-4">
          Il pioche une carte dans la pioche OU que lui seul regarde et peut,
          selon son choix :
        </p>
        <ul className="text-quinary pt-4 pl-10 pr-4 list-disc">
          <li>
            La reposer dans la défausse (située à côté de la pioche, face
            visible) en utilisant, ou pas, le pouvoir de cette carte le cas
            échéant (voir partie : pouvoir des cartes) (A).
          </li>
          <li>
            La placer dans son jeu face cachée à la place de n'importe quelle
            autre de ses 4 cartes et défausse ensuite la carte ainsi remplacée
            (face visible comme toujours dans une défausse) (B).
          </li>
        </ul>
        <p className="text-quinary pt-4 pl-4 pr-4">
          Le joueur suivant a le choix :
        </p>
        <ul className="text-quinary pt-4 pl-10 pr-4 list-disc">
          <li>
            Soit de prendre la dernière carte de la défausse pour l'intégrer à
            son jeu (voir B).
          </li>
          <li>
            Soit de piocher une carte et effectuer une des actions précédentes
            (A ou B).
          </li>
        </ul>
      </div>
      <div className="flex flex-cols justify-center items-center pt-10 pb-4">
        <SmallSubtitle title="Défausse rapide" />
      </div>
      <div>
        <p className="text-quinary pt-4 pl-4 pr-4">
          Lorsqu'un joueur défausse une de ses cartes au cours de son tour,
          n'importe lequel des autres joueurs peut poser sur cette défausse une
          carte de même valeur, issue des cartes disposées devant lui.
        </p>
        <p className="text-quinary pt-4 pl-4 pr-4">
          Un joueur peut défausser une carte même après l'annoncement d'un Gabo.
        </p>
      </div>
      <div className="flex flex-cols justify-center items-center pt-10 pb-4">
        <SmallSubtitle title="Fin d'une manche" />
      </div>
      <div>
        <p className="text-quinary pt-4 pl-4 pr-4">
          Au fur et à mesure des tours, les joueurs doivent abaisser la valeur
          de leur main (cartes disposées face cachées devant eux) en les
          remplaçant par des cartes piochées, en les jetant dans la défausse le
          cas échéant, ou en échangeant ses cartes avec celles de ses
          adversaires en cas de pouvoir.
        </p>
        <p className="text-quinary pt-4 pl-4 pr-4">
          Le joueur ajoutant la valeur de ses cartes et obtenant un résultat
          inférieur ou égal à 7 points annonce ensuite le "Gabo" A ce moment la,
          l'ensemble des joueurs dévoile ses cartes.
        </p>
        <p className="text-quinary pt-4 pl-4 pr-4">
          Le vaiqueur récolte 0 points, tandis que le reste additione le poid de
          chaque carte qu'il a en sa possession. Plusieurs joueurs peuvent
          annoncer Gabo même après la première annonce, on se retrouve dans une
          situation ou plusiuers joueurs peuvent récolter 0 points en une
          manche.
        </p>
        <p className="text-quinary pt-4 pl-4 pr-4">
          NB: Si un joueur se défausse de toutes ses cartes, la manche se
          termine automatiquement et personne ne peut annoncer "Gabo". Dans le
          cas ou le joueur annonce le gabo, et avant la révélation des cartes un
          joueur se défausse de toutes ses cartes. Le gabo est annulé , la
          manche se termine aussi.
        </p>
      </div>
      <div className="flex flex-cols justify-center items-center pt-10 pb-4">
        <SmallSubtitle title="Poids des cartes" />
      </div>
      <div className="flex flex-wrap justify-center ">
        <MiniCard icon="A" pts="1" />
        <MiniCard icon="2" pts="2" />
        <MiniCard icon="3" pts="3" />
        <MiniCard icon="4" pts="4" />
        <MiniCard icon="5" pts="5" />
        <MiniCard icon="6" pts="6" />
        <MiniCard icon="7" pts="7" />
        <MiniCard icon="8" pts="8" />
        <MiniCard icon="9" pts="9" />
        <MiniCard icon="10" pts="10" />
        <MiniCard icon="V" pts="11" />
        <MiniCard icon="D" pts="12" />
        <MiniCard icon="R" pts="13" />
        <MiniCard icon="R" color="red" pts="0" />
      </div>
      <div className="flex flex-cols justify-center items-center pt-10 pb-4">
        <SmallSubtitle title="Pouvoirs des cartes" />
      </div>
      <div>
        <p className="text-quinary pt-4 pl-4 pr-4">
          Lorsqu'une des cartes citées ci-dessous est piochée puis défaussée par
          un joueur, il peut, s'il le souhaite, exercer le pouvoir conféré à
          cette carte.
        </p>
      </div>
      <div className="flex flex-cols justify-center">
        <MiniCard
          icon={"7"}
          icon2="8"
          text={
            "Possibilité de regarder une de ses propres cartes, puis de la reposer toujours face cachée au même endroit"
          }
        />
        <MiniCard
          icon={"9"}
          icon2="10"
          text={
            "Possibilité de regarder une des cartes d'un adversaire, puis de la reposer toujours face cachée au même endroit."
          }
        />
        <MiniCard
          icon={"V"}
          text={
            "Possibilité d'échanger à l'aveugle une de ses cartes avec celle d'un adversaire. Interdiction pour les joueurs de regarder les cartes ainsi échangées (possibilité ultérieure à l'aide du pouvoir des cartes 7 et 8). Aucun Gabo ne peut être annoncé avant que le joueur n'ait effectué son choix."
          }
        />
        <MiniCard
          icon={"D"}
          text={
            "Possibilité de regarder la carte d'un adversaire et possibilité de l'échanger avec l'une de ses cartes. Aucun Gabo ne peut être annoncé avant que le joueur n'ait effectué son choix."
          }
        />
      </div>
      <div className="flex flex-cols justify-center items-center pt-10 pb-4">
        <SmallSubtitle title="Pénalité" />
      </div>
      <div>
        <ul className="text-quinary pt-4 pb-2 pl-10 pr-4 list-disc">
          <li>
            Si un joueur regarde une de ses cartes qu'il a oublié ou qu'il se
            défausse d'une carte qui se retrouve ne pas être la bonne, il est
            pénalisé en prenant la première carte de la pioche sans la regarder
            et en la disposant face cachée devant lui, se rajoutant ainsi une
            nouvelle carte inconnue à gérer.
          </li>
          <li>
            Pénalité A: Si un joueur annonce "Gabo", hors il se retrouve avec un
            score supérieur à 7. Lors du décompte des points, il auras une
            pénalité de +25 points.
          </li>
          <li>
            Pénalité B: Si un joueur se retrouve victime d'un "Contre-Gabo"
            (voir la section Contre-Gabo). Lors du décompte des points, il auras
            une pénalité de +50 points.
          </li>
          <li>
            Pénalité C: Un Gabo est annoncé, Le scenario de la pénalité A
            devrait être appliqué mais au moment ou elle se passe, mais 2 autres
            joueurs (pour n'importe quelle parti a "n" joueurs) ont plus ou égal
            25 points de carte. La pénalité C s'applique, les joueurs ayant plus
            ou égal de 25 en points, prenne la pénalité A. La personne ayant
            annoncé le gabo: prend la pénalité A ~et~ la somme des points de ses
            cartes.
          </li>
        </ul>
      </div>
      <div>
        <p className="text-quinary pt-4 pl-4 pr-4">
          NB: Si un joueur prends la pénalité (A) il est dans l'impossibilité de
          prendre la pénalité (B) pendant la même manche.
        </p>
      </div>
      <div className="flex flex-cols justify-center items-center pt-10 pb-4">
        <SmallSubtitle title="Contre-Gabo - Bataille" />
      </div>
      <div>
        <p className="text-quinary pt-4 pl-4 pr-4">
          Lorsqu'un joueur annonce Gabo, on passe alors en phase de
          "Contre-Gabo".
        </p>
        <p className="text-quinary pt-4 pl-4 pr-4">
          Si un joueur pense contesté le Gabo de son adversaire il peut annoncer
          un "Contre-Gabo" et tout les autres joueurs ayant annoncé Gabo se
          retrouvent dans *La Bataille* Le joueur ayant annoncé le premier Gabo
          peut aussi annoncer le Contre-Gabo en réaction au Gabo d'un autre
          joueur.
        </p>
        <p className="text-quinary pt-4 pl-4 pr-4">
          Tout autres joueurs annonçant un Gabo après l'annonce du Contre-Gabo
          se retrouve dans la *Battaille* et se doit de comparer ses cartes avec
          les autres joueurs aussi.
        </p>
        <p className="text-quinary pt-4 pl-4 pr-4">
          Le(s) joueur(s) ayant le plus de point parmis les joueurs dans la
          *Bataille* se récolte une pénalité de +50 points.
        </p>
      </div>
      <div className="flex flex-cols justify-center items-center pt-10 pb-4">
        <SmallSubtitle title="Redescente" />
      </div>
      <div>
        <p className="text-quinary pt-4 pl-4 pr-4">
          Lorsqu'un joueur atteint le score de 50, son score retombe a 25.
        </p>
        <p className="text-quinary pt-4 pl-4 pr-4">
          Lorsqu'un joueur atteint le score de 100, son score retombe a 50.
        </p>
        <p className="text-quinary pt-4 pl-4 pr-4">
          Un joueur ne peut pas redescendre la même manche ou il subit une
          pénalité (A) ou (B)
        </p>
      </div>
    </div>
  );
}

export default RulesText;
