def tempo():
    tempo = input("")
    total_tempo = int(tempo)

    horas = total_tempo // 3600
    segs_restantes = total_tempo % 3600
    minutos = segs_restantes // 60
    segundos = segs_restantes % 60

    print(horas,minutos,segundos, sep = ':')
def main():
    tempo()

if __name__ == '__main__' :
    main()
