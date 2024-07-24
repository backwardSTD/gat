import sys, os ,platform
import argparse
import sqlite3
from util.gatsql import *
from db.gatcolumn import *


DB_PATH = "tutorial.db"


aaa = GatSQL(DB_PATH)

data = [
    ['LN05LPE_CalibreDRC_A00_V1.0.1.0_DRC', 'selfksdflkji39sdfoiksjdfl', 'CalibredDRC', 'samsung', 'LN05LPE', 'automotive'],
    ['LN08LPP_CalibrePERC_S00_V1.0.1.0_PERC', 'selskdfjvsdlkcjvisdof', 'CalibrePERC', 'samsung', 'LN08LPP', 'consumer'],
    ['LN08LPP_CalibreLFD_S00_V1.0.1.0_LFD', 'awefawefwewfaefw', 'CalibreLFD', 'samsung', 'LN08LPP', 'consumer'],
    ['LN08LPP_CalibreVRC_S00_V1.0.1.0_VRC', 'awgheragerfgrefdg', 'CalibreVRC', 'samsung', 'LN08LPP', 'consumer'],
    ['LN08LPP_CalibreFLT_S00_V1.0.1.0_FLT', 'sergedgrrdrgegdfg', 'CalibreFLT', 'samsung', 'LN08LPP', 'consumer'],
    ['LN08LPP_CalibreLVS_S00_V1.0.1.0_LVS', 'dfwfsfeafsdfkjshdfk', 'CalibreLVS', 'samsung', 'LN08LPP', 'consumer'],
    ['LN08LPP_CalibreSmartFill_S00_V1.0.1.0_SmartFill', 'zsdfergfdghfghfhr', 'CalibreSmartFill', 'samsung', 'LN08LPP', 'consumer']
]


for d in data:
    aaa.add_row( 'gat_pdk', *d)


aaa.show_current_table('gat_pdk')

#GatSQL.print_table(data, True)

#aaa.create_new_table(SAMSUNG_PDK)
#aaa.add_new_row('gat_pdk', **{'product_name' : 'LN08LPP_CalibreDRC_S00_V1.0.1.0_DRC',
#                              'hash' : '234lknsdf9swlsksd',
#                              'product_type': 'CalibreDRC',
#                              'foundry': 'samsung',
#                              'process': '111',
#                              'architecture': 'consumer'})