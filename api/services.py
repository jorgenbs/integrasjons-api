from clients.fagsystem import Fagsystem

fagsystem = Fagsystem()


def create_avtale(kunde_info) -> (str, str):
    kunde_nummer = fagsystem.opprett_kunde(kunde_info)
    avtale_nummer = fagsystem.opprett_avtale(kunde_nummer)

    status = send_email(kunde_nummer, avtale_nummer)

    return (avtale_nummer, status)


def send_email(kunde_nummer, avtale_nummer):
    pass
