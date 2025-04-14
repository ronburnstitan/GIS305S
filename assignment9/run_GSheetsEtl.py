from GSheetsEtl import GSheetEtl

if __name__ == '__main__':
    etl_instance = GSheetEtl("https://foo_bar.com", "C:/Users", "GSheets", "C:/Users/my.gdb")

    etl_instance.process()