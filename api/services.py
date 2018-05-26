from clients.fagsystem import Fagsystem
from  clients.brevtjeneste import Brevtjeneste

fagsystem = Fagsystem()
brevtjenste = Brevtjeneste()


def create_avtale(kunde_info) -> (str, str):
    kunde_nummer, kunde_mail = fagsystem.opprett_kunde(kunde_info)
    avtale_nummer = fagsystem.opprett_avtale(kunde_nummer)

    status_utsendelse = send_email(kunde_mail, avtale_nummer)
    fagsystem.oppdater_avtale(avtale_nummer, status_utsendelse)

    """
        Usikker på hva som ønskes med følgende tekst. Skulle helst ha en rollback som unngår
        mismatch i det hele tatt, men vi får vel si ifra til klient:

        `Konsekvensen av at kallet mot fagsystemet oppdater status feiler, vil være at avtalen
        ikke blir kativert noe som resulterer i en mismatch mellom det som informeres til
        kunde og status på avtalen i fagsystemet.`
    """

    return (avtale_nummer, status_utsendelse)


def send_email(kunde_mail, avtale_nummer) -> bool:
    status = brevtjenste.send_mail(kunde_mail, "ny avtale {}".format(avtale_nummer))

    if status is True:
        return 'Avtale sendt'
    return 'Avtale ble opprettet men ikke sendt. Kontakt support med avtalenummer'
