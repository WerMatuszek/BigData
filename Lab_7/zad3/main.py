import FileUser as FU

if __name__ == '__main__':
    df = FU.FileReadCSV("2010-12-01.csv")
    df.show()
    df2 = FU.HighestFive(df, "UnitPrice")
    df2.show()
    FU.FileSaveCSV(df2, "Highest5PriceUnit.csv")
