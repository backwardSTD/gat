import sys, os ,platform
import argparse
import sqlite3
from util.gatsql import *
from db.gatcolumn import *
from util.table import *


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

test = Table(DB_PATH)
test.savedb()
test.createTable('gat_pdk', SAMSUNG_PDK)
test.dropTable('gat_pdk')