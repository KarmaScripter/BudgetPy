import subprocess as sp
from enum import Enum, auto


class Client( Enum ):
    '''Enumeration of auxiliary applications'''
    NS = auto( )
    SQLite = auto( )
    Access = auto( )
    Excel = auto( )
    Linq = auto( )


class App( ):
    '''factory methods for running process'''
    __app = None
    __sqliteclient = None
    __accessclient = None
    __excelapp = None

    @property
    def sqlite( self ):
        if isinstance( self.__sqliteclient, str ) and self.__sqliteclient != '':
            return self.__sqliteclient

    @property
    def access( self ):
        if isinstance( self.__accessclient, str ) and self.__accessclient != '':
            return self.__accessclient

    @property
    def excel( self ):
        if isinstance( self.__excelapp, str ) and self.__excelapp != '':
            return self.__excelapp

    def __init__( self, app ):
        self.__app = app if isinstance( app, Client ) else None
        self.__sqliteclient = r'db\sqlite\gui\SQLiteDatabaseBrowserPortable.exe'
        self.__accessclient = r'C:\Program Files\Microsoft Office\root\Office16\MSACCESS.EXE'
        self.__excelapp = r'C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE'

    def run( self ):
        if isinstance( self.__app, Client ) and self.__app == Client.SQLite:
            sp.Popen( self.__sqliteclient )
        elif isinstance( self.__app, Client ) and self.__app == Client.Access:
            sp.Popen( self.__accessclient )
        elif isinstance( self.__app, Client ) and self.__app == Client.Excel:
            sp.Popen( self.__excelapp )

