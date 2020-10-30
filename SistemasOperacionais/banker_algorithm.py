class ProcessInfoModel:

    def __init__(self, id, execute_qtd, required_qtd):
        self.process_id = id
        self.execute = execute_qtd
        self.required = required_qtd


class BankersAlgothm:

    def __init__(self):
        self.process_count = None
        self.resource_count = None
        self.resources_matrix = []
        self.free_resources = 0

    def get_data(self):
        self.process_count = int(input('Quantidade de processos\n>>> '))
        self.resource_count = int(input('Quantidade de instâncias do processos\n>>> '))
        self.get_resources_matrix()

    def get_resources_matrix(self):
        resource_execute_total = 0
        for i in range(self.process_count):
            process_input = int(input('Digite a quantidade de recursos utilizados no processo {}\n>>> '.format(i+1)))
            required_input = int(input('Digite a quantidade de recursos que o processo {} necessita\n>>> '.format(i+1)))
            resource_execute_total += process_input
            process_info = ProcessInfoModel(i, process_input, required_input)
            self.resources_matrix.append(process_info)
        self.free_resources = self.resource_count - resource_execute_total

    def verify_deadlock(self):
        is_valid = True

    def show_matrix(self):
        print('='*30)
        for item in self.matrix_resources:
            print('{} | {} | {}'.format(item['process'], item['execute'], item['necessary']))
        print('Free: {}'.format(self.free_resource))
        print('='*30)

    def show_matrix(self):
        print('='*30)
        for process_info in self.resources_matrix:
            print('P{} | {} | {}'.format(process_info.process_id, process_info.execute, process_info.required))
        print('Free: {}'.format(self.free_resources))
        print('='*30)

