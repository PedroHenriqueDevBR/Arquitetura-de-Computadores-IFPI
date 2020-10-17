from copy import copy

class Process:

    def __init__(self, process_id, cpu_time):
        self.process_id = process_id
        self.cpu_time = cpu_time
        self.turnaround = 0


class CircleAlgorithm:

    def __init__(self):
        self.process = []
        self.change_timer = 0
        self.quantum = 0

    def get_informations(self):
        self.change_timer = int(input('Qual é o tempo de troca: '))
        self.quantum = int(input('Qual é o quantum: '))
        self._get_process()

    def _get_process(self):
        process_count = int(input('Digite a quantidade de processos: '))

        for i in range(process_count):
            print('='*50)
            print('Dados do processo {}'.format(i))
            print('='*50)

            cpu_time = int(input('Tempo de CPU: '))
            process = Process(i, cpu_time)
            self.process.append(process)

    def show_process(self):
        print('-'*10)
        for process_item in self.process:
            print('P{} | {} | {}'.format(process_item.process_id, process_item.cpu_time, process_item.turnaround))
            print('-'*10)

    def calc_turnaround(self):
        process_list_aux = self.process
        quantum_count = 0

        while True:
            for aux_process in process_list_aux:
                process = copy(aux_process)
                if self.quantum - process.cpu_time >= 0:
                    quantum_count += process.cpu_time
                    process.cpu_time -= process.cpu_time
                    process.turnaround = quantum_count
                else:
                    quantum_count += self.quantum
                    process.cpu_time -= quantum_count

            done = True
            for process in process_list_aux:
                if process.cpu_time > 0:
                    done = False
            if done:
                break

        for i in range(len(process_list_aux)):
            self.process[i].turnaround = process_list_aux[i].turnaround


def main():
    circle_algorithm = CircleAlgorithm()
    circle_algorithm.get_informations()
    circle_algorithm.calc_turnaround()
    circle_algorithm.show_process()


if __name__ == '__main__':
    main()