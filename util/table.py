import sqlite3
import sys, os
import inspect
from db.gatcolumn import *

class InitialSetTable:
    def __init__(self, DB_PATH):
        if os.path.isfile(DB_PATH):
            try:
                self.table = sqlite3.connect(DB_PATH)
                print("Reading '{}' done.".format(DB_PATH))
                self.db = DB_PATH
            except Exception as e:
                print(e)
                
    def savedb(self):
        if 'table' in self.__dict__:
            self.table.commit()
            print("Saving '{}' done.".format(self.db))
        else:
            print("How can you use this method???")


    def closedb(self):
        if 'table' in self.__dict__():
            self.table.close()
        else:
            print("How can you use this method???")
        

class Table(InitialSetTable):
    def __init__(self, DB_PATH):
        super().__init__(DB_PATH)

    def checkTable(func):
        def wrapper(self, *args):
            sig = inspect.signature(func)
            bound_args = sig.bind(self, *args)
            bound_args.apply_defaults()
            
            if 'table_name' in bound_args.arguments:
                _table_name = bound_args.arguments['table_name']
                try:
                    self.table.execute("SELECT '{}' FROM sqlite_master WHERE type=?".format(_table_name), ('table',))
                    self.table.cursor().fetchall
                except sqlite3.OperationalError:
                    print("[ERROR] There no table name({}) in datebase.".format(_table_name))
                    
            else:
                print("The method does not have a valid parameter name. ('table_name')")

        return wrapper
    
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

    def createTable(self, table_name, template:str):
        try:
            print("Creating table : '{}'".format(table_name))
            _cur = self.table.cursor()
            _cur.execute(template.format(table_name))
        except Exception as e:
            print(e)
            

    def dropTable(self, table_name):
        print("Drop the beat")
        if ['_cur', '_tn'] in self.__dict__ and ():
            self._cur.execute("DROP TABLE {}".format(self._tn))
            print("[INFO] The opened table has been deleted. You must run 'openTable' again.")
            del self._tn
        else:
            self._cur.execute("DROP TABLE {}".format(table_name))
            print("[INFO] Table name : '{}' is deleted".format(table_name))
            

    @checkTable
    def openTable(self, table_name):
        self._cur = self.table.cursor()
        self._tn = table_name


    def showTable(self):
         if ['_cur', '_tn'] in self.__dict__:
            self._cur.execute("SELECT * FROM {}".format(self._tn))
            col_names = [ row[0] for row in self._cur.description]
            result = []
            result.append(col_names)
            for _ in self._cur.fetchall():
                result.append(list(_))
            self.print_table(True, *result)
    
    def addRow(self, *args, **kwargs):
        if ['_cur', '_tn'] in self.__dict__:
            self._cur.execute("INSERT INTO {} ")
        # Extract list of column name
        self._cur.execute("""SELECT * FROM pragma_table_info('{}')""".format(self._tn))
        col = self._cur.fetchall()
        column_list = []

        for _ in col:
            column_list.append(_[1])

        # Unpack args or kwargs, and insert rows into table.
        if args and kwargs:
            raise ValueError("User either *args or **kwrgs, not both.")
        
        # Case of kwargs (dictionary)
        elif kwargs:
            if ( self._db_check_new(self._tn) ):


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
                                        .format(self._tn, ','.join(_i_items), ','.join(_i_values)))
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