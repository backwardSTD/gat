import sys, os ,platform
import argparse
import sqlite3
from util.gatsql import *
from db.gatcolumn import *


DB_PATH = "tutorial.db"


aaa = GatSQL(DB_PATH)

data = [
    [33, 53, 62, 64, 20, 98, 28, 89, 57, 88],
    [7, 45, 13, 30, 43, 93, 3, 58, 1, 68],
    [82, 77, 69, 32, 10, 17, 73, 18, 25, 94],
    [11, 21, 54, 60, 23, 65, 71, 50, 38, 56],
    [36, 87, 42, 75, 52, 12, 24, 41, 4, 84],
    [59, 8, 78, 95, 31, 19, 14, 39, 99, 5],
    [46, 66, 67, 85, 15, 2, 92, 16, 91, 70],
    [61, 35, 74, 81, 27, 9, 96, 29, 26, 40],
    [76, 6, 97, 34, 79, 55, 22, 47, 48, 90],
    [49, 37, 51, 63, 72, 44, 80, 86, 83, 87],
]

GatSQL.print_table(data, True)

#aaa.create_new_table(SAMSUNG_PDK)
#aaa.add_new_row('gat_pdk', **{'product_name' : 'LN08LPP_CalibreDRC_S00_V1.0.1.0_DRC',
#                              'hash' : '234lknsdf9swlsksd',
#                              'product_type': 'CalibreDRC',
#                              'foundry': 'samsung',
#                              'process': '111',
#                              'architecture': 'consumer'})