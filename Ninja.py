import sqlite3 as sl
import pandas as pd
import pyodbc as db
import os

class Source( ):
    '''Provides list of Budget Execution tables
    across two databases (data and references)'''
    __data = [ ]
    __references = [ ]

    @property
    def data( self ):
        ''' Property used to store table names in a list '''
        if self.__data is not None:
            return list( self.__data )

    @property
    def references( self ):
        ''' Property used to store table names in a list '''
        if self.__references is not None:
            return list( self.__references )

    def __init__( self ):
        '''Constructor for the Source class providing
        a list of tables in the data database and/or
        reference database'''
        self.__data = [ 'Allocations', 'ApplicationTables', 'CarryoverEstimates',
                        'CarryoverSurvey', 'Changes', 'CongressionalReprogrammings',
                        'Deobligations', 'Defactos', 'DocumentControlNumbers',
                        'Obligations', 'OperatingPlans', 'OperatingPlanUpdates',
                        'ObjectClassOutlays', 'CarryoverOutlays', 'UnobligatedAuthority',
                        'QueryDefinitions', 'RegionalAuthority', 'SpendingRates',
                        'GrowthRates', 'ReimbursableAgreements', 'ReimbursableFunds',
                        'ReimbursableSurvey', 'Reports', 'StatusOfAppropriations',
                        'BudgetControls', 'AppropriationDocuments', 'BudgetDocuments',
                        'Apportionments', 'BudgetOutlays', 'BudgetResourceExecution',
                        'Reprogrammings', 'SiteActivity', 'SiteProjectCodes',
                        'StatusOfFunds', 'Supplementals', 'Transfers',
                        'HeadquartersAuthority', 'TravelObligations', 'StatusOfAppropriations',
                        'StatusOfJobsActFunding', 'StatusOfSupplementalFunding', 'SuperfundSites',
                        'PayrollAuthority', 'TransTypes', 'ProgramFinancingSchedule',
                        'PayrollRequests', 'CarryoverRequests', 'CompassLevels',
                        'AdministrativeRequests', 'OpenCommitments', 'Expenditures',
                        'UnliquidatedObligations' ]

        self.__references = [ 'Accounts', 'ActivityCodes', 'AllowanceHolders',
                              'Appropriations', 'BudgetObjectClasses',
                              'CostAreas', 'CPIC', 'Divisions',
                              'Documents', 'FederalHolidays', 'FinanceObjectClasses',
                              'FiscalYears', 'FiscalYearsBackUp', 'Funds',
                              'Goals', 'GsPayScale', 'Images',
                              'Messages', 'NationalPrograms', 'Objectives',
                              'Organizations', 'ProgramAreas', 'ProgramDescriptions',
                              'ProgramProjects', 'Projects', 'Providers',
                              'ReferenceTables', 'ResourcePlanningOffices', 'ResponsibilityCenters',
                              'SchemaTypes', 'Sources' ]

class Provider( ):
    '''Provides data providers used to identify
    the type of database (access, sqlite, sqlserver, or sqlce)'''
    __access = None
    __sqlite = None
    __sqlce = None
    __mssql = None
    __oledb = None

    @property
    def access( self ):
        ''' Property used to identify
         access provider '''
        if self.__access is not None:
            return self.__access

    @property
    def sqlite( self ):
        ''' Property used to identify
         sqlite provider '''
        if self.__sqlite is not None:
            return self.__sqlite

    @property
    def sqlserver( self ):
        ''' Property used to identify
         sql server provider '''
        if self.__mssql is not None:
            return self.__mssql

    @property
    def sqlce( self ):
        ''' Property used to identify sqlserver
         compact provider '''
        if self.__sqlce is not None:
            return self.__sqlce

    @property
    def excel( self ):
        ''' Property used to identify excel provider '''
        if self.__oledb is not None:
            return self.__oledb

    def __init__( self ):
        self.__access = 'ACCDB'
        self.__sqlite = 'DB'
        self.__sqlce = 'SDF'
        self.__mssql = 'MDF'
        self.__oledb = 'XLSX'

