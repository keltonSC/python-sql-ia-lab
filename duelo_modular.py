from dataclasses import dataclass


@dataclass(frozen=True)
class Robot:
    name: str
    hull: int
    attack: int
    shield: int


def duel(first, second):
    robots = (first, second)
    hulls = [first.hull, second.hull]
    if any(robot.hull <= 0 or robot.attack < 0 or robot.shield < 0 for robot in robots):
        raise ValueError("Estrutura precisa ser positiva. Ataque e escudo devem ser não negativos.")
    moves = []
    for turn in range(first.hull + second.hull):
        attacker, target = turn % 2, 1 - turn % 2
        damage = max(1, robots[attacker].attack - robots[target].shield)
        hulls[target] = max(0, hulls[target] - damage)
        moves.append((robots[attacker].name, robots[target].name, damage, hulls[target]))
        if hulls[target] == 0:
            return robots[attacker].name, moves
    raise AssertionError("Cada jogada precisa reduzir a estrutura do alvo.")


if __name__ == "__main__":
    winner, log = duel(Robot("Curupira", 12, 5, 1), Robot("Mapinguari", 15, 4, 2))
    for actor, target, damage, hull in log:
        print(f"{actor} ataca {target} por {damage}. Estrutura restante: {hull}.")
    print(f"Vencedor: {winner}")
