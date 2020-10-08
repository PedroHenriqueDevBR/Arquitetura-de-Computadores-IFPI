class BankersAlgothm:

    def __init__(self):
        self.process_count = None
        self.type_count = None
        self.recursos = []

    def get_data(self):
        self.process_count = int(input('informe a quantidade de processos em execução\n> '))
        self.type_count = int(input('Informe a quantidade de recursos que serão utilizadas pelos processos\n> '))
        


def main():
    banker = BankersAlgothm()
    banker.get_data()


if __name__ == "__main__":
    main()