class CommandType( ):
    '''defines the types of sql commands
    used to query the database'''
    __select = None
    __insert = None
    __update = None
    __delete = None
    __createtable = None
    __createview = None
    __altertable = None
    __altercolumn = None
    __type = None

    @property
    def select( self ):
        return self.__select

    @property
    def insert( self ):
        return self.__insert

    @property
    def update( self ):
        return self.__update

    @property
    def createtable( self ):
        return self.__createtable

    @property
    def createview( self ):
        return self.__createview

    @property
    def delete( self ):
        return self.__delete

    @property
    def altertable( self ):
        return self.__altertable

    @property
    def altercolumn( self ):
        return self.__altercolumn

    def setcommand( self, cmd ):
        '''Function to set the type of sql command that
        will be used to query the database'''
        if isinstance( cmd, str ) and cmd == 'SELECT':
            self.__type = self.__select
        elif cmd == 'INSERT':
            self.__type = self.__insert
        elif cmd == 'DELETE':
            self.__type = self.__delete
        elif cmd == 'UPDATE':
            self.__type = self.__update
        elif cmd == 'CREATE TABLE':
            self.__type = self.__createtable
        elif cmd == 'CREATE VIEW':
            self.__type = self.__createview
        elif cmd == 'ALTER TABLE':
            self.__type = self.__altertable
        elif cmd == 'ALTER COLUMN':
            self.__type = self.__altercolumn
        else:
            self.__type = self.__select

    def __init__( self, cmd ):
        '''constructor for the CommandType class'''
        self.__select = 'SELECT'
        self.__insert = 'INSERT'
        self.__delete = 'DELETE'
        self.__update = 'UPDATE'
        self.__createtable = 'CREATE TABLE'
        self.__createview = 'CREATE VIEW'
        self.__altercolumn = 'ALTER COLUMN'
        self.__altertable = 'ALTER TABLE'
        self.setcommand( cmd )

    def __str__( self ):
        if self.__type is not None:
            return str( self.__type )

class DataPath( ):
    ''' Defines object used to provide the path to data model databases '''
    __accesspath = None
    __sqlitepath = None
    __mssqlpath = None

    @property
    def access( self ):
        if self.__accesspath is not None:
            return str( self.__accesspath )

    @access.setter
    def access( self, path ):
        if path is not None:
            self.__accesspath = str( path )

    @property
    def sqlite( self ):
        if self.__sqlitepath is not None:
            return str( self.__sqlitepath )

    @sqlite.setter
    def sqlite( self, path ):
        if path is not None:
            self.__sqlitepath = str( path )

    @property
    def sqlserver( self ):
        if self.__mssqlpath is not None:
            return str( self.__mssqlpath )

    @sqlserver.setter
    def sqlserver( self, path ):
        if path is not None:
            self.__mssqlpath = str( path )

    def __init__( self ):
        self.__accesspath = r'C:\Users\terry\source\repos\BudgetPy' \
                            r'\db\access\datamodels\Data.accdb'
        self.__sqlitepath = r'C:\Users\terry\source\repos\BudgetPy' \
                            r'\db\sqlite\datamodels\Data.db'
        self.__mssqlpath = r'C:\Users\terry\source\repos\BudgetPy' \
                           r'\db\mssql\datamodels\Data.mdf'

