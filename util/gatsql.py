import os,sys,platform
import sqlite3
import shlex
import db.gatcolumn as gatcolumn
from typing import Any

__all__ = ['GatSQL']

class GatSQL:

    def __init__(self, db_path):
        self.DBPATH = db_path
        self.con = sqlite3.connect(self.DBPATH)


    def print_table(self,title:bool, *data):    # =>  2-dimention list of table # include title
        col_widths = [max(len(str(item)) for item in col) for col in zip(*data)]
        col_cnt = len(data)
        bar_widths = sum(col_widths) + (col_cnt-1)*3
        print("".rjust(bar_widths,'-'))
        i = 0
        for row in data:
            print(" | ".join("{}".format(str(item).ljust(col_widths[i])) for i, item in enumerate(row)))
            if title == True and i == 0:
                print("".rjust(bar_widths,'-'))
                i += 1
    
    
    def _db_check_new(self, table):
        #print("Checking table existance of name '{}'".format(table))
        cur = self.con.execute("SELECT * FROM {}".format(table))
        result = cur.fetchall

        if result is None:
            return False
        else:
            return True
        

    def _check_dub_col(self, table, col, row):
        ...
        #cur = self.con.execute("SELECT ")

    
    def create_new_table(self, column_template: str):
        '''
            column_list : str
            insert create table statement
            refer to db.gatcolumn.py
            >> import db.gatcolumn.py
        '''
        try:
            cur = self.con.execute(gatcolumn.SAMSUNG_PDK)
        except sqlite3.OperationalError as e:
            print(e)
            

    def add_row(self, table , *args: Any, **kwargs: Any ):
        cur = self.con.cursor()

        # Extract list of column name
        cur.execute("""SELECT * FROM pragma_table_info('{}')""".format(table))  
        col = cur.fetchall()
        column_list = []

        for _ in col:
            column_list.append(_[1])

        # Unpack args or kwargs, and insert rows into table.
        if args and kwargs:
            raise ValueError("User either *args or **kwrgs, not both.")
        
        # Case of kwargs (dictionary)
        elif kwargs:
            if ( self._db_check_new(table) ):


                _i_items = []
                _i_values = []
                for item, value in kwargs.items():
                    _i_items.append("'"+item+"'")

                    if type(value).__name__ != str:
                        _i_values.append("'"+value+"'")
                    else:
                        _i_values.append(value)
                try:
                    cur = cur.execute("""INSERT INTO {}({}) VALUES({})"""
                                        .format(table, ','.join(_i_items), ','.join(_i_values)))
                    self.con.commit
                except sqlite3.IntegrityError as e:
                    print(e)
            else:
                print("Can not find table name to add row : {}".format(table))
                return 1
            
        # Case of args (list)
        elif args:
            
            if ( self._db_check_new(table) ):
                _i_items = []
                _i_values = []
                cur.execute("PRAGMA table_info({})".format(table))
                rows = cur.fetchall()
                for row in rows:
                    if row[3] == 0 or row[5] == 1:
                        continue
                    else:
                        _i_items.append("'"+row[1]+"'")

                for value in args:
                    if type(value).__name__ != str:
                        _i_values.append("'"+value+"'")
                    else:
                        _i_values.append(value)
                try:
                    cur = cur.execute("""INSERT INTO {}({}) VALUES({})"""
                                      .format(table, ','.join(_i_items),','.join(_i_values)))
                    self.con.commit
                except sqlite3.IntegrityError as e:
                    print(e)
            else:
                print("Can not find table name to add row : {}".format(table))
                return 1
                      
        
    def show_current_table(self, table):
        cur = self.con.execute(" SELECT * FROM {}".format(table))
        col_names = [ row[0] for row in cur.description ]
        result = []
        result.append(col_names)
        print(col_names)
        for _ in cur.fetchall():
            result.append(list(_))
        self.print_table(True, *result)