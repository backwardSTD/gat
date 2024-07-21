import os,sys,platform
import sqlite3
import shlex
import db.gatcolumn as gatcolumn

__all__ = ['GatSQL']

class GatSQL:

    def __init__(self, db_path):
        self.DBPATH = db_path
        self.con = sqlite3.connect(self.DBPATH)


    def print_table(data, title:bool):    # =>  2-dimention list of table # include title
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
        print("Checking table existance of name '{}'".format(table))
        cur = self.con.execute("SELECT * FROM {}".format(table))
        result = cur.fetchall

        if result is None:
            return False
        else:
            return True
        

    def _check_dub_col(self, table, col, row):
        ...
    #    self.con.execute("SELECT

    
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
            

    def add_new_row(self, table ,**add_kwargs):
        if ( self._db_check_new(table) ):
            cur = self.con.cursor()
            cur.execute("""SELECT * FROM pragma_table_info('{}')""".format(table))
            col = cur.fetchall()
            column_list = []

            for _ in col:
                column_list.append(_[1])
            print(column_list)

            _i_items = []
            _i_values = []
            for item, value in add_kwargs.items():
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
        
    def find_row_from_column(self, table, **add_kwargs):
        ... 