class ReferencePath( ):
    '''Defines object used to provide paths to the references model databases '''
    __accesspath = None
    __sqlitepath = None
    __mssqlpath = None

    @property
    def access( self ):
        if self.__accesspath is not None:
            return str( self.__accesspath )

    @access.setter
    def access( self, path ):
        if os.path.exists( path ):
            self.__accesspath = str( path )

    @property
    def sqlite( self ):
        if self.__sqlitepath is not None:
            return str( self.__sqlitepath )

    @sqlite.setter
    def sqlite( self, path ):
        if os.path.exists( path ):
            self.__sqlitepath = str( path )

    @property
    def sqlserver( self ):
        if self.__mssqlpath is not None:
            return str( self.__mssqlpath )

    def __init__( self ):
        self.__accesspath = r'C:\Users\terry\source\repos\BudgetPy' \
                            r'\db\access\referencemodels\References.accdb'
        self.__sqlitepath = r'C:\Users\terry\source\repos\BudgetPy' \
                            r'\db\sqlite\referencemodels\References.db'
        self.__mssqlpath = r'C:\Users\terry\source\repos\BudgetPy' \
                           r'\db\mssql\referencemodels\References.mdf'

class CriteriaBuilder( ):
    '''Defines the CriteriaBuilder class'''
    __criteria = None
    __cmd = None

    @property
    def command( self ):
        if self.__cmd is not None:
            return self.__cmd

    @command.setter
    def command( self, cmd ):
        if isinstance( cmd, CommandType ):
            self.__cmd = cmd

    @property
    def pairs( self ):
        ''' builds criteria from name value pairs'''
        if isinstance( self.__criteria, dict ):
            return self.__criteria

    @pairs.setter
    def pairs( self, namevaluepairs ):
        ''' builds criteria from name value pairs'''
        if isinstance( namevaluepairs, dict ):
            self.__criteria = namevaluepairs

    def create( self ):
        if self.__criteria is not None:
            for name, value in self.__criteria:
                criteria = ''
                criteria += f'{name} = {value} AND'
                criteria.rstrip( ' AND' )
                return criteria

    def __init__( self, nvp, cmd ):
        self.__criteria = nvp if isinstance( nvp, dict ) else None
        self.__cmd = cmd if isinstance( cmd, CommandType ) else CommandType( 'SELECT' )

class SqlStatement( ):
    '''Class representing the sql queries
    used in the application'''
    __provider = None
    __command = None
    __path = None
    __table = None

    @property
    def provider( self ):
        if self.__provider is not None:
            return self.__provider

    @provider.setter
    def provider( self, pdr ):
        if isinstance( pdr, Provider ):
            self.__provider = pdr
        else:
            provider = Provider( )
            self.__provider = provider.sqlite

    @property
    def command( self ):
        if self.__command is not None:
            return self.__command

    @command.setter
    def command( self, cmd ):
        if isinstance( cmd, CommandType ):
            self.__command = cmd
        else:
            command = CommandType( 'SELECT' )
            self.__command = command

    @property
    def table( self ):
        if self.__table is not None:
            return self.__table

    @table.setter
    def table( self, src ):
        if isinstance( src, Source ):
            self.__table = src
        else:
            source = Source( )
            self.__table = source.data

    @property
    def sqlpath( self ):
        if self.__path is not None:
            return self.__path

    @sqlpath.setter
    def sqlpath( self, path ):
        if isinstance( path, DataPath ):
            self.__path = path
        else:
            model = DataPath( ).sqlite
            self.__path = model

    def __init__( self, pvdr, cmd, src, path = None ):
        self.__provider = pvdr if isinstance( pvdr, Provider ) else Provider( ).sqlite
        self.__command = cmd if isinstance( cmd, CommandType ) else CommandType( 'SELECT' )
        self.__table = src if isinstance( src, Source ) else Source( ).data
        self.__path = path if isinstance( path, DataPath ) else DataPath( ).sqlite

