from clients.fagsystem import Fagsystem

fagsystem = Fagsystem()


def create_avtale(kunde_info) -> (str, int):
    kunde_nummer = fagsystem.opprett_kunde(kunde_info)
    avtale_nummer = fagsystem.opprett_avtale(kunde_nummer)

    send_email(kunde_nummer, avtale_nummer)

    return (avtale_nummer, 1)


def send_email():
    pass