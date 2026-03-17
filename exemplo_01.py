from time import sleep
from loguru import logger

def primeira_atividade():
    logger.info("minha primeira atividade!")
    sleep(2)

def segunda_atividade():
    logger.info("minha segunda atividade")
    sleep(2)

def terceira_atividade():
    logger.info("minha terceira atividade")
    sleep(2)

def pipeline():
    primeira_atividade()
    segunda_atividade()
    terceira_atividade()
    logger.success("pipeline finalizou!")

if __name__ == "__main__":
    pipeline()