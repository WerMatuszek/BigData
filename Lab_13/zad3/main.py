import FileUser as FU
import logging

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    df = FU.FileReadCSV("2010-12-01.csv")
    df.show()
    df2 = FU.HighestFive(df, "UnitPrice")
    df2.show()
    FU.FileSaveCSV(df2, "Highest5PriceUnit.csv")

    logger.info("INFO INFO INFO")
    logger.warning("WARNING WARNING WARNING")
    logger.error("ERROR ERROR ERROR")