class DataRow( sl.Row ):
    '''Defines the DataRow Class'''
    __source = None
    __names = None
    __items = None
    __data = None
    __values = None
    __id = None

    @property
    def index( self ):
        if isinstance( self.__id, int ):
            return self.__id

    @index.setter
    def index( self, ordinal ):
        if isinstance( ordinal, int ):
            self.__id = ordinal

    @property
    def data( self ):
        if self.__data is not None:
            return dict( self.__data )

    @data.setter
    def data( self, items ):
        if isinstance( items, dict ):
            self.__items = items

    @property
    def items( self ):
        if isinstance( self.__items, tuple ):
            return self.__items

    @items.setter
    def items( self, data ):
        if isinstance( data, tuple ):
            self.__items = data

    @property
    def names( self ):
        if self.__names is not None:
            return self.__names

    @names.setter
    def names( self, data ):
        if isinstance( data, dict ):
            self.__names = data.keys( )

    @property
    def values( self ):
        if self.__values is not None:
            return list( self.__values )

    @values.setter
    def values( self, items ):
        if isinstance( items, list ):
            self.__values = items

    @property
    def source( self ):
        if self.__source is not None:
            return self.__source

    @source.setter
    def source( self, row ):
        if isinstance( row, sl.Row ):
            self.__source = row

    def __init__( self, items = None ):
        super( ).__init__( items )
        self.__source = sl.Row( )
        self.__items = dict( items )
        self.__id = int( items[ 0 ] )
        self.__names = list( self.__items.keys( ) )
        self.__values = self.__items.values( )

    def __str__( self ):
        return 'Row ID: ' + str( self.__id )

class DataColumn( ):
    '''Defines the DataColumn Class'''
    __base = None
    __source = None
    __row = None
    __name = None
    __value = None
    __type = None
    __caption = None
    __id = None
    __table = None
    __data = None

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, name ):
        if name is not None:
            self.__name = str( name )

    @property
    def value( self ):
        if self.__value is not None:
            return self.__value

    @value.setter
    def value( self, value ):
        if value is not None:
            self.__value = value

    @property
    def type( self ):
        if self.__type is not None:
            return self.__type
        else:
            return 'NS'

    @type.setter
    def type( self, typ ):
        if typ is not None:
            self.__type = str( type( typ ) )

    @property
    def caption( self ):
        if self.__caption is not None:
            return self.__caption

    @caption.setter
    def caption( self, text ):
        if text is not None:
            self.__caption = str( text )

    @property
    def ordinal( self ):
        if self.__id > -1:
            return self.__id

    @ordinal.setter
    def ordinal( self, index ):
        if isinstance( index, int ):
            self.__id = index

    @property
    def table( self ):
        if self.__table is not None:
            return self.__table

    @table.setter
    def table( self, name ):
        if name is not None:
            self.__table = str( name )

    @property
    def row( self ):
        if self.__row is not None:
            return self.__row

    @row.setter
    def row( self, items ):
        if isinstance( items, dict ):
            self.__base = items
            self.__row = self.__base

    @property
    def source( self ):
        if self.__source is not None:
            return self.__source

    @source.setter
    def source( self, table ):
        if table is not None:
            self.__source = str( table )

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @property
    def isnumeric( self ):
        if not isinstance( self.__value, str ):
            return True

    @property
    def istext( self ):
        if isinstance( self.__value, str ):
            return True

    def __init__( self, name, value ):
        self.__name = str( name )
        self.__value = value
        self.__base = { self.__name: self.__value }
        self.__data = { 'ordinal': self.__id, 'name': self.__name,
                        'caption': self.__caption, 'value': self.__value,
                        'datatype': self.__type, 'table': self.__table }

    def __str__( self ):
        return self.__name

