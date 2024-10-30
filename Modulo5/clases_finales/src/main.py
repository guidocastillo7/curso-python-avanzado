# Ver documentacion y uso de prefect https://www.prefect.io/
from prefect import flow
import logging
from tasks.get_offers import get_offers
from tasks.save_offers import save_offers

log = logging.getLogger()
SKILL = "python"


#@flow(name="LINKEDIN SCRAPER")
def main_flow():
    log.info(f"PROCESO DE EXTRACCION")

    offers = get_offers(SKILL)

    save_offers(offers)
    print("PROCESO FINALIZADO.")


if __name__ == "__main__":
    main_flow()