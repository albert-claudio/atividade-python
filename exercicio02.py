dados = ["Ana", 8], ["Bruno", 5], ["Carla", 8], ["Daniel", 10], ["Eva", 4]

students = {}

for name, score in dados:
    if score not in students:
        students[name] = [score]
    else:
        students[name].append(score)

def get_media(tuple):
    return tuple[1]
media = {name: sum(scores) / len(scores) for name, scores in students.items()}

ordered_media = sorted (media.items(), key=get_media)

for name, score in ordered_media:
    print(f"Aluno: {name} - Média: {score:.2f}")