class DataTable( pd.DataFrame ):
    '''Defines the DataTable Class'''
    __base = None
    __name = None
    __data = None
    __columns = None

    @property
    def name( self ):
        if isinstance( self.__name, str ):
            return self.__name

    @name.setter
    def name( self, name ):
        if name is not None:
            self.__name = str( name )

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, dataframe ):
        if isinstance( dataframe, pd.DataFrame ):
            self.__data = pd.DataFrame( dataframe )

    @property
    def schema( self ):
        if self.__columns is not None:
            return self.__columns

    @schema.setter
    def schema( self, columns ):
        if isinstance( columns, dict ):
            self.__columns = pd.Series( columns ).index

    @property
    def rows( self ):
        if self.__rows is not None:
            return self.__rows

    @rows.setter
    def rows( self, items ):
        if isinstance( items, list ):
            self.__rows = items

    def __init__( self, name ):
        super( ).__init__( )
        self.__base = str( name )
        self.__name = self.__base
        self.__data = pd.DataFrame( self.__name )
        self.__rows = [ tuple( r ) for r in self.__data[ 0: ] ]
        self.__columns = self.__data.columns

    def __str__( self ):
        if self.__name is not None:
            return self.__name

class AccessData( ):
    '''Builds the budget execution data classes'''
    __dbpath = None
    __driver = None
    __connstr = None
    __data = None
    __source = None
    __command = None

    @property
    def path( self ):
        if self.__dbpath is not None:
            return str( self.__dbpath )

    @path.setter
    def path( self, path ):
        if path is not None:
            self.__dbpath = str( path )

    @property
    def source( self ):
        if self.__source is not None:
            return self.__source

    @source.setter
    def source( self, src ):
        if isinstance( src, Source ):
            self.__source = src

    @property
    def connstr( self ):
        if self.__connstr is not None:
            return str( self.__connstr )

    @connstr.setter
    def connstr( self, conn ):
        if conn is not None:
            self.__connstr = str( conn )

    @property
    def data( self ):
        if self.__data is not None:
            return iter( self.__data[ 0: ] )

    @data.setter
    def data( self, dframe ):
        if dframe is not None and isinstance( dframe, pd.DataFrame ):
            self.__data = dframe.items

    @property
    def driver( self ):
        if self.__driver is not None:
            return str( self.__driver )

    @driver.setter
    def driver( self, name ):
        if name is not None:
            self.__driver = name

    @property
    def command( self ):
        if self.__command is not None:
            return self.__command
        if self.__command is None:
            cmd = CommandType( 'SELECT' )
            return cmd

    @command.setter
    def command( self, cmd ):
        if isinstance( cmd, CommandType ):
            self.__command = cmd

    def connect( self ):
        if not self.__connstr == '':
            return db.connect( self.__connstr )

    def __init__( self, table ):
        self.__source = table
        self.__driver = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
        self.__dbpath = r'DBQ=C:\Users\terry\source\repos\BudgetPy\db' \
                        r'\access\datamodels\Data.accdb;'
        self.__connstr = f'{self.__driver} {self.__dbpath}'
        self.__data = pd.DataFrame
        self.__command = CommandType( 'SELECT' )

class AccessReference( ):
    '''Builds the budget execution data classes'''
    __dbpath = None
    __driver = None
    __connstr = None
    __data = None
    __source = None
    __command = None

    @property
    def path( self ):
        if self.__dbpath is not None:
            return str( self.__dbpath )

    @path.setter
    def path( self, path ):
        if path is not None:
            self.__dbpath = str( path )

    @property
    def source( self ):
        if self.__source is not None:
            return str( self.__source )

    @source.setter
    def source( self, source ):
        if source is not None:
            self.__source = str( source )

    @property
    def connstr( self ):
        if self.__connstr is not None:
            return str( self.__connstr )

    @connstr.setter
    def connstr( self, conn ):
        if conn is not None:
            self.__connstr = str( conn )

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, dframe ):
        if dframe is not None and isinstance( dframe, pd.DataFrame ):
            self.__data = dframe.items

    @property
    def driver( self ):
        if self.__driver is not None:
            return str( self.__driver )

    @driver.setter
    def driver( self, name ):
        if name is not None:
            self.__driver = name

    @property
    def command( self ):
        if self.__command is not None:
            return self.__command
        if self.__command is None:
            cmd = CommandType( 'SELECT' )
            return cmd

    @command.setter
    def command( self, cmd ):
        if isinstance( cmd, CommandType ):
            self.__command = cmd

    def __init__( self, table = None ):
        self.__source = table
        self.__driver = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
        self.__dbpath = r'DBQ=C:\Users\terry\source\repos\BudgetPy\db\access' \
                        r'\referencemodels\References.accdb;'
        self.__connstr = f'{self.__driver} {self.__dbpath}'
        self.__data = pd.DataFrame
        self.__command = CommandType( 'SELECT' )

    def connect( self ):
        if self.__connstr is not None:
            return db.connect( self.__connstr )

