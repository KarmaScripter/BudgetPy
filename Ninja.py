'''
  ******************************************************************************************
      Assembly:                BudgetPy
      Filename:                Ninja.py
      Author:                  Terry D. Eppler
      Created:                 05-31-2023

      Last Modified By:        Terry D. Eppler
      Last Modified On:        06-01-2023
  ******************************************************************************************
  <copyright file="Ninja.py" company="Terry D. Eppler">

     This is a Federal Budget, Finance, and Accounting application.
     Copyright ©  2023  Terry Eppler

     Permission is hereby granted, free of charge, to any person obtaining a copy
     of this software and associated documentation files (the “Software”),
     to deal in the Software without restriction,
     including without limitation the rights to use,
     copy, modify, merge, publish, distribute, sublicense,
     and/or sell copies of the Software,
     and to permit persons to whom the Software is furnished to do so,
     subject to the following conditions:

     The above copyright notice and this permission notice shall be included in all
     copies or substantial portions of the Software.

     THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
     INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
     FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT.
     IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
     DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
     ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
     DEALINGS IN THE SOFTWARE.

     You can contact me at:  terryeppler@gmail.com or eppler.terry@epa.gov

  </copyright>
  <summary>
    The Ninja module defines the data transfer objects used in the
    BudgetPy application.
  </summary>
  ******************************************************************************************
  '''
import datetime as dt
from datetime import datetime

from pandas import DataFrame
from sqlite3 import Row
from Booger import Error, ErrorDialog
from Static import SQL
from Static import Source, Provider
from Data import ( DbConfig, SqlConfig, Connection,
                  SqlStatement, BudgetData, DataBuilder )

class Unit( ):
    '''
    Constructor: Unit( id: int )

    Purpose: Base class defines an object
    representing fundemental unit of data
    in the Budget Execution application'''
    __index = None
    __code = None

    @property
    def id( self ) -> int:
        if self.__index is not None:
            return self.__index

    @id.setter
    def id( self, id: int ):
        if id is not None:
            self.__index = id

    def __init__( self, id: int ):
        self.__index = id

    def __str__( self ) -> str:
        if self.__code is not None:
            return self.__code

class DataUnit( Unit ):
    '''
    Constructor: DataUnit( id: int, code: str, name: str )

    Purpose: Base class providing a code and name
    '''
    __index = None
    __code = None
    __name = None

    @property
    def name( self ) -> str:
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, name: str ):
        if name is not None:
            self.__name = name

    @property
    def code( self ) -> str:
        if self.__name is not None:
            return self.__name

    def __init__( self, id: int, code: str, name: str ):
        super( ).__init__( id )
        self.__id = super( ).id
        self.__code = code
        self.__name = name

    def __str__( self ) -> str:
        if self.__code is not None:
            return self.__code

class BudgetUnit( DataUnit ):
    '''
    Constructor: BudgetUnit( id: int, code: str, nam: str, treas: str, main: str )

    Purpose: Base class for OMB reporting classes
    '''
    __treasuryaccountcode = None
    __treasuryaccountname = None
    __budgetaccountcode = None
    __budgetaccountname = None

    @property
    def treasury_account_code( self ) -> str:
        if self.__treasuryaccountcode is not None:
            return self.__treasuryaccountcode

    @treasury_account_code.setter
    def treasury_account_code( self, value: str ):
        if value is not None:
            self.__treasuryaccountcode = value

    @property
    def treasury_account_name( self ) -> str:
        if self.__treasuryaccountname is not None:
            return self.__treasuryaccountname

    @treasury_account_name.setter
    def treasury_account_name( self, value: str ):
        if value is not None:
            self.__treasuryaccountname = value

    @property
    def budget_account_code( self ) -> str:
        if self.__budgetaccountcode is not None:
            return self.__budgetaccountcode

    @budget_account_code.setter
    def budget_account_code( self, value: str ):
        if value is not None:
            self.__budgetaccountcode = value

    @property
    def budget_account_name( self ) -> str:
        if self.__budgetaccountname is not None:
            return self.__budgetaccountname

    @budget_account_name.setter
    def budget_account_name( self, value: str ):
        if value is not None:
            self.__budgetaccountname = value

    def __init__( self, id: int, code: str, name: str, treas: str, omb: str ):
        super( ).__init__( id, code, name )
        self.__treasuryaccountcode = treas
        self.__budgetaccountcode = omb

class Account( ):
    '''
    Constructor:  Account( treas: str, pvdr: Provider = Provider.SQLite )

    Purpose:  Class defines object representing Account Codes'''
    __source = None
    __provider = None
    __accountsid = None
    __code = None
    __name = None
    __goalcode = None
    __objectivecode = None
    __npmcode = None
    __programprojectcode = None
    __programprojectname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ) -> int:
        if self.__accountsid is not None:
            return self.__accountsid

    @id.setter
    def id( self, value: int ):
        if value is not None:
            self.__accountsid = value

    @property
    def code( self ) -> str:
        if  self.__code is not None:
            return self.__code

    @code.setter
    def code( self, value: str ):
        if value is not None:
            self.__code = value

    @property
    def name( self ) -> str:
        if self.__programprojectname is not None:
            return self.__programprojectname

    @name.setter
    def name( self, value: str ):
        if value is not None:
            self.__name = value

    @property
    def goal_code( self ) -> str:
        if self.__goalcode is not None:
            return self.__goalcode

    @goal_code.setter
    def goal_code( self, value: str ):
        if value is not None:
            self.__goalcode = value

    @property
    def objective_code( self ) -> str:
        if self.__objectivecode is not None:
            return self.__objectivecode

    @objective_code.setter
    def objective_code( self, value: str ):
        if value is not None:
            self.__objectivecode = value

    @property
    def npm_code( self ) -> str:
        if  self.__npmcode is not None:
            return self.__npmcode

    @npm_code.setter
    def npm_code( self, value: str ):
        if value is not None:
            self.__npmcode = value

    @property
    def program_project_code( self ) -> str:
        if self.__programprojectcode is not None:
            return self.__programprojectcode

    @program_project_code.setter
    def program_project_code( self, value: str ):
        if value is not None:
            self.__programprojectcode = value

    @property
    def program_project_name( self ) -> str:
        if self.__programprojectcode is not None:
            return self.__programprojectcode

    @program_project_name.setter
    def program_project_name( self, value: str ):
        if value is not None:
            self.__programprojectname = value

    @property
    def data( self ) -> list[ Row ]:
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, value: list[ Row ] ):
        if value is not None:
            self.__data = value

    @property
    def table( self ) -> DataFrame:
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, value: DataFrame ):
        if value is not None:
            self.__frame = value

    @property
    def fields( self ) -> list[ str ]:
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value: list[ str ] ):
        if value is not None:
            self.__fields = value

    def __init__( self, code: str, provider = Provider.SQLite ):
        self.__code = code
        self.__provider = provider
        self.__source = Source.Accounts
        self.__goalcode = self.__code[ 0 ]
        self.__objectivecode = self.__code[ 1:3 ]
        self.__npmcode = self.__code[ 3 ]
        self.__programprojectcode = self.__code[ 4:6 ]
        self.__fields = [ 'AccountsId',
                           'Code',
                           'GoalCode',
                           'ObjectiveCode',
                           'NpmCode',
                           'NpmName',
                           'ProgramProjectCode',
                           'ProgramProjectName',
                           'ProgramAreaCode',
                           'ProgramAreaName',
                           'ActivityCode',
                           'ActivityName',
                           'AgencyActivity' ]

    def __str__( self ) -> str:
        if self.__code is not None:
            return self.__code

    def copy( self ):
        try:
            _clone = Account( code = self.__code )
            _clone.goal_code = self.__goalcode
            _clone.objective_code = self.__objectivecode
            _clone.npm_code = self.__npmcode
            _clone.program_project_code = self.__programprojectcode
            return _clone
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Execution'
            _exc.cause = 'Account'
            _exc.method = 'copy( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def get_data( self ) -> list[ Row ]:
        try:
            _source = Source.Accounts
            _provider = Provider.SQLite
            _names = [ 'Code', ]
            _values = (self.__code,)
            _sqlconfig = SqlConfig( names = _names, values = _values )
            _connection = Connection( _source, _provider )
            _sql = SqlStatement( _connection, _sqlconfig )
            _sqlite = _connection.connect( )
            _cursor = _sqlite.cursor( )
            _query = _sql.get_query( )
            _db = _cursor.execute( _query )
            self.__data =  [ i for i in _db.fetchall( ) ]
            _cursor.close( )
            _sqlite.close( )
            return self.__data
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Execution'
            _exc.cause = 'Account'
            _exc.method = 'get_data( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def get_frame( self ) -> DataFrame:
        '''Method returning a pandas dataframe
        comprised of datatable _data'''
        try:
            _src = self.__source
            _data = BudgetData( _src )
            return _data.create_frame( )
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Execution'
            _exc.cause = 'Account'
            _exc.method = 'create_frame( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class ActivityCode( ):
    '''
    Constructor: ActivityCode( treas: str, pvdr: Provider = Provider.SQLite )

    Purpose: Data class representing Activity Codes
    '''
    __source = None
    __provider = None
    __activitycodesid = None
    __code = None
    __name = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ) -> int:
        if self.__activitycodesid is not None:
            return self.__activitycodesid

    @id.setter
    def id( self, value: int ):
        if value is not None:
            self.__activitycodesid = value

    @property
    def code( self ) -> str:
        if  self.__code is not None:
            return self.__code

    @code.setter
    def code( self, value: str ):
        if value is not None:
            self.__code = value

    @property
    def name( self ) -> str:
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, value: str ):
        if value is not None:
            self.__name = value

    @property
    def data( self ) -> list:
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, value: list ):
        if value is not None:
            self.__data = value

    @property
    def table( self ) -> DataFrame:
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, value: DataFrame ):
        if value is not None:
            self.__frame = value

    @property
    def fields( self ) -> list[ str ]:
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value: list[ str ] ):
        if value is not None:
            self.__fields = value

    def __init__( self, code: str, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.ActivityCodes
        self.__code = code
        self.__fields = [ 'ActivityCodesId',
                           'Code',
                           'Name',
                           'Title' ]

    def __str__( self ) -> str:
        if self.__code is not None:
            return self.__code

    def get_data( self ) -> list[ Row ]:
        try:
            _source = self.__source
            _provider = self.__provider
            _names = [ 'Code', ]
            _values = (self.__code,)
            _dbconfig = DbConfig( _source, _provider )
            _sqlconfig = SqlConfig( names = _names, values = _values )
            _connection = Connection( self.__source )
            _sql = SqlStatement( _dbconfig, _sqlconfig )
            _sqlite = _connection.connect( )
            _cursor = _sqlite.cursor( )
            _query = _sql.get_query( )
            _db = _cursor.execute( _query )
            self.__data =  [ i for i in _db.fetchall( ) ]
            _cursor.close( )
            _sqlite.close( )
            return self.__data
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Execution'
            _exc.cause = 'Activity'
            _exc.method = 'get_data( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def get_frame( self ) -> DataFrame:
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            _source = self.__source
            _data = BudgetData( _source )
            return _data.create_frame( )
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Execution'
            _exc.cause = 'Activity'
            _exc.method = 'create_frame( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class AllowanceHolder( ):
    '''
    Constructor: AllowanceHolder( code: str, pvdr: Provider = Provider.SQLite )

    Purpose: Data class representing Allowance Holders'''
    __source = None
    __provider = None
    __allowancholdersid = None
    __code = None
    __name = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ) -> int:
        if self.__allowancholdersid is not None:
            return self.__allowancholdersid

    @id.setter
    def id( self, id: int ):
        if id is not None:
            self.__allowancholdersid = id

    @property
    def code( self ) -> str:
        if  self.__code is not None:
            return self.__code

    @code.setter
    def code( self, code: str ):
        if code is not None:
            self.__code = code

    @property
    def name( self ) -> str:
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, name: str ):
        if  name is not None:
            self.__name = name

    @property
    def data( self ) -> list[ Row ]:
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, cache: list[ Row ] ):
        if list is not None:
            self.__data = cache

    @property
    def table( self ) -> DataFrame:
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, frame: DataFrame ):
        if frame is not None:
            self.__frame = frame

    @property
    def fields( self ) -> list[ str ]:
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value: list[ str ] ):
        if value is not None:
            self.__fields = value

    def __init__( self, code: str, provider: Provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.AllowanceHolders
        self.__code = code if isinstance( self.__code, str ) else None
        self.__fields = [ 'AllowanceHoldersId',
                           'Code',
                           'Name' ]

    def __str__( self ) -> str:
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code

    def get_data( self ) -> list[ Row ]:
        try:
            _source = self.__source
            _provider = self.__provider
            _names = [ 'Code', ]
            _values = ( self.__code, )
            _dbconfig = DbConfig( _source, _provider )
            _sqlconfig = SqlConfig( names = _names, values = _values )
            _connection = Connection( self.__source )
            _sql = SqlStatement( _dbconfig, _sqlconfig )
            _sqlite = _connection.connect( )
            _cursor = _sqlite.cursor( )
            _query = _sql.get_query( )
            _db = _cursor.execute( _query )
            self.__data =  [ i for i in _db.fetchall( ) ]
            _cursor.close( )
            _sqlite.close( )
            return self.__data
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Execution'
            _exc.cause = 'AllowanceHolder'
            _exc.method = 'get_data( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def get_frame( self ) -> DataFrame:
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            _source = self.__source
            _data = BudgetData( _source )
            return _data.create_frame( )
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Execution'
            _exc.cause = 'AllowanceHolder'
            _exc.method = 'create_frame( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class AmericanRescuePlanCarryoverEstimate( ):
    '''
    Constructor: CarryoverEstimate( bfy: str, pvdr = Provider.SQLite )

    Purpose: Class representing estimates for ARP carryover
    '''
    __source = None
    __provider = None
    __arpcarryoverestimatesid = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __rpioname = None
    __fundcode = None
    __fundname = None
    __amount = None
    __opencommitments = None
    __obligations = None
    __estimate = None
    __treasuryaccountcode = None
    __treasuryaccountname = None
    __budgetaccountcode = None
    __budgetaccountname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ) -> int:
        if self.__arpcarryoverestimatesid is not None:
            return self.__arpcarryoverestimatesid

    @id.setter
    def id( self, value: int ):
        if value is not None:
            self.__annualcarryoverestimatesid = value

    @property
    def bfy( self ) -> str:
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value: str ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ) -> str:
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value: str ):
        if value is not None:
            self.__efy = value

    @property
    def rpio_code( self ) -> str:
        if self.__rpiocode is not None:
            return self.__rpiocode

    @rpio_code.setter
    def rpio_code( self, value: str ):
        if value is not None:
            self.__rpiocode = value

    @property
    def rpio_name( self ) -> str:
        if self.__rpioname is not None:
            return self.__rpioname

    @rpio_code.setter
    def rpio_code( self, value: str ):
        if value is not None:
            self.__rpiocode = value

    @property
    def fund_code( self ) -> str:
        if self.__fundcode is not None:
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value: str ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund_name( self ) -> str:
        if self.__fundname is not None:
            return self.__fundname

    @fund_name.setter
    def fund_name( self, value: str ):
        if value is not None:
            self.__fundname = value

    @property
    def amount( self ) -> float:
        if self.__amount is not None:
            return self.__amount

    @amount.setter
    def amount( self, value: float ):
        if value is not None:
            self.__amount = value

    @property
    def available( self ) -> float:
        if self.__availablebalance is not None:
            return self.__availablebalance

    @available.setter
    def available( self, value: float ):
        if value is not None:
            self.__availablebalance = value

    @property
    def open_commitments( self ) -> float:
        if self.__opencommitments is not None:
            return self.__opencommitments

    @open_commitments.setter
    def open_commitments( self, value: float ):
        if value is not None:
            self.__opencommitments = value

    @property
    def obligations( self ) -> float:
        if self.__obligations is not None:
            return self.__obligations

    @obligations.setter
    def obligations( self, value: float ):
        if value is not None:
            self.__obligations = value

    @property
    def treasury_account_code( self ) -> float:
        if self.__treasuryaccountcode is not None:
            return self.__treasuryaccountcode

    @treasury_account_code.setter
    def treasury_account_code( self, value: float ):
        if value is not None:
            self.__treasuryaccountcode = value

    @property
    def treasury_account_name( self ) -> str:
        if self.__treasuryaccountname is not None:
            return self.__treasuryaccountname

    @treasury_account_name.setter
    def treasury_account_name( self, value: str ):
        if value is not None:
            self.__treasuryaccountname = value

    @property
    def budget_account_code( self ) -> str:
        if self.__budgetaccountcode is not None:
            return self.__budgetaccountcode

    @budget_account_code.setter
    def budget_account_code( self, value: str ):
        if value is not None:
            self.__budgetaccountcode = value

    @property
    def budget_account_name( self ) -> str:
        if self.__budgetaccountname is not None:
            return self.__budgetaccountname

    @budget_account_name.setter
    def budget_account_name( self, value: str ):
        if value is not None:
            self.__budgetaccountname = value

    @property
    def data( self ) -> list[ Row ]:
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, value: list[ Row ] ):
        if value is not None:
            self.__data = value

    @property
    def table( self ) -> DataFrame:
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, value: DataFrame ):
        if value is not None:
            self.__frame = value

    @property
    def fields( self ) -> list[ str ]:
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value: list[ str ] ):
        if value is not None:
            self.__fields = value


    def __init__( self, bfy: str, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.AmericanRescuePlanCarryoverEstimates
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__fields = [ 'CarryoverEstimatesId',
                           'BudgetLevel',
                           'BFY',
                           'EFY',
                           'RpioCode',
                           'RpioName',
                           'AhCode',
                           'AhName',
                           'FundCode',
                           'FundName',
                           'OrgCode',
                           'AccountCode',
                           'ProgramProjectCode',
                           'ProgramProjectName',
                           'ProgramAreaCode',
                           'ProgramAreaName',
                           'BocCode',
                           'BocName',
                           'AvailableBalance',
                           'OpenCommitment',
                           'UnobligatedAuthority' ]

    def __str__( self ) -> str:
        if self.__fundcode is not None:
            return self.__fundcode

    def get_data( self  ) -> list[ Row ]:
        try:
            _source = self.__source
            _provider = self.__provider
            _names = [ 'BFY', 'EFY' ]
            _values = (self.__bfy, self.__efy)
            _dbconfig = DbConfig( _source, _provider )
            _sqlconfig = SqlConfig( names = _names, values = _values )
            _connection = Connection( self.__source )
            _sql = SqlStatement( _dbconfig, _sqlconfig )
            _sqlite = _connection.connect( )
            _cursor = _sqlite.cursor( )
            _query = _sql.get_query( )
            _db = _cursor.execute( _query )
            self.__data =  [ i for i in _db.fetchall( ) ]
            _cursor.close( )
            _sqlite.close( )
            return self.__data
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Reporting'
            _exc.cause = 'CarryoverEstimate'
            _exc.method = 'get_data( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def get_frame( self ) -> DataFrame:
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            _data = BudgetData( self.__source )
            return _data.create_frame( )
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Reporting'
            _exc.cause = 'CarryoverEstimate'
            _exc.method = 'create_frame( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class AnnualCarryoverEstimate( ):
    '''
    Constructor: AnnualCarryoverEstimate( bfy: str, pvdr: Provider = Provider.SQLite )

    Purpose: Class providing Carryover Estimate data for'''
    __source = None
    __provider = None
    __annualcarryoverestimatesid = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __rpioname = None
    __fundcode = None
    __fundname = None
    __amount = None
    __opencommitments = None
    __obligations = None
    __estimate = None
    __treasuryaccountcode = None
    __treasuryaccountname = None
    __budgetaccountcode = None
    __budgetaccountname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ) -> int:
        if self.__annualcarryoverestimatesid is not None:
            return self.__annualcarryoverestimatesid

    @id.setter
    def id( self, value: int ):
        if value is not None:
            self.__annualcarryoverestimatesid = value

    @property
    def bfy( self ) -> str:
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value: str ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ) -> str:
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value: str ):
        if value is not None:
            self.__efy = value

    @property
    def rpio_code( self ) -> str:
        if self.__rpiocode is not None:
            return self.__rpiocode

    @rpio_code.setter
    def rpio_code( self, value: str ):
        if value is not None:
            self.__rpiocode = value

    @property
    def rpio_name( self ) -> str:
        if self.__rpioname is not None:
            return self.__rpioname

    @rpio_code.setter
    def rpio_code( self, value: str ):
        if value is not None:
            self.__rpiocode = value

    @property
    def fund_code( self ) -> str:
        if self.__fundcode is not None:
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value: str ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund_name( self ) -> str:
        if self.__fundname is not None:
            return self.__fundname

    @fund_name.setter
    def fund_name( self, value: str ):
        if value is not None:
            self.__fundname = value

    @property
    def amount( self ) -> float:
        if self.__amount is not None:
            return self.__amount

    @amount.setter
    def amount( self, value: float ):
        if value is not None:
            self.__amount = value

    @property
    def available( self ) -> float:
        if self.__availablebalance is not None:
            return self.__availablebalance

    @available.setter
    def available( self, value: float ):
        if value is not None:
            self.__availablebalance = value

    @property
    def open_commitments( self ) -> float:
        if self.__opencommitments is not None:
            return self.__opencommitments

    @open_commitments.setter
    def open_commitments( self, value: float ):
        if value is not None:
            self.__opencommitments = value

    @property
    def obligations( self ) -> float:
        if self.__obligations is not None:
            return self.__obligations

    @obligations.setter
    def obligations( self, value: float ):
        if value is not None:
            self.__obligations = value

    @property
    def treasury_account_code( self ) -> str:
        if self.__treasuryaccountcode is not None:
            return self.__treasuryaccountcode

    @treasury_account_code.setter
    def treasury_account_code( self, value: str ):
        if value is not None:
            self.__treasuryaccountcode = value

    @property
    def treasury_account_name( self ) -> str:
        if self.__treasuryaccountname is not None:
            return self.__treasuryaccountname

    @treasury_account_name.setter
    def treasury_account_name( self, value: str ):
        if value is not None:
            self.__treasuryaccountname = value

    @property
    def budget_account_code( self ) -> str:
        if self.__budgetaccountcode is not None:
            return self.__budgetaccountcode

    @budget_account_code.setter
    def budget_account_code( self, value: str ):
        if value is not None:
            self.__budgetaccountcode = value

    @property
    def budget_account_name( self ) -> str:
        if self.__budgetaccountname is not None:
            return self.__budgetaccountname

    @budget_account_name.setter
    def budget_account_name( self, value: str ):
        if value is not None:
            self.__budgetaccountname = value

    @property
    def data( self ) -> list:
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, value: list ):
        if isinstance( value, list ):
            self.__data = value

    @property
    def table( self ) -> DataFrame:
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, value: DataFrame):
        if value is not None:
            self.__frame = value

    @property
    def fields( self ) -> list[ str ]:
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value: list[ str ] ):
        if value is not None:
            self.__fields = value


    def __init__( self, bfy: str, provider: Provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.AnnualCarryoverEstimates
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__frame = DataFrame( )
        self.__fields = [ 'CarryoverEstimatesId',
                           'BudgetLevel',
                           'BFY',
                           'EFY',
                           'RpioCode',
                           'RpioName',
                           'AhCode',
                           'AhName',
                           'FundCode',
                           'FundName',
                           'OrgCode',
                           'AccountCode',
                           'ProgramProjectCode',
                           'ProgramProjectName',
                           'ProgramAreaCode',
                           'ProgramAreaName',
                           'BocCode',
                           'BocName',
                           'AvailableBalance',
                           'OpenCommitment',
                           'UnobligatedAuthority' ]

    def __str__( self ) -> str:
        if self.__fundcode is not None:
            return str( self.__fundcode )

    def get_data( self  ) -> list[ Row ]:
        try:
            _source = self.__source
            _provider = self.__provider
            _names = [ 'BFY', 'EFY' ]
            _values = (self.__bfy, self.__efy)
            _dbconfig = DbConfig( _source, _provider )
            _sqlconfig = SqlConfig( names = _names, values = _values )
            _connection = Connection( self.__source )
            _sql = SqlStatement( _dbconfig, _sqlconfig )
            _sqlite = _connection.connect( )
            _cursor = _sqlite.cursor( )
            _query = _sql.get_query( )
            _db = _cursor.execute( _query )
            self.__data =  [ i for i in _db.fetchall( ) ]
            _cursor.close( )
            _sqlite.close( )
            return self.__data
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Reporting'
            _exc.cause = 'CarryoverEstimate'
            _exc.method = 'get_data( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def get_frame( self ) -> DataFrame:
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            _source = self.__source
            _data = BudgetData( _source )
            return _data.create_frame( )
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Reporting'
            _exc.cause = 'CarryoverEstimate'
            _exc.method = 'create_frame( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class AnnualReimbursableEstimate( ):
    '''
    Constructor: AnnualReimbursableEstimate( bfy: str, pvdr: Provider = Provider.SQLite )

    Purpose:  Class defining object representing reimbursable estimates'''
    __source = None
    __provider = None
    __annualreimbursableestimatesid = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __rpioname = None
    __fundcode = None
    __fundname = None
    __amount = None
    __opencommitments = None
    __obligations = None
    __estimate = None
    __treasuryaccountcode = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ) -> int:
        if self.__annualcarryoverestimatesid is not None:
            return self.__annualcarryoverestimatesid

    @id.setter
    def id( self, value: int ):
        if value is not None:
            self.__annualcarryoverestimatesid = value

    @property
    def bfy( self ) -> str:
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value: str ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ) -> str:
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value: str ):
        if value is not None:
            self.__efy = value

    @property
    def rpio_code( self ) -> str:
        if self.__rpiocode is not None:
            return self.__rpiocode

    @rpio_code.setter
    def rpio_code( self, value: str ):
        if value is not None:
            self.__rpiocode = value

    @property
    def rpio_name( self ) -> str:
        if self.__rpioname is not None:
            return self.__rpioname

    @rpio_code.setter
    def rpio_code( self, value: str ):
        if value is not None:
            self.__rpiocode = value

    @property
    def fund_code( self ) -> str:
        if self.__fundcode is not None:
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value: str ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund_name( self ) -> str:
        if self.__fundname is not None:
            return self.__fundname

    @fund_name.setter
    def fund_name( self, value: str ):
        if value is not None:
            self.__fundname = value

    @property
    def available( self ) -> float:
        if self.__availablebalance is not None:
            return self.__availablebalance

    @available.setter
    def available( self, value: float ):
        if value is not None:
            self.__availablebalance = value

    @property
    def open_commitments( self ) -> float:
        if isinstance( self.__opencommitments, float ):
            return self.__opencommitments

    @open_commitments.setter
    def open_commitments( self, value: float ):
        if value is not None:
            self.__opencommitments = value

    @property
    def data( self ) -> list[ Row ]:
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, value: list[ Row ] ):
        if isinstance( value, list ):
            self.__data = value

    @property
    def table( self ) -> DataFrame:
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, value: DataFrame ):
        if value is not None:
            self.__frame = value

    @property
    def fields( self ) -> list[ str ]:
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value: list[ str ] ):
        if value is not None:
            self.__fields = value


    def __init__( self, bfy: str, provider: Provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.AnnualReimbursableEstimates
        self.__bfy = bfy
        self.__fields = [ 'AnnualReimbursableEstimatesId',
                           'BudgetLevel',
                           'BFY',
                           'EFY',
                           'RpioCode',
                           'RpioName',
                           'AhCode',
                           'AhName',
                           'FundCode',
                           'FundName',
                           'OrgCode',
                           'AccountCode',
                           'ProgramProjectCode',
                           'ProgramProjectName',
                           'ProgramAreaCode',
                           'ProgramAreaName',
                           'BocCode',
                           'BocName',
                           'AvailableBalance',
                           'OpenCommitment',
                           'UnobligatedAuthority' ]

    def __str__( self ) -> str:
        if self.__fundcode is not None:
            return self.__fundcode

    def get_data( self  ) -> list[ Row ]:
        try:
            _source = self.__source
            _provider = self.__provider
            _names = [ 'BFY', 'EFY' ]
            _values = (self.__bfy, self.__efy)
            _dbconfig = DbConfig( _source, _provider )
            _sqlconfig = SqlConfig( names = _names, values = _values )
            _connection = Connection( self.__source )
            _sql = SqlStatement( _dbconfig, _sqlconfig )
            _sqlite = _connection.connect( )
            _cursor = _sqlite.cursor( )
            _query = _sql.get_query( )
            _db = _cursor.execute( _query )
            self.__data =  [ i for i in _db.fetchall( ) ]
            _cursor.close( )
            _sqlite.close( )
            return self.__data
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Reporting'
            _exc.cause = 'CarryoverEstimate'
            _exc.method = 'get_data( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def get_frame( self ) -> DataFrame:
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            _source = self.__source
            _data = BudgetData( _source )
            return _data.create_frame( )
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Reporting'
            _exc.cause = 'CarryoverEstimate'
            _exc.method = 'create_frame( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class Appropriation( ):
    '''
    Constructor: Appropriation( fund: str, pvdr: Provider = Provider.SQLite )

    Purpose: Data class representing Appropriations'''
    __source = None
    __provider = None
    __appropriationsid = None
    __code = None
    __name = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ) -> int:
        if self.__appropriationsid is not None:
            return self.__appropriationsid

    @id.setter
    def id( self, value: int ):
        if value is not None:
            self.__appropriationsid  = value

    @property
    def code( self ) -> str:
        if  self.__code is not None:
            return self.__code

    @code.setter
    def code( self, value: str ):
        if value is not None:
            self.__code = value

    @property
    def name( self ) -> str:
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, name: str  ):
        if  name is not None:
            self.__name = name

    @property
    def data( self ) -> list[ Row ]:
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, value: list[ Row ] ):
        if isinstance( value, list ):
            self.__data = value

    @property
    def fields( self ) -> list[ str ]:
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value: list[ str ] ):
        if value is not None:
            self.__fields = value

    def __init__( self, code: str ):
        self.__source = Source.Appropriations
        self.__provider = Provider.SQLite
        self.__code = code
        self.__fields = [ 'AppropriationsId',
                           'Code',
                           'Name' ]

    def __str__( self ) -> str:
        if self.__code is not None:
            return self.__code

    def get_data( self ) -> list[ Row ]:
        try:
            _source = self.__source
            _provider = self.__provider
            _names = [ 'Code' ]
            _values = ( self.__code, )
            _dbconfig = DbConfig( _source, _provider )
            _sqlconfig = SqlConfig( names = _names, values = _values )
            _connection = Connection( self.__source )
            _sql = SqlStatement( _dbconfig, _sqlconfig )
            _sqlite = _connection.connect( )
            _cursor = _sqlite.cursor( )
            _query = _sql.get_query( )
            _db = _cursor.execute( _query )
            self.__data =  [ i for i in _db.fetchall( ) ]
            _cursor.close( )
            _sqlite.close( )
            return self.__data
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Execution'
            _exc.cause = 'Appropriation'
            _exc.method = 'get_data( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def get_frame( self ) -> DataFrame:
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            _source = self.__source
            _data = BudgetData( _source )
            return _data.create_frame( )
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Execution'
            _exc.cause = 'Appropriation'
            _exc.method = 'create_frame( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class AppropriationAvailableBalance( ):
    '''
    Constructor: AppropriationAvailableBalance( bfy: str, efy: str, fund: str )

    Purpose: Data class representing Appropriation-level balances'''
    __source = None
    __provider = None
    __appropriationavailablebalancesid = None
    __bfy = None
    __efy = None
    __fundcode = None
    __fundname = None
    __budgetaccountcode = None
    __budgetaccountname = None
    __treasuryaccountcode = None
    __treasuryaccountname = None
    __authority = None
    __budgeted = None
    __carryover = None
    __reimbursements = None
    __recoveries = None
    __used = None
    __available = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ) -> int:
        if self.__appropriationavailablebalancesid is not None:
            return self.__appropriationavailablebalancesid

    @id.setter
    def id( self, value: int ):
        if value is not None:
            self.__appropriationavailablebalancesid  = value

    @property
    def bfy( self ) -> str:
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value: str ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ) -> str:
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value: str ):
        if value is not None:
            self.__efy = value

    @property
    def fund_code( self ) -> str:
        if  self.__fundcode is not None:
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value: str ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund_name( self ) -> str:
        if self.__fundname is not None:
            return self.__fundname

    @fund_name.setter
    def fund_name( self, name: str ):
        if  name is not None:
            self.__fundname = name

    @property
    def treasury_account_code( self ) -> str:
        if isinstance( self.__treasuryaccountcode, str ) \
                and self.__treasuryaccountcode != '':
            return self.__treasuryaccountcode

    @treasury_account_code.setter
    def treasury_account_code( self, value: str ):
        if value is not None:
            self.__treasuryaccountcode = value

    @property
    def treasury_account_name( self ) -> str:
        if isinstance( self.__treasuryaccountname, str ) \
                and self.__treasuryaccountname != '':
            return self.__treasuryaccountname

    @treasury_account_name.setter
    def treasury_account_name( self, value: str ):
        if value is not None:
            self.__treasuryaccountname = value

    @property
    def budget_account_code( self ) -> str:
        if self.__budgetaccountcode is not None:
            return self.__budgetaccountcode

    @budget_account_code.setter
    def budget_account_code( self, value: str ):
        if value is not None:
            self.__budgetaccountcode = value

    @property
    def budget_account_name( self ) -> str:
        if self.__budgetaccountname is not None:
            return self.__budgetaccountname

    @budget_account_name.setter
    def budget_account_name( self, value: str ):
        if value is not None:
            self.__budgetaccountname = value

    @property
    def authority( self ) -> float:
        if self.__authority is not None:
            return self.__authority

    @authority.setter
    def authority( self, value: float ):
        if value is not None:
            self.__authority = value

    @property
    def budgeted( self ) -> float:
        if self.__budgeted is not None:
            return self.__budgeted

    @budgeted.setter
    def budgeted( self, value: float ):
        if value is not None:
            self.__budgeted = value

    @property
    def reimbursements( self ) -> float:
        if self.__reimbursements is not None:
            return self.__reimbursements

    @reimbursements.setter
    def reimbursements( self, value: float ):
        if value is not None:
            self.__reimbursements = value

    @property
    def recoveries( self ) -> float:
        if self.__recoveries is not None:
            return self.__recoveries

    @recoveries.setter
    def recoveries( self, value: float ):
        if value is not None:
            self.__recoveries = value

    @property
    def used( self ) -> float:
        if self.__used is not None:
            return self.__used

    @used.setter
    def used( self, value: float ):
        if value is not None:
            self.__used = value

    @property
    def available( self ) -> float:
        if self.__available is not None:
            return self.__available

    @available.setter
    def available( self, value: float ):
        if value is not None:
            self.__available = value

    @property
    def data( self ) -> list[ Row ]:
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, value: list[ Row ] ):
        if isinstance( value, list ):
            self.__data = value

    @property
    def fields( self ) -> list[ str ]:
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value: list[ str ] ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy: str, efy: str, fundcode: str ):
        self.__source = Source.Appropriations
        self.__provider = Provider.SQLite
        self.__bfy = bfy
        self.__efy = efy
        self.__fundcode = fundcode
        self.__fields = [ 'AppropriationAvailableBalancesId',
                          'BFY',
                          'EFY',
                          'FundCode',
                          'FundName',
                          'OmbAccountCode',
                          'OmbAccountName',
                          'TreasuryAccountCode',
                          'TreasuryAccountName',
                          'TotalAuthority',
                          'Budgeted',
                          'TotalReimbursements',
                          'TotalRecoveries',
                          'TotalUsed',
                          'TotalAvailable']

    def __str__( self ) -> str:
        if self.__fundcode is not None:
            return self.__fundcode

    def get_data( self ) -> list[ Row ]:
        try:
            _source = self.__source
            _provider = self.__provider
            _names = [ 'Code' ]
            _values = ( self.__fundcode, )
            _dbconfig = DbConfig( _source, _provider )
            _sqlconfig = SqlConfig( names = _names, values = _values )
            _connection = Connection( self.__source )
            _sql = SqlStatement( _dbconfig, _sqlconfig )
            _sqlite = _connection.connect( )
            _cursor = _sqlite.cursor( )
            _query = _sql.get_query( )
            _db = _cursor.execute( _query )
            self.__data =  [ i for i in _db.fetchall( ) ]
            _cursor.close( )
            _sqlite.close( )
            return self.__data
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Execution'
            _exc.cause = 'Appropriation'
            _exc.method = 'get_data( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def get_frame( self ) -> DataFrame:
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            _source = self.__source
            _data = BudgetData( _source )
            return _data.create_frame( )
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Execution'
            _exc.cause = 'Appropriation'
            _exc.method = 'create_frame( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class AppropriationLevelAuthority( ):
    '''
    Constructor: AppropriationLevelAuthority( bfy: str, efy: str, fund: str )

    Purpose: Data class representing Appropriation-level authority'''
    __source = None
    __provider = None
    __appropriationlevelauthorityid = None
    __bfy = None
    __efy = None
    __fundcode = None
    __fundname = None
    __treasuryaccountcode = None
    __budgeted = None
    __carryover = None
    __reimbursements = None
    __authority = None
    __recoveries = None
    __treasuryaccountname = None
    __budgetaccountcode = None
    __budgetaccountname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ) -> int:
        if self.__appropriationlevelauthorityid is not None:
            return self.__appropriationlevelauthorityid

    @id.setter
    def id( self, value: int ):
        if value is not None:
            self.__appropriationlevelauthorityid  = value

    @property
    def bfy( self ) -> str:
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value: str ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ) -> str:
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value: str ):
        if value is not None:
            self.__efy = value

    @property
    def fund_code( self ) -> str:
        if  self.__fundcode is not None:
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value: str ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund_name( self ) -> str:
        if self.__fundname is not None:
            return self.__fundname

    @fund_name.setter
    def fund_name( self, name ):
        if  name is not None:
            self.__fundname = name

    @property
    def treasury_account_code( self ) -> str:
        if isinstance( self.__treasuryaccountcode, str ) \
                and self.__treasuryaccountcode != '':
            return self.__treasuryaccountcode

    @treasury_account_code.setter
    def treasury_account_code( self, value: str ):
        if value is not None:
            self.__treasuryaccountcode = value

    @property
    def treasury_account_name( self ) -> str:
        if isinstance( self.__treasuryaccountname, str ) \
                and self.__treasuryaccountname != '':
            return self.__treasuryaccountname

    @treasury_account_name.setter
    def treasury_account_name( self, value: str ):
        if value is not None:
            self.__treasuryaccountname = value

    @property
    def budget_account_code( self ) -> str:
        if self.__budgetaccountcode is not None:
            return self.__budgetaccountcode

    @budget_account_code.setter
    def budget_account_code( self, value: str ):
        if value is not None:
            self.__budgetaccountcode = value

    @property
    def budget_account_name( self ) -> str:
        if self.__budgetaccountname is not None:
            return self.__budgetaccountname

    @budget_account_name.setter
    def budget_account_name( self, value: str ):
        if value is not None:
            self.__budgetaccountname = value

    @property
    def authority( self ) -> float:
        if self.__authority is not None:
            return self.__authority

    @authority.setter
    def authority( self, value: float ):
        if value is not None:
            self.__authority = value

    @property
    def budgeted( self ) -> float:
        if self.__budgeted is not None:
            return self.__budgeted

    @budgeted.setter
    def budgeted( self, value: float ):
        if value is not None:
            self.__budgeted = value

    @property
    def reimbursements( self ) -> float:
        if self.__reimbursements is not None:
            return self.__reimbursements

    @reimbursements.setter
    def reimbursements( self, value: float ):
        if value is not None:
            self.__reimbursements = value

    @property
    def recoveries( self ) -> float:
        if self.__recoveries is not None:
            return self.__recoveries

    @recoveries.setter
    def recoveries( self, value: float ):
        if value is not None:
            self.__recoveries = value

    @property
    def data( self ) -> list[ Row ]:
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, value: list[ Row ] ):
        if isinstance( value, list ):
            self.__data = value

    @property
    def fields( self ) -> list[ str ]:
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value: list[ str ] ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy: str, efy: str, fundcode: str ):
        self.__source = Source.Appropriations
        self.__provider = Provider.SQLite
        self.__bfy = bfy
        self.__efy = efy
        self.__fundcode = fundcode
        self.__fields = [ 'AppropriationLevelAuthorityId',
                           'Code',
                           'Name' ]

    def __str__( self ) -> str:
        if isinstance( self.__fundcode, str ) and self.__fundcode != '':
            return self.__fundcode

    def get_data( self  ) -> list[ Row ]:
        try:
            _source = self.__source
            _provider = self.__provider
            _names = [ 'Code' ]
            _values = tuple( self.__fundcode, )
            _dbconfig = DbConfig( _source, _provider )
            _sqlconfig = SqlConfig( names = _names, values = _values )
            _connection = Connection( self.__source )
            _sql = SqlStatement( _dbconfig, _sqlconfig )
            _sqlite = _connection.connect( )
            _cursor = _sqlite.cursor( )
            _query = _sql.get_query( )
            _db = _cursor.execute( _query )
            self.__data =  [ i for i in _db.fetchall( ) ]
            _cursor.close( )
            _sqlite.close( )
            return self.__data
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Execution'
            _exc.cause = 'Appropriation'
            _exc.method = 'get_data( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def get_frame( self ) -> DataFrame:
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            _source = self.__source
            _data = BudgetData( _source )
            return _data.create_frame( )
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Execution'
            _exc.cause = 'Appropriation'
            _exc.method = 'create_frame( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class Allocation( ):
    '''
    Constructor: Allocation( bfy = None, fund = None, pvdr: Provider = Provider.SQLite )

    Purpose: Class defining object representing Allocations'''
    __source = None
    __provider = None
    __allocationsid = None
    __statusoffundsid = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __rpioname = None
    __fundcode = None
    __fundname = None
    __ahcode = None
    __ahname = None
    __orgcode = None
    __orgname = None
    __accountcode = None
    __boccode = None
    __bocname = None
    __rccode = None
    __rcname = None
    __amount = None
    __programprojectcode = None
    __programprojectname = None
    __programareacode = None
    __programareaname = None
    __goalcode = None
    __goalname = None
    __objectivecode = None
    __objectivename = None
    __npmcode = None
    __npmname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ) -> int:
        if self.__statusoffundsid is not None:
            return self.__statusoffundsid

    @id.setter
    def id( self, value: int ):
        if value is not None:
            self.__statusoffundsid = value

    @property
    def bfy( self ) -> str:
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value: str ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ) -> str:
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value: str ):
        if value is not None:
            self.__efy = value

    @property
    def rpio_code( self ) -> str:
        if self.__rpiocode is not None:
            return self.__rpiocode

    @rpio_code.setter
    def rpio_code( self, value: str ):
        if value is not None:
            self.__rpiocode = value

    @property
    def rpio_name( self ) -> str:
        if self.__rpioname is not None:
            return self.__rpioname

    @rpio_code.setter
    def rpio_code( self, value: str ):
        if value is not None:
            self.__rpiocode = value

    @property
    def ah_code( self ) -> str:
        if self.__ahcode is not None:
            return self.__ahcode

    @ah_code.setter
    def ah_code( self, value: str  ):
        if value is not None:
            self.__ahcode = value

    @property
    def ah_name( self ) -> str:
        if self.__ahname is not None:
            return self.__ahname

    @ah_name.setter
    def ah_name( self, value: str  ):
        if value is not None:
            self.__ahname = value

    @property
    def fund_code( self ) -> str:
        if self.__fundcode is not None:
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value: str  ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund_name( self ) -> str:
        if self.__fundname is not None:
            return self.__fundname

    @fund_name.setter
    def fund_name( self, value: str  ):
        if value is not None:
            self.__fundname = value

    @property
    def org_code( self ) -> str:
        if self.__orgcode is not None:
            return self.__orgcode

    @org_code.setter
    def org_code( self, value: str  ):
        if value is not None:
            self.__orgcode = value

    @property
    def org_name( self  ) -> str:
        if self.__orgname is not None:
            return self.__orgname

    @org_name.setter
    def org_name( self, value: str   ):
        if value is not None:
            self.__orgname = value

    @property
    def account_code( self ) -> str:
        if self.__accountcode is not None:
            return self.__accountcode

    @account_code.setter
    def account_code( self, value: str  ):
        if value is not None:
            self.__accountcode = value

    @property
    def boc_code( self ) -> str:
        if self.__boccode is not None:
            return self.__boccode

    @boc_code.setter
    def boc_code( self, value: str  ):
        if value is not None:
            self.__boccode = value

    @property
    def boc_name( self ) -> str:
        if self.__bocname is not None:
            return self.__bocname

    @boc_name.setter
    def boc_name( self, value: str  ):
        if value is not None:
            self.__bocname = value

    @property
    def rc_code( self ) -> str:
        if self.__rccode is not None:
            return self.__rccode

    @rc_code.setter
    def rc_code( self, value: str  ):
        if value is not None:
            self.__rccode = value

    @property
    def rc_name( self ) -> str:
        if self.__rcname is not None:
            return self.__rcname

    @rc_name.setter
    def rc_name( self, value: str  ):
        if value is not None:
            self.__rcname = value

    @property
    def amount( self ) -> float:
        if self.__amount is not None:
            return self.__amount

    @amount.setter
    def amount( self, value: float ):
        if value is not None:
            self.__amount = value

    @property
    def program_project_code( self ) -> str:
        if self.__programprojectcode is not None:
            return self.__programprojectcode

    @program_project_code.setter
    def program_project_code( self, value: str ):
        if value is not None:
            self.__programprojectcode = value

    @property
    def program_project_name( self ) -> str:
        if self.__programprojectname is not None:
            return self.__programprojectname

    @program_project_name.setter
    def program_project_name( self, value: str ):
        if value is not None:
            self.__programprojectname = value

    @property
    def program_area_code( self ) -> str:
        if self.__programareacode is not None:
            return self.__programareacode

    @program_area_code.setter
    def program_area_code( self, value: str ):
        if value is not None:
            self.__programareacode = value

    @property
    def program_area_name( self ) -> str:
        if self.__programareaname is not None:
            return self.__programareaname

    @program_area_name.setter
    def program_area_name( self, value: str ):
        if value is not None:
            self.__programareaname = value

    @property
    def goal_code( self ) -> str:
        if self.__goalcode is not None:
            return self.__goalcode

    @goal_code.setter
    def goal_code( self, value: str ):
        if value is not None:
            self.__goalcode = value

    @property
    def goal_name( self ) -> str:
        if self.__goalname is not None:
            return self.__goalname

    @goal_name.setter
    def goal_name( self, value: str ):
        if value is not None:
            self.__goalname = value

    @property
    def objective_code( self ) -> str:
        if self.__objectivecode is not None:
            return self.__objectivecode

    @objective_code.setter
    def objective_code( self, value: str ):
        if value is not None:
            self.__objectivecode = value

    @property
    def objective_name( self ) -> str:
        if self.__objectivename is not None:
            return self.__objectivename

    @objective_name.setter
    def objective_name( self, value: str ):
        if value is not None:
            self.__objectivename = value

    @property
    def npm_code( self ) -> str:
        if  self.__npmcode is not None:
            return self.__npmcode

    @npm_code.setter
    def npm_code( self, value: str ):
        if value is not None:
            self.__npmcode = value

    @property
    def npm_name( self ) -> str:
        if self.__npmname is not None:
            return self.__npmname

    @npm_name.setter
    def npm_name( self, value: str ):
        if value is not None:
            self.__npmname = value

    @property
    def fields( self ) -> list[ str ]:
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value: list[ str ] ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy = None, fund = None, provider: Provider = Provider.SQLite ):
        self.__source = Source.Allocations
        self.__provider = provider
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__fundcode = fund if isinstance( fund, str ) and fund != '' else None
        self.__fields = [ 'AllocationsId',
                           'StatusOfFundsId',
                           'BudgetLevel',
                           'BFY',
                           'EFY',
                           'RpioCode',
                           'RpioName',
                           'AhCode',
                           'AhName',
                           'FundCode',
                           'FundName',
                           'OrgCode',
                           'OrgName',
                           'AccountCode',
                           'BocCode',
                           'BocName',
                           'ProgramProjectCode',
                           'ProgramProjectName',
                           'ProgramAreaCode',
                           'ProgramAreaName',
                           'RcCode',
                           'RcName',
                           'LowerName',
                           'Amount',
                           'NpmCode',
                           'NpmName' ]

    def get_data( self  ) -> list[ Row ]:
        try:
            _source = self.__source
            _provider = self.__provider
            _names = [ 'BFY', 'FundCode' ]
            _values = (self.__bfy, self.__fundcode)
            _dbconfig = DbConfig( _source, _provider )
            _sqlconfig = SqlConfig( names = _names, values = _values )
            _connection = Connection( self.__source )
            _sql = SqlStatement( _dbconfig, _sqlconfig )
            _sqlite = _connection.connect( )
            _cursor = _sqlite.cursor( )
            _query = _sql.get_query( )
            _db = _cursor.execute( _query )
            self.__data =  [ i for i in _db.fetchall( ) ]
            _cursor.close( )
            _sqlite.close( )
            return self.__data
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Ninja'
            _exc.cause = 'Allocation'
            _exc.method = 'get_data( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def get_frame( self ) -> DataFrame:
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            _source = self.__source
            _data = BudgetData( _source )
            return _data.create_frame( )
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Ninja'
            _exc.cause = 'Allocation'
            _exc.method = 'create_frame( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class ApportionmentData( ):
    '''
    Constructor:  ApportionmentData( bfy: str, efy: str, main: str,
                                pvdr: Provider = Provider.SQLite )

    Purpose: Data class representing Letters Of Apportionment'''
    __source = None
    __provider = None
    __apportionmentdataid = None
    __bfy = None
    __efy = None
    __treasuryaccountcode = None
    __treasuryaccountname = None
    __budgetaccountcode = None
    __budgetaccountname = None
    __linenumber = None
    __linedescription = None
    __sectionnumber = None
    __sectiondescription = None
    __subline = None
    __amount = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ) -> int:
        if self.__apportionmentsid is not None:
            return self.__apportionmentsid

    @id.setter
    def id( self, value: int ):
        if value is not None:
            self.__apportionmentsid = value

    @property
    def bfy( self ) -> str:
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value: str ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ) -> str:
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value: str ):
        if value is not None:
            self.__efy = value

    @property
    def treasury_account_code( self ) -> str:
        if self.__treasuryaccountcode is not None:
            return self.__treasuryaccountcode

    @treasury_account_code.setter
    def treasury_account_code( self, value: str ):
        if value is not None:
            self.__treasuryaccountcode = value

    @property
    def treasury_account_name( self ) -> str:
        if self.__treasuryaccountname is not None:
            return self.__treasuryaccountname

    @treasury_account_name.setter
    def treasury_account_name( self, value: str ):
        if value is not None:
            self.__treasuryaccountname = value

    @property
    def budget_account_code( self ) -> str:
        if self.__budgetaccountcode is not None:
            return self.__budgetaccountcode

    @budget_account_code.setter
    def budget_account_code( self, value: str ):
        if value is not None:
            self.__budgetaccountcode = value

    @property
    def budget_account_name( self ) -> str:
        if self.__budgetaccountname is not None:
            return self.__budgetaccountname

    @budget_account_name.setter
    def budget_account_name( self, value: str ):
        if value is not None:
            self.__budgetaccountname = value

    @property
    def line_number( self ) -> str:
        if self.__linenumber is not None:
            return self.__linenumber

    @line_number.setter
    def line_number( self, value: str ):
        if value is not None:
            self.__linenumber = value

    @property
    def line_description( self ) -> str:
        if self.__linedescription is not None:
            return self.__linedescription

    @line_description.setter
    def line_description( self, value: str ):
        if value is not None:
            self.__linedescription = value

    @property
    def section_number( self ) -> str:
        if self.__sectionnumber is not None:
            return self.__sectionnumber

    @section_number.setter
    def section_number( self, value: str ):
        if value is not None:
            self.__sectionnumber = value

    @property
    def section_description( self ) -> str:
        if self.__sectiondescription is not None:
            return self.__sectiondescription

    @section_description.setter
    def section_description( self, value: str ):
        if value is not None:
            self.__sectiondescription = value

    @property
    def subline( self ) -> str:
        if self.__subline is not None:
            return self.__subline

    @subline.setter
    def subline( self, value: str ):
        if value is not None:
            self.__subline = value

    @property
    def amount( self ) -> float:
        if self.__amount is not None:
            return self.__amount

    @amount.setter
    def amount( self, value: float ):
        if value is not None:
            self.__amount = value

    @property
    def fields( self ) -> list[ str ]:
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value: list[ str ] ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy: str, efy: str, main: str,
                  provider: Provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.ApportionmentData
        self.__bfy = bfy
        self.__efy = efy
        self.__budgetaccountcode = main
        self.__fields = [ 'ApportionmentDataId',
                          'FiscalYear',
                          'BFY',
                          'EFY',
                          'Availability',
                          'TreasuryFundCode',
                          'TreasuryFundName',
                          'TreasuryAgencyCode',
                          'TreasuryAccountCode',
                          'TreasuryAccountName',
                          'OmbAgencyCode',
                          'OmbBureauCode',
                          'OmbAccountCode',
                          'OmbAgencyName',
                          'OmbAccountName',
                          'ApprovalDate',
                          'LineNumber',
                          'LineName',
                          'Amount',
                          'Footnote',
                          'Narrative' ]

    def get_data( self  ) -> list[ Row ]:
        try:
            _source = self.__source
            _provider = self.__provider
            _names = [ 'BFY', 'EFY', 'OmbAccountCode', ]
            _values = (self.__bfy, self.__efy, self.__budgetaccountcode)
            _dbconfig = DbConfig( _source, _provider )
            _sqlconfig = SqlConfig( names = _names, values = _values )
            _connection = Connection( self.__source )
            _sql = SqlStatement( _dbconfig, _sqlconfig )
            _sqlite = _connection.connect( )
            _cursor = _sqlite.cursor( )
            _query = _sql.get_query( )
            _db = _cursor.execute( _query )
            self.__data =  [ i for i in _db.fetchall( ) ]
            _cursor.close( )
            _sqlite.close( )
            return self.__data
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Reporting'
            _exc.cause = 'Apportionment'
            _exc.method = 'get_data( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def get_frame( self ) -> DataFrame:
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            _source = self.__source
            _data = BudgetData( _source )
            return _data.create_frame( )
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Reporting'
            _exc.cause = 'Apportionment'
            _exc.method = 'create_frame( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class Actual( ):
    '''
    Constructor: Actual( bfy, fund, pvdr = Provider.SQLite  )

    Purpose:  Object representing expenditure data'''
    __source = None
    __provider = None
    __actualsid = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __rpioname = None
    __appropriationcode = None
    __appropriationname = None
    __subappropriationcode = None
    __subappropriationname = None
    __fundcode = None
    __fundname = None
    __ahcode = None
    __ahname = None
    __orgcode = None
    __orgname = None
    __accountcode = None
    __boccode = None
    __bocname = None
    __balance = None
    __obligations = None
    __ulo = None
    __programprojectcode = None
    __programprojectname = None
    __programareacode = None
    __programareaname = None
    __goalcode = None
    __goalname = None
    __objectivecode = None
    __objectivename = None
    __npmcode = None
    __npmname = None
    __treasuryaccountcode = None
    __treasuryaccountname = None
    __budgetaccountcode = None
    __budgetaccountname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ) -> int:
        if self.__actualsid is not None:
            return self.__actualsid

    @id.setter
    def id( self, value: int ):
        if value is not None:
            self.__id = value

    @property
    def bfy( self ) -> str:
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value: str ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ) -> str:
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value: str ):
        if value is not None:
            self.__efy = value

    @property
    def rpio_code( self ) -> str:
        if self.__rpiocode is not None:
            return self.__rpiocode

    @rpio_code.setter
    def rpio_code( self, value: str ):
        if value is not None:
            self.__rpiocode = value

    @property
    def rpio_name( self ) -> str:
        if self.__rpioname is not None:
            return self.__rpioname

    @rpio_code.setter
    def rpio_code( self, value: str ):
        if value is not None:
            self.__rpiocode = value

    @property
    def ah_code( self ) -> str:
        if self.__ahcode is not None:
            return self.__ahcode

    @ah_code.setter
    def ah_code( self, value: str ):
        if value is not None:
            self.__ahcode = value

    @property
    def ah_name( self ) -> str:
        if self.__ahname is not None:
            return self.__ahname

    @ah_name.setter
    def ah_name( self, value: str ):
        if value is not None:
            self.__ahname = value

    @property
    def fund_code( self ) -> str:
        if self.__fundcode is not None:
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value: str ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund_name( self ) -> str:
        if self.__fundname is not None:
            return self.__fundname

    @fund_name.setter
    def fund_name( self, value: str ):
        if value is not None:
            self.__fundname = value

    @property
    def org_code( self ) -> str:
        if self.__orgcode is not None:
            return self.__orgcode

    @org_code.setter
    def org_code( self, value: str ):
        if value is not None:
            self.__orgcode = value

    @property
    def org_name( self  ):
        if self.__orgname is not None:
            return self.__orgname

    @org_name.setter
    def org_name( self, value  ):
        if value is not None:
            self.__orgname = value

    @property
    def account_code( self ) -> str:
        if self.__accountcode is not None:
            return self.__accountcode

    @account_code.setter
    def account_code( self, value: str ):
        if value is not None:
            self.__accountcode = value

    @property
    def boc_code( self ) -> str:
        if self.__boccode is not None:
            return self.__boccode

    @boc_code.setter
    def boc_code( self, value: str ):
        if value is not None:
            self.__boccode = value

    @property
    def boc_name( self ) -> str:
        if self.__bocname is not None:
            return self.__bocname

    @boc_name.setter
    def boc_name( self, value: str ):
        if value is not None:
            self.__bocname = value

    @property
    def rc_code( self ) -> str:
        if self.__rccode is not None:
            return self.__rccode

    @rc_code.setter
    def rc_code( self, value: str ):
        if value is not None:
            self.__rccode = value

    @property
    def rc_name( self ) -> str:
        if self.__rcname is not None:
            return self.__rcname

    @rc_name.setter
    def rc_name( self, value: str ):
        if value is not None:
            self.__rcname = value

    @property
    def balance( self ) -> str:
        if self.__balance is not None:
            return self.__balance

    @balance.setter
    def balance( self, value: str ):
        if value is not None:
            self.__balance = value

    @property
    def ulo( self ) -> str:
        if self.__ulo is not None:
            return self.__ulo

    @ulo.setter
    def ulo( self, value: str ):
        if value is not None:
            self.__ulo = value

    @property
    def obligations( self ) -> float:
        if self.__obligations is not None:
            return self.__obligations

    @obligations.setter
    def obligations( self, value: float ):
        if value is not None:
            self.__obligations = value

    @property
    def program_project_code( self ) -> str:
        if self.__programprojectcode is not None:
            return self.__programprojectcode

    @program_project_code.setter
    def program_project_code( self, value: str ):
        if value is not None:
            self.__programprojectcode = value

    @property
    def program_project_name( self ) -> str:
        if self.__programprojectname is not None:
            return self.__programprojectname

    @program_project_name.setter
    def program_project_name( self, value: str ):
        if value is not None:
            self.__programprojectname = value

    @property
    def program_area_code( self ) -> str:
        if self.__programareacode is not None:
            return self.__programareacode

    @program_area_code.setter
    def program_area_code( self, value: str ):
        if value is not None:
            self.__programareacode = value

    @property
    def program_area_name( self ) -> str:
        if self.__programareaname is not None:
            return self.__programareaname

    @program_area_name.setter
    def program_area_name( self, value: str ):
        if value is not None:
            self.__programareaname = value

    @property
    def goal_code( self ) -> str:
        if self.__goalcode is not None:
            return self.__goalcode

    @goal_code.setter
    def goal_code( self, value: str ):
        if value is not None:
            self.__goalcode = value

    @property
    def goal_name( self ) -> str:
        if self.__goalname is not None:
            return self.__goalname

    @goal_name.setter
    def goal_name( self, value: str ):
        if value is not None:
            self.__goalname = value

    @property
    def objective_code( self ) -> str:
        if self.__objectivecode is not None:
            return self.__objectivecode

    @objective_code.setter
    def objective_code( self, value: str ):
        if value is not None:
            self.__objectivecode = value

    @property
    def objective_name( self ) -> str:
        if self.__objectivename is not None:
            return self.__objectivename

    @objective_name.setter
    def objective_name( self, value: str ):
        if value is not None:
            self.__objectivename = value

    @property
    def npm_code( self ) -> str:
        if  self.__npmcode is not None:
            return self.__npmcode

    @npm_code.setter
    def npm_code( self, value: str ):
        if value is not None:
            self.__npmcode = value

    @property
    def npm_name( self ) -> str:
        if self.__npmname is not None:
            return self.__npmname

    @npm_name.setter
    def npm_name( self, value: str ):
        if value is not None:
            self.__npmname = value

    @property
    def treasury_account_code( self ) -> str:
        if self.__treasuryaccountcode is not None:
            return self.__treasuryaccountcode

    @treasury_account_code.setter
    def treasury_account_code( self, value: str ):
        if value is not None:
            self.__treasuryaccountcode = value

    @property
    def treasury_account_name( self ) -> str:
        if self.__treasuryaccountname is not None:
            return self.__treasuryaccountname

    @treasury_account_name.setter
    def treasury_account_name( self, value: str ):
        if value is not None:
            self.__treasuryaccountname = value

    @property
    def budget_account_code( self ) -> str:
        if self.__budgetaccountcode is not None:
            return self.__budgetaccountcode

    @budget_account_code.setter
    def budget_account_code( self, value: str ):
        if value is not None:
            self.__budgetaccountcode = value

    @property
    def budget_account_name( self ) -> str:
        if self.__budgetaccountname is not None:
            return self.__budgetaccountname

    @budget_account_name.setter
    def budget_account_name( self, value: str ):
        if value is not None:
            self.__budgetaccountname = value

    @property
    def fields( self ) -> list[ str ]:
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value: list[ str ] ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy = None, fund = None, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.Actuals
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__fundcode = fund if isinstance(fund, str ) and fund != '' else None
        self.__fields = [ 'ActualsId',
                           'BFY',
                           'EFY',
                           'RpioCode',
                           'RpioName',
                           'AhCode',
                           'AhName',
                           'FundCode',
                           'FundName',
                           'AppropriationCode',
                           'AppropriationName',
                           'SubAppropriationCode',
                           'SubAppropriationName',
                           'OrgCode',
                           'OrgName',
                           'AccountCode',
                           'ProgramProjectCode',
                           'ProgramProjectName',
                           'RpioActivityCode',
                           'RpioActivityName',
                           'BocCode',
                           'BocName',
                           'ULO',
                           'Obligation',
                           'Balance',
                           'ProgramAreaCode',
                           'ProgramAreaName',
                           'GoalCode',
                           'GoalName',
                           'ObjectiveCode',
                           'ObjectiveName' ]

    def get_data( self  ) -> list[ Row ]:
        try:
            _source = self.__source
            _provider = self.__provider
            _names = [ 'BFY', 'FundCode' ]
            _values = (self.__bfy, self.__fundcode)
            _dbconfig = DbConfig( _source, _provider )
            _sqlconfig = SqlConfig( names = _names, values = _values )
            _connection = Connection( self.__source )
            _sql = SqlStatement( _dbconfig, _sqlconfig )
            _sqlite = _connection.connect( )
            _cursor = _sqlite.cursor( )
            _query = _sql.get_query( )
            _db = _cursor.execute( _query )
            self.__data =  [ i for i in _db.fetchall( ) ]
            _cursor.close( )
            _sqlite.close( )
            return self.__data
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Ninja'
            _exc.cause = 'Actual'
            _exc.method = 'get_data( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def get_frame( self ) -> DataFrame:
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            _source = self.__source
            _data = BudgetData( _source )
            return _data.create_frame( )
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Ninja'
            _exc.cause = 'Actual'
            _exc.method = 'create_frame( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class ApplicationTable( ):
    '''
    Constructor: ApplicationTable( name, pvdr = Provider.SQLite )

    Purpose:  Class defines object that represents all the tables
    '''
    __source = None
    __provider = None
    __applicationtablesid = None
    __tablename = None
    __model = None
    __title = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ) -> int:
        if self.__applicationtablesid is not None:
            return self.__applicationtablesid

    @id.setter
    def id( self, value: int ):
        if value is not None:
            self.__applicationtablesid = value

    @property
    def table_name( self ) -> str:
        if self.__tablename is not None:
            return self.__tablename

    @table_name.setter
    def table_name( self, value: str ):
        if value is not None:
            self.__tablename = value

    @property
    def model( self ) -> str:
        if self.__model is not None:
            return self.__model

    @model.setter
    def model( self, value: str ):
        if value is not None:
            self.__model = value

    @property
    def title( self ) -> str:
        if self.__title is not None:
            return self.__title

    @title.setter
    def title( self, value: str ):
        if value is not None:
            self.__title = value

    def __init__( self, name, provider = Provider.SQLite ):
        self.__source = Source.ApplicationTables
        self.__provider = provider
        self.__tablename = name

class AppropriationDocument( ):
    '''
    Constructor:  AppropriationDocument( bfy, fund, pvdr = Provider.SQLite )

    Purpose:  Class defines object representing Level 1 documents'''
    __source = None
    __provider = None
    __appropriationdocumentsid = None
    __bfy = None
    __efy = None
    __fundcode = None
    __fund = None
    __documenttype = None
    __documentnumber = None
    __documentdate = None
    __lastdocumentdate = None
    __budgetlevel = None
    __budgetingcontrols = None
    __postingcontrols = None
    __precommitmentcontrols = None
    __commitmentcontrols = None
    __obligationcontrols = None
    __accrualcontrols = None
    __expenditurecontrols = None
    __expensecontrols = None
    __reimbursementcontrols = None
    __reimbursableagreementcontrols = None
    __budgeted = None
    __posted = None
    __carryoverout = None
    __carryoverin = None
    __estimatedreimbursements = None
    __estimatedrecoveries = None
    __treasuryaccountcode = None
    __treasuryaccountname = None
    __budgetaccountcode = None
    __budgetaccountname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ) -> int:
        if self.__appropriationdocumentsid is not None:
            return self.__appropriationdocumentsid

    @id.setter
    def id( self, value: int ):
        if value is not None:
            self.__appropriationdocumentsid = value

    @property
    def bfy( self ) -> str:
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value: str ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ) -> str:
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value: str ):
        if value is not None:
            self.__efy = value

    @property
    def fund_code( self ) -> str:
        if self.__fundcode is not None:
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value: str ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund( self ) -> str:
        if self.__fund is not None:
            return self.__fund

    @fund.setter
    def fund( self, value: str ):
        if value is not None:
            self.__fund = value

    @property
    def document_type( self ) -> str:
        if self.__documenttype is not None:
            return self.__documenttype

    @document_type.setter
    def document_type( self, value: str ):
        if value is not None:
            self.__documenttype = value

    @property
    def document_number( self ) -> str:
        if self.__documentname is not None:
            return self.__documentname

    @document_number.setter
    def document_number( self, value: str ):
        if value is not None:
            self.__documentname = value

    @property
    def document_date( self ) -> str:
        if self.__documentdate is not None:
            return self.__documentdate

    @document_date.setter
    def document_date( self, value: str ):
        if value is not None:
            self.__documentdate = value

    @property
    def last_document_date( self ) -> str:
        if self.__lastdocumentdate is not None:
            return self.__lastdocumentdate

    @last_document_date.setter
    def last_document_date( self, value: str ):
        if value is not None:
            self.__lastdocumentdate = value

    @property
    def budget_level( self ) -> str:
        if self.__budgetlevel is not None:
            return self.__budgetlevel

    @budget_level.setter
    def budget_level( self, value: str ):
        if value is not None:
            self.__budgetlevel = value

    @property
    def budgeting_controls( self ) -> str:
        if self.__budgetingcontrols is not None:
            return self.__budgetingcontrols

    @budgeting_controls.setter
    def budgeting_controls( self, value: str ):
        if value is not None:
            self.__budgetingcontrols = value

    @property
    def posting_controls( self ) -> str:
        if self.__postingcontrols is not None:
            return self.__postingcontrols

    @posting_controls.setter
    def posting_controls( self, value: str ):
        if value is not None:
            self.__postingcontrols = value

    @property
    def precommitment_controls( self ) -> str:
        if self.__precommitmentcontrols is not None:
            return self.__precommitmentcontrols

    @precommitment_controls.setter
    def precommitment_controls( self, value: str ):
        if value is not None:
            self.__precommitmentcontrols = value

    @property
    def commitment_controls( self ) -> str:
        if self.__commitmentcontrols is not None:
            return self.__commitmentcontrols

    @commitment_controls.setter
    def commitment_controls( self, value: str ):
        if value is not None:
            self.__commitmentcontrols = value

    @property
    def obligation_controls( self ) -> str:
        if self.__obligationcontrols is not None:
            return self.__obligationcontrols

    @obligation_controls.setter
    def obligation_controls( self, value: str ):
        if value is not None:
            self.__obligationcontrols = value

    @property
    def accrual_controls( self ) -> str:
        if self.__accrualcontrols is not None:
            return self.__accrualcontrols

    @accrual_controls.setter
    def accrual_controls( self, value: str ):
        if value is not None:
            self.__accrualcontrols = value

    @property
    def expenditure_controls( self ) -> str:
        if self.__expenditurecontrols is not None:
            return self.__expenditurecontrols

    @expenditure_controls.setter
    def expenditure_controls( self, value: str ):
        if value is not None:
            self.__expenditurecontrols = value

    @property
    def expense_controls( self ) -> str:
        if self.__expensecontrols is not None:
            return self.__expensecontrols

    @expense_controls.setter
    def expense_controls( self, value: str ):
        if value is not None:
            self.__expensecontrols = value

    @property
    def reimbursement_controls( self ) -> str:
        if self.__reimbursementcontrols is not None:
            return self.__reimbursementcontrols

    @reimbursement_controls.setter
    def reimbursement_controls( self, value: str ):
        if value is not None:
            self.__reimbursementcontrols = value

    @property
    def reimbursable_agreement_controls( self ) -> str:
        if self.__reimbursableagreementcontrols is not None:
            return self.__reimbursableagreementcontrols

    @reimbursable_agreement_controls.setter
    def reimbursable_agreement_controls( self, value: str ):
        if value is not None:
            self.__reimbursableagreementcontrols = value

    @property
    def budgeted( self ) -> str:
        if self.__budgeted is not None:
            return self.__budgeted

    @budgeted.setter
    def budgeted( self, value: str ):
        if value is not None:
            self.__budgeted = value

    @property
    def posted( self ) -> float:
        if self.__posted is not None:
            return self.__posted

    @posted.setter
    def posted( self, value: float ):
        if value is not None:
            self.__posted = value

    @property
    def carryover_in( self ) -> str:
        if self.__carryoverin is not None:
            return self.__carryoverin

    @carryover_in.setter
    def carryover_in( self, value: str ):
        if value is not None:
            self.__carryoverin = value

    @property
    def carryover_out( self ) -> str:
        if self.__carryoverout is not None:
            return self.__carryoverout

    @carryover_out.setter
    def carryover_out( self, value: str ):
        if value is not None:
            self.__carryoverout = value

    @property
    def estimated_reimbursements( self ) -> str:
        if self.__reimbursementcontrols is not None:
            return self.__reimbursementcontrols

    @estimated_reimbursements.setter
    def estimated_reimbursements( self, value: str ):
        if value is not None:
            self.__estimatedreimbursements = value

    @property
    def estimated_recoveries( self ) -> str:
        if self.__estimatedrecoveries is not None:
            return self.__estimatedrecoveries

    @estimated_recoveries.setter
    def estimated_recoveries( self, value: str ):
        if value is not None:
            self.__estimatedrecoveries = value

    @property
    def treasury_account_code( self ) -> str:
        if self.__treasuryaccountcode is not None:
            return self.__treasuryaccountcode

    @treasury_account_code.setter
    def treasury_account_code( self, value: str ):
        if value is not None:
            self.__treasuryaccountcode = value

    @property
    def treasury_account_name( self ) -> str:
        if self.__treasuryaccountname is not None:
            return self.__treasuryaccountname

    @treasury_account_name.setter
    def treasury_account_name( self, value: str ):
        if value is not None:
            self.__treasuryaccountname = value

    @property
    def budget_account_code( self ) -> str:
        if self.__budgetaccountcode is not None:
            return self.__budgetaccountcode

    @budget_account_code.setter
    def budget_account_code( self, value: str ):
        if value is not None:
            self.__budgetaccountcode = value

    @property
    def budget_account_name( self ) -> str:
        if self.__budgetaccountname is not None:
            return self.__budgetaccountname

    @budget_account_name.setter
    def budget_account_name( self, value: str ):
        if value is not None:
            self.__budgetaccountname = value

    @property
    def fields( self ) -> list[ str ]:
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value: list[ str ] ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy = None, fund = None, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.AppropriationDocuments
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__fundcode = fund if isinstance( fund, str ) and fund != '' else None
        self.__fields = [ 'AppropriationDocumentsId',
                           'BFY',
                           'EFY',
                           'Fund',
                           'FundCode',
                           'DocumentType',
                           'DocumentNumber',
                           'DocumentDate',
                           'LastDocumentDate',
                           'BudgetLevel',
                           'BudgetingControls',
                           'PostingControls',
                           'PreCommitmentControls',
                           'CommitmentControls',
                           'ObligationControls',
                           'AccrualControls',
                           'ExpenditureControls',
                           'ExpenseControls',
                           'ReimbursementControls',
                           'ReimbursableAgreementControls',
                           'Budgeted',
                           'Posted',
                           'CarryOut',
                           'CarryIn',
                           'EstimatedReimbursements',
                           'EstimatedRecoveries' ]

    def get_data( self  ) -> list[ Row ]:
        try:
            _source = self.__source
            _provider = self.__provider
            _names = [ 'BFY', 'FundCode' ]
            _values = (self.__bfy, self.__fundcode)
            _dbconfig = DbConfig( _source, _provider )
            _sqlconfig = SqlConfig( names = _names, values = _values )
            _connection = Connection( self.__source )
            _sql = SqlStatement( _dbconfig, _sqlconfig )
            _sqlite = _connection.connect( )
            _cursor = _sqlite.cursor( )
            _query = _sql.get_query( )
            _db = _cursor.execute( _query )
            self.__data =  [ i for i in _db.fetchall( ) ]
            _cursor.close( )
            _sqlite.close( )
            return self.__data
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Ninja'
            _exc.cause = 'AppropriationDocument'
            _exc.method = 'get_data( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def get_frame( self ) -> DataFrame:
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            _source = self.__source
            _data = BudgetData( _source )
            return _data.create_frame( )
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Ninja'
            _exc.cause = 'AppropriationDocument'
            _exc.method = 'create_frame( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class BudgetDocument( ):
    '''
    Constructor:  BudgetDocument( bfy, fund, pvdr = Provider.SQLite )

    Purpose: Class defines object representing Level 2-3 documents'''
    __source = None
    __provider = None
    __budgetdocumentsid = None
    __bfy = None
    __efy = None
    __budgetlevel = None
    __fundcode = None
    __fundname = None
    __documenttype = None
    __documentnumber = None
    __documentdate = None
    __lastdocumentdate = None
    __rpiocode = None
    __rpioname = None
    __ahcode = None
    __ahname = None
    __orgcode = None
    __orgname = None
    __accountcode = None
    __programprojectcode = None
    __programprojectname = None
    __programareacode = None
    __programareaname = None
    __boccode = None
    __bocname = None
    __budgetingcontrols = None
    __postingcontrols = None
    __precommitmentcontrols = None
    __commitmentcontrols = None
    __obligationcontrols = None
    __accrualcontrols = None
    __expenditurecontrols = None
    __expensecontrols = None
    __reimbursementcontrols = None
    __reimbursableagreementcontrols = None
    __budgeted = None
    __posted = None
    __carryoverout = None
    __carryoverin = None
    __estimatedreimbursements = None
    __estimatedrecoveries = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ) -> int:
        if isinstance( self.__budgetdocumentsid, int ):
            return self.__budgetdocumentsid

    @id.setter
    def id( self, value: int ):
        if self.__budgetdocumentsid is not None:
            self.__budgetdocumentsid = value

    @property
    def bfy( self ) -> str:
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value: str ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ) -> str:
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value: str ):
        if value is not None:
            self.__efy = value

    @property
    def budget_level( self ) -> str:
        if self.__budgetlevel is not None:
            return self.__budgetlevel

    @budget_level.setter
    def budget_level( self, value: str ):
        if value is not None:
            self.__budgetlevel = value

    @property
    def rpio_code( self ) -> str:
        if self.__rpiocode is not None:
            return self.__rpiocode

    @rpio_code.setter
    def rpio_code( self, value: str ):
        if value is not None:
            self.__rpiocode = value

    @property
    def rpio_name( self ) -> str:
        if self.__rpioname is not None:
            return self.__rpioname

    @rpio_name.setter
    def rpio_name( self, value: str ):
        if value is not None:
            self.__rpioname = value

    @property
    def ah_code( self ) -> str:
        if self.__ahcode is not None:
            return self.__ahcode

    @ah_code.setter
    def ah_code( self, value: str ):
        if value is not None:
            self.__ahcode = value

    @property
    def ah_name( self ) -> str:
        if self.__ahname is not None:
            return self.__ahname

    @ah_name.setter
    def ah_name( self, value: str ):
        if value is not None:
            self.__ahname = value

    @property
    def fund_code( self ) -> str:
        if self.__fundcode is not None:
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value: str ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund_name( self ) -> str:
        if self.__fundname is not None:
            return self.__fundname

    @fund_name.setter
    def fund_name( self, value: str ):
        if value is not None:
            self.__fundname = value

    @property
    def document_type( self ) -> str:
        if self.__documenttype is not None:
            return self.__documenttype

    @document_type.setter
    def document_type( self, value: str ):
        if value is not None:
            self.__documenttype = value

    @property
    def document_number( self ) -> str:
        if self.__documentnumber is not None:
            return self.__documentnumber

    @document_number.setter
    def document_number( self, value: str ):
        if value is not None:
            self.__documentname = value

    @property
    def document_date( self ) -> str:
        if self.__documentdate is not None:
            return self.__documentdate

    @document_date.setter
    def document_date( self, value: str ):
        if value is not None:
            self.__documentdate = value

    @property
    def last_document_date( self ) -> str:
        if self.__lastdocumentdate is not None:
            return self.__lastdocumentdate

    @last_document_date.setter
    def last_document_date( self, value: str ):
        if value is not None:
            self.__lastdocumentdate = value

    @property
    def org_code( self ) -> str:
        if self.__orgcode is not None:
            return self.__orgcode

    @org_code.setter
    def org_code( self, value: str ):
        if value is not None:
            self.__orgcode = value

    @property
    def org_name( self  ):
        if self.__orgname is not None:
            return self.__orgname

    @org_name.setter
    def org_name( self, value  ):
        if value is not None:
            self.__orgname = value

    @property
    def account_code( self ) -> str:
        if self.__accountcode is not None:
            return self.__accountcode

    @account_code.setter
    def account_code( self, value: str ):
        if value is not None:
            self.__accountcode = value

    @property
    def program_project_code( self ) -> str:
        if self.__programprojectcode is not None:
            return self.__programprojectcode

    @program_project_code.setter
    def program_project_code( self, value: str ):
        if value is not None:
            self.__programprojectcode = value

    @property
    def program_project_name( self ) -> str:
        if self.__programprojectcode is not None:
            return self.__programprojectname

    @program_project_name.setter
    def program_project_name( self, value: str ):
        if value is not None:
            self.__programprojectname = value

    @property
    def program_area_code( self ) -> str:
        if self.__programareacode is not None:
            return self.__programareacode

    @program_area_code.setter
    def program_area_code( self, value: str ):
        if value is not None:
            self.__programareacode = value

    @property
    def program_area_name( self ) -> str:
        if self.__programareaname is not None:
            return self.__programareaname

    @program_area_name.setter
    def program_area_name( self, value: str ):
        if value is not None:
            self.__programareaname = value

    @property
    def boc_code( self ) -> str:
        if self.__boccode is not None:
            return self.__boccode

    @boc_code.setter
    def boc_code( self, value: str ):
        if value is not None:
            self.__boccode = value

    @property
    def boc_name( self ) -> str:
        if self.__bocname is not None:
            return self.__bocname

    @boc_name.setter
    def boc_name( self, value: str ):
        if value is not None:
            self.__bocname = value

    @property
    def budgeting_controls( self ) -> str:
        if self.__budgetingcontrols is not None:
            return self.__budgetingcontrols

    @budgeting_controls.setter
    def budgeting_controls( self, value: str ):
        if value is not None:
            self.__budgetingcontrols = value

    @property
    def posting_controls( self ) -> str:
        if  self.__postingcontrols is not None:
            return self.__postingcontrols

    @posting_controls.setter
    def posting_controls( self, value: str ):
        if value is not None:
            self.__postingcontrols = value

    @property
    def precommitment_controls( self ) -> str:
        if  self.__precommitmentcontrols is not None:
            return self.__precommitmentcontrols

    @precommitment_controls.setter
    def precommitment_controls( self, value: str ):
        if value is not None:
            self.__precommitmentcontrols = value

    @property
    def commitment_controls( self ) -> str:
        if self.__commitmentcontrols is not None:
            return self.__commitmentcontrols

    @commitment_controls.setter
    def commitment_controls( self, value: str ):
        if value is not None:
            self.__commitmentcontrols = value

    @property
    def obligation_controls( self ) -> str:
        if self.__obligationcontrols is not None:
            return self.__obligationcontrols

    @obligation_controls.setter
    def obligation_controls( self, value: str ):
        if value is not None:
            self.__obligationcontrols = value

    @property
    def accrual_controls( self ) -> str:
        if self.__accrualcontrols is not None:
            return self.__accrualcontrols

    @accrual_controls.setter
    def accrual_controls( self, value: str ):
        if value is not None:
            self.__accrualcontrols = value

    @property
    def expenditure_controls( self ) -> str:
        if self.__expenditurecontrols is not None:
            return self.__expenditurecontrols

    @expenditure_controls.setter
    def expenditure_controls( self, value: str ):
        if value is not None:
            self.__expenditurecontrols = value

    @property
    def expense_controls( self ) -> str:
        if self.__expensecontrols is not None:
            return self.__expensecontrols

    @expense_controls.setter
    def expense_controls( self, value: str ):
        if value is not None:
            self.__expensecontrols = value

    @property
    def reimbursement_controls( self ) -> str:
        if self.__reimbursementcontrols is not None:
            return self.__reimbursementcontrols

    @reimbursement_controls.setter
    def reimbursement_controls( self, value: str ):
        if value is not None:
            self.__reimbursementcontrols = value

    @property
    def reimbursable_agreement_controls( self ) -> str:
        if self.__reimbursableagreementcontrols is not None:
            return self.__reimbursableagreementcontrols

    @reimbursable_agreement_controls.setter
    def reimbursable_agreement_controls( self, value: str ):
        if value is not None:
            self.__reimbursableagreementcontrols = value

    @property
    def budgeted( self ) -> str:
        if self.__budgeted is not None:
            return self.__budgeted

    @budgeted.setter
    def budgeted( self, value: str ):
        if value is not None:
            self.__budgeted = value

    @property
    def posted( self ) -> float:
        if self.__posted is not None:
            return self.__posted

    @posted.setter
    def posted( self, value: float ):
        if value is not None:
            self.__posted = value

    @property
    def carryover_in( self ) -> float:
        if self.__carryoverin is not None:
            return self.__carryoverin

    @carryover_in.setter
    def carryover_in( self, value: float ):
        if value is not None:
            self.__carryoverin = value

    @property
    def carryover_out( self ) -> str:
        if self.__carryoverout is not None:
            return self.__carryoverout

    @carryover_out.setter
    def carryover_out( self, value: str ):
        if value is not None:
            self.__carryoverout = value

    @property
    def estimated_reimbursements( self ) -> str:
        if self.__reimbursementcontrols is not None:
            return self.__reimbursementcontrols

    @estimated_reimbursements.setter
    def estimated_reimbursements( self, value: str ):
        if value is not None:
            self.__estimatedreimbursements = value

    @property
    def estimated_recoveries( self ) -> str:
        if self.__estimatedrecoveries is not None:
            return self.__estimatedrecoveries

    @estimated_recoveries.setter
    def estimated_recoveries( self, value: str ):
        if value is not None:
            self.__estimatedrecoveries = value

    @property
    def fields( self ) -> list[ str ]:
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value: list[ str ] ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy = None, efy = None,
                  fundcode = None, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.BudgetDocuments
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__efy = efy if isinstance( efy, str ) and efy != '' else None
        self.__fundcode = fundcode if isinstance( fundcode, str ) and fundcode != '' else None
        self.__fields = [ 'BudgetDocumentsId',
                           'BFY',
                           'EFY',
                           'BudgetLevel',
                           'DocumentDate',
                           'LastDocumentDate',
                           'DocumentType',
                           'DocumentNumber',
                           'FundCode',
                           'FundName',
                           'RpioCode',
                           'RpioName',
                           'AhCode',
                           'AhName',
                           'OrgCode',
                           'OrgName',
                           'AccountCode',
                           'ProgramProjectName',
                           'ProgramAreaCode',
                           'ProgramAreaName',
                           'BocCode',
                           'BocName',
                           'ReimbursableAgreementControls',
                           'BudgetingControls',
                           'PostingControls',
                           'PreCommitmentControls',
                           'CommitmentControls',
                           'ObligationControls',
                           'ExpenditureControls',
                           'ExpenseControls',
                           'AccrualControls',
                           'ReimbursementControls',
                           'Budgeted',
                           'Posted',
                           'CarryOut',
                           'CarryIn',
                           'EstimatedRecoveries',
                           'EstimatedReimbursements' ]

    def get_data( self  ) -> list[ Row ]:
        try:
            _source = self.__source
            _provider = self.__provider
            _names = [ 'BFY', 'EFY', 'FundCode' ]
            _values = (self.__bfy, self.__efy, self.__fundcode)
            _dbconfig = DbConfig( _source, _provider )
            _sqlconfig = SqlConfig( names = _names, values = _values )
            _connection = Connection( self.__source )
            _sql = SqlStatement( _dbconfig, _sqlconfig )
            _sqlite = _connection.connect( )
            _cursor = _sqlite.cursor( )
            _query = _sql.get_query( )
            _db = _cursor.execute( _query )
            self.__data =  [ i for i in _db.fetchall( ) ]
            _cursor.close( )
            _sqlite.close( )
            return self.__data
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Ninja'
            _exc.cause = 'BudgetDocument'
            _exc.method = 'get_data( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def get_frame( self ) -> DataFrame:
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            _source = self.__source
            _data = BudgetData( _source )
            return _data.create_frame( )
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Ninja'
            _exc.cause = 'BudgetDocument'
            _exc.method = 'create_frame( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class BudgetContact( ):
    '''
    Constructor: BudgetContact( last: str, first: str )

    Purpose: Class defines object represent budget contact info
    '''
    __firstname = None
    __lastname = None
    __rpiocode = None
    __rpioname = None
    __section = None
    __jobtitle = None
    __zipcode = None
    __state = None
    __account = None
    __emailaddress = None
    __emailtype = None
    __displayname = None
    __officelocation = None

    @property
    def first_name( self ):
        if self.__firstname is not None:
            return self.__firstname

    @first_name.setter
    def first_name( self, value: str ):
        if value is not None:
            self.__firstname = value

    @property
    def last_name( self ):
        if self.__lastname is not None:
            return self.__lastname

    @last_name.setter
    def last_name( self, value: str ):
        if value is not None:
            self.__lastname = value

    @property
    def rpio_code( self ):
        if self.__rpiocode is not None:
            return self.__rpiocode

    @rpio_code.setter
    def rpio_code( self, value: str ):
        if value is not None:
            self.__rpiocode = value

    @property
    def rpio_name( self ):
        if self.__rpioname is not None:
            return self.__rpioname

    @rpio_name.setter
    def rpio_name( self, value: str ):
        if value is not None:
            self.__rpioname = value

    @property
    def section( self ):
        if self.__section is not None:
            return self.__section

    @section.setter
    def section( self, value: str ):
        if value is not None:
            self.__section = value

    @property
    def job_title( self ):
        if self.__jobtitle is not None:
            return self.__jobtitle

    @job_title.setter
    def job_title( self, value: str ):
        if value is not None:
            self.__jobtitle = value

    @property
    def zipcode( self ):
        if self.__zipcode is not None:
            return self.__zipcode

    @zipcode.setter
    def zipcode( self, value: str ):
        if value is not None:
            self.__zipcode = value

    @property
    def city( self ):
        if self.__city is not None:
            return self.__city

    @city.setter
    def city( self, value: str ):
        if value is not None:
            self.__city = value

    @property
    def state( self ):
        if self.__state is not None:
            return self.__state

    @state.setter
    def state( self, value: str ):
        if value is not None:
            self.__state = value

    @property
    def account( self ):
        if self.__account is not None:
            return self.__account

    @account.setter
    def account( self, value: str ):
        if value is not None:
            self.__account = value

    @property
    def email_address( self ):
        if self.__emailaddress is not None:
            return self.__emailaddress

    @email_address.setter
    def email_address( self, value: str ):
        if value is not None:
            self.__emailaddress = value

    @property
    def display_name( self ):
        if self.__displayname is not None:
            return self.__displayname

    @display_name.setter
    def display_name( self, value: str ):
        if value is not None:
            self.__displayname = value

    @property
    def email_type( self ):
        if self.__emailtype is not None:
            return self.__emailtype

    @email_type.setter
    def email_type( self, value: str ):
        if value is not None:
            self.__emailtype = value

    @property
    def office_location( self ):
        if self.__officelocation is not None:
            return self.__officelocation

    @office_location.setter
    def office_location( self, value: str ):
        if value is not None:
            self.__officelocation = value

    def __init__( self, last: str, first: str ):
        self.__lastname = last
        self.__first = first

class BudgetControl( ):
    '''
    Constructor:  BudgetControl( fund, pvdr = Provider.SQLite )

    Purpose;  Class defines object representing compass control data'''
    __source = None
    __provider = None
    __budgetcontrolsid = None
    __code = None
    __name = None
    __budgetedtranstype = None
    __postedtranstype = None
    __estimatedreimbursementstranstype = None
    __spendingadjustmenttranstype = None
    __estimatedrecoveriestranstype = None
    __actualrecoveriestranstype = None
    __statusreservetranstype = None
    __profitlosstranstype = None
    __estimatedreimbursementsspendingoptions = None
    __estimatedreimbursementsbudgetingoptions = None
    __trackagreementlowerlevels = None
    __budgetestimatedlowerlevels = None
    __recoverynextlevel = None
    __recoverybudgetmismatch = None
    __profitlossspendingoption = None
    __profitlossbudgetingoption = None
    __recoveriescarryinlowerlevelcontrol = None
    __recoveriescarryinlowerlevel = None
    __recoveriescarryinamountcontrol = None
    __budgetedcontrol = None
    __postedcontrol = None
    __precommitmentspendingcontrol = None
    __commitmentspendingcontrol = None
    __obligationspendingcontrol = None
    __accrualspendingcontrol = None
    __expenditurespendingcontrol = None
    __expensespendingcontrol = None
    __reimbursementspendingcontrol = None
    __reimbursableagreementspendingcontrol = None
    __ftebudgetingcontrol = None
    __ftespendingcontrol = None
    __transactiontypecontrol = None
    __authoritydistributioncontrol = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ) -> int:
        if self.__budgetcontrolsid is not None:
            return self.__budgetcontrolsid

    @id.setter
    def id( self, value: int ):
        if value is not None:
            self.__budgetcontrolsid = value

    @property
    def code( self ) -> str:
        if self.__code is not None:
            return self.__code

    @code.setter
    def code( self, value: str ):
        if value is not None:
            self.__code = value

    @property
    def name( self ) -> str:
        if self.__name is not None:
            return self.__name

    @code.setter
    def code( self, value: str ):
        if value is not None:
            self.__name = value

    @property
    def budgeted_transtype( self ) -> str:
        if self.__budgetedtranstype is not None:
            return self.__budgetedtranstype

    @budgeted_transtype.setter
    def budgeted_transtype( self, value: str ):
        if value is not None:
            self.__budgetedtranstype = value

    @property
    def posted_transtype( self ) -> str:
        if self.__postedtranstype is not None:
            return self.__postedtranstype

    @posted_transtype.setter
    def posted_transtype( self, value: str ):
        if value is not None:
            self.__postedtranstype = value

    @property
    def spending_adjustment_transtype( self ) -> str:
        if self.__spendingadjustmenttranstype is not None:
            return self.__spendingadjustmenttranstype

    @spending_adjustment_transtype.setter
    def spending_adjustment_transtype( self, value: str ):
        if value is not None:
            self.__spendingadjustmenttranstype = value

    @property
    def estimated_reimbursements_transtype( self ) -> str:
        if self.__estimatedreimbursementstranstype is not None:
            return self.__estimatedreimbursementstranstype

    @estimated_reimbursements_transtype.setter
    def estimated_reimbursements_transtype( self, value: str ):
        if value is not None:
            self.__estimatedreimbursementstranstype = value

    @property
    def estimated_recoveries_transtype( self ) -> str:
        if self.__estimatedrecoveriestranstype is not None:
            return self.__estimatedrecoveriestranstype

    @estimated_recoveries_transtype.setter
    def estimated_recoveries_transtype( self, value: str ):
        if value is not None:
            self.__estimatedrecoveriestranstype = value

    @property
    def actual_recoveries_transtype( self ) -> str:
        if self.__actualrecoveriestranstype is not None:
            return self.__actualrecoveriestranstype

    @actual_recoveries_transtype.setter
    def actual_recoveries_transtype( self, value: str ):
        if value is not None:
            self.__actualrecoveriestranstype = value

    @property
    def status_reserve_transtype( self ) -> str:
        if self.__statusreservetranstype is not None:
            return self.__statusreservetranstype

    @status_reserve_transtype.setter
    def status_reserve_transtype( self, value: str ):
        if value is not None:
            self.__statusreservetranstype = value

    @property
    def profit_loss_transtype( self ) -> str:
        if self.__profitlosstranstype is not None:
            return self.__profitlosstranstype

    @profit_loss_transtype.setter
    def profit_loss_transtype( self, value: str ):
        if value is not None:
            self.__profitlosstranstype = value

    @property
    def estimated_reimbursements_spending_options( self ) -> str:
        if self.__estimatedreimbursementsspendingoptions is not None:
            return self.__estimatedreimbursementsspendingoptions

    @estimated_reimbursements_spending_options.setter
    def estimated_reimbursements_spending_options( self, value: str ):
        if value is not None:
            self.__estimatedreimbursementsspendingoptions = value

    @property
    def estimated_reimbursements_budgeting_options( self ) -> str:
        if self.__estimatedreimbursementsbudgetingoptions is not None:
            return self.__estimatedreimbursementsbudgetingoptions

    @estimated_reimbursements_budgeting_options.setter
    def estimated_reimbursements_budgeting_options( self, value: str ):
        if value is not None:
            self.__estimatedreimbursementsbudgetingoptions = value

    @property
    def tracking_agreement_lower_levels( self ) -> str:
        if self.__trackingagreementlowerlevels is not None:
            return self.__trackingagreementlowerlevels

    @tracking_agreement_lower_levels.setter
    def tracking_agreement_lower_levels( self, value: str ):
        if value is not None:
            self.__trackingagreementlowerlevels = value

    @property
    def budget_estimated_lowerlevels( self ) -> str:
        if self.__budgetestimatedlowerlevels is not None:
            return self.__budgetestimatedlowerlevels

    @budget_estimated_lowerlevels.setter
    def budget_estimated_lowerlevels( self, value: str ):
        if value is not None:
            self.__budgetestimatedlowerlevels = value

    @property
    def recovery_nextlevel( self ) -> str:
        if self.__recoverynextlevel is not None:
            return self.__recoverynextlevel

    @recovery_nextlevel.setter
    def recovery_nextlevel( self, value: str ):
        if value is not None:
            self.__recoverynextlevel = value

    @property
    def recovery_budget_mismatch( self ) -> str:
        if self.__recoverybudgetmismatch is not None:
            return self.__recoverybudgetmismatch

    @recovery_budget_mismatch.setter
    def recovery_budget_mismatch( self, value: str ):
        if value is not None:
            self.__recoverybudgetmismatch = value

    @property
    def profit_loss_spending_option( self ) -> str:
        if self.__profitlossspendingoption is not None:
            return self.__profitlossspendingoption

    @profit_loss_spending_option.setter
    def profit_loss_spending_option( self, value: str ):
        if value is not None:
            self.__profitlossspendingoption = value

    @property
    def profit_loss_budgeting_option( self ) -> str:
        if self.__profitlossbudgetingoption is not None:
            return self.__profitlossbudgetingoption

    @profit_loss_budgeting_option.setter
    def profit_loss_budgeting_option( self, value: str ):
        if value is not None:
            self.__profitlossbudgetingoption = value

    @property
    def recoveries_carryin_lowerlevel_control( self ) -> str:
        if self.__recoveriescarryinlowerelevelcontrol is not None:
            return self.__recoveriescarryinlowerelevelcontrol

    @recoveries_carryin_lowerlevel_control.setter
    def recoveries_carryin_lowerlevel_control( self, value: str ):
        if value is not None:
            self.__recoveriescarryinlowerelevelcontrol = value

    @property
    def recoveries_carryin_lowerlevel( self ) -> str:
        if self.__recoveriescarryinlowerlevel is not None:
            return self.__recoveriescarryinlowerlevel

    @recoveries_carryin_lowerlevel.setter
    def recoveries_carryin_lowerlevel( self, value: str ):
        if value is not None:
            self.__recoveriescarryinlowerlevel = value

    @property
    def recoveries_carryin_amount_control( self ) -> str:
        if self.__recoveriescarryinamountcontrol is not None:
            return self.__recoveriescarryinamountcontrol

    @recoveries_carryin_amount_control.setter
    def recoveries_carryin_amount_control( self, value: str ):
        if value is not None:
            self.__recoveriescarryinamountcontrol = value

    @property
    def budgeted_control( self ) -> str:
        if self.__budgetedcontrol is not None:
            return self.__budgetedcontrol

    @budgeted_control.setter
    def budgeted_control( self, value: str ):
        if value is not None:
            self.__budgetedcontrol = value

    @property
    def posted_control( self ) -> str:
        if self.__postedcontrol is not None:
            return self.__postedcontrol

    @posted_control.setter
    def posted_control( self, value: str ):
        if value is not None:
            self.__postedcontrol = value

    @property
    def precommitment_spending_control( self ) -> str:
        if self.__precommitmentspendingcontrol is not None:
            return self.__precommitmentspendingcontrol

    @precommitment_spending_control.setter
    def precommitment_spending_control( self, value: str ):
        if value is not None:
            self.__precommitmentspendingcontrol = value

    @property
    def commitment_spending_control( self ) -> str:
        if self.__commitmentspendingcontrol is not None:
            return self.__commitmentspendingcontrol

    @commitment_spending_control.setter
    def commitment_spending_control( self, value: str ):
        if value is not None:
            self.__commitmentspendingcontrol = value

    @property
    def obligation_spending_control( self ) -> str:
        if self.__obligationspendingcontrol is not None:
            return self.__obligationspendingcontrol

    @obligation_spending_control.setter
    def obligation_spending_control( self, value: str ):
        if value is not None:
            self.__obligationspendingcontrol = value

    @property
    def accrual_spending_control( self ) -> str:
        if self.__accrualspendingcontrol is not None:
            return self.__accrualspendingcontrol

    @accrual_spending_control.setter
    def accrual_spending_control( self, value: str ):
        if value is not None:
            self.__accrualspendingcontrol = value

    @property
    def expenditure_spending_control( self ) -> str:
        if self.__expenditurespendingcontrol is not None:
            return self.__expenditurespendingcontrol

    @expenditure_spending_control.setter
    def expenditure_spending_control( self, value: str ):
        if value is not None:
            self.__expenditurespendingcontrol = value

    @property
    def expense_spending_control( self ) -> str:
        if self.__expensespendingcontrol is not None:
            return self.__expensespendingcontrol

    @expense_spending_control.setter
    def expense_spending_control( self, value: str ):
        if value is not None:
            self.__expensespendingcontrol = value

    @property
    def reimbursement_spending_control( self ) -> str:
        if self.__reimbursementspendingcontrol is not None:
            return self.__reimbursementspendingcontrol

    @reimbursement_spending_control.setter
    def reimbursement_spending_control( self, value: str ):
        if value is not None:
            self.__reimbursementspendingcontrol = value

    @property
    def reimbursableagreement_spending_control( self ) -> str:
        if self.__reimbursableagreementspendingcontrol is not None:
            return self.__reimbursableagreementspendingcontrol

    @reimbursableagreement_spending_control.setter
    def reimbursableagreement_spending_control( self, value: str ):
        if value is not None:
            self.__reimbursableagreementspendingcontrol = value

    @property
    def fte_budgeting_control( self ) -> str:
        if self.__ftebudgetingcontrol is not None:
            return self.__ftebudgetingcontrol

    @fte_budgeting_control.setter
    def fte_budgeting_control( self, value: str ):
        if value is not None:
            self.__ftebudgetingcontrol = value

    @property
    def fte_spending_control( self ) -> str:
        if  self.__ftespendingcontrol is not None:
            return self.__ftespendingcontrol

    @fte_spending_control.setter
    def fte_spending_control( self, value: str ):
        if value is not None:
            self.__ftespendingcontrol = value

    @property
    def transaction_type_control( self ) -> str:
        if  self.__transactiontypecontrol is not None:
            return self.__transactiontypecontrol

    @transaction_type_control.setter
    def transaction_type_control( self, value: str ):
        if value is not None:
            self.__transactiontypecontrol = value

    @property
    def authority_distribution_control( self ) -> str:
        if  self.__authoritydistributioncontrol is not None:
            return self.__authoritydistributioncontrol

    @authority_distribution_control.setter
    def authority_distribution_control( self, value: str ):
        if value is not None:
            self.__authoritydistributioncontrol = value

    @property
    def fields( self ) -> list[ str ]:
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value: list[ str ] ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy = None, efy = None, fund = None, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.BudgetControls
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__efy = efy if isinstance( efy, str ) and efy != '' else None
        self.__fundcode = fund if isinstance( fund, str ) and fund != '' else None
        self.__fields = [ 'BudgetControlValuesId',
                           'Code',
                           'Name',
                           'SecurityOrg',
                           'BudgetingTransType',
                           'PostedTransType',
                           'EstimatedReimbursableTransType',
                           'SpendingAdjustmentTransType',
                           'EstimatedRecoveriesTransType',
                           'ActualRecoveriesTransType',
                           'StategicReserveTransType',
                           'ProfLossTransType',
                           'EstimatedReimbursableSpendingOption',
                           'EstimatedReimbursableBudgetingOption',
                           'TrackAgreementLowerLevel',
                           'BudgetEstimateLowerLevel',
                           'EstimatedRecoveriesSpendingOption',
                           'EstimatedRecoveriesBudgetingOption',
                           'RecordNextLevel',
                           'RecordBudgetingMismatch',
                           'ProfitLossSpendingOption',
                           'ProfitLossBudgetingOption',
                           'RecordCarryInLowerLevel',
                           'RecordCarryInLowerLevelControl',
                           'RecordCarryInAmountControl',
                           'BudgetingControl',
                           'PostingControl',
                           'PreCommitmentSpendingControl',
                           'CommitmentSpendingControl',
                           'ObligationSpendingControl',
                           'AccrualSpendingControl',
                           'ExpenditureSpendingControl',
                           'ExpenseSpendingControl',
                           'ReimbursableSpendingControl',
                           'ReimbursableAgreementSpendingControl',
                           'FteBudgetingControl',
                           'FteSpendingControl',
                           'TransactionTypeControl',
                           'AuthorityDistributionControl' ]

    def get_data( self  ) -> list[ Row ]:
        try:
            _source = self.__source
            _provider = self.__provider
            _names = [ 'BFY', 'EFY', 'FundCode' ]
            _values = (self.__bfy, self.__efy, self.__fundcode)
            _dbconfig = DbConfig( _source, _provider )
            _sqlconfig = SqlConfig( names = _names, values = _values )
            _connection = Connection( self.__source )
            _sql = SqlStatement( _dbconfig, _sqlconfig )
            _sqlite = _connection.connect( )
            _cursor = _sqlite.cursor( )
            _query = _sql.get_query( )
            _db = _cursor.execute( _query )
            self.__data =  [ i for i in _db.fetchall( ) ]
            _cursor.close( )
            _sqlite.close( )
            return self.__data
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Ninja'
            _exc.cause = 'BudgetControl'
            _exc.method = 'get_data( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def get_frame( self ) -> DataFrame:
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            _source = self.__source
            _data = BudgetData( _source )
            return _data.create_frame( )
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Ninja'
            _exc.cause = 'BudgetControl'
            _exc.method = 'create_frame( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class BudgetFiscalYear( ):
    '''
    Constructor: BudgetFiscalYear( bfy, efy, date = None, pvdr = Provider.SQLite ).


    Purpose:  Class to describe the federal fiscal year'''
    __source = None
    __provider = None
    __budgetfiscalyearsid = None
    __input = None
    __bfy = None
    __efy = None
    __today = None
    __date = None
    __startdate = None
    __enddate = None
    __expiration = None
    __weekends = None
    __workdays = None
    __currentyear = None
    __currentmonth = None
    __currentday = None
    __holidays = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ) -> int:
        if self.__budgetfiscalyearsid is not None:
            return self.__budgetfiscalyearsid

    @id.setter
    def id( self, value: int ):
        if value is not None:
            self.__budgetfiscalyearsid = value

    @property
    def first_year( self ) -> str:
        if self.__bfy is not None:
            return self.__bfy

    @first_year.setter
    def first_year( self, value: str ):
        if value is not None:
            self.__bfy = value

    @property
    def last_year( self ) -> str:
        if self.__efy is not None:
            return self.__efy

    @last_year.setter
    def last_year( self, value: str ):
        if value is not None:
            self.__efy = value

    @property
    def current_year( self ) -> int:
        if self.__currentyear is not None:
            return self.__currentyear

    @current_year.setter
    def current_year( self, value: int ):
        if value is not None:
            self.__currentyear = value

    @property
    def start_date( self ) -> datetime:
        if self.__startdate is not None:
            return self.__startdate

    @start_date.setter
    def start_date( self, value: datetime ):
        if value is not None:
            self.__startdate = value

    @property
    def end_date( self ) -> datetime:
        if self.__enddate is not None:
            return self.__enddate

    @end_date.setter
    def end_date( self, value: datetime ):
        if value is not None:
            self.__enddate = value

    @property
    def expiration( self ) -> str:
        if self.__expiration is not None:
            return self.__expiration

    @expiration.setter
    def expiration( self, value: str ):
        if value is not None:
            self.__expiration = value

    @property
    def weekends( self ) -> str:
        if self.__weekends is not None:
            return self.__weekends

    @weekends.setter
    def weekends( self, value: str ):
        if value is not None:
            self.__weekends = value

    @property
    def workdays( self ) -> str:
        if self.__workdays is not None:
            return self.__workdays

    @workdays.setter
    def workdays( self, value: str ):
        if value is not None:
            self.__workdays = value

    @property
    def today( self ) -> datetime:
        if self.__today is not None:
            return self.__today

    @today.setter
    def today( self, value: datetime ):
        if value is not None:
            self.__today = value

    @property
    def date( self ) -> datetime:
        if self.__date is not None:
            return self.__date

    @date.setter
    def date( self, value: datetime ):
        if value is not None:
            self.__date = value

    @property
    def current_day( self ) -> int:
        if self.__currentday is not None:
            return self.__currentday

    @current_day.setter
    def current_day( self, value: int ):
        if value is not None:
            self.__currentday = value

    @property
    def current_month( self ) -> int:
        if self.__currentmonth is not None:
            return self.__currentmonth

    @property
    def holidays( self ) -> list[ str ]:
        if self.__holidays is not None:
            return self.__holidays

    @property
    def data( self ) -> list:
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, value: list ):
        if value is not None:
            self.__data = value

    @property
    def table( self ) -> DataFrame:
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, frame: DataFrame ):
        if frame is not None:
            self.__frame = frame

    @property
    def fields( self ) -> list[ str ]:
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value: list[ str ] ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy: str, efy: str,
                  dt: datetime = None, provider: Provider = Provider.SQLite ):
        self.__provider = provider
        self.__source  = Source.FiscalYears
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__efy = efy if isinstance( efy, str ) and len( efy ) <= 4 else None
        self.__today = datetime.today( )
        self.__currentday = datetime.today( ).day
        self.__currentmonth = datetime.today( ).month
        self.__date = dt if isinstance( dt, datetime ) else datetime.today( )
        self.__currentyear = datetime.today( ).year
        self.__startdate = datetime( datetime.today( ).year, 10, 1 )
        self.__enddate = datetime( datetime.today( ).year + 1, 9, 30 )
        self.__holidays = [ 'Columbus', 'Veterans', 'Thanksgiving', 'Christmas',
                            'NewYearsDay', 'MartinLutherKing', 'Washingtons',
                            'Memorial', 'Juneteenth', 'Independence', 'Labor' ]
        self.__fields = [ 'FiscalYearsId',
                          'BFY',
                          'EFY',
                          'StartDate',
                          'EndDate',
                          'Columbus',
                          'Veterans',
                          'Thanksgiving',
                          'Christmas',
                          'NewYears',
                          'MartinLutherKing',
                          'Presidents',
                          'Memorial',
                          'Juneteenth',
                          'Independence',
                          'Labor',
                          'ExpiringYear',
                          'ExpirationDate',
                          'CancellationDate',
                          'Workdays',
                          'Weekdays',
                          'Weekends',
                          'Availability' ]

    def __str__( self ) -> str:
        if self.__bfy is not None:
            return self.__bfy

    def get_data( self  ) -> list[ Row ]:
        try:
            _source = self.__source
            _provider = self.__provider
            _names = [ 'BFY', 'EFY' ]
            _values = (self.__bfy, self.__efy)
            _dbconfig = DbConfig( _source, _provider )
            _sqlconfig = SqlConfig( names = _names, values = _values )
            _connection = Connection( self.__source )
            _sql = SqlStatement( _dbconfig, _sqlconfig )
            _sqlite = _connection.connect( )
            _cursor = _sqlite.cursor( )
            _query = _sql.get_query( )
            _db = _cursor.execute( _query )
            self.__data =  [ i for i in _db.fetchall( ) ]
            _cursor.close( )
            _sqlite.close( )
            return self.__data
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Execution'
            _exc.cause = 'BudgetFiscalYear'
            _exc.method = 'get_data( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def get_frame( self ) -> DataFrame:
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            _source = self.__source
            _data = BudgetData( _source )
            return _data.create_frame( )
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Execution'
            _exc.cause = 'BudgetFiscalYear'
            _exc.method = 'create_frame( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class BudgetObjectClass( ):
    '''
    Constructor:  BudgetObjectClass( code, pvdr = Provider.SQLite  ).

    Purpose:  Defines the BudgetObjectClass Class
    '''
    __source = None
    __provider = None
    __budgetobjectclassesid = None
    __code = None
    __boc = None
    __name = None
    __value = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ) -> int:
        if self.__accountsid is not None:
            return self.__accountsid

    @id.setter
    def id( self, value: int ):
        if value is not None:
            self.__accountsid = value

    @property
    def code( self ) -> str:
        if  self.__code is not None:
            return self.__code

    @code.setter
    def code( self, value: str ):
        if value is not None:
            self.__code = value

    @property
    def name( self ) -> str:
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, value: str ):
        if value is not None:
            self.__name = value

    @property
    def value( self ) -> str:
        if self.__value is not None:
            return self.__value

    @value.setter
    def value( self, val: str ):
        if val is not None:
            self.__value = val

    @property
    def data( self ) -> list:
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, value: list ):
        if value is not None:
            self.__data = value

    @property
    def table( self ) -> DataFrame:
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, value: DataFrame ):
        if value is not None:
            self.__frame = value

    @property
    def fields( self ) -> list[ str ]:
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value: list[ str ] ):
        if value is not None:
            self.__fields = value

    def __init__( self, code: str, provider: Provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.BudgetObjectClasses
        self.__code = code
        self.__fields = [ 'BudgetObjectClassesId',
                          'Code',
                          'Name' ]

    def __str__( self ) -> str:
        if self.__code is not None:
            return self.__code

    def get_data( self  ) -> list[ Row ]:
        try:
            _source = self.__source
            _provider = self.__provider
            _names = [ 'Code', ]
            _values = (self.__code,)
            _dbconfig = DbConfig( _source, _provider )
            _sqlconfig = SqlConfig( names = _names, values = _values )
            _connection = Connection( self.__source )
            _sql = SqlStatement( _dbconfig, _sqlconfig )
            _sqlite = _connection.connect( )
            _cursor = _sqlite.cursor( )
            _query = _sql.get_query( )
            _db = _cursor.execute( _query )
            self.__data =  [ i for i in _db.fetchall( ) ]
            _cursor.close( )
            _sqlite.close( )
            return self.__data
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Execution'
            _exc.cause = 'BudgetObjectClass'
            _exc.method = 'get_data( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def get_frame( self ) -> DataFrame:
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            _source = self.__source
            _data = BudgetData( _source )
            return _data.create_frame( )
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Execution'
            _exc.cause = 'BudgetObjectClass'
            _exc.method = 'create_frame( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class BudgetaryResourceExecution( ):
    '''
    Constructor: BudgetaryResourceExecution( bfy: str, efy: str,
                  main: str, pvdr: Provider = Provider.SQLite )

    Purpose:  Class defines object representing the MAX A-11 DE/SF-133
    Status Of Budgetary Resources Execution Report
    '''
    __source = None
    __provider = None
    __budgetaryresourceexecutionid = None
    __bfy = None
    __efy = None
    __fundcode = None
    __treasuryaccountcode = None
    __treasuryaccountname = None
    __budgetaccountcode = None
    __budgetaccountname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ) -> int:
        if self.__budgetaryresourceexecutionid is not None:
            return self.__budgetaryresourceexecutionid

    @id.setter
    def id( self, value: int ):
        if value is not None:
            self.__budgetaryresourceexecutionid = value

    @property
    def bfy( self ) -> str:
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value: str ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ) -> str:
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value: str ):
        if value is not None:
            self.__efy = value

    @property
    def treasury_account_code( self ) -> str:
        if self.__treasuryaccountcode is not None:
            return self.__treasuryaccountcode

    @treasury_account_code.setter
    def treasury_account_code( self, value: str ):
        if value is not None:
            self.__treasuryaccountcode = value

    @property
    def treasury_account_name( self ) -> str:
        if self.__treasuryaccountname is not None:
            return self.__treasuryaccountname

    @treasury_account_name.setter
    def treasury_account_name( self, value: str ):
        if value is not None:
            self.__treasuryaccountname = value

    @property
    def budget_account_code( self ) -> str:
        if self.__budgetaccountcode is not None:
            return self.__budgetaccountcode

    @budget_account_code.setter
    def budget_account_code( self, value: str ):
        if value is not None:
            self.__budgetaccountcode = value

    @property
    def budget_account_name( self ) -> str:
        if  self.__budgetaccountname is not None:
            return self.__budgetaccountname

    @budget_account_name.setter
    def budget_account_name( self, value: str ):
        if value is not None:
            self.__budgetaccountname = value

    @property
    def fields( self ) -> list[ str ]:
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value: list[ str ] ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy: str, efy: str,
                  main: str, provider: Provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.BudgetaryResourceExecution
        self.__bfy = bfy
        self.__efy = efy
        self.__budgetaccountcode = main
        self.__fields = [ 'BudgetaryResourceExecutionId',
                          'FiscalYear',
                          'BFY',
                          'EFY',
                          'LastUpdate',
                          'TreasurySymbol',
                          'OmbAccount',
                          'TreasuryAgencyCode',
                          'TreasuryAccountCode',
                          'STAT',
                          'CreditIndicator',
                          'LineNumber',
                          'LineDescription',
                          'SectionName',
                          'SectionNumber',
                          'LineType',
                          'FinancingAccounts',
                          'November',
                          'January',
                          'Feburary',
                          'April',
                          'May',
                          'June',
                          'August',
                          'October',
                          'Amount1',
                          'Amount2',
                          'Amount3',
                          'Amount4',
                          'Agency',
                          'Bureau' ]

    def get_data( self  ) -> list[ Row ]:
        try:
            _source = self.__source
            _provider = self.__provider
            _names = [ 'BFY', 'EFY', 'OmbAccountCode', ]
            _values = (self.__bfy, self.__efy, self.__budgetaccountcode)
            _dbconfig = DbConfig( _source, _provider )
            _sqlconfig = SqlConfig( names = _names, values = _values )
            _connection = Connection( self.__source )
            _sql = SqlStatement( _dbconfig, _sqlconfig )
            _sqlite = _connection.connect( )
            _cursor = _sqlite.cursor( )
            _query = _sql.get_query( )
            _db = _cursor.execute( _query )
            self.__data =  [ i for i in _db.fetchall( ) ]
            _cursor.close( )
            _sqlite.close( )
            return self.__data
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Reporting'
            _exc.cause = 'BudgetaryResourceExecution'
            _exc.method = 'get_data( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def get_frame( self ) -> DataFrame:
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            _source = self.__source
            _data = BudgetData( _source )
            return _data.create_frame( )
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Reporting'
            _exc.cause = 'BudgetaryResourceExecution'
            _exc.method = 'create_frame( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class Outlay( ):
    '''
    Constructor: Outlay( account: str, pvdr: Provider = Provider.SQLite  )

    Purpose: Class defines object that provides OMB data
    '''
    __source = None
    __provider = None
    __budgetoutlaysid = None
    __reportyear = None
    __budgetaccountcode = None
    __budgetaccountname = None
    __linenumber = None
    __linesection = None
    __linename = None
    __linecategory = None
    __beacategory = None
    __beacategoryname = None
    __prioryear = None
    __currentyear = None
    __budgetyear = None
    __outyear1 = None
    __outyear2 = None
    __outyear3 = None
    __outyear4 = None
    __outyear5 = None
    __outyear6 = None
    __outyear7 = None
    __outyear8 = None
    __outyear9 = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ) -> int:
        if self.__budgetoutlaysid is not None:
            return self.__budgetoutlaysid

    @id.setter
    def id( self, value: int ):
        if value is not None:
            self.__budgetoutlaysid = value

    @property
    def report_year( self ) -> str:
        if self.__reportyear is not None:
            return self.__reportyear

    @report_year.setter
    def report_year( self, value: str ):
        if value is not None:
            self.__reportyear = value

    @property
    def line_number( self ) -> str:
        if self.__linenumber is not None:
            return self.__linenumber

    @line_number.setter
    def line_number( self, value: str ):
        if value is not None:
            self.__linenumber = value

    @property
    def line_section( self ) -> str:
        if self.__linesection is not None:
            return self.__linesection

    @line_section.setter
    def line_section( self, value: str ):
        if value is not None:
            self.__linesection = value

    @property
    def line_name( self ) -> str:
        if self.__linename is not None:
            return self.__linename

    @line_name.setter
    def line_name( self, value: str ):
        if value is not None:
            self.__linename = value

    @property
    def line_category( self ) -> str:
        if self.__linecategory is not None:
            return self.__linecategory

    @line_category.setter
    def line_category( self, value: str ):
        if value is not None:
            self.__linecategory = value

    @property
    def bea_category( self ) -> str:
        if self.__beacategory is not None:
            return self.__beacategory

    @bea_category.setter
    def bea_category( self, value: str ):
        if value is not None:
            self.__beacategory = value

    @property
    def bea_category_name( self ) -> str:
        if  self.__beacategoryname is not None:
            return self.__beacategoryname

    @bea_category_name.setter
    def bea_category_name( self, value: str ):
        if value is not None:
            self.__beacategoryname = value

    @property
    def budget_account_code( self ) -> str:
        if self.__budgetaccountcode is not None:
            return self.__budgetaccountcode

    @budget_account_code.setter
    def budget_account_code( self, value: str ):
        if value is not None:
            self.__budgetaccountcode = value

    @property
    def budget_account_name( self ) -> str:
        if self.__budgetaccountname is not None:
            return self.__budgetaccountname

    @budget_account_name.setter
    def budget_account_name( self, value: str ):
        if value is not None:
            self.__budgetaccountname = value

    @property
    def prior_year( self ) -> float:
        if self.__prioryear is not None:
            return self.__prioryear

    @prior_year.setter
    def prior_year( self, value: float ):
        if value is not None:
            self.__prioryear = value

    @property
    def current_year( self ) -> float:
        if self.__currentyear is not None:
            return self.__currentyear

    @current_year.setter
    def current_year( self, value: float):
        if  value is not None:
            self.__currentyear = value

    @property
    def budget_year( self ) -> float:
        if self.__budgetyear is not None:
            return self.__budgetyear

    @budget_year.setter
    def budget_year( self, value: float ):
        if value is not None:
            self.__budgetyear = value

    @property
    def out_year_1( self ) -> float:
        if self.__outyear1 is not None:
            return self.__outyear1

    @out_year_1.setter
    def out_year_1( self, value: float):
        if value is not None:
            self.__outyear1 = value

    @property
    def out_year_2( self ) -> float:
        if self.__outyear2 is not None:
            return self.__outyear2

    @out_year_2.setter
    def out_year_2( self, value: float ):
        if value is not None:
            self.__outyear2 = value

    @property
    def out_year_3( self ) -> float:
        if self.__outyear3 is not None:
            return self.__outyear3

    @out_year_3.setter
    def out_year_3( self, value: float ):
        if value is not None:
            self.__outyear3 = value

    @property
    def out_year_4( self ) -> float:
        if self.__outyear4 is not None:
            return self.__outyear4

    @out_year_4.setter
    def out_year_4( self, value: float ):
        if value is not None:
            self.__outyear4 = value

    @property
    def out_year_5( self ) -> float:
        if self.__outyear5 is not None:
            return self.__outyear5

    @out_year_5.setter
    def out_year_5( self, value: float ):
        if value is not None:
            self.__outyear5 = value

    @property
    def out_year_6( self ) -> float:
        if self.__outyear6 is not None:
            return self.__outyear6

    @out_year_6.setter
    def out_year_6( self, value: float ):
        if value is not None:
            self.__outyear6 = value

    @property
    def out_year_7( self ) -> float:
        if self.__outyear7 is not None:
            return self.__outyear7

    @out_year_7.setter
    def out_year_7( self, value: float ):
        if value is not None:
            self.__outyear7 = value

    @property
    def out_year_8( self ) -> float:
        if self.__outyear8 is not None:
            return self.__outyear8

    @out_year_8.setter
    def out_year_8( self, value: float ):
        if value is not None:
            self.__outyear8 = value

    @property
    def out_year_9( self ) -> float:
        if self.__outyear9 is not None:
            return self.__outyear9

    @out_year_9.setter
    def out_year_9( self, value: float ):
        if value is not None:
            self.__outyear9 = value

    @property
    def fields( self ) -> list[ str ]:
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value: list[ str ] ):
        if value is not None:
            self.__fields = value

    def __init__( self, account: str, provider: Provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.Outlays
        self.__budgetaccountcode = account
        self.__fields = [ 'BudgetOutlaysId',
                          'ReportYear',
                          'Category',
                          'AgencyName',
                          'LineNumber',
                          'LineSection',
                          'OmbAccount',
                          'LineTitle',
                          'AccountType',
                          'AuthorityTypeName',
                          'Line',
                          'AuthorityType',
                          'PriorYear',
                          'CurrentYear',
                          'BudgetYear',
                          'BudgetYear1',
                          'BudgetYear2',
                          'BudgetYear3',
                          'BudgetYear4',
                          'BudgetYear5',
                          'BudgetYear6',
                          'BudgetYear7',
                          'BudgetYear8',
                          'BudgetYear9' ]

    def get_data( self  ) -> list[ Row ]:
        try:
            _source = self.__source
            _provider = self.__provider
            _names = [ 'OmbAccountCode', ]
            _values = (self.__budgetaccountcode,)
            _dbconfig = DbConfig( _source, _provider )
            _sqlconfig = SqlConfig( names = _names, values = _values )
            _connection = Connection( self.__source )
            _sql = SqlStatement( _dbconfig, _sqlconfig )
            _sqlite = _connection.connect( )
            _cursor = _sqlite.cursor( )
            _query = _sql.get_query( )
            _db = _cursor.execute( _query )
            self.__data =  [ i for i in _db.fetchall( ) ]
            _cursor.close( )
            _sqlite.close( )
            return self.__data
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Reporting'
            _exc.cause = 'BudgetOutlay'
            _exc.method = 'get_data( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def get_frame( self ) -> DataFrame:
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            _source = self.__source
            _data = BudgetData( _source )
            return _data.create_frame( )
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Reporting'
            _exc.cause = 'BudgetOutlay'
            _exc.method = 'create_frame( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class CongressionalControl( ):
    '''
    Constructor: CongressionalControl( bfy, fund, pvdr = Provider.SQLite )

    Purpose:  Class defining object representing congressional control data'''
    __source = None
    __provider = None
    __congressionalcontrolsid = None
    __bfy = None
    __efy = None
    __fundcode = None
    __fundname = None
    __programprojectcode = None
    __programprojectname = None
    __programareacode = None
    __programareaname = None
    __subprojectcode = None
    __subprojectname = None
    __reprogrammingrestriction = None
    __increaserestriction = None
    __decreaserestriction = None
    __memorandumrequired = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ) -> int:
        if self.__congressionalcontrolsid is not None:
            return self.__congressionalcontrolsid

    @id.setter
    def id( self, value: int ):
        if value is not None:
            self.__congressionalcontrolsid = value

    @property
    def bfy( self ) -> str:
        if self.__bfy is not None:
            return self.__bfy

    @property
    def bfy( self ) -> str:
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value: str ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ) -> str:
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value: str ):
        if value is not None:
            self.__efy = value

    @property
    def fund_code( self ) -> str:
        if self.__fundcode is not None:
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value: str ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund_name( self ) -> str:
        if self.__fundname is not None:
            return self.__fundname

    @fund_name.setter
    def fund_name( self, value: str ):
        if value is not None:
            self.__fundname = value

    @property
    def program_project_code( self ) -> str:
        if self.__programprojectcode is not None:
            return self.__programprojectcode

    @program_project_code.setter
    def program_project_code( self, value: str ):
        if value is not None:
            self.__programprojectcode = value

    @property
    def program_project_name( self ) -> str:
        if self.__programprojectname is not None:
            return self.__programprojectname

    @program_project_name.setter
    def program_project_name( self, value: str ):
        if value is not None:
            self.__programprojectname = value

    @property
    def sub_project_code( self ) -> str:
        if self.__subprojectcode is not None:
            return self.__subprojectcode

    @sub_project_code.setter
    def sub_project_code( self, value: str ):
        if value is not None:
            self.__subprojectcode = value

    @property
    def sub_project_name( self ) -> str:
        if self.__subprojectname is not None:
            return self.__subprojectname

    @sub_project_name.setter
    def sub_project_name( self, value: str ):
        if value is not None:
            self.__subprojectname = value

    @property
    def program_area_code( self ) -> str:
        if self.__programareacode is not None:
            return self.__programareacode

    @program_area_code.setter
    def program_area_code( self, value: str ):
        if value is not None:
            self.__programareacode = value

    @property
    def program_area_name( self ) -> str:
        if self.__programareaname is not None:
            return self.__programareaname

    @program_area_name.setter
    def program_area_name( self, value: str ):
        if value is not None:
            self.__programareaname = value

    @property
    def reprogramming_restriction( self ) -> str:
        if self.__reprogrammingrestriction is not None:
            return self.__reprogrammingrestriction

    @reprogramming_restriction.setter
    def reprogramming_restriction( self, value: str ):
        if value is not None:
            self.__reprogrammingrestriction = value

    @property
    def increase_restriction( self ) -> str:
        if self.__increaserestriction is not None:
            return self.__increaserestriction

    @increase_restriction.setter
    def increase_restriction( self, value: str ):
        if value is not None:
            self.__increaserestriction = value

    @property
    def decrease_restriction( self ) -> str:
        if self.__decreaserestriction is not None:
            return self.__decreaserestriction

    @decrease_restriction.setter
    def decrease_restriction( self, value: str ):
        if value is not None:
            self.__decreaserestriction = value

    @property
    def memorandum_required( self ) -> str:
        if self.__memorandumrequired is not None:
            return self.__memorandumrequired

    @memorandum_required.setter
    def memorandum_required( self, value: str ):
        if value is not None:
            self.__memorandumrequired = value

    @property
    def fields( self ) -> list[ str ]:
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value: list[ str ] ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy: str = None, fundcode: str = None,
                  provider: Provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.CongressionalControls
        self.__bfy = bfy
        self.__fundcode = fundcode
        self.__fields = [ 'CongressionalControlsId',
                           'FundCode',
                           'FundName',
                           'ProgramAreaCode',
                           'ProgramAreaName',
                           'ProgramProjectCode',
                           'ProgramProjectName',
                           'SubProjectCode',
                           'SubProjectName',
                           'ReprogrammingRestriction',
                           'IncreaseRestriction',
                           'DecreaseRestriction',
                           'MemoRequirement' ]

    def get_data( self  ) -> list[ Row ]:
        try:
            _source = self.__source
            _provider = self.__provider
            _names = [ 'BFY', 'FundCode' ]
            _values = (self.__bfy, self.__fundcode)
            _dbconfig = DbConfig( _source, _provider )
            _sqlconfig = SqlConfig( names = _names, values = _values )
            _connection = Connection( self.__source )
            _sql = SqlStatement( _dbconfig, _sqlconfig )
            _sqlite = _connection.connect( )
            _cursor = _sqlite.cursor( )
            _query = _sql.get_query( )
            _db = _cursor.execute( _query )
            self.__data =  [ i for i in _db.fetchall( ) ]
            _cursor.close( )
            _sqlite.close( )
            return self.__data
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Ninja'
            _exc.cause = 'CongressionalControl'
            _exc.method = 'get_data( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class CompassLevel( ):
    '''
    Constructor: CompassLevel( bfy: str, efy: str,
                  fund: str, pvdr: Provider = Provider.SQLite )

    Purpose: Class defines object representing Compass data levels 1-7
    '''
    __source = None
    __provider = None
    __compasslevelsid = None
    __bfy = None
    __efy = None
    __fundcode = None
    __fundname = None
    __appropriationcode = None
    __subappropriationcode = None
    __appropriationname = None
    __treasurysymbol = None
    __documenttype = None
    __lowername = None
    __description = None
    __postedcontrolflag = None
    __actualrecoverytranstype = None
    __commitmentspendingcontrolflag = None
    __budgetdefault = None
    __lowerchildexpenditurecontrolflag = None
    __lowerchildexpensespendingcontrolflag = None
    __ftecontrolflag = None
    __accrualspendigcontrolflag = None
    __obligationspendingcontrolflag = None
    __precommitmentspendingcontrolflag = None
    __lowercommitmentspendingcontrolflag = None
    __lowerobligationspendingcontrolflag = None
    __lowerexpenditurespendingcontrolflag = None
    __lowerexpensespendingcontrolflag = None
    __lowerpostedcontrolflag = None
    __lowerpostedtranstype = None
    __lowerpostedflag = None
    __lowerprecommitmentspendingcontrolflag = None
    __lowerrecoveriesspendingoption = None
    __lowerrecoveriesoption = None
    __lowerreimbursablespendingoption = None
    __date = None
    __totalauthority = None
    __originalauthority = None
    __carryoveravailabilitypercentage = None
    __carryoverin = None
    __carryoverout = None
    __fundsin = None
    __fundsout = None
    __recoverieswithdrawn = None
    __actualrecoveries = None
    __actualreimbursements = None
    __agreementreimbursables = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ) -> int:
        if self.__compasslevelsid is not None:
            return self.__compasslevelsid

    @id.setter
    def id( self, value: int ):
        if value is not None:
            self.__compasslevelsid = value

    @property
    def bfy( self ) -> str:
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value: str ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ) -> str:
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value: str ):
        if value is not None:
            self.__efy = value

    @property
    def fund_code( self ) -> str:
        if self.__fundcode is not None:
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value: str ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund_name( self ) -> str:
        if self.__fundname is not None:
            return self.__fundname

    @fund_name.setter
    def fund_name( self, value: str ):
        if value is not None:
            self.__fundname = value

    @property
    def appropriation_code( self ) -> str:
        if self.__appropriationcode is not None:
            return self.__appropriationcode

    @appropriation_code.setter
    def appropriation_code( self, value: str ):
        if value is not None:
            self.__appropriationcode = value

    @property
    def appropriation_name( self ) -> str:
        if self.__appropriationname is not None:
            return self.__appropriationname

    @appropriation_name.setter
    def appropriation_name( self, value: str ):
        if value is not None:
            self.__appropriationname = value

    @property
    def sub_appropriation_code( self ) -> str:
        if self.__subappropriationcode is not None:
            return self.__subappropriationcode

    @sub_appropriation_code.setter
    def sub_appropriation_code( self, value: str ):
        if value is not None:
            self.__subappropriationcode = value

    @property
    def fields( self ) -> list[ str ]:
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value: list[ str ] ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy: str, efy: str,
                  fund: str, provider: Provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.CompassLevels
        self.__bfy = bfy
        self.__efy = efy
        self.__fundcode = fund
        self.__fields = [ 'CompassLevelsId',
                           'BudgetLevel',
                           'BFY',
                           'EFY',
                           'FundCode',
                           'FundName',
                           'AppropriationCode',
                           'SubAppropriationCode',
                           'AppropriationName'
                           'TreasurySymbol',
                           'DocumentType',
                           'LowerName',
                           'Description',
                           'PostedControlFlag',
                           'ActualRecoveryTransType',
                           'CommitmentSpendingControlFlag',
                           'BudgetDefault'
                           'LowerChildExpenditureSpendingControlFlag',
                           'LowerChildExpenseSpendingControlFlag',
                           'FteControlFlag',
                           'AccrualSpendingControlFlag',
                           'ObligationSpendingControlFlag',
                           'PreCommitmentSpendingControlFlag',
                           'LowerCommitmentSpendingControlFlag',
                           'LowerObligationSpendingControlFlag',
                           'LowerExpenditureSpendingControlFlag',
                           'LowerExpenseSpendingControlFlag',
                           'LowerPostedControlFlag',
                           'LowerPostedTransType',
                           'LowerTransType',
                           'LowerPostedFlag',
                           'LowerPreCommitmentSpendingControlFlag',
                           'LowerRecoveriesSpendingOption',
                           'LowerRecoveriesOption',
                           'LowerReimbursableSpendingOption',
                           'Date',
                           'TotalAuthority',
                           'OriginalAmount',
                           'CarryoverAvailabilityPercentage',
                           'CarryIn',
                           'CarryOut',
                           'FundsIn',
                           'FundOut',
                           'RecoveriesWithdrawn',
                           'ActualRecoveries',
                           'ActualReimbursements',
                           'AgreementReimbursables' ]

    def get_data( self  ) -> list[ Row ]:
        try:
            _source = self.__source
            _provider = self.__provider
            _names = [ 'BFY', 'EFY', 'FundCode' ]
            _values = (self.__bfy, self.__efy, self.__fundcode)
            _dbconfig = DbConfig( _source, _provider )
            _sqlconfig = SqlConfig( names = _names, values = _values )
            _connection = Connection( self.__source )
            _sql = SqlStatement( _dbconfig, _sqlconfig )
            _sqlite = _connection.connect( )
            _cursor = _sqlite.cursor( )
            _query = _sql.get_query( )
            _db = _cursor.execute( _query )
            self.__data =  [ i for i in _db.fetchall( ) ]
            _cursor.close( )
            _sqlite.close( )
            return self.__data
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Ninja'
            _exc.cause = 'CompassLevel'
            _exc.method = 'get_data( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def get_frame( self ) -> DataFrame:
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            _source = self.__source
            _data = BudgetData( _source )
            return _data.create_frame( )
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Ninja'
            _exc.cause = 'CompassLevel'
            _exc.method = 'create_frame( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class Commitment( ):
    '''
    Constructor: Commitment( bfy: str = None, fund: str = None,
                  account: str = None, boc: str = None, pvdr: Provider = Provider.SQLite )

    Purpose: Defines the CommitmentS class.
    '''
    __source = None
    __provider = None
    __opencommitmentsid = None
    __obligationsid = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __rpioname = None
    __fundcode = None
    __fundname = None
    __ahcode = None
    __ahname = None
    __orgcode = None
    __orgname = None
    __accountcode = None
    __programprojectname = None
    __boccode = None
    __bocname = None
    __rccode = None
    __rcname = None
    __documenttype = None
    __documentnumber = None
    __documentcontrolnumber = None
    __referencedocumentnumber = None
    __programprojectcode = None
    __programareacode = None
    __programareaname = None
    __processeddate = None
    __lastactivitydate = None
    __age = None
    __vendorcode = None
    __vendorage = None
    __foccode = None
    __focname = None
    __amount = None
    __goalcode = None
    __goalname = None
    __objectivecode = None
    __objectivename = None
    __npmcode = None
    __npmname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ) -> int:
        if isinstance( self.__expendituresid, int ):
            return self.__expendituresid

    @id.setter
    def id( self, value: int ):
        if value is not None:
            self.__expendituresid = value

    @property
    def bfy( self ) -> str:
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value: str ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ) -> str:
        if isinstance( self.__efy, str ) and self.__efy != '':
            return self.__efy

    @efy.setter
    def efy( self, value: str ):
        if value is not None:
            self.__efy = value

    @property
    def rpio_code( self ) -> str:
        if self.__rpiocode is not None:
            return self.__rpiocode

    @rpio_code.setter
    def rpio_code( self, value: str ):
        if value is not None:
            self.__rpiocode = value

    @property
    def rpio_name( self ) -> str:
        if self.__rpioname is not None:
            return self.__rpioname

    @rpio_code.setter
    def rpio_code( self, value: str ):
        if value is not None:
            self.__rpiocode = value

    @property
    def ah_code( self ) -> str:
        if self.__ahcode is not None:
            return self.__ahcode

    @ah_code.setter
    def ah_code( self, value: str ):
        if value is not None:
            self.__ahcode = value

    @property
    def ah_name( self ) -> str:
        if self.__ahname is not None:
            return self.__ahname

    @ah_name.setter
    def ah_name( self, value: str ):
        if value is not None:
            self.__ahname = value

    @property
    def fund_code( self ) -> str:
        if self.__fundcode is not None:
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value: str ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund_name( self ) -> str:
        if self.__fundname is not None:
            return self.__fundname

    @fund_name.setter
    def fund_name( self, value: str ):
        if value is not None:
            self.__fundname = value

    @property
    def org_code( self ) -> str:
        if self.__orgcode is not None:
            return self.__orgcode

    @org_code.setter
    def org_code( self, value: str ):
        if value is not None:
            self.__orgcode = value

    @property
    def org_name( self  ):
        if self.__orgname is not None:
            return self.__orgname

    @org_name.setter
    def org_name( self, value  ):
        if value is not None:
            self.__orgname = value

    @property
    def account_code( self ) -> str:
        if self.__accountcode is not None:
            return self.__accountcode

    @account_code.setter
    def account_code( self, value: str ):
        if value is not None:
            self.__accountcode = value

    @property
    def boc_code( self ) -> str:
        if self.__boccode is not None:
            return self.__boccode

    @boc_code.setter
    def boc_code( self, value: str ):
        if value is not None:
            self.__boccode = value

    @property
    def boc_name( self ) -> str:
        if self.__bocname is not None:
            return self.__bocname

    @boc_name.setter
    def boc_name( self, value: str ):
        if value is not None:
            self.__bocname = value

    @property
    def rc_code( self ) -> str:
        if self.__rccode is not None:
            return self.__rccode

    @rc_code.setter
    def rc_code( self, value: str ):
        if value is not None:
            self.__rccode = value

    @property
    def rc_name( self ) -> str:
        if self.__rcname is not None:
            return self.__rcname

    @rc_name.setter
    def rc_name( self, value: str ):
        if value is not None:
            self.__rcname = value

    @property
    def document_type( self ) -> str:
        if self.__documenttype is not None:
            return self.__documenttype

    @document_type.setter
    def document_type( self, value: str ):
        if value is not None:
            self.__documenttype = value

    @property
    def document_number( self ) -> str:
        if self.__documentnumber is not None:
            return self.__documentnumber

    @document_number.setter
    def document_number( self, value: str ):
        if value is not None:
            self.__documentnumber = value

    @property
    def document_control_number( self ) -> str:
        if self.__documentcontrolnumber is not None:
            return self.__documentcontrolnumber

    @document_control_number.setter
    def document_control_number( self, value: str ):
        if value is not None:
            self.__documentcontrolnumber = value

    @property
    def reference_document_number( self ) -> str:
        if self.__referencedocumentnumber is not None:
            return self.__referencedocumentnumber

    @reference_document_number.setter
    def reference_document_number( self, value: str ):
        if value is not None:
            self.__referencedocumentnumber = value

    @property
    def processed_date( self ) -> datetime:
        if self.__processeddate is not None:
            return self.__processeddate

    @processed_date.setter
    def processed_date( self, value: datetime ):
        if isinstance( value, datetime ):
            self.__processeddate = value

    @property
    def last_activity_date( self ) -> datetime:
        if self.__lastactivitydate is not None:
            return self.__lastactivitydate

    @last_activity_date.setter
    def last_activity_date( self, value: datetime ):
        if isinstance( value, datetime ):
            self.__lastactivitydate = value

    @property
    def age( self ) -> float:
        if self.__age is not None:
            return self.__age

    @age.setter
    def age( self, value: float ):
        if value is not None:
            self.__age = value

    @property
    def vendor_code( self ) -> str:
        if self.__vendorcode is not None:
            return self.__vendorcode

    @vendor_code.setter
    def vendor_code( self, value: str ):
        if value is not None:
            self.__vendorcode = value

    @property
    def vendor_name( self ) -> str:
        if self.__vendorname is not None:
            return self.__vendorname

    @vendor_name.setter
    def vendor_name( self, value: str ):
        if value is not None:
            self.__vendorname = value

    @property
    def foc_code( self ) -> str:
        if self.__foccode is not None:
            return self.__foccode

    @foc_code.setter
    def foc_code( self, value: str ):
        if value is not None:
            self.__foccode = value

    @property
    def foc_name( self ) -> str:
        if self.__focname is not None:
            return self.__focname

    @foc_name.setter
    def foc_name( self, value: str ):
        if value is not None:
            self.__focname = value

    @property
    def amount( self ) -> float:
        if self.__amount is not None:
            return self.__amount

    @amount.setter
    def amount( self, value: float ):
        if value is not None:
            self.__amount = value

    @property
    def program_project_code( self ) -> str:
        if self.__programprojectcode is not None:
            return self.__programprojectcode

    @program_project_code.setter
    def program_project_code( self, value: str ):
        if value is not None:
            self.__programprojectcode = value

    @property
    def program_project_name( self ) -> str:
        if  self.__programprojectname is not None:
            return self.__programprojectname

    @program_project_name.setter
    def program_project_name( self, value: str ):
        if value is not None:
            self.__programprojectname = value

    @property
    def program_area_code( self ) -> str:
        if self.__programareacode is not None:
            return self.__programareacode

    @program_area_code.setter
    def program_area_code( self, value: str ):
        if value is not None:
            self.__programareacode = value

    @property
    def program_area_name( self ) -> str:
        if self.__programareaname is not None:
            return self.__programareaname

    @program_area_name.setter
    def program_area_name( self, value: str ):
        if value is not None:
            self.__programareaname = value

    @property
    def goal_code( self ) -> str:
        if  self.__goalcode is not None:
            return self.__goalcode

    @goal_code.setter
    def goal_code( self, value: str ):
        if value is not None:
            self.__goalcode = value

    @property
    def goal_name( self ) -> str:
        if self.__goalname is not None:
            return self.__goalname

    @goal_name.setter
    def goal_name( self, value: str ):
        if value is not None:
            self.__goalname = value

    @property
    def objective_code( self ) -> str:
        if self.__objectivecode is not None:
            return self.__objectivecode

    @objective_code.setter
    def objective_code( self, value: str ):
        if value is not None:
            self.__objectivecode = value

    @property
    def objective_name( self ) -> str:
        if self.__objectivename is not None:
            return self.__objectivename

    @objective_name.setter
    def objective_name( self, value: str ):
        if value is not None:
            self.__objectivename = value

    @property
    def npm_code( self ) -> str:
        if self.__npmcode is not None:
            return self.__npmcode

    @npm_code.setter
    def npm_code( self, value: str ):
        if value is not None:
            self.__npmcode = value

    @property
    def npm_name( self ) -> str:
        if self.__npmname is not None:
            return self.__npmname

    @npm_name.setter
    def npm_name( self, value: str ):
        if value is not None:
            self.__npmname = value

    @property
    def fields( self ) -> list[ str ]:
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value: list[ str ] ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy: str = None, fund: str = None,
                  account: str = None, boc: str = None, provider: Provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.OpenCommitments
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__fundcode = fund if isinstance( fund, str ) and fund != '' else None
        self.__accountcode = account if isinstance( account, str ) and account != '' else None
        self.__boccode = boc if isinstance( boc, str ) and boc != '' else None
        self.__fields = [ 'CommitmentsId',
                           'ObligationsId',
                           'BFY',
                           'EFY',
                           'RpioCode',
                           'RpioName',
                           'AhCode',
                           'AhName',
                           'FundCode',
                           'FundName',
                           'OrgCode',
                           'OrgName',
                           'AccountCode',
                           'ProgramProjectCode',
                           'ProgramProjectName',
                           'RcCode',
                           'RcName',
                           'DocumentType',
                           'DocumentNumber',
                           'DocumentControlNumber',
                           'ReferenceDocumentNumber',
                           'ProcessedDate',
                           'LastActivityDate',
                           'Age',
                           'BocCode',
                           'BocName',
                           'FocCode',
                           'FocName',
                           'NpmCode',
                           'NpmName',
                           'VendorCode',
                           'VendorName',
                           'OpenCommitment',
                           'Obligation',
                           'ULO',
                           'Expenditure' ]

    def __str__( self ) -> str:
        if isinstance( self.__amount, float ):
            return str( self.__amount )

    def get_data( self  ) -> list[ Row ]:
        try:
            _source = self.__source
            _provider = self.__provider
            _names = [ 'BFY', 'FundCode', 'AccountCode', 'BocCode' ]
            _values = (self.__bfy, self.__fundcode, self.__accountcode, self.__boccode)
            _dbconfig = DbConfig( _source, _provider )
            _sqlconfig = SqlConfig( names = _names, values = _values )
            _connection = Connection( self.__source )
            _sql = SqlStatement( _dbconfig, _sqlconfig )
            _sqlite = _connection.connect( )
            _cursor = _sqlite.cursor( )
            _query = _sql.get_query( )
            _db = _cursor.execute( _query )
            self.__data =  [ i for i in _db.fetchall( ) ]
            _cursor.close( )
            _sqlite.close( )
            return self.__data
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Ninja'
            _exc.cause = 'Commitment'
            _exc.method = 'get_data( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def get_frame( self ) -> DataFrame:
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            _source = self.__source
            _data = BudgetData( _source )
            return _data.create_frame( )
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Ninja'
            _exc.cause = 'Commitment'
            _exc.method = 'create_frame( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class CostArea( ):
    '''
    Constructor: CostArea( fund, pvdr = Provider.SQLite )

    Purpose: Data class object for cost areas
    '''
    __source = None
    __provider = None
    __code = None
    __fields = None

    @property
    def id( self ) -> int:
        if isinstance( self.__transfersid, int ):
            return self.__transfersid

    @id.setter
    def id( self, value: int ):
        if value is not None:
            self.__transfersid = value

    @property
    def fields( self ) -> list[ str ]:
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value: list[ str ] ):
        if value is not None:
            self.__fields = value

    def __init__( self, code: str, provider: Provider = Provider.SQLite ):
        self.__code = code
        self.__provider = provider
        self.__fields = [ 'CostAreasId',
                          'Code',
                          'Name' ]

class CapitalPlanningInvestmentCodes( ):
    '''
    Constructor:  CapitalPlanningInvestmentCodes( treas, pvdr = Provider.SQLite  )

    Purpose:  Class eefines the CPIC Codes'''
    __source = None
    __provider = None
    __capitalplanninginvestmentcodesid = None
    __code = None
    __name = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ) -> int:
        if isinstance( self.__capitalplanninginvestmentcodesid, int ):
            return self.__capitalplanninginvestmentcodesid

    @id.setter
    def id( self, value: int ):
        if value is not None:
            self.__accountsid = value

    @property
    def code( self ) -> str:
        if  self.__code is not None:
            return self.__code

    @code.setter
    def code( self, value: str ):
        if value is not None:
            self.__code = value

    @property
    def name( self ) -> str:
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, value: str ):
        if value is not None:
            self.__name = value

    @property
    def data( self ) -> list:
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, value: list ):
        if isinstance( value, list ):
            self.__data = value

    @property
    def table( self ) -> DataFrame:
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, value: DataFrame ):
        if value is not None:
            self.__frame = value

    @property
    def fields( self ) -> list[ str ]:
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value: list[ str ] ):
        if value is not None:
            self.__fields = value

    def __init__( self, code, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.CapitalPlanningInvestmentCodes
        self.__code = code
        self.__fields = [ 'CpicId',
                          'Type'
                          'Code',
                          'Name' ]

    def __str__( self ) -> str:
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code

    def get_data( self  ) -> list[ Row ]:
        try:
            _source = self.__source
            _provider = self.__provider
            _names = [ 'Code', ]
            _values = ( self.__code, )
            _dbconfig = DbConfig( _source, _provider )
            _sqlconfig = SqlConfig( names = _names, values = _values )
            _connection = Connection( self.__source )
            _sql = SqlStatement( _dbconfig, _sqlconfig )
            _sqlite = _connection.connect( )
            _cursor = _sqlite.cursor( )
            _query = _sql.get_query( )
            _db = _cursor.execute( _query )
            self.__data =  [ i for i in _db.fetchall( ) ]
            _cursor.close( )
            _sqlite.close( )
            return self.__data
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Execution'
            _exc.cause = 'ITProjectCode'
            _exc.method = 'get_data( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def get_frame( self ) -> DataFrame:
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            _source = self.__source
            _data = BudgetData( _source )
            return _data.create_frame( )
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Execution'
            _exc.cause = 'ITProjectCode'
            _exc.method = 'create_frame( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class ColumnSchema( ):
    '''
    Constructor: ColumnSchema( column, table_name, pvdr = Provider.SQLite )

    Purpose:  Provides data on the coolumn_names used in the application'''
    __source = None
    __provider = None
    __columnschemaid = None
    __datatype = None
    __columnname = None
    __tablename = None
    __columncaption = None
    __fields = None
    __data = None
    __frame = None


    @property
    def id( self ) -> int:
        if self.__columnschemaid is not None:
            return self.__columnschemaid

    @id.setter
    def id( self, value: int ):
        if value is not None:
            self.__columnschemaid = value

    @property
    def data_type( self ) -> str:
        if self.__datatype is not None:
            return self.__datatype

    @data_type.setter
    def data_type( self, value: str ):
        if value is not None:
            self.__datatype = value

    @property
    def column_name( self ) -> str:
        if self.__columnname is not None:
            return self.__columnname

    @column_name.setter
    def column_name( self, value: str ):
        if value is not None:
            self.__columnname = value

    @property
    def table_name( self ) -> str:
        if self.__tablename is not None:
            return self.__tablename

    @table_name.setter
    def table_name( self, value: str ):
        if value is not None:
            self.__tablename = value

    @property
    def column_caption( self ) -> str:
        if self.__columncaption is not None:
            return self.__columncaption

    @column_caption.setter
    def column_caption( self, value: str ):
        if value is not None:
            self.__columncaption = value

    def __init__( self, column, table, provider = Provider.SQLite ):
        self.__source = Source.ColumnSchema
        self.__provider = provider
        self.__columnname = column
        self.__tablename = table

class DataRuleDescription( ):
    '''
    Constructor:DataRuleDescription( schedule, line, rule, pvdr = Provider.SQLite )

    Purpose: Class defines object providing OMB MAX A11 rule data '''
    __source = None
    __provider = None
    __dataruledescriptionsid = None
    __schedule = None
    __linenumber = None
    __rulenumber = None
    __ruledescription = None
    __scheduleorder = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ) -> int:
        if isinstance( self.__dataruledescriptionsid, int ):
            return self.__dataruledescriptionsid

    @id.setter
    def id( self, value: int ):
        if value is not None:
            self.__dataruledescriptionsid = value

    @property
    def schedule( self ) -> str:
        if isinstance( self.__schedule, str ) and self.__schedule != '':
            return self.__schedule

    @schedule.setter
    def schedule( self, value: str ):
        if value is not None:
            self.__schedule = value

    @property
    def line_number( self ) -> str:
        if isinstance( self.__linenumber, str ) and self.__linenumber != '':
            return self.__linenumber

    @line_number.setter
    def line_number( self, value: str ):
        if value is not None:
            self.__linenumber = value

    @property
    def line_description( self ) -> str:
        if isinstance( self.__linedescription, str ) and self.__linedescription != '':
            return self.__linedescription

    @line_description.setter
    def line_description( self, value: str ):
        if value is not None:
            self.__linedescription = value

    @property
    def rule_number( self ) -> str:
        if isinstance( self.__rulenumber, str ) and self.__rulenumber != '':
            return self.__rulenumber

    @rule_number.setter
    def rule_number( self, value: str ):
        if value is not None:
            self.__rulenumber = value

    @property
    def rule_description( self ) -> str:
        if isinstance( self.__ruledescription, str ) and self.__ruledescription != '':
            return self.__ruledescription

    @rule_description.setter
    def rule_description( self, value: str ):
        if value is not None:
            self.__ruledescription = value

    @property
    def fields( self ) -> list[ str ]:
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value: list[ str ] ):
        if value is not None:
            self.__fields = value

    def __init__( self, schedule, line, rule, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.DataRuleDescriptions
        self.__schedule = schedule
        self.__linenumber = line
        self.__rulenumber = rule
        self.__fields = [ 'DataRuleDescriptionsId',
                          'Schedule',
                          'LineNumber',
                          'RuleNumber',
                          'RuleDescription',
                          'ScheduleOrder' ]

    def get_data( self  ) -> list[ Row ]:
        try:
            _source = self.__source
            _provider = self.__provider
            _names = [ 'Schedule', 'LineNumber', 'RuleNumber' ]
            _values = (self.__schedule, self.__linenumber, self.__rulenumber)
            _dbconfig = DbConfig( _source, _provider )
            _sqlconfig = SqlConfig( names = _names, values = _values )
            _connection = Connection( self.__source )
            _sql = SqlStatement( _dbconfig, _sqlconfig )
            _sqlite = _connection.connect( )
            _cursor = _sqlite.cursor( )
            _query = _sql.get_query( )
            _db = _cursor.execute( _query )
            self.__data =  [ i for i in _db.fetchall( ) ]
            _cursor.close( )
            _sqlite.close( )
            return self.__data
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Reporting'
            _exc.cause = 'DataRuleDescription'
            _exc.method = 'get_data( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def get_frame( self ) -> DataFrame:
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            _source = self.__source
            _data = BudgetData( _source )
            return _data.create_frame( )
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Reporting'
            _exc.cause = 'DataRuleDescription'
            _exc.method = 'create_frame( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class Defacto( ):
    '''
    Constructor:  Defacto(  bfy: str, fund: str, pvdr: Provider = Provider.SQLite )

    Purpose:  Class defines object representing defacto obligations
    '''
    __source = None
    __provider = None
    __defactosid = None
    __statusoffundsid = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __rpioname = None
    __fundcode = None
    __fundname = None
    __ahcode = None
    __ahname = None
    __orgcode = None
    __orgname = None
    __accountcode = None
    __boccode = None
    __bocname = None
    __rccode = None
    __rcname = None
    __amount = None
    __budgeted = None
    __posted = None
    __opencommitments = None
    __obligations = None
    __unliquidatedobligations = None
    __expenditures = None
    __used = None
    __avaialable = None
    __programprojectcode = None
    __programprojectname = None
    __programareacode = None
    __programareaname = None
    __goalcode = None
    __goalname = None
    __objectivecode = None
    __objectivename = None
    __npmcode = None
    __npmname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ) -> int:
        if isinstance( self.__statusoffundsid, int ):
            return self.__statusoffundsid

    @id.setter
    def id( self, value: int ):
        if isinstance( value, int ) and value > -1:
            self.__statusoffundsid = value

    @property
    def bfy( self ) -> str:
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value: str ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ) -> str:
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value: str ):
        if value is not None:
            self.__efy = value

    @property
    def rpio_code( self ) -> str:
        if self.__rpiocode is not None:
            return self.__rpiocode

    @rpio_code.setter
    def rpio_code( self, value: str ):
        if value is not None:
            self.__rpiocode = value

    @property
    def rpio_name( self ) -> str:
        if self.__rpioname is not None:
            return self.__rpioname

    @rpio_code.setter
    def rpio_code( self, value: str ):
        if value is not None:
            self.__rpiocode = value

    @property
    def ah_code( self ) -> str:
        if self.__ahcode is not None:
            return self.__ahcode

    @ah_code.setter
    def ah_code( self, value: str ):
        if value is not None:
            self.__ahcode = value

    @property
    def ah_name( self ) -> str:
        if self.__ahname is not None:
            return self.__ahname

    @ah_name.setter
    def ah_name( self, value: str ):
        if value is not None:
            self.__ahname = value

    @property
    def fund_code( self ) -> str:
        if self.__fundcode is not None:
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value: str ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund_name( self ) -> str:
        if self.__fundname is not None:
            return self.__fundname

    @fund_name.setter
    def fund_name( self, value: str ):
        if value is not None:
            self.__fundname = value

    @property
    def org_code( self ) -> str:
        if self.__orgcode is not None:
            return self.__orgcode

    @org_code.setter
    def org_code( self, value: str ):
        if value is not None:
            self.__orgcode = value

    @property
    def org_name( self  ):
        if self.__orgname is not None:
            return self.__orgname

    @org_name.setter
    def org_name( self, value  ):
        if value is not None:
            self.__orgname = value

    @property
    def account_code( self ) -> str:
        if self.__accountcode is not None:
            return self.__accountcode

    @account_code.setter
    def account_code( self, value: str ):
        if value is not None:
            self.__accountcode = value

    @property
    def boc_code( self ) -> str:
        if self.__boccode is not None:
            return self.__boccode

    @boc_code.setter
    def boc_code( self, value: str ):
        if value is not None:
            self.__boccode = value

    @property
    def boc_name( self ) -> str:
        if self.__bocname is not None:
            return self.__bocname

    @boc_name.setter
    def boc_name( self, value: str ):
        if value is not None:
            self.__bocname = value

    @property
    def rc_code( self ) -> str:
        if self.__rccode is not None:
            return self.__rccode

    @rc_code.setter
    def rc_code( self, value: str ):
        if value is not None:
            self.__rccode = value

    @property
    def rc_name( self ) -> str:
        if self.__rcname is not None:
            return self.__rcname

    @rc_name.setter
    def rc_name( self, value: str ):
        if value is not None:
            self.__rcname = value

    @property
    def amount( self ) -> float:
        if self.__amount is not None:
            return self.__amount

    @amount.setter
    def amount( self, value: float ):
        if value is not None:
            self.__amount = value

    @property
    def budgeted( self ) -> float:
        if self.__budgeted is not None:
            return self.__budgeted

    @budgeted.setter
    def budgeted( self, value: float ):
        if value is not None:
            self.__budgeted = value

    @property
    def posted( self ) -> float:
        if self.__posted is not None:
            return self.__posted

    @posted.setter
    def posted( self, value: float ):
        if value is not None:
            self.__posted = value

    @property
    def open_commitments( self ) -> float:
        if self.__opencommitments is not None:
            return self.__opencommitments

    @open_commitments.setter
    def open_commitments( self, value: float ):
        if value is not None:
            self.__opencommitments = value

    @property
    def obligations( self ) -> float:
        if self.__obligations is not None:
            return self.__obligations

    @obligations.setter
    def obligations( self, value: float ):
        if value is not None:
            self.__obligations = value

    @property
    def unliquidated_obligations( self ) -> float:
        if self.__unliquidatedobligations is not None:
            return self.__unliquidatedobligations

    @unliquidated_obligations.setter
    def unliquidated_obligations( self, value: float ):
        if value is not None:
            self.__unliquidatedobligations = value

    @property
    def expenditures( self ) -> float:
        if self.__expenditures is not None:
            return self.__expenditures

    @expenditures.setter
    def expenditures( self, value: float ):
        if value is not None:
            self.__expenditures = value

    @property
    def used( self ) -> float:
        if self.__used is not None:
            return self.__used

    @used.setter
    def used( self, value: float ):
        if value is not None:
            self.__used = value

    @property
    def available( self ) -> float:
        if self.__avaialable is not None:
            return self.__avaialable

    @available.setter
    def available( self, value: float ):
        if value is not None:
            self.__avaialable = value

    @property
    def program_project_code( self ) -> str:
        if self.__programprojectcode is not None:
            return self.__programprojectcode

    @program_project_code.setter
    def program_project_code( self, value: str ):
        if value is not None:
            self.__programprojectcode = value

    @property
    def program_project_name( self ) -> str:
        if self.__programprojectname is not None:
            return self.__programprojectname

    @program_project_name.setter
    def program_project_name( self, value: str ):
        if value is not None:
            self.__programprojectname = value

    @property
    def program_area_code( self ) -> str:
        if self.__programareacode is not None:
            return self.__programareacode

    @program_area_code.setter
    def program_area_code( self, value: str ):
        if value is not None:
            self.__programareacode = value

    @property
    def program_area_name( self ) -> str:
        if self.__programareaname is not None:
            return self.__programareaname

    @program_area_name.setter
    def program_area_name( self, value: str ):
        if value is not None:
            self.__programareaname = value

    @property
    def goal_code( self ) -> str:
        if self.__goalcode is not None:
            return self.__goalcode

    @goal_code.setter
    def goal_code( self, value: str ):
        if value is not None:
            self.__goalcode = value

    @property
    def goal_name( self ) -> str:
        if self.__goalname is not None:
            return self.__goalname

    @goal_name.setter
    def goal_name( self, value: str ):
        if value is not None:
            self.__goalname = value

    @property
    def objective_code( self ) -> str:
        if self.__objectivecode is not None:
            return self.__objectivecode

    @objective_code.setter
    def objective_code( self, value: str ):
        if value is not None:
            self.__objectivecode = value

    @property
    def objective_name( self ) -> str:
        if self.__objectivename is not None:
            return self.__objectivename

    @objective_name.setter
    def objective_name( self, value: str ):
        if value is not None:
            self.__objectivename = value

    @property
    def npm_code( self ) -> str:
        if self.__npmcode is not None:
            return self.__npmcode

    @npm_code.setter
    def npm_code( self, value: str ):
        if value is not None:
            self.__npmcode = value

    @property
    def npm_name( self ) -> str:
        if self.__npmname is not None:
            return self.__npmname

    @npm_name.setter
    def npm_name( self, value: str ):
        if value is not None:
            self.__npmname = value

    @property
    def fields( self ) -> list[ str ]:
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value: list[ str ] ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy: str, fund: str, provider: Provider = Provider.SQLite ):
        self.__source = Source.Defactos
        self.__provider = provider
        self.__bfy = bfy
        self.__fundcode = fund
        self.__fields = [ 'DefactosId',
                           'StatusOfFundsId',
                           'BudgetLevel',
                           'BFY',
                           'EFY',
                           'RpioCode',
                           'RpioName',
                           'AhCode',
                           'AhName',
                           'FundCode',
                           'FundName',
                           'OrgCode',
                           'OrgName',
                           'AccountCode',
                           'BocCode',
                           'BocName',
                           'ProgramProjectCode',
                           'ProgramProjectName',
                           'ProgramAreaCode',
                           'ProgramAreaName',
                           'RcCode',
                           'RcName',
                           'LowerName',
                           'Amount',
                           'Budgeted',
                           'Posted',
                           'OpenCommitment',
                           'ULO',
                           'Expenditure',
                           'Obligation',
                           'Used',
                           'Available',
                           'NpmCode',
                           'NpmName' ]

    def get_data( self  ) -> list[ Row ]:
        try:
            _source = self.__source
            _provider = self.__provider
            _names = [ 'BFY', 'FundCode' ]
            _values = (self.__bfy, self.__fundcode)
            _dbconfig = DbConfig( _source, _provider )
            _sqlconfig = SqlConfig( names = _names, values = _values )
            _connection = Connection( self.__source )
            _sql = SqlStatement( _dbconfig, _sqlconfig )
            _sqlite = _connection.connect( )
            _cursor = _sqlite.cursor( )
            _query = _sql.get_query( )
            _db = _cursor.execute( _query )
            self.__data =  [ i for i in _db.fetchall( ) ]
            _cursor.close( )
            _sqlite.close( )
            return self.__data
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Ninja'
            _exc.cause = 'Defacto'
            _exc.method = 'get_data( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def get_frame( self ) -> DataFrame:
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            _source = self.__source
            _data = BudgetData( _source )
            return _data.create_frame( )
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Ninja'
            _exc.cause = 'Defacto'
            _exc.method = 'create_frame( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class Deobligation( ):
    '''
    Constructor: Deobligation( bfy, fund, account, boc, pvdr = Provider.SQLite )

    Purpose:  Class defines object providing Deobligation data '''
    __source = None
    __provider = None
    __deobligationsid = None
    __obligationsid = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __rpioname = None
    __fundcode = None
    __fundname = None
    __ahcode = None
    __ahname = None
    __orgcode = None
    __orgname = None
    __accountcode = None
    __programprojectname = None
    __boccode = None
    __bocname = None
    __rccode = None
    __rcname = None
    __documenttype = None
    __documentnumber = None
    __documentcontrolnumber = None
    __referencedocumentnumber = None
    __programprojectcode = None
    __programareacode = None
    __programareaname = None
    __processeddate = None
    __lastactivitydate = None
    __age = None
    __vendorcode = None
    __vendorage = None
    __foccode = None
    __focname = None
    __amount = None
    __goalcode = None
    __goalname = None
    __objectivecode = None
    __objectivename = None
    __npmcode = None
    __npmname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ) -> int:
        if isinstance( self.__deobligationsid, int ):
            return self.__deobligationsid

    @id.setter
    def id( self, value: int ):
        if value is not None:
            self.__deobligationsid = value

    @property
    def bfy( self ) -> str:
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value: str ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ) -> str:
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value: str ):
        if value is not None:
            self.__efy = value

    @property
    def rpio_code( self ) -> str:
        if self.__rpiocode is not None:
            return self.__rpiocode

    @rpio_code.setter
    def rpio_code( self, value: str ):
        if value is not None:
            self.__rpiocode = value

    @property
    def rpio_name( self ) -> str:
        if self.__rpioname is not None:
            return self.__rpioname

    @rpio_code.setter
    def rpio_code( self, value: str ):
        if value is not None:
            self.__rpiocode = value

    @property
    def ah_code( self ) -> str:
        if self.__ahcode is not None:
            return self.__ahcode

    @ah_code.setter
    def ah_code( self, value: str ):
        if value is not None:
            self.__ahcode = value

    @property
    def ah_name( self ) -> str:
        if self.__ahname is not None:
            return self.__ahname

    @ah_name.setter
    def ah_name( self, value: str ):
        if value is not None:
            self.__ahname = value

    @property
    def fund_code( self ) -> str:
        if self.__fundcode is not None:
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value: str ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund_name( self ) -> str:
        if self.__fundname is not None:
            return self.__fundname

    @fund_name.setter
    def fund_name( self, value: str ):
        if value is not None:
            self.__fundname = value

    @property
    def org_code( self ) -> str:
        if self.__orgcode is not None:
            return self.__orgcode

    @org_code.setter
    def org_code( self, value: str ):
        if value is not None:
            self.__orgcode = value

    @property
    def org_name( self  ):
        if self.__orgname is not None:
            return self.__orgname

    @org_name.setter
    def org_name( self, value  ):
        if value is not None:
            self.__orgname = value

    @property
    def account_code( self ) -> str:
        if self.__accountcode is not None:
            return self.__accountcode

    @account_code.setter
    def account_code( self, value: str ):
        if value is not None:
            self.__accountcode = value

    @property
    def boc_code( self ) -> str:
        if self.__boccode is not None:
            return self.__boccode

    @boc_code.setter
    def boc_code( self, value: str ):
        if value is not None:
            self.__boccode = value

    @property
    def boc_name( self ) -> str:
        if self.__bocname is not None:
            return self.__bocname

    @boc_name.setter
    def boc_name( self, value: str ):
        if value is not None:
            self.__bocname = value

    @property
    def rc_code( self ) -> str:
        if self.__rccode is not None:
            return self.__rccode

    @rc_code.setter
    def rc_code( self, value: str ):
        if value is not None:
            self.__rccode = value

    @property
    def rc_name( self ) -> str:
        if self.__rcname is not None:
            return self.__rcname

    @rc_name.setter
    def rc_name( self, value: str ):
        if value is not None:
            self.__rcname = value

    @property
    def document_type( self ) -> str:
        if self.__documenttype is not None:
            return self.__documenttype

    @document_type.setter
    def document_type( self, value: str ):
        if value is not None:
            self.__documenttype = value

    @property
    def document_number( self ) -> str:
        if self.__documentnumber is not None:
            return self.__documentnumber

    @document_number.setter
    def document_number( self, value: str ):
        if value is not None:
            self.__documentnumber = value

    @property
    def document_control_number( self ) -> str:
        if self.__documentcontrolnumber is not None:
            return self.__documentcontrolnumber

    @document_control_number.setter
    def document_control_number( self, value: str ):
        if value is not None:
            self.__documentcontrolnumber = value

    @property
    def reference_document_number( self ) -> str:
        if self.__referencedocumentnumber is not None:
            return self.__referencedocumentnumber

    @reference_document_number.setter
    def reference_document_number( self, value: str ):
        if value is not None:
            self.__referencedocumentnumber = value

    @property
    def processed_date( self ) -> str:
        if self.__processeddate is not None:
            return self.__processeddate

    @processed_date.setter
    def processed_date( self, value: str ):
        if value is not None:
            self.__processeddate = value

    @property
    def last_activity_date( self ) -> str:
        if self.__lastactivitydate is not None:
            return self.__lastactivitydate

    @last_activity_date.setter
    def last_activity_date( self, value: str ):
        if value is not None:
            self.__lastactivitydate = value

    @property
    def age( self ) -> str:
        if self.__age is not None:
            return self.__age

    @age.setter
    def age( self, value: str ):
        if value is not None:
            self.__age = value

    @property
    def vendor_code( self ) -> str:
        if self.__vendorcode is not None:
            return self.__vendorcode

    @vendor_code.setter
    def vendor_code( self, value: str ):
        if value is not None:
            self.__vendorcode = value

    @property
    def vendor_name( self ) -> str:
        if self.__vendorname is not None:
            return self.__vendorname

    @vendor_name.setter
    def vendor_name( self, value: str ):
        if value is not None:
            self.__vendorname = value

    @property
    def foc_code( self ) -> str:
        if self.__foccode is not None:
            return self.__foccode

    @foc_code.setter
    def foc_code( self, value: str ):
        if value is not None:
            self.__rccode = value

    @property
    def foc_name( self ) -> str:
        if self.__focname is not None:
            return self.__focname

    @foc_name.setter
    def foc_name( self, value: str ):
        if value is not None:
            self.__focname = value

    @property
    def amount( self ) -> float:
        if self.__amount is not None:
            return self.__amount

    @amount.setter
    def amount( self, value: float ):
        if value is not None:
            self.__amount = value

    @property
    def program_project_code( self ) -> str:
        if self.__programprojectcode is not None:
            return self.__programprojectcode

    @program_project_code.setter
    def program_project_code( self, value: str ):
        if value is not None:
            self.__programprojectcode = value

    @property
    def program_project_name( self ) -> str:
        if self.__programprojectname is not None:
            return self.__programprojectname

    @program_project_name.setter
    def program_project_name( self, value: str ):
        if value is not None:
            self.__programprojectname = value

    @property
    def program_area_code( self ) -> str:
        if self.__programareacode is not None:
            return self.__programareacode

    @program_area_code.setter
    def program_area_code( self, value: str ):
        if value is not None:
            self.__programareacode = value

    @property
    def program_area_name( self ) -> str:
        if self.__programareaname is not None:
            return self.__programareaname

    @program_area_name.setter
    def program_area_name( self, value: str ):
        if value is not None:
            self.__programareaname = value

    @property
    def goal_code( self ) -> str:
        if self.__goalcode is not None:
            return self.__goalcode

    @goal_code.setter
    def goal_code( self, value: str ):
        if value is not None:
            self.__goalcode = value

    @property
    def goal_name( self ) -> str:
        if self.__goalname is not None:
            return self.__goalname

    @goal_name.setter
    def goal_name( self, value: str ):
        if value is not None:
            self.__goalname = value

    @property
    def objective_code( self ) -> str:
        if self.__objectivecode is not None:
            return self.__objectivecode

    @objective_code.setter
    def objective_code( self, value: str ):
        if value is not None:
            self.__objectivecode = value

    @property
    def objective_name( self ) -> str:
        if self.__objectivename is not None:
            return self.__objectivename

    @objective_name.setter
    def objective_name( self, value: str ):
        if value is not None:
            self.__objectivename = value

    @property
    def npm_code( self ) -> str:
        if self.__npmcode is not None:
            return self.__npmcode

    @npm_code.setter
    def npm_code( self, value: str ):
        if value is not None:
            self.__npmcode = value

    @property
    def npm_name( self ) -> str:
        if self.__npmname is not None:
            return self.__npmname

    @npm_name.setter
    def npm_name( self, value: str ):
        if value is not None:
            self.__npmname = value

    @property
    def fields( self ) -> list[ str ]:
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value: list[ str ] ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy = None, fund = None,
                  account = None, boc = None, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.Deobligations
        self.__bfy = bfy
        self.__fundcode = fund
        self.__accountcode = account
        self.__boccode = boc
        self.__fields = [ 'DeobligationsId',
                           'BFY',
                           'RpioCode',
                           'RpioName',
                           'AhCode',
                           'AhName',
                           'FundCode',
                           'FundName',
                           'AccountCode',
                           'NpmCode',
                           'NpmName',
                           'ProgramProjectCode',
                           'ProgramProjectName',
                           'OrgCode',
                           'OrgName',
                           'BocCode',
                           'BocName',
                           'DocumentNumber',
                           'FocCode',
                           'FocName',
                           'ProcessedDate',
                           'Amount' ]

    def __str__( self ) -> str:
        if isinstance( self.__amount, float ):
            return str( self.__amount )

    def get_data( self  ) -> list[ Row ]:
        try:
            _source = self.__source
            _provider = self.__provider
            _names = [ 'BFY', 'FundCode', 'AccountCode', 'BocCode' ]
            _values = (self.__bfy, self.__fundcode, self.__accountcode, self.__boccode)
            _dbconfig = DbConfig( _source, _provider )
            _sqlconfig = SqlConfig( names = _names, values = _values )
            _connection = Connection( self.__source )
            _sql = SqlStatement( _dbconfig, _sqlconfig )
            _sqlite = _connection.connect( )
            _cursor = _sqlite.cursor( )
            _query = _sql.get_query( )
            _db = _cursor.execute( _query )
            self.__data =  [ i for i in _db.fetchall( ) ]
            _cursor.close( )
            _sqlite.close( )
            return self.__data
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Ninja'
            _exc.cause = 'Deobligations'
            _exc.method = 'get_data( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def get_frame( self ) -> DataFrame:
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            _source = self.__source
            _data = BudgetData( _source )
            return _data.create_frame( )
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Ninja'
            _exc.cause = 'Deobligations'
            _exc.method = 'create_frame( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class DocumentControlNumber( ):
    '''
    Constructor: DocumentControlNumber( dcn, pvdr = Provider.SQLite )

    Purpose:  Class defines object provides DCN data'''
    __source = None
    __provider = None
    __documentcontrolnumbersid = None
    __rpiocode = None
    __rpioname = None
    __documenttype = None
    __documentnumber = None
    __documentprefix = None
    __documentcontrolnumber = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ) -> int:
        if self.__documentcontrolnumbersid is not None:
            return self.__documentcontrolnumbersid

    @id.setter
    def id( self, value: int ):
        if value is not None:
            self.__documentcontrolnumbersid = value

    @property
    def rpio_code( self ) -> str:
        if self.__rpiocode is not None:
            return self.__rpiocode

    @rpio_code.setter
    def rpio_code( self, value: str ):
        if value is not None:
            self.__rpiocode = value

    @property
    def rpio_name( self ) -> str:
        if self.__rpioname is not None:
            return self.__rpioname

    @rpio_name.setter
    def rpio_name( self, value: str ):
        if value is not None:
            self.__rpioname = value

    @property
    def document_type( self ) -> str:
        if self.__documenttype is not None:
            return self.__documenttype

    @document_type.setter
    def document_type( self, value: str ):
        if value is not None:
            self.__documenttype = value

    @property
    def document_prefix( self ) -> str:
        if self.__documentprefix is not None:
            return self.__documentprefix

    @document_prefix.setter
    def document_prefix( self, value: str ):
        if value is not None:
            self.__documentprefix = value

    @property
    def document_number( self ) -> str:
        if self.__documentnumber is not None:
            return self.__documentnumber

    @document_number.setter
    def document_number( self, value: str ):
        if value is not None:
            self.__documentnumber = value

    @property
    def document_control_number( self ) -> str:
        if self.__documentcontrolnumber is not None:
            return self.__documentcontrolnumber

    @document_control_number.setter
    def document_control_number( self, value: str ):
        if value is not None:
            self.__documentcontrolnumber = value

    @property
    def fields( self ) -> list[ str ]:
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value: list[ str ] ):
        if value is not None:
            self.__fields = value

    def __init__( self, dcn, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.DocumentControlNumbers
        self.__documentcontrolnumber = dcn
        self.__fields = [ 'DocumentControlNumbersId',
                           'RpioCode',
                           'RpioName',
                           'DocumentType',
                           'DocumentNumber',
                           'DocumentPrefix',
                           'DocumentControlNumbe' ]

    def get_data( self  ) -> list[ Row ]:
        try:
            _source = self.__source
            _provider = self.__provider
            _names = [ 'DocumentControlNumber', ]
            _values = (self.__documentcontrolnumber,)
            _dbconfig = DbConfig( _source, _provider )
            _sqlconfig = SqlConfig( names = _names, values = _values )
            _connection = Connection( self.__source )
            _sql = SqlStatement( _dbconfig, _sqlconfig )
            _sqlite = _connection.connect( )
            _cursor = _sqlite.cursor( )
            _query = _sql.get_query( )
            _db = _cursor.execute( _query )
            self.__data =  [ i for i in _db.fetchall( ) ]
            _cursor.close( )
            _sqlite.close( )
            return self.__data
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Ninja'
            _exc.cause = 'DocumentControlNumber'
            _exc.method = 'get_data( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def get_frame( self ) -> DataFrame:
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            _source = self.__source
            _data = BudgetData( _source )
            return _data.create_frame( )
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Ninja'
            _exc.cause = 'DocumentControlNumber'
            _exc.method = 'create_frame( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class Expenditure( ):
    '''
    Constructor:  Expenditure( bfy: str, fund: str, account: str,
                        boc: str, pvdr: Provider = Provider.SQLite )

    Purpose:  Class defines object providing Expenditure data'''
    __source = None
    __provider = None
    __expendituresid = None
    __obligationsid = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __rpioname = None
    __fundcode = None
    __fundname = None
    __ahcode = None
    __ahname = None
    __orgcode = None
    __orgname = None
    __accountcode = None
    __programprojectname = None
    __boccode = None
    __bocname = None
    __rccode = None
    __rcname = None
    __documenttype = None
    __documentnumber = None
    __documentcontrolnumber = None
    __referencedocumentnumber = None
    __programprojectcode = None
    __programareacode = None
    __programareaname = None
    __processeddate = None
    __lastactivitydate = None
    __age = None
    __vendorcode = None
    __vendorage = None
    __foccode = None
    __focname = None
    __amount = None
    __goalcode = None
    __goalname = None
    __objectivecode = None
    __objectivename = None
    __npmcode = None
    __npmname = None
    __treasuryaccountcode = None
    __treasuryaccountname = None
    __budgetaccountcode = None
    __budgetaccountname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ) -> int:
        if self.__expendituresid is not None:
            return self.__expendituresid

    @id.setter
    def id( self, value: int ):
        if value is not None:
            self.__expendituresid = value

    @property
    def bfy( self ) -> str:
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value: str ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ) -> str:
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value: str ):
        if value is not None:
            self.__efy = value

    @property
    def rpio_code( self ) -> str:
        if self.__rpiocode is not None:
            return self.__rpiocode

    @rpio_code.setter
    def rpio_code( self, value: str ):
        if value is not None:
            self.__rpiocode = value

    @property
    def rpio_name( self ) -> str:
        if self.__rpioname is not None:
            return self.__rpioname

    @rpio_code.setter
    def rpio_code( self, value: str ):
        if value is not None:
            self.__rpiocode = value

    @property
    def ah_code( self ) -> str:
        if self.__ahcode is not None:
            return self.__ahcode

    @ah_code.setter
    def ah_code( self, value: str ):
        if value is not None:
            self.__ahcode = value

    @property
    def ah_name( self ) -> str:
        if self.__ahname is not None:
            return self.__ahname

    @ah_name.setter
    def ah_name( self, value: str ):
        if value is not None:
            self.__ahname = value

    @property
    def fund_code( self ) -> str:
        if self.__fundcode is not None:
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value: str ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund_name( self ) -> str:
        if self.__fundname is not None:
            return self.__fundname

    @fund_name.setter
    def fund_name( self, value: str ):
        if value is not None:
            self.__fundname = value

    @property
    def org_code( self ) -> str:
        if self.__orgcode is not None:
            return self.__orgcode

    @org_code.setter
    def org_code( self, value: str ):
        if value is not None:
            self.__orgcode = value

    @property
    def org_name( self  ):
        if self.__orgname is not None:
            return self.__orgname

    @org_name.setter
    def org_name( self, value  ):
        if value is not None:
            self.__orgname = value

    @property
    def account_code( self ) -> str:
        if self.__accountcode is not None:
            return self.__accountcode

    @account_code.setter
    def account_code( self, value: str ):
        if value is not None:
            self.__accountcode = value

    @property
    def boc_code( self ) -> str:
        if self.__boccode is not None:
            return self.__boccode

    @boc_code.setter
    def boc_code( self, value: str ):
        if value is not None:
            self.__boccode = value

    @property
    def boc_name( self ) -> str:
        if self.__bocname is not None:
            return self.__bocname

    @boc_name.setter
    def boc_name( self, value: str ):
        if value is not None:
            self.__bocname = value

    @property
    def rc_code( self ) -> str:
        if self.__rccode is not None:
            return self.__rccode

    @rc_code.setter
    def rc_code( self, value: str ):
        if value is not None:
            self.__rccode = value

    @property
    def rc_name( self ) -> str:
        if self.__rcname is not None:
            return self.__rcname

    @rc_name.setter
    def rc_name( self, value: str ):
        if value is not None:
            self.__rcname = value

    @property
    def document_type( self ) -> str:
        if self.__documenttype is not None:
            return self.__documenttype

    @document_type.setter
    def document_type( self, value: str ):
        if value is not None:
            self.__documenttype = value

    @property
    def document_number( self ) -> str:
        if self.__documentnumber is not None:
            return self.__documentnumber

    @document_number.setter
    def document_number( self, value: str ):
        if value is not None:
            self.__documentnumber = value

    @property
    def document_control_number( self ) -> str:
        if self.__documentcontrolnumber is not None:
            return self.__documentcontrolnumber

    @document_control_number.setter
    def document_control_number( self, value: str ):
        if value is not None:
            self.__documentcontrolnumber = value

    @property
    def reference_document_number( self ) -> str:
        if self.__referencedocumentnumber is not None:
            return self.__referencedocumentnumber

    @reference_document_number.setter
    def reference_document_number( self, value: str ):
        if value is not None:
            self.__referencedocumentnumber = value

    @property
    def processed_date( self ) -> str:
        if self.__processeddate is not None:
            return self.__processeddate

    @processed_date.setter
    def processed_date( self, value: str ):
        if value is not None:
            self.__processeddate = value

    @property
    def last_activity_date( self ) -> str:
        if self.__lastactivitydate is not None:
            return self.__lastactivitydate

    @last_activity_date.setter
    def last_activity_date( self, value: str ):
        if value is not None:
            self.__lastactivitydate = value

    @property
    def age( self ) -> str:
        if self.__age is not None:
            return self.__age

    @age.setter
    def age( self, value: str ):
        if value is not None:
            self.__age = value

    @property
    def vendor_code( self ) -> str:
        if self.__vendorcode is not None:
            return self.__vendorcode

    @vendor_code.setter
    def vendor_code( self, value: str ):
        if value is not None:
            self.__vendorcode = value

    @property
    def vendor_name( self ) -> str:
        if self.__vendorname is not None:
            return self.__vendorname

    @vendor_name.setter
    def vendor_name( self, value: str ):
        if value is not None:
            self.__vendorname = value

    @property
    def foc_code( self ) -> str:
        if self.__foccode is not None:
            return self.__foccode

    @foc_code.setter
    def foc_code( self, value: str ):
        if value is not None:
            self.__rccode = value

    @property
    def foc_name( self ) -> str:
        if self.__focname is not None:
            return self.__focname

    @foc_name.setter
    def foc_name( self, value: str ):
        if value is not None:
            self.__focname = value

    @property
    def amount( self ) -> float:
        if self.__amount is not None:
            return self.__amount

    @amount.setter
    def amount( self, value: float ):
        if value is not None:
            self.__amount = value

    @property
    def program_project_code( self ) -> str:
        if self.__programprojectcode is not None:
            return self.__programprojectcode

    @program_project_code.setter
    def program_project_code( self, value: str ):
        if value is not None:
            self.__programprojectcode = value

    @property
    def program_project_name( self ) -> str:
        if self.__programprojectname is not None:
            return self.__programprojectname

    @program_project_name.setter
    def program_project_name( self, value: str ):
        if value is not None:
            self.__programprojectname = value

    @property
    def program_area_code( self ) -> str:
        if self.__programareacode is not None:
            return self.__programareacode

    @program_area_code.setter
    def program_area_code( self, value: str ):
        if value is not None:
            self.__programareacode = value

    @property
    def program_area_name( self ) -> str:
        if self.__programareaname is not None:
            return self.__programareaname

    @program_area_name.setter
    def program_area_name( self, value: str ):
        if value is not None:
            self.__programareaname = value

    @property
    def goal_code( self ) -> str:
        if self.__goalcode is not None:
            return self.__goalcode

    @goal_code.setter
    def goal_code( self, value: str ):
        if value is not None:
            self.__goalcode = value

    @property
    def goal_name( self ) -> str:
        if self.__goalname is not None:
            return self.__goalname

    @goal_name.setter
    def goal_name( self, value: str ):
        if value is not None:
            self.__goalname = value

    @property
    def objective_code( self ) -> str:
        if self.__objectivecode is not None:
            return self.__objectivecode

    @objective_code.setter
    def objective_code( self, value: str ):
        if value is not None:
            self.__objectivecode = value

    @property
    def objective_name( self ) -> str:
        if self.__objectivename is not None:
            return self.__objectivename

    @objective_name.setter
    def objective_name( self, value: str ):
        if value is not None:
            self.__objectivename = value

    @property
    def npm_code( self ) -> str:
        if self.__npmcode is not None:
            return self.__npmcode

    @npm_code.setter
    def npm_code( self, value: str ):
        if value is not None:
            self.__npmcode = value

    @property
    def npm_name( self ) -> str:
        if self.__npmname is not None:
            return self.__npmname

    @npm_name.setter
    def npm_name( self, value: str ):
        if value is not None:
            self.__npmname = value

    @property
    def treasury_account_code( self ) -> str:
        if self.__treasuryaccountcode is not None:
            return self.__treasuryaccountcode

    @treasury_account_code.setter
    def treasury_account_code( self, value: str ):
        if value is not None:
            self.__treasuryaccountcode = value

    @property
    def treasury_account_name( self ) -> str:
        if self.__treasuryaccountname is not None:
            return self.__treasuryaccountname

    @treasury_account_name.setter
    def treasury_account_name( self, value: str ):
        if value is not None:
            self.__treasuryaccountname = value

    @property
    def budget_account_code( self ) -> str:
        if self.__budgetaccountcode is not None:
            return self.__budgetaccountcode

    @budget_account_code.setter
    def budget_account_code( self, value: str ):
        if value is not None:
            self.__budgetaccountcode = value

    @property
    def budget_account_name( self ) -> str:
        if self.__budgetaccountname is not None:
            return self.__budgetaccountname

    @budget_account_name.setter
    def budget_account_name( self, value: str ):
        if value is not None:
            self.__budgetaccountname = value

    @property
    def fields( self ) -> list[ str ]:
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value: list[ str ] ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy: str, fund: str, account: str,
                  boc: str, provider: Provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.Expenditures
        self.__bfy = bfy
        self.__fundcode = fund
        self.__accountcode = account
        self.__boccode = boc
        self.__fields = [ 'ExpendituresId',
                           'ObligationsId',
                           'BFY',
                           'EFY',
                           'RpioCode',
                           'RpioName',
                           'AhCode',
                           'AhName',
                           'FundCode',
                           'FundName',
                           'OrgCode',
                           'OrgName',
                           'AccountCode',
                           'ProgramProjectCode',
                           'ProgramProjectName',
                           'RcCode',
                           'RcName',
                           'DocumentType',
                           'DocumentNumber',
                           'DocumentControlNumber',
                           'ReferenceDocumentNumber',
                           'ProcessedDate',
                           'LastActivityDate',
                           'Age',
                           'BocCode',
                           'BocName',
                           'FocCode',
                           'FocName',
                           'NpmCode',
                           'NpmName',
                           'VendorCode',
                           'VendorName',
                           'Amount' ]

    def __str__( self ) -> str:
        if self.__amount is not None:
            return str( self.__amount )

    def get_data( self  ) -> list[ Row ]:
        try:
            _source = self.__source
            _provider = self.__provider
            _names = [ 'BFY', 'FundCode', 'AccountCode', 'BocCode' ]
            _values = (self.__bfy, self.__fundcode, self.__accountcode, self.__boccode)
            _dbconfig = DbConfig( _source, _provider )
            _sqlconfig = SqlConfig( names = _names, values = _values )
            _connection = Connection( self.__source )
            _sql = SqlStatement( _dbconfig, _sqlconfig )
            _sqlite = _connection.connect( )
            _cursor = _sqlite.cursor( )
            _query = _sql.get_query( )
            _db = _cursor.execute( _query )
            self.__data =  [ i for i in _db.fetchall( ) ]
            _cursor.close( )
            _sqlite.close( )
            return self.__data
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Ninja'
            _exc.cause = 'Expenditure'
            _exc.method = 'get_data( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def get_frame( self ) -> DataFrame:
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            _source = self.__source
            _data = BudgetData( _source )
            return _data.create_frame( )
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Ninja'
            _exc.cause = 'Expenditure'
            _exc.method = 'create_frame( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class FinanceObjectClass( ):
    '''
    Constructor:  FinanceObjectClass( code: str, pvdr: Provider = Provider.SQLite )

    Purpose: Class defines object representing the Finance Object Class'''
    __source = None
    __provider = None
    __financeobjectclassesid = None
    __code = None
    __name = None
    __boccode = None
    __bocname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ) -> int:
        if self.__financeobjectclassesid is not None:
            return self.__financeobjectclassesid

    @id.setter
    def id( self, id ):
        if id is not None:
            self.__financeobjectclassesid = id

    @property
    def code( self ) -> str:
        if  self.__code is not None:
            return self.__code

    @code.setter
    def code( self, code ):
        if code is not None:
            self.__code = code

    @property
    def name( self ) -> str:
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, name ):
        if  name is not None:
            self.__name = name

    @property
    def boc_code( self ) -> str:
        if self.__boccode is not None:
            return self.__boccode

    @boc_code.setter
    def boc_code( self, value: str ):
        if value is not None:
            self.__boccode = value

    @property
    def boc_name( self ) -> str:
        if self.__bocname is not None:
            return self.__bocname

    @boc_name.setter
    def boc_name( self, name ):
        if  name is not None:
            self.__bocname = name

    @property
    def data( self ) -> list:
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, cache ):
        if list is not None:
            self.__data = cache

    @property
    def table( self ) -> DataFrame:
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, frame: DataFrame ):
        if isinstance( frame, DataFrame ):
            self.__frame = frame

    @property
    def fields( self ) -> list[ str ]:
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value: list[ str ] ):
        if value is not None:
            self.__fields = value

    def __init__( self, code: str, provider: Provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.FinanceObjectClasses
        self.__code = code
        self.__fields = [ 'FinanceObjectClassesId',
                          'Code',
                          'Name',
                          'BocCode',
                          'BocName' ]

    def __str__( self ) -> str:
        if self.__code is not None:
            return self.__code

    def get_data( self  ) -> list[ Row ]:
        try:
            _source = self.__source
            _provider = self.__provider
            _names = [ 'Code', ]
            _values = (self.__code,)
            _dbconfig = DbConfig( _source, _provider )
            _sqlconfig = SqlConfig( names = _names, values = _values )
            _connection = Connection( self.__source )
            _sql = SqlStatement( _dbconfig, _sqlconfig )
            _sqlite = _connection.connect( )
            _cursor = _sqlite.cursor( )
            _query = _sql.get_query( )
            _db = _cursor.execute( _query )
            self.__data =  [ i for i in _db.fetchall( ) ]
            _cursor.close( )
            _sqlite.close( )
            return self.__data
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Execution'
            _exc.cause = 'FinanceObjectClass'
            _exc.method = 'get_data( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def get_frame( self ) -> DataFrame:
        '''Method returning pandas dataframe
        comprised of datatable _data'''
        try:
            _src = self.__source
            _data = BudgetData( _src )
            return _data.create_frame( )
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Execution'
            _exc.cause = 'FinanceObjectClass'
            _exc.method = 'create_frame( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class Fund( ):
    '''
    Constructor:  Fund( bfy: str, efy: str,
                  code: str, pvdr: Provider = Provider.SQLite )

    Purpose:  Class defines object represening Funds'''
    __source = None
    __provider = None
    __fundsid = None
    __code = None
    __name = None
    __bfy = None
    __efy = None
    __shortname = None
    __status = None
    __beginningperiodofavailability = None
    __endingperiodofavailability = None
    __main = None
    __multiyearindicator = None
    __sublevelprefix = None
    __allocationtransferagency = None
    __agencyidentifier = None
    __fundcategory = None
    __appropriationcode = None
    __appropriationname = None
    __fundgroup = None
    __noyear = None
    __carryover = None
    __cancelledyearspendingaccount = None
    __applyatalllevels = None
    __batsfund = None
    __batsenddate = None
    __batsoptionid = None
    __securityorg = None
    __treasuryaccountcode = None
    __treasuryaccountname = None
    __budgetaccountcode = None
    __budgetaccountname = None
    __apportionmentaccountcode = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ) -> int:
        if self.__fundsid is not None:
            return self.__fundsid

    @id.setter
    def id( self, value: int ):
        if value is not None:
            self.__fundsid = value

    @property
    def code( self ) -> str:
        if  self.__code is not None:
            return self.__code

    @code.setter
    def code( self, value: str ):
        if value is not None:
            self.__code = value

    @property
    def name( self ) -> str:
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, value: str ):
        if value is not None:
            self.__name = value

    @property
    def short_name( self ) -> str:
        if self.__shortname is not None:
            return self.__shortname

    @short_name.setter
    def short_name( self, value: str ):
        if value is not None:
            self.__shortname = value

    @property
    def status( self ) -> str:
        if self.__status is not None:
            return self.__status

    @status.setter
    def status( self, value: str ):
        if value is not None and value in [ 'ACTIVE', 'INACTIVE' ]:
            self.__status = value

    @property
    def bpoa( self ) -> str:
        if self.__beginningperiodofavailability is not None:
            return self.__beginningperiodofavailability

    @bpoa.setter
    def bpoa( self, value: str ):
        if value is not None:
            self.__beginningperiodofavailability = value

    @property
    def epoa( self ) -> str:
        if self.__endingperiodofavailability is not None:
            return self.__endingperiodofavailability

    @epoa.setter
    def epoa( self, value: str ):
        if value is not None:
            self.__endingperiodofavailability = value

    @property
    def main( self ) -> str:
        if self.__main is not None:
            return self.__main

    @main.setter
    def main( self, value: str ):
        if value is not None:
           self.__main = value

    @property
    def multiyear_indicator( self ) -> str:
        if self.__multiyearindicator is not None:
            return self.__multiyearindicator

    @multiyear_indicator.setter
    def multiyear_indicator( self, value: str ):
        if value is not None:
            self.__multiyearindicator = value

    @property
    def sub_level( self ) -> str:
        if self.__sublevelprefix is not None:
            return self.__sublevelprefix

    @sub_level.setter
    def sub_level( self, value: str ):
        if value is not None:
            self.__sublevelprefix = value

    @property
    def allocation_transfer_agency( self ) -> str:
        if self.__allocationtransferagency is not None:
            return self.__allocationtransferagency

    @allocation_transfer_agency.setter
    def allocation_transfer_agency( self, value: str ):
        if value is not None:
            self.__allocationtransferagency = value

    @property
    def agency_identifier( self ) -> str:
        if self.__agencyidentifier is not None:
            return self.__agencyidentifier

    @agency_identifier.setter
    def agency_identifier( self, value: str ):
        if value is not None:
            self.__agencyidentifier = value

    @property
    def fund_category( self ) -> str:
        if self.__fundcategory is not None:
            return self.__fundcategory

    @fund_category.setter
    def fund_category( self, value: str ):
        if value is not None:
            self.__fundcategory = value

    @property
    def appropriation_code( self ) -> str:
        if self.__appropriationcode is not None:
            return self.__appropriationcode

    @appropriation_code.setter
    def appropriation_code( self, value: str ):
        if value is not None:
            self.__appropriationcode = value

    @property
    def appropriation_name( self ) -> str:
        if self.__appropriationname is not None:
            return self.__appropriationname

    @appropriation_name.setter
    def appropriation_name( self, name ):
        if  name is not None:
            self.__appropriationname = name

    @property
    def fund_group( self ) -> str:
        if self.__fundgroup is not None:
            return self.__fundgroup

    @fund_group.setter
    def fund_group( self, value: str ):
        if value is not None:
            self.__fundgroup = value

    @property
    def no_year( self ) -> str:
        if self.__noyear is not None:
            return self.__noyear

    @no_year.setter
    def no_year( self, value: str ):
        if value is not None:
            self.__noyear = value

    @property
    def carry_over( self ) -> str:
        if self.__carryover is not None:
            return self.__carryover

    @carry_over.setter
    def carry_over( self, value: str ):
        if value is not None:
            self.__carryover = value

    @property
    def cancelled_spending_account( self ) -> str:
        if self.__cancelledyearspendingaccount is not None:
            return self.__cancelledyearspendingaccount

    @cancelled_spending_account.setter
    def cancelled_spending_account( self, acct ):
        if  acct is not None:
            self.__cancelledyearspendingaccount = acct

    @property
    def apply_all_levels( self ) -> str:
        if  self.__applyatalllevels is not None:
            return self.__applyatalllevels

    @apply_all_levels.setter
    def apply_all_levels( self, value: str ):
        if value is not None:
           self.__applyatalllevels = value

    @property
    def bats_fund( self ) -> str:
        if self.__batsfund is not None:
            return self.__batsfund

    @bats_fund.setter
    def bats_fund( self, value: str ):
        if value is not None:
            self.__batsfund = value

    @property
    def bats_end_date( self ) -> datetime:
        if self.__batsenddate is not None:
            return self.__batsenddate

    @bats_end_date.setter
    def bats_end_date( self, value: datetime ):
        if isinstance( value, datetime ):
            self.__batsenddate = value

    @property
    def bats_option_id( self ) -> str:
        if self.__batsoptionid is not None:
            return self.__batsoptionid

    @bats_option_id.setter
    def bats_option_id( self, value: str ):
        if value is not None:
            self.__batsoptionid = value

    @property
    def security_org( self ) -> str:
        if self.__securityorg is not None:
            return self.__securityorg

    @security_org.setter
    def security_org( self, value: str ):
        if value is not None:
            self.__securityorg = value

    @property
    def treasury_account_code( self ) -> str:
        if self.__treasuryaccountcode is not None:
            return self.__treasuryaccountcode

    @treasury_account_code.setter
    def treasury_account_code( self, value: str ):
        if value is not None:
            self.__treasuryaccountcode = value

    @property
    def treasury_account_name( self ) -> str:
        if self.__treasuryaccountname is not None:
            return self.__treasuryaccountname

    @treasury_account_name.setter
    def treasury_account_name( self, value: str ):
        if value is not None:
            self.__treasuryaccountname = value

    @property
    def budget_account_code( self ) -> str:
        if self.__budgetaccountcode is not None:
            return self.__budgetaccountcode

    @budget_account_code.setter
    def budget_account_code( self, value: str ):
        if value is not None:
            self.__budgetaccountcode = value

    @property
    def budget_account_name( self ) -> str:
        if self.__budgetaccountname is not None:
            return self.__budgetaccountname

    @budget_account_name.setter
    def budget_account_name( self, value: str ):
        if value is not None:
            self.__budgetaccountname = value

    @property
    def apportionment_account_code( self ) -> str:
        if self.__apportionmentaccountcode is not None:
            return self.__apportionmentaccountcode

    @apportionment_account_code.setter
    def apportionment_account_code( self, value: str ):
        if value is not None:
            self.__apportionmentaccountcode = value

    @property
    def data( self ) -> list:
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, value: list ):
        if isinstance( value, list ):
            self.__data = value

    @property
    def table( self ) -> DataFrame:
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, value: DataFrame ):
        if value is not None:
            self.__frame = value

    @property
    def fields( self ) -> list[ str ]:
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value: list[ str ] ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy: str, efy: str,
                  code: str, provider: Provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.Funds
        self.__bfy = bfy
        self.__efy = efy
        self.__code = code
        self.__fields = [ 'FundsId',
                          'BFY',
                          'EFY',
                          'Code',
                          'Name',
                          'ShortName',
                          'Status',
                          'SubLevelPrefix',
                          'ATA',
                          'BeginningPeriodOfAvailability',
                          'EndingPeriodOfAvailability',
                          'MAIN',
                          'A',
                          'AID',
                          'SUB',
                          'FundCategory',
                          'AppropriationCode',
                          'SubAppropriationCode',
                          'FundGroup',
                          'NoYear',
                          'Carryover',
                          'CancelledYearSpendingAccount',
                          'ApplyAtAllLevels',
                          'BatsFund',
                          'BatsEndDate',
                          'BatsOptionId',
                          'SecurityOrg' ]

    def __str__( self ) -> str:
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code

    def get_data( self  ) -> list[ Row ]:
        try:
            _source = self.__source
            _provider = self.__provider
            _names = [ 'BFY', 'EFY', 'Code', ]
            _values = (self.__bfy, self.__efy, self.__code)
            _dbconfig = DbConfig( _source, _provider )
            _sqlconfig = SqlConfig( names = _names, values = _values )
            _connection = Connection( self.__source )
            _sql = SqlStatement( _dbconfig, _sqlconfig )
            _sqlite = _connection.connect( )
            _cursor = _sqlite.cursor( )
            _query = _sql.get_query( )
            _db = _cursor.execute( _query )
            self.__data =  [ i for i in _db.fetchall( ) ]
            _cursor.close( )
            _sqlite.close( )
            return self.__data
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Execution'
            _exc.cause = 'Fund'
            _exc.method = 'get_data( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def get_frame( self ) -> DataFrame:
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            _source = self.__source
            _data = BudgetData( _source )
            return _data.create_frame( )
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Execution'
            _exc.cause = 'Fund'
            _exc.method = 'create_frame( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class FederalHoliday( ):
    '''
    Constructor: FederalHoliday( bfy: str, efy: str,
            name: str, pvdr: Provider = Provider.SQLite )

    Purpose: Defines the FederalHoliday class
    '''
    __source = None
    __provider = None
    __federalholidaysid = None
    __bfy = None
    __efy = None
    __name = None
    __newyearsday = None
    __martinlutherking = None
    __memorial = None
    __juneteenth = None
    __independence = None
    __washingtons = None
    __labor = None
    __columbus = None
    __veterans = None
    __thanksgiving = None
    __christmas = None
    __holidays = None
    __today = None
    __date = None
    __dayofweek = None
    __day = None
    __month = None
    __year = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ) -> int:
        if self.__federalholidaysid is not None:
            return self.__federalholidaysid

    @id.setter
    def id( self, value: int ):
        if value is not None:
            self.__federalholidaysid = value

    @property
    def bfy( self ) -> str:
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value: str ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ) -> str:
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value: str ):
        if value is not None:
            self.__efy = value

    @property
    def name( self ) -> str:
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, value: str ):
        if value in self.__holidays:
            self.__name = value

    @property
    def date( self ) -> datetime:
        if self.__date is not None:
            return self.__date

    @property
    def day( self ) -> int:
        if self.__day is not None:
            return self.__day

    @property
    def month( self ) -> int:
        if self.__month is not None:
            return self.__month

    @property
    def data( self ) -> list[ str ]:
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, value: list ):
        if value is not None:
            self.__data = value

    @property
    def holidays( self ) -> list[ str ]:
        if self.__holidays is not None:
            return self.__holidays

    @property
    def table( self ) -> DataFrame:
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, value: DataFrame ):
        if value is not None:
            self.__frame = value

    @property
    def observances( self ) -> dict:
        if self.__observance is not None:
            return self.__observance

    @property
    def fields( self ) -> list:
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value: list ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy: str, efy: str, name: str = '',
                  provider: Provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.FederalHolidays
        self.__holidays = [ 'Columbus', 'Veterans', 'Thanksgiving', 'Christmas',
                        'NewYearsDay', 'MartinLutherKing', 'Washingtons',
                        'Memorial', 'Juneteenth', 'Independence', 'Labor' ]
        self.__observance = { 'Columbus': 'The second Monday in October',
                              'Veterans': 'Veterans Day, November 11',
                              'Thanksgiving': 'The fourth Thursday in November',
                              'Christmas': 'Christmas Day, December 25',
                              'NewYearsDay': 'January 1',
                              'MartinLutherKing': 'The third Monday in January',
                              'Washingtons': 'The third Monday in February',
                              'Memorial': 'The last Monday in May.',
                              'Juneteenth': 'Juneteenth National Independence Day, June 19',
                              'Independence': 'Independence Day, July 4',
                              'Labor': 'The first Monday in September' }
        self.__bfy = bfy
        self.__efy = efy
        self.__year = int( bfy )
        self.__today = dt.datetime.today( )
        self.__name = self.set_name( name )
        self.__date = self.set_date( name )
        self.__dayofweek = self.__date.day
        self.__month = self.__date.month
        self.__day = self.__date.isoweekday( )
        self.__fields = [ 'FederalHolidaysId',
                          'BFY',
                          'Columbus',
                          'Veterans',
                          'Thanksgiving',
                          'Christmas',
                          'NewYears',
                          'MartinLutherKing',
                          'Presidents',
                          'Memorial',
                          'Juneteenth',
                          'Independence',
                          'Labor' ]
        self.__data = None
        self.__frame = None

    def __str__( self ) -> str:
        if not self.__name == '':
            return self.__name

    def get_data( self  ) -> list:
        try:
            _source = self.__source
            _provider = self.__provider
            _names = [ 'BFY', 'EFY', 'Name', ]
            _values = (self.__bfy, self.__efy, self.__name,)
            _dbconfig = DbConfig( _source, _provider )
            _sqlconfig = SqlConfig( names = _names, values = _values )
            _connection = Connection( self.__source )
            _sql = SqlStatement( _dbconfig, _sqlconfig )
            _sqlite = _connection.connect( )
            _cursor = _sqlite.cursor( )
            _query = _sql.get_query( )
            _db = _cursor.execute( _query )
            self.__data =  [ i for i in _db.fetchall( ) ]
            _cursor.close( )
            _sqlite.close( )
            return self.__data
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Execution'
            _exc.cause = 'FederalHoliday'
            _exc.method = 'get_data( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def get_frame( self ) -> DataFrame:
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            _source = self.__source
            _data = BudgetData( _source )
            return _data.create_frame( )
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Execution'
            _exc.cause = 'FederalHoliday'
            _exc.method = 'create_frame( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def get_columbus_day( self ) -> datetime:
        '''The second Monday in October'''
        try:
            if self.__year is not None:
                __start = datetime( self.__year, 10, 1 )
                __end = datetime( self.__year, 10, 31 )
                __delta = ( __start - __end ).days
                for i in range( 1, 31 ):
                    d = datetime( self.__year, 10, __start.day + i )
                    if ( 15 < d.day < 28 ) and datetime( self.__year, 10, d.day ).isoweekday( ) == 1:
                        self.__columbus = datetime( self.__year, 10, d.day )
                        return self.__columbus
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Execution'
            _exc.cause = 'FederalHoliday'
            _exc.method = 'columnbusday( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def get_veterans_day( self ) -> datetime:
        '''Veterans Day, November 11'''
        try:
            if self.__year is not None:
                self.__veterans = datetime( self.__year, 11, 11 )
                return self.__veterans
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Execution'
            _exc.cause = 'FederalHoliday'
            _exc.method = 'get_veterans_day( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def get_thanksgiving_day( self ) -> datetime:
        '''The fourth Thursday in November'''
        try:
            if self.__year is not None:
                __start = datetime( self.__year, 11, 15 )
                __end = datetime( self.__year, 11, 30 )
                __delta = ( __start - __end ).days
                for i in range( 15, 31 ):
                    d = datetime( self.__year, 11, i )
                    if ( 21 < d.day < 31 ) and datetime( self.__year, 11, d.day ).isoweekday( ) == 4:
                        self.__thanksgiving = datetime( self.__year, 11, d.day )
                        return self.__thanksgiving
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Execution'
            _exc.cause = 'FederalHoliday'
            _exc.method = 'get_thanksgiving_day( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def get_christmas_day( self ) -> datetime:
        '''Christmas Day, December 25'''
        try:
            if self.__year is not None:
                self.__christmas = datetime( self.__year, 12, 25 )
                return self.__christmas
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Execution'
            _exc.cause = 'FederalHoliday'
            _exc.method = 'get_christmas_day( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def get_newyears_day( self ) -> datetime:
        '''January 1'''
        try:
            if self.__year is not None:
                self.__newyearsday = datetime( self.__year, 1, 1 )
                return self.__newyearsday
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Execution'
            _exc.cause = 'FederalHoliday'
            _exc.method = 'get_newyears_day( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def get_martinlutherking_day( self ) -> datetime:
        '''The third Monday in January'''
        try:
            if self.__year is not None:
                __start = datetime( self.__year, 1, 15 )
                __end = datetime( self.__year, 1, 31 )
                __delta = ( __start - __end ).days
                for i in range( __delta ):
                    d = datetime( self.__year, 1, __start.day + i )
                    if ( 15 < d.day < 31) and datetime( self.__year, 1, d.day ).isoweekday( ) == 1:
                        self.__martinlutherking = datetime( self.__year, 1, d.day )
                        return self.__martinlutherking
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Execution'
            _exc.cause = 'FederalHoliday'
            _exc.method = 'get_martinlutherking_day( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def get_presidents_day( self ) -> datetime:
        '''The third Monday in February'''
        try:
            if self.__year is not None:
                __start = datetime( self.__year, 2, 15 )
                __end = datetime( self.__year, 2, 28 )
                __delta = ( __start - __end ).days
                for i in range( __delta ):
                    d = datetime( self.__year, 2, __start.day + i )
                    if (15 < d.day < 28) and datetime( self.__year, 2, d.day ).isoweekday( ) == 1:
                        self.__washingtons = datetime( self.__year, 2, d.day )
                        return self.__washingtons
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Execution'
            _exc.cause = 'FederalHoliday'
            _exc.method = 'get_presidents_day( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def get_memorial_day( self ) -> datetime:
        '''The last Monday in May'''
        try:
            if self.__year is not None:
                __start = datetime( self.__year, 5, 1 )
                __end = datetime( self.__year, 5, 31 )
                __delta = ( __start - __end ).days
                for i in range( 15, 31 ):
                    d = datetime( self.__year, 5, i )
                    if ( 21 < d.day < 31 ) and datetime( self.__year, 5, d.day ).isoweekday( ) == 1:
                        self.__memorial = datetime( self.__year, 5, d.day )
                        return self.__memorial
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Execution'
            _exc.cause = 'FederalHoliday'
            _exc.method = 'get_memorial_day( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def get_juneteenth_day( self ) -> datetime:
        '''Juneteenth National Independence Day, June 19'''
        try:
            if self.__year is not None:
                self.__juneteenth = datetime( self.__year, 6, 19 )
                return self.__juneteenth
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Execution'
            _exc.cause = 'FederalHoliday'
            _exc.method = 'get_juneteenth_day( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def get_independence_day( self ) -> datetime:
        '''Independence Day, July 4'''
        try:
            if self.__year is not None:
                self.__independence = datetime( self.__year, 7, 4 )
                return self.__independence
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Execution'
            _exc.cause = 'FederalHoliday'
            _exc.method = 'get_independence_day( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def get_labor_day( self ) -> datetime:
        '''The first Monday in September'''
        try:
            if self.__year is not None:
                __monday = list( )
                __month = dt.date( self.__year, 9, 1 ) - dt.date( self.__year, 9, 31 )
                for i in range( 1, __month.days - 1 ):
                    if datetime( self.__year, 9, i ).isoweekday( ) == 1:
                        __monday.append( datetime( self.__year, 9, i ) )
                y = __monday[ 0 ].date( ).year
                m = __monday[ 0 ].date( ).month
                d = __monday[ 0 ].date( ).day
                self.__labor = datetime( y, m, d )
                return self.__labor
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Execution'
            _exc.cause = 'FederalHoliday'
            _exc.method = 'get_labor_day( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def day_of_week( self ) -> str:
        try:
            if 0 < self.__day < 8 and  self.__day == 1:
                self.__dayofweek = 'Monday'
                return self.__dayofweek
            elif 0 <  self.__day < 8 and  self.__day == 2:
                self.__dayofweek = 'Tuesday'
                return self.__dayofweek
            elif 0 < self.__day < 8 and self.__day == 3:
                self.__dayofweek = 'Wednesday'
                return self.__dayofweek
            elif 0 < self.__day < 8 and self.__day == 4:
                self.__dayofweek = 'Thursday'
                return self.__dayofweek
            elif 0 < self.__day < 8 and self.__day == 5:
                self.__dayofweek = 'Friday'
                return self.__dayofweek
            elif 0 < self.__day < 8 and self.__day == 6:
                self.__dayofweek = 'Saturday'
                return self.__dayofweek
            elif 0 < self.__day < 8 and self.__day == 7:
                self.__dayofweek = 'Sunday'
                return self.__dayofweek
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Execution'
            _exc.cause = 'FederalHoliday'
            _exc.method = 'day_of_week( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def is_weekday( self ) -> bool:
        try:
            if 1 <= self.__date.isoweekday() <= 5:
                return True
            else:
                return False
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Execution'
            _exc.cause = 'FederalHoliday'
            _exc.method = 'is_weekday( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def is_weekend( self ) -> bool:
        try:
            if 5 < self.__date.isoweekday() <= 7:
                return True
            else:
                return False
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Execution'
            _exc.cause = 'FederalHoliday'
            _exc.method = 'is_weekend( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def set_date( self, name: str ):
        try:
            if isinstance( name, str ) and name in self.__holidays:
                if name == 'Columbus':
                    self.__date = self.get_columbus_day( )
                    return self.__date
                elif name == 'Veterans':
                    self.__date = self.get_veterans_day( )
                    return self.__date
                elif name == 'Thanksgiving':
                    self.__date = self.get_thanksgiving_day( )
                    return self.__date
                elif name == 'Christmas':
                    self.__date = self.get_christmas_day( )
                    return self.__date
                elif name == 'NewYearsDay':
                    self.__date = self.get_newyears_day( )
                    return self.__date
                elif name == 'MartinLutherKing':
                    self.__date = self.get_martinlutherking_day( )
                    return self.__date
                elif name == 'Washingtons':
                    self.__date = self.get_presidents_day( )
                    return self.__date
                elif name == 'Memorial':
                    self.__date = self.get_memorial_day( )
                    return self.__date
                elif name == 'Juneteenth':
                    self.__date = self.get_juneteenth_day( )
                    return self.__date
                elif name == 'Labor':
                    self.__date = self.get_labor_day( )
                    return self.__date
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Execution'
            _exc.cause = 'FederalHoliday'
            _exc.method = 'set_date( self, value )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def set_name( self, name: str ):
        try:
            if isinstance( name, str ) and name in self.__holidays:
                self.__name = name
                return self.__name
            else:
                self.__name = 'NS'
                return self.__name
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Execution'
            _exc.cause = 'FederalHoliday'
            _exc.method = 'set_name( self, value  ) '
            _err = ErrorDialog( _exc )
            _err.show( )

class FullTimeEquivalent( ):
    '''
    Constructor: FullTimeEquivalent( bfy: str, fund: str, pvdr: Provider = Provider.SQLite )

    Purpose:  Object representing Operating Plan FTE
    '''
    __source = None
    __provider = None
    __fulltimeequivalentsid = None
    __operatingplansid = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __rpioname = None
    __fundcode = None
    __fundname = None
    __ahcode = None
    __ahname = None
    __orgcode = None
    __orgname = None
    __accountcode = None
    __boccode = None
    __bocname = None
    __rccode = None
    __rcname = None
    __amount = None
    __programprojectcode = None
    __programprojectname = None
    __programareacode = None
    __programareaname = None
    __goalcode = None
    __goalname = None
    __objectivecode = None
    __objectivename = None
    __npmcode = None
    __npmname = None
    __treasuryaccountcode = None
    __treasuryaccountname = None
    __budgetaccountcode = None
    __budgetaccountname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ) -> int:
        if self.__fulltimeequivalentsid is not None:
            return self.__fulltimeequivalentsid

    @id.setter
    def id( self, value: int ):
        if value is not None:
            self.__fulltimeequivalentsid = value

    @property
    def bfy( self ) -> str:
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value: str ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ) -> str:
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value: str ):
        if value is not None:
            self.__efy = value

    @property
    def rpio_code( self ) -> str:
        if self.__rpiocode is not None:
            return self.__rpiocode

    @rpio_code.setter
    def rpio_code( self, value: str ):
        if value is not None:
            self.__rpiocode = value

    @property
    def rpio_name( self ) -> str:
        if self.__rpioname is not None:
            return self.__rpioname

    @rpio_code.setter
    def rpio_code( self, value: str ):
        if value is not None:
            self.__rpiocode = value

    @property
    def ah_code( self ) -> str:
        if self.__ahcode is not None:
            return self.__ahcode

    @ah_code.setter
    def ah_code( self, value: str ):
        if value is not None:
            self.__ahcode = value

    @property
    def ah_name( self ) -> str:
        if self.__ahname is not None:
            return self.__ahname

    @ah_name.setter
    def ah_name( self, value: str ):
        if value is not None:
            self.__ahname = value

    @property
    def fund_code( self ) -> str:
        if self.__fundcode is not None:
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value: str ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund_name( self ) -> str:
        if self.__fundname is not None:
            return self.__fundname

    @fund_name.setter
    def fund_name( self, value: str ):
        if value is not None:
            self.__fundname = value

    @property
    def org_code( self ) -> str:
        if self.__orgcode is not None:
            return self.__orgcode

    @org_code.setter
    def org_code( self, value: str ):
        if value is not None:
            self.__orgcode = value

    @property
    def org_name( self  ):
        if self.__orgname is not None:
            return self.__orgname

    @org_name.setter
    def org_name( self, value  ):
        if value is not None:
            self.__orgname = value

    @property
    def account_code( self ) -> str:
        if self.__accountcode is not None:
            return self.__accountcode

    @account_code.setter
    def account_code( self, value: str ):
        if value is not None:
            self.__accountcode = value

    @property
    def boc_code( self ) -> str:
        if self.__boccode is not None:
            return self.__boccode

    @boc_code.setter
    def boc_code( self, value: str ):
        if value is not None:
            self.__boccode = value

    @property
    def boc_name( self ) -> str:
        if self.__bocname is not None:
            return self.__bocname

    @boc_name.setter
    def boc_name( self, value: str ):
        if value is not None:
            self.__bocname = value

    @property
    def rc_code( self ) -> str:
        if self.__rccode is not None:
            return self.__rccode

    @rc_code.setter
    def rc_code( self, value: str ):
        if value is not None:
            self.__rccode = value

    @property
    def rc_name( self ) -> str:
        if self.__rcname is not None:
            return self.__rcname

    @rc_name.setter
    def rc_name( self, value: str ):
        if value is not None:
            self.__rcname = value

    @property
    def amount( self ) -> float:
        if self.__amount is not None:
            return self.__amount

    @amount.setter
    def amount( self, value: float ):
        if value is not None:
            self.__amount = value

    @property
    def program_project_code( self ) -> str:
        if self.__programprojectcode is not None:
            return self.__programprojectcode

    @program_project_code.setter
    def program_project_code( self, value: str ):
        if value is not None:
            self.__programprojectcode = value

    @property
    def program_project_name( self ) -> str:
        if self.__programprojectname is not None:
            return self.__programprojectname

    @program_project_name.setter
    def program_project_name( self, value: str ):
        if value is not None:
            self.__programprojectname = value

    @property
    def program_area_code( self ) -> str:
        if self.__programareacode is not None:
            return self.__programareacode

    @program_area_code.setter
    def program_area_code( self, value: str ):
        if value is not None:
            self.__programareacode = value

    @property
    def program_area_name( self ) -> str:
        if self.__programareaname is not None:
            return self.__programareaname

    @program_area_name.setter
    def program_area_name( self, value: str ):
        if value is not None:
            self.__programareaname = value

    @property
    def goal_code( self ) -> str:
        if self.__goalcode is not None:
            return self.__goalcode

    @goal_code.setter
    def goal_code( self, value: str ):
        if value is not None:
            self.__goalcode = value

    @property
    def goal_name( self ) -> str:
        if self.__goalname is not None:
            return self.__goalname

    @goal_name.setter
    def goal_name( self, value: str ):
        if value is not None:
            self.__goalname = value

    @property
    def objective_code( self ) -> str:
        if self.__objectivecode is not None:
            return self.__objectivecode

    @objective_code.setter
    def objective_code( self, value: str ):
        if value is not None:
            self.__objectivecode = value

    @property
    def objective_name( self ) -> str:
        if self.__objectivename is not None:
            return self.__objectivename

    @objective_name.setter
    def objective_name( self, value: str ):
        if value is not None:
            self.__objectivename = value

    @property
    def npm_code( self ) -> str:
        if self.__npmcode is not None:
            return self.__npmcode

    @npm_code.setter
    def npm_code( self, value: str ):
        if value is not None:
            self.__npmcode = value

    @property
    def npm_name( self ) -> str:
        if self.__npmname is not None:
            return self.__npmname

    @npm_name.setter
    def npm_name( self, value: str ):
        if value is not None:
            self.__npmname = value

    @property
    def treasury_account_code( self ) -> str:
        if self.__treasuryaccountcode is not None:
            return self.__treasuryaccountcode

    @treasury_account_code.setter
    def treasury_account_code( self, value: str ):
        if value is not None:
            self.__treasuryaccountcode = value

    @property
    def treasury_account_name( self ) -> str:
        if self.__treasuryaccountname is not None:
            return self.__treasuryaccountname

    @treasury_account_name.setter
    def treasury_account_name( self, value: str ):
        if value is not None:
            self.__treasuryaccountname = value

    @property
    def budget_account_code( self ) -> str:
        if self.__budgetaccountcode is not None:
            return self.__budgetaccountcode

    @budget_account_code.setter
    def budget_account_code( self, value: str ):
        if value is not None:
            self.__budgetaccountcode = value

    @property
    def budget_account_name( self ) -> str:
        if self.__budgetaccountname is not None:
            return self.__budgetaccountname

    @budget_account_name.setter
    def budget_account_name( self, value: str ):
        if value is not None:
            self.__budgetaccountname = value

    @property
    def fields( self ) -> list[ str ]:
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value: list[ str ] ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy: str, fund: str, provider: Provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.FullTimeEquivalents
        self.__bfy = bfy
        self.__fundcode = fund
        self.__fields = [ 'FullTimeEquivalentsId',
                          'OperatingPlansId',
                          'RpioCode',
                          'RpioName',
                          'BFY',
                          'EFY',
                          'AhCode',
                          'FundCode',
                          'OrgCode',
                          'AccountCode',
                          'BocCode',
                          'BocName',
                          'Amount',
                          'ITProjectCode',
                          'ProjectCode',
                          'ProjectName',
                          'NpmCode',
                          'ProjectTypeName',
                          'ProjectTypeCode',
                          'ProgramProjectCode',
                          'ProgramAreaCode',
                          'NpmName',
                          'AhName',
                          'FundName',
                          'OrgName',
                          'RcName',
                          'ProgramProjectName',
                          'ActivityCode',
                          'ActivityName',
                          'LocalCode',
                          'LocalCodeName',
                          'ProgramAreaName',
                          'CostAreaCode',
                          'CostAreaName',
                          'GoalCode',
                          'GoalName',
                          'ObjectiveCode',
                          'ObjectiveName' ]

    def get_data( self  ) -> list[ Row ]:
        try:
            _source = self.__source
            _provider = self.__provider
            _names = [ 'BFY', 'FundCode' ]
            _values = (self.__bfy, self.__fundcode,)
            _dbconfig = DbConfig( _source, _provider )
            _sqlconfig = SqlConfig( names = _names, values = _values )
            _connection = Connection( self.__source )
            _sql = SqlStatement( _dbconfig, _sqlconfig )
            _sqlite = _connection.connect( )
            _cursor = _sqlite.cursor( )
            _query = _sql.get_query( )
            _db = _cursor.execute( _query )
            self.__data =  [ i for i in _db.fetchall( ) ]
            _cursor.close( )
            _sqlite.close( )
            return self.__data
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Ninja'
            _exc.cause = 'FullTimeEquivalent'
            _exc.method = 'get_data( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def get_frame( self ) -> DataFrame:
        '''Method returning pandas dataframe'''
        try:
            _source = self.__source
            _data = BudgetData( _source )
            return _data.create_frame( )
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Ninja'
            _exc.cause = 'FullTimeEquivalent'
            _exc.method = 'create_frame( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class GeneralLedgerAccount( ):
    '''
    Constructor:  GeneralLedgerAccount( bfy: str, number: str,
        pvdr: Provider = Provider.SQLite  )

    Purpose: Class defines object representing General Ledger Accounts
    '''
    __source = None
    __provider = None
    __generalledgeraccountsid = None
    __bfy = None
    __efy = None
    __treasurysymbol = None
    __fundcode = None
    __fundname = None
    __accountnumber = None
    __accountname = None
    __fields = None

    @property
    def id( self ) -> int:
        if self.__ledgeraccountsid is not None:
            return self.__ledgeraccountsid

    @id.setter
    def id( self, value: int ):
        if value is not None:
            self.__ledgeraccountsid = value

    @property
    def bfy( self ) -> str:
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value: str ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ) -> str:
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value: str ):
        if value is not None:
            self.__efy = value

    @property
    def fund_code( self ) -> str:
        if self.__fundcode is not None:
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value: str ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund_name( self ) -> str:
        if self.__fundname is not None:
            return self.__fundname

    @fund_name.setter
    def fund_name( self, value: str ):
        if value is not None:
            self.__fundname = value

    @property
    def account_number( self ) -> str:
        if self.__accountnumber is not None:
            return self.__accountnumber

    @account_number.setter
    def account_number( self, value: str ):
        if value is not None:
            self.__accountnumber = value

    @property
    def account_name( self ) -> str:
        if self.__accountname is not None:
            return self.__accountname

    @account_name.setter
    def account_name( self, value: str ):
        if value is not None:
            self.__accountname = value

    @property
    def treasury_symbol( self ) -> str:
        if self.__treasuryaccount is not None:
            return self.__treasuryaccount

    @treasury_symbol.setter
    def treasury_symbol( self, value: str ):
        if value is not None:
            self.__treasuryaccount = value

    @property
    def fields( self ) -> list[ str ]:
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value: list[ str ] ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy: str, number: str, provider: Provider = Provider.SQLite ):
        self.__bfy = bfy
        self.__accountnumber = number
        self.__provider = provider
        self.__source = Source.GeneralLedgerAccounts
        self.__fields = [ 'GeneralLedgerAccountsId',
                          'BFY',
                          'EFY',
                          'FundCode',
                          'FundName',
                          'TreasurySymbol',
                          'AccountNumber',
                          'AccountName',
                          'BeginningBalance',
                          'CreditBalance',
                          'DebitBalance',
                          'ClosingAmount' ]

class Goal( ):
    '''
    Constructor: Goal( code: str, pvdr: Provider = Provider.SQLite )

    Purpose;  Class defines object representing EPA  Goals
    '''
    __source = None
    __provider = None
    __goalsid = None
    __code = None
    __name = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ) -> int:
        if self.__goalsid is not None:
            return self.__goalsid

    @id.setter
    def id( self, value: int ):
        if value is not None:
            self.__goalsid = value

    @property
    def code( self ) -> str:
        if  self.__code is not None:
            return self.__code

    @code.setter
    def code( self, value: str ):
        if value is not None:
            self.__code = value

    @property
    def name( self ) -> str:
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, value: str ):
        if value is not None:
            self.__name = value

    @property
    def data( self ) -> list:
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, value: list ):
        if isinstance( value, list ):
            self.__data = value

    @property
    def table( self ) -> DataFrame:
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, value: DataFrame ):
        if value is not None:
            self.__frame = value

    @property
    def fields( self ) -> list[ str ]:
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value: list[ str ] ):
        if value is not None:
            self.__fields = value

    def __init__( self, code: str, provider: Provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.Goals
        self.__code = code
        self.__fields = [ 'GoalsId',
                          'Code',
                          'Name',
                          'Title' ]

    def __str__( self ) -> str:
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code

    def get_data( self  ) -> list[ Row ]:
        try:
            _source = self.__source
            _provider = self.__provider
            _names = [ 'Code', ]
            _values = (self.__code,)
            _dbconfig = DbConfig( _source, _provider )
            _sqlconfig = SqlConfig( names = _names, values = _values )
            _connection = Connection( self.__source )
            _sql = SqlStatement( _dbconfig, _sqlconfig )
            _sqlite = _connection.connect( )
            _cursor = _sqlite.cursor( )
            _query = _sql.get_query( )
            _db = _cursor.execute( _query )
            self.__data =  [ i for i in _db.fetchall( ) ]
            _cursor.close( )
            _sqlite.close( )
            return self.__data
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Execution'
            _exc.cause = 'Goal'
            _exc.method = 'get_data( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class HeadquartersAuthority( ):
    '''
    Constructor: HeadquartersAuthority( bfy, rpio, pvdr = Provider.SQLite )

    Purpose:  Class defines object representing HQ Allocation'''
    __source = None
    __provider = None
    __headquartersauthorityid = None
    __statusoffundsid = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __rpioname = None
    __fundcode = None
    __fundname = None
    __ahcode = None
    __ahname = None
    __orgcode = None
    __orgname = None
    __accountcode = None
    __boccode = None
    __bocname = None
    __rccode = None
    __rcname = None
    __amount = None
    __programprojectcode = None
    __programprojectname = None
    __programareacode = None
    __programareaname = None
    __goalcode = None
    __goalname = None
    __objectivecode = None
    __objectivename = None
    __npmcode = None
    __npmname = None
    __treasuryaccountcode = None
    __treasuryaccountname = None
    __budgetaccountcode = None
    __budgetaccountname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ) -> int:
        if self.__statusoffundsid is not None:
            return self.__statusoffundsid

    @id.setter
    def id( self, value: int ):
        if value is not None:
            self.__statusoffundsid = value

    @property
    def bfy( self ) -> str:
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value: str ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ) -> str:
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value: str ):
        if value is not None:
            self.__efy = value

    @property
    def rpio_code( self ) -> str:
        if self.__rpiocode is not None:
            return self.__rpiocode

    @rpio_code.setter
    def rpio_code( self, value: str ):
        if value is not None:
            self.__rpiocode = value

    @property
    def rpio_name( self ) -> str:
        if self.__rpioname is not None:
            return self.__rpioname

    @rpio_code.setter
    def rpio_code( self, value: str ):
        if value is not None:
            self.__rpiocode = value

    @property
    def ah_code( self ) -> str:
        if self.__ahcode is not None:
            return self.__ahcode

    @ah_code.setter
    def ah_code( self, value: str ):
        if value is not None:
            self.__ahcode = value

    @property
    def ah_name( self ) -> str:
        if self.__ahname is not None:
            return self.__ahname

    @ah_name.setter
    def ah_name( self, value: str ):
        if value is not None:
            self.__ahname = value

    @property
    def fund_code( self ) -> str:
        if self.__fundcode is not None:
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value: str ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund_name( self ) -> str:
        if self.__fundname is not None:
            return self.__fundname

    @fund_name.setter
    def fund_name( self, value: str ):
        if value is not None:
            self.__fundname = value

    @property
    def org_code( self ) -> str:
        if self.__orgcode is not None:
            return self.__orgcode

    @org_code.setter
    def org_code( self, value: str ):
        if value is not None:
            self.__orgcode = value

    @property
    def org_name( self  ):
        if self.__orgname is not None:
            return self.__orgname

    @org_name.setter
    def org_name( self, value  ):
        if value is not None:
            self.__orgname = value

    @property
    def account_code( self ) -> str:
        if self.__accountcode is not None:
            return self.__accountcode

    @account_code.setter
    def account_code( self, value: str ):
        if value is not None:
            self.__accountcode = value

    @property
    def boc_code( self ) -> str:
        if self.__boccode is not None:
            return self.__boccode

    @boc_code.setter
    def boc_code( self, value: str ):
        if value is not None:
            self.__boccode = value

    @property
    def boc_name( self ) -> str:
        if self.__bocname is not None:
            return self.__bocname

    @boc_name.setter
    def boc_name( self, value: str ):
        if value is not None:
            self.__bocname = value

    @property
    def rc_code( self ) -> str:
        if self.__rccode is not None:
            return self.__rccode

    @rc_code.setter
    def rc_code( self, value: str ):
        if value is not None:
            self.__rccode = value

    @property
    def rc_name( self ) -> str:
        if self.__rcname is not None:
            return self.__rcname

    @rc_name.setter
    def rc_name( self, value: str ):
        if value is not None:
            self.__rcname = value

    @property
    def amount( self ) -> float:
        if self.__amount is not None:
            return self.__amount

    @amount.setter
    def amount( self, value: float ):
        if value is not None:
            self.__amount = value

    @property
    def program_project_code( self ) -> str:
        if self.__programprojectcode is not None:
            return self.__programprojectcode

    @program_project_code.setter
    def program_project_code( self, value: str ):
        if value is not None:
            self.__programprojectcode = value

    @property
    def program_project_name( self ) -> str:
        if self.__programprojectname is not None:
            return self.__programprojectname

    @program_project_name.setter
    def program_project_name( self, value: str ):
        if value is not None:
            self.__programprojectname = value

    @property
    def program_area_code( self ) -> str:
        if self.__programareacode is not None:
            return self.__programareacode

    @program_area_code.setter
    def program_area_code( self, value: str ):
        if value is not None:
            self.__programareacode = value

    @property
    def program_area_name( self ) -> str:
        if self.__programareaname is not None:
            return self.__programareaname

    @program_area_name.setter
    def program_area_name( self, value: str ):
        if value is not None:
            self.__programareaname = value

    @property
    def goal_code( self ) -> str:
        if self.__goalcode is not None:
            return self.__goalcode

    @goal_code.setter
    def goal_code( self, value: str ):
        if value is not None:
            self.__goalcode = value

    @property
    def goal_name( self ) -> str:
        if self.__goalname is not None:
            return self.__goalname

    @goal_name.setter
    def goal_name( self, value: str ):
        if value is not None:
            self.__goalname = value

    @property
    def objective_code( self ) -> str:
        if self.__objectivecode is not None:
            return self.__objectivecode

    @objective_code.setter
    def objective_code( self, value: str ):
        if value is not None:
            self.__objectivecode = value

    @property
    def objective_name( self ) -> str:
        if self.__objectivename is not None:
            return self.__objectivename

    @objective_name.setter
    def objective_name( self, value: str ):
        if value is not None:
            self.__objectivename = value

    @property
    def npm_code( self ) -> str:
        if self.__npmcode is not None:
            return self.__npmcode

    @npm_code.setter
    def npm_code( self, value: str ):
        if value is not None:
            self.__npmcode = value

    @property
    def npm_name( self ) -> str:
        if self.__npmname is not None:
            return self.__npmname

    @npm_name.setter
    def npm_name( self, value: str ):
        if value is not None:
            self.__npmname = value

    @property
    def treasury_account_code( self ) -> str:
        if self.__treasuryaccountcode is not None:
            return self.__treasuryaccountcode

    @treasury_account_code.setter
    def treasury_account_code( self, value: str ):
        if value is not None:
            self.__treasuryaccountcode = value

    @property
    def treasury_account_name( self ) -> str:
        if self.__treasuryaccountname is not None:
            return self.__treasuryaccountname

    @treasury_account_name.setter
    def treasury_account_name( self, value: str ):
        if value is not None:
            self.__treasuryaccountname = value

    @property
    def budget_account_code( self ) -> str:
        if self.__budgetaccountcode is not None:
            return self.__budgetaccountcode

    @budget_account_code.setter
    def budget_account_code( self, value: str ):
        if value is not None:
            self.__budgetaccountcode = value

    @property
    def budget_account_name( self ) -> str:
        if self.__budgetaccountname is not None:
            return self.__budgetaccountname

    @budget_account_name.setter
    def budget_account_name( self, value: str ):
        if value is not None:
            self.__budgetaccountname = value

    @property
    def fields( self ) -> list[ str ]:
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value: list[ str ] ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy, efy, rpio, provider = Provider.SQLite ):
        self.__source = Source.HeadquartersAuthority
        self.__provider = provider
        self.__bfy = bfy
        self.__efy = efy
        self.__rpiocode = rpio
        self.__fields = [ 'HeadquartersAuthorityId',
                           'AllocationsId',
                           'StatusOfFundsId',
                           'BudgetLevel',
                           'BFY',
                           'EFY',
                           'RpioCode',
                           'RpioName',
                           'AhCode',
                           'AhName',
                           'FundCode',
                           'FundName',
                           'OrgCode',
                           'OrgName',
                           'AccountCode',
                           'ProgramProjectCode',
                           'ProgramProjectName',
                           'ProgramAreaCode',
                           'ProgramAreaName',
                           'RcCode',
                           'RcName',
                           'BocCode',
                           'BocName',
                           'Amount',
                           'NpmCode',
                           'NpmName' ]

    def get_data( self  ) -> list[ Row ]:
        try:
            _source = self.__source
            _provider = self.__provider
            _names = [ 'BFY', 'RpioCode' ]
            _values = (self.__bfy, self.__rpiocode)
            _dbconfig = DbConfig( _source, _provider )
            _sqlconfig = SqlConfig( names = _names, values = _values )
            _connection = Connection( self.__source )
            _sql = SqlStatement( _dbconfig, _sqlconfig )
            _sqlite = _connection.connect( )
            _cursor = _sqlite.cursor( )
            _query = _sql.get_query( )
            _db = _cursor.execute( _query )
            self.__data =  [ i for i in _db.fetchall( ) ]
            _cursor.close( )
            _sqlite.close( )
            return self.__data
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Ninja'
            _exc.cause = 'HeadquartersAuthority'
            _exc.method = 'get_data( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def get_frame( self ) -> DataFrame:
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            _source = self.__source
            _data = BudgetData( _source )
            return _data.create_frame( )
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Ninja'
            _exc.cause = 'HeadquartersAuthority'
            _exc.method = 'create_frame( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class HeadquartersOffice( ):
    '''
    Constructor: HeadquartersOffice( code: str, pvdr: Provider = Provider.SQLite )

    Prupose:  Class defines object representing RPIO'''
    __source = None
    __provider = None
    __resourceplanningofficesid = None
    __rpiocode = None
    __rpioname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ) -> int:
        if self.__resourceplanningofficesid is not None:
            return self.__resourceplanningofficesid

    @id.setter
    def id( self, value: int ):
        if value is not None:
            self.___resourceplanningofficesid = value

    @property
    def rpio_code( self ) -> str:
        if self.__rpiocode is not None:
            return self.__rpiocode

    @rpio_code.setter
    def rpio_code( self, value: str ):
        if value is not None:
            self.__rpiocode = value

    @property
    def rpio_name( self ) -> str:
        if self.__rpioname is not None:
            return self.__rpioname

    @rpio_name.setter
    def rpio_name( self, value: str ):
        if value is not None:
            self.__rpioname = value

    @property
    def data( self ) -> list:
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, value: list ):
        if isinstance( value, list ):
            self.__data = value

    @property
    def table( self ) -> DataFrame:
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, value: DataFrame ):
        if value is not None:
            self.__frame = value

    @property
    def fields( self ) -> list[ str ]:
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value: list[ str ] ):
        if value is not None:
            self.__fields = value

    def __init__( self, code: str, provider: Provider = Provider.SQLite ):
        self.__rpiocode = code
        self.__provider = provider
        self.__source = Source.HeadquartersOffices
        self.__fields = [ 'HeadquartersOfficesId',
                          'ResourcePlanningOfficesId',
                          'RpioCode',
                          'RpioName' ]


    def __str__( self ) -> str:
        if self.__rpiocode is not None:
            return self.__rpiocode

    def get_data( self  ) -> list[ Row ]:
        try:
            _source = self.__source
            _provider = self.__provider
            _names = [ 'RpioCode', ]
            _values = (self.__rpiocode,)
            _dbconfig = DbConfig( _source, _provider )
            _sqlconfig = SqlConfig( names = _names, values = _values )
            _connection = Connection( self.__source )
            _sql = SqlStatement( _dbconfig, _sqlconfig )
            _sqlite = _connection.connect( )
            _cursor = _sqlite.cursor( )
            _query = _sql.get_query( )
            _db = _cursor.execute( _query )
            self.__data =  [ i for i in _db.fetchall( ) ]
            _cursor.close( )
            _sqlite.close( )
            return self.__data
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Execution'
            _exc.cause = 'HeadquartersOffice'
            _exc.method = 'get_data( self ) '
            _err = ErrorDialog( _exc )
            _err.show( )

    def get_frame( self ) -> DataFrame:
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            _source = self.__source
            _data = BudgetData( _source )
            return _data.create_frame( )
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Execution'
            _exc.cause = 'HeadquartersOffice'
            _exc.method = 'create_frame( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class InflationReductionActCarryoverEstimate( ):
    '''
    Constructor: InflationReductionActCarryoverEstimate( bfy: str,
        pvdr: Provider = Provider.SQLite )

    Purpose:  Class defines object providing IRA Carryover Estimates
    '''
    __source = None
    __provider = None
    __iracarryoverestimatesid = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __rpioname = None
    __fundcode = None
    __fundname = None
    __amount = None
    __opencommitments = None
    __obligations = None
    __estimate = None
    __treasuryaccountcode = None
    __treasuryaccountname = None
    __budgetaccountcode = None
    __budgetaccountname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ) -> int:
        if self.__annualcarryoverestimatesid is not None:
            return self.__annualcarryoverestimatesid

    @id.setter
    def id( self, value: int ):
        if value is not None:
            self.__annualcarryoverestimatesid = value

    @property
    def bfy( self ) -> str:
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value: str ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ) -> str:
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value: str ):
        if value is not None:
            self.__efy = value

    @property
    def rpio_code( self ) -> str:
        if self.__rpiocode is not None:
            return self.__rpiocode

    @rpio_code.setter
    def rpio_code( self, value: str ):
        if value is not None:
            self.__rpiocode = value

    @property
    def rpio_name( self ) -> str:
        if self.__rpioname is not None:
            return self.__rpioname

    @rpio_code.setter
    def rpio_code( self, value: str ):
        if value is not None:
            self.__rpiocode = value

    @property
    def fund_code( self ) -> str:
        if self.__fundcode is not None:
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value: str ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund_name( self ) -> str:
        if self.__fundname is not None:
            return self.__fundname

    @fund_name.setter
    def fund_name( self, value: str ):
        if value is not None:
            self.__fundname = value

    @property
    def amount( self ) -> float:
        if self.__amount is not None:
            return self.__amount

    @amount.setter
    def amount( self, value: float ):
        if value is not None:
            self.__amount = value

    @property
    def available( self ) -> float:
        if isinstance( self.__availablebalance, float ):
            return self.__availablebalance

    @available.setter
    def available( self, value: float ):
        if value is not None:
            self.__availablebalance = value

    @property
    def open_commitments( self ) -> float:
        if isinstance( self.__opencommitments, float ):
            return self.__opencommitments

    @open_commitments.setter
    def open_commitments( self, value: float ):
        if value is not None:
            self.__opencommitments = value

    @property
    def obligations( self ) -> float:
        if self.__obligations is not None:
            return self.__obligations

    @obligations.setter
    def obligations( self, value: float ):
        if value is not None:
            self.__obligations = value

    @property
    def treasury_account_code( self ) -> str:
        if isinstance( self.__treasuryaccountcode, str ) \
                and self.__treasuryaccountcode != '':
            return self.__treasuryaccountcode

    @treasury_account_code.setter
    def treasury_account_code( self, value: str ):
        if value is not None:
            self.__treasuryaccountcode = value

    @property
    def treasury_account_name( self ) -> str:
        if isinstance( self.__treasuryaccountname, str ) \
                and self.__treasuryaccountname != '':
            return self.__treasuryaccountname

    @treasury_account_name.setter
    def treasury_account_name( self, value: str ):
        if value is not None:
            self.__treasuryaccountname = value

    @property
    def budget_account_code( self ) -> str:
        if self.__budgetaccountcode is not None:
            return self.__budgetaccountcode

    @budget_account_code.setter
    def budget_account_code( self, value: str ):
        if value is not None:
            self.__budgetaccountcode = value

    @property
    def budget_account_name( self ) -> str:
        if self.__budgetaccountname is not None:
            return self.__budgetaccountname

    @budget_account_name.setter
    def budget_account_name( self, value: str ):
        if value is not None:
            self.__budgetaccountname = value

    @property
    def data( self ) -> list:
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, value: list ):
        if isinstance( value, list ):
            self.__data = value

    @property
    def table( self ) -> DataFrame:
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, value: DataFrame ):
        if value is not None:
            self.__frame = value

    @property
    def fields( self ) -> list[ str ]:
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value: list[ str ] ):
        if value is not None:
            self.__fields = value


    def __init__( self, bfy: str, provider: Provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.AnnualCarryoverEstimates
        self.__bfy = bfy
        self.__fields = [ 'AnnualCarryoverEstimatesId',
                           'BudgetLevel',
                           'BFY',
                           'EFY',
                           'RpioCode',
                           'RpioName',
                           'AhCode',
                           'AhName',
                           'FundCode',
                           'FundName',
                           'OrgCode',
                           'AccountCode',
                           'ProgramProjectCode',
                           'ProgramProjectName',
                           'ProgramAreaCode',
                           'ProgramAreaName',
                           'BocCode',
                           'BocName',
                           'AvailableBalance',
                           'OpenCommitment',
                           'UnobligatedAuthority' ]

    def __str__( self ) -> str:
        if self.__fundcode is not None:
            return self.__fundcode

    def get_data( self  ) -> list[ Row ]:
        try:
            _source = self.__source
            _provider = self.__provider
            _names = [ 'BFY', 'EFY' ]
            _values = (self.__bfy, self.__efy)
            _dbconfig = DbConfig( _source, _provider )
            _sqlconfig = SqlConfig( names = _names, values = _values )
            _connection = Connection( self.__source )
            _sql = SqlStatement( _dbconfig, _sqlconfig )
            _sqlite = _connection.connect( )
            _cursor = _sqlite.cursor( )
            _query = _sql.get_query( )
            _db = _cursor.execute( _query )
            self.__data =  [ i for i in _db.fetchall( ) ]
            _cursor.close( )
            _sqlite.close( )
            return self.__data
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Reporting'
            _exc.cause = 'CarryoverEstimate'
            _exc.method = 'get_data( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def get_frame( self ) -> DataFrame:
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            _source = self.__source
            _data = BudgetData( _source )
            return _data.create_frame( )
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Reporting'
            _exc.cause = 'CarryoverEstimate'
            _exc.method = 'create_frame( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class JobsActCarryoverEstimate( ):
    '''
    Constructor:  JobsActCarryoverEstimate( bfy )

    Purpose:  Class defines object providing IIJA Carryover Estimate data for'''
    __source = None
    __provider = None
    __jobsactcarryoverestimatesid = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __rpioname = None
    __fundcode = None
    __fundname = None
    __amount = None
    __opencommitments = None
    __obligations = None
    __estimate = None
    __treasuryaccountcode = None
    __treasuryaccountname = None
    __budgetaccountcode = None
    __budgetaccountname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ) -> int:
        if self.__jobsactcarryoverestimatesid is not None:
            return self.__jobsactcarryoverestimatesid

    @id.setter
    def id( self, value: int ):
        if value is not None:
            self.__annualcarryoverestimatesid = value

    @property
    def bfy( self ) -> str:
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value: str ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ) -> str:
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value: str ):
        if value is not None:
            self.__efy = value

    @property
    def rpio_code( self ) -> str:
        if self.__rpiocode is not None:
            return self.__rpiocode

    @rpio_code.setter
    def rpio_code( self, value: str ):
        if value is not None:
            self.__rpiocode = value

    @property
    def rpio_name( self ) -> str:
        if self.__rpioname is not None:
            return self.__rpioname

    @rpio_code.setter
    def rpio_code( self, value: str ):
        if value is not None:
            self.__rpiocode = value

    @property
    def fund_code( self ) -> str:
        if self.__fundcode is not None:
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value: str ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund_name( self ) -> str:
        if self.__fundname is not None:
            return self.__fundname

    @fund_name.setter
    def fund_name( self, value: str ):
        if value is not None:
            self.__fundname = value

    @property
    def amount( self ) -> float:
        if self.__amount is not None:
            return self.__amount

    @amount.setter
    def amount( self, value: float ):
        if value is not None:
            self.__amount = value

    @property
    def available( self ) -> float:
        if self.__availablebalance is not None:
            return self.__availablebalance

    @available.setter
    def available( self, value: float ):
        if value is not None:
            self.__availablebalance = value

    @property
    def open_commitments( self ) -> float:
        if self.__opencommitments is not None:
            return self.__opencommitments

    @open_commitments.setter
    def open_commitments( self, value: float ):
        if value is not None:
            self.__opencommitments = value

    @property
    def obligations( self ) -> float:
        if self.__obligations is not None:
            return self.__obligations

    @obligations.setter
    def obligations( self, value: float ):
        if value is not None:
            self.__obligations = value

    @property
    def treasury_account_code( self ) -> str:
        if self.__treasuryaccountcode is not None:
            return self.__treasuryaccountcode

    @treasury_account_code.setter
    def treasury_account_code( self, value: str ):
        if value is not None:
            self.__treasuryaccountcode = value

    @property
    def treasury_account_name( self ) -> str:
        if self.__treasuryaccountname is not None:
            return self.__treasuryaccountname

    @treasury_account_name.setter
    def treasury_account_name( self, value: str ):
        if value is not None:
            self.__treasuryaccountname = value

    @property
    def budget_account_code( self ) -> str:
        if self.__budgetaccountcode is not None:
            return self.__budgetaccountcode

    @budget_account_code.setter
    def budget_account_code( self, value: str ):
        if value is not None:
            self.__budgetaccountcode = value

    @property
    def budget_account_name( self ) -> str:
        if self.__budgetaccountname is not None:
            return self.__budgetaccountname

    @budget_account_name.setter
    def budget_account_name( self, value: str ):
        if value is not None:
            self.__budgetaccountname = value

    @property
    def data( self ) -> list:
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, value: list ):
        if isinstance( value, list ):
            self.__data = value

    @property
    def table( self ) -> DataFrame:
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, value: DataFrame ):
        if value is not None:
            self.__frame = value

    @property
    def fields( self ) -> list[ str ]:
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value: list[ str ] ):
        if value is not None:
            self.__fields = value


    def __init__( self, bfy: str, provider: Provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.JobsActCarryoverEstimates
        self.__bfy = bfy
        self.__fields = [ 'CarryoverEstimatesId',
                           'BudgetLevel',
                           'BFY',
                           'EFY',
                           'RpioCode',
                           'RpioName',
                           'AhCode',
                           'AhName',
                           'FundCode',
                           'FundName',
                           'OrgCode',
                           'AccountCode',
                           'ProgramProjectCode',
                           'ProgramProjectName',
                           'ProgramAreaCode',
                           'ProgramAreaName',
                           'BocCode',
                           'BocName',
                           'AvailableBalance',
                           'OpenCommitment',
                           'UnobligatedAuthority' ]

    def __str__( self ) -> str:
        if self.__fundcode is not None:
            return self.__fundcode

    def get_data( self  ) -> list[ Row ]:
        try:
            _source = self.__source
            _provider = self.__provider
            _names = [ 'BFY', 'EFY' ]
            _values = (self.__bfy, self.__efy)
            _dbconfig = DbConfig( _source, _provider )
            _sqlconfig = SqlConfig( names = _names, values = _values )
            _connection = Connection( self.__source )
            _sql = SqlStatement( _dbconfig, _sqlconfig )
            _sqlite = _connection.connect( )
            _cursor = _sqlite.cursor( )
            _query = _sql.get_query( )
            _db = _cursor.execute( _query )
            self.__data =  [ i for i in _db.fetchall( ) ]
            _cursor.close( )
            _sqlite.close( )
            return self.__data
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Reporting'
            _exc.cause = 'CarryoverEstimate'
            _exc.method = 'get_data( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def get_frame( self ) -> DataFrame:
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            _source = self.__source
            _data = BudgetData( _source )
            return _data.create_frame( )
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Reporting'
            _exc.cause = 'CarryoverEstimate'
            _exc.method = 'create_frame( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class MonthlyActual( ):
    '''
    Constructor:   Actual( bfy = None, fund = None, pvdr = Provider.SQLite )

    Purpose:  Class defines object representing expenditure data'''
    __source = None
    __provider = None
    __monthlyactualsid = None
    __bfy = None
    __efy = None
    __fundcode = None
    __fundname = None
    __rpiocode = None
    __rpioname = None
    __ahcode = None
    __ahname = None
    __appropriationcode = None
    __appropriationname = None
    __subappropriationcode = None
    __subappropriationname = None
    __orgcode = None
    __orgname = None
    __accountcode = None
    __programprojectcode = None
    __programprojectname = None
    __boccode = None
    __bocname = None
    __netoutlays = None
    __grossoutlays = None
    __obligations = None
    __treasuryaccountcode = None
    __treasuryaccountname = None
    __budgetaccountcode = None
    __budgetaccountname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ) -> int:
        if self.__monthlyactualsid is not None:
            return self.__monthlyactualsid

    @id.setter
    def id( self, value: int ):
        if value is not None:
            self.__id = value

    @property
    def bfy( self ) -> str:
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value: str ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ) -> str:
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value: str ):
        if value is not None:
            self.__efy = value

    @property
    def fund_code( self ) -> str:
        if self.__fundcode is not None:
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value: str ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund_name( self ) -> str:
        if self.__fundname is not None:
            return self.__fundname

    @fund_name.setter
    def fund_name( self, value: str ):
        if value is not None:
            self.__fundname = value

    @property
    def rpio_code( self ) -> str:
        if self.__rpiocode is not None:
            return self.__rpiocode

    @rpio_code.setter
    def rpio_code( self, value: str ):
        if value is not None:
            self.__rpiocode = value

    @property
    def rpio_name( self ) -> str:
        if self.__rpioname is not None:
            return self.__rpioname

    @rpio_code.setter
    def rpio_code( self, value: str ):
        if value is not None:
            self.__rpiocode = value

    @property
    def ah_code( self ) -> str:
        if self.__ahcode is not None:
            return self.__ahcode

    @ah_code.setter
    def ah_code( self, value: str ):
        if value is not None:
            self.__ahcode = value

    @property
    def ah_name( self ) -> str:
        if self.__ahname is not None:
            return self.__ahname

    @ah_name.setter
    def ah_name( self, value: str ):
        if value is not None:
            self.__ahname = value

    @property
    def org_code( self ) -> str:
        if self.__orgcode is not None:
            return self.__orgcode

    @org_code.setter
    def org_code( self, value: str ):
        if value is not None:
            self.__orgcode = value

    @property
    def org_name( self  ):
        if self.__orgname is not None:
            return self.__orgname

    @org_name.setter
    def org_name( self, value  ):
        if value is not None:
            self.__orgname = value

    @property
    def account_code( self ) -> str:
        if self.__accountcode is not None:
            return self.__accountcode

    @account_code.setter
    def account_code( self, value: str ):
        if value is not None:
            self.__accountcode = value

    @property
    def boc_code( self ) -> str:
        if self.__boccode is not None:
            return self.__boccode

    @boc_code.setter
    def boc_code( self, value: str ):
        if value is not None:
            self.__boccode = value

    @property
    def boc_name( self ) -> str:
        if self.__bocname is not None:
            return self.__bocname

    @boc_name.setter
    def boc_name( self, value: str ):
        if value is not None:
            self.__bocname = value

    @property
    def gross_outlays( self ) -> str:
        if self.__grossoutlays is not None:
            return self.__grossoutlays

    @gross_outlays.setter
    def gross_outlays( self, value: str ):
        if value is not None:
            self.__grossoutlays = value

    @property
    def net_outlays( self ) -> str:
        if self.__netoutlays is not None:
            return self.__netoutlays

    @net_outlays.setter
    def net_outlays( self, value: str ):
        if value is not None:
            self.__netoutlays  = value

    @property
    def obligations( self ) -> float:
        if self.__obligations is not None:
            return self.__obligations

    @obligations.setter
    def obligations( self, value: float ):
        if value is not None:
            self.__obligations = value

    @property
    def program_project_code( self ) -> str:
        if self.__programprojectcode is not None:
            return self.__programprojectcode

    @program_project_code.setter
    def program_project_code( self, value: str ):
        if value is not None:
            self.__programprojectcode = value

    @property
    def program_project_name( self ) -> str:
        if self.__programprojectname is not None:
            return self.__programprojectname

    @program_project_name.setter
    def program_project_name( self, value: str ):
        if value is not None:
            self.__programprojectname = value

    @property
    def treasury_account_code( self ) -> str:
        if self.__treasuryaccountcode is not None:
            return self.__treasuryaccountcode

    @treasury_account_code.setter
    def treasury_account_code( self, value: str ):
        if value is not None:
            self.__treasuryaccountcode = value

    @property
    def treasury_account_name( self ) -> str:
        if self.__treasuryaccountname is not None:
            return self.__treasuryaccountname

    @treasury_account_name.setter
    def treasury_account_name( self, value: str ):
        if value is not None:
            self.__treasuryaccountname = value

    @property
    def budget_account_code( self ) -> str:
        if self.__budgetaccountcode is not None:
            return self.__budgetaccountcode

    @budget_account_code.setter
    def budget_account_code( self, value: str ):
        if value is not None:
            self.__budgetaccountcode = value

    @property
    def budget_account_name( self ) -> str:
        if self.__budgetaccountname is not None:
            return self.__budgetaccountname

    @budget_account_name.setter
    def budget_account_name( self, value: str ):
        if value is not None:
            self.__budgetaccountname = value

    @property
    def fields( self ) -> list[ str ]:
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value: list[ str ] ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy = None, fund = None, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.MonthlyActuals
        self.__bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
        self.__fundcode = fund if isinstance(fund, str ) and fund != '' else None
        self.__fields = [ 'ActualsId',
                           'BFY',
                           'EFY',
                           'RpioCode',
                           'RpioName',
                           'AhCode',
                           'AhName',
                           'FundCode',
                           'FundName',
                           'AppropriationCode',
                           'AppropriationName',
                           'SubAppropriationCode',
                           'SubAppropriationName',
                           'OrgCode',
                           'OrgName',
                           'AccountCode',
                           'ProgramProjectCode',
                           'ProgramProjectName',
                           'RpioActivityCode',
                           'RpioActivityName',
                           'BocCode',
                           'BocName',
                           'ULO',
                           'Obligation',
                           'Balance',
                           'ProgramAreaCode',
                           'ProgramAreaName',
                           'GoalCode',
                           'GoalName',
                           'ObjectiveCode',
                           'ObjectiveName' ]

    def get_data( self  ) -> list[ Row ]:
        try:
            _source = self.__source
            _provider = self.__provider
            _names = [ 'BFY', 'FundCode' ]
            _values = (self.__bfy, self.__fundcode)
            _dbconfig = DbConfig( _source, _provider )
            _sqlconfig = SqlConfig( names = _names, values = _values )
            _connection = Connection( self.__source )
            _sql = SqlStatement( _dbconfig, _sqlconfig )
            _sqlite = _connection.connect( )
            _cursor = _sqlite.cursor( )
            _query = _sql.get_query( )
            _db = _cursor.execute( _query )
            self.__data =  [ i for i in _db.fetchall( ) ]
            _cursor.close( )
            _sqlite.close( )
            return self.__data
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Ninja'
            _exc.cause = 'Actual'
            _exc.method = 'get_data( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def get_frame( self ) -> DataFrame:
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            _source = self.__source
            _data = BudgetData( _source )
            return _data.create_frame( )
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Ninja'
            _exc.cause = 'Actual'
            _exc.method = 'create_frame( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class MonthlyOutlay( ):
    '''
    Constructor:  MonthlyOutlay( bfy, efy, main )

    Purpose;  Class defines object providing OMB outlay data'''
    __source = None
    __provider = None
    __monthlyoutlaysid = None
    __reportyear = None
    __bfy = None
    __efy = None
    __linenumber = None
    __linename = None
    __taxationcode = None
    __treasuryagencycode = None
    __subaccountcode = None
    __january = None
    __february = None
    __march = None
    __april = None
    __may = None
    __june = None
    __july = None
    __august = None
    __september = None
    __october = None
    __november = None
    __december = None
    __treasuryaccountcode = None
    __treasuryaccountname = None
    __budgetaccountcode = None
    __budgetaccountname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ) -> int:
        if self.__monthlyoutlaysid is not None:
            return self.__monthlyoutlaysid

    @id.setter
    def id( self, value: int ):
        if value is not None:
            self.__monthlyoutlaysid = value

    @property
    def line_number( self ) -> str:
        if self.__linenumber is not None:
            return self.__linenumber

    @line_number.setter
    def line_number( self, value: str ):
        if value is not None:
            self.__linenumber = value

    @property
    def line_name( self ) -> str:
        if self.__linename is not None:
            return self.__linename

    @line_name.setter
    def line_name( self, value: str ):
        if value is not None:
            self.__linename = value

    @property
    def bfy( self ) -> str:
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value: str ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ) -> str:
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value: str ):
        if value is not None:
            self.__efy = value

    @property
    def taxation_code( self ) -> str:
        if self.__taxationcode is not None:
            return self.__taxationcode

    @taxation_code.setter
    def taxation_code( self, value: str ):
        if value is not None:
            self.__taxationcode = value

    @property
    def treasury_agency_code( self ) -> str:
        if self.__treasuryagencycode is not None:
            return self.__treasuryagencycode

    @treasury_agency_code.setter
    def treasury_agency_code( self, value: str ):
        if value is not None:
            self.__treasuryagencycode = value

    @property
    def subaccount_code( self ) -> str:
        if self.__subaccountcode is not None:
            return self.__subaccountcode

    @subaccount_code.setter
    def subaccount_code( self, value: str ):
        if value is not None:
            self.__subaccountcode = value

    @property
    def treasury_account_code( self ) -> str:
        if self.__treasuryaccountcode is not None:
            return self.__treasuryaccountcode

    @treasury_account_code.setter
    def treasury_account_code( self, value: str ):
        if value is not None:
            self.__treasuryaccountcode = value

    @property
    def treasury_account_name( self ) -> str:
        if self.__treasuryaccountname is not None:
            return self.__treasuryaccountname

    @treasury_account_name.setter
    def treasury_account_name( self, value: str ):
        if value is not None:
            self.__treasuryaccountname = value

    @property
    def budget_account_code( self ) -> str:
        if self.__budgetaccountcode is not None:
            return self.__budgetaccountcode

    @budget_account_code.setter
    def budget_account_code( self, value: str ):
        if value is not None:
            self.__budgetaccountcode = value

    @property
    def budget_account_name( self ) -> str:
        if self.__budgetaccountname is not None:
            return self.__budgetaccountname

    @budget_account_name.setter
    def budget_account_name( self, value: str ):
        if value is not None:
            self.__budgetaccountname = value

    @property
    def fields( self ) -> list[ str ]:
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value: list[ str ] ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy, efy, account, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.MonthlyOutlays
        self.__bfy = bfy
        self.__efy = efy
        self.__budgetaccountcode = account
        self.__fields = [ 'MonthlyOutlaysId',
                          'FiscalYear',
                          'LineNumber',
                          'LineTitle',
                          'TaxationCode',
                          'TreasuryAgency',
                          'TreasuryAccount',
                          'SubAccount',
                          'BFY',
                          'EFY',
                          'OmbAgency',
                          'OmbBureau',
                          'OmbAccount',
                          'AgencySequence',
                          'BureauSequence',
                          'AccountSequence',
                          'AgencyTitle',
                          'BureauTitle',
                          'OmbAccountTitle',
                          'TreasuryAccountTitle',
                          'October',
                          'November',
                          'December',
                          'January',
                          'Feburary',
                          'March',
                          'April',
                          'May',
                          'June',
                          'July',
                          'August',
                          'September' ]

    def get_data( self  ) -> list[ Row ]:
        try:
            _source = self.__source
            _provider = self.__provider
            _names = [ 'BFY', 'EFY', 'OmbAccountCode', ]
            _values = (self.__bfy, self.__efy, self.__budgetaccountcode)
            _dbconfig = DbConfig( _source, _provider )
            _sqlconfig = SqlConfig( names = _names, values = _values )
            _connection = Connection( self.__source )
            _sql = SqlStatement( _dbconfig, _sqlconfig )
            _sqlite = _connection.connect( )
            _cursor = _sqlite.cursor( )
            _query = _sql.get_query( )
            _db = _cursor.execute( _query )
            self.__data =  [ i for i in _db.fetchall( ) ]
            _cursor.close( )
            _sqlite.close( )
            return self.__data
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Reporting'
            _exc.cause = 'MonthlyOutlay'
            _exc.method = 'create_frame( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def get_frame( self ) -> DataFrame:
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            _source = self.__source
            _data = BudgetData( _source )
            return _data.create_frame( )
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Reporting'
            _exc.cause = 'MonthlyOutlay'
            _exc.method = 'create_frame( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class NationalProgram( ):
    '''
    Constructor:  NationalProgram( code: str, pvdr = Provider.SQLite )

    Purpose:  Class defines object representing the NationalProgram Class'''
    __source = None
    __provider = None
    __nationalprogramsid = None
    __code = None
    __name = None
    __rpio = None
    __title = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ) -> int:
        if self.__nationalprogramsid is not None:
            return self.__nationalprogramsid

    @id.setter
    def id( self, value: int ):
        if value is not None:
            self.__nationalprogramsid = value

    @property
    def code( self ) -> str:
        if  self.__code is not None:
            return self.__code

    @code.setter
    def code( self, value: str ):
        if value is not None:
            self.__code = value

    @property
    def name( self ) -> str:
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, value: str ):
        if value is not None:
            self.__name = value

    @property
    def rpio( self ) -> str:
        if self.__rpio is not None:
            return self.__rpio

    @rpio.setter
    def rpio( self, value: str ):
        if value is not None:
            self.__rpio = value

    @property
    def title( self ) -> str:
        if self.__title is not None:
            return self.__title

    @title.setter
    def title( self, value: str ):
        if value is not None:
            self.__title = value

    @property
    def data( self ) -> list:
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, value: list ):
        if isinstance( value, list ):
            self.__data = value

    @property
    def table( self ) -> DataFrame:
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, value: DataFrame ):
        if value is not None:
            self.__frame = value

    @property
    def fields( self ) -> list[ str ]:
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value: list[ str ] ):
        if value is not None:
            self.__fields = value

    def __init__( self, code: str, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.NationalPrograms
        self.__code = code
        self.__fields = [ 'NationalProgramsId',
                          'Code',
                          'Name',
                          'RpioCode',
                          'Title' ]

    def __str__( self ) -> str:
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code

    def get_data( self  ) -> list[ Row ]:
        try:
            _source = self.__source
            _provider = self.__provider
            _names = [ 'Code', ]
            _values = (self.__code,)
            _dbconfig = DbConfig( _source, _provider )
            _sqlconfig = SqlConfig( names = _names, values = _values )
            _connection = Connection( self.__source )
            _sql = SqlStatement( _dbconfig, _sqlconfig )
            _sqlite = _connection.connect( )
            _cursor = _sqlite.cursor( )
            _query = _sql.get_query( )
            _db = _cursor.execute( _query )
            self.__data =  [ i for i in _db.fetchall( ) ]
            _cursor.close( )
            _sqlite.close( )
            return self.__data
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Execution'
            _exc.cause = 'NationalProgram'
            _exc.method = 'get_data( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def get_frame( self ) -> DataFrame:
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            _source = self.__source
            _data = BudgetData( _source )
            return _data.create_frame( )
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Execution'
            _exc.cause = 'NationalProgram'
            _exc.method = 'create_frame( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class Objective( ):
    '''
    Constructor:  Objective( code: str, pvdr: Provider = Provider.SQLite )


    Purpose: Class defines object representing the Objective Class'''
    __source = None
    __provider = None
    __objectivesid = None
    __code = None
    __name = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ) -> int:
        if  self.__objectivesid is not None:
            return self.__objectivesid

    @id.setter
    def id( self, value: int ):
        if value is not None:
            self.__objectivesid = value

    @property
    def code( self ) -> str:
        if  self.__code is not None:
            return self.__code

    @code.setter
    def code( self, value: str ):
        if value is not None:
            self.__code = value

    @property
    def name( self ) -> str:
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, value: str ):
        if value is not None:
            self.__name = value

    @property
    def data( self ) -> list:
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, value: list ):
        if value is not None:
            self.__data = value

    @property
    def table( self ) -> DataFrame:
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, value: DataFrame ):
        if value is not None:
            self.__frame = value

    @property
    def fields( self ) -> list[ str ]:
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value: list[ str ] ):
        if value is not None:
            self.__fields = value

    def __init__( self, code: str, provider: Provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.Objectives
        self.__code = code
        self.__fields = [ 'ObjectivesId',
                          'Code',
                          'Name',
                          'Title' ]

    def __str__( self ) -> str:
        if isinstance( self.__code, str ) and self.__code != '':
            return self.__code

    def get_data( self  ) -> list[ Row ]:
        try:
            _source = Source.Objectives
            _provider = Provider.SQLite
            _names = [ 'Code', ]
            _values = (self.__code,)
            _dbconfig = DbConfig( _source, _provider )
            _sqlconfig = SqlConfig( names = _names, values = _values )
            _connection = Connection( self.__source )
            _sql = SqlStatement( _dbconfig, _sqlconfig )
            _sqlite = _connection.connect( )
            _cursor = _sqlite.cursor( )
            _query = _sql.get_query( )
            _db = _cursor.execute( _query )
            self.__data =  [ i for i in _db.fetchall( ) ]
            _cursor.close( )
            _sqlite.close( )
            return self.__data
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Execution'
            _exc.cause = 'Objective'
            _exc.method = 'get_data( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def get_frame( self ) -> DataFrame:
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            _source = self.__source
            _data = BudgetData( _source )
            return _data.create_frame( )
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Execution'
            _exc.cause = 'Objective'
            _exc.method = 'create_frame( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class Organization( ):
    '''
    Constructor:  Organization( code: str, pvdr: Provider = Provider.SQLite  )

    Purpose: Class defines object representing the Organization Codes'''
    __source = None
    __provider = None
    __organizationsid = None
    __code = None
    __name = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ) -> int:
        if self.__organizationsid is not None:
            return self.__organizationsid

    @id.setter
    def id( self, id ):
        if isinstance( id, int ):
            self.__organizationsid = id

    @property
    def code( self ) -> str:
        if  self.__code is not None:
            return self.__code

    @code.setter
    def code( self, code ):
        if code is not None:
            self.__code = code

    @property
    def name( self ) -> str:
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, name ):
        if  name is not None:
            self.__name = name

    @property
    def data( self ) -> list:
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, cache ):
        if list is not None:
            self.__data = cache

    @property
    def table( self ) -> DataFrame:
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, frame ):
        if isinstance( frame, DataFrame ):
            self.__frame = frame

    @property
    def fields( self ) -> list[ str ]:
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value: list[ str ] ):
        if value is not None:
            self.__fields = value

    def __init__( self, code: str, provider: Provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.Organizations
        self.__code = code
        self.__fields = [ 'OrganizationsId',
                          'Code',
                          'Name' ]

    def __str__( self ) -> str:
        if self.__code is not None:
            return self.__code

    def get_data( self  ) -> list[ Row ]:
        try:
            _source = self.__source
            _provider = self.__provider
            _names = [ 'Code', ]
            _values = (self.__code,)
            _dbconfig = DbConfig( _source, _provider )
            _sqlconfig = SqlConfig( names = _names, values = _values )
            _connection = Connection( self.__source )
            _sql = SqlStatement( _dbconfig, _sqlconfig )
            _sqlite = _connection.connect( )
            _cursor = _sqlite.cursor( )
            _query = _sql.get_query( )
            _db = _cursor.execute( _query )
            self.__data =  [ i for i in _db.fetchall( ) ]
            _cursor.close( )
            _sqlite.close( )
            return self.__data
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Execution'
            _exc.cause = 'Organization'
            _exc.method = 'get_data( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class OperatingPlan( ):
    '''
    Constructor:  OperatingPlan( bfy, efy, treas, pvdr = Provider.SQLite )

    Purpose: Class defining object representing Operating plan allocations'''
    __operatingplansid = None
    __source = None
    __provider = None
    __operatingplansid = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __rpioname = None
    __fundcode = None
    __fundname = None
    __ahcode = None
    __ahname = None
    __orgcode = None
    __orgname = None
    __accountcode = None
    __boccode = None
    __bocname = None
    __rccode = None
    __rcname = None
    __amount = None
    __programprojectcode = None
    __programprojectname = None
    __programareacode = None
    __programareaname = None
    __goalcode = None
    __goalname = None
    __objectivecode = None
    __objectivename = None
    __npmcode = None
    __npmname = None
    __treasuryaccountcode = None
    __treasuryaccountname = None
    __budgetaccountcode = None
    __budgetaccountname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ) -> int:
        if self.__operatingplansid is not None:
            return self.__operatingplansid

    @id.setter
    def id( self, value: int ):
        if value is not None:
            self.__operatingplansid = value

    @property
    def bfy( self ) -> str:
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value: str ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ) -> str:
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value: str ):
        if value is not None:
            self.__efy = value

    @property
    def rpio_code( self ) -> str:
        if self.__rpiocode is not None:
            return self.__rpiocode

    @rpio_code.setter
    def rpio_code( self, value: str ):
        if value is not None:
            self.__rpiocode = value

    @property
    def rpio_name( self ) -> str:
        if self.__rpioname is not None:
            return self.__rpioname

    @rpio_name.setter
    def rpio_name( self, value: str ):
        if value is not None:
            self.__rpioname = value

    @property
    def ah_code( self ) -> str:
        if self.__ahcode is not None:
            return self.__ahcode

    @ah_code.setter
    def ah_code( self, value: str ):
        if value is not None:
            self.__ahcode = value

    @property
    def ah_name( self ) -> str:
        if self.__ahname is not None:
            return self.__ahname

    @ah_name.setter
    def ah_name( self, value: str ):
        if value is not None:
            self.__ahname = value

    @property
    def fund_code( self ) -> str:
        if self.__fundcode is not None:
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value: str ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund_name( self ) -> str:
        if self.__fundname is not None:
            return self.__fundname

    @fund_name.setter
    def fund_name( self, value: str ):
        if value is not None:
            self.__fundname = value

    @property
    def org_code( self ) -> str:
        if self.__orgcode is not None:
            return self.__orgcode

    @org_code.setter
    def org_code( self, value: str ):
        if value is not None:
            self.__orgcode = value

    @property
    def org_name( self  ):
        if self.__orgname is not None:
            return self.__orgname

    @org_name.setter
    def org_name( self, value  ):
        if value is not None:
            self.__orgname = value

    @property
    def account_code( self ) -> str:
        if self.__accountcode is not None:
            return self.__accountcode

    @account_code.setter
    def account_code( self, value: str ):
        if value is not None:
            self.__accountcode = value

    @property
    def boc_code( self ) -> str:
        if self.__boccode is not None:
            return self.__boccode

    @boc_code.setter
    def boc_code( self, value: str ):
        if value is not None:
            self.__boccode = value

    @property
    def boc_name( self ) -> str:
        if self.__bocname is not None:
            return self.__bocname

    @boc_name.setter
    def boc_name( self, value: str ):
        if value is not None:
            self.__bocname = value

    @property
    def rc_code( self ) -> str:
        if self.__rccode is not None:
            return self.__rccode

    @rc_code.setter
    def rc_code( self, value: str ):
        if value is not None:
            self.__rccode = value

    @property
    def rc_name( self ) -> str:
        if self.__rcname is not None:
            return self.__rcname

    @rc_name.setter
    def rc_name( self, value: str ):
        if value is not None:
            self.__rcname = value

    @property
    def amount( self ) -> float:
        if self.__amount is not None:
            return self.__amount

    @amount.setter
    def amount( self, value: float ):
        if value is not None:
            self.__amount = value

    @property
    def program_project_code( self ) -> str:
        if self.__programprojectcode is not None:
            return self.__programprojectcode

    @program_project_code.setter
    def program_project_code( self, value: str ):
        if value is not None:
            self.__programprojectcode = value

    @property
    def program_project_name( self ) -> str:
        if self.__programprojectname is not None:
            return self.__programprojectname

    @program_project_name.setter
    def program_project_name( self, value: str ):
        if value is not None:
            self.__programprojectname = value

    @property
    def program_area_code( self ) -> str:
        if self.__programareacode is not None:
            return self.__programareacode

    @program_area_code.setter
    def program_area_code( self, value: str ):
        if value is not None:
            self.__programareacode = value

    @property
    def program_area_name( self ) -> str:
        if self.__programareaname is not None:
            return self.__programareaname

    @program_area_name.setter
    def program_area_name( self, value: str ):
        if value is not None:
            self.__programareaname = value

    @property
    def goal_code( self ) -> str:
        if self.__goalcode is not None:
            return self.__goalcode

    @goal_code.setter
    def goal_code( self, value: str ):
        if value is not None:
            self.__goalcode = value

    @property
    def goal_name( self ) -> str:
        if self.__goalname is not None:
            return self.__goalname

    @goal_name.setter
    def goal_name( self, value: str ):
        if value is not None:
            self.__goalname = value

    @property
    def objective_code( self ) -> str:
        if self.__objectivecode is not None:
            return self.__objectivecode

    @objective_code.setter
    def objective_code( self, value: str ):
        if value is not None:
            self.__objectivecode = value

    @property
    def objective_name( self ) -> str:
        if self.__objectivename is not None:
            return self.__objectivename

    @objective_name.setter
    def objective_name( self, value: str ):
        if value is not None:
            self.__objectivename = value

    @property
    def npm_code( self ) -> str:
        if self.__npmcode is not None:
            return self.__npmcode

    @npm_code.setter
    def npm_code( self, value: str ):
        if value is not None:
            self.__npmcode = value

    @property
    def npm_name( self ) -> str:
        if self.__npmname is not None:
            return self.__npmname

    @property
    def fields( self ) -> list[ str ]:
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value: list[ str ] ):
        if value is not None:
            self.__fields = value

    @npm_name.setter
    def npm_name( self, value: str ):
        if value is not None:
            self.__npmname = value

    @property
    def treasury_account_code( self ) -> str:
        if self.__treasuryaccountcode is not None:
            return self.__treasuryaccountcode

    @treasury_account_code.setter
    def treasury_account_code( self, value: str ):
        if value is not None:
            self.__treasuryaccountcode = value

    @property
    def treasury_account_name( self ) -> str:
        if self.__treasuryaccountname is not None:
            return self.__treasuryaccountname

    @treasury_account_name.setter
    def treasury_account_name( self, value: str ):
        if value is not None:
            self.__treasuryaccountname = value

    @property
    def budget_account_code( self ) -> str:
        if self.__budgetaccountcode is not None:
            return self.__budgetaccountcode

    @budget_account_code.setter
    def budget_account_code( self, value: str ):
        if value is not None:
            self.__budgetaccountcode = value

    @property
    def budget_account_name( self ) -> str:
        if self.__budgetaccountname is not None:
            return self.__budgetaccountname

    @budget_account_name.setter
    def budget_account_name( self, value: str ):
        if value is not None:
            self.__budgetaccountname = value

    def __init__( self, bfy: str, fund: str, provider: Provider = Provider.SQLite ):
        self.__source = Source.OperatingPlans
        self.__provider = provider
        self.__bfy = bfy
        self.__fundcode = fund
        self.__fields = [ 'OperatingPlansId', 'RpioCode', 'RpioName', 'BFY', 'EFY', 'AhCode',
                           'FundCode', 'OrgCode', 'AccountCode', 'RcCode', 'BocCode', 'BocName',
                           'Amount', 'ITProjectCode', 'ProjectCode', 'ProjectName', 'NpmCode',
                           'ProjectTypeName', 'ProjectTypeCode', 'ProgramProjectCode', 'ProgramAreaCode',
                           'NpmName', 'AhName', 'FundName', 'OrgName', 'RcName', 'ProgramProjectName',
                           'ActivityCode', 'ActivityName', 'LocalCode', 'LocalCodeName', 'ProgramAreaName',
                           'CostAreaCode', 'CostAreaName', 'GoalCode', 'GoalName',
                           'ObjectiveCode', 'ObjectiveName' ]

    def get_data( self  ) -> list[ Row ]:
        try:
            _names = [ 'BFY', 'FundCode' ]
            _values = ( self.__bfy, self.__fundcode )
            _dbconfig = DbConfig( self.__source, self.__provider )
            _sqlconfig = SqlConfig( names = _names, values = _values )
            _connection = Connection( self.__source )
            _sql = SqlStatement( _dbconfig, _sqlconfig )
            _sqlite = _connection.connect( )
            _cursor = _sqlite.cursor( )
            _query = _sql.get_query( )
            _db = _cursor.execute( _query )
            self.__data =  [ i for i in _db.fetchall( ) ]
            _cursor.close( )
            _sqlite.close( )
            return self.__data
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Ninja'
            _exc.cause = 'OperatingPlan'
            _exc.method = 'get_data( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def get_frame( self ) -> DataFrame:
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            _source = self.__source
            _data = BudgetData( _source )
            return _data.create_frame( )
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Ninja'
            _exc.cause = 'OperatingPlan'
            _exc.method = 'create_frame( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class OpenCommitment( ):
    '''
    Constructor:  OpenCommitment( bfy: str, efy: str, fund: str,
                  account: str, boc: str, pvdr: Provider = Provider.SQLite )

    Purpose: Class defines object providing OpenCommitment data.'''
    __source = None
    __provider = None
    __opencommitmentsid = None
    __obligationsid = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __rpioname = None
    __fundcode = None
    __fundname = None
    __ahcode = None
    __ahname = None
    __orgcode = None
    __orgname = None
    __accountcode = None
    __programprojectname = None
    __boccode = None
    __bocname = None
    __rccode = None
    __rcname = None
    __documenttype = None
    __documentnumber = None
    __documentcontrolnumber = None
    __referencedocumentnumber = None
    __programprojectcode = None
    __programareacode = None
    __programareaname = None
    __processeddate = None
    __lastactivitydate = None
    __age = None
    __vendorcode = None
    __vendorage = None
    __foccode = None
    __focname = None
    __amount = None
    _posted = None
    __goalcode = None
    __goalname = None
    __objectivecode = None
    __objectivename = None
    __npmcode = None
    __npmname = None
    __treasuryaccountcode = None
    __treasuryaccountname = None
    __budgetaccountcode = None
    __budgetaccountname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ) -> int:
        if self.__opencommitmentsid is not None:
            return self.__opencommitmentsid

    @id.setter
    def id( self, value: int ):
        if value is not None:
            self.__opencommitmentsid = value

    @property
    def bfy( self ) -> str:
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value: str ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ) -> str:
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value: str ):
        if value is not None:
            self.__efy = value

    @property
    def rpio_code( self ) -> str:
        if self.__rpiocode is not None:
            return self.__rpiocode

    @rpio_code.setter
    def rpio_code( self, value: str ):
        if value is not None:
            self.__rpiocode = value

    @property
    def rpio_name( self ) -> str:
        if self.__rpioname is not None:
            return self.__rpioname

    @rpio_code.setter
    def rpio_code( self, value: str ):
        if value is not None:
            self.__rpiocode = value

    @property
    def ah_code( self ) -> str:
        if self.__ahcode is not None:
            return self.__ahcode

    @ah_code.setter
    def ah_code( self, value: str ):
        if value is not None:
            self.__ahcode = value

    @property
    def ah_name( self ) -> str:
        if self.__ahname is not None:
            return self.__ahname

    @ah_name.setter
    def ah_name( self, value: str ):
        if value is not None:
            self.__ahname = value

    @property
    def fund_code( self ) -> str:
        if self.__fundcode is not None:
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value: str ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund_name( self ) -> str:
        if self.__fundname is not None:
            return self.__fundname

    @fund_name.setter
    def fund_name( self, value: str ):
        if value is not None:
            self.__fundname = value

    @property
    def org_code( self ) -> str:
        if self.__orgcode is not None:
            return self.__orgcode

    @org_code.setter
    def org_code( self, value: str ):
        if value is not None:
            self.__orgcode = value

    @property
    def org_name( self  ):
        if self.__orgname is not None:
            return self.__orgname

    @org_name.setter
    def org_name( self, value  ):
        if value is not None:
            self.__orgname = value

    @property
    def account_code( self ) -> str:
        if self.__accountcode is not None:
            return self.__accountcode

    @account_code.setter
    def account_code( self, value: str ):
        if value is not None:
            self.__accountcode = value

    @property
    def boc_code( self ) -> str:
        if self.__boccode is not None:
            return self.__boccode

    @boc_code.setter
    def boc_code( self, value: str ):
        if value is not None:
            self.__boccode = value

    @property
    def boc_name( self ) -> str:
        if self.__bocname is not None:
            return self.__bocname

    @boc_name.setter
    def boc_name( self, value: str ):
        if value is not None:
            self.__bocname = value

    @property
    def rc_code( self ) -> str:
        if self.__rccode is not None:
            return self.__rccode

    @rc_code.setter
    def rc_code( self, value: str ):
        if value is not None:
            self.__rccode = value

    @property
    def rc_name( self ) -> str:
        if self.__rcname is not None:
            return self.__rcname

    @rc_name.setter
    def rc_name( self, value: str ):
        if value is not None:
            self.__rcname = value

    @property
    def amount( self ) -> float:
        if self.__amount is not None:
            return self.__amount

    @amount.setter
    def amount( self, value: float ):
        if value is not None:
            self.__amount = value

    @property
    def budgeted( self ) -> float:
        if self.__budgeted is not None:
            return self.__budgeted

    @budgeted.setter
    def budgeted( self, value: float ):
        if value is not None:
            self.__budgeted = value

    @property
    def posted( self ) -> float:
        if self.__posted is not None:
            return self.__posted

    @posted.setter
    def posted( self, value: float ):
        if self.__posted is not None:
            self.__posted = value

    @property
    def open_commitments( self ) -> float:
        if self.__opencommitments is not None:
            return self.__opencommitments

    @open_commitments.setter
    def open_commitments( self, value: float ):
        if value is not None:
            self.__opencommitments = value

    @property
    def obligations( self ) -> float:
        if self.__obligations is not None:
            return self.__obligations

    @obligations.setter
    def obligations( self, value: float ):
        if value is not None:
            self.__obligations = value

    @property
    def unliquidated_obligations( self ) -> str:
        if self.__unliquidatedobligations is not None:
            return self.__unliquidatedobligations

    @unliquidated_obligations.setter
    def unliquidated_obligations( self, value: str ):
        if value is not None:
            self.__unliquidatedobligations = value

    @property
    def expenditures( self ) -> str:
        if self.__expenditures is not None:
            return self.__expenditures

    @expenditures.setter
    def expenditures( self, value: str ):
        if value is not None:
            self.__expenditures = value

    @property
    def used( self ) -> str:
        if self.__used is not None:
            return self.__used

    @used.setter
    def used( self, value: str ):
        if value is not None:
            self.__used = value

    @property
    def available( self ) -> float:
        if self.__avaialable is not None:
            return self.__avaialable

    @available.setter
    def available( self, value: float ):
        if value is not None:
            self.__avaialable = value

    @property
    def program_project_code( self ) -> str:
        if self.__programprojectcode is not None:
            return self.__programprojectcode

    @program_project_code.setter
    def program_project_code( self, value: str ):
        if value is not None:
            self.__programprojectcode = value

    @property
    def program_project_name( self ) -> str:
        if self.__programprojectname is not None:
            return self.__programprojectname

    @program_project_name.setter
    def program_project_name( self, value: str ):
        if value is not None:
            self.__programprojectname = value

    @property
    def program_area_code( self ) -> str:
        if self.__programareacode is not None:
            return self.__programareacode

    @program_area_code.setter
    def program_area_code( self, value: str ):
        if value is not None:
            self.__programareacode = value

    @property
    def program_area_name( self ) -> str:
        if self.__programareaname is not None:
            return self.__programareaname

    @program_area_name.setter
    def program_area_name( self, value: str ):
        if value is not None:
            self.__programareaname = value

    @property
    def goal_code( self ) -> str:
        if self.__goalcode is not None:
            return self.__goalcode

    @goal_code.setter
    def goal_code( self, value: str ):
        if value is not None:
            self.__goalcode = value

    @property
    def goal_name( self ) -> str:
        if self.__goalname is not None:
            return self.__goalname

    @goal_name.setter
    def goal_name( self, value: str ):
        if value is not None:
            self.__goalname = value

    @property
    def objective_code( self ) -> str:
        if self.__objectivecode is not None:
            return self.__objectivecode

    @objective_code.setter
    def objective_code( self, value: str ):
        if value is not None:
            self.__objectivecode = value

    @property
    def objective_name( self ) -> str:
        if self.__objectivename is not None:
            return self.__objectivename

    @objective_name.setter
    def objective_name( self, value: str ):
        if value is not None:
            self.__objectivename = value

    @property
    def npm_code( self ) -> str:
        if self.__npmcode is not None:
            return self.__npmcode

    @npm_code.setter
    def npm_code( self, value: str ):
        if value is not None:
            self.__npmcode = value

    @property
    def npm_name( self ) -> str:
        if self.__npmname is not None:
            return self.__npmname

    @npm_name.setter
    def npm_name( self, value: str ):
        if value is not None:
            self.__npmname = value

    @property
    def document_type( self ) -> str:
        if self.__documenttype is not None:
            return self.__documenttype

    @document_type.setter
    def document_type( self, value: str ):
        if value is not None:
            self.__documenttype = value

    @property
    def document_number( self ) -> str:
        if self.__documentnumber is not None:
            return self.__documentnumber

    @document_number.setter
    def document_number( self, value: str ):
        if value is not None:
            self.__documentnumber = value

    @property
    def document_control_number( self ) -> str:
        if self.__documentcontrolnumber is not None:
            return self.__documentcontrolnumber

    @document_control_number.setter
    def document_control_number( self, value: str ):
        if value is not None:
            self.__documentcontrolnumber = value

    @property
    def reference_document_number( self ) -> str:
        if self.__referencedocumentnumber is not None:
            return self.__referencedocumentnumber

    @reference_document_number.setter
    def reference_document_number( self, value: str ):
        if value is not None:
            self.__referencedocumentnumber = value

    @property
    def processed_date( self ) -> datetime:
        if self.__processeddate is not None:
            return self.__processeddate

    @processed_date.setter
    def processed_date( self, value: str ):
        if isinstance( value, datetime ):
            self.__processeddate = value

    @property
    def last_activity_date( self ) -> str:
        if  self.__lastactivitydate is not None:
            return self.__lastactivitydate

    @last_activity_date.setter
    def last_activity_date( self, value: str ):
        if value is not None:
            self.__lastactivitydate = value

    @property
    def age( self ) -> str:
        if self.__age is not None:
            return self.__age

    @age.setter
    def age( self, value: str ):
        if value is not None:
            self.__age = value

    @property
    def vendor_code( self ) -> str:
        if self.__vendorcode is not None:
            return self.__vendorcode

    @vendor_code.setter
    def vendor_code( self, value: str ):
        if value is not None:
            self.__vendorcode = value

    @property
    def vendor_name( self ) -> str:
        if self.__vendorname is not None:
            return self.__vendorname

    @vendor_name.setter
    def vendor_name( self, value: str ):
        if value is not None:
            self.__vendorname = value

    @property
    def foc_code( self ) -> str:
        if self.__foccode is not None:
            return self.__foccode

    @foc_code.setter
    def foc_code( self, value: str ):
        if value is not None:
            self.__foccode = value

    @property
    def foc_name( self ) -> str:
        if self.__focname is not None:
            return self.__focname

    @foc_name.setter
    def foc_name( self, value: str ):
        if value is not None:
            self.__focname = value

    @property
    def treasury_account_code( self ) -> str:
        if self.__treasuryaccountcode is not None:
            return self.__treasuryaccountcode

    @treasury_account_code.setter
    def treasury_account_code( self, value: str ):
        if value is not None:
            self.__treasuryaccountcode = value

    @property
    def treasury_account_name( self ) -> str:
        if self.__treasuryaccountname is not None:
            return self.__treasuryaccountname

    @treasury_account_name.setter
    def treasury_account_name( self, value: str ):
        if value is not None:
            self.__treasuryaccountname = value

    @property
    def budget_account_code( self ) -> str:
        if self.__budgetaccountcode is not None:
            return self.__budgetaccountcode

    @budget_account_code.setter
    def budget_account_code( self, value: str ):
        if value is not None:
            self.__budgetaccountcode = value

    @property
    def budget_account_name( self ) -> str:
        if self.__budgetaccountname is not None:
            return self.__budgetaccountname

    @budget_account_name.setter
    def budget_account_name( self, value: str ):
        if value is not None:
            self.__budgetaccountname = value

    @property
    def fields( self ) -> list[ str ]:
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value: list[ str ] ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy: str, efy: str, fund: str,
                  account: str, boc: str, provider: Provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.OpenCommitments
        self.__bfy = bfy
        self.__efy = efy
        self.__fundcode = fund
        self.__accountcode = account
        self.__boccode = boc
        self.__fields = [ 'OpenCommitmentsId',
                           'ObligationsId',
                           'BFY',
                           'EFY',
                           'RpioCode',
                           'RpioName',
                           'AhCode',
                           'AhName',
                           'FundCode',
                           'FundName',
                           'OrgCode',
                           'OrgName',
                           'AccountCode',
                           'ProgramProjectCode',
                           'ProgramProjectName',
                           'RcCode',
                           'RcName',
                           'DocumentType',
                           'DocumentNumber',
                           'DocumentControlNumber',
                           'ReferenceDocumentNumber',
                           'ProcessedDate',
                           'LastActivityDate',
                           'Age',
                           'BocCode',
                           'BocName',
                           'FocCode',
                           'FocName',
                           'NpmCode',
                           'NpmName',
                           'VendorCode',
                           'VendorName',
                           'OpenCommitment',
                           'Obligation',
                           'ULO',
                           'Expenditure' ]

    def __str__( self ) -> str:
        if self.__accountcode is not None:
            return self.__accountcode

    def get_data( self  ) -> list[ Row ]:
        try:
            _source = self.__source
            _provider = self.__provider
            _names = [ 'BFY', 'FundCode', 'AccountCode', 'BocCode' ]
            _values = (self.__bfy, self.__fundcode, self.__accountcode, self.__boccode)
            _dbconfig = DbConfig( _source, _provider )
            _sqlconfig = SqlConfig( names = _names, values = _values )
            _connection = Connection( self.__source )
            _sql = SqlStatement( _dbconfig, _sqlconfig )
            _sqlite = _connection.connect( )
            _cursor = _sqlite.cursor( )
            _query = _sql.get_query( )
            _db = _cursor.execute( _query )
            self.__data =  [ i for i in _db.fetchall( ) ]
            _cursor.close( )
            _sqlite.close( )
            return self.__data
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Ninja'
            _exc.cause = 'OpenCommitment'
            _exc.method = 'get_data( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def get_frame( self ) -> DataFrame:
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            _source = self.__source
            _data = BudgetData( _source )
            return _data.create_frame( )
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Ninja'
            _exc.cause = 'OpenCommitment'
            _exc.method = 'create_frame( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class Obligation( ):
    '''
    Constructor:  Obligation( bfy: str, efy: str, fund: str,
                  account: str, boc: str, pvdr: Provider = Provider.SQLite )

    Purpose:  Class defines object providing Obligation data'''
    __source = None
    __provider = None
    __obligationsid = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __rpioname = None
    __fundcode = None
    __fundname = None
    __ahcode = None
    __ahname = None
    __orgcode = None
    __orgname = None
    __accountcode = None
    __programprojectname = None
    __boccode = None
    __bocname = None
    __rccode = None
    __rcname = None
    __documenttype = None
    __documentnumber = None
    __documentcontrolnumber = None
    __referencedocumentnumber = None
    __programprojectcode = None
    __programareacode = None
    __programareaname = None
    __processeddate = None
    __lastactivitydate = None
    __age = None
    __vendorcode = None
    __vendorage = None
    __foccode = None
    __focname = None
    __amount = None
    __goalcode = None
    __goalname = None
    __objectivecode = None
    __objectivename = None
    __npmcode = None
    __npmname = None
    __treasuryaccountcode = None
    __treasuryaccountname = None
    __budgetaccountcode = None
    __budgetaccountname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ) -> int:
        if self.__obligationsid is not None:
            return self.__obligationsid

    @id.setter
    def id( self, value: int ):
        if value is not None:
            self.__obligationsid = value

    @property
    def bfy( self ) -> str:
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value: str ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ) -> str:
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value: str ):
        if value is not None:
            self.__efy = value

    @property
    def rpio_code( self ) -> str:
        if self.__rpiocode is not None:
            return self.__rpiocode

    @rpio_code.setter
    def rpio_code( self, value: str ):
        if value is not None:
            self.__rpiocode = value

    @property
    def rpio_name( self ) -> str:
        if self.__rpioname is not None:
            return self.__rpioname

    @rpio_code.setter
    def rpio_code( self, value: str ):
        if value is not None:
            self.__rpiocode = value

    @property
    def ah_code( self ) -> str:
        if self.__ahcode is not None:
            return self.__ahcode

    @ah_code.setter
    def ah_code( self, value: str ):
        if value is not None:
            self.__ahcode = value

    @property
    def ah_name( self ) -> str:
        if self.__ahname is not None:
            return self.__ahname

    @ah_name.setter
    def ah_name( self, value: str ):
        if value is not None:
            self.__ahname = value

    @property
    def fund_code( self ) -> str:
        if self.__fundcode is not None:
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value: str ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund_name( self ) -> str:
        if self.__fundname is not None:
            return self.__fundname

    @fund_name.setter
    def fund_name( self, value: str ):
        if value is not None:
            self.__fundname = value

    @property
    def org_code( self ) -> str:
        if self.__orgcode is not None:
            return self.__orgcode

    @org_code.setter
    def org_code( self, value: str ):
        if value is not None:
            self.__orgcode = value

    @property
    def org_name( self  ):
        if self.__orgname is not None:
            return self.__orgname

    @org_name.setter
    def org_name( self, value  ):
        if value is not None:
            self.__orgname = value

    @property
    def account_code( self ) -> str:
        if self.__accountcode is not None:
            return self.__accountcode

    @account_code.setter
    def account_code( self, value: str ):
        if value is not None:
            self.__accountcode = value

    @property
    def boc_code( self ) -> str:
        if self.__boccode is not None:
            return self.__boccode

    @boc_code.setter
    def boc_code( self, value: str ):
        if value is not None:
            self.__boccode = value

    @property
    def boc_name( self ) -> str:
        if self.__bocname is not None:
            return self.__bocname

    @boc_name.setter
    def boc_name( self, value: str ):
        if value is not None:
            self.__bocname = value

    @property
    def rc_code( self ) -> str:
        if self.__rccode is not None:
            return self.__rccode

    @rc_code.setter
    def rc_code( self, value: str ):
        if value is not None:
            self.__rccode = value

    @property
    def rc_name( self ) -> str:
        if self.__rcname is not None:
            return self.__rcname

    @rc_name.setter
    def rc_name( self, value: str ):
        if value is not None:
            self.__rcname = value

    @property
    def amount( self ) -> float:
        if self.__amount is not None:
            return self.__amount

    @amount.setter
    def amount( self, value: float ):
        if value is not None:
            self.__amount = value

    @property
    def budgeted( self ) -> str:
        if self.__budgeted is not None:
            return self.__budgeted

    @budgeted.setter
    def budgeted( self, value: str ):
        if value is not None:
            self.__budgeted = value

    @property
    def posted( self ) -> float:
        if self.__posted is not None:
            return self.__posted

    @posted.setter
    def posted( self, value: float ):
        if value is not None:
            self.__posted = value

    @property
    def open_commitments( self ) -> float:
        if self.__opencommitments is not None:
            return self.__opencommitments

    @open_commitments.setter
    def open_commitments( self, value: float ):
        if value is not None:
            self.__opencommitments = value

    @property
    def obligations( self ) -> float:
        if self.__obligations is not None:
            return self.__obligations

    @obligations.setter
    def obligations( self, value: float ):
        if value is not None:
            self.__obligations = value

    @property
    def unliquidated_obligations( self ) -> str:
        if self.__unliquidatedobligations is not None:
            return self.__unliquidatedobligations

    @unliquidated_obligations.setter
    def unliquidated_obligations( self, value: str ):
        if value is not None:
            self.__unliquidatedobligations = value

    @property
    def expenditures( self ) -> float:
        if self.__expenditures is not None:
            return self.__expenditures

    @expenditures.setter
    def expenditures( self, value: float ):
        if value is not None:
            self.__expenditures = value

    @property
    def used( self ) -> float:
        if self.__used is not None:
            return self.__used

    @used.setter
    def used( self, value: float ):
        if value is not None:
            self.__used = value

    @property
    def available( self ) -> float:
        if self.__avaialable is not None:
            return self.__avaialable

    @available.setter
    def available( self, value: float ):
        if value is not None:
            self.__avaialable = value

    @property
    def program_project_code( self ) -> str:
        if self.__programprojectcode is not None:
            return self.__programprojectcode

    @program_project_code.setter
    def program_project_code( self, value: str ):
        if value is not None:
            self.__programprojectcode = value

    @property
    def program_project_name( self ) -> str:
        if self.__programprojectname is not None:
            return self.__programprojectname

    @program_project_name.setter
    def program_project_name( self, value: str ):
        if value is not None:
            self.__programprojectname = value

    @property
    def program_area_code( self ) -> str:
        if self.__programareacode is not None:
            return self.__programareacode

    @program_area_code.setter
    def program_area_code( self, value: str ):
        if value is not None:
            self.__programareacode = value

    @property
    def program_area_name( self ) -> str:
        if self.__programareaname is not None:
            return self.__programareaname

    @program_area_name.setter
    def program_area_name( self, value: str ):
        if value is not None:
            self.__programareaname = value

    @property
    def goal_code( self ) -> str:
        if self.__goalcode is not None:
            return self.__goalcode

    @goal_code.setter
    def goal_code( self, value: str ):
        if value is not None:
            self.__goalcode = value

    @property
    def goal_name( self ) -> str:
        if self.__goalname is not None:
            return self.__goalname

    @goal_name.setter
    def goal_name( self, value: str ):
        if value is not None:
            self.__goalname = value

    @property
    def objective_code( self ) -> str:
        if self.__objectivecode is not None:
            return self.__objectivecode

    @objective_code.setter
    def objective_code( self, value: str ):
        if value is not None:
            self.__objectivecode = value

    @property
    def objective_name( self ) -> str:
        if self.__objectivename is not None:
            return self.__objectivename

    @objective_name.setter
    def objective_name( self, value: str ):
        if value is not None:
            self.__objectivename = value

    @property
    def npm_code( self ) -> str:
        if self.__npmcode is not None:
            return self.__npmcode

    @npm_code.setter
    def npm_code( self, value: str ):
        if value is not None:
            self.__npmcode = value

    @property
    def npm_name( self ) -> str:
        if self.__npmname is not None:
            return self.__npmname

    @npm_name.setter
    def npm_name( self, value: str ):
        if value is not None:
            self.__npmname = value

    @property
    def document_type( self ) -> str:
        if self.__documenttype is not None:
            return self.__documenttype

    @document_type.setter
    def document_type( self, value: str ):
        if value is not None:
            self.__documenttype = value

    @property
    def document_number( self ) -> str:
        if self.__documentnumber is not None:
            return self.__documentnumber

    @document_number.setter
    def document_number( self, value: str ):
        if value is not None:
            self.__documentnumber = value

    @property
    def document_control_number( self ) -> str:
        if self.__documentcontrolnumber is not None:
            return self.__documentcontrolnumber

    @document_control_number.setter
    def document_control_number( self, value: str ):
        if value is not None:
            self.__documentcontrolnumber = value

    @property
    def reference_document_number( self ) -> str:
        if self.__referencedocumentnumber is not None:
            return self.__referencedocumentnumber

    @reference_document_number.setter
    def reference_document_number( self, value: str ):
        if value is not None:
            self.__referencedocumentnumber = value

    @property
    def processed_date( self ) -> datetime:
        if self.__processeddate is not None:
            return self.__processeddate

    @processed_date.setter
    def processed_date( self, value: datetime ):
        if value is not None:
            self.__processeddate = value

    @property
    def last_activity_date( self ) -> datetime:
        if self.__lastactivitydate is not None:
            return self.__lastactivitydate

    @last_activity_date.setter
    def last_activity_date( self, value: datetime ):
        if value is not None:
            self.__lastactivitydate = value

    @property
    def age( self ) -> float:
        if self.__age is not None:
            return self.__age

    @age.setter
    def age( self, value: float ):
        if value is not None:
            self.__age = value

    @property
    def vendor_code( self ) -> str:
        if self.__vendorcode is not None:
            return self.__vendorcode

    @vendor_code.setter
    def vendor_code( self, value: str ):
        if value is not None:
            self.__vendorcode = value

    @property
    def vendor_name( self ) -> str:
        if self.__vendorname is not None:
            return self.__vendorname

    @vendor_name.setter
    def vendor_name( self, value: str ):
        if value is not None:
            self.__vendorname = value

    @property
    def foc_code( self ) -> str:
        if self.__foccode is not None:
            return self.__foccode

    @foc_code.setter
    def foc_code( self, value: str ):
        if value is not None:
            self.__foccode = value

    @property
    def foc_name( self ) -> str:
        if self.__focname is not None:
            return self.__focname

    @foc_name.setter
    def foc_name( self, value: str ):
        if value is not None:
            self.__focname = value

    @property
    def treasury_account_code( self ) -> str:
        if self.__treasuryaccountcode is not None:
            return self.__treasuryaccountcode

    @treasury_account_code.setter
    def treasury_account_code( self, value: str ):
        if value is not None:
            self.__treasuryaccountcode = value

    @property
    def treasury_account_name( self ) -> str:
        if self.__treasuryaccountname is not None:
            return self.__treasuryaccountname

    @treasury_account_name.setter
    def treasury_account_name( self, value: str ):
        if value is not None:
            self.__treasuryaccountname = value

    @property
    def budget_account_code( self ) -> str:
        if self.__budgetaccountcode is not None:
            return self.__budgetaccountcode

    @budget_account_code.setter
    def budget_account_code( self, value: str ):
        if value is not None:
            self.__budgetaccountcode = value

    @property
    def budget_account_name( self ) -> str:
        if self.__budgetaccountname is not None:
            return self.__budgetaccountname

    @budget_account_name.setter
    def budget_account_name( self, value: str ):
        if value is not None:
            self.__budgetaccountname = value

    @property
    def fields( self ) -> list[ str ]:
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value: list[ str ] ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy: str, efy: str, fund: str,
                  account: str, boc: str, provider: Provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.Obligations
        self.__bfy = bfy
        self.__efy = efy
        self.__fundcode = fund
        self.__accountcode = account
        self.__boccode = boc
        self.__fields = [ 'ObligationsId',
                           'BFY',
                           'EFY',
                           'RpioCode',
                           'RpioName',
                           'AhCode',
                           'AhName',
                           'FundCode',
                           'FundName',
                           'OrgCode',
                           'OrgName',
                           'AccountCode',
                           'ProgramProjectCode',
                           'ProgramProjectName',
                           'RcCode',
                           'RcName',
                           'DocumentType',
                           'DocumentNumber',
                           'DocumentControlNumber',
                           'ReferenceDocumentNumber',
                           'ProcessedDate',
                           'LastActivityDate',
                           'Age',
                           'BocCode',
                           'BocName',
                           'FocCode',
                           'FocName',
                           'NpmCode',
                           'NpmName',
                           'VendorCode',
                           'VendorName',
                           'OpenCommitment',
                           'Obligation',
                           'ULO',
                           'Expenditure' ]

    def __str__( self ) -> str:
        if self.__amount is not None:
            return str( self.__amount )

    def get_data( self  ) -> list[ Row ]:
        try:
            _source = self.__source
            _provider = self.__provider
            _names = [ 'BFY', 'FundCode', 'AccountCode', 'BocCode' ]
            _values = (self.__bfy, self.__fundcode, self.__accountcode, self.__boccode)
            _dbconfig = DbConfig( _source, _provider )
            _sqlconfig = SqlConfig( names = _names, values = _values )
            _connection = Connection( self.__source )
            _sql = SqlStatement( _dbconfig, _sqlconfig )
            _sqlite = _connection.connect( )
            _cursor = _sqlite.cursor( )
            _query = _sql.get_query( )
            _db = _cursor.execute( _query )
            self.__data =  [ i for i in _db.fetchall( ) ]
            _cursor.close( )
            _sqlite.close( )
            return self.__data
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Ninja'
            _exc.cause = 'Obligaions'
            _exc.method = 'get_data( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def get_frame( self ) -> DataFrame:
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            _source = self.__source
            _data = BudgetData( _source )
            return _data.create_frame( )
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Ninja'
            _exc.cause = 'Obligation'
            _exc.method = 'create_frame( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class PublicLaw( ):
    '''
    Constructor: PublicLaw( bfy: str, efy: str,
                  number: str, pvdr: Provider = Provider.SQLite  )

    Purpose:
    '''
    __source = None
    __provider = None
    __publiclawsid = None
    __bfy = None
    __efy = None
    __lawnumber = None
    __enacteddate = None
    __congress = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ) -> int:
        if self.__publiclawsid is not None:
            return self.__publiclawsid

    @id.setter
    def id( self, value: int ):
        if value is not None:
            self.__publiclawsid = value

    @property
    def bfy( self ) -> str:
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value: str ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ) -> str:
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value: str ):
        if value is not None:
            self.__efy = value

    @property
    def lawnumber( self ) -> str:
        if self.__lawnumber is not None:
            return self.__lawnumber

    @lawnumber.setter
    def lawnumber( self, value: str ):
        if value is not None:
            self.__lawnumber = value

    @property
    def fields( self ) -> list[ str ]:
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value: list[ str ] ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy: str, efy: str,
                  number: str, provider: Provider = Provider.SQLite ):
        self.__bfy = bfy
        self.__efy = efy
        self.__lawnumber = number
        self.__provider = provider
        self.__source = Source.PublicLaws
        self.__fields = [ 'PublicLawsId',
                          'LawNumber',
                          'BillTitle',
                          'EnactedDate',
                          'Congress',
                          'BFY' ]

class Project( ):
    '''
    Constructor:  Project( code: str, pvdr: Provider = Provider.SQLite )

    Purpoe:  Class defines the Organization Class'''
    __source = None
    __projectsid = None
    __code = None
    __name = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ) -> int:
        if self.__projectsid is not None:
            return self.__projectsid

    @id.setter
    def id( self, value: int ):
        if value is not None:
            self.__accountsid = value

    @property
    def code( self ) -> str:
        if  self.__code is not None:
            return self.__code

    @code.setter
    def code( self, value: str ):
        if value is not None:
            self.__code = value

    @property
    def name( self ) -> str:
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, value: str ):
        if value is not None:
            self.__name = value

    @property
    def data( self ) -> list:
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, value: list ):
        if isinstance( value, list ):
            self.__data = value

    @property
    def table( self ) -> DataFrame:
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, value: DataFrame ):
        if value is not None:
            self.__frame = value

    @property
    def fields( self ) -> list[ str ]:
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value: list[ str ] ):
        if value is not None:
            self.__fields = value

    def __init__( self, code: str, provider: Provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.Projects
        self.__code = code
        self.__fields = [ 'ProjectId',
                          'Code',
                          'Name' ]

    def __str__( self ) -> str:
        if  self.__code is not None:
            return self.__code

    def get_data( self  ) -> list[ Row ]:
        try:
            _source = self.__source
            _provider = self.__provider
            _names = [ 'Code', ]
            _values = (self.__code,)
            _dbconfig = DbConfig( _source, _provider )
            _sqlconfig = SqlConfig( names = _names, values = _values )
            _connection = Connection( self.__source )
            _sql = SqlStatement( _dbconfig, _sqlconfig )
            _sqlite = _connection.connect( )
            _cursor = _sqlite.cursor( )
            _query = _sql.get_query( )
            _db = _cursor.execute( _query )
            self.__data =  [ i for i in _db.fetchall( ) ]
            _cursor.close( )
            _sqlite.close( )
            return self.__data
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Execution'
            _exc.cause = 'Project'
            _exc.method = 'get_data( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def get_frame( self ) -> DataFrame:
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            _source = self.__source
            _data = BudgetData( _source )
            return _data.create_frame( )
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Execution'
            _exc.cause = 'Project'
            _exc.method = 'create_frame( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class ProgramArea( ):
    '''
    Constructor:   ProgramArea( code: str, pvdr: Provider = Provider.SQLite  )

    Purpose:  defines the ProgramArea class
    '''
    __source = None
    __provider = None
    __programareasid = None
    __code = None
    __name = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ) -> int:
        if self.__programareasid is not None:
            return self.__programareasid

    @id.setter
    def id( self, value: int ):
        if value is not None:
            self.__accountsid = value

    @property
    def code( self ) -> str:
        if  self.__code is not None:
            return self.__code

    @code.setter
    def code( self, value: str ):
        if value is not None:
            self.__code = value

    @property
    def name( self ) -> str:
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, value: str ):
        if value is not None:
            self.__name = value

    @property
    def data( self ) -> list:
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, value: list ):
        if value is not None:
            self.__data = value

    @property
    def table( self ) -> DataFrame:
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, value: DataFrame ):
        if value is not None:
            self.__frame = value

    @property
    def fields( self ) -> list[ str ]:
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value: list[ str ] ):
        if value is not None:
            self.__fields = value

    def __init__( self, code: str, provider: Provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.ProgramAreas
        self.__code = code
        self.__fields = [ 'ProgramAreasId',
                          'Code',
                          'Name' ]

    def __str__( self ) -> str:
        if self.__code is not None:
            return self.__code

    def get_data( self  ) -> list[ Row ]:
        try:
            _source = self.__source
            _provider = self.__provider
            _names = [ 'Code', ]
            _values = (self.__code,)
            _dbconfig = DbConfig( _source, _provider )
            _sqlconfig = SqlConfig( names = _names, values = _values )
            _connection = Connection( self.__source )
            _sql = SqlStatement( _dbconfig, _sqlconfig )
            _sqlite = _connection.connect( )
            _cursor = _sqlite.cursor( )
            _query = _sql.get_query( )
            _db = _cursor.execute( _query )
            self.__data =  [ i for i in _db.fetchall( ) ]
            _cursor.close( )
            _sqlite.close( )
            return self.__data
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Execution'
            _exc.cause = 'ProgramArea'
            _exc.method = 'get_data( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def get_frame( self ) -> DataFrame:
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            _source = self.__source
            _data = BudgetData( _source )
            return _data.create_frame( )
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Execution'
            _exc.cause = 'ProgramArea'
            _exc.method = 'create_frame( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class ProgramProject( ):
    '''
    Constructor:  ProgramProject( code: str, pvdr: Provider = Provider.SQLite )

    Purpose:  Defines the ProgramProject Class
    '''
    __source = None
    __provider = None
    __programprojectsid = None
    __code = None
    __name = None
    __programareacode = None
    __programareaname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ) -> int:
        if self.__programprojectsid is not None:
            return self.__programprojectsid

    @id.setter
    def id( self, value: int ):
        if value is not None:
            self.__programprojectsid  = value

    @property
    def code( self ) -> str:
        if  self.__code is not None:
            return self.__code

    @code.setter
    def code( self, value: str ):
        if value is not None:
            self.__code = value

    @property
    def name( self ) -> str:
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, value: str ):
        if value is not None:
            self.__name = value

    @property
    def program_area_code( self ) -> str:
        if self.__programareacode is not None:
            return self.__programareacode

    @program_area_code.setter
    def program_area_code( self, value: str ):
        if value is not None:
            self.__programareacode = value

    @property
    def program_area_name( self ) -> str:
        if self.__programareaname is not None:
            return self.__programareaname

    @program_area_name.setter
    def program_area_name( self, value: str ):
        if value is not None:
            self.____programareaname = value

    @property
    def data( self ) -> list:
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, value: list ):
        if isinstance( value, list ):
            self.__data = value

    @property
    def table( self ) -> DataFrame:
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, value: DataFrame ):
        if value is not None:
            self.__frame = value

    @property
    def fields( self ) -> list[ str ]:
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value: list[ str ] ):
        if value is not None:
            self.__fields = value

    def __init__( self, code: str, provider: Provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.ProgramProjects
        self.__code = code
        self.__fields = [ 'ProgramProjectsId',
                          'Code',
                          'Name',
                          'ProgramAreaCode',
                          'ProgramAreaName' ]

    def __str__( self ) -> str:
        if self.__code is not None:
            return self.__code

    def get_data( self  ) -> list[ Row ]:
        try:
            _source = self.__source
            _provider = self.__provider
            _names = [ 'Code', ]
            _values = (self.__code,)
            _dbconfig = DbConfig( _source, _provider )
            _sqlconfig = SqlConfig( names = _names, values = _values )
            _connection = Connection( self.__source )
            _sql = SqlStatement( _dbconfig, _sqlconfig )
            _sqlite = _connection.connect( )
            _cursor = _sqlite.cursor( )
            _query = _sql.get_query( )
            _db = _cursor.execute( _query )
            self.__data =  [ i for i in _db.fetchall( ) ]
            _cursor.close( )
            _sqlite.close( )
            return self.__data
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Execution'
            _exc.cause = 'ProgramProject'
            _exc.method = 'get_data( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class ProgramResultsCode( ):
    '''
    Constructor:   ProgramResultsCode( bfy: str = None, efy: str = None, fund: str = None,
                  rpio: str = None, ah: str = None, account: str = None, boc: str = None,
                  amount: float = 0.0, pvdr: Provider = Provider.SQLite )

    Purpose:  Class defines the PRCs
    '''
    __source = None
    __provider = None
    __allocationsid = None
    __rpiocode = None
    __rpioname = None
    __bfy = None
    __efy = None
    __ahcode = None
    __ahname = None
    __fundcode = None
    __fundname = None
    __orgcode = None
    __orgname = None
    __accountcode = None
    __accountname = None
    __activitycode = None
    __activityname = None
    __rccode = None
    __rcname = None
    __boccode = None
    __bocname = None
    __amount = None
    __programprojectcode = None
    __programprojectname = None
    __programareacode = None
    __programareaname = None
    __goalcode = None
    __goalname = None
    __objectivecode = None
    __objectivename = None
    __npmcode = None
    __npmname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ) -> int:
        if self.__allocationsid is not None:
            return self.__allocationsid

    @id.setter
    def id( self, value: int ):
        if value is not None:
            self.__allocationsid = value

    @property
    def bfy( self ) -> str:
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value: str ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ) -> str:
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value: str ):
        if value is not None:
            self.__efy = value

    @property
    def rpio_code( self ) -> str:
        if self.__rpiocode is not None:
            return self.__rpiocode

    @rpio_code.setter
    def rpio_code( self, value: str ):
        if value is not None:
            self.__rpiocode = value

    @property
    def rpio_name( self ) -> str:
        if self.__rpioname is not None:
            return self.__rpioname

    @rpio_name.setter
    def rpio_name( self, value: str ):
        if value is not None:
            self.__rpioname = value

    @property
    def ah_code( self ) -> str:
        if self.__ahcode is not None:
            return self.__ahcode

    @ah_code.setter
    def ah_code( self, value: str ):
        if value is not None:
            self.__ahcode = value

    @property
    def ah_name( self ) -> str:
        if self.__ahname is not None:
            return self.__ahname

    @ah_name.setter
    def ah_name( self, value: str ):
        if value is not None:
            self.__ahname = value

    @property
    def fund_code( self ) -> str:
        if self.__fundcode is not None:
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value: str ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund_name( self ) -> str:
        if self.__fundname is not None:
            return self.__fundname

    @fund_name.setter
    def fund_name( self, value: str ):
        if value is not None:
            self.__fundname = value

    @property
    def org_code( self ) -> str:
        if self.__orgcode is not None:
            return self.__orgcode

    @org_code.setter
    def org_code( self, value: str ):
        if value is not None:
            self.__orgcode = value

    @property
    def org_name( self  ):
        if self.__orgname is not None:
            return self.__orgname

    @org_name.setter
    def org_name( self, value  ):
        if value is not None:
            self.__orgname = value

    @property
    def account_code( self ) -> str:
        if self.__accountcode is not None:
            return self.__accountcode

    @account_code.setter
    def account_code( self, value: str ):
        if value is not None:
            self.__accountcode = value

    @property
    def boc_code( self ) -> str:
        if self.__boccode is not None:
            return self.__boccode

    @boc_code.setter
    def boc_code( self, value: str ):
        if value is not None:
            self.__boccode = value

    @property
    def boc_name( self ) -> str:
        if self.__bocname is not None:
            return self.__bocname

    @boc_name.setter
    def boc_name( self, value: str ):
        if value is not None:
            self.__bocname = value

    @property
    def rc_code( self ) -> str:
        if self.__rccode is not None:
            return self.__rccode

    @rc_code.setter
    def rc_code( self, value: str ):
        if value is not None:
            self.__rccode = value

    @property
    def rc_name( self ) -> str:
        if self.__rcname is not None:
            return self.__rcname

    @rc_name.setter
    def rc_name( self, value: str ):
        if value is not None:
            self.__rcname = value

    @property
    def amount( self ) -> float:
        if self.__amount is not None:
            return self.__amount

    @amount.setter
    def amount( self, value: float ):
        if value is not None:
            self.__amount = value

    @property
    def budgeted( self ) -> str:
        if self.__budgeted is not None:
            return self.__budgeted

    @budgeted.setter
    def budgeted( self, value: str ):
        if value is not None:
            self.__budgeted = value

    @property
    def posted( self ) -> float:
        if self.__posted is not None:
            return self.__posted

    @posted.setter
    def posted( self, value: float ):
        if value is not None:
            self.__posted = value

    @property
    def open_commitments( self ) -> float:
        if self.__opencommitments is not None:
            return self.__opencommitments

    @open_commitments.setter
    def open_commitments( self, value: float ):
        if value is not None:
            self.__opencommitments = value

    @property
    def obligations( self ) -> float:
        if self.__obligations is not None:
            return self.__obligations

    @obligations.setter
    def obligations( self, value: float ):
        if value is not None:
            self.__obligations = value

    @property
    def unliquidated_obligations( self ) -> float:
        if self.__unliquidatedobligations is not None:
            return self.__unliquidatedobligations

    @unliquidated_obligations.setter
    def unliquidated_obligations( self, value: float ):
        if value is not None:
            self.__unliquidatedobligations = value

    @property
    def expenditures( self ) -> float:
        if self.__expenditures is not None:
            return self.__expenditures

    @expenditures.setter
    def expenditures( self, value: float ):
        if value is not None:
            self.__expenditures = value

    @property
    def used( self ) -> float:
        if self.__used is not None:
            return self.__used

    @used.setter
    def used( self, value: float ):
        if value is not None:
            self.__used = value

    @property
    def available( self ) -> float:
        if self.__avaialable is not None:
            return self.__avaialable

    @available.setter
    def available( self, value: float ):
        if value is not None:
            self.__avaialable = value

    @property
    def program_project_code( self ) -> str:
        if self.__programprojectcode is not None:
            return self.__programprojectcode

    @program_project_code.setter
    def program_project_code( self, value: str ):
        if value is not None:
            self.__programprojectcode = value

    @property
    def program_project_name( self ) -> str:
        if self.__programprojectname is not None:
            return self.__programprojectname

    @program_project_name.setter
    def program_project_name( self, value: str ):
        if value is not None:
            self.__programprojectname = value

    @property
    def program_area_code( self ) -> str:
        if self.__programareacode is not None:
            return self.__programareacode

    @program_area_code.setter
    def program_area_code( self, value: str ):
        if value is not None:
            self.__programareacode = value

    @property
    def program_area_name( self ) -> str:
        if self.__programareaname is not None:
            return self.__programareaname

    @program_area_name.setter
    def program_area_name( self, value: str ):
        if value is not None:
            self.__programareaname = value

    @property
    def goal_code( self ) -> str:
        if self.__goalcode is not None:
            return self.__goalcode

    @goal_code.setter
    def goal_code( self, value: str ):
        if value is not None:
            self.__goalcode = value

    @property
    def goal_name( self ) -> str:
        if self.__goalname is not None:
            return self.__goalname

    @goal_name.setter
    def goal_name( self, value: str ):
        if value is not None:
            self.__goalname = value

    @property
    def objective_code( self ) -> str:
        if self.__objectivecode is not None:
            return self.__objectivecode

    @objective_code.setter
    def objective_code( self, value: str ):
        if value is not None:
            self.__objectivecode = value

    @property
    def objective_name( self ) -> str:
        if self.__objectivename is not None:
            return self.__objectivename

    @objective_name.setter
    def objective_name( self, value: str ):
        if value is not None:
            self.__objectivename = value

    @property
    def npm_code( self ) -> str:
        if self.__npmcode is not None:
            return self.__npmcode

    @npm_code.setter
    def npm_code( self, value: str ):
        if value is not None:
            self.__npmcode = value

    @property
    def npm_name( self ) -> str:
        if self.__npmname is not None:
            return self.__npmname

    @npm_name.setter
    def npm_name( self, value: str ):
        if value is not None:
            self.__npmname = value

    @property
    def activity_code( self ) -> str:
        if self.__activitycode is not None:
            return self.__activitycode

    @activity_code.setter
    def activity_code( self, value: str ):
        if value is not None:
            self.__activitycode = value

    @property
    def activity_name( self ) -> str:
        if self.__activityname is not None:
            return self.__activityname

    @activity_name.setter
    def activity_name( self, value: str ):
        if value is not None:
            self.__activityname = value

    @property
    def data( self ) -> list[ tuple ]:
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, value: list[ tuple ] ):
        if isinstance( value, list ):
            self.__data = value

    @property
    def table( self ) -> DataFrame:
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, value: DataFrame ):
        if value is not None:
            self.__frame = value

    @property
    def fields( self ) -> list[ str ]:
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value: list[ str ] ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy: str = None, efy: str = None, fund: str = None,
                  rpio: str = None, ah: str = None, account: str = None, boc: str = None,
                  amount: float = 0.0, provider: Provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.Allocations
        self.__accountcode = account
        self.__bfy = bfy
        self.__efy = efy
        self.__fundcode = fund
        self.__rpiocode = rpio
        self.__ahcode = ah
        self.__boccode = boc
        self.__amount = amount
        self.__fields = [ 'AllocationsId',
                           'StatusOfFundsId',
                           'BudgetLevel',
                           'BFY',
                           'EFY',
                           'RpioCode',
                           'RpioName',
                           'AhCode',
                           'AhName',
                           'FundCode',
                           'FundName',
                           'OrgCode',
                           'OrgName',
                           'AccountCode',
                           'BocCode',
                           'BocName',
                           'ProgramProjectCode',
                           'ProgramProjectName',
                           'ProgramAreaCode',
                           'ProgramAreaName',
                           'RcCode',
                           'RcName',
                           'Amount',
                           'NpmCode',
                           'NpmName' ]

    def __str__( self ) -> str:
        if self.__fundcode is not None:
            return self.__fundcode

    def get_data( self  ) -> list[ Row ]:
        try:
            _source = self.__source
            _provider = self.__provider
            _command = SQL.SELECTALL
            _names = [ 'BFY', 'EFY', 'FundCode', 'RpioCode', 'AhCode',
                      'AccountCode', 'BocCode', 'Amount' ]
            _values = (self.__bfy, self.__efy, self.__fundcode, self.__rpiocode,
                       self.__ahcode, self.__accountcode, self.__boccode, self.__amount)
            _db = DataBuilder( _source, _provider, _command, _names, _values )
            self.__data = _db.create_table( )
            return [ ( i ) for i in self.__data ]
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Execution'
            _exc.cause = 'ProgramResultsCode'
            _exc.method = 'get_data( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def get_frame( self ) -> DataFrame:
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            _source = self.__source
            _data = BudgetData( _source )
            return _data.create_frame( )
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Execution'
            _exc.cause = 'ProgramResultsCode'
            _exc.method = 'create_frame( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class ResponsibilityCenter( ):
    '''
    Constructor:  ResponsibilityCenter( code: str,
            pvdr: Provider = Provider.SQLite  )

    Purpose:  Class defines the ResponsibilityCenter Class
    '''
    __source = None
    __provider = None
    __responsibilitycentersid = None
    __code = None
    __name = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ) -> int:
        if self.__responsibilitycentersid is not None:
            return self.__responsibilitycentersid

    @id.setter
    def id( self, value: int ):
        if value is not None:
            self.__accountsid = value

    @property
    def code( self ) -> str:
        if  self.__code is not None:
            return self.__code

    @code.setter
    def code( self, value: str ):
        if value is not None:
            self.__code = value

    @property
    def name( self ) -> str:
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, value: str ):
        if value is not None:
            self.__name = value

    @property
    def data( self ) -> list:
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, value: list ):
        if isinstance( value, list ):
            self.__data = value

    @property
    def table( self ) -> DataFrame:
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, value: DataFrame ):
        if value is not None:
            self.__frame = value

    @property
    def fields( self ) -> list[ str ]:
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value: list[ str ] ):
        if value is not None:
            self.__fields = value

    def __init__( self, code: str, provider: Provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.ResponsibilityCenters
        self.__code = code if isinstance( code, str ) else None
        self.__fields = [ 'ResponsibilityCentersId',
                          'Code',
                          'Name',
                          'Title' ]

    def __str__( self ) -> str:
        if self.__code is not None:
            return self.__code

    def get_data( self  ) -> list[ tuple ]:
        try:
            _source = self.__source
            _provider = self.__provider
            _names = [ 'Code', ]
            _values = (self.__code,)
            _dbconfig = DbConfig( _source, _provider )
            _sqlconfig = SqlConfig( names = _names, values = _values )
            _connection = Connection( self.__source )
            _sql = SqlStatement( _dbconfig, _sqlconfig )
            _sqlite = _connection.connect( )
            _cursor = _sqlite.cursor( )
            _query = _sql.get_query( )
            _db = _cursor.execute( _query )
            self.__data =  [ i for i in _db.fetchall( ) ]
            _cursor.close( )
            _sqlite.close( )
            return self.__data
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Execution'
            _exc.cause = 'ResponsibilityCenter'
            _exc.method = 'get_data( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def get_frame( self ) -> DataFrame:
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            _source = self.__source
            _data = BudgetData( _source )
            return _data.create_frame( )
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Execution'
            _exc.cause = 'ResponsibilityCenter'
            _exc.method = 'create_frame( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class ResourcePlanningOffice( ):
    '''
    Constuctor:  ResourcePlanningOffice( code: str,
            pvdr: Provider = Provider.SQLite )

    Purpose:  defines the ResponsiblePlanningOffice class'''
    __source = None
    __provider = None
    __resourceplanningofficesid = None
    __code = None
    __name = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ) -> int:
        if self.__resourceplanningofficesid is not None:
            return self.__resourceplanningofficesid

    @id.setter
    def id( self, value: int ):
        if value is not None:
            self.__resourceplanningofficesid = value

    @property
    def code( self ) -> str:
        if  self.__code is not None:
            return self.__code

    @code.setter
    def code( self, value: str ):
        if value is not None:
            self.__code = value

    @property
    def name( self ) -> str:
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, value: str ):
        if value is not None:
            self.__name = value

    @property
    def data( self ) -> list:
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, value: list ):
        if isinstance( value, list ):
            self.__data = value

    @property
    def table( self ) -> DataFrame:
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, value: DataFrame ):
        if value is not None:
            self.__frame = value

    @property
    def fields( self ) -> list[ str ]:
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value: list[ str ] ):
        if value is not None:
            self.__fields = value

    def __init__( self, code: str, provider: Provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.ResourcePlanningOffices
        self.__code = code
        self.__fields = [ 'ResourcePlanningOfficesId',
                          'Code',
                          'Name' ]

    def __str__( self ) -> str:
        if self.__code is not None:
            return self.__code

    def get_data( self  ) -> list[ Row ]:
        try:
            _source = self.__source
            _provider = self.__provider
            _names = [ 'Code', ]
            _values = (self.__code,)
            _dbconfig = DbConfig( _source, _provider )
            _sqlconfig = SqlConfig( names = _names, values = _values )
            _connection = Connection( self.__source )
            _sql = SqlStatement( _dbconfig, _sqlconfig )
            _sqlite = _connection.connect( )
            _cursor = _sqlite.cursor( )
            _query = _sql.get_query( )
            _db = _cursor.execute( _query )
            self.__data =  [ i for i in _db.fetchall( ) ]
            _cursor.close( )
            _sqlite.close( )
            return self.__data
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Execution'
            _exc.cause = 'ResourcePlanningOffice'
            _exc.method = 'get_data( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def get_frame( self ) -> DataFrame:
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            _source = self.__source
            _data = BudgetData( _source )
            return _data.create_frame( )
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Execution'
            _exc.cause = 'ResourcePlanningOffice'
            _exc.method = 'create_frame( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class RegionalOffice( ):
    '''
    Constructor:  RegionalOffice( code: str, pvdr: Provider = Provider.SQLite )

    Purpose:  Defines a regional RPIO
    '''
    __source = None
    __provider = None
    __resourceplanningofficesid = None
    __rpiocode = None
    __rpioname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ) -> int:
        if self.__resourceplanningofficesid is not None:
            return self.__resourceplanningofficesid

    @id.setter
    def id( self, value: int ):
        if value is not None:
            self.___resourceplanningofficesid = value

    @property
    def rpio_code( self ) -> str:
        if self.__rpiocode is not None:
            return self.__rpiocode

    @rpio_code.setter
    def rpio_code( self, value: str ):
        if value is not None:
            self.__rpiocode = value

    @property
    def rpio_name( self ) -> str:
        if self.__rpioname is not None:
            return self.__rpioname

    @rpio_name.setter
    def rpio_name( self, value: str ):
        if value is not None:
            self.__rpioname = value

    @property
    def data( self ) -> list:
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, value: list ):
        if value is not None:
            self.__data = value

    @property
    def table( self ) -> DataFrame:
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, value: DataFrame ):
        if value is not None:
            self.__frame = value

    @property
    def fields( self ) -> list[ str ]:
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value: list[ str ] ):
        if value is not None:
            self.__fields = value

    def __init__( self, code: str, provider: Provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.ResourcePlanningOffices
        self.__rpiocode = code
        self.__fields = [ 'RegionalOfficesId',
                          'ResourcePlanningOfficesId',
                          'RpioCode',
                          'RpioName' ]

    def __str__( self ) -> str:
        if self.__rpiocode is not None:
            return self.__rpiocode

    def get_data( self  ) -> list[ Row ]:
        try:
            _source = self.__source
            _provider = self.__provider
            _names = [ 'Code', ]
            _values = (self.__rpiocode,)
            _dbconfig = DbConfig( _source, _provider )
            _sqlconfig = SqlConfig( names = _names, values = _values )
            _connection = Connection( self.__source )
            _sql = SqlStatement( _dbconfig, _sqlconfig )
            _sqlite = _connection.connect( )
            _cursor = _sqlite.cursor( )
            _query = _sql.get_query( )
            _db = _cursor.execute( _query )
            self.__data =  [ i for i in _db.fetchall( ) ]
            _cursor.close( )
            _sqlite.close( )
            return self.__data
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Execution'
            _exc.cause = 'RegionalOffice'
            _exc.method = 'get_data( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class ReimbursableAgreement( ):
    '''
    Constructor:  ReimbursableAgreement( number: str,
            pvdr: Provider = Provider.SQLite  )

    Purpose:  Class defines object representing Reimbursable Agreements
    '''
    __source = None
    __provider = None
    __reimbursableagreementsid = None
    __bfy = None
    __efy = None
    __fundcode = None
    __rpiocode = None
    __agreementnumber = None
    __startdate = None
    __enddate = None
    __rccode = None
    __rcname = None
    __orgcode = None
    __siteprojectcode = None
    __accountcode = None
    __vendorcode = None
    __vendorname = None
    __amount = None
    __opencommitments = None
    __unliquidatedobligations = None
    __obligations = None
    __available = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ) -> int:
        if self.__reimbursableagreementsid is not None:
            return self.__reimbursableagreementsid

    @id.setter
    def id( self, value: int ):
        if value is not None:
            self.__reimbursableagreementsid = value

    @property
    def bfy( self ) -> str:
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value: str ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ) -> str:
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value: str ):
        if value is not None:
            self.__efy = value

    @property
    def fund_code( self ) -> str:
        if self.__fundcode is not None:
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value: str ):
        if value is not None:
            self.__fundcode = value

    @property
    def rpio_code( self ) -> str:
        if self.__rpiocode is not None:
            return self.__rpiocode

    @rpio_code.setter
    def rpio_code( self, value: str ):
        if value is not None:
            self.__rpiocode = value

    @property
    def agreement_number( self ) -> str:
        if self.__agreementnumber is not None:
            return self.__agreementnumber

    @agreement_number.setter
    def agreement_number( self, value: str ):
        if value is not None:
            self.__agreementnumber = value

    @property
    def account_code( self ) -> str:
        if self.__accountcode is not None:
            return self.__accountcode

    @account_code.setter
    def account_code( self, value: str ):
        if value is not None:
            self.__accountcode = value

    @property
    def org_code( self ) -> str:
        if self.__orgcode is not None:
            return self.__orgcode

    @org_code.setter
    def org_code( self, value: str ):
        if value is not None:
            self.__orgcode = value

    @property
    def rc_code( self ) -> str:
        if self.__rccode is not None:
            return self.__rccode

    @rc_code.setter
    def rc_code( self, value: str ):
        if value is not None:
            self.__rccode = value

    @property
    def rc_name( self ) -> str:
        if self.__rcname is not None:
            return self.__rcname

    @rc_name.setter
    def rc_name( self, value: str ):
        if value is not None:
            self.__rcname = value

    @property
    def vendor_code( self ) -> str:
        if self.__vendorcode is not None:
            return self.__vendorcode

    @vendor_code.setter
    def vendor_code( self, value: str ):
        if value is not None:
            self.__vendorcode = value

    @property
    def vendor_name( self ) -> str:
        if self.__vendorname is not None:
            return self.__vendorname

    @vendor_name.setter
    def vendor_name( self, value: str ):
        if value is not None:
            self.__vendorname = value

    @property
    def amount( self ) -> float:
        if self.__amount is not None:
            return self.__amount

    @amount.setter
    def amount( self, value: float ):
        if value is not None:
            self.__amount = value

    @property
    def open_commitments( self ) -> float:
        if self.__opencommitments is not None:
            return self.__opencommitments

    @open_commitments.setter
    def open_commitments( self, value: float ):
        if value is not None:
            self.__opencommitments = value

    @property
    def obligations( self ) -> float:
        if self.__obligations is not None:
            return self.__obligations

    @obligations.setter
    def obligations( self, value: float ):
        if value is not None:
            self.__obligations = value

    @property
    def unliquidated_obligations( self ) -> str:
        if self.__unliquidatedobligations is not None:
            return self.__unliquidatedobligations

    @unliquidated_obligations.setter
    def unliquidated_obligations( self, value: str ):
        if value is not None:
            self.__unliquidatedobligations = value

    @property
    def available( self ) -> float:
        if self.__avaialable is not None:
            return self.__avaialable

    @available.setter
    def available( self, value: float ):
        if value is not None:
            self.__avaialable = value

    @property
    def fields( self ) -> list[ str ]:
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value: list[ str ] ):
        if value is not None:
            self.__fields = value

    def __init__( self, number: str, provider: Provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.ReimbursableAgreements
        self.__agreementnumber = number
        self.__fields = [ 'ReimbursableAgreementsId'
                          'BFY',
                          'EFY',
                          'FundCode',
                          'RpioCode',
                          'AgreementNumber',
                          'StartDate',
                          'EndDate',
                          'RcCode',
                          'RcName',
                          'OrgCode',
                          'SiteProjectCode',
                          'AccountCode',
                          'VendorCode',
                          'VendorName',
                          'Amount',
                          'OpenCommitment',
                          'Obligation',
                          'ULO',
                          'Available' ]

    def __str__( self ) -> str:
        if self.__agreementnumber is not None:
            return self.__agreementnumber

    def get_data( self  ) -> list[ Row ]:
        try:
            _source = self.__source
            _provider = self.__provider
            _names = [ 'BFY', ]
            _values = (self.__bfy,)
            _dbconfig = DbConfig( _source, _provider )
            _sqlconfig = SqlConfig( names = _names, values = _values )
            _connection = Connection( self.__source )
            _sql = SqlStatement( _dbconfig, _sqlconfig )
            _sqlite = _connection.connect( )
            _cursor = _sqlite.cursor( )
            _query = _sql.get_query( )
            _db = _cursor.execute( _query )
            self.__data =  [ i for i in _db.fetchall( ) ]
            _cursor.close( )
            _sqlite.close( )
            return self.__data
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Reporting'
            _exc.cause = 'ObjectClassOutlay'
            _exc.method = 'get_data( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def get_frame( self ) -> DataFrame:
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            _source = self.__source
            _data = BudgetData( _source )
            return _data.create_frame( )
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Reporting'
            _exc.cause = 'ObjectClassOutlay'
            _exc.method = 'create_frame( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class RegionalAuthority( ):
    '''
    Constructor:  RegionalAuthority( bfy: str, efy: str,
     fund: str, pvdr: Provider = Provider.SQLite )

    Purpose:  Class defines object representing Regional Allocation
    '''
    __source = None
    __provider = None
    __regionalauthorityid = None
    __statusoffundsid = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __rpioname = None
    __fundcode = None
    __fundname = None
    __ahcode = None
    __ahname = None
    __orgcode = None
    __orgname = None
    __accountcode = None
    __boccode = None
    __bocname = None
    __rccode = None
    __rcname = None
    __amount = None
    __programprojectcode = None
    __programprojectname = None
    __programareacode = None
    __programareaname = None
    __goalcode = None
    __goalname = None
    __objectivecode = None
    __objectivename = None
    __npmcode = None
    __npmname = None
    __treasuryaccountcode = None
    __treasuryaccountname = None
    __budgetaccountcode = None
    __budgetaccountname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ) -> int:
        if self.__statusoffundsid is not None:
            return self.__statusoffundsid

    @id.setter
    def id( self, value: int ):
        if value is not None:
            self.__statusoffundsid = value

    @property
    def bfy( self ) -> str:
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value: str ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ) -> str:
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value: str ):
        if value is not None:
            self.__efy = value

    @property
    def rpio_code( self ) -> str:
        if self.__rpiocode is not None:
            return self.__rpiocode

    @rpio_code.setter
    def rpio_code( self, value: str ):
        if value is not None:
            self.__rpiocode = value

    @property
    def rpio_name( self ) -> str:
        if self.__rpioname is not None:
            return self.__rpioname

    @rpio_name.setter
    def rpio_name( self, value: str ):
        if value is not None:
            self.__rpioname = value

    @property
    def ah_code( self ) -> str:
        if self.__ahcode is not None:
            return self.__ahcode

    @ah_code.setter
    def ah_code( self, value: str ):
        if value is not None:
            self.__ahcode = value

    @property
    def ah_name( self ) -> str:
        if self.__ahname is not None:
            return self.__ahname

    @ah_name.setter
    def ah_name( self, value: str ):
        if value is not None:
            self.__ahname = value

    @property
    def fund_code( self ) -> str:
        if self.__fundcode is not None:
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value: str ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund_name( self ) -> str:
        if self.__fundname is not None:
            return self.__fundname

    @fund_name.setter
    def fund_name( self, value: str ):
        if value is not None:
            self.__fundname = value

    @property
    def org_code( self ) -> str:
        if self.__orgcode is not None:
            return self.__orgcode

    @org_code.setter
    def org_code( self, value: str ):
        if value is not None:
            self.__orgcode = value

    @property
    def org_name( self  ):
        if self.__orgname is not None:
            return self.__orgname

    @org_name.setter
    def org_name( self, value  ):
        if value is not None:
            self.__orgname = value

    @property
    def account_code( self ) -> str:
        if self.__accountcode is not None:
            return self.__accountcode

    @account_code.setter
    def account_code( self, value: str ):
        if value is not None:
            self.__accountcode = value

    @property
    def boc_code( self ) -> str:
        if self.__boccode is not None:
            return self.__boccode

    @boc_code.setter
    def boc_code( self, value: str ):
        if value is not None:
            self.__boccode = value

    @property
    def boc_name( self ) -> str:
        if self.__bocname is not None:
            return self.__bocname

    @boc_name.setter
    def boc_name( self, value: str ):
        if value is not None:
            self.__bocname = value

    @property
    def rc_code( self ) -> str:
        if self.__rccode is not None:
            return self.__rccode

    @rc_code.setter
    def rc_code( self, value: str ):
        if value is not None:
            self.__rccode = value

    @property
    def rc_name( self ) -> str:
        if self.__rcname is not None:
            return self.__rcname

    @rc_name.setter
    def rc_name( self, value: str ):
        if value is not None:
            self.__rcname = value

    @property
    def amount( self ) -> float:
        if self.__amount is not None:
            return self.__amount

    @amount.setter
    def amount( self, value: float ):
        if value is not None:
            self.__amount = value

    @property
    def budgeted( self ) -> str:
        if self.__budgeted is not None:
            return self.__budgeted

    @budgeted.setter
    def budgeted( self, value: str ):
        if value is not None:
            self.__budgeted = value

    @property
    def posted( self ) -> float:
        if self.__posted is not None:
            return self.__posted

    @posted.setter
    def posted( self, value: float ):
        if value is not None:
            self.__posted = value

    @property
    def open_commitments( self ) -> float:
        if self.__opencommitments is not None:
            return self.__opencommitments

    @open_commitments.setter
    def open_commitments( self, value: float ):
        if value is not None:
            self.__opencommitments = value

    @property
    def obligations( self ) -> float:
        if self.__obligations is not None:
            return self.__obligations

    @obligations.setter
    def obligations( self, value: float ):
        if value is not None:
            self.__obligations = value

    @property
    def unliquidated_obligations( self ) -> str:
        if self.__unliquidatedobligations is not None:
            return self.__unliquidatedobligations

    @unliquidated_obligations.setter
    def unliquidated_obligations( self, value: str ):
        if value is not None:
            self.__unliquidatedobligations = value

    @property
    def expenditures( self ) -> str:
        if self.__expenditures is not None:
            return self.__expenditures

    @expenditures.setter
    def expenditures( self, value: str ):
        if value is not None:
            self.__expenditures = value

    @property
    def used( self ) -> str:
        if self.__used is not None:
            return self.__used

    @used.setter
    def used( self, value: str ):
        if value is not None:
            self.__used = value

    @property
    def available( self ) -> float:
        if self.__avaialable is not None:
            return self.__avaialable

    @available.setter
    def available( self, value: float ):
        if value is not None:
            self.__avaialable = value

    @property
    def program_project_code( self ) -> str:
        if self.__programprojectcode is not None:
            return self.__programprojectcode

    @program_project_code.setter
    def program_project_code( self, value: str ):
        if value is not None:
            self.__programprojectcode = value

    @property
    def program_project_name( self ) -> str:
        if self.__programprojectname is not None:
            return self.__programprojectname

    @program_project_name.setter
    def program_project_name( self, value: str ):
        if value is not None:
            self.__programprojectname = value

    @property
    def program_area_code( self ) -> str:
        if self.__programareacode is not None:
            return self.__programareacode

    @program_area_code.setter
    def program_area_code( self, value: str ):
        if value is not None:
            self.__programareacode = value

    @property
    def program_area_name( self ) -> str:
        if self.__programareaname is not None:
            return self.__programareaname

    @program_area_name.setter
    def program_area_name( self, value: str ):
        if value is not None:
            self.__programareaname = value

    @property
    def goal_code( self ) -> str:
        if self.__goalcode is not None:
            return self.__goalcode

    @goal_code.setter
    def goal_code( self, value: str ):
        if value is not None:
            self.__goalcode = value

    @property
    def goal_name( self ) -> str:
        if self.__goalname is not None:
            return self.__goalname

    @goal_name.setter
    def goal_name( self, value: str ):
        if value is not None:
            self.__goalname = value

    @property
    def objective_code( self ) -> str:
        if self.__objectivecode is not None:
            return self.__objectivecode

    @objective_code.setter
    def objective_code( self, value: str ):
        if value is not None:
            self.__objectivecode = value

    @property
    def objective_name( self ) -> str:
        if self.__objectivename is not None:
            return self.__objectivename

    @objective_name.setter
    def objective_name( self, value: str ):
        if value is not None:
            self.__objectivename = value

    @property
    def npm_code( self ) -> str:
        if self.__npmcode is not None:
            return self.__npmcode

    @npm_code.setter
    def npm_code( self, value: str ):
        if value is not None:
            self.__npmcode = value

    @property
    def npm_name( self ) -> str:
        if self.__npmname is not None:
            return self.__npmname

    @npm_name.setter
    def npm_name( self, value: str ):
        if value is not None:
            self.__npmname = value

    @property
    def treasury_account_code( self ) -> str:
        if self.__treasuryaccountcode is not None:
            return self.__treasuryaccountcode

    @treasury_account_code.setter
    def treasury_account_code( self, value: str ):
        if value is not None:
            self.__treasuryaccountcode = value

    @property
    def treasury_account_name( self ) -> str:
        if self.__treasuryaccountname is not None:
            return self.__treasuryaccountname

    @treasury_account_name.setter
    def treasury_account_name( self, value: str ):
        if value is not None:
            self.__treasuryaccountname = value

    @property
    def budget_account_code( self ) -> str:
        if self.__budgetaccountcode is not None:
            return self.__budgetaccountcode

    @budget_account_code.setter
    def budget_account_code( self, value: str ):
        if value is not None:
            self.__budgetaccountcode = value

    @property
    def budget_account_name( self ) -> str:
        if self.__budgetaccountname is not None:
            return self.__budgetaccountname

    @budget_account_name.setter
    def budget_account_name( self, value: str ):
        if value is not None:
            self.__budgetaccountname = value

    @property
    def fields( self ) -> list[ str ]:
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value: list[ str ] ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy: str, efy: str, fund: str, provider: Provider = Provider.SQLite ):
        self.__source = Source.RegionalAuthority
        self.__provider = provider
        self.__bfy = bfy
        self.__efy = efy
        self.__fundcode = fund
        self.__fields = [ 'RegionalAuthorityId',
                           'AllocationsId',
                           'StatusOfFundsId',
                           'BudgetLevel',
                           'BFY',
                           'EFY',
                           'RpioCode',
                           'RpioName',
                           'AhCode',
                           'AhName',
                           'FundCode',
                           'FundName',
                           'OrgCode',
                           'OrgName',
                           'AccountCode',
                           'ProgramProjectCode',
                           'ProgramProjectName',
                           'ProgramAreaCode',
                           'ProgramAreaName',
                           'RcCode',
                           'RcName',
                           'BocCode',
                           'BocName',
                           'Amount',
                           'NpmCode',
                           'NpmName' ]

    def get_data( self  ) -> list[ Row ]:
        try:
            _source = self.__source
            _provider = self.__provider
            _names = [ 'BFY', 'RpioCode' ]
            _values = (self.__bfy, self.__rpiocode)
            _dbconfig = DbConfig( _source, _provider )
            _sqlconfig = SqlConfig( names = _names, values = _values )
            _connection = Connection( self.__source )
            _sql = SqlStatement( _dbconfig, _sqlconfig )
            _sqlite = _connection.connect( )
            _cursor = _sqlite.cursor( )
            _query = _sql.get_query( )
            _db = _cursor.execute( _query )
            self.__data =  [ i for i in _db.fetchall( ) ]
            _cursor.close( )
            _sqlite.close( )
            return self.__data
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Ninja'
            _exc.cause = 'RegionalAuthority'
            _exc.method = 'get_data( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def get_frame( self ) -> DataFrame:
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            _source = self.__source
            _data = BudgetData( _source )
            return _data.create_frame( )
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Ninja'
            _exc.cause = 'RegionalAuthority'
            _exc.method = 'create_frame( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class StatusOfFunds( ):
    '''
    Constructor:  StatusOfFunds( bfy: str, fund: str, pvdr: Provider = Provider.SQLite )

    Purpose:  Class defines object representing execution data
    '''
    __source = None
    __provider = None
    __statusoffundsid = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __rpioname = None
    __fundcode = None
    __fundname = None
    __ahcode = None
    __ahname = None
    __orgcode = None
    __orgname = None
    __accountcode = None
    __boccode = None
    __bocname = None
    __rccode = None
    __rcname = None
    __amount = None
    __budgeted = None
    __posted = None
    __opencommitments = None
    __obligations = None
    __unliquidatedobligations = None
    __expenditures = None
    __used = None
    __avaialable = None
    __programprojectcode = None
    __programprojectname = None
    __programareacode = None
    __programareaname = None
    __goalcode = None
    __goalname = None
    __objectivecode = None
    __objectivename = None
    __npmcode = None
    __npmname = None
    __treasuryaccountcode = None
    __treasuryaccountname = None
    __budgetaccountcode = None
    __budgetaccountname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ) -> int:
        if self.__statusoffundsid is not None:
            return self.__statusoffundsid

    @id.setter
    def id( self, value: int ):
        if value is not None:
            self.__statusoffundsid = value

    @property
    def bfy( self ) -> str:
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value: str ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ) -> str:
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value: str ):
        if value is not None:
            self.__efy = value

    @property
    def rpio_code( self ) -> str:
        if self.__rpiocode is not None:
            return self.__rpiocode

    @rpio_code.setter
    def rpio_code( self, value: str ):
        if value is not None:
            self.__rpiocode = value

    @property
    def rpio_name( self ) -> str:
        if self.__rpioname is not None:
            return self.__rpioname

    @rpio_name.setter
    def rpio_name( self, value: str ):
        if value is not None:
            self.__rpioname = value

    @property
    def ah_code( self ) -> str:
        if self.__ahcode is not None:
            return self.__ahcode

    @ah_code.setter
    def ah_code( self, value: str ):
        if value is not None:
            self.__ahcode = value

    @property
    def ah_name( self ) -> str:
        if self.__ahname is not None:
            return self.__ahname

    @ah_name.setter
    def ah_name( self, value: str ):
        if value is not None:
            self.__ahname = value

    @property
    def fund_code( self ) -> str:
        if self.__fundcode is not None:
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value: str ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund_name( self ) -> str:
        if self.__fundname is not None:
            return self.__fundname

    @fund_name.setter
    def fund_name( self, value: str ):
        if value is not None:
            self.__fundname = value

    @property
    def org_code( self ) -> str:
        if self.__orgcode is not None:
            return self.__orgcode

    @org_code.setter
    def org_code( self, value: str ):
        if value is not None:
            self.__orgcode = value

    @property
    def org_name( self  ):
        if self.__orgname is not None:
            return self.__orgname

    @org_name.setter
    def org_name( self, value  ):
        if value is not None:
            self.__orgname = value

    @property
    def account_code( self ) -> str:
        if self.__accountcode is not None:
            return self.__accountcode

    @account_code.setter
    def account_code( self, value: str ):
        if value is not None:
            self.__accountcode = value

    @property
    def boc_code( self ) -> str:
        if self.__boccode is not None:
            return self.__boccode

    @boc_code.setter
    def boc_code( self, value: str ):
        if value is not None:
            self.__boccode = value

    @property
    def boc_name( self ) -> str:
        if self.__bocname is not None:
            return self.__bocname

    @boc_name.setter
    def boc_name( self, value: str ):
        if value is not None:
            self.__bocname = value

    @property
    def rc_code( self ) -> str:
        if self.__rccode is not None:
            return self.__rccode

    @rc_code.setter
    def rc_code( self, value: str ):
        if value is not None:
            self.__rccode = value

    @property
    def rc_name( self ) -> str:
        if self.__rcname is not None:
            return self.__rcname

    @rc_name.setter
    def rc_name( self, value: str ):
        if value is not None:
            self.__rcname = value

    @property
    def amount( self ) -> float:
        if self.__amount is not None:
            return self.__amount

    @amount.setter
    def amount( self, value: float ):
        if value is not None:
            self.__amount = value

    @property
    def budgeted( self ) -> str:
        if self.__budgeted is not None:
            return self.__budgeted

    @budgeted.setter
    def budgeted( self, value: str ):
        if value is not None:
            self.__budgeted = value

    @property
    def posted( self ) -> float:
        if self.__posted is not None:
            return self.__posted

    @posted.setter
    def posted( self, value: float ):
        if self.__posted is not None:
            self.__posted = value

    @property
    def open_commitments( self ) -> float:
        if self.__opencommitments is not None:
            return self.__opencommitments

    @open_commitments.setter
    def open_commitments( self, value: float ):
        if value is not None:
            self.__opencommitments = value

    @property
    def obligations( self ) -> float:
        if self.__obligations is not None:
            return self.__obligations

    @obligations.setter
    def obligations( self, value: float ):
        if value is not None:
            self.__obligations = value

    @property
    def unliquidated_obligations( self ) -> float:
        if self.__unliquidatedobligations is not None:
            return self.__unliquidatedobligations

    @unliquidated_obligations.setter
    def unliquidated_obligations( self, value: float ):
        if value is not None:
            self.__unliquidatedobligations = value

    @property
    def expenditures( self ) -> float:
        if isinstance( self.__expenditures, float ):
            return self.__expenditures

    @expenditures.setter
    def expenditures( self, value: float ):
        if value is not None:
            self.__expenditures = value

    @property
    def used( self ) -> float:
        if self.__used is not None:
            return self.__used

    @used.setter
    def used( self, value: float ):
        if value is not None:
            self.__used = value

    @property
    def available( self ) -> float:
        if self.__avaialable is not None:
            return self.__avaialable

    @available.setter
    def available( self, value: float ):
        if value is not None:
            self.__avaialable = value

    @property
    def program_project_code( self ) -> str:
        if self.__programprojectcode is not None:
            return self.__programprojectcode

    @program_project_code.setter
    def program_project_code( self, value: str ):
        if value is not None:
            self.__programprojectcode = value

    @property
    def program_project_name( self ) -> str:
        if self.__programprojectname is not None:
            return self.__programprojectname

    @program_project_name.setter
    def program_project_name( self, value: str ):
        if value is not None:
            self.__programprojectname = value

    @property
    def program_area_code( self ) -> str:
        if self.__programareacode is not None:
            return self.__programareacode

    @program_area_code.setter
    def program_area_code( self, value: str ):
        if value is not None:
            self.__programareacode = value

    @property
    def program_area_name( self ) -> str:
        if self.__programareaname is not None:
            return self.__programareaname

    @program_area_name.setter
    def program_area_name( self, value: str ):
        if value is not None:
            self.__programareaname = value

    @property
    def goal_code( self ) -> str:
        if self.__goalcode is not None:
            return self.__goalcode

    @goal_code.setter
    def goal_code( self, value: str ):
        if value is not None:
            self.__goalcode = value

    @property
    def goal_name( self ) -> str:
        if self.__goalname is not None:
            return self.__goalname

    @goal_name.setter
    def goal_name( self, value: str ):
        if value is not None:
            self.__goalname = value

    @property
    def objective_code( self ) -> str:
        if self.__objectivecode is not None:
            return self.__objectivecode

    @objective_code.setter
    def objective_code( self, value: str ):
        if value is not None:
            self.__objectivecode = value

    @property
    def objective_name( self ) -> str:
        if self.__objectivename is not None:
            return self.__objectivename

    @objective_name.setter
    def objective_name( self, value: str ):
        if value is not None:
            self.__objectivename = value

    @property
    def npm_code( self ) -> str:
        if self.__npmcode is not None:
            return self.__npmcode

    @npm_code.setter
    def npm_code( self, value: str ):
        if value is not None:
            self.__npmcode = value

    @property
    def npm_name( self ) -> str:
        if self.__npmname is not None:
            return self.__npmname

    @npm_name.setter
    def npm_name( self, value: str ):
        if value is not None:
            self.__npmname = value

    @property
    def treasury_account_code( self ) -> str:
        if self.__treasuryaccountcode is not None:
            return self.__treasuryaccountcode

    @treasury_account_code.setter
    def treasury_account_code( self, value: str ):
        if value is not None:
            self.__treasuryaccountcode = value

    @property
    def treasury_account_name( self ) -> str:
        if self.__treasuryaccountname is not None:
            return self.__treasuryaccountname

    @treasury_account_name.setter
    def treasury_account_name( self, value: str ):
        if value is not None:
            self.__treasuryaccountname = value

    @property
    def budget_account_code( self ) -> str:
        if self.__budgetaccountcode is not None:
            return self.__budgetaccountcode

    @budget_account_code.setter
    def budget_account_code( self, value: str ):
        if value is not None:
            self.__budgetaccountcode = value

    @property
    def budget_account_name( self ) -> str:
        if self.__budgetaccountname is not None:
            return self.__budgetaccountname

    @budget_account_name.setter
    def budget_account_name( self, value: str ):
        if value is not None:
            self.__budgetaccountname = value

    @property
    def fields( self ) -> list[ str ]:
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value: list[ str ] ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy: str, fund: str, provider: Provider = Provider.SQLite ):
        self.__source = Source.StatusOfFunds
        self.__provider = provider
        self.__bfy = bfy
        self.__fundcode = fund
        self.__fields = [ 'StatusOfFundsId',
                           'BudgetLevel',
                           'BFY',
                           'EFY',
                           'RpioCode',
                           'RpioName',
                           'AhCode',
                           'AhName',
                           'FundCode',
                           'FundName',
                           'OrgCode',
                           'OrgName',
                           'AccountCode',
                           'BocCode',
                           'BocName',
                           'ProgramProjectCode',
                           'ProgramProjectName',
                           'ProgramAreaCode',
                           'ProgramAreaName',
                           'RcCode',
                           'RcName',
                           'LowerName',
                           'Amount',
                           'Budgeted',
                           'Posted',
                           'OpenCommitment',
                           'ULO',
                           'Expenditure',
                           'Obligation',
                           'Used',
                           'Available',
                           'NpmCode',
                           'NpmName' ]

    def get_data( self  ) -> list[ Row ]:
        try:
            _source = self.__source
            _provider = self.__provider
            _dbconfig = DbConfig( _source, _provider )
            _sqlconfig = SqlConfig( )
            _connection = Connection( self.__source )
            _sql = SqlStatement( _dbconfig, _sqlconfig )
            _sqlite = _connection.connect( )
            _cursor = _sqlite.cursor( )
            _query = _sql.get_query( )
            _db = _cursor.execute( _query )
            self.__data =  [ i for i in _db.fetchall( ) ]
            _cursor.close( )
            _sqlite.close( )
            return self.__data
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Ninja'
            _exc.cause = 'StatusOfFunds'
            _exc.method = 'get_data( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def get_frame( self ) -> DataFrame:
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            _source = self.__source
            _data = BudgetData( _source )
            return _data.create_frame( )
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Ninja'
            _exc.cause = 'StatusOfFunds'
            _exc.method = 'create_frame( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class StatusOfSupplementalFunding( ):
    '''
    Constructor:  StatusOfFunds( bfy: str, efy: str,
    fund: str, pvdr: Provider = Provider.SQLite )

    Purpose:  Class representing Supplemental Funding execution data
    '''
    __source = None
    __provider = None
    __statusofsupplementalfundsid = None
    __statusoffundsid = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __rpioname = None
    __fundcode = None
    __fundname = None
    __ahcode = None
    __ahname = None
    __orgcode = None
    __orgname = None
    __accountcode = None
    __boccode = None
    __bocname = None
    __rccode = None
    __rcname = None
    __amount = None
    __budgeted = None
    __posted = None
    __opencommitments = None
    __obligations = None
    __unliquidatedobligations = None
    __expenditures = None
    __used = None
    __avaialable = None
    __programprojectcode = None
    __programprojectname = None
    __programareacode = None
    __programareaname = None
    __goalcode = None
    __goalname = None
    __objectivecode = None
    __objectivename = None
    __npmcode = None
    __npmname = None
    __treasuryaccountcode = None
    __treasuryaccountname = None
    __budgetaccountcode = None
    __budgetaccountname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ) -> int:
        if self.__statusoffundsid is not None:
            return self.__statusoffundsid

    @id.setter
    def id( self, value: int ):
        if  value is not None:
            self.__statusoffundsid = value

    @property
    def bfy( self ) -> str:
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value: str ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ) -> str:
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value: str ):
        if value is not None:
            self.__efy = value

    @property
    def rpio_code( self ) -> str:
        if self.__rpiocode is not None:
            return self.__rpiocode

    @rpio_code.setter
    def rpio_code( self, value: str ):
        if value is not None:
            self.__rpiocode = value

    @property
    def rpio_name( self ) -> str:
        if self.__rpioname is not None:
            return self.__rpioname

    @rpio_name.setter
    def rpio_name( self, value: str ):
        if value is not None:
            self.__rpioname = value

    @property
    def ah_code( self ) -> str:
        if self.__ahcode is not None:
            return self.__ahcode

    @ah_code.setter
    def ah_code( self, value: str ):
        if value is not None:
            self.__ahcode = value

    @property
    def ah_name( self ) -> str:
        if self.__ahname is not None:
            return self.__ahname

    @ah_name.setter
    def ah_name( self, value: str ):
        if value is not None:
            self.__ahname = value

    @property
    def fund_code( self ) -> str:
        if self.__fundcode is not None:
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value: str ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund_name( self ) -> str:
        if self.__fundname is not None:
            return self.__fundname

    @fund_name.setter
    def fund_name( self, value: str ):
        if value is not None:
            self.__fundname = value

    @property
    def org_code( self ) -> str:
        if self.__orgcode is not None:
            return self.__orgcode

    @org_code.setter
    def org_code( self, value: str ):
        if value is not None:
            self.__orgcode = value

    @property
    def org_name( self  ):
        if self.__orgname is not None:
            return self.__orgname

    @org_name.setter
    def org_name( self, value  ):
        if value is not None:
            self.__orgname = value

    @property
    def account_code( self ) -> str:
        if self.__accountcode is not None:
            return self.__accountcode

    @account_code.setter
    def account_code( self, value: str ):
        if value is not None:
            self.__accountcode = value

    @property
    def boc_code( self ) -> str:
        if self.__boccode is not None:
            return self.__boccode

    @boc_code.setter
    def boc_code( self, value: str ):
        if value is not None:
            self.__boccode = value

    @property
    def boc_name( self ) -> str:
        if self.__bocname is not None:
            return self.__bocname

    @boc_name.setter
    def boc_name( self, value: str ):
        if value is not None:
            self.__bocname = value

    @property
    def rc_code( self ) -> str:
        if self.__rccode is not None:
            return self.__rccode

    @rc_code.setter
    def rc_code( self, value: str ):
        if value is not None:
            self.__rccode = value

    @property
    def rc_name( self ) -> str:
        if self.__rcname is not None:
            return self.__rcname

    @rc_name.setter
    def rc_name( self, value: str ):
        if value is not None:
            self.__rcname = value

    @property
    def amount( self ) -> float:
        if self.__amount is not None:
            return self.__amount

    @amount.setter
    def amount( self, value: float ):
        if value is not None:
            self.__amount = value

    @property
    def budgeted( self ) -> str:
        if self.__budgeted is not None:
            return self.__budgeted

    @budgeted.setter
    def budgeted( self, value: str ):
        if value is not None:
            self.__budgeted = value

    @property
    def posted( self ) -> float:
        if self.__posted is not None:
            return self.__posted

    @posted.setter
    def posted( self, value: float ):
        if value is not None:
            self.__posted = value

    @property
    def open_commitments( self ) -> float:
        if self.__opencommitments is not None:
            return self.__opencommitments

    @open_commitments.setter
    def open_commitments( self, value: float ):
        if value is not None:
            self.__opencommitments = value

    @property
    def obligations( self ) -> float:
        if self.__obligations is not None:
            return self.__obligations

    @obligations.setter
    def obligations( self, value: float ):
        if value is not None:
            self.__obligations = value

    @property
    def unliquidated_obligations( self ) -> str:
        if self.__unliquidatedobligations is not None:
            return self.__unliquidatedobligations

    @unliquidated_obligations.setter
    def unliquidated_obligations( self, value: str ):
        if value is not None:
            self.__unliquidatedobligations = value

    @property
    def expenditures( self ) -> str:
        if self.__expenditures is not None:
            return self.__expenditures

    @expenditures.setter
    def expenditures( self, value: str ):
        if value is not None:
            self.__expenditures = value

    @property
    def used( self ) -> str:
        if self.__used is not None:
            return self.__used

    @used.setter
    def used( self, value: str ):
        if value is not None:
            self.__used = value

    @property
    def available( self ) -> float:
        if self.__avaialable is not None:
            return self.__avaialable

    @available.setter
    def available( self, value: float ):
        if value is not None:
            self.__avaialable = value

    @property
    def program_project_code( self ) -> str:
        if self.__programprojectcode is not None:
            return self.__programprojectcode

    @program_project_code.setter
    def program_project_code( self, value: str ):
        if value is not None:
            self.__programprojectcode = value

    @property
    def program_project_name( self ) -> str:
        if self.__programprojectname is not None:
            return self.__programprojectname

    @program_project_name.setter
    def program_project_name( self, value: str ):
        if value is not None:
            self.__programprojectname = value

    @property
    def program_area_code( self ) -> str:
        if self.__programareacode is not None:
            return self.__programareacode

    @program_area_code.setter
    def program_area_code( self, value: str ):
        if value is not None:
            self.__programareacode = value

    @property
    def program_area_name( self ) -> str:
        if self.__programareaname is not None:
            return self.__programareaname

    @program_area_name.setter
    def program_area_name( self, value: str ):
        if value is not None:
            self.__programareaname = value

    @property
    def goal_code( self ) -> str:
        if self.__goalcode is not None:
            return self.__goalcode

    @goal_code.setter
    def goal_code( self, value: str ):
        if value is not None:
            self.__goalcode = value

    @property
    def goal_name( self ) -> str:
        if self.__goalname is not None:
            return self.__goalname

    @goal_name.setter
    def goal_name( self, value: str ):
        if value is not None:
            self.__goalname = value

    @property
    def objective_code( self ) -> str:
        if self.__objectivecode is not None:
            return self.__objectivecode

    @objective_code.setter
    def objective_code( self, value: str ):
        if value is not None:
            self.__objectivecode = value

    @property
    def objective_name( self ) -> str:
        if self.__objectivename is not None:
            return self.__objectivename

    @objective_name.setter
    def objective_name( self, value: str ):
        if value is not None:
            self.__objectivename = value

    @property
    def npm_code( self ) -> str:
        if self.__npmcode is not None:
            return self.__npmcode

    @npm_code.setter
    def npm_code( self, value: str ):
        if value is not None:
            self.__npmcode = value

    @property
    def npm_name( self ) -> str:
        if self.__npmname is not None:
            return self.__npmname

    @npm_name.setter
    def npm_name( self, value: str ):
        if value is not None:
            self.__npmname = value

    @property
    def treasury_account_code( self ) -> str:
        if self.__treasuryaccountcode is not None:
            return self.__treasuryaccountcode

    @treasury_account_code.setter
    def treasury_account_code( self, value: str ):
        if value is not None:
            self.__treasuryaccountcode = value

    @property
    def treasury_account_name( self ) -> str:
        if self.__treasuryaccountname is not None:
            return self.__treasuryaccountname

    @treasury_account_name.setter
    def treasury_account_name( self, value: str ):
        if value is not None:
            self.__treasuryaccountname = value

    @property
    def budget_account_code( self ) -> str:
        if self.__budgetaccountcode is not None:
            return self.__budgetaccountcode

    @budget_account_code.setter
    def budget_account_code( self, value: str ):
        if value is not None:
            self.__budgetaccountcode = value

    @property
    def budget_account_name( self ) -> str:
        if self.__budgetaccountname is not None:
            return self.__budgetaccountname

    @budget_account_name.setter
    def budget_account_name( self, value: str ):
        if value is not None:
            self.__budgetaccountname = value

    @property
    def fields( self ) -> list[ str ]:
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value: list[ str ] ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy: str, efy: str, fund: str, provider: Provider = Provider.SQLite ):
        self.__source = Source.StatusOfSupplementalFunding
        self.__provider = Provider.SQLite
        self.__bfy = bfy
        self.__efy = efy
        self.__fundcode = fund
        self.__fields = [ 'StatusOfFundsId',
                           'BudgetLevel',
                           'BFY',
                           'EFY',
                           'RpioCode',
                           'RpioName',
                           'AhCode',
                           'AhName',
                           'FundCode',
                           'FundName',
                           'OrgCode',
                           'OrgName',
                           'AccountCode',
                           'BocCode',
                           'BocName',
                           'ProgramProjectCode',
                           'ProgramProjectName',
                           'ProgramAreaCode',
                           'ProgramAreaName',
                           'RcCode',
                           'RcName',
                           'LowerName',
                           'Amount',
                           'Budgeted',
                           'Posted',
                           'OpenCommitment',
                           'ULO',
                           'Expenditure',
                           'Obligation',
                           'Used',
                           'Available',
                           'NpmCode',
                           'NpmName' ]


    def get_data( self  ) -> list[ Row ]:
        try:
            _source = self.__source
            _provider = self.__provider
            _names = [ 'BFY', 'FundCode' ]
            _values = (self.__bfy, self.__fundcode)
            _dbconfig = DbConfig( _source, _provider )
            _sqlconfig = SqlConfig( names = _names, values = _values )
            _connection = Connection( self.__source )
            _sql = SqlStatement( _dbconfig, _sqlconfig )
            _sqlite = _connection.connect( )
            _cursor = _sqlite.cursor( )
            _query = _sql.get_query( )
            _db = _cursor.execute( _query )
            self.__data =  [ i for i in _db.fetchall( ) ]
            _cursor.close( )
            _sqlite.close( )
            return self.__data
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Ninja'
            _exc.cause = 'StatusOfSupplementalFunding'
            _exc.method = 'get_data( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def get_frame( self ) -> DataFrame:
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            _source = self.__source
            _data = BudgetData( _source )
            return _data.create_frame( )
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Ninja'
            _exc.cause = 'StatusOfSupplementalFunding'
            _exc.method = 'create_frame( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class StateGrantObligation( ):
    '''
    Constructor:  StateGrantObligation( bfy: str, rpio: str, pvdr: Provider = Provider.SQLite )

    Purpose:  Class defines object representing the BIS
    '''
    __source = None
    __provider = None
    __stategrantobligationsid = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __rpioname = None
    __fundcode = None
    __fundname = None
    __ahcode = None
    __ahname = None
    __orgcode = None
    __orgname = None
    __accountcode = None
    __rccode = None
    __rcname = None
    __boccode = None
    __bocname = None
    __statecode = None
    __statename = None
    __amount = None
    __treasuryaccountcode = None
    __treasuryaccountname = None
    __budgetaccountcode = None
    __budgetaccountname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ) -> int:
        if self.__stategrantobligationsid is not None:
            return self.__stategrantobligationsid

    @id.setter
    def id( self, value: int ):
        if value is not None:
            self.__stategrantobligationsid = value

    @property
    def bfy( self ) -> str:
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value: str ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ) -> str:
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value: str ):
        if value is not None:
            self.__efy = value

    @property
    def rpio_code( self ) -> str:
        if self.__rpiocode is not None:
            return self.__rpiocode

    @rpio_code.setter
    def rpio_code( self, value: str ):
        if value is not None:
            self.__rpiocode = value

    @property
    def rpio_name( self ) -> str:
        if self.__rpioname is not None:
            return self.__rpioname

    @rpio_name.setter
    def rpio_name( self, value: str ):
        if value is not None:
            self.__rpioname = value

    @property
    def ah_code( self ) -> str:
        if self.__ahcode is not None:
            return self.__ahcode

    @ah_code.setter
    def ah_code( self, value: str ):
        if value is not None:
            self.__ahcode = value

    @property
    def ah_name( self ) -> str:
        if self.__ahname is not None:
            return self.__ahname

    @ah_name.setter
    def ah_name( self, value: str ):
        if value is not None:
            self.__ahname = value

    @property
    def fund_code( self ) -> str:
        if self.__fundcode is not None:
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value: str ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund_name( self ) -> str:
        if self.__fundname is not None:
            return self.__fundname

    @fund_name.setter
    def fund_name( self, value: str ):
        if value is not None:
            self.__fundname = value

    @property
    def org_code( self ) -> str:
        if self.__orgcode is not None:
            return self.__orgcode

    @org_code.setter
    def org_code( self, value: str ):
        if value is not None:
            self.__orgcode = value

    @property
    def org_name( self  ):
        if self.__orgname is not None:
            return self.__orgname

    @org_name.setter
    def org_name( self, value  ):
        if value is not None:
            self.__orgname = value

    @property
    def account_code( self ) -> str:
        if self.__accountcode is not None:
            return self.__accountcode

    @account_code.setter
    def account_code( self, value: str ):
        if value is not None:
            self.__accountcode = value

    @property
    def boc_code( self ) -> str:
        if self.__boccode is not None:
            return self.__boccode

    @boc_code.setter
    def boc_code( self, value: str ):
        if value is not None:
            self.__boccode = value

    @property
    def boc_name( self ) -> str:
        if self.__bocname is not None:
            return self.__bocname

    @boc_name.setter
    def boc_name( self, value: str ):
        if value is not None:
            self.__bocname = value

    @property
    def rc_code( self ) -> str:
        if self.__rccode is not None:
            return self.__rccode

    @rc_code.setter
    def rc_code( self, value: str ):
        if value is not None:
            self.__rccode = value

    @property
    def rc_name( self ) -> str:
        if self.__rcname is not None:
            return self.__rcname

    @rc_name.setter
    def rc_name( self, value: str ):
        if value is not None:
            self.__rcname = value

    @property
    def state_code( self ) -> str:
        if self.__statecode is not None:
            return self.__statecode

    @state_code.setter
    def state_code( self, value: str ):
        if value is not None:
            self.__statecode = value

    @property
    def state_name( self ) -> str:
        if self.__statename is not None:
            return self.__statename

    @state_name.setter
    def state_name( self, value: str ):
        if value is not None:
            self.__statename = value

    @property
    def amount( self ) -> float:
        if isinstance( self.__amount, float ):
            return self.__amount

    @amount.setter
    def amount( self, value: float ):
        if value is not None:
            self.__amount = value

    @property
    def treasury_account_code( self ) -> str:
        if self.__treasuryaccountcode is not None:
            return self.__treasuryaccountcode

    @treasury_account_code.setter
    def treasury_account_code( self, value: str ):
        if value is not None:
            self.__treasuryaccountcode = value

    @property
    def treasury_account_name( self ) -> str:
        if self.__treasuryaccountname is not None:
            return self.__treasuryaccountname

    @treasury_account_name.setter
    def treasury_account_name( self, value: str ):
        if value is not None:
            self.__treasuryaccountname = value

    @property
    def budget_account_code( self ) -> str:
        if self.__budgetaccountcode is not None:
            return self.__budgetaccountcode

    @budget_account_code.setter
    def budget_account_code( self, value: str ):
        if value is not None:
            self.__budgetaccountcode = value

    @property
    def budget_account_name( self ) -> str:
        if self.__budgetaccountname is not None:
            return self.__budgetaccountname

    @budget_account_name.setter
    def budget_account_name( self, value: str ):
        if value is not None:
            self.__budgetaccountname = value

    @property
    def fields( self ) -> list[ str ]:
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value: list[ str ] ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy: str, rpio: str, provider: Provider = Provider.SQLite ):
        self.__source = Source.StateGrantObligations
        self.__provider = provider
        self.__bfy = bfy
        self.__rpiocode = rpio
        self.__fields = [ 'StateGrantObligationsId',
                           'RpioCode',
                           'RpioName',
                           'FundCode',
                           'FundName',
                           'AhCode',
                           'AhName',
                           'OrgCode',
                           'OrgName',
                           'StateCode',
                           'StateName',
                           'AccountCode',
                           'ProgramProjectCode',
                           'ProgramProjectName',
                           'RcCode',
                           'RcName',
                           'BocCode',
                           'BocName',
                           'Amount' ]

    def get_data( self  ) -> list[ Row ]:
        try:
            _source = self.__source
            _provider = self.__provider
            _names = [ 'BFY', 'RpioCode' ]
            _values = (self.__rpiocode, self.__rpiocode)
            _dbconfig = DbConfig( _source, _provider )
            _sqlconfig = SqlConfig( names = _names, values = _values )
            _connection = Connection( self.__source )
            _sql = SqlStatement( _dbconfig, _sqlconfig )
            _sqlite = _connection.connect( )
            _cursor = _sqlite.cursor( )
            _query = _sql.get_query( )
            _db = _cursor.execute( _query )
            self.__data =  [ i for i in _db.fetchall( ) ]
            _cursor.close( )
            _sqlite.close( )
            return self.__data
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Ninja'
            _exc.cause = 'StateGrantObligation'
            _exc.method = 'get_data( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def get_frame( self ) -> DataFrame:
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            _source = self.__source
            _data = BudgetData( _source )
            return _data.create_frame( )
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Ninja'
            _exc.cause = 'StateGrantObligation'
            _exc.method = 'create_frame( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class StatusOfSpecialAccountFunds( ):
    '''
     Constructor:  StatusOfSpecialAccountFunds( bfy = None, fund = None,
                  account = None, boc = None, pvdr = Provider.SQLite )

     Purpose: Class defines object providing SF Special Account data
     '''
    __source = None
    __provider = None
    __specialaccountsid = None
    __bfy = None
    __efy = None
    __fundcode = None
    __fundname = None
    __rpiocode = None
    __rpioname = None
    __specialaccountnumber = None
    __specialaccountname = None
    __specialaccountstatus = None
    __nplstatusname = None
    __nplstatuscode = None
    __epasiteid = None
    __cerclisid = None
    __sitecode = None
    __sitename = None
    __operableunit = None
    __pipelinecode = None
    __pipelinedescription = None
    __programcode = None
    __interestdate = None
    __trustfundtransfer = None
    __transactiontype = None
    __transactiondescription = None
    __availablebalance = None
    __opencommitments = None
    __obligations = None
    __unliquidatedobligations = None
    __disbursements = None
    __unpaidbalances = None
    __collectionsandinterest = None
    __cumulativereciepts = None
    __netreceipts = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ) -> int:
        if self.__specialaccountsid is not None:
            return self.__specialaccountsid

    @id.setter
    def id( self, value: int ):
        if value is not None:
            self.__specialaccountsid = value

    @property
    def bfy( self ) -> str:
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value: str ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ) -> str:
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value: str ):
        if value is not None:
            self.__efy = value

    @property
    def rpio_code( self ) -> str:
        if self.__rpiocode is not None:
            return self.__rpiocode

    @rpio_code.setter
    def rpio_code( self, value: str ):
        if value is not None:
            self.__rpiocode = value

    @property
    def rpio_name( self ) -> str:
        if self.__rpioname is not None:
            return self.__rpioname

    @rpio_name.setter
    def rpio_name( self, value: str ):
        if value is not None:
            self.__rpioname = value

    @property
    def site_code( self ) -> str:
        if self.__sitecode is not None:
            return self.__sitecode

    @site_code.setter
    def site_code( self, value: str ):
        if value is not None:
            self.__sitecode = value

    @property
    def site_name( self ) -> str:
        if self.__sitename is not None:
            return self.__sitename

    @site_name.setter
    def site_name( self, value: str ):
        if value is not None:
            self.__sitename = value

    @property
    def program_code( self ) -> str:
        if self.__programcode is not None:
            return self.__programcode

    @program_code.setter
    def program_code( self, value: str ):
        if value is not None:
            self.__programcode = value

    @property
    def interest_date( self ) -> datetime:
        if self.__interestdate is not None:
            return self.__interestdate

    @interest_date.setter
    def interest_date( self, value: datetime ):
        if value is not None:
            self.__interestdate = value

    @property
    def trustfund_transfer( self ) -> float:
        if self.__trustfundtransfer is not None:
            return self.__trustfundtransfer

    @trustfund_transfer.setter
    def trustfund_transfer( self, value: float ):
        if value is not None:
            self.__trustfundtransfer = value

    @property
    def special_account_number( self ) -> str:
        if self.__specialaccountnumber is not None:
            return self.__specialaccountnumber

    @special_account_number.setter
    def special_account_number( self, value: str ):
        if value is not None:
            self.__specialaccountnumber = value

    @property
    def special_account_name( self ) -> str:
        if self.__specialaccountnumber is not None:
            return self.__specialaccountnumber

    @special_account_name.setter
    def special_account_name( self, value: str ):
        if value is not None:
            self.__specialaccountnumber = value

    @property
    def special_account_status( self ) -> str:
        if self.__specialaccountstatus is not None:
            return self.__specialaccountstatus

    @special_account_status.setter
    def special_account_status( self, value: str ):
        if value is not None:
            self.__specialaccountstatus = value

    @property
    def npl_status_code( self ) -> str:
        if self.__nplstatuscode is not None:
            return self.__nplstatuscode

    @npl_status_code.setter
    def npl_status_code( self, value: str ):
        if value is not None:
            self.__nplstatuscode = value

    @property
    def npl_status_name( self ) -> str:
        if self.__nplstatusname is not None:
            return self.__nplstatusname

    @npl_status_name.setter
    def npl_status_name( self, value: str ):
        if value is not None:
            self.__nplstatusname = value

    @property
    def epa_site_id( self ) -> str:
        if self.__epasiteid is not None:
            return self.__epasiteid

    @epa_site_id.setter
    def epa_site_id( self, value: str ):
        if value is not None:
            self.__value = value

    @property
    def cerclis_id( self ) -> str:
        if self.__cerclisid is not None:
            return self.__cerclisid

    @cerclis_id.setter
    def cerclis_id( self, value: str ):
        if value is not None:
            self.__cerclisid = value

    @property
    def trustfund_transfer( self ) -> float:
        if self.__trustfundtransfer is not None:
            return self.__trustfundtransfer

    @trustfund_transfer.setter
    def trustfund_transfer( self, value: float ):
        if value is not None:
            self.__trustfundtransfer = value

    @property
    def open_commitments( self ) -> float:
        if self.__opencommitments is not None:
            return self.__opencommitments

    @open_commitments.setter
    def open_commitments( self, value: float ):
        if value is not None:
            self.__opencommitments = value

    @property
    def obligations( self ) -> float:
        if self.__obligations is not None:
            return self.__obligations

    @obligations.setter
    def obligations( self, value: float ):
        if value is not None:
            self.__obligations = value

    @property
    def unliquidated_obligations( self ) -> float:
        if self.__unliquidatedobligations is not None:
            return self.__unliquidatedobligations

    @unliquidated_obligations.setter
    def unliquidated_obligations( self, value: float ):
        if value is not None:
            self.__unliquidatedobligations = value

    @property
    def disbursements( self ) -> float:
        if self.__disbursements is not None:
            return self.__disbursements

    @disbursements.setter
    def disbursements( self, value: float ):
        if value is not None:
            self.__disbursements = value

    @property
    def unpaid_balances( self ) -> float:
        if self.__unpaidbalances is not None:
            return self.__unpaidbalances

    @unpaid_balances.setter
    def unpaid_balances( self, value: float ):
        if value is not None:
            self.__unpaidbalances = value

    @property
    def cumulative_receipts( self ) -> float:
        if self.__cumulativereceipts is not None:
            return self.__cumulativereceipts

    @cumulative_receipts.setter
    def cumulative_receipts( self, value: float ):
        if value is not None:
            self.__cumulativereceipts = value

    @property
    def net_receipts( self ) -> float:
        if self.__netreceipts is not None:
            return self.__netreceipts

    @net_receipts.setter
    def net_receipts( self, value: float ):
        if value is not None:
            self.__netreceipts = value

    @property
    def collections_and_interest( self ) -> float:
        if self.__collectionsandinterest is not None:
            return self.__collectionsandinterest

    @collections_and_interest.setter
    def collections_and_interest( self, value: float ):
        if value is not None:
            self.__collectionsandinterest = value

    @property
    def fields( self ) -> list[ str ]:
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value: list[ str ] ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy = None, fund = None,
                  account = None, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.StatusOfSpecialAccountFunds
        self.__bfy = bfy
        self.__fundcode = fund
        self.__programcode = account
        self.__fields = [ 'SpecialAccountsId',
                           'BFY',
                           'RpioCode',
                           'FundCode',
                           'SpecialAccountFund',
                           'SpecialAccountNumber',
                           'SpecialAccountName',
                           'AccountStatus',
                           'NplStatusCode',
                           'NplStatusName',
                           'SiteId',
                           'CerclisId',
                           'SiteCode',
                           'SiteName',
                           'OperableUnit',
                           'PipelineCode',
                           'PipelineDescription',
                           'AccountCode',
                           'BocCode',
                           'BocName',
                           'TransactionType',
                           'TransactionTypeName',
                           'FocCode',
                           'FocName',
                           'TransactionDate',
                           'AvailableBalance',
                           'OpenCommitment',
                           'Obligation',
                           'ULO',
                           'Disbursements',
                           'UnpaidBalances',
                           'Collections',
                           'CumulativeReceipts' ]

    def __str__( self ) -> str:
        if  self.__sitecode is not None:
            return self.__sitecode

    def get_data( self  ) -> list[ Row ]:
        try:
            _source = self.__source
            _provider = self.__provider
            _names = [ 'BFY', 'FundCode', 'AccountCode', 'BocCode' ]
            _values = (self.__bfy, self.__fundcode, self.__programcode, self.__interestdate)
            _dbconfig = DbConfig( _source, _provider )
            _sqlconfig = SqlConfig( names = _names, values = _values )
            _connection = Connection( self.__source )
            _sql = SqlStatement( _dbconfig, _sqlconfig )
            _sqlite = _connection.connect( )
            _cursor = _sqlite.cursor( )
            _query = _sql.get_query( )
            _db = _cursor.execute( _query )
            self.__data =  [ i for i in _db.fetchall( ) ]
            _cursor.close( )
            _sqlite.close( )
            return self.__data
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Ninja'
            _exc.cause = 'StatusOfSpecialAccountFunds'
            _exc.method = 'get_data( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def get_frame( self ) -> DataFrame:
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            _source = self.__source
            _data = BudgetData( _source )
            return _data.create_frame( )
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Ninja'
            _exc.cause = 'StatusOfSpecialAccountFunds'
            _exc.method = 'create_frame( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class SubAppropriation( ):
    '''
    Constructor:  SubAppropriation( bfy: str, efy: str,
    code: str, pvdr: Provider = Provider.SQLite )

    Purpose: Class defines object representing the Sub-Appropriations'''
    __source = None
    __provider = None
    __subappropriationsid = None
    __bfy = None
    __efy = None
    __code = None
    __name = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ) -> int:
        if self.__subappropriationsid is not None:
            return self.__appropriationsid

    @id.setter
    def id( self, value: int ):
        if value is not None:
            self.__appropriationsid  = value

    @property
    def code( self ) -> str:
        if  self.__code is not None:
            return self.__code

    @code.setter
    def code( self, value: str ):
        if value is not None:
            self.__code = value

    @property
    def name( self ) -> str:
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, name ):
        if  name is not None:
            self.__name = name

    @property
    def bfy( self ) -> str:
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value: str ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ) -> str:
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value: str ):
        if value is not None:
            self.__efy = value

    @property
    def data( self ) -> list[ Row ]:
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, value: list[ Row ] ):
        if isinstance( value, list ):
            self.__data = value

    @property
    def fields( self ) -> list[ str ]:
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value: list[ str ] ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy: str, efy: str, code: str, provider: Provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.Appropriations
        self.__bfy = bfy
        self.__efy = efy
        self.__code = code
        self.__fields = [ 'SubAppropriationsId',
                           'Code',
                           'Name' ]

    def __str__( self ) -> str:
        if self.__code is not None:
            return self.__code

    def get_data( self  ) -> list[ Row ]:
        try:
            _source = self.__source
            _provider = self.__provider
            _names = [ 'Code' ]
            _values = ( self.__code, )
            _dbconfig = DbConfig( _source, _provider )
            _sqlconfig = SqlConfig( names = _names, values = _values )
            _connection = Connection( self.__source )
            _sql = SqlStatement( _dbconfig, _sqlconfig )
            _sqlite = _connection.connect( )
            _cursor = _sqlite.cursor( )
            _query = _sql.get_query( )
            _db = _cursor.execute( _query )
            self.__data =  [ i for i in _db.fetchall( ) ]
            _cursor.close( )
            _sqlite.close( )
            return self.__data
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Execution'
            _exc.cause = 'SubAppropriation'
            _exc.method = 'get_data( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def get_frame( self ) -> DataFrame:
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            _source = self.__source
            _data = BudgetData( _source )
            return _data.create_frame( )
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Execution'
            _exc.cause = 'Appropriation'
            _exc.method = 'create_frame( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class StateOrganization( ):
    '''
    Constructor:  StateOrganization( code: str, pvdr: Provider = Provider.SQLite )

    Purpose:  Class defines object representing state organization codes'''
    __source = None
    __provider = None
    __stateorganizationsid = None
    __code = None
    __name = None
    __orgcode = None
    __rpiocode = None
    __rpioname = None
    __fields = None
    __data = None

    @property
    def id( self ) -> int:
        if self.__stateorganizationsid is not None:
            return self.__stateorganizationsid

    @id.setter
    def id( self, value: int ):
        if value is not None:
            self.__stateorganizationsid = value

    @property
    def code( self ) -> str:
        if  self.__code is not None:
            return self.__code

    @code.setter
    def code( self, value: str ):
        if value is not None:
            self.__code = value

    @property
    def name( self ) -> str:
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, value: str ):
        if value is not None:
            self.__name = value

    @property
    def data( self ) -> list:
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, value: list ):
        if value is not None:
            self.__data = value

    @property
    def fields( self ) -> list[ str ]:
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value: list[ str ] ):
        if value is not None:
            self.__fields = value

    def __init__( self, code: str, provider: Provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.StateOrganizations
        self.__code = code
        self.__fields = [ 'StateOrganizationsId',
                          'Name',
                          'Code',
                          'RpioName',
                          'RpioCode' ]

    def __str__( self ) -> str:
        if self.__code is not None:
            return self.__code

    def get_data( self  ) -> list[ Row ]:
        try:
            _source = self.__source
            _provider = self.__provider
            _names = [ 'Code', ]
            _values = (self.__code,)
            _dbconfig = DbConfig( _source, _provider )
            _sqlconfig = SqlConfig( names = _names, values = _values )
            _connection = Connection( self.__source )
            _sql = SqlStatement( _dbconfig, _sqlconfig )
            _sqlite = _connection.connect( )
            _cursor = _sqlite.cursor( )
            _query = _sql.get_query( )
            _db = _cursor.execute( _query )
            self.__data =  [ i for i in _db.fetchall( ) ]
            _cursor.close( )
            _sqlite.close( )
            return self.__data
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Execution'
            _exc.cause = 'StateOrganization'
            _exc.method = 'get_data( self ) '
            _err = ErrorDialog( _exc )
            _err.show( )

    def get_frame( self ) -> DataFrame:
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            _source = self.__source
            _data = BudgetData( _source )
            return _data.create_frame( )
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Execution'
            _exc.cause = 'StateOrganization'
            _exc.method = 'create_frame( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class StatusOfAppropriations( ):
    '''
    Constructor:  StatusOfAppropriations( bfy: str, efy: str,
                  fund: str, pvdr: Provider = Provider.SQLite )

    Purpose: Class defines object representing Appropriation-level execution data'''
    __source = None
    __provider = None
    __statusofappropriationsid = None
    __bfy = None
    __efy = None
    __budgetlevel = None
    __appropriationfundcode = None
    __appropriationfundname = None
    __appropriationcreationdate = None
    __appropriationcode = None
    __subappropriationcode = None
    __appropriationdescription = None
    __fundgroup = None
    __fundgroupname = None
    __documenttype = None
    __transtype = None
    __actualrecoverytranstype = None
    __commitmentspendingcontrolflag = None
    __expensespendingcontrolflag = None
    __agreementlimit = None
    __estimatedrecoveriestranstype = None
    __estimatedreimbursementstranstype = None
    __obligationspendingcontrolflag = None
    __precommitmentspendingcontrolflag = None
    __postedcontrolflag = None
    __postedflag = None
    __recordcarryoveratlowerlevel = None
    __reimbursablespendingoption = None
    __recoveriesoption = None
    __recoveriesspendingoption = None
    __originalbudgetedamount = None
    __apportionmentsposted = None
    __totalauthority = None
    __totalbudgeted = None
    __totalpostedamount = None
    __fundswithdrawnprioryearamounts = None
    __fundinginamount = None
    __fundingoutamount = None
    __totalaccrualrecoveries = None
    __totalactualreimbursements = None
    __totalagreeementreimbursables = None
    __totalcarriedforwardin = None
    __totalcarriedforwardout = None
    __totalcommited = None
    __totalestimatedrecoveries = None
    __totalestimatedreimbursements = None
    __totalexpenses = None
    __totalexpenditureexpenses = None
    __totalexpenseaccruals = None
    __totalprecommitments = None
    __unliquidatedprecommitments = None
    __totalobligations = None
    __unliquidatedobligations = None
    __voidedamount = None
    __totalusedamount = None
    __availableamount = None
    __treasuryaccountcode = None
    __treasuryaccountname = None
    __budgetaccountcode = None
    __budgetaccountname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ) -> int:
        if self.__statusofappropriationsid is not None:
            return self.__statusofappropriationsid

    @id.setter
    def id( self, value: int ):
        if value is not None:
            self.__statusofappropriationsid = value

    @property
    def bfy( self ) -> str:
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value: str ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ) -> str:
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value: str ):
        if value is not None:
            self.__efy = value

    @property
    def budget_level( self ) -> str:
        if self.__budgetlevel is not None:
            return self.__budgetlevel

    @budget_level.setter
    def budget_level( self, value: str ):
        if value is not None:
            self.__budgetlevel = value

    @property
    def appropriation_fund_code( self ) -> str:
        if self.__appropriationfundcode is not None:
            return self.__appropriationfundcode

    @appropriation_fund_code.setter
    def appropriation_fund_code( self, value: str ):
        if value is not None:
            self.__appropriationfundcode = value

    @property
    def appropriation_fund_name( self ) -> str:
        if self.__appropriationfundname is not None:
            return self.__appropriationfundname

    @appropriation_fund_name.setter
    def appropriation_fund_name( self, value: str ):
        if value is not None:
            self.__appropriationfundname = value

    @property
    def appropriation_creation_date( self ) -> str:
        if self.__appropriationcreationdate is not None:
            return self.__appropriationcreationdate

    @appropriation_creation_date.setter
    def appropriation_creation_date( self, value: str ):
        if  value is not None:
            self.__appropriationcreationdate = value

    @property
    def appropriation_code( self ) -> str:
        if self.__appropriationcode is not None:
            return self.__appropriationcode

    @appropriation_code.setter
    def appropriation_code( self, value: str ):
        if value is not None:
            self.__appropriationcode = value

    @property
    def sub_appropriation_code( self ) -> str:
        if self.__subappropriationcode is not None:
            return self.__subappropriationcode

    @sub_appropriation_code.setter
    def sub_appropriation_code( self, value: str ):
        if value is not None:
            self.__subappropriationcode = value

    @property
    def appropriation_description( self ) -> str:
        if self.__appropriationdescription is not None:
            return self.__appropriationdescription

    @appropriation_description.setter
    def appropriation_description( self, value: str ):
        if value is not None:
            self.__appropriationdescription = value

    @property
    def fund_group( self ) -> str:
        if self.__fundgroup is not None:
            return self.__fundgroup

    @fund_group.setter
    def fund_group( self, value: str ):
        if value is not None:
            self.__fundgroup = value

    @property
    def fund_group_name( self ) -> str:
        if self.__fundgroupname is not None:
            return self.__fundgroupname

    @fund_group_name.setter
    def fund_group_name( self, value: str ):
        if value is not None:
            self.__fundgroupname = value

    @property
    def document_type( self ) -> str:
        if self.__documenttype is not None:
            return self.__documenttype

    @document_type.setter
    def document_type( self, value: str ):
        if value is not None:
            self.__documenttype = value

    @property
    def transtype( self ) -> str:
        if self.__transtype is not None:
            return self.__transtype

    @transtype.setter
    def transtype( self, value: str ):
        if value is not None:
            self.__transtype = value

    @property
    def recovery_transtype( self ) -> str:
        if self.__actualrecoverytranstype is not None:
            return self.__actualrecoverytranstype

    @recovery_transtype.setter
    def recovery_transtype( self, value: str ):
        if value is not None:
            self.__actualrecoverytranstype = value

    @property
    def commitment_control_flag( self ) -> str:
        if self.__commitmentspendingcontrolflag is not None:
            return self.__commitmentspendingcontrolflag

    @commitment_control_flag.setter
    def commitment_control_flag( self, value: str ):
        if value is not None:
            self.__commitmentspendingcontrolflag = value

    @property
    def agreement_limit( self ) -> str:
        if self.__agreementlimit is not None:
            return self.__agreementlimit

    @agreement_limit.setter
    def agreement_limit( self, value: str ):
        if value is not None:
            self.__agreementlimit = value

    @property
    def estimated_recoveries_transtype( self ) -> str:
        if self.__estimatedrecoveriestranstype is not None:
            return self.__estimatedrecoveriestranstype

    @estimated_recoveries_transtype.setter
    def estimated_recoveries_transtype( self, value: str ):
        if value is not None:
            self.__estimatedrecoveriestranstype = value

    @property
    def estimated_reimbursements_transtype( self ) -> str:
        if self.__estimatedreimbursementstranstype is not None:
            return self.__estimatedreimbursementstranstype

    @estimated_reimbursements_transtype.setter
    def estimated_reimbursements_transtype( self, value: str ):
        if value is not None:
            self.__estimatedreimbursementstranstype = value

    @property
    def expense_control_flag( self ) -> str:
        if self.__expensespendingcontrolflag is not None:
            return self.__expensespendingcontrolflag

    @expense_control_flag.setter
    def expense_control_flag( self, value: str ):
        if value is not None:
            self.__expensespendingcontrolflag = value

    @property
    def obligation_control_flag( self ) -> str:
        if self.__obligationspendingcontrolflag is not None:
            return self.__obligationspendingcontrolflag

    @obligation_control_flag.setter
    def obligation_control_flag( self, value: str ):
        if value is not None:
            self.__obligationspendingcontrolflag = value

    @property
    def precommitment_control_flag( self ) -> str:
        if self.__precommitmentspendingcontrolflag is not None:
            return self.__precommitmentspendingcontrolflag

    @precommitment_control_flag.setter
    def precommitment_control_flag( self, value: str ):
        if value is not None:
            self.__precommitmentspendingcontrolflag = value

    @property
    def posted_control_flag( self ) -> str:
        if self.__postedcontrolflag is not None:
            return self.__postedcontrolflag

    @posted_control_flag.setter
    def posted_control_flag( self, value: str ):
        if value is not None:
            self.__expensespendingcontrolflag = value

    @property
    def posted_flag( self ) -> str:
        if self.__postedflag is not None:
            return self.__postedflag

    @posted_flag.setter
    def posted_flag( self, value: str ):
        if value is not None:
            self.__postedflag = value

    @property
    def record_lower_level( self ) -> str:
        if self.__recordcarryoveratlowerlevel is not None:
            return self.__recordcarryoveratlowerlevel

    @record_lower_level.setter
    def record_lower_level( self, value: str ):
        if value is not None:
            self.__recordcarryoveratlowerlevel = value

    @property
    def reimbursable_spending_option( self ) -> str:
        if self.__reimbursablespendingoption is not None:
            return self.__reimbursablespendingoption

    @reimbursable_spending_option.setter
    def reimbursable_spending_option( self, value: str ):
        if value is not None:
            self.__reimbursablespendingoption = value

    @property
    def recoveries_option( self ) -> str:
        if self.__recoveriesoption is not None:
            return self.__recoveriesoption

    @recoveries_option.setter
    def recoveries_option( self, value: str ):
        if value is not None:
            self.__recoveriesoption = value

    @property
    def recoveries_spending_option( self ) -> str:
        if self.__recoveriesspendingoption is not None:
            return self.__recoveriesspendingoption

    @recoveries_spending_option.setter
    def recoveries_spending_option( self, value: str ):
        if value is not None:
            self.__recoveriesspendingoption = value

    @property
    def original_budgeted_amount( self ) -> float:
        if self.__originalbudgetedamount is not None:
            return self.__originalbudgetedamount

    @original_budgeted_amount.setter
    def original_budgeted_amount( self, value: float ):
        if value is not None:
            self.__originalbudgetedamount = value

    @property
    def apportionments_posted( self ) -> float:
        if self.__apportionmentsposted is not None:
            return self.__apportionmentsposted

    @apportionments_posted.setter
    def apportionments_posted( self, value: float ):
        if value is not None:
            self.__apportionmentsposted = value

    @property
    def total_authority( self ) -> float:
        if self.__totalauthority is not None:
            return self.__totalauthority

    @total_authority.setter
    def total_authority( self, value: float ):
        if value is not None:
            self.__totalauthority = value

    @property
    def total_budgeted( self ) -> float:
        if self.__totalbudgeted is not None:
            return self.__totalbudgeted

    @total_budgeted.setter
    def total_budgeted( self, value: float ):
        if value is not None:
            self.__totalbudgeted = value

    @property
    def total_posted_amount( self ) -> float:
        if self.__totalpostedamount is not None:
            return self.__totalpostedamount

    @total_posted_amount.setter
    def total_posted_amount( self, value: float ):
        if value is not None:
            self.__totalpostedamount = value

    @property
    def funds_withdrawn_amounts( self ) -> float:
        if self.__fundswithdrawnprioryearamounts is not None:
            return self.__fundswithdrawnprioryearamounts

    @funds_withdrawn_amounts.setter
    def funds_withdrawn_amounts( self, value: float ):
        if value is not None:
            self.__fundswithdrawnprioryearamounts = value

    @property
    def funding_in_amount( self ) -> float:
        if self.__fundinginamount is not None:
            return self.__fundinginamount

    @funding_in_amount.setter
    def funding_in_amount( self, value: float ):
        if value is not None:
            self.__fundinginamount = value

    @property
    def funding_out_amount( self ) -> float:
        if self.__fundingoutamount is not None:
            return self.__fundingoutamount

    @funding_out_amount.setter
    def funding_out_amount( self, value: float ):
        if value is not None:
            self.__fundingoutamount = value

    @property
    def total_accrual_recoveries( self ) -> float:
        if self.__totalaccrualrecoveries is not None:
            return self.__totalaccrualrecoveries

    @total_accrual_recoveries.setter
    def total_accrual_recoveries( self, value: float ):
        if value is not None:
            self.__totalaccrualrecoveries = value

    @property
    def total_actual_reimbursements( self ) -> float:
        if self.__totalactualreimbursements is not None:
            return self.__totalactualreimbursements

    @total_actual_reimbursements.setter
    def total_actual_reimbursements( self, value: float ):
        if value is not None:
            self.__totalactualreimbursements = value

    @property
    def total_agreement_reimbursables( self ) -> float:
        if self.__totalagreementreimbursables is not None:
            return self.__totalagreementreimbursables

    @total_agreement_reimbursables.setter
    def total_agreement_reimbursables( self, value: float ):
        if value is not None:
            self.__totalagreementreimbursables = value

    @property
    def total_carried_in( self ) -> float:
        if self.__totalcarriedforwardin is not None:
            return self.__totalcarriedforwardin

    @total_carried_in.setter
    def total_carried_in( self, value: float ):
        if value is not None:
            self.__totalcarriedforwardin = value

    @property
    def total_carried_out( self ) -> float:
        if self.__totalcarriedforwardout is not None:
            return self.__totalcarriedforwardout

    @total_carried_out.setter
    def total_carried_out( self, value: float ):
        if value is not None:
            self.__totalcarriedforwardout = value

    @property
    def total_estimated_recoveries( self ) -> float:
        if self.__totalestimatedrecoveries is not None:
            return self.__totalestimatedrecoveries

    @total_estimated_recoveries.setter
    def total_estimated_recoveries( self, value: float ):
        if value is not None:
            self.__totalestimatedrecoveries = value

    @property
    def total_estimated_reimbursements( self ) -> float:
        if self.__totalestimatedreimbursements is not None:
            return self.__totalestimatedreimbursements

    @total_estimated_reimbursements.setter
    def total_estimated_reimbursements( self, value: float ):
        if value is not None:
            self.__totalestimatedreimbursements = value

    @property
    def total_expenses( self ) -> float:
        if self.__totalexpenses is not None:
            return self.__totalexpenses

    @total_expenses.setter
    def total_expenses( self, value: float ):
        if value is not None:
            self.__totalexpenses = value

    @property
    def total_expenditure_expenses( self ) -> float:
        if self.__totalexpenditureexpenses is not None:
            return self.__totalexpenditureexpenses

    @total_expenditure_expenses.setter
    def total_expenditure_expenses( self, value: float ):
        if value is not None:
            self.__totalexpenditureexpenses = value

    @property
    def total_expense_accruals( self ) -> float:
        if self.__totalexpenseaccruals is not None:
            return self.__totalexpenseaccruals

    @total_expense_accruals.setter
    def total_expense_accruals( self, value: float ):
        if value is not None:
            self.__totalexpenseaccruals = value

    @property
    def total_precommitments( self ) -> float:
        if self.__totalprecommitments is not None:
            return self.__totalprecommitments

    @total_precommitments.setter
    def total_precommitments( self, value: float ):
        if value is not None:
            self.__totalprecommitments = value

    @property
    def unliquidated_precommitments( self ) -> float:
        if self.__unliquidatedprecommitments is not None:
            return self.__unliquidatedprecommitments

    @unliquidated_precommitments.setter
    def unliquidated_precommitments( self, value: float ):
        if value is not None:
            self.__unliquidatedprecommitments = value

    @property
    def total_obligations( self ) -> float:
        if self.__totalobligations is not None:
            return self.__totalobligations

    @total_obligations.setter
    def total_obligations( self, value: float ):
        if value is not None:
            self.__totalobligations = value

    @property
    def unliquidated_obligations( self ) -> float:
        if self.__unliquidatedobligations is not None:
            return self.__unliquidatedobligations

    @unliquidated_obligations.setter
    def unliquidated_obligations( self, value: float ):
        if value is not None:
            self.__unliquidatedobligations = value

    @property
    def voided_amount( self ) -> float:
        if self.__voidedamount is not None:
            return self.__voidedamount

    @voided_amount.setter
    def voided_amount( self, value: float ):
        if value is not None:
            self.__voidedamount = value

    @property
    def total_used_amount( self ) -> float:
        if self.__totalusedamount is not None:
            return self.__totalusedamount

    @total_used_amount.setter
    def total_used_amount( self, value: float ):
        if value is not None:
            self.__totalusedamount = value

    @property
    def available_amount( self ) -> float:
        if self.__availableamount is not None:
            return self.__availableamount

    @available_amount.setter
    def available_amount( self, value: float ):
        if value is not None:
            self.__availableamount = value

    @property
    def treasury_account_code( self ) -> str:
        if self.__treasuryaccountcode is not None:
            return self.__treasuryaccountcode

    @treasury_account_code.setter
    def treasury_account_code( self, value: str ):
        if value is not None:
            self.__treasuryaccountcode = value

    @property
    def treasury_account_name( self ) -> str:
        if self.__treasuryaccountname is not None:
            return self.__treasuryaccountname

    @treasury_account_name.setter
    def treasury_account_name( self, value: str ):
        if value is not None:
            self.__treasuryaccountname = value

    @property
    def budget_account_code( self ) -> str:
        if self.__budgetaccountcode is not None:
            return self.__budgetaccountcode

    @budget_account_code.setter
    def budget_account_code( self, value: str ):
        if value is not None:
            self.__budgetaccountcode = value

    @property
    def budget_account_name( self ) -> str:
        if self.__budgetaccountname is not None:
            return self.__budgetaccountname

    @budget_account_name.setter
    def budget_account_name( self, value: str ):
        if value is not None:
            self.__budgetaccountname = value

    @property
    def fields( self ) -> list[ str ]:
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value: list[ str ] ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy: str, efy: str,
                  fund: str, provider: Provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.StatusOfAppropriations
        self.__bfy = bfy
        self.__efy = efy
        self.__appropriationfundcode = fund
        self.__fields =[ 'StatusOfAppropriationsId',
                           'BFY',
                           'EFY',
                           'BudgetLevel',
                           'AppropriationFundCode',
                           'AppropriationFundName',
                           'Availability',
                           'TreasurySymbol',
                           'AppropriationCreationDate',
                           'AppropriationCode',
                           'SubAppropriationCode',
                           'AppropriationDescription',
                           'FundGroup',
                           'FundGroupName',
                           'DocumentType',
                           'TransType',
                           'ActualRecoveryTransType',
                           'CommitmentSpendingControlFlag',
                           'AgreementLimit',
                           'EstimatedRecoveriesTransType',
                           'EstimatedReimbursmentsTransType',
                           'ExpenseSpendingControlFlag',
                           'ObligationSpendingControlFlag',
                           'PreCommitmentSpendingControlFlag',
                           'PostedControlFlag',
                           'PostedFlag',
                           'RecordCarryoverAtLowerLevel',
                           'ReimbursableSpendingOption',
                           'RecoveriesOption',
                           'RecoveriesSpendingOption',
                           'OriginalBudgetedAmount',
                           'ApportionmentsPosted',
                           'TotalAuthority',
                           'TotalBudgeted',
                           'TotalPostedAmount',
                           'FundsWithdrawnPriorYearsAmount',
                           'FundingInAmount',
                           'FundingOutAmount',
                           'TotalAccrualRecoveries',
                           'TotalActualReimbursements',
                           'TotalAgreementReimbursables',
                           'TotalCarriedForwardIn',
                           'TotalCarriedForwardOut',
                           'TotalCommitted',
                           'TotalEstimatedRecoveries',
                           'TotalEstimatedReimbursements',
                           'TotalExpenses',
                           'TotalExpenditureExpenses',
                           'TotalExpenseAccruals',
                           'TotalPreCommitments',
                           'UnliquidatedPreCommitments',
                           'TotalObligations',
                           'ULO',
                           'VoidedAmount',
                           'TotalUsedAmount',
                           'AvailableAmount' ]

    def get_data( self  ) -> list[ Row ]:
        try:
            _source = self.__source
            _provider = self.__provider
            _names = [ 'BFY', 'EFY', 'AppropriationFundCode', ]
            _values = (self.__bfy, self.__efy, self.__appropriationfundcode)
            _dbconfig = DbConfig( _source, _provider )
            _sqlconfig = SqlConfig( names = _names, values = _values )
            _connection = Connection( self.__source )
            _sql = SqlStatement( _dbconfig, _sqlconfig )
            _sqlite = _connection.connect( )
            _cursor = _sqlite.cursor( )
            _query = _sql.get_query( )
            _db = _cursor.execute( _query )
            self.__data =  [ i for i in _db.fetchall( ) ]
            _cursor.close( )
            _sqlite.close( )
            return self.__data
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Reporting'
            _exc.cause = 'StatusOfAppropriations'
            _exc.method = 'get_data( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def get_frame( self ) -> DataFrame:
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            _source = self.__source
            _data = BudgetData( _source )
            return _data.create_frame( )
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Reporting'
            _exc.cause = 'StatusOfAppropriations'
            _exc.method = 'create_frame( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class SpendingRate( ):
    '''
    Constructor:  SpendingRate( accountcode: str, pvdr: Provider = Provider.SQLite )

    Purpose: class object providing OMB spending rate data'''
    __source = None
    __provider = None
    __spendingratesid = None
    __ombagencycode = None
    __ombagencyname = None
    __treasuryagencycode = None
    __treasuryagencyname = None
    __treasuryaccountcode = None
    __treasuryaccountname = None
    __budgetaccountcode = None
    __budgetaccountname = None
    __ombaccounttitle = None
    __subfunction = None
    __linenumber = None
    __linename = None
    __category = None
    __subcategory = None
    __subcategoryname = None
    __jurisdiction = None
    __yearofauthority = None
    __budgetauthority = None
    __outyear1 = None
    __outyear2 = None
    __outyear3 = None
    __outyear4 = None
    __outyear5 = None
    __outyear6 = None
    __outyear7 = None
    __outyear8 = None
    __outyear9 = None
    __outyear10 = None
    __outyear11 = None
    __totalspendout = None
    __data = None
    __frame = None

    @property
    def id( self ) -> int:
        if self.__spendingratesid is not None:
            return self.__spendingratesid

    @id.setter
    def id( self, value: int ):
        if value is not None:
            self.__spendingratesid = value

    @property
    def treasury_agency_code( self ) -> str:
        if self.__treasuryagencycode is not None:
            return self.__treasuryagencycode

    @treasury_agency_code.setter
    def treasury_agency_code( self, value: str ):
        if value is not None:
            self.__treasuryagencycode = value

    @property
    def treasury_agency_name( self ) -> str:
        if self.__treasuryagencyname is not None:
            return self.__treasuryagencyname

    @treasury_agency_name.setter
    def treasury_agency_name( self, value: str ):
        if value is not None:
            self.__treasuryagencyname = value

    @property
    def treasury_account_code( self ) -> str:
        if self.__treasuryaccountcode is not None:
            return self.__treasuryaccountcode

    @treasury_account_code.setter
    def treasury_account_code( self, value: str ):
        if value is not None:
            self.__treasuryaccountcode = value

    @property
    def treasury_account_name( self ) -> str:
        if self.__treasuryaccountname is not None:
            return self.__treasuryaccountname

    @treasury_account_name.setter
    def treasury_account_name( self, value: str ):
        if value is not None:
            self.__treasuryaccountname = value

    @property
    def omb_agency_code( self ) -> str:
        if self.__ombagencycode is not None:
            return self.__ombagencycode

    @omb_agency_code.setter
    def omb_agency_code( self, value: str ):
        if value is not None:
            self.__ombagencycode = value

    @property
    def omb_agency_name( self ) -> str:
        if self.__ombagencyname is not None:
            return self.__ombagencyname

    @omb_agency_name.setter
    def omb_agency_name( self, value: str ):
        if value is not None:
            self.__ombagencyname = value

    @property
    def budget_account_code( self ) -> str:
        if self.__budgetaccountcode is not None:
            return self.__budgetaccountcode

    @budget_account_code.setter
    def budget_account_code( self, value: str ):
        if value is not None:
            self.__budgetaccountcode = value

    @property
    def budget_account_name( self ) -> str:
        if self.__budgetaccountname is not None:
            return self.__budgetaccountname

    @budget_account_name.setter
    def budget_account_name( self, value: str ):
        if value is not None:
            self.__budgetaccountname = value

    @property
    def subfunction( self ) -> str:
        if self.__subfunction is not None:
            return self.__subfunction

    @subfunction.setter
    def subfunction( self, value: str ):
        if value is not None:
            self.__subfunction = value

    @property
    def category( self ) -> str:
        if self.__category is not None:
            return self.__category

    @category.setter
    def category( self, value: str ):
        if value is not None:
            self.__category = value

    @property
    def subcategory( self ) -> str:
        if self.__subcategory is not None:
            return self.__subcategory

    @subcategory.setter
    def subcategory( self, value: str ):
        if value is not None:
            self.__subcategory = value

    @property
    def line_number( self ) -> str:
        if self.__linenumber is not None:
            return self.__linenumber

    @line_number.setter
    def line_number( self, value: str ):
        if value is not None:
            self.__linenumber = value

    @property
    def line_name( self ) -> str:
        if self.__linename is not None:
            return self.__linename

    @line_name.setter
    def line_name( self, value: str ):
        if value is not None:
            self.__linename = value

    @property
    def year_of_authority( self ) -> str:
        if self.__yearofauthority is not None:
            return self.__yearofauthority

    @year_of_authority.setter
    def year_of_authority( self, value: str ):
        if value is not None:
            self.__yearofauthority = value

    @property
    def budget_authority( self ) -> str:
        if self.__budgetauthority is not None:
            return self.__budgetauthority

    @budget_authority.setter
    def budget_authority( self, value: str ):
        if value is not None:
            self.__budgetauthority = value

    @property
    def out_year_1( self ) -> str:
        if self.__outyear1 is not None:
            return self.__outyear1

    @out_year_1.setter
    def out_year_1( self, value: str ):
        if value is not None:
            self.__outyear1 = value

    @property
    def out_year_2( self ) -> str:
        if self.__outyear2 is not None:
            return self.__outyear2

    @out_year_2.setter
    def out_year_2( self, value: str ):
        if value is not None:
            self.__outyear2 = value

    @property
    def out_year_3( self ) -> str:
        if self.__outyear3 is not None:
            return self.__outyear3

    @out_year_3.setter
    def out_year_3( self, value: str ):
        if value is not None:
            self.__outyear3 = value

    @property
    def out_year_4( self ) -> str:
        if self.__outyear4 is not None:
            return self.__outyear4

    @out_year_4.setter
    def out_year_4( self, value: str ):
        if value is not None:
            self.__outyear4 = value

    @property
    def out_year_5( self ) -> str:
        if self.__outyear5 is not None:
            return self.__outyear5

    @out_year_5.setter
    def out_year_5( self, value: str ):
        if value is not None:
            self.__outyear5 = value

    @property
    def out_year_6( self ) -> str:
        if self.__outyear6 is not None:
            return self.__outyear6

    @out_year_6.setter
    def out_year_6( self, value: str ):
        if value is not None:
            self.__outyear6 = value

    @property
    def out_year_7( self ) -> str:
        if self.__outyear7 is not None:
            return self.__outyear7

    @out_year_7.setter
    def out_year_7( self, value: str ):
        if value is not None:
            self.__outyear7 = value

    @property
    def out_year_8( self ) -> str:
        if self.__outyear8 is not None:
            return self.__outyear8

    @out_year_8.setter
    def out_year_8( self, value: str ):
        if value is not None:
            self.__outyear8 = value

    @property
    def out_year_9( self ) -> str:
        if self.__outyear9 is not None:
            return self.__outyear9

    @out_year_9.setter
    def out_year_9( self, value: str ):
        if value is not None:
            self.__outyear9 = value

    @property
    def out_year_10( self ) -> str:
        if self.__outyear10 is not None:
            return self.__outyear10

    @out_year_10.setter
    def out_year_10( self, value: str ):
        if value is not None:
            self.__outyear10 = value

    @property
    def out_year_11( self ) -> str:
        if self.__outyear11 is not None:
            return self.__outyear11

    @out_year_11.setter
    def out_year_11( self, value: str ):
        if value is not None:
            self.__outyear11 = value

    @property
    def total_spendout( self ) -> str:
        if self.__totalspendout is not None:
            return self.__totalspendout

    @total_spendout.setter
    def total_spendout( self, value: str ):
        if value is not None:
            self.__totalspendout = value

    @property
    def fields( self ) -> list[ str ]:
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value: list[ str ] ):
        if value is not None:
            self.__fields = value

    def __init__( self, accountcode: str, provider: Provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.SpendingRates
        self.__budgetaccountcode = accountcode
        self.__fields = [ 'SpendingRatesId',
                          'OmbAgencyCode',
                          'OmbAgencyName',
                          'OmbBureauCode',
                          'OmbBureauName',
                          'TreausuryAgencyCode',
                          'TreausuryAccountCode',
                          'TreausuryAccountName',
                          'AccountTitle',
                          'Subfunction',
                          'Line',
                          'LineNumber',
                          'Category',
                          'Subcategory',
                          'SubcategoryName',
                          'AccountCode',
                          'Jurisdiction',
                          'YearOfAuthority',
                          'BudgetAuthority',
                          'OutYear1',
                          'OutYear2',
                          'OutYear3',
                          'OutYear4',
                          'OutYear5',
                          'OutYear6',
                          'OutYear7',
                          'OutYear8',
                          'OutYear9',
                          'OutYear10',
                          'OutYear11',
                          'TotalSpendout' ]

    def get_data( self  ) -> list[ Row ]:
        try:
            _source = self.__source
            _provider = self.__provider
            _command = SQL.SELECTALL
            _names = [ 'OmbAccountCode', ]
            _values = (self.__budgetaccountcode,)
            _db = DataBuilder( _source, _provider, _command, _names, _values )
            self.__data = [ i for i in _db.create_table( ) ]
            return [ i  for i in self.__data ]

        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Reporting'
            _exc.cause = 'SpendingRate'
            _exc.method = 'get_data( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def get_frame( self ) -> DataFrame:
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            _source = self.__source
            _data = BudgetData( _source )
            return _data.create_frame( )
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Reporting'
            _exc.cause = 'SpendingRate'
            _exc.method = 'create_frame( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class StatusOfSupplementalFunds( ):
    '''
    Constructor:  StatusOfSupplementalFunds( bfy, efy, fund, pvdr = Provider.SQLite )

    Purpose:  Class defines object used for reporting on Supplemental funding
    '''
    __statusofsupplementalfundsid = None
    __statusoffundsid = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __rpioname = None
    __fundcode = None
    __fundname = None
    __ahcode = None
    __ahname = None
    __orgcode = None
    __orgname = None
    __accountcode = None
    __boccode = None
    __bocname = None
    __rccode = None
    __rcname = None
    __amount = None
    __budgeted = None
    __posted = None
    __opencommitments = None
    __obligations = None
    __unliquidatedobligations = None
    __expenditures = None
    __used = None
    __avaialable = None
    __programprojectcode = None
    __programprojectname = None
    __programareacode = None
    __programareaname = None
    __goalcode = None
    __goalname = None
    __objectivecode = None
    __objectivename = None
    __npmcode = None
    __npmname = None
    __treasuryaccountcode = None
    __treasuryaccountname = None
    __budgetaccountcode = None
    __budgetaccountname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ) -> int:
        if self.__statusofsupplementalfundsid is not None:
            return self.__statusofsupplementalfundsid

    @id.setter
    def id( self, value: int ):
        if value is not None:
            self.__statusofsupplementalfundsid = value

    @property
    def bfy( self ) -> str:
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value: str ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ) -> str:
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value: str ):
        if value is not None:
            self.__efy = value

    @property
    def rpio_code( self ) -> str:
        if self.__rpiocode is not None:
            return self.__rpiocode

    @rpio_code.setter
    def rpio_code( self, value: str ):
        if value is not None:
            self.__rpiocode = value

    @property
    def rpio_name( self ) -> str:
        if self.__rpioname is not None:
            return self.__rpioname

    @rpio_name.setter
    def rpio_name( self, value: str ):
        if value is not None:
            self.__rpioname = value

    @property
    def ah_code( self ) -> str:
        if self.__ahcode is not None:
            return self.__ahcode

    @ah_code.setter
    def ah_code( self, value: str ):
        if value is not None:
            self.__ahcode = value

    @property
    def ah_name( self ) -> str:
        if self.__ahname is not None:
            return self.__ahname

    @ah_name.setter
    def ah_name( self, value: str ):
        if value is not None:
            self.__ahname = value

    @property
    def fund_code( self ) -> str:
        if self.__fundcode is not None:
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value: str ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund_name( self ) -> str:
        if self.__fundname is not None:
            return self.__fundname

    @fund_name.setter
    def fund_name( self, value: str ):
        if value is not None:
            self.__fundname = value

    @property
    def org_code( self ) -> str:
        if self.__orgcode is not None:
            return self.__orgcode

    @org_code.setter
    def org_code( self, value: str ):
        if value is not None:
            self.__orgcode = value

    @property
    def org_name( self  ):
        if self.__orgname is not None:
            return self.__orgname

    @org_name.setter
    def org_name( self, value  ):
        if value is not None:
            self.__orgname = value

    @property
    def account_code( self ) -> str:
        if self.__accountcode is not None:
            return self.__accountcode

    @account_code.setter
    def account_code( self, value: str ):
        if value is not None:
            self.__accountcode = value

    @property
    def boc_code( self ) -> str:
        if self.__boccode is not None:
            return self.__boccode

    @boc_code.setter
    def boc_code( self, value: str ):
        if value is not None:
            self.__boccode = value

    @property
    def boc_name( self ) -> str:
        if self.__bocname is not None:
            return self.__bocname

    @boc_name.setter
    def boc_name( self, value: str ):
        if value is not None:
            self.__bocname = value

    @property
    def rc_code( self ) -> str:
        if self.__rccode is not None:
            return self.__rccode

    @rc_code.setter
    def rc_code( self, value: str ):
        if value is not None:
            self.__rccode = value

    @property
    def rc_name( self ) -> str:
        if self.__rcname is not None:
            return self.__rcname

    @rc_name.setter
    def rc_name( self, value: str ):
        if value is not None:
            self.__rcname = value

    @property
    def amount( self ) -> float:
        if self.__amount is not None:
            return self.__amount

    @amount.setter
    def amount( self, value: float ):
        if value is not None:
            self.__amount = value

    @property
    def budgeted( self ) -> str:
        if self.__budgeted is not None:
            return self.__budgeted

    @budgeted.setter
    def budgeted( self, value: str ):
        if value is not None:
            self.__budgeted = value

    @property
    def posted( self ) -> float:
        if self.__posted is not None:
            return self.__posted

    @posted.setter
    def posted( self, value: float ):
        if value is not None:
            self.__posted = value

    @property
    def open_commitments( self ) -> float:
        if self.__opencommitments is not None:
            return self.__opencommitments

    @open_commitments.setter
    def open_commitments( self, value: float ):
        if value is not None:
            self.__opencommitments = value

    @property
    def obligations( self ) -> float:
        if self.__obligations is not None:
            return self.__obligations

    @obligations.setter
    def obligations( self, value: float ):
        if value is not None:
            self.__obligations = value

    @property
    def unliquidated_obligations( self ) -> float:
        if self.__unliquidatedobligations is not None:
            return self.__unliquidatedobligations

    @unliquidated_obligations.setter
    def unliquidated_obligations( self, value: float ):
        if value is not None:
            self.__unliquidatedobligations = value

    @property
    def expenditures( self ) -> float:
        if self.__expenditures is not None:
            return self.__expenditures

    @expenditures.setter
    def expenditures( self, value: float ):
        if value is not None:
            self.__expenditures = value

    @property
    def used( self ) -> float:
        if self.__used is not None:
            return self.__used

    @used.setter
    def used( self, value: float ):
        if value is not None:
            self.__used = value

    @property
    def available( self ) -> float:
        if self.__avaialable is not None:
            return self.__avaialable

    @available.setter
    def available( self, value: float ):
        if value is not None:
            self.__avaialable = value

    @property
    def program_project_code( self ) -> str:
        if self.__programprojectcode is not None:
            return self.__programprojectcode

    @program_project_code.setter
    def program_project_code( self, value: str ):
        if value is not None:
            self.__programprojectcode = value

    @property
    def program_project_name( self ) -> str:
        if self.__programprojectname is not None:
            return self.__programprojectname

    @program_project_name.setter
    def program_project_name( self, value: str ):
        if value is not None:
            self.__programprojectname = value

    @property
    def program_area_code( self ) -> str:
        if self.__programareacode is not None:
            return self.__programareacode

    @program_area_code.setter
    def program_area_code( self, value: str ):
        if value is not None:
            self.__programareacode = value

    @property
    def program_area_name( self ) -> str:
        if self.__programareaname is not None:
            return self.__programareaname

    @program_area_name.setter
    def program_area_name( self, value: str ):
        if value is not None:
            self.__programareaname = value

    @property
    def goal_code( self ) -> str:
        if self.__goalcode is not None:
            return self.__goalcode

    @goal_code.setter
    def goal_code( self, value: str ):
        if value is not None:
            self.__goalcode = value

    @property
    def goal_name( self ) -> str:
        if self.__goalname is not None:
            return self.__goalname

    @goal_name.setter
    def goal_name( self, value: str ):
        if value is not None:
            self.__goalname = value

    @property
    def objective_code( self ) -> str:
        if self.__objectivecode is not None:
            return self.__objectivecode

    @objective_code.setter
    def objective_code( self, value: str ):
        if value is not None:
            self.__objectivecode = value

    @property
    def objective_name( self ) -> str:
        if self.__objectivename is not None:
            return self.__objectivename

    @objective_name.setter
    def objective_name( self, value: str ):
        if value is not None:
            self.__objectivename = value

    @property
    def npm_code( self ) -> str:
        if self.__npmcode is not None:
            return self.__npmcode

    @npm_code.setter
    def npm_code( self, value: str ):
        if value is not None:
            self.__npmcode = value

    @property
    def npm_name( self ) -> str:
        if self.__npmname is not None:
            return self.__npmname

    @npm_name.setter
    def npm_name( self, value: str ):
        if value is not None:
            self.__npmname = value

    @property
    def treasury_account_code( self ) -> str:
        if self.__treasuryaccountcode is not None:
            return self.__treasuryaccountcode

    @treasury_account_code.setter
    def treasury_account_code( self, value: str ):
        if value is not None:
            self.__treasuryaccountcode = value

    @property
    def treasury_account_name( self ) -> str:
        if self.__treasuryaccountname is not None:
            return self.__treasuryaccountname

    @treasury_account_name.setter
    def treasury_account_name( self, value: str ):
        if value is not None:
            self.__treasuryaccountname = value

    @property
    def budget_account_code( self ) -> str:
        if self.__budgetaccountcode is not None:
            return self.__budgetaccountcode

    @budget_account_code.setter
    def budget_account_code( self, value: str ):
        if value is not None:
            self.__budgetaccountcode = value

    @property
    def budget_account_name( self ) -> str:
        if self.__budgetaccountname is not None:
            return self.__budgetaccountname

    @budget_account_name.setter
    def budget_account_name( self, value: str ):
        if value is not None:
            self.__budgetaccountname = value

    @property
    def fields( self ) -> list[ str ]:
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value: list[ str ] ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy: str, efy: str, fund: str, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.StatusOfSupplementalFunding
        self.__bfy = bfy
        self.__efy = efy
        self.__fundcode = fund
        self.__fields =[ 'StatusOfSupplementalFundsId',
                           'StatusOfFundsId',
                           'BudgetLevel',
                           'BFY',
                           'EFY',
                           'RpioCode',
                           'RpioName',
                           'AhCode',
                           'AhName',
                           'FundCode',
                           'FundName',
                           'OrgCode',
                           'OrgName',
                           'AccountCode',
                           'BocCode',
                           'BocName',
                           'ProgramProjectCode',
                           'ProgramProjectName',
                           'ProgramAreaCode',
                           'ProgramAreaName',
                           'RcCode',
                           'RcName',
                           'LowerName',
                           'Amount',
                           'Budgeted',
                           'Posted',
                           'OpenCommitment',
                           'ULO',
                           'Expenditure',
                           'Obligation',
                           'Used',
                           'Available',
                           'NpmCode',
                           'NpmName' ]

class StatusOfJobsActFunding( ):
    '''
    Constructor:  StatusOfJobsActFunding(  bfy: str, efy: str,
        fundcode: str, pvdr = Provider.SQLite )

    Purpose: Class defines object for reporting on IIJA funds
    '''
    __source = None
    __provider = None
    __statusofjobsactfundingid = None
    __statusoffundsid = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __rpioname = None
    __fundcode = None
    __fundname = None
    __ahcode = None
    __ahname = None
    __orgcode = None
    __orgname = None
    __accountcode = None
    __boccode = None
    __bocname = None
    __rccode = None
    __rcname = None
    __amount = None
    __budgeted = None
    __posted = None
    __opencommitments = None
    __obligations = None
    __unliquidatedobligations = None
    __expenditures = None
    __used = None
    __avaialable = None
    __programprojectcode = None
    __programprojectname = None
    __programareacode = None
    __programareaname = None
    __goalcode = None
    __goalname = None
    __objectivecode = None
    __objectivename = None
    __npmcode = None
    __npmname = None
    __treasuryaccountcode = None
    __treasuryaccountname = None
    __budgetaccountcode = None
    __budgetaccountname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ) -> int:
        if self.__statusofjobsactfundingid is not None:
            return self.__statusofjobsactfundingid

    @id.setter
    def id( self, value: int ):
        if value is not None:
            self.__statusofjobsactfundingid= value

    @property
    def bfy( self ) -> str:
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value: str ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ) -> str:
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value: str ):
        if value is not None:
            self.__efy = value

    @property
    def rpio_code( self ) -> str:
        if self.__rpiocode is not None:
            return self.__rpiocode

    @rpio_code.setter
    def rpio_code( self, value: str ):
        if value is not None:
            self.__rpiocode = value

    @property
    def rpio_name( self ) -> str:
        if self.__rpioname is not None:
            return self.__rpioname

    @rpio_name.setter
    def rpio_name( self, value: str ):
        if value is not None:
            self.__rpioname = value

    @property
    def ah_code( self ) -> str:
        if self.__ahcode is not None:
            return self.__ahcode

    @ah_code.setter
    def ah_code( self, value: str ):
        if value is not None:
            self.__ahcode = value

    @property
    def ah_name( self ) -> str:
        if self.__ahname is not None:
            return self.__ahname

    @ah_name.setter
    def ah_name( self, value: str ):
        if value is not None:
            self.__ahname = value

    @property
    def fund_code( self ) -> str:
        if self.__fundcode is not None:
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value: str ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund_name( self ) -> str:
        if self.__fundname is not None:
            return self.__fundname

    @fund_name.setter
    def fund_name( self, value: str ):
        if value is not None:
            self.__fundname = value

    @property
    def org_code( self ) -> str:
        if self.__orgcode is not None:
            return self.__orgcode

    @org_code.setter
    def org_code( self, value: str ):
        if value is not None:
            self.__orgcode = value

    @property
    def org_name( self  ):
        if self.__orgname is not None:
            return self.__orgname

    @org_name.setter
    def org_name( self, value  ):
        if value is not None:
            self.__orgname = value

    @property
    def account_code( self ) -> str:
        if self.__accountcode is not None:
            return self.__accountcode

    @account_code.setter
    def account_code( self, value: str ):
        if value is not None:
            self.__accountcode = value

    @property
    def boc_code( self ) -> str:
        if self.__boccode is not None:
            return self.__boccode

    @boc_code.setter
    def boc_code( self, value: str ):
        if value is not None:
            self.__boccode = value

    @property
    def boc_name( self ) -> str:
        if self.__bocname is not None:
            return self.__bocname

    @boc_name.setter
    def boc_name( self, value: str ):
        if value is not None:
            self.__bocname = value

    @property
    def rc_code( self ) -> str:
        if self.__rccode is not None:
            return self.__rccode

    @rc_code.setter
    def rc_code( self, value: str ):
        if value is not None:
            self.__rccode = value

    @property
    def rc_name( self ) -> str:
        if self.__rcname is not None:
            return self.__rcname

    @rc_name.setter
    def rc_name( self, value: str ):
        if value is not None:
            self.__rcname = value

    @property
    def amount( self ) -> float:
        if self.__amount is not None:
            return self.__amount

    @amount.setter
    def amount( self, value: float ):
        if value is not None:
            self.__amount = value

    @property
    def budgeted( self ) -> str:
        if self.__budgeted is not None:
            return self.__budgeted

    @budgeted.setter
    def budgeted( self, value: str ):
        if value is not None:
            self.__budgeted = value

    @property
    def posted( self ) -> float:
        if self.__posted is not None:
            return self.__posted

    @posted.setter
    def posted( self, value: float ):
        if value is not None:
            self.__posted = value

    @property
    def open_commitments( self ) -> float:
        if self.__opencommitments is not None:
            return self.__opencommitments

    @open_commitments.setter
    def open_commitments( self, value: float ):
        if value is not None:
            self.__opencommitments = value

    @property
    def obligations( self ) -> float:
        if self.__obligations is not None:
            return self.__obligations

    @obligations.setter
    def obligations( self, value: float):
        if value is not None:
            self.__obligations = value

    @property
    def unliquidated_obligations( self ) -> float:
        if self.__unliquidatedobligations is not None:
            return self.__unliquidatedobligations

    @unliquidated_obligations.setter
    def unliquidated_obligations( self, value: float ):
        if value is not None:
            self.__unliquidatedobligations = value

    @property
    def expenditures( self ) -> float:
        if self.__expenditures is not None:
            return self.__expenditures

    @expenditures.setter
    def expenditures( self, value: float ):
        if value is not None:
            self.__expenditures = value

    @property
    def used( self ) -> str:
        if self.__used is not None:
            return self.__used

    @used.setter
    def used( self, value: str ):
        if value is not None:
            self.__used = value

    @property
    def available( self ) -> float:
        if self.__avaialable is not None:
            return self.__avaialable

    @available.setter
    def available( self, value: float ):
        if value is not None:
            self.__avaialable = value

    @property
    def program_project_code( self ) -> str:
        if self.__programprojectcode is not None:
            return self.__programprojectcode

    @program_project_code.setter
    def program_project_code( self, value: str ):
        if value is not None:
            self.__programprojectcode = value

    @property
    def program_project_name( self ) -> str:
        if self.__programprojectname is not None:
            return self.__programprojectname

    @program_project_name.setter
    def program_project_name( self, value: str ):
        if value is not None:
            self.__programprojectname = value

    @property
    def program_area_code( self ) -> str:
        if self.__programareacode is not None:
            return self.__programareacode

    @program_area_code.setter
    def program_area_code( self, value: str ):
        if value is not None:
            self.__programareacode = value

    @property
    def program_area_name( self ) -> str:
        if self.__programareaname is not None:
            return self.__programareaname

    @program_area_name.setter
    def program_area_name( self, value: str ):
        if value is not None:
            self.__programareaname = value

    @property
    def goal_code( self ) -> str:
        if self.__goalcode is not None:
            return self.__goalcode

    @goal_code.setter
    def goal_code( self, value: str ):
        if value is not None:
            self.__goalcode = value

    @property
    def goal_name( self ) -> str:
        if self.__goalname is not None:
            return self.__goalname

    @goal_name.setter
    def goal_name( self, value: str ):
        if value is not None:
            self.__goalname = value

    @property
    def objective_code( self ) -> str:
        if self.__objectivecode is not None:
            return self.__objectivecode

    @objective_code.setter
    def objective_code( self, value: str ):
        if value is not None:
            self.__objectivecode = value

    @property
    def objective_name( self ) -> str:
        if self.__objectivename is not None:
            return self.__objectivename

    @objective_name.setter
    def objective_name( self, value: str ):
        if value is not None:
            self.__objectivename = value

    @property
    def npm_code( self ) -> str:
        if self.__npmcode is not None:
            return self.__npmcode

    @npm_code.setter
    def npm_code( self, value: str ):
        if value is not None:
            self.__npmcode = value

    @property
    def npm_name( self ) -> str:
        if self.__npmname is not None:
            return self.__npmname

    @npm_name.setter
    def npm_name( self, value: str ):
        if value is not None:
            self.__npmname = value

    @property
    def treasury_account_code( self ) -> str:
        if self.__treasuryaccountcode is not None:
            return self.__treasuryaccountcode

    @treasury_account_code.setter
    def treasury_account_code( self, value: str ):
        if value is not None:
            self.__treasuryaccountcode = value

    @property
    def treasury_account_name( self ) -> str:
        if self.__treasuryaccountname is not None:
            return self.__treasuryaccountname

    @treasury_account_name.setter
    def treasury_account_name( self, value: str ):
        if value is not None:
            self.__treasuryaccountname = value

    @property
    def budget_account_code( self ) -> str:
        if self.__budgetaccountcode is not None:
            return self.__budgetaccountcode

    @budget_account_code.setter
    def budget_account_code( self, value: str ):
        if value is not None:
            self.__budgetaccountcode = value

    @property
    def budget_account_name( self ) -> str:
        if self.__budgetaccountname is not None:
            return self.__budgetaccountname

    @budget_account_name.setter
    def budget_account_name( self, value: str ):
        if value is not None:
            self.__budgetaccountname = value

    @property
    def fields( self ) -> list[ str ]:
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value: list[ str ] ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy: str, efy: str, fundcode: str, provider = Provider.SQLite ):
        self.__bfy = bfy
        self.__efy = efy
        self.__fundcode = fundcode
        self.__provider = provider
        self.__source = Source.StatusOfJobsActFunding
        self.__fields = [ 'StatusOfJobsActFundingId',
                           'StatusOfFundsId',
                           'BudgetLevel',
                           'BFY',
                           'EFY',
                           'RpioCode',
                           'RpioName',
                           'AhCode',
                           'AhName',
                           'FundCode',
                           'FundName',
                           'OrgCode',
                           'OrgName',
                           'AccountCode',
                           'BocCode',
                           'BocName',
                           'ProgramProjectCode',
                           'ProgramProjectName',
                           'ProgramAreaCode',
                           'ProgramAreaName',
                           'NpmCode',
                           'NpmName',
                           'RcCode',
                           'RcName',
                           'LowerName',
                           'Amount',
                           'Budgeted',
                           'Posted',
                           'OpenCommitment',
                           'ULO',
                           'Expenditure',
                           'Obligation',
                           'Used',
                           'Available' ]

class StatusOfEarmarks( ):
    '''
    Constructor:  StatusOfEarmarks(  bfy: str, efy: str,
     'fundcode: str, pvdr = Provider.SQLite )

     Purpose: Class defines object for reporting on Earmarks
    '''
    __source = None
    __provider = None
    __statusofearmarksid = None
    __statusoffundsid = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __rpioname = None
    __fundcode = None
    __fundname = None
    __ahcode = None
    __ahname = None
    __orgcode = None
    __orgname = None
    __accountcode = None
    __boccode = None
    __bocname = None
    __rccode = None
    __rcname = None
    __amount = None
    __budgeted = None
    __posted = None
    __opencommitments = None
    __obligations = None
    __unliquidatedobligations = None
    __expenditures = None
    __used = None
    __avaialable = None
    __programprojectcode = None
    __programprojectname = None
    __programareacode = None
    __programareaname = None
    __goalcode = None
    __goalname = None
    __objectivecode = None
    __objectivename = None
    __npmcode = None
    __npmname = None
    __statecode = None
    __statename = None
    __zipcode = None
    __treasuryaccountcode = None
    __treasuryaccountname = None
    __budgetaccountcode = None
    __budgetaccountname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ) -> int:
        if self.__statusofearmarksid is not None:
            return self.__statusofearmarksid

    @id.setter
    def id( self, value: int ):
        if value is not None:
            self.__statusofearmarksid = value

    @property
    def bfy( self ) -> str:
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value: str ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ) -> str:
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value: str ):
        if value is not None:
            self.__efy = value

    @property
    def rpio_code( self ) -> str:
        if self.__rpiocode is not None:
            return self.__rpiocode

    @rpio_code.setter
    def rpio_code( self, value: str ):
        if value is not None:
            self.__rpiocode = value

    @property
    def rpio_name( self ) -> str:
        if self.__rpioname is not None:
            return self.__rpioname

    @rpio_name.setter
    def rpio_name( self, value: str ):
        if value is not None:
            self.__rpioname = value

    @property
    def ah_code( self ) -> str:
        if self.__ahcode is not None:
            return self.__ahcode

    @ah_code.setter
    def ah_code( self, value: str ):
        if value is not None:
            self.__ahcode = value

    @property
    def ah_name( self ) -> str:
        if self.__ahname is not None:
            return self.__ahname

    @ah_name.setter
    def ah_name( self, value: str ):
        if value is not None:
            self.__ahname = value

    @property
    def fund_code( self ) -> str:
        if self.__fundcode is not None:
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value: str ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund_name( self ) -> str:
        if self.__fundname is not None:
            return self.__fundname

    @fund_name.setter
    def fund_name( self, value: str ):
        if value is not None:
            self.__fundname = value

    @property
    def org_code( self ) -> str:
        if self.__orgcode is not None:
            return self.__orgcode

    @org_code.setter
    def org_code( self, value: str ):
        if value is not None:
            self.__orgcode = value

    @property
    def org_name( self  ):
        if self.__orgname is not None:
            return self.__orgname

    @org_name.setter
    def org_name( self, value  ):
        if value is not None:
            self.__orgname = value

    @property
    def account_code( self ) -> str:
        if self.__accountcode is not None:
            return self.__accountcode

    @account_code.setter
    def account_code( self, value: str ):
        if value is not None:
            self.__accountcode = value

    @property
    def boc_code( self ) -> str:
        if self.__boccode is not None:
            return self.__boccode

    @boc_code.setter
    def boc_code( self, value: str ):
        if value is not None:
            self.__boccode = value

    @property
    def boc_name( self ) -> str:
        if self.__bocname is not None:
            return self.__bocname

    @boc_name.setter
    def boc_name( self, value: str ):
        if value is not None:
            self.__bocname = value

    @property
    def rc_code( self ) -> str:
        if self.__rccode is not None:
            return self.__rccode

    @rc_code.setter
    def rc_code( self, value: str ):
        if value is not None:
            self.__rccode = value

    @property
    def rc_name( self ) -> str:
        if self.__rcname is not None:
            return self.__rcname

    @rc_name.setter
    def rc_name( self, value: str ):
        if value is not None:
            self.__rcname = value

    @property
    def zip_code( self ) -> str:
        if self.__zipcode is not None:
            return self.__zipcode

    @zip_code.setter
    def zip_code( self, value: str ):
        if value is not None:
            self.__zipcode = value

    @property
    def state_code( self ) -> str:
        if self.__statecode is not None:
            return self.__statecode

    @state_code.setter
    def state_code( self, value: str ):
        if value is not None:
            self.__statecode = value

    @property
    def state_name( self ) -> str:
        if self.__statename is not None:
            return self.__statename

    @state_name.setter
    def state_name( self, value: str ):
        if value is not None:
            self.__statename = value

    @property
    def amount( self ) -> float:
        if self.__amount is not None:
            return self.__amount

    @amount.setter
    def amount( self, value: float ):
        if value is not None:
            self.__amount = value

    @property
    def budgeted( self ) -> float:
        if self.__budgeted is not None:
            return self.__budgeted

    @budgeted.setter
    def budgeted( self, value: float ):
        if value is not None:
            self.__budgeted = value

    @property
    def posted( self ) -> float:
        if self.__posted is not None:
            return self.__posted

    @posted.setter
    def posted( self, value: float ):
        if value is not None:
            self.__posted = value

    @property
    def open_commitments( self ) -> float:
        if self.__opencommitments is not None:
            return self.__opencommitments

    @open_commitments.setter
    def open_commitments( self, value: float ):
        if value is not None:
            self.__opencommitments = value

    @property
    def obligations( self ) -> float:
        if self.__obligations is not None:
            return self.__obligations

    @obligations.setter
    def obligations( self, value: float ):
        if value is not None:
            self.__obligations = value

    @property
    def unliquidated_obligations( self ) -> float:
        if self.__unliquidatedobligations is not None:
            return self.__unliquidatedobligations

    @unliquidated_obligations.setter
    def unliquidated_obligations( self, value: float ):
        if value is not None:
            self.__unliquidatedobligations = value

    @property
    def expenditures( self ) -> float:
        if self.__expenditures is not None:
            return self.__expenditures

    @expenditures.setter
    def expenditures( self, value: float ):
        if value is not None:
            self.__expenditures = value

    @property
    def used( self ) -> float:
        if self.__used is not None:
            return self.__used

    @used.setter
    def used( self, value: float ):
        if value is not None:
            self.__used = value

    @property
    def available( self ) -> float:
        if self.__avaialable is not None:
            return self.__avaialable

    @available.setter
    def available( self, value: float ):
        if value is not None:
            self.__avaialable = value

    @property
    def program_project_code( self ) -> str:
        if self.__programprojectcode is not None:
            return self.__programprojectcode

    @program_project_code.setter
    def program_project_code( self, value: str ):
        if value is not None:
            self.__programprojectcode = value

    @property
    def program_project_name( self ) -> str:
        if self.__programprojectname is not None:
            return self.__programprojectname

    @program_project_name.setter
    def program_project_name( self, value: str ):
        if value is not None:
            self.__programprojectname = value

    @property
    def program_area_code( self ) -> str:
        if self.__programareacode is not None:
            return self.__programareacode

    @program_area_code.setter
    def program_area_code( self, value: str ):
        if value is not None:
            self.__programareacode = value

    @property
    def program_area_name( self ) -> str:
        if self.__programareaname is not None:
            return self.__programareaname

    @program_area_name.setter
    def program_area_name( self, value: str ):
        if value is not None:
            self.__programareaname = value

    @property
    def goal_code( self ) -> str:
        if self.__goalcode is not None:
            return self.__goalcode

    @goal_code.setter
    def goal_code( self, value: str ):
        if value is not None:
            self.__goalcode = value

    @property
    def goal_name( self ) -> str:
        if self.__goalname is not None:
            return self.__goalname

    @goal_name.setter
    def goal_name( self, value: str ):
        if value is not None:
            self.__goalname = value

    @property
    def objective_code( self ) -> str:
        if self.__objectivecode is not None:
            return self.__objectivecode

    @objective_code.setter
    def objective_code( self, value: str ):
        if value is not None:
            self.__objectivecode = value

    @property
    def objective_name( self ) -> str:
        if self.__objectivename is not None:
            return self.__objectivename

    @objective_name.setter
    def objective_name( self, value: str ):
        if value is not None:
            self.__objectivename = value

    @property
    def npm_code( self ) -> str:
        if self.__npmcode is not None:
            return self.__npmcode

    @npm_code.setter
    def npm_code( self, value: str ):
        if value is not None:
            self.__npmcode = value

    @property
    def npm_name( self ) -> str:
        if self.__npmname is not None:
            return self.__npmname

    @npm_name.setter
    def npm_name( self, value: str ):
        if value is not None:
            self.__npmname = value

    @property
    def treasury_account_code( self ) -> str:
        if self.__treasuryaccountcode is not None:
            return self.__treasuryaccountcode

    @treasury_account_code.setter
    def treasury_account_code( self, value: str ):
        if value is not None:
            self.__treasuryaccountcode = value

    @property
    def treasury_account_name( self ) -> str:
        if self.__treasuryaccountname is not None:
            return self.__treasuryaccountname

    @treasury_account_name.setter
    def treasury_account_name( self, value: str ):
        if value is not None:
            self.__treasuryaccountname = value

    @property
    def budget_account_code( self ) -> str:
        if self.__budgetaccountcode is not None:
            return self.__budgetaccountcode

    @budget_account_code.setter
    def budget_account_code( self, value: str ):
        if value is not None:
            self.__budgetaccountcode = value

    @property
    def budget_account_name( self ) -> str:
        if self.__budgetaccountname is not None:
            return self.__budgetaccountname

    @budget_account_name.setter
    def budget_account_name( self, value: str ):
        if value is not None:
            self.__budgetaccountname = value

    @property
    def fields( self ) -> list[ str ]:
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value: list[ str ] ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy: str, efy: str, fundcode: str, provider = Provider.SQLite ):
        self.__bfy = bfy
        self.__efy = efy
        self.__fundcode = fundcode
        self.__provider = provider
        self.__source = Source.StatusOfEarmarks
        self.__fields = [ 'StatusOfEarmarksId',
                           'StatusOfFundsId',
                           'BudgetLevel',
                           'BFY',
                           'EFY',
                           'RpioCode',
                           'RpioName',
                           'AhCode',
                           'AhName',
                           'FundCode',
                           'FundName',
                           'OrgCode',
                           'OrgName',
                           'AccountCode',
                           'BocCode',
                           'BocName',
                           'ProgramProjectCode',
                           'ProgramProjectName',
                           'ProgramAreaCode',
                           'ProgramAreaName',
                           'NpmCode',
                           'NpmName',
                           'RcCode',
                           'RcName',
                           'LowerName',
                           'Amount',
                           'Budgeted',
                           'Posted',
                           'OpenCommitment',
                           'ULO',
                           'Expenditure',
                           'Obligation',
                           'Used',
                           'Available' ]

class StatusOfSuperfundSites( ):
    '''
    Constructor:  StatusOfSuperfundSites(  bfy: str, efy: str,
     'fundcode: str, pvdr = Provider.SQLite )

     Purpose: Class defines object for reporting on Earmarks
    '''
    __source = None
    __provider = None
    __statusofsuperfundsitesid = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __rpioname = None
    __fundcode = None
    __fundname = None
    __programprojectcode = None
    __programprojectname = None
    __cityname = None
    __siteid = None
    __sitename = None
    __statecode = None
    __statename = None
    __countyname = None
    __zipcode = None
    __streetaddress = None
    __zipcode = None
    __obligations = None
    __deobligations = None
    __expenditures = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ) -> int:
        if self.__statusofsuperfundsitesid is not None:
            return self.__statusofsuperfundsitesid

    @id.setter
    def id( self, value: int ):
        if value is not None:
            self.__statusofsuperfundsitesid = value

    @property
    def bfy( self ) -> str:
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value: str ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ) -> str:
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value: str ):
        if value is not None:
            self.__efy = value

    @property
    def rpio_code( self ) -> str:
        if self.__rpiocode is not None:
            return self.__rpiocode

    @rpio_code.setter
    def rpio_code( self, value: str ):
        if value is not None:
            self.__rpiocode = value

    @property
    def rpio_name( self ) -> str:
        if self.__rpioname is not None:
            return self.__rpioname

    @rpio_name.setter
    def rpio_name( self, value: str ):
        if value is not None:
            self.__rpioname = value

    @property
    def state_code( self ) -> str:
        if self.__statecode is not None:
            return self.__statecode

    @state_code.setter
    def state_code( self, value: str ):
        if value is not None:
            self.__statecode = value

    @property
    def state_name( self ) -> str:
        if self.__statename is not None:
            return self.__statename

    @state_name.setter
    def state_name( self, value: str ):
        if value is not None:
            self.__statename = value

    @property
    def fund_code( self ) -> str:
        if self.__fundcode is not None:
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value: str ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund_name( self ) -> str:
        if self.__fundname is not None:
            return self.__fundname

    @fund_name.setter
    def fund_name( self, value: str ):
        if value is not None:
            self.__fundname = value

    @property
    def county_name( self ) -> str:
        if self.__countyname is not None:
            return self.__countyname

    @county_name.setter
    def county_name( self, value: str ):
        if value is not None:
            self.__countyname = value

    @property
    def zip_code( self ):
        if self.__zipcode is not None:
            return self.__zipcode

    @zip_code.setter
    def zip_code( self, value ):
        if value is not None:
            self.__zipcode = value

    @property
    def street_address( self ) -> str:
        if self.__streetaddress is not None:
            return self.__streetaddress

    @street_address.setter
    def street_address( self, value: str ):
        if value is not None:
            self.__streetaddress = value

    @property
    def program_project_code( self ) -> str:
        if self.__programprojectcode is not None:
            return self.__programprojectcode

    @program_project_code.setter
    def program_project_code( self, value: str ):
        if value is not None:
            self.__programprojectcode = value

    @property
    def program_project_name( self ) -> str:
        if self.__programprojectname is not None:
            return self.__programprojectname

    @program_project_name.setter
    def program_project_name( self, value: str ):
        if value is not None:
            self.__programprojectname = value

    @property
    def site_id( self ) -> str:
        if self.__siteid is not None:
            return self.__siteid

    @site_id.setter
    def site_id( self, value: str ):
        if value is not None:
            self.__siteid = value

    @property
    def site_name( self ) -> str:
        if self.__sitename is not None:
            return self.__sitename

    @site_name.setter
    def site_name( self, value: str ):
        if value is not None:
            self.__sitename = value

    @property
    def city_name( self ) -> str:
        if self.__cityname is not None:
            return self.__cityname

    @city_name.setter
    def city_name( self, value: str ):
        if value is not None:
            self.__cityname = value

    @property
    def obligations( self ) -> float:
        if self.__obligations is not None:
            return self.__obligations

    @obligations.setter
    def obligations( self, value: float ):
        if value is not None:
            self.__obligations = value

    @property
    def deobligations( self ) -> float:
        if self.__deobligations is not None:
            return self.__deobligations

    @deobligations.setter
    def deobligations( self, value: float ):
        if value is not None:
            self.__deobligations = value

    @property
    def expenditures( self ) -> float:
        if self.__expenditures is not None:
            return self.__expenditures

    @expenditures.setter
    def expenditures( self, value: float ):
        if value is not None:
            self.__expenditures = value

    @property
    def fields( self ) -> list[ str ]:
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value: list[ str ] ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy: str, efy: str, rpio: str, provider: Provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.StatusOfSuperfundSites
        self.__bfy = bfy
        self.__efy = efy
        self.__rpiocode = rpio
        self.__fields = [ 'SiteActivityId',
                           'FiscalYear',
                           'BFY',
                           'EFY',
                           'RpioCode',
                           'RpioName',
                           'FundCode',
                           'FundName',
                           'ProgramProjectCode',
                           'ProgramProjectName',
                           'SiteId',
                           'SiteName',
                           'CityName',
                           'StreetAddres',
                           'ZipCode',
                           'CountyName',
                           'StateName',
                           'Obligations',
                           'Deobligations',
                           'Expenditures' ]

    def get_data( self  ) -> list[ Row ]:
        try:
            _source = self.__source
            _provider = self.__provider
            _names = [ 'BFY', 'RpioCode' ]
            _values = (self.__bfy, self.__rpiocode)
            _dbconfig = DbConfig( _source, _provider )
            _sqlconfig = SqlConfig( names = _names, values = _values )
            _connection = Connection( self.__source )
            _sql = SqlStatement( _dbconfig, _sqlconfig )
            _sqlite = _connection.connect( )
            _cursor = _sqlite.cursor( )
            _query = _sql.get_query( )
            _db = _cursor.execute( _query )
            self.__data =  [ i for i in _db.fetchall( ) ]
            _cursor.close( )
            _sqlite.close( )
            return self.__data
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Ninja'
            _exc.cause = 'StatusOfSuperfundSites'
            _exc.method = 'get_data( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def create_frame( self ) -> DataFrame:
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            _source = self.__source
            _data = BudgetData( _source )
            return _data.create_frame( )
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Ninja'
            _exc.cause = 'StatusOfSuperfundSites'
            _exc.method = 'create_frame( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class SpendingDocument( ):
    '''
    Constructor;   SpendingDocument(  bfy: str, efy: str, fund: str, account: str,
                  boc: str, pvdr = Provider.SQLite )

    Purpose:  Class defines object representing Spending documnets
    '''
    __source = None
    __provider = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __rpioname = None
    __fundcode = None
    __fundname = None
    __ahcode = None
    __ahname = None
    __orgcode = None
    __orgname = None
    __accountcode = None
    __programprojectname = None
    __boccode = None
    __bocname = None
    __rccode = None
    __rcname = None
    __documenttype = None
    __documentnumber = None
    __documentcontrolnumber = None
    __referencedocumentnumber = None
    __programprojectcode = None
    __programareacode = None
    __programareaname = None
    __processeddate = None
    __lastactivitydate = None
    __age = None
    __vendorcode = None
    __vendorage = None
    __foccode = None
    __focname = None
    __amount = None
    __commitments = None
    __obligations = None
    __deobligations = None
    __unliquidatedobligations = None
    __goalcode = None
    __goalname = None
    __objectivecode = None
    __objectivename = None
    __npmcode = None
    __npmname = None
    __treasuryaccountcode = None
    __treasuryaccountname = None
    __budgetaccountcode = None
    __budgetaccountname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ) -> int:
        if self.__obligationsid is not None:
            return self.__obligationsid

    @id.setter
    def id( self, value: int ):
        if value is not None:
            self.__obligationsid = value

    @property
    def bfy( self ) -> str:
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value: str ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ) -> str:
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value: str ):
        if value is not None:
            self.__efy = value

    @property
    def rpio_code( self ) -> str:
        if self.__rpiocode is not None:
            return self.__rpiocode

    @rpio_code.setter
    def rpio_code( self, value: str ):
        if value is not None:
            self.__rpiocode = value

    @property
    def rpio_name( self ) -> str:
        if self.__rpioname is not None:
            return self.__rpioname

    @rpio_name.setter
    def rpio_name( self, value: str ):
        if value is not None:
            self.__rpiocode = value

    @property
    def ah_code( self ) -> str:
        if self.__ahcode is not None:
            return self.__ahcode

    @ah_code.setter
    def ah_code( self, value: str ):
        if value is not None:
            self.__ahcode = value

    @property
    def ah_name( self ) -> str:
        if self.__ahname is not None:
            return self.__ahname

    @ah_name.setter
    def ah_name( self, value: str ):
        if value is not None:
            self.__ahname = value

    @property
    def fund_code( self ) -> str:
        if self.__fundcode is not None:
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value: str ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund_name( self ) -> str:
        if self.__fundname is not None:
            return self.__fundname

    @fund_name.setter
    def fund_name( self, value: str ):
        if value is not None:
            self.__fundname = value

    @property
    def org_code( self ) -> str:
        if self.__orgcode is not None:
            return self.__orgcode

    @org_code.setter
    def org_code( self, value: str ):
        if value is not None:
            self.__orgcode = value

    @property
    def org_name( self  ):
        if self.__orgname is not None:
            return self.__orgname

    @org_name.setter
    def org_name( self, value  ):
        if value is not None:
            self.__orgname = value

    @property
    def account_code( self ) -> str:
        if self.__accountcode is not None:
            return self.__accountcode

    @account_code.setter
    def account_code( self, value: str ):
        if value is not None:
            self.__accountcode = value

    @property
    def boc_code( self ) -> str:
        if self.__boccode is not None:
            return self.__boccode

    @boc_code.setter
    def boc_code( self, value: str ):
        if value is not None:
            self.__boccode = value

    @property
    def boc_name( self ) -> str:
        if self.__bocname is not None:
            return self.__bocname

    @boc_name.setter
    def boc_name( self, value: str ):
        if value is not None:
            self.__bocname = value

    @property
    def rc_code( self ) -> str:
        if self.__rccode is not None:
            return self.__rccode

    @rc_code.setter
    def rc_code( self, value: str ):
        if value is not None:
            self.__rccode = value

    @property
    def rc_name( self ) -> str:
        if self.__rcname is not None:
            return self.__rcname

    @rc_name.setter
    def rc_name( self, value: str ):
        if value is not None:
            self.__rcname = value

    @property
    def amount( self ) -> float:
        if self.__amount is not None:
            return self.__amount

    @amount.setter
    def amount( self, value: float ):
        if value is not None:
            self.__amount = value

    @property
    def budgeted( self ) -> str:
        if self.__budgeted is not None:
            return self.__budgeted

    @budgeted.setter
    def budgeted( self, value: str ):
        if value is not None:
            self.__budgeted = value

    @property
    def posted( self ) -> float:
        if self.__posted is not None:
            return self.__posted

    @posted.setter
    def posted( self, value: float ):
        if value is not None:
            self.__posted = value

    @property
    def commitments( self ) -> str:
        if self.__commitments is not None:
            return self.__commitments

    @commitments.setter
    def commitments( self, value: str ):
        if value is not None:
            self.__commitments = value

    @property
    def obligations( self ) -> float:
        if self.__obligations is not None:
            return self.__obligations

    @obligations.setter
    def obligations( self, value: float ):
        if value is not None:
            self.__obligations = value

    @property
    def unliquidated_obligations( self ) -> float:
        if self.__unliquidatedobligations is not None:
            return self.__unliquidatedobligations

    @unliquidated_obligations.setter
    def unliquidated_obligations( self, value: float ):
        if value is not None:
            self.__unliquidatedobligations = value

    @property
    def expenditures( self ) -> float:
        if self.__expenditures is not None:
            return self.__expenditures

    @expenditures.setter
    def expenditures( self, value: float ):
        if value is not None:
            self.__expenditures = value

    @property
    def used( self ) -> str:
        if self.__used is not None:
            return self.__used

    @used.setter
    def used( self, value: str ):
        if value is not None:
            self.__used = value

    @property
    def available( self ) -> float:
        if self.__avaialable is not None:
            return self.__avaialable

    @available.setter
    def available( self, value: float ):
        if value is not None:
            self.__avaialable = value

    @property
    def program_project_code( self ) -> str:
        if self.__programprojectcode is not None:
            return self.__programprojectcode

    @program_project_code.setter
    def program_project_code( self, value: str ):
        if value is not None:
            self.__programprojectcode = value

    @property
    def program_project_name( self ) -> str:
        if self.__programprojectname is not None:
            return self.__programprojectname

    @program_project_name.setter
    def program_project_name( self, value: str ):
        if value is not None:
            self.__programprojectname = value

    @property
    def program_area_code( self ) -> str:
        if self.__programareacode is not None:
            return self.__programareacode

    @program_area_code.setter
    def program_area_code( self, value: str ):
        if value is not None:
            self.__programareacode = value

    @property
    def program_area_name( self ) -> str:
        if self.__programareaname is not None:
            return self.__programareaname

    @program_area_name.setter
    def program_area_name( self, value: str ):
        if value is not None:
            self.__programareaname = value

    @property
    def goal_code( self ) -> str:
        if self.__goalcode is not None:
            return self.__goalcode

    @goal_code.setter
    def goal_code( self, value: str ):
        if value is not None:
            self.__goalcode = value

    @property
    def goal_name( self ) -> str:
        if self.__goalname is not None:
            return self.__goalname

    @goal_name.setter
    def goal_name( self, value: str ):
        if value is not None:
            self.__goalname = value

    @property
    def objective_code( self ) -> str:
        if self.__objectivecode is not None:
            return self.__objectivecode

    @objective_code.setter
    def objective_code( self, value: str ):
        if value is not None:
            self.__objectivecode = value

    @property
    def objective_name( self ) -> str:
        if self.__objectivename is not None:
            return self.__objectivename

    @objective_name.setter
    def objective_name( self, value: str ):
        if value is not None:
            self.__objectivename = value

    @property
    def npm_code( self ) -> str:
        if self.__npmcode is not None:
            return self.__npmcode

    @npm_code.setter
    def npm_code( self, value: str ):
        if value is not None:
            self.__npmcode = value

    @property
    def npm_name( self ) -> str:
        if self.__npmname is not None:
            return self.__npmname

    @npm_name.setter
    def npm_name( self, value: str ):
        if value is not None:
            self.__npmname = value

    @property
    def document_type( self ) -> str:
        if self.__documenttype is not None:
            return self.__documenttype

    @document_type.setter
    def document_type( self, value: str ):
        if value is not None:
            self.__documenttype = value

    @property
    def document_number( self ) -> str:
        if self.__documentnumber is not None:
            return self.__documentnumber

    @document_number.setter
    def document_number( self, value: str ):
        if value is not None:
            self.__documentnumber = value

    @property
    def document_control_number( self ) -> str:
        if self.__documentcontrolnumber is not None:
            return self.__documentcontrolnumber

    @document_control_number.setter
    def document_control_number( self, value: str ):
        if value is not None:
            self.__documentcontrolnumber = value

    @property
    def reference_document_number( self ) -> str:
        if self.__referencedocumentnumber is not None:
            return self.__referencedocumentnumber

    @reference_document_number.setter
    def reference_document_number( self, value: str ):
        if value is not None:
            self.__referencedocumentnumber = value

    @property
    def processed_date( self ) -> datetime:
        if self.__processeddate is not None:
            return self.__processeddate

    @processed_date.setter
    def processed_date( self, value: datetime ):
        if isinstance( value, datetime ):
            self.__processeddate = value

    @property
    def last_activity_date( self ) -> datetime:
        if self.__lastactivitydate is not None:
            return self.__lastactivitydate

    @last_activity_date.setter
    def last_activity_date( self, value: datetime ):
        if value is not None:
            self.__lastactivitydate = value

    @property
    def age( self ) -> float:
        if self.__age is not None:
            return self.__age

    @age.setter
    def age( self, value: float ):
        if value is not None:
            self.__age = value

    @property
    def vendor_code( self ) -> str:
        if self.__vendorcode is not None:
            return self.__vendorcode

    @vendor_code.setter
    def vendor_code( self, value: str ):
        if value is not None:
            self.__vendorcode = value

    @property
    def vendor_name( self ) -> str:
        if self.__vendorname is not None:
            return self.__vendorname

    @vendor_name.setter
    def vendor_name( self, value: str ):
        if value is not None:
            self.__vendorname = value

    @property
    def foc_code( self ) -> str:
        if self.__foccode is not None:
            return self.__foccode

    @foc_code.setter
    def foc_code( self, value: str ):
        if value is not None:
            self.__foccode = value

    @property
    def foc_name( self ) -> str:
        if self.__focname is not None:
            return self.__focname

    @foc_name.setter
    def foc_name( self, value: str ):
        if value is not None:
            self.__focname = value

    @property
    def treasury_account_code( self ) -> str:
        if self.__treasuryaccountcode is not None:
            return self.__treasuryaccountcode

    @treasury_account_code.setter
    def treasury_account_code( self, value: str ):
        if value is not None:
            self.__treasuryaccountcode = value

    @property
    def treasury_account_name( self ) -> str:
        if self.__treasuryaccountname is not None:
            return self.__treasuryaccountname

    @treasury_account_name.setter
    def treasury_account_name( self, value: str ):
        if value is not None:
            self.__treasuryaccountname = value

    @property
    def budget_account_code( self ) -> str:
        if self.__budgetaccountcode is not None:
            return self.__budgetaccountcode

    @budget_account_code.setter
    def budget_account_code( self, value: str ):
        if value is not None:
            self.__budgetaccountcode = value

    @property
    def budget_account_name( self ) -> str:
        if self.__budgetaccountname is not None:
            return self.__budgetaccountname

    @budget_account_name.setter
    def budget_account_name( self, value: str ):
        if value is not None:
            self.__budgetaccountname = value

    @property
    def fields( self ) -> list[ str ]:
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value: list[ str ] ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy: str, efy: str, fund: str, account: str,
                  boc: str, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.Obligations
        self.__bfy = bfy
        self.__efy = efy
        self.__fundcode = fund
        self.__accountcode = account
        self.__boccode = boc
        self.__fields = [ 'ObligationsId',
                           'BFY',
                           'EFY',
                           'RpioCode',
                           'RpioName',
                           'AhCode',
                           'AhName',
                           'FundCode',
                           'FundName',
                           'OrgCode',
                           'OrgName',
                           'AccountCode',
                           'ProgramProjectCode',
                           'ProgramProjectName',
                           'RcCode',
                           'RcName',
                           'DocumentType',
                           'DocumentNumber',
                           'DocumentControlNumber',
                           'ReferenceDocumentNumber',
                           'ProcessedDate',
                           'LastActivityDate',
                           'Age',
                           'BocCode',
                           'BocName',
                           'FocCode',
                           'FocName',
                           'NpmCode',
                           'NpmName',
                           'VendorCode',
                           'VendorName',
                           'OpenCommitment',
                           'Obligation',
                           'ULO',
                           'Expenditure' ]

    def __str__( self ) -> float:
        if self.__amount is not None:
            return self.__amount

    def get_data( self ) -> list[ Row ]:
        try:
            _source = self.__source
            _provider = self.__provider
            _names = [ 'BFY', 'FundCode', 'AccountCode', 'BocCode' ]
            _values = ( self.__bfy, self.__fundcode, self.__accountcode, self.__boccode )
            _dbconfig = DbConfig( _source, _provider )
            _sqlconfig = SqlConfig( names = _names, values = _values )
            _connection = Connection( self.__source )
            _sql = SqlStatement( _dbconfig, _sqlconfig )
            _sqlite = _connection.connect( )
            _cursor = _sqlite.cursor( )
            _query = _sql.get_query( )
            _db = _cursor.execute( _query )
            self.__data =  [ i for i in _db.fetchall( ) ]
            _cursor.close( )
            _sqlite.close( )
            return self.__data
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Ninja'
            _exc.cause = 'Obligaions'
            _exc.method = 'get_data( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def get_frame( self ) -> DataFrame:
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            _source = self.__source
            _data = BudgetData( _source )
            return _data.create_frame( )
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Ninja'
            _exc.cause = 'Obligation'
            _exc.method = 'create_frame( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class SupplementalCarryoverEstimate( ):
    '''
    Constructor:  CarryoverEstimate( bfy: str, pvdr: Provider = Provider.SQLite )

    Purpose:  Class defines object providing Supplemental Carryover Estimate data for'''
    __source = None
    __provider = None
    __supplementalcarryoverestimatesid = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __rpioname = None
    __fundcode = None
    __fundname = None
    __amount = None
    __opencommitments = None
    __obligations = None
    __estimate = None
    __treasuryaccountcode = None
    __treasuryaccountname = None
    __budgetaccountcode = None
    __budgetaccountname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ) -> int:
        if self.__annualcarryoverestimatesid is not None:
            return self.__annualcarryoverestimatesid

    @id.setter
    def id( self, value: int ):
        if value is not None:
            self.__annualcarryoverestimatesid = value

    @property
    def bfy( self ) -> str:
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value: str ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ) -> str:
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value: str ):
        if value is not None:
            self.__efy = value

    @property
    def rpio_code( self ) -> str:
        if self.__rpiocode is not None:
            return self.__rpiocode

    @rpio_code.setter
    def rpio_code( self, value: str ):
        if value is not None:
            self.__rpiocode = value

    @property
    def rpio_name( self ) -> str:
        if self.__rpioname is not None:
            return self.__rpioname

    @rpio_code.setter
    def rpio_code( self, value: str ):
        if value is not None:
            self.__rpiocode = value

    @property
    def fund_code( self ) -> str:
        if self.__fundcode is not None:
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value: str ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund_name( self ) -> str:
        if self.__fundname is not None:
            return self.__fundname

    @fund_name.setter
    def fund_name( self, value: str ):
        if value is not None:
            self.__fundname = value

    @property
    def amount( self ) -> float:
        if self.__amount is not None:
            return self.__amount

    @amount.setter
    def amount( self, value: float ):
        if value is not None:
            self.__amount = value

    @property
    def available( self ) -> float:
        if self.__availablebalance is not None:
            return self.__availablebalance

    @available.setter
    def available( self, value: float ):
        if value is not None:
            self.__availablebalance = value

    @property
    def open_commitments( self ) -> float:
        if self.__opencommitments is not None:
            return self.__opencommitments

    @open_commitments.setter
    def open_commitments( self, value: float ):
        if value is not None:
            self.__opencommitments = value

    @property
    def obligations( self ) -> float:
        if self.__obligations is not None:
            return self.__obligations

    @obligations.setter
    def obligations( self, value: float ):
        if value is not None:
            self.__obligations = value

    @property
    def treasury_account_code( self ) -> str:
        if self.__treasuryaccountcode is not None:
            return self.__treasuryaccountcode

    @treasury_account_code.setter
    def treasury_account_code( self, value: str ):
        if value is not None:
            self.__treasuryaccountcode = value

    @property
    def treasury_account_name( self ) -> str:
        if self.__treasuryaccountname is not None:
            return self.__treasuryaccountname

    @treasury_account_name.setter
    def treasury_account_name( self, value: str ):
        if value is not None:
            self.__treasuryaccountname = value

    @property
    def budget_account_code( self ) -> str:
        if self.__budgetaccountcode is not None:
            return self.__budgetaccountcode

    @budget_account_code.setter
    def budget_account_code( self, value: str ):
        if value is not None:
            self.__budgetaccountcode = value

    @property
    def budget_account_name( self ) -> str:
        if self.__budgetaccountname is not None:
            return self.__budgetaccountname

    @budget_account_name.setter
    def budget_account_name( self, value: str ):
        if value is not None:
            self.__budgetaccountname = value

    @property
    def data( self ) -> list[ Row ]:
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, value: list[ Row ] ):
        if isinstance( value, list ):
            self.__data = value

    @property
    def table( self ) -> DataFrame:
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, value: DataFrame ):
        if value is not None:
            self.__frame = value

    @property
    def fields( self ) -> list[ str ]:
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value: list[ str ] ):
        if value is not None:
            self.__fields = value


    def __init__( self, bfy: str, provider: Provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.SupplementalCarryoverEstimates
        self.__bfy = bfy
        self.__fields = [ 'CarryoverEstimatesId',
                           'BudgetLevel',
                           'BFY',
                           'EFY',
                           'RpioCode',
                           'RpioName',
                           'AhCode',
                           'AhName',
                           'FundCode',
                           'FundName',
                           'OrgCode',
                           'AccountCode',
                           'ProgramProjectCode',
                           'ProgramProjectName',
                           'ProgramAreaCode',
                           'ProgramAreaName',
                           'BocCode',
                           'BocName',
                           'AvailableBalance',
                           'OpenCommitment',
                           'UnobligatedAuthority' ]

    def __str__( self ) -> str:
        if  self.__rpiocode is not None:
            return self.__rpiocode

    def get_data( self  ) -> list[ Row ]:
        try:
            _source = self.__source
            _provider = self.__provider
            _names = [ 'BFY', 'EFY' ]
            _values = (self.__bfy, self.__efy)
            _dbconfig = DbConfig( _source, _provider )
            _sqlconfig = SqlConfig( names = _names, values = _values )
            _connection = Connection( self.__source )
            _sql = SqlStatement( _dbconfig, _sqlconfig )
            _sqlite = _connection.connect( )
            _cursor = _sqlite.cursor( )
            _query = _sql.get_query( )
            _db = _cursor.execute( _query )
            self.__data =  [ i for i in _db.fetchall( ) ]
            _cursor.close( )
            _sqlite.close( )
            return self.__data
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Reporting'
            _exc.cause = 'CarryoverEstimate'
            _exc.method = 'get_data( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def get_frame( self ) -> DataFrame:
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            _source = self.__source
            _data = BudgetData( _source )
            return _data.create_frame( )
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Reporting'
            _exc.cause = 'CarryoverEstimate'
            _exc.method = 'create_frame( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class SupplementalOutlayEstimate( ):
    '''
    Constructor:  CarryoverEstimate( bfy: str, pvdr: Provider = Provider.SQLite )

    Purpose:  Class defines object providing Supplemental Carryover Estimate data for'''
    __source = None
    __provider = None
    __supplementaloutlayestimatesid = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __rpioname = None
    __fundcode = None
    __fundname = None
    __amount = None
    __opencommitments = None
    __obligations = None
    __estimate = None
    __treasuryaccountcode = None
    __treasuryaccountname = None
    __budgetaccountcode = None
    __budgetaccountname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ) -> int:
        if self.__annualcarryoverestimatesid is not None:
            return self.__annualcarryoverestimatesid

    @id.setter
    def id( self, value: int ):
        if value is not None:
            self.__annualcarryoverestimatesid = value

    @property
    def bfy( self ) -> str:
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value: str ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ) -> str:
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value: str ):
        if value is not None:
            self.__efy = value

    @property
    def rpio_code( self ) -> str:
        if self.__rpiocode is not None:
            return self.__rpiocode

    @rpio_code.setter
    def rpio_code( self, value: str ):
        if value is not None:
            self.__rpiocode = value

    @property
    def rpio_name( self ) -> str:
        if self.__rpioname is not None:
            return self.__rpioname

    @rpio_code.setter
    def rpio_code( self, value: str ):
        if value is not None:
            self.__rpiocode = value

    @property
    def fund_code( self ) -> str:
        if self.__fundcode is not None:
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value: str ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund_name( self ) -> str:
        if self.__fundname is not None:
            return self.__fundname

    @fund_name.setter
    def fund_name( self, value: str ):
        if value is not None:
            self.__fundname = value

    @property
    def amount( self ) -> float:
        if self.__amount is not None:
            return self.__amount

    @amount.setter
    def amount( self, value: float ):
        if value is not None:
            self.__amount = value

    @property
    def available( self ) -> float:
        if self.__availablebalance is not None:
            return self.__availablebalance

    @available.setter
    def available( self, value: float ):
        if value is not None:
            self.__availablebalance = value

    @property
    def open_commitments( self ) -> float:
        if self.__opencommitments is not None:
            return self.__opencommitments

    @open_commitments.setter
    def open_commitments( self, value: float ):
        if value is not None:
            self.__opencommitments = value

    @property
    def obligations( self ) -> float:
        if self.__obligations is not None:
            return self.__obligations

    @obligations.setter
    def obligations( self, value: float ):
        if value is not None:
            self.__obligations = value

    @property
    def treasury_account_code( self ) -> str:
        if self.__treasuryaccountcode is not None:
            return self.__treasuryaccountcode

    @treasury_account_code.setter
    def treasury_account_code( self, value: str ):
        if value is not None:
            self.__treasuryaccountcode = value

    @property
    def treasury_account_name( self ) -> str:
        if self.__treasuryaccountname is not None:
            return self.__treasuryaccountname

    @treasury_account_name.setter
    def treasury_account_name( self, value: str ):
        if value is not None:
            self.__treasuryaccountname = value

    @property
    def budget_account_code( self ) -> str:
        if self.__budgetaccountcode is not None:
            return self.__budgetaccountcode

    @budget_account_code.setter
    def budget_account_code( self, value: str ):
        if value is not None:
            self.__budgetaccountcode = value

    @property
    def budget_account_name( self ) -> str:
        if self.__budgetaccountname is not None:
            return self.__budgetaccountname

    @budget_account_name.setter
    def budget_account_name( self, value: str ):
        if value is not None:
            self.__budgetaccountname = value

    @property
    def data( self ) -> list[ Row ]:
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, value: list[ Row ] ):
        if isinstance( value, list ):
            self.__data = value

    @property
    def table( self ) -> DataFrame:
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, value: DataFrame ):
        if value is not None:
            self.__frame = value

    @property
    def fields( self ) -> list[ str ]:
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value: list[ str ] ):
        if value is not None:
            self.__fields = value


    def __init__( self, bfy: str, provider: Provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.SupplementalCarryoverEstimates
        self.__bfy = bfy
        self.__fields = [ 'CarryoverEstimatesId',
                           'BudgetLevel',
                           'BFY',
                           'EFY',
                           'RpioCode',
                           'RpioName',
                           'AhCode',
                           'AhName',
                           'FundCode',
                           'FundName',
                           'OrgCode',
                           'AccountCode',
                           'ProgramProjectCode',
                           'ProgramProjectName',
                           'ProgramAreaCode',
                           'ProgramAreaName',
                           'BocCode',
                           'BocName',
                           'AvailableBalance',
                           'OpenCommitment',
                           'UnobligatedAuthority' ]

    def __str__( self ) -> str:
        if  self.__rpiocode is not None:
            return self.__rpiocode

    def get_data( self  ) -> list[ Row ]:
        try:
            _source = self.__source
            _provider = self.__provider
            _names = [ 'BFY', 'EFY' ]
            _values = (self.__bfy, self.__efy)
            _dbconfig = DbConfig( _source, _provider )
            _sqlconfig = SqlConfig( names = _names, values = _values )
            _connection = Connection( self.__source )
            _sql = SqlStatement( _dbconfig, _sqlconfig )
            _sqlite = _connection.connect( )
            _cursor = _sqlite.cursor( )
            _query = _sql.get_query( )
            _db = _cursor.execute( _query )
            self.__data =  [ i for i in _db.fetchall( ) ]
            _cursor.close( )
            _sqlite.close( )
            return self.__data
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Reporting'
            _exc.cause = 'CarryoverEstimate'
            _exc.method = 'get_data( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def get_frame( self ) -> DataFrame:
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            _source = self.__source
            _data = BudgetData( _source )
            return _data.create_frame( )
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Reporting'
            _exc.cause = 'CarryoverEstimate'
            _exc.method = 'create_frame( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class TreasurySymbol( ):
    '''
    Constructor:  TreasurySymbol( bfy: str, efy: str,
                treas: str, pvdr: Provider = Provider.SQLite)

    Purpose:  Class defines object that represents a TAFS'''
    __source = None
    __provider = None
    __treasurysymbolsid = None
    __ombagencycode = None
    __treasuryagencycode = None
    __bfy = None
    __efy = None
    __budgetaccountcode = None
    __budgetaccountname = None
    __treasuryaccountcode = None
    __treasuryaccountname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ) -> int:
        if self.__treasurysymbolsid is not None:
            return self.__treasurysymbolsid

    @id.setter
    def id( self, value: int ):
        if value is not None:
            self.__treasurysymbolsid = value

    @property
    def bfy( self ) -> str:
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value: str ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ) -> str:
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value: str ):
        if value is not None:
            self.__efy = value

    @property
    def treasury_account_code( self ) -> str:
        if self.__treasuryaccountcode is not None:
            return self.__treasuryaccountcode

    @treasury_account_code.setter
    def treasury_account_code( self, value: str ):
        if value is not None:
            self.__treasuryaccountcode = value

    @property
    def treasury_account_name( self ) -> str:
        if self.__treasuryaccountname is not None:
            return self.__treasuryaccountname

    @treasury_account_name.setter
    def treasury_account_name( self, value: str ):
        if value is not None:
            self.__treasuryaccountname = value

    @property
    def budget_account_code( self ) -> str:
        if self.__budgetaccountcode is not None:
            return self.__budgetaccountcode

    @budget_account_code.setter
    def budget_account_code( self, value: str ):
        if value is not None:
            self.__budgetaccountcode = value

    @property
    def budget_account_name( self ) -> str:
        if self.__budgetaccountname is not None:
            return self.__budgetaccountname

    @budget_account_name.setter
    def budget_account_name( self, value: str ):
        if value is not None:
            self.__budgetaccountname = value

    @property
    def fields( self ) -> list[ str ]:
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value: list[ str ] ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy: str, efy: str, treas: str, provider: Provider = Provider.SQLite ):
        self.__provider = provider
        self.__soruce = Source.FundSymbols
        self.__bfy = bfy
        self.__efy = efy
        self.__treasuryaccountcode = treas
        self.__fields = [ 'TreasurySymbolsId',
                          'BFY',
                          'EFY',
                          'FundCode',
                          'FundName',
                          'TreasuryAccountCode',
                          'TreasuryAccountName',
                          'OmbAccountCode',
                          'OmbAccountName',
                          'ApportionmentAccountCode' ]

    def __str__( self ) -> str:
        if self.__treasuryaccountname is not None:
            return self.__treasuryaccountname

    def get_data( self  ) -> list[ Row ]:
        try:
            _source = self.__source
            _provider = self.__provider
            command = SQL.SELECTALL
            _names = [ 'BFY', 'EFY', 'TreasuryAccountCode' ]
            _values = (self.__bfy, self.__efy, self.__treasuryaccountcode)
            dbcfg = DbConfig( _source, _provider )
            sqlcfg = SqlConfig( names = _names, values = _values )
            _connection = Connection( self.__source )
            _sql = SqlStatement( dbcfg, sqlcfg )
            _sqlite = _connection.connect( )
            _cursor = _sqlite.cursor( )
            _query = _sql.get_query( )
            _db = _cursor.execute( _query )
            self.__data =  [ i for i in _db.fetchall( ) ]
            _cursor.close( )
            _sqlite.close( )
            return self.__data
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Execution'
            _exc.cause = 'TreasurySymbol'
            _exc.method = 'get_data( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def get_frame( self ) -> DataFrame:
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            _source = self.__source
            _data = BudgetData( _source )
            return _data.create_frame( )
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Execution'
            _exc.cause = 'TreasurySymbol'
            _exc.method = 'create_frame( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class Transfer( ):
    '''
     Constructor:  Transfer( documentnumber: str, pvdr = Provider.SQLite )

     Purpose:  Class defines object representing EPA reprogrammings'''
    __source = None
    __provider = None
    __transfersid = None
    __documenttype = None
    __documentnumber = None
    __processeddate = None
    __budgetlevel = None
    __rpiocode = None
    __rpioname = None
    __bfy = None
    __efy = None
    __ahcode = None
    __ahname = None
    __fundcode = None
    __fundname = None
    __orgcode = None
    __orgname = None
    __accountcode = None
    __rccode = None
    __rcname = None
    __boccode = None
    __bocname = None
    __amount = None
    __programprojectcode = None
    __programprojectname = None
    __programareacode = None
    __programareaname = None
    __treasuryaccountcode = None
    __treasuryaccountname = None
    __budgetaccountcode = None
    __budgetaccountname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ) -> int:
        if self.__transfersid is not None:
            return self.__transfersid

    @id.setter
    def id( self, value: int ):
        if value is not None:
            self.__transfersid = value

    @property
    def bfy( self ) -> str:
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value: str ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ) -> str:
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value: str ):
        if value is not None:
            self.__efy = value

    @property
    def budget_level( self ) -> str:
        if self.__budgetlevel is not None:
            return self.__budgetlevel

    @budget_level.setter
    def budget_level( self, value: str ):
        if value is not None:
            self.__budgetlevel = value

    @property
    def document_type( self ) -> str:
        if self.__documenttype is not None:
            return self.__documenttype

    @document_type.setter
    def document_type( self, value: str ):
        if value is not None:
            self.__documenttype = value

    @property
    def document_number( self ) -> str:
        if self.__documentnumber is not None:
            return self.__documentnumber

    @document_number.setter
    def document_number( self, value: str ):
        if value is not None:
            self.__documentnumber = value

    @property
    def processed_date( self ) -> str:
        if self.__processeddate is not None:
            return self.__processeddate

    @processed_date.setter
    def processed_date( self, value: str ):
        if value is not None:
            self.__processeddate = value

    @property
    def rpio_code( self ) -> str:
        if self.__rpiocode is not None:
            return self.__rpiocode

    @rpio_code.setter
    def rpio_code( self, value: str ):
        if value is not None:
            self.__rpiocode = value

    @property
    def rpio_name( self ) -> str:
        if self.__rpiocode is not None:
            return self.__rpiocode

    @rpio_name.setter
    def rpio_name( self, name ):
        if  name is not None:
            self.__rpiocode = name

    @property
    def fund_code( self ) -> str:
        if self.__fundcode is not None:
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value: str ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund_name( self ) -> str:
        if self.__fundname is not None:
            return self.__fundname

    @fund_name.setter
    def fund_name( self, value: str ):
        if value is not None:
            self.__fundname = value

    @property
    def ah_code( self ) -> str:
        if self.__ahcode is not None:
            return self.__ahcode

    @ah_code.setter
    def ah_code( self, value: str ):
        if value is not None:
            self.__ahcode = value

    @property
    def ah_name( self ) -> str:
        if self.__ahname is not None:
            return self.__ahname

    @ah_name.setter
    def ah_name( self, value: str ):
        if value is not None:
            self.__ahname = value

    @property
    def account_code( self ) -> str:
        if self.__accountcode is not None:
            return self.__accountcode

    @account_code.setter
    def account_code( self, value: str ):
        if value is not None:
            self.__accountcode = value

    @property
    def program_project_code( self ) -> str:
        if self.__programprojectcode is not None:
            return self.__programprojectcode

    @program_project_code.setter
    def program_project_code( self, value: str ):
        if value is not None:
            self.__programprojectcode = value

    @property
    def program_project_name( self ) -> str:
        if self.__programprojectname is not None:
            return self.__programprojectname

    @program_project_name.setter
    def program_project_name( self, value: str ):
        if value is not None:
            self.__programprojectname = value

    @property
    def activity_code( self ) -> str:
        if self.__activitycode is not None:
            return self.__activitycode

    @activity_code.setter
    def activity_code( self, value: str ):
        if value is not None:
            self.__activitycode = value

    @property
    def activity_name( self ) -> str:
        if self.__activityname is not None:
            return self.__activityname

    @activity_name.setter
    def activity_name( self, value: str ):
        if value is not None:
            self.__activityname = value

    @property
    def org_code( self ) -> str:
        if self.__orgcode is not None:
            return self.__orgcode

    @org_code.setter
    def org_code( self, value: str ):
        if value is not None:
            self.__orgcode = value

    @property
    def rc_code( self ) -> str:
        if self.__rccode is not None:
            return self.__rccode

    @rc_code.setter
    def rc_code( self, value: str ):
        if value is not None:
            self.__rccode = value

    @property
    def rc_name( self ) -> str:
        if self.__rcname is not None:
            return self.__rcname

    @rc_name.setter
    def rc_name( self, value: str ):
        if value is not None:
            self.__rcname = value

    @property
    def boc_code( self ) -> str:
        if self.__boccode is not None:
            return self.__boccode

    @boc_code.setter
    def boc_code( self, value: str ):
        if value is not None:
            self.__boccode = value

    @property
    def boc_name( self ) -> str:
        if self.__bocname is not None:
            return self.__bocname

    @boc_name.setter
    def boc_name( self, value: str ):
        if value is not None:
            self.__bocname = value

    @property
    def amount( self ) -> float:
        if self.__amount is not None:
            return self.__amount

    @amount.setter
    def amount( self, value: float ):
        if value is not None:
            self.__amount = value

    @property
    def program_area_code( self ) -> str:
        if self.__programareacode is not None:
            return self.__programareacode

    @program_area_code.setter
    def program_area_code( self, value: str ):
        if value is not None:
            self.__programareacode = value

    @property
    def program_area_name( self ) -> str:
        if self.__programareaname is not None:
            return self.__programareaname

    @program_area_name.setter
    def program_area_name( self, value: str ):
        if value is not None:
            self.__programareaname = value

    @property
    def treasury_account_code( self ) -> str:
        if self.__treasuryaccountcode is not None:
            return self.__treasuryaccountcode

    @treasury_account_code.setter
    def treasury_account_code( self, value: str ):
        if value is not None:
            self.__treasuryaccountcode = value

    @property
    def treasury_account_name( self ) -> str:
        if self.__treasuryaccountname is not None:
            return self.__treasuryaccountname

    @treasury_account_name.setter
    def treasury_account_name( self, value: str ):
        if value is not None:
            self.__treasuryaccountname = value

    @property
    def budget_account_code( self ) -> str:
        if self.__budgetaccountcode is not None:
            return self.__budgetaccountcode

    @budget_account_code.setter
    def budget_account_code( self, value: str ):
        if value is not None:
            self.__budgetaccountcode = value

    @property
    def budget_account_name( self ) -> str:
        if self.__budgetaccountname is not None:
            return self.__budgetaccountname

    @budget_account_name.setter
    def budget_account_name( self, value: str ):
        if value is not None:
            self.__budgetaccountname = value

    @property
    def fields( self ) -> list[ str ]:
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value: list[ str ] ):
        if value is not None:
            self.__fields = value

    def __init__( self, documentnumber: str, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.Transfers
        self.__documentnumber = documentnumber
        self.__fields = [ 'TransfersId',
                           'BudgetLevel',
                           'DocPrefix',
                           'DocType',
                           'BFY',
                           'RpioCode',
                           'RpioName',
                           'FundCode',
                           'FundName',
                           'ReprogrammingNumber',
                           'ControlNumber',
                           'ProcessedDate',
                           'Quarter',
                           'Line',
                           'Subline',
                           'AhCode',
                           'AhName',
                           'OrgCode',
                           'OrgName',
                           'RcCode',
                           'RcName',
                           'AccountCode',
                           'ProgramAreaCode',
                           'ProgramAreaName',
                           'ProgramProjectName',
                           'ProgramProjectCode',
                           'FromTo',
                           'BocCode',
                           'BocName',
                           'NpmCode',
                           'Amount',
                           'ResourceType',
                           'Purpose',
                           'ExtendedPurpose' ]

    def get_data( self  ) -> list[ Row ]:
        try:
            _source = self.__source
            command = SQL.SELECTALL
            _names = [ 'DocumentNumber', ]
            _values = (self.__documentnumber,)
            _dbconfig = DbConfig( _source  )
            _sqlconfig = SqlConfig( names = _names, values = _values )
            _connection = Connection( self.__source )
            _sql = SqlStatement( _dbconfig, _sqlconfig )
            _sqlite = _connection.connect( )
            _cursor = _sqlite.cursor( )
            _query = _sql.get_query( )
            _db = _cursor.execute( _query )
            self.__data =  [ i for i in _db.fetchall( ) ]
            _cursor.close( )
            _sqlite.close( )
            return self.__data
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Execution'
            _exc.cause = 'Transfer'
            _exc.method = 'get_data( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def get_frame( self ) -> DataFrame:
        '''Method returning pandas dataframe'''
        try:
            _source = self.__source
            _data = BudgetData( _source )
            return _data.create_frame( )
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Execution'
            _exc.cause = 'Transfer'
            _exc.method = 'create_frame( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

class TransType( ):
    '''
    Constructor:  TransType( bfy: str, fundcode: str, pvdr = Provider.SQLite )

    Purpose: Class defines object representing trans types
    '''
    __source = None
    __provider = None
    __transtypesid = None
    __bfy = None
    __efy = None
    __fundcode = None
    __doctype = None
    __appropriationbill = None
    __continuingresolution = None
    __rescissioncurrentyear = None
    __rescissionprioryear = None
    __sequesterreduction = None
    __sequesterreturn = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ) -> int:
        if self.__transtypesid is not None:
            return self.__transtypesid

    @id.setter
    def id( self, value: int ):
        if value is not None:
            self.__transtypesid = value

    @property
    def bfy( self ) -> str:
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value: str ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ) -> str:
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value: str ):
        if value is not None:
            self.__efy = value

    @property
    def fund_code( self ) -> str:
        if self.__fundcode is not None:
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value: str ):
        if value is not None:
            self.__fundcode = value

    @property
    def appropriation( self ) -> str:
        if self.__appropriation is not None:
            return self.__appropriation

    @appropriation.setter
    def appropriation( self, value: str ):
        if value is not None:
            self.__appropriation = value

    @property
    def treasury_symbol( self ) -> str:
        if self.__treasuryaccount is not None:
            return self.__treasuryaccount

    @treasury_symbol.setter
    def treasury_symbol( self, value: str ):
        if value is not None:
            self.__treasuryaccount = value

    @property
    def fields( self ) -> list[ str ]:
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value: list[ str ] ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy: str, fundcode: str, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.TransTypes
        self.__bfy = bfy
        self.__fundcode = fundcode
        self.__fields = [ 'TransTypesId',
                          'FundCode',
                          'Appropriation',
                          'BFY',
                          'EFY',
                          'TreasurySymbol',
                          'DocType',
                          'AppropriationBill',
                          'ContinuingResolution',
                          'RescissionCurrentYear',
                          'RescissionPriorYear',
                          'SequesterReduction',
                          'SequesterReturn' ]

class UnliquidatedObligation( ):
    '''
    Constructor:  UnliquidatedObligation( bfy: str, fund: str, account: str,
                  boc: str, pvdr = Provider.SQLite )

    Purpose: Class defines object providing ULO data'''
    __source = None
    __provider = None
    __unliquidatedobligationsid = None
    __obligationsid = None
    __bfy = None
    __efy = None
    __rpiocode = None
    __rpioname = None
    __fundcode = None
    __fundname = None
    __ahcode = None
    __ahname = None
    __orgcode = None
    __orgname = None
    __accountcode = None
    __programprojectname = None
    __boccode = None
    __bocname = None
    __rccode = None
    __rcname = None
    __documenttype = None
    __documentnumber = None
    __documentcontrolnumber = None
    __referencedocumentnumber = None
    __programprojectcode = None
    __programareacode = None
    __programareaname = None
    __processeddate = None
    __lastactivitydate = None
    __age = None
    __vendorcode = None
    __vendorage = None
    __foccode = None
    __focname = None
    __amount = None
    __goalcode = None
    __goalname = None
    __objectivecode = None
    __objectivename = None
    __npmcode = None
    __npmname = None
    __treasuryaccountcode = None
    __treasuryaccountname = None
    __budgetaccountcode = None
    __budgetaccountname = None
    __fields = None
    __data = None
    __frame = None

    @property
    def id( self ) -> int:
        if self.__expendituresid is not None:
            return self.__expendituresid

    @id.setter
    def id( self, value: int ):
        if value is not None:
            self.__expendituresid = value

    @property
    def bfy( self ) -> str:
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, value: str ):
        if value is not None:
            self.__bfy = value

    @property
    def efy( self ) -> str:
        if self.__efy is not None:
            return self.__efy

    @efy.setter
    def efy( self, value: str ):
        if value is not None:
            self.__efy = value

    @property
    def rpio_code( self ) -> str:
        if self.__rpiocode is not None:
            return self.__rpiocode

    @rpio_code.setter
    def rpio_code( self, value: str ):
        if value is not None:
            self.__rpiocode = value

    @property
    def rpio_name( self ) -> str:
        if self.__rpioname is not None:
            return self.__rpioname

    @rpio_name.setter
    def rpio_name( self, value: str ):
        if value is not None:
            self.__rpioname = value

    @property
    def ah_code( self ) -> str:
        if self.__ahcode is not None:
            return self.__ahcode

    @ah_code.setter
    def ah_code( self, value: str ):
        if value is not None:
            self.__ahcode = value

    @property
    def ah_name( self ) -> str:
        if self.__ahname is not None:
            return self.__ahname

    @ah_name.setter
    def ah_name( self, value: str ):
        if value is not None:
            self.__ahname = value

    @property
    def fund_code( self ) -> str:
        if self.__fundcode is not None:
            return self.__fundcode

    @fund_code.setter
    def fund_code( self, value: str ):
        if value is not None:
            self.__fundcode = value

    @property
    def fund_name( self ) -> str:
        if self.__fundname is not None:
            return self.__fundname

    @fund_name.setter
    def fund_name( self, value: str ):
        if value is not None:
            self.__fundname = value

    @property
    def org_code( self ) -> str:
        if self.__orgcode is not None:
            return self.__orgcode

    @org_code.setter
    def org_code( self, value: str ):
        if value is not None:
            self.__orgcode = value

    @property
    def org_name( self  ):
        if self.__orgname is not None:
            return self.__orgname

    @org_name.setter
    def org_name( self, value  ):
        if value is not None:
            self.__orgname = value

    @property
    def account_code( self ) -> str:
        if self.__accountcode is not None:
            return self.__accountcode

    @account_code.setter
    def account_code( self, value: str ):
        if value is not None:
            self.__accountcode = value

    @property
    def boc_code( self ) -> str:
        if self.__boccode is not None:
            return self.__boccode

    @boc_code.setter
    def boc_code( self, value: str ):
        if value is not None:
            self.__boccode = value

    @property
    def boc_name( self ) -> str:
        if self.__bocname is not None:
            return self.__bocname

    @boc_name.setter
    def boc_name( self, value: str ):
        if value is not None:
            self.__bocname = value

    @property
    def rc_code( self ) -> str:
        if self.__rccode is not None:
            return self.__rccode

    @rc_code.setter
    def rc_code( self, value: str ):
        if value is not None:
            self.__rccode = value

    @property
    def rc_name( self ) -> str:
        if self.__rcname is not None:
            return self.__rcname

    @rc_name.setter
    def rc_name( self, value: str ):
        if value is not None:
            self.__rcname = value

    @property
    def document_type( self ) -> str:
        if self.__documenttype is not None:
            return self.__documenttype

    @document_type.setter
    def document_type( self, value: str ):
        if value is not None:
            self.__documenttype = value

    @property
    def document_number( self ) -> str:
        if self.__documentnumber is not None:
            return self.__documentnumber

    @document_number.setter
    def document_number( self, value: str ):
        if value is not None:
            self.__documentnumber = value

    @property
    def document_control_number( self ) -> str:
        if self.__documentcontrolnumber is not None:
            return self.__documentcontrolnumber

    @document_control_number.setter
    def document_control_number( self, value: str ):
        if value is not None:
            self.__documentcontrolnumber = value

    @property
    def reference_document_number( self ) -> str:
        if self.__referencedocumentnumber is not None:
            return self.__referencedocumentnumber

    @reference_document_number.setter
    def reference_document_number( self, value: str ):
        if value is not None:
            self.__referencedocumentnumber = value

    @property
    def processed_date( self ) -> datetime:
        if self.__processeddate is not None:
            return self.__processeddate

    @processed_date.setter
    def processed_date( self, value: datetime ):
        if isinstance( value, datetime ):
            self.__processeddate = value

    @property
    def last_activity_date( self ) -> datetime:
        if self.__lastactivitydate is not None:
            return self.__lastactivitydate

    @last_activity_date.setter
    def last_activity_date( self, value: datetime ):
        if value is not None:
            self.__lastactivitydate = value

    @property
    def age( self ) -> float:
        if self.__age is not None:
            return self.__age

    @age.setter
    def age( self, value: float ):
        if value is not None:
            self.__age = value

    @property
    def vendor_code( self ) -> str:
        if self.__vendorcode is not None:
            return self.__vendorcode

    @vendor_code.setter
    def vendor_code( self, value: str ):
        if value is not None:
            self.__vendorcode = value

    @property
    def vendor_name( self ) -> str:
        if self.__vendorname is not None:
            return self.__vendorname

    @vendor_name.setter
    def vendor_name( self, value: str ):
        if value is not None:
            self.__vendorname = value

    @property
    def foc_code( self ) -> str:
        if self.__foccode is not None:
            return self.__foccode

    @foc_code.setter
    def foc_code( self, value: str ):
        if value is not None:
            self.__rccode = value

    @property
    def foc_name( self ) -> str:
        if self.__focname is not None:
            return self.__focname

    @foc_name.setter
    def foc_name( self, value: str ):
        if value is not None:
            self.__focname = value

    @property
    def amount( self ) -> float:
        if self.__amount is not None:
            return self.__amount

    @amount.setter
    def amount( self, value: float ):
        if value is not None:
            self.__amount = value

    @property
    def program_project_code( self ) -> str:
        if self.__programprojectcode is not None:
            return self.__programprojectcode

    @program_project_code.setter
    def program_project_code( self, value: str ):
        if value is not None:
            self.__programprojectcode = value

    @property
    def program_project_name( self ) -> str:
        if self.__programprojectname is not None:
            return self.__programprojectname

    @program_project_name.setter
    def program_project_name( self, value: str ):
        if value is not None:
            self.__programprojectname = value

    @property
    def program_area_code( self ) -> str:
        if self.__programareacode is not None:
            return self.__programareacode

    @program_area_code.setter
    def program_area_code( self, value: str ):
        if value is not None:
            self.__programareacode = value

    @property
    def program_area_name( self ) -> str:
        if self.__programareaname is not None:
            return self.__programareaname

    @program_area_name.setter
    def program_area_name( self, value: str ):
        if value is not None:
            self.__programareaname = value

    @property
    def goal_code( self ) -> str:
        if self.__goalcode is not None:
            return self.__goalcode

    @goal_code.setter
    def goal_code( self, value: str ):
        if value is not None:
            self.__goalcode = value

    @property
    def goal_name( self ) -> str:
        if self.__goalname is not None:
            return self.__goalname

    @goal_name.setter
    def goal_name( self, value: str ):
        if value is not None:
            self.__goalname = value

    @property
    def objective_code( self ) -> str:
        if self.__objectivecode is not None:
            return self.__objectivecode

    @objective_code.setter
    def objective_code( self, value: str ):
        if value is not None:
            self.__objectivecode = value

    @property
    def objective_name( self ) -> str:
        if self.__objectivename is not None:
            return self.__objectivename

    @objective_name.setter
    def objective_name( self, value: str ):
        if value is not None:
            self.__objectivename = value

    @property
    def npm_code( self ) -> str:
        if self.__npmcode is not None:
            return self.__npmcode

    @npm_code.setter
    def npm_code( self, value: str ):
        if value is not None:
            self.__npmcode = value

    @property
    def npm_name( self ) -> str:
        if self.__npmname is not None:
            return self.__npmname

    @npm_name.setter
    def npm_name( self, value: str ):
        if value is not None:
            self.__npmname = value

    @property
    def treasury_account_code( self ) -> str:
        if self.__treasuryaccountcode is not None:
            return self.__treasuryaccountcode

    @treasury_account_code.setter
    def treasury_account_code( self, value: str ):
        if value is not None:
            self.__treasuryaccountcode = value

    @property
    def treasury_account_name( self ) -> str:
        if self.__treasuryaccountname is not None:
            return self.__treasuryaccountname

    @treasury_account_name.setter
    def treasury_account_name( self, value: str ):
        if value is not None:
            self.__treasuryaccountname = value

    @property
    def budget_account_code( self ) -> str:
        if self.__budgetaccountcode is not None:
            return self.__budgetaccountcode

    @budget_account_code.setter
    def budget_account_code( self, value: str ):
        if value is not None:
            self.__budgetaccountcode = value

    @property
    def budget_account_name( self ) -> str:
        if self.__budgetaccountname is not None:
            return self.__budgetaccountname

    @budget_account_name.setter
    def budget_account_name( self, value: str ):
        if value is not None:
            self.__budgetaccountname = value

    @property
    def fields( self ) -> list[ str ]:
        if self.__fields is not None:
            return self.__fields

    @fields.setter
    def fields( self, value: list[ str ] ):
        if value is not None:
            self.__fields = value

    def __init__( self, bfy: str, fund: str, account: str,
                  boc: str, provider = Provider.SQLite ):
        self.__provider = provider
        self.__source = Source.UnliquidatedObligations
        self.__bfy = bfy
        self.__fundcode = fund
        self.__accountcode = account
        self.__boccode = boc
        self.__fields = [ 'UnliquidatedObligationsId'
                           'ObligationsId',
                           'BFY',
                           'EFY',
                           'RpioCode',
                           'RpioName',
                           'AhCode',
                           'AhName',
                           'FundCode',
                           'FundName',
                           'OrgCode',
                           'OrgName',
                           'AccountCode',
                           'ProgramProjectCode',
                           'ProgramProjectName',
                           'RcCode',
                           'RcName',
                           'DocumentType',
                           'DocumentNumber',
                           'DocumentControlNumber',
                           'ReferenceDocumentNumber',
                           'ProcessedDate',
                           'LastActivityDate',
                           'Age',
                           'BocCode',
                           'BocName',
                           'FocCode',
                           'FocName',
                           'NpmCode',
                           'NpmName',
                           'VendorCode',
                           'VendorName',
                           'OpenCommitment',
                           'Obligation',
                           'ULO',
                           'Expenditure' ]

    def __str__( self ) -> str:
        if isinstance( self.__amount, float ):
            return str( self.__amount )

    def get_data( self  ) -> list[ Row ]:
        try:
            _source = self.__source
            _provider = self.__provider
            _names = [ 'BFY', 'FundCode', 'AccountCode', 'BocCode' ]
            _values = ( self.__bfy, self.__fundcode, self.__accountcode, self.__boccode)
            _dbconfig = DbConfig( _source, _provider )
            _sqlconfig = SqlConfig( names = _names, values = _values )
            _connection = Connection( self.__source )
            _sql = SqlStatement( _dbconfig, _sqlconfig )
            _sqlite = _connection.connect( )
            _cursor = _sqlite.cursor( )
            _query = _sql.get_query( )
            _db = _cursor.execute( _query )
            self.__data =  [ i for i in _db.fetchall( ) ]
            _cursor.close( )
            _sqlite.close( )
            return self.__data
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Ninja'
            _exc.cause = 'UnliquidatedObligation'
            _exc.method = 'get_data( self )'
            _err = ErrorDialog( _exc )
            _err.show( )

    def get_frame( self ) -> DataFrame:
        '''Method returning pandas dataframe
        comprised of datatable data'''
        try:
            _source = self.__source
            _data = BudgetData( _source )
            return _data.create_frame( )
        except Exception as e:
            _exc = Error( e )
            _exc.module = 'Ninja'
            _exc.cause = 'UnliquidatedObligation'
            _exc.method = 'create_frame( self )'
            _err = ErrorDialog( _exc )
            _err.show( )
