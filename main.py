from bs4 import BeautifulSoup as BS
import requests
import pandas as pd
import src.methods as methods


main_url = 'http://lib.ru/'
sections = [
    'INOOLD/', 'INPROZ/', 'PROZA/',
    'RUSSLIT/', 'LITRA/', 'PXESY/',
    'NEWPROZA/', 'POEEAST/', 'POECHIN/',
    'TALES/', 'PRIKL/', 'RAZNOE/',
    'SOCFANT/', 'INOFANT/', 'RUFANT/',
    'RUSS_DETEKTIW/', 'FILOSOF/'
]

if __name__ == "__main__":
    path = 'tables/authors/lib_ru_authors.csv'
    df = pd.read_csv(path)
    #methods.create_all_authors_table(sections, main_url)
    methods.create_all_tables_books(df)
    #methods.create_table_books_from_table_authors(df, 'ALLPROZA')
    #methods.create_table_authors(main_url+sections[2], sections[2][:-1])
    #methods.create_table_books(main_url+sections[2], sections[2][:-1])
    #methods.download_books(df, df)
    #methods.download_all_books(path)
    # temp_url = "http://www.lib.ru/INOOLD/DUMA/tri.txt"
    #duma = "http://www.lib.ru/INOOLD/DUMA/"
    #methods.create_table_books(duma, 'DUMA')
    # methods.create_table_authors('http://lib.ru/INOOLD/', 'INOOLD')

