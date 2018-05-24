from clients.fagsystem import Fagsystem

fagsystem = Fagsystem()

def create_customer(kunde_info) -> (str, int):
    fagsystem.opprett_kunde(kunde_info)
