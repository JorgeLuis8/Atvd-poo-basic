class Televisao:
    def __init__(self):
        self.volume = 0
        self.canal = 1

    def aumentar_volume(self):
        self.volume += 1
        print("Volume:", self.volume)

    def diminuir_volume(self):
        self.volume -= 1
        print("Volume:", self.volume)

    def mudar_canal(self, canal):
        self.canal = canal
        print("Canal:", self.canal)

    def consultar(self):
        print("Volume:", self.volume)
        print("Canal:", self.canal)


class Controle:
    def __init__(self, televisao):
        self.televisao = televisao

    def menu(self):
        opcao = None
        while opcao != "s":
            print("1 - Aumentar volume")
            print("2 - Diminuir volume")
            print("3 - Mudar canal")
            print("4 - Consultar TV")
            print("s - Sair")
            opcao = input("Escolha uma opção: ")
            if opcao == "1":
                self.televisao.aumentar_volume()
            elif opcao == "2":
                self.televisao.diminuir_volume()
            elif opcao == "3":
                canal = int(input("Informe o canal desejado: "))
                self.televisao.mudar_canal(canal)
            elif opcao == "4":
                self.televisao.consultar()

tv = Televisao()
controle = Controle(tv)
controle.menu()
