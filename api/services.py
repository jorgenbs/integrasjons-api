from clients.fagsystem import Fagsystem
from  clients.brevtjeneste import Brevtjeneste

fagsystem = Fagsystem()
brevtjenste = Brevtjeneste()


def create_avtale(kunde_info) -> (str, str):
    kunde_nummer, kunde_mail = fagsystem.opprett_kunde(kunde_info)
    avtale_nummer = fagsystem.opprett_avtale(kunde_nummer)

    status = send_email(kunde_mail, avtale_nummer)

    return (avtale_nummer, status)


def send_email(kunde_mail, avtale_nummer):
    status = brevtjenste.send_mail(kunde_mail, "ny avtale {}".format(avtale_nummer))
    return status
