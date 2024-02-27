from array import array

def import_lista(file):
    lista = []
    with open(file) as f:
        lines = f.read().split('","')
    for line in lines:
        lista.append(line)
    return lista

def search_binary(lista, search_name):
    size_list = len(lista)
    start = 0
    end = size_list - 1

    while start <= end:
        quite = (start+end) // 2
        if lista[quite] == search_name:
            return quite
        elif lista[quite] < search_name:
            start = quite + 1
        elif lista[quite] > search_name:
            end = quite - 1

    return - 1

def main():
    list_of_students = sorted(import_lista("to_path/lista_alunos.txt"))
    for i in range(0, 3500):
        student_position = search_binary(list_of_students, "Zeina")
        print(f"Aluno(a) {list_of_students[student_position]} está na posição {student_position}")

if __name__ == "__main__":
    main()