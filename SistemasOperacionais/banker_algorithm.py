class BankersAlgothm:

    def __init__(self):
        self.process_count = None
        self.type_count = None
        self.matrix_resources = []
        self.free_resource = 0

    def get_data(self):
        self.process_count = int(input('informe a quantidade de processos em execução\n>>> '))
        self.type_count = int(input('Informe a quantidade de recursos que serão utilizadas pelos processos\n>>> '))
        self.get_process_matrix()

    def get_process_matrix(self):
        resource_execute_total = 0
        for i in range(self.process_count):
            process_input = int(input('Digite a quantidade de recursos utilizados no processo {}\n>>> '.format(i+1)))
            necessary_input = int(input('Digite a quantidade de recursos que o processo {} necessita\n>>> '.format(i+1)))
            resource_execute_total += process_input
            self.matrix_resources.append({
                'process': i + 1,
                'execute': process_input,
                'necessary': necessary_input
            })
        self.free_resource = self.type_count - resource_execute_total

    def show_matrix(self):
        print('='*30)
        for item in self.matrix_resources:
            print('{} | {} | {}'.format(item['process'], item['execute'], item['necessary']))
        print('Free: {}'.format(self.free_resource))
        print('='*30)


def main():
    banker = BankersAlgothm()
    banker.get_data()
    banker.show_matrix()


if __name__ == "__main__":
    main()
