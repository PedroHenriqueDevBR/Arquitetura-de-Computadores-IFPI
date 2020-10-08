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
        completed_indexes = []
        while self.free_resources < self.resource_count:
            resource_is_available = False
            process_index = -1

            for process_info in self.resources_matrix:
                if process_info.process_id in completed_indexes:
                    continue
                resource_available_now = process_info.execute + self.free_resources
                if resource_available_now >= process_info.required:
                    resource_is_available = True
                    process_index = process_info.process_id
                    break

            if resource_is_available:
                process_info = self.resources_matrix[process_index]
                amount_execute = process_info.execute
                self.free_resources += amount_execute
                process_info.execute = 0
                completed_indexes.append(process_info.process_id)
                self.show_matrix()
            else:
                return True
        return False

    def show_matrix(self):
        print('='*30)
        for process_info in self.resources_matrix:
            print('P{} | {} | {}'.format(process_info.process_id, process_info.execute, process_info.required))
        print('Free: {}'.format(self.free_resources))
        print('='*30)

