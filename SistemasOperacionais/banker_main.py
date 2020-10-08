from SistemasOperacionais.banker_algorithm import BankersAlgothm

def main():
    banker = BankersAlgothm()
    banker.get_data()
    if banker.verify_deadlock():
        print('processos em deadlock')
    else:
        print('Não há deadlock entre os processos')


if __name__ == "__main__":
    main()