class SQLiteData( ):
    '''Builds the budget execution data classes'''
    __dbpath = None
    __connstr = None
    __data = None
    __source = None
    __command = None

    @property
    def path( self ):
        if self.__dbpath is not None:
            return str( self.__dbpath )

    @path.setter
    def path( self, path ):
        if path is not None:
            self.__dbpath = str( path )

    @property
    def source( self ):
        if self.__source is not None:
            return str( self.__source )

    @source.setter
    def source( self, source ):
        if source is not None:
            self.__source = str( source )

    @property
    def connstr( self ):
        if not self.__dbpath == '':
            return self.__dbpath

    @connstr.setter
    def connstr( self, conn ):
        if conn is not None:
            self.__dbpath = str( conn )

    @property
    def data( self ):
        if isinstance( self.__data, pd.DataFrame ):
            return self.__data

    @data.setter
    def data( self, dframe ):
        if isinstance( dframe, pd.DataFrame ):
            self.__data = dframe

    @property
    def command( self ):
        if self.__command is not None:
            return self.__command
        if self.__command is None:
            cmd = CommandType( 'SELECT' )
            return cmd

    @command.setter
    def command( self, cmd ):
        if isinstance( cmd, CommandType ):
            self.__command = cmd

    def connect( self ):
        if self.__connstr is not None:
            return sl.connect( self.__connstr )

    def __init__( self, table = None ):
        self.__source = str( table )
        self.__dbpath = r'C:\Users\terry\source\repos\BudgetPy' \
                        r'\db\sqlite\datamodels\Data.db'
        self.__connstr = self.__dbpath
        self.__data = pd.DataFrame
        self.__command = CommandType( 'SELECT' )

    def __str__( self ):
        if self.__dbpath is not None:
            return self.__dbpath

class SQLiteReference( ):
    '''Class representing the budget execution references models'''
    __source = None
    __dbpath = None
    __connstr = None
    __data = None
    __command = None

    @property
    def path( self ):
        if self.__dbpath is not None:
            return str( self.__dbpath )

    @path.setter
    def path( self, path ):
        if path is not None:
            self.__dbpath = str( path )

    @property
    def source( self ):
        if self.__source is not None:
            return str( self.__source )

    @source.setter
    def source( self, src ):
        if src is not None:
            self.__source = str( src )

    @property
    def connstr( self ):
        if self.__connstr is not None:
            return str( self.__connstr )

    @connstr.setter
    def connstr( self, conn ):
        if conn is not None:
            self.__connstr = str( conn )

    @property
    def data( self ):
        if self.__data is not None:
            return iter( self.__data[ 0: ] )

    @data.setter
    def data( self, dframe ):
        if dframe is not None:
            self.__data = dframe

    @property
    def command( self ):
        if self.__command is not None:
            return self.__command
        if self.__command is None:
            cmd = CommandType( 'SELECT' )
            return cmd

    @command.setter
    def command( self, cmd ):
        if isinstance( cmd, CommandType ):
            self.__command = cmd

    def connect( self ):
        if self.__connstr is not None:
            return sl.connect( self.__connstr )

    def __init__( self, table = None ):
        self.__source = str( table )
        self.__dbpath = r'C:\Users\terry\source\repos\BudgetPy' \
                        r'\db\sqlite\referencemodels\References.db'
        self.__connstr = self.__dbpath
        self.__data = pd.DataFrame
        self.__data = [ ]
        self.__command = CommandType( 'SELECT' )

