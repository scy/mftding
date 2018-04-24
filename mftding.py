#!/usr/bin/env python3
# coding=utf-8

import xlrd

xls = xlrd.open_workbook("mftexcel2005.xls")

def findeTWert(sheet, geschlecht, alter, wdh):
    # Bestimme Spalte basierend auf Geschlecht und Alter.
    if geschlecht == "m":
        spalte = alter - 5
    else:
        spalte = alter + 9
    for index, zelle in enumerate(sheet.col(spalte)):
        if zelle.value == wdh:
            zeile = index
    return int(sheet.col(0)[zeile].value)

t = findeTWert(xls.sheet_by_name("Übung 1"), "m", 13, 40)

print(t)