class SqlServerData( ):
    '''Builds the budget execution data classes'''
    __source = None
    __dbpath = None
    __data = None
    __connstr = None
    __command = None
    __server = None

    @property
    def path( self ):
        if self.__dbpath is not None:
            return str( self.__dbpath )

    @path.setter
    def path( self, path ):
        if path is not None:
            self.__dbpath = str( path )

    @property
    def server( self ):
        if self.__server is not None:
            return str( self.__server )

    @server.setter
    def server( self, path ):
        if isinstance( path, str ):
            self.__server = path

    @property
    def source( self ):
        if self.__source is not None:
            return str( self.__source )

    @source.setter
    def source( self, source ):
        if source is not None:
            self.__source = str( source )

    @property
    def connstring( self ):
        if not self.__connstr == '':
            return self.__connstr

    @connstring.setter
    def connstring( self, conn ):
        if conn is not None:
            self.__dbpath = str( conn )

    @property
    def data( self ):
        if isinstance( self.__data, pd.DataFrame ):
            return self.__data

    @data.setter
    def data( self, dframe ):
        if isinstance( dframe, pd.DataFrame ):
            self.__data = dframe

    @property
    def command( self ):
        if self.__command is not None:
            return self.__command
        if self.__command is None:
            cmd = CommandType( 'SELECT' )
            return cmd

    @command.setter
    def command( self, cmd ):
        if isinstance( cmd, CommandType ):
            self.__command = cmd

    def __str__( self ):
        if self.__dbpath is not None:
            return self.__dbpath

    def __init__( self, table = None ):
        self.__server = r'(LocalDB)\MSSQLLocalDB'
        self.__source = str( table )
        self.__command = CommandType( 'SELECT' )
        self.__dbpath = r'C:\Users\terry\source\repos\BudgetPy' \
                        r'\db\mssql\datamodels\Data.mdf'
        self.__connstr = self.__dbpath
        self.__data = pd.DataFrame

class SqlServerReference( ):
    '''Class representing the budget execution references models'''
    __source = None
    __dbpath = None
    __data = None
    __connstr = None
    __command = None
    __server = None

    @property
    def path( self ):
        if self.__dbpath is not None:
            return str( self.__dbpath )

    @path.setter
    def path( self, path ):
        if path is not None:
            self.__dbpath = str( path )

    @property
    def source( self ):
        if self.__source is not None:
            return str( self.__source )

    @source.setter
    def source( self, src ):
        if src is not None:
            self.__source = str( src )

    @property
    def connstring( self ):
        if not self.__connstr == '':
            return self.__connstr

    @connstring.setter
    def connstring( self, conn ):
        if isinstance( conn, str ) and os.path.exists( conn ):
            self.__connstr = conn

    @property
    def data( self ):
        if self.__data is not None:
            return iter( self.__data[ 0: ] )

    @data.setter
    def data( self, dframe ):
        if dframe is not None:
            self.__data = dframe

    @property
    def command( self ):
        if self.__command is not None:
            return self.__command
        if self.__command is None:
            cmd = CommandType( 'SELECT' )
            return cmd

    @command.setter
    def command( self, cmd ):
        if isinstance( cmd, CommandType ):
            self.__command = cmd

    def __init__( self, table = None ):
        self.__server = r'(LocalDB)\MSSQLLocalDB'
        self.__source = str( table )
        self.__command = CommandType( 'SELECT' )
        self.__dbpath = r'C:\Users\terry\source\repos\BudgetPy' \
                        r'\db\mssql\referencemodels\References.mdf'
        self.__connstr = self.__dbpath
        self.__data = pd.DataFrame
