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
     Copyright ©  2024  Terry Eppler

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
from Static import Source, Provider, SQL
from Data import (DbConfig, SqlConfig, Connection, SqlStatement, BudgetData, DataBuilder)

class Account( ):
	'''
    Constructor:
    Account( treas: str, provider: Provider=Provider.SQLite )

    Purpose:
    Class defines object representing Account Codes
    '''
	
	def __init__( self, id: int=None, code: str=None, provider: Provider=Provider.SQLite ):
		self.id = id
		self.code = code
		self.provider = provider
		self.source = Source.Accounts
		self.goalcode = self.code[ 0 ]
		self.objectivecode = self.code[ 1:3 ]
		self.npmcode = self.code[ 3 ]
		self.programprojectcode = self.code[ 4:6 ]
		self.fields = [ 'AccountsId',
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
		if self.code is not None:
			return self.code

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'code', 'name',
		         'goal_code', 'objective_code', 'npm_code',
		         'program_project_code', 'program_project_name',
		         'data', 'fields', 'frame',
		         'copy', 'getdata', 'getframe' ]

	def copy( self ):
		try:
			_clone = Account( code = self.code )
			_clone.goalcode = self.goalcode
			_clone.objectivecode = self.objectivecode
			_clone.npmcode = self.npmcode
			_clone.programprojectcode = self.programprojectcode
			return _clone
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Account'
			_exc.method = 'copy( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getdata( self ) -> list[ Row ]:
		try:
			_source = Source.Accounts
			_provider = Provider.SQLite
			_names = [ 'Code', ]
			_values = ( self.code, )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( _source, _provider )
			_sql = SqlStatement( _connection, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Account'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''

		try:
			_src = self.source
			_data = BudgetData( _src )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Account'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class ActivityCode( ):
	'''

    Constructor:
        ActivityCode( code: str, provider: Provider=Provider.SQLite )

    Purpose:
        Data class representing Activity Codes

    '''

	def __init__( self, code: str, provider: Provider=Provider.SQLite ):
		self.provider = provider
		self.source = Source.ActivityCodes
		self.id = id
		self.code = code
		self.name = None
		self.title = None
		self.fields = [ 'ActivityCodesId',
		                  'Code',
		                  'Name',
		                  'Title' ]

	def __str__( self ) -> str:
		if self.code is not None:
			return self.code

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'code', 'name',
		         'data', 'fields', 'frame',
		         'fields', 'getdata', 'getframe' ]

	def getdata( self ) -> list[ Row ]:
		'''
        Purpose:

        Parameters:

        Returns:
        '''

		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'Code', ]
			_values = ( self.code, )
			_dbcfg = DbConfig( _source, _provider )
			_sqlcfg = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbcfg, _sqlcfg )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.command_text
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Activity'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''
		
        Purpose:

        Parameters:

        Returns:

        '''

		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Activity'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class AdjustedTrialBalance( ):
	'''

	Constructor:
	AdjustedTrialBalances( bfy: str, number: str )

	Purpose:
	Data class representing a record in the ATB

	'''

	def __init__( self, bfy: str, efy: str,
	              fundcode: str, provider: Provider=Provider.SQLite ):
		self.source = Source.AdjustedTrialBalances
		self.provider = provider
		self.bfy = bfy
		self.efy = efy
		self.fundcode = fundcode
		self.fields = [ 'AdjustedTrialBalancesId',
		                  'BFY',
		                  'EFY',
		                  'FundCode',
		                  'FundName',
		                  'TreasurySymbol',
		                  'AccountNumber',
		                  'AccountName',
		                  'MainAccount',
		                  'TreasuryAccountCode',
		                  'TreasuryAccountName',
		                  'BudgetAccountCode',
		                  'BudgetAccountName' ]

	def __str__( self ) -> str:
		if self.accountnumber is not None:
			return self.accountnumber

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'bfy', 'efy', 'fund_code', 'fund_name',
		         'treasury_symbol', 'account_number', 'account_name',
		         'main_account', 'treasury_account_code', 'treasury_account_name',
		         'budget_account_code', 'budget_account_name',
		         'fields', 'data', 'frame',
		         'getdata', 'getframe' ]

	def getdata( self ) -> list[ Row ]:
		'''
        Purpose:

        Parameters:

        Returns:
        '''

		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'EFY', 'FundCode' ]
			_values = ( self.code, )
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'AdjustedTrialBalances'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''

		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'AdjustedTrialBalances'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class AllowanceHolder( ):
	'''

    Constructor:
    AllowanceHolder( code: str, provider: Provider=Provider.SQLite )

    Purpose:
    Data class representing Allowance Holders

    '''

	def __init__( self, code: str=None,
	              provider: Provider=Provider.SQLite ):
		self.provider = provider
		self.source = Source.AllowanceHolders
		self.code = code
		self.fields = [ 'AllowanceHoldersId',
		                  'Code',
		                  'Name'
		                  'Status'
		                  'EarmarkFlag' ]

	def __str__( self ) -> str:
		if self.code is not None:
			return self.code

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'code', 'name',
		         'status', 'earmark_flag', 'usage',
		         'fields', 'data', 'frame',
		         'getdata', 'getframe' ]

	def getdata( self ) -> list[ Row ]:
		'''
        Purpose:

        Parameters:

        Returns:
        	
        '''

		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'AllowanceHoldersId', 'Code', 'Name', ]
			_values = ( self.code, )
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'AllowanceHolder'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''

		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'AllowanceHolder'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class AmericanRescuePlanCarryoverEstimate( ):
	'''

    Constructor:
    CarryoverEstimate( bfy: str, pvdr = Provider.SQLite )

    Purpose:
    Class representing estimates for ARP carryover

    '''

	def __init__( self, bfy: str, provider: Provider=Provider.SQLite ):
		self.provider = provider
		self.source = Source.AmericanRescuePlanCarryoverEstimates
		self.bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
		self.fields = [ 'CarryoverEstimatesId',
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
		                  'OpenCommitments',
		                  'UnobligatedAuthority' ]

	def __str__( self ) -> str:
		if self.fundcode is not None:
			return self.fundcode

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'bfy', 'efy',
		         'rpio_code', 'rpio_name', 'fund_code', 'fund_name',
		         'amount', 'available', 'open_commitments', 'obligations',
		         'main_account', 'treasury_account_code', 'treasury_account_name',
		         'budget_account_code', 'budget_account_name', 'estimate',
		         'fields', 'data', 'frame',
		         'getdata', 'getframe' ]

	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'EFY' ]
			_values = ( self.bfy, self.efy)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Reporting'
			_exc.cause = 'CarryoverEstimate'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''

		try:
			_data = BudgetData( self.source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Reporting'
			_exc.cause = 'CarryoverEstimate'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class AnnualCarryoverEstimate( ):
	'''
    Constructor:
    AnnualCarryoverEstimate( bfy: str, provider: Provider=Provider.SQLite )

    Purpose:
    Class providing Carryover Estimate data for
    '''

	def __init__( self, bfy: str, provider: Provider=Provider.SQLite ):
		self.provider = provider
		self.source = Source.AnnualCarryoverEstimates
		self.bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
		self.frame = DataFrame( )
		self.fields = [ 'CarryoverEstimatesId',
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
		                  'OpenCommitments',
		                  'UnobligatedAuthority' ]

	def __str__( self ) -> str:
		if self.fundcode is not None:
			return self.fundcode

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'bfy', 'efy', 'fund_code', 'fund_name',
		         'rpio_code', 'rpio_name', 'amount',
		         'available', 'open_commitments', 'obligations',
		         'main_account', 'treasury_account_code', 'treasury_account_name',
		         'budget_account_code', 'budget_account_name',
		         'fields', 'data', 'frame',
		         'getdata', 'getframe' ]

	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'EFY' ]
			_values = ( self.bfy, self.efy)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Reporting'
			_exc.cause = 'CarryoverEstimate'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''

		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Reporting'
			_exc.cause = 'CarryoverEstimate'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class AnnualReimbursableEstimate( ):
	'''
    Constructor:
    AnnualReimbursableEstimate( bfy: str, provider: Provider=Provider.SQLite )

    Purpose:
    Class defining object representing reimbursable estimates'''
	
	def __init__( self, bfy: str, provider: Provider=Provider.SQLite ):
		self.provider = provider
		self.source = Source.AnnualReimbursableEstimates
		self.bfy = bfy
		self.fields = [ 'AnnualReimbursableEstimatesId',
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
		                  'OpenCommitments',
		                  'UnobligatedAuthority' ]

	def __str__( self ) -> str:
		if self.fundcode is not None:
			return self.fundcode

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'bfy', 'efy', 'fund_code', 'fund_name',
		         'rpio_code', 'rpio_name', 'amount', 'estimate',
		         'available', 'open_commitments', 'obligations',
		         'main_account', 'treasury_account_code', 'treasury_account_name',
		         'budget_account_code', 'budget_account_name',
		         'fields', 'data', 'frame',
		         'getdata', 'getframe' ]

	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'EFY' ]
			_values = ( self.bfy, self.efy)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Reporting'
			_exc.cause = 'CarryoverEstimate'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''

		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Reporting'
			_exc.cause = 'CarryoverEstimate'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class Appropriation( ):
	'''
    Constructor:
    Appropriation( fund: str, provider: Provider=Provider.SQLite )

    Purpose:
    Data class representing Appropriations
    '''

	def __init__( self, code: str ):
		self.source = Source.Appropriations
		self.provider = Provider.SQLite
		self.code = code
		self.fields = [ 'AppropriationsId',
		                  'Code',
		                  'Name' ]

	def __str__( self ) -> str:
		if self.code is not None:
			return self.code

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'data', 'fields',
		         'code', 'name',
		         'getdata', 'getframe']

	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'Code' ]
			_values = ( self.code, )
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Appropriation'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''

		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Appropriation'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class AppropriationAvailableBalance( ):
	'''
    Constructor:
    AppropriationAvailableBalance( bfy: str, efy: str, fund: str )

    Purpose:
    Data class representing Appropriation-level balances
    '''
	
	def __init__( self, bfy: str, efy: str, fundcode: str ):
		self.source = Source.Appropriations
		self.provider = Provider.SQLite
		self.bfy = bfy
		self.efy = efy
		self.fundcode = fundcode
		self.fields = [ 'AppropriationAvailableBalancesId',
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
		                  'TotalAvailable' ]

	def __str__( self ) -> str:
		if self.fundcode is not None:
			return self.fundcode

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'bfy', 'efy', 'fund_code', 'fund_name', 'authority',
		         'budgeted', 'reimbursements', 'recoveries', 'used', 'available',
		         'main_account', 'treasury_account_code', 'treasury_account_name',
		         'budget_account_code', 'budget_account_name',
		         'data', 'fields', 'frame',
		         'getdata', 'getframe']

	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'Code' ]
			_values = ( self.fundcode,)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Appropriation'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''

		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Appropriation'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class AppropriationLevelAuthority( ):
	'''
    Constructor:
    AppropriationLevelAuthority( bfy: str, efy: str, fund: str )

    Purpose:
    Data class representing Appropriation-level authority
    '''

	def __init__( self, bfy: str, efy: str, fundcode: str ):
		self.source = Source.AppropriationLevelAuthority
		self.provider = Provider.SQLite
		self.bfy = bfy
		self.efy = efy
		self.fundcode = fundcode
		self.fields = [ 'AppropriationLevelAuthorityId',
		                  'BFY',
		                  'EFY',
		                  'FundCode',
		                  'FundName',
		                  'MainAccount',
		                  'Authority',
		                  'Budgeted',
		                  'Reimbursements',
		                  'Recoveries',
		                  'MainAccount',
		                  'TreasuryAccountCode',
		                  'TreasuryAccountName',
		                  'BudgetAccountCode',
		                  'BudgetAccountName' ]

	def __str__( self ) -> str:
		if isinstance( self.fundcode, str ) and self.fundcode != '':
			return self.fundcode

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'bfy', 'efy', 'fund_code', 'fund_name', 'authority',
		         'budgeted', 'reimbursements', 'recoveries', 'used', 'available',
		         'main_account', 'treasury_account_code', 'treasury_account_name',
		         'budget_account_code', 'budget_account_name',
		         'data', 'fields', 'frame',
		         'getdata', 'getframe']

	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'Code' ]
			_values = tuple( self.fundcode, )
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Appropriation'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''

		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Appropriation'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class Allocation( ):
	'''
    Constructor:
    Allocation( bfy = None, fund = None, provider: Provider=Provider.SQLite )

    Purpose:
    Class defining object representing Allocations

    '''

	def __init__( self, bfy: str, efy: str, fundcode: str,
	              provider: Provider=Provider.SQLite ):
		self.source = Source.Allocations
		self.provider = provider
		self.bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
		self.fundcode = fund if isinstance( fund, str ) and fund != '' else None
		self.fields = [ 'AllocationsId',
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
		                  'NpmName',
		                  'MainAccount',
		                  'TreasuryAccountCode',
		                  'TreasuryAccountName',
		                  'BudgetAccountCode',
		                  'BudgetAccountName' ]

	def __str__( self ) -> str:
		if self.programprojectname is not None:
			return self.programprojectname

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'bfy', 'efy', 'fund_code', 'fund_name', 
		         'rpio_code', 'rpio_name', 'ah_code', 'ah_name',
		         'org_code', 'org_name', 'boc_code', 'boc_name',
		         'rc_code', 'rc_name', 'npm_code', 'npm_name',
		         'program_project_code', 'program_project_name', 'program_area_code',
		         'program_area_name',  'goal_code', 'goal_name',
		         'account_code', 'objective_code', 'objective_name', 'authority',
		         'budgeted', 'reimbursements', 'recoveries', 'used', 'available',
		         'main_account', 'treasury_account_code', 'treasury_account_name',
		         'budget_account_code', 'budget_account_name',
		         'data', 'fields', 'frame',
		         'getdata', 'getframe' ]

	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'EFY', 'FundCode' ]
			_values = ( self.bfy, self.fundcode )
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Allocations'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''

		Purpose: Method returning pandas dataframe
        comprised of datatable data

        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Allocations'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class ApportionmentData( ):
	'''
    Constructor:
    ApportionmentData( bfy: str, efy: str, main: str,
                       provider: Provider=Provider.SQLite )

    Purpose:
    Data class representing Letters Of Apportionment
    '''

	def __init__( self, year: str, bfy: str, efy: str,
	              main: str, provider: Provider=Provider.SQLite ):
		self.provider = provider
		self.source = Source.ApportionmentData
		self.fiscalyear = year
		self.bfy = bfy
		self.efy = efy
		self.mainaccount = main
		self.fields = [ 'ApportionmentDataId',
		                  'FiscalYear',
		                  'BFY',
		                  'EFY',
		                  'AvailabilityType',
		                  'MainAccount',
		                  'TreasuryAccountCode',
		                  'TreasuryAccountName',
		                  'BudgetAccountCode',
		                  'BudgetAccountName',
		                  'ApprovalDate',
		                  'LineNumber',
		                  'LineSplit',
		                  'LineName',
		                  'Amount',
		                  'FundCode',
		                  'FundName' ]

	def __str__( self ) -> str:
		if self.mainaccount is not None:
			return self.mainaccount

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'fiscal_year', 'bfy', 'efy', 'availability_type',
		         'approval_date', 'line_number', 'line_split', 'line_name',
		         'amount', 'fund_code', 'fund_name',
		         'main_account', 'treasury_account_code', 'treasury_account_name',
		         'budget_account_code', 'budget_account_name',
		         'fields', 'data', 'frame', 'getdata', 'getframe' ]

	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'EFY', 'OmbAccountCode', ]
			_values = ( self.bfy, self.efy, self.budgetaccountcode )
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Reporting'
			_exc.cause = 'Apportionment'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''

		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Reporting'
			_exc.cause = 'Apportionment'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class Actual( ):
	'''
    Constructor:
    Actual( bfy, fund, pvdr = Provider.SQLite  )

    Purpose:
    Object representing expenditure data
    '''

	def __init__( self, bfy: str, fund: str, provider: Provider=Provider.SQLite ):
		self.provider = provider
		self.source = Source.Actuals
		self.bfy = bfy
		self.fundcode = fund
		self.fields = [ 'ActualsId',
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
		                  'UnliquidatedObligations',
		                  'Obligations',
		                  'Balance',
		                  'ProgramAreaCode',
		                  'ProgramAreaName',
		                  'GoalCode',
		                  'GoalName',
		                  'ObjectiveCode',
		                  'ObjectiveName',
		                  'MainAccount',
		                  'TreasuryAccountCode',
		                  'TreasuryAccountName',
		                  'BudgetAccountCode',
		                  'BudgetAccountName' ]

	def __str__( self ) -> str:
		if self.programprojectname is not None:
			return self.programprojectname

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'bfy', 'efy', 'fund_code', 'fund_name',
		         'appropriation_code', 'appropriation_name', 'subappropriation_code',
		         'subappropriation_name', 'rpio_code', 'rpio_name',
		         'ah_code', 'ah_name', 'org_code', 'org_name', 'account_code',
		         'boc_code', 'boc_name', 'rc_code', 'rc_name',
		         'program_project_code', 'program_project_name', 'program_area_code',
		         'program_area_name', 'npm_code', 'npm_name', 'goal_code', 'goal_name',
		         'objective_code', 'objective_name', 'balance',
		         'obligations', 'unliquidated_obligations',
		         'main_account', 'treasury_account_code', 'treasury_account_name',
		         'budget_account_code', 'budget_account_name',
		         'data', 'fields', 'frame',
		         'getdata', 'getframe' ]

	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'FundCode' ]
			_values = ( self.bfy, self.fundcode )
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Actual'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''Method returning pandas dataframe
        comprised of datatable data'''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Actual'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class ApplicationTable( ):
	'''
    Constructor:
    ApplicationTable( name, pvdr = Provider.SQLite )

    Purpose:
    Class defines object that represents all the tables
    '''

	def __init__( self, name: str, provider: Provider=Provider.SQLite ):
		self.source = Source.ApplicationTables
		self.provider = provider
		self.name = name
		self.fields = [ 'ApplicationTablesId',
		                  'Name',
		                  'Model',
		                  'Caption' ]

	def __str__( self ) -> str:
		if self.name is not None:
			return self.name

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'name', 'model',
		         'caption', 'fields', 'data',
		         'frame', 'getdata', 'getframe' ]

	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'Name', ]
			_values = ( self.bfy, self.fundcode )
			_dbconfig = DbConfig( self.source, self.provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'ApplicationTables'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''

        Purpose: Method returning pandas dataframe
        comprised of datatable data

        Parameters:

        Returns:

        	'''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'ApplicationTables'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class AppropriationDocument( ):
	'''
    Constructor:
    AppropriationDocument( bfy, fund, pvdr = Provider.SQLite )

    Purpose:
    Class defines object representing Level 1 documents
    '''

	def __init__( self, bfy: str, efy: str, fund: str, provider: Provider=Provider.SQLite ):
		self.provider = provider
		self.source = Source.AppropriationDocuments
		self.bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
		self.fundcode = fund if isinstance( fund, str ) and fund != '' else None
		self.fields = [ 'AppropriationDocumentsId',
		                  'BFY',
		                  'EFY',
		                  'Fund',
		                  'Appropriation',
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
		                  'CarryoverOut',
		                  'CarryoverIn',
		                  'EstimatedReimbursements',
		                  'EstimatedRecoveries',
		                  'MainAccount',
		                  'TreasuryAccountCode',
		                  'TreasuryAccountName',
		                  'BudgetAccountCode',
		                  'BudgetAccountName' ]

	def __str__( self ):
		if self.fundcode is not None:
			return self.fundcode

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'bfy', 'efy', 'fund_code', 'appropriation',
		         'budget_level', 'document_type', 'document_number', 'document_date',
		         'last_document_date', 'budgeting_controls', 'posting_controls',
		         'precommitment_controls', 'commitment_controls', 'obligation_controls',
		         'accrual_controls', 'expenditure_controls', 'expense_controls',
		         'reimbursement_controls', 'reimbursement_controls',
		         'reimbursable_agreement_controls', 'budgeted', 'posted',
		         'carryover_in', 'carryover_out',
		         'estimated_reimbursments', 'estimated_recoveries',
		         'main_account', 'treasury_account_code', 'treasury_account_name',
		         'budget_account_code', 'budget_account_name',
		         'fields', 'data', 'frame', 'getdata', 'getframe' ]

	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'FundCode' ]
			_values = ( self.bfy, self.fundcode )
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'AppropriationDocument'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''

		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'AppropriationDocument'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class BudgetDocument( ):
	'''
    Constructor:
    BudgetDocument( bfy, fund, pvdr = Provider.SQLite )

    Purpose:
    Class defines object representing Level 2-3 documents
    '''

	def __init__( self, bfy: str, efy: str,fundcode: str,
	              provider: Provider=Provider.SQLite ):
		self.provider = provider
		self.source = Source.BudgetDocuments
		self.bfy = bfy
		self.efy = efy
		self.fundcode = fundcode
		self.fields = [ 'BudgetDocumentsId',
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
		                  'CarryoverOut',
		                  'CarryoverIn',
		                  'EstimatedRecoveries',
		                  'EstimatedReimbursements',
		                  'MainAccount',
		                  'TreasuryAccountCode',
		                  'TreasuryAccountName',
		                  'BudgetAccountCode',
		                  'BudgetAccountName' ]

	def __str__( self ) -> str:
		if self.documentnumber is not None:
			return self.documentnumber

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'bfy', 'efy', 'budget_level', 'document_date',
		         'last_document_date', 'document_type','document_number', 'fund_code',
		         'fund_name', 'rpio_code', 'rpio_name', 'ah_code', 'ah_name',
		         'org_code', 'org_name', 'account_code', 'program_project_pame',
		         'program_area_code', 'program_area_name', 'boc_code', 'boc_name',
		         'reimbursable_agreement_controls', 'budgeting_controls', 'posting_controls',
		         'precommitment_controls', 'commitment_controls', 'obligation_controls',
		         'expenditure_controls', 'expense_controls', 'accrual_controls',
		         'reimbursement_controls', 'budgeted', 'posted', 'carryover_out',
		         'carryover_in', 'estimated_recoveries', 'estimated_reimbursements',
		         'main_account', 'treasury_account_code',  'treasury_account_name',
		         'budget_account_code',  'budget_account_name' ]

	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'EFY', 'FundCode' ]
			_values = ( self.bfy, self.efy, self.fundcode )
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'BudgetDocument'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'BudgetDocument'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class BudgetContact( ):
	'''
    Constructor:
    BudgetContact( last: str, first: str )

    Purpose:
    Class defines object represent budget contact info
    '''

	def __init__( self, last: str, first: str, provider: Provider=Provider.SQLite ):
		self.lastname = last
		self.__first = first
		self.fields = [ 'BudgetContactsId',
		                  'FirstName',
		                  'LastName',
		                  'RpioCode',
		                  'RpioName',
		                  'Section',
		                  'JobTitle',
		                  'City',
		                  'State',
		                  'ZipCode',
		                  'OfficeLocation',
		                  'Account',
		                  'EmailAddress',
		                  'EmailType',
		                  'DisplayName' ]

	def __str__( self ) ->str:
		if self.emailaddress is not None:
			return self.emailaddress

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'first_name', 'last_name', 'rpio_code', 'rpio_name',
		         'section', 'job_title', 'state', 'zip_code', 'office_location',
		         'city', 'account', 'email_type', 'display_name',
		         'fields', 'data', 'frame', 'getdata', 'getframe' ]

	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'EFY' ]
			_values = ( self.bfy, self.efy)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'BudgetContacts'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'BudgetContacts'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class BudgetControl( ):
	'''
    Constructor:  BudgetControl( fund, pvdr = Provider.SQLite )

    Purpose;  Class defines object representing compass control data'''
	

	def __init__( self, bfy: str, efy: str,
	              fund: str, provider: Provider=Provider.SQLite ):
		self.provider = provider
		self.source = Source.BudgetControls
		self.bfy = bfy
		self.efy = efy
		self.fundcode = fund
		self.fields = [ 'BudgetControlValuesId',
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
		                  'ProfitLossTransType',
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

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'code', 'name', 'security_org', 'posted_trans_type',
		         'estimated_reimbursements_transtype', 'spending_adjustment_transtype',
		         'estimated_recoveries_transtype', 'actual_recoveries_transtype',
		         'strategic_reserve_transtype',  'profit_loss_transtype',
		         'estimated_reimbursements_spending_option',
		         'estimated_reimbursable_budgeting_option',
		         'track_agreement_lower_level', 'budget_estimate_lower_level',
		         'estimated_recoveries_spending_option', 'estimated_recoveries_budgeting_option',
		         'record_next_level', 'record_budgeting_mismatch', 'profitloss_spending_option',
		         'profitloss_budgeting_option', 'record_carryoverin_lowerlevel',
		         'RecordCarryInLowerLevelControl', 'record_carryin_amount_control',
		         'BudgetingControl', 'PostingControl', 'PreCommitmentSpendingControl',
		         'CommitmentSpendingControl', 'ObligationSpendingControl',
		         'accrual_spending_control', 'expenditure_spending_control',
		         'expense_spending_control', 'reimbursable_spending_control',
		         'reimbursable_agreement_spending_control', 'fte_budgeting_control',
		         'fte_spending_control', 'transaction_type_control',
		         'authority_distribution_control'
		         'fields', 'data', 'frame', 'getdata', 'getframe' ]

	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'EFY', 'FundCode' ]
			_values = ( self.bfy, self.efy, self.fundcode )
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'BudgetControl'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''Method returning pandas dataframe
        comprised of datatable data'''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'BudgetControl'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class BudgetFiscalYear( ):
	'''
    Constructor:
    BudgetFiscalYear( bfy, efy, date = None, pvdr = Provider.SQLite ).


    Purpose:
    Class to describe the federal fiscal year
    '''
	

	def __init__( self, bfy: str, efy: str,
	              dt: datetime=None, provider: Provider=Provider.SQLite ):
		self.provider = provider
		self.source = Source.FiscalYears
		self.bfy = bfy
		self.efy = efy
		self.today = datetime.today( )
		self.currentday = datetime.today( ).day
		self.currentmonth = datetime.today( ).month
		self.date = dt if dt is not None else datetime.today( )
		self.currentyear = datetime.today( ).year
		self.startdate = datetime( datetime.today( ).year, 10, 1 )
		self.enddate = datetime( datetime.today( ).year + 1, 9, 30 )
		self.holidays = [ 'ColumbusDay', 'VeteransDay', 'ThanksgivingDay', 'ChristmasDay',
		                    'NewYearsDay', 'MartinLutherKingDay', 'PresidentsDay',
		                    'MemorialDay', 'JuneteenthDay', 'IndependenceDay', 'LaborDay' ]
		self.fields = [ 'FiscalYearsId',
		                  'BFY',
		                  'EFY',
		                  'StartDate',
		                  'EndDate',
		                  'ColumbusDay',
		                  'VeteransDay',
		                  'ThanksgivingDay',
		                  'ChristmasDay',
		                  'NewYearsDay',
		                  'MartinLutherKingsDay',
		                  'PresidentsDay',
		                  'MemorialDay',
		                  'JuneteenthDay',
		                  'IndependenceDay',
		                  'LaborDay',
		                  'ExpiringYear',
		                  'ExpirationDate',
		                  'CancellationDate',
		                  'Workdays',
		                  'Weekdays',
		                  'Weekends',
		                  'Availability' ]

	def __str__( self ) -> str:
		if self.bfy is not None:
			return self.bfy

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'first_year', 'last_year', 'weekdays', 'weekends',
		         'today', 'date', 'current_day', 'current_month', 'current_year',
		         'start_date', 'end_date', 'holidays', 'expiring_year', 'expiration_date',
				 'id', 'fields', 'data', 'frame', 'getdata', 'getframe' ]

	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'EFY' ]
			_values = ( self.bfy, self.efy)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'BudgetFiscalYear'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'BudgetFiscalYear'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class BudgetObjectClass( ):
	'''
    Constructor:
    BudgetObjectClass( code, pvdr = Provider.SQLite  ).

    Purpose:
    Defines the BudgetObjectClass Class
    '''
	

	def __init__( self, code: str, provider: Provider=Provider.SQLite ):
		self.provider = provider
		self.source = Source.BudgetObjectClasses
		self.code = code
		self.fields = [ 'BudgetObjectClassesId',
		                  'Code',
		                  'Name' ]

	def __str__( self ) -> str:
		if self.code is not None:
			return self.code

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'fields', 'data',
		         'frame', 'getdata', 'getframe' ]

	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'Code', ]
			_values = ( self.code, )
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'BudgetObjectClass'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'BudgetObjectClass'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class BudgetaryResourceExecution( ):
	'''
    Constructor:
    BudgetaryResourceExecution( bfy: str, efy: str,
                                main: str, provider: Provider=Provider.SQLite )

    Purpose:
    Class defines object representing the MAX A-11 DE/SF-133
    Status Of Budgetary Resources Execution Report
    '''


	def __init__( self, bfy: str, efy: str,
	              main: str, provider: Provider=Provider.SQLite ):
		self.provider = provider
		self.source = Source.BudgetaryResourceExecution
		self.bfy = bfy
		self.efy = efy
		self.budgetaccountcode = main
		self.fields = [ 'BudgetaryResourceExecutionId',
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

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'bfy', 'efy',
		         'main_account', 'treasury_account_code', 'treasury_account_name',
		         'budget_account_code', 'budget_account_name',
		         'fields', 'data', 'frame',
		         'getdata', 'getframe' ]

	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'EFY', 'OmbAccountCode', ]
			_values = ( self.bfy, self.efy, self.budgetaccountcode )
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Reporting'
			_exc.cause = 'BudgetaryResourceExecution'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Reporting'
			_exc.cause = 'BudgetaryResourceExecution'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class CongressionalControl( ):
	'''
    Constructor:
    CongressionalControl( bfy, fund, pvdr = Provider.SQLite )

    Purpose:
    Class defining object representing congressional control data
    '''
	

	def __init__( self, bfy: str=None, fundcode: str=None,
	              provider: Provider=Provider.SQLite ):
		self.provider = provider
		self.source = Source.CongressionalControls
		self.bfy = bfy
		self.fundcode = fundcode
		self.fields = [ 'CongressionalControlsId',
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

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'bfy', 'efy', 'fund_code', 'fund_name',
		         'program_project_code', 'program_project_name', 'program_area_code',
		         'program_area_name',  'sub_project_code', 'sub_project_name',
		         'reprogramming_restriction', 'increase_restriction', 'decrease_restiction',
		         'memorandum_required', 'data', 'fields', 'frame',
		         'getdata', 'getframe' ]

	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'Code', ]
			_values = ( self.code, )
			_dbcfg = DbConfig( _source, _provider )
			_sqlcfg = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbcfg, _sqlcfg )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.command_text
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'CongressionalControls'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''

        Purpose:

        Parameters:

        Returns:

        '''

		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'CongressionalControls'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class CongressionalProject( ):
	'''
	Constructor:
	CongressionalProjects( bfy: str, fund: str, rpio: str, ahcode: str )

	Purpose:
	Class used to allocated Earmarks
	'''
	

	def __init__( self, bfy: str, fund: str, 
	              rpio: str, ahcode: str, provider: Provider=Provider.SQLite ):
		self.source = Source.CongressionalProjects
		self.provider = provider
		self.bfy = bfy
		self.fundcode = fund
		self.rpiocode = rpio
		self.ahcode = ahcode

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'bfy', 'efy',
		         'fund_code', 'ah_code', 'amount'
		         'fields', 'data', 'frame', 'getdata', 'getframe' ]

	def getdata( self ) -> list[ Row ]:
		'''
        Purpose:

        Parameters:

        Returns:
        '''

		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'Code', ]
			_values = ( self.code, )
			_dbcfg = DbConfig( _source, _provider )
			_sqlcfg = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbcfg, _sqlcfg )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.command_text
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'CongressionalProjects'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''

        Purpose:

        Parameters:

        Returns:

        '''

		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'CongressionalProjects'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class CompassLevel( ):
	'''
    Constructor:
    CompassLevel( bfy: str, efy: str,
                  fund: str, provider: Provider=Provider.SQLite )

    Purpose:
    Class defines object representing Compass data levels 1-7
    '''

	def __init__( self, bfy: str, efy: str,
	              fund: str, provider: Provider=Provider.SQLite ):
		self.provider = provider
		self.source = Source.CompassLevels
		self.bfy = bfy
		self.efy = efy
		self.fundcode = fund
		self.fields = [ 'CompassLevelsId',
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
		                  'AgreementReimbursables',
		                  'MainAccount',
		                  'TreasuryAccountCode',
		                  'TreasuryAccountName',
		                  'BudgetAccountCode',
		                  'BudgetAccountName' ]

	def __str__( self ) -> str:
		if self.documenttype is not None:
			return self.documenttype

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members
		'''
		return [ 'id', 'bfy', 'efy', 'fund_code', 'appropriation',
				 'subappropriation_code', 'main_account', 'treasury_account_code',
				 'treasury_account_name', 'budget_account_code', 'budget_account_name',
		         'fields', 'data', 'frame', 'getdata', 'getframe' ]

	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'EFY', 'FundCode' ]
			_values = ( self.bfy, self.efy, self.fundcode )
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'CompassLevel'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'CompassLevel'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class Commitment( ):
	'''
    Constructor:
    Commitment( bfy: str=None, fund: str=None,
                account: str=None, boc: str=None, provider: Provider=Provider.SQLite )

    Purpose:
    Defines the CommitmentS class.
    '''
	

	def __init__( self, bfy: str, efy: str,  fund: str=None, account: str=None,
	              boc: str=None, provider: Provider=Provider.SQLite ):
		self.provider = provider
		self.source = Source.OpenCommitments
		self.bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
		self.fundcode = fund if isinstance( fund, str ) and fund != '' else None
		self.accountcode = account if isinstance( account, str ) and account != '' else None
		self.boccode = boc if isinstance( boc, str ) and boc != '' else None
		self.fields = [ 'CommitmentsId',
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
		                  'OpenCommitments',
		                  'Obligations',
		                  'UnliquidatedObligations',
		                  'Expenditures' ]

	def __str__( self ) -> str:
		if isinstance( self.amount, float ):
			return str( self.amount )

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'bfy', 'efy', 'fund_code', 'fund_name', 'rpio_code', 'rpio_name',
		         'ah_code', 'ah_name', 'org_code', 'org_name', 'account_code',
		         'boc_code', 'boc_name', 'rc_code', 'rc_name',
		         'program_project_code', 'program_project_name', 'program_area_code',
		         'program_area_name', 'npm_code', 'npm_name', 'goal_code', 'goal_name',
		         'objective_code', 'objective_name', 'document_type',
		         'document_number', 'document_control_number', 'rerference_document_number',
		         'last_activity_date', 'processed_date', 'age', 'vendor_code', 'vendor_name',
		         'foc_code', 'foc_name', 'amount',
		         'main_account', 'treasury_account_code', 'treasury_account_name',
		         'budget_account_code', 'budget_account_name',
		         'data', 'fields',
		         'getdata', 'getframe' ]

	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'FundCode', 'AccountCode', 'BocCode' ]
			_values = ( self.bfy, self.fundcode, self.accountcode, self.boccode )
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Commitment'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Commitment'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class CostArea( ):
	'''
    Constructor:
    CostArea( fund, pvdr = Provider.SQLite )

    Purpose:
    Data class object for cost areas
    '''


	def __init__( self, code: str, provider: Provider=Provider.SQLite ):
		self.code = code
		self.provider = provider
		self.fields = [ 'CostAreasId',
		                  'Code',
		                  'Name' ]

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'fields', 'data', 'frame', 'getdata', 'getframe' ]

	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'Code', ]
			_values = ( self.code, )
			_dbcfg = DbConfig( _source, _provider )
			_sqlcfg = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbcfg, _sqlcfg )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.command_text
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'CostAreas'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''

        Purpose:

        Parameters:

        Returns:

        '''

		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'CostAreas'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class CapitalPlanningInvestmentCode( ):
	'''
    Constructor:
    CapitalPlanningInvestmentCodes( treas, pvdr = Provider.SQLite  )

    Purpose:
    Class eefines the CPIC Codes'''
	
	def __init__( self, code: str, provider: Provider=Provider.SQLite ):
		self.provider = provider
		self.source = Source.CapitalPlanningInvestmentCodes
		self.code = code
		self.fields = [ 'CpicId',
		                  'Type'
		                  'Code',
		                  'Name' ]

	def __str__( self ) -> str:
		if isinstance( self.code, str ) and self.code != '':
			return self.code

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'fields', 'data', 'frame', 'getdata', 'getframe' ]

	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'Code', ]
			_values = ( self.code, )
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'ITProjectCode'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'ITProjectCode'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class ColumnSchema( ):
	'''
    Constructor:
    ColumnSchema( column, table_name, pvdr = Provider.SQLite )

    Purpose:
    Provides data on the coolumn_names used in the application
    '''
	

	def __init__( self, column: str, table: str, provider: Provider=Provider.SQLite ):
		self.source = Source.ColumnSchema
		self.provider = provider
		self.columnname = column
		self.tablename = table

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'fields', 'data', 'frame', 'getdata', 'getframe' ]

	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'Code', ]
			_values = ( self.code, )
			_dbcfg = DbConfig( _source, _provider )
			_sqlcfg = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbcfg, _sqlcfg )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.command_text
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'ColumnSchema'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''

        Purpose:

        Parameters:

        Returns:

        '''

		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'ColumnSchema'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class DataRuleDescription( ):
	'''
    Constructor:
    DataRuleDescription( schedule, line, rule, pvdr = Provider.SQLite )

    Purpose:
    Class defines object providing OMB MAX A11 rule data '''
	

	def __init__( self, schedule: str, line: str,
	              rule: str, provider: Provider=Provider.SQLite ):
		self.provider = provider
		self.source = Source.DataRuleDescriptions
		self.schedule = schedule
		self.linenumber = line
		self.rulenumber = rule
		self.fields = [ 'DataRuleDescriptionsId',
		                  'Schedule',
		                  'LineNumber',
		                  'RuleNumber',
		                  'RuleDescription',
		                  'ScheduleOrder' ]

	def __str__( self ) -> str:
		if self.ruledescription is not None:
			return self.ruledescription

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'fields', 'data', 'frame', 'getdata', 'getframe' ]

	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'Schedule', 'LineNumber', 'RuleNumber' ]
			_values = ( self.schedule, self.linenumber, self.rulenumber)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Reporting'
			_exc.cause = 'DataRuleDescription'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Reporting'
			_exc.cause = 'DataRuleDescription'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class Defacto( ):
	'''
    Constructor:
    Defacto(  bfy: str, fund: str, provider: Provider=Provider.SQLite )

    Purpose:
    Class defines object representing defacto obligations
    '''


	def __init__( self, bfy: str, fund: str, provider: Provider=Provider.SQLite ):
		self.source = Source.Defactos
		self.provider = provider
		self.bfy = bfy
		self.fundcode = fund
		self.fields = [ 'DefactosId',
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
		                  'OpenCommitments',
		                  'UnliquidatedObligations',
		                  'Expenditure',
		                  'Obligations',
		                  'Used',
		                  'Available',
		                  'NpmCode',
		                  'NpmName' ]

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'fields', 'data', 'frame', 'getdata', 'getframe' ]

	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'FundCode' ]
			_values = ( self.bfy, self.fundcode )
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Defacto'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Defacto'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class Deobligation( ):
	'''
    Constructor:
    Deobligation( bfy, fund, account, boc, pvdr = Provider.SQLite )

    Purpose:
    Class defines object providing Deobligation data
    '''


	def __init__( self, bfy = None, fund = None,
	              account = None, boc = None, provider: Provider=Provider.SQLite ):
		self.provider = provider
		self.source = Source.Deobligations
		self.bfy = bfy
		self.fundcode = fund
		self.accountcode = account
		self.boccode = boc
		self.fields = [ 'DeobligationsId',
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
		if isinstance( self.amount, float ):
			return str( self.amount )

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'fields', 'data', 'frame', 'getdata', 'getframe' ]

	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'FundCode', 'AccountCode', 'BocCode' ]
			_values = ( self.bfy, self.fundcode, self.accountcode, self.boccode )
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Deobligations'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Deobligations'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class DocumentControlNumber( ):
	'''
    Constructor:
    DocumentControlNumber( dcn, pvdr = Provider.SQLite )

    Purpose:
    Class defines object provides DCN data
    '''


	def __init__( self, dcn: str, provider: Provider=Provider.SQLite ):
		self.provider = provider
		self.source = Source.DocumentControlNumbers
		self.documentcontrolnumber = dcn
		self.fields = [ 'DocumentControlNumbersId',
		                  'RpioCode',
		                  'RpioName',
		                  'DocumentType',
		                  'DocumentNumber',
		                  'DocumentPrefix',
		                  'DocumentControlNumbe' ]

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'fields', 'data', 'frame', 'getdata', 'getframe' ]

	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'DocumentControlNumber', ]
			_values = ( self.documentcontrolnumber,)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'DocumentControlNumber'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'DocumentControlNumber'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class Expenditure( ):
	'''
    Constructor:
    Expenditure( bfy: str, fund: str, account: str,
                 boc: str, provider: Provider=Provider.SQLite )

    Purpose:
    Class defines object providing Expenditure data
    '''


	def __init__( self, bfy: str, efy: str, fund: str, account: str=None,
	              boc: str=None, provider: Provider=Provider.SQLite ):
		self.provider = provider
		self.source = Source.Expenditures
		self.bfy = bfy
		self.fundcode = fund
		self.accountcode = account
		self.boccode = boc
		self.fields = [ 'ExpendituresId',
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
		if self.amount is not None:
			return str( self.amount )

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'bfy', 'efy', 'fund_code', 'fund_name', 'rpio_code', 'rpio_name',
		         'ah_code', 'ah_name', 'org_code', 'org_name', 'account_code',
		         'boc_code', 'boc_name', 'rc_code', 'rc_name',
		         'program_project_code', 'program_project_name', 'program_area_code',
		         'program_area_name', 'npm_code', 'npm_name', 'goal_code', 'goal_name',
		         'objective_code', 'objective_name', 'document_type',
		         'document_number', 'document_control_number', 'rerference_document_number',
		         'last_activity_date', 'processed_date', 'age', 'vendor_code', 'vendor_name',
		         'foc_code', 'foc_name', 'amount',
		         'main_account', 'treasury_account_code', 'treasury_account_name',
		         'budget_account_code', 'budget_account_name',
		         'data', 'fields',
		         'getdata', 'getframe' ]

	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'FundCode', 'AccountCode', 'BocCode' ]
			_values = ( self.bfy, self.fundcode, self.accountcode, self.boccode )
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Expenditure'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''

		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Expenditure'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class FinanceObjectClass( ):
	'''
    Constructor:
    FinanceObjectClass( code: str, provider: Provider=Provider.SQLite )

    Purpose:
    Class defines object representing the Finance Object Class'''
	

	def __init__( self, code: str, provider: Provider=Provider.SQLite ):
		self.provider = provider
		self.source = Source.FinanceObjectClasses
		self.code = code
		self.fields = [ 'FinanceObjectClassesId',
		                  'Code',
		                  'Name',
		                  'BocCode',
		                  'BocName' ]

	def __str__( self ) -> str:
		if self.code is not None:
			return self.code

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'fields', 'data', 'frame', 'getdata', 'getframe' ]

	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'Code', ]
			_values = ( self.code, )
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'FinanceObjectClass'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_src = self.source
			_data = BudgetData( _src )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'FinanceObjectClass'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class Fund( ):
	'''
    Constructor:
    Fund( bfy: str, efy: str,
          code: str, provider: Provider=Provider.SQLite )

    Purpose:
    Class defines object represening Funds
    '''
	

	def __init__( self, bfy: str, efy: str, code: str, provider: Provider=Provider.SQLite ):
		self.provider = provider
		self.source = Source.Funds
		self.bfy = bfy
		self.efy = efy
		self.code = code
		self.fields = [ 'FundsId',
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
		if isinstance( self.code, str ) and self.code != '':
			return self.code

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'fields', 'data', 'frame', 'getdata', 'getframe' ]

	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'EFY', 'Code', ]
			_values = ( self.bfy, self.efy, self.code )
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Fund'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Fund'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class FederalHoliday( ):
	'''
    Constructor:
    FederalHoliday( bfy: str, efy: str,
                    name: str, provider: Provider=Provider.SQLite )

    Purpose:
    Defines the FederalHoliday class
    '''
	

	def __init__( self, bfy: str, efy: str, name: str = '',
	              provider: Provider=Provider.SQLite ):
		self.provider = provider
		self.source = Source.FederalHolidays
		self.holidays = [ 'ColumbusDay', 'VeteransDay', 'ThanksgivingDay', 'ChristmasDay',
		                    'NewYearsDay', 'MartinLutherKingsDay', 'PresidentsDay',
		                    'MemorialDay', 'JuneteenthDay', 'IndependenceDay', 'LaborDay' ]
		self.__observance = { 'ColumbusDay': 'The second Monday in October',
		                      'VeteransDay': 'Veterans Day, November 11',
		                      'ThanksgivingDay': 'The fourth Thursday in November',
		                      'ChristmasDay': 'Christmas Day, December 25',
		                      'NewYearsDay': 'January 1',
		                      'MartinLutherKingDay': 'The third Monday in January',
		                      'WashingtonsDay': 'The third Monday in February',
		                      'MemorialDay': 'The last Monday in May.',
		                      'JuneteenthDay': 'Juneteenth National Independence Day, June 19',
		                      'IndependenceDay': 'Independence Day, July 4',
		                      'LaborDay': 'The first Monday in September' }
		self.bfy = bfy
		self.efy = efy
		self.__year = bfy
		self.today = dt.datetime.today( )
		self.name = self.set_name( name )
		self.fields = [ 'FederalHolidaysId',
		                  'BFY',
		                  'ColumbusDay',
		                  'VeteransDay',
		                  'ThanksgivingDay',
		                  'ChristmasDay',
		                  'NewYearsDay',
		                  'MartinLutherKingDay',
		                  'PresidentsDay',
		                  'MemorialDay',
		                  'JuneteenthDay',
		                  'IndependenceDay',
		                  'LaborDay' ]
		self.data: list[ Row ]=None
		self.frame: DataFrame=None

	def __str__( self ) -> str:
		if not self.name == '':
			return self.name

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'fields', 'data', 'frame', 'getdata', 'getframe',
		         'get_columbus_day', 'get_veterans_day', 'get_thanksgiving_day',
		         'get_christmas_day', 'get_newyears_day', 'get_martinlutherking_day',
		         'get_presidents_day', 'get_memorial_day', 'independence_day',
		         'labor_day', 'day_of_week', 'is_weekday', 'is_weekend', 'set_date',
		         'set_name' ]

	def getdata( self ) -> list:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'EFY', 'Name', ]
			_values = ( self.bfy, self.efy, self.name,)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'FederalHoliday'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'FederalHoliday'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def get_columbus_day( self ) -> datetime:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			if self.__year is not None:
				__start = datetime( self.__year, 10, 1 )
				__end = datetime( self.__year, 10, 31 )
				__delta = (__start - __end).days
				for i in range( 1, 31 ):
					d = datetime( self.__year, 10, __start.day + i )
					if (15 < d.day < 28) and \
							datetime( self.__year, 10, d.day ).isoweekday( ) == 1:
						self.__columbus = datetime( self.__year, 10, d.day )
						return self.__columbus
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'FederalHoliday'
			_exc.method = 'get_columnbus_day( self )'
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
			_exc.module = 'Ninja'
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
				__delta = (__start - __end).days
				for i in range( 15, 31 ):
					d = datetime( self.__year, 11, i )
					if (21 < d.day < 31) and \
							datetime( self.__year, 11, d.day ).isoweekday( ) == 4:
						self.__thanksgiving = datetime( self.__year, 11, d.day )
						return self.__thanksgiving
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
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
			_exc.module = 'Ninja'
			_exc.cause = 'FederalHoliday'
			_exc.method = 'get_christmas_day( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def get_newyears_day( self ) -> datetime:
		'''January 1'''
		try:
			if self.__year is not None:
				self.newyearsday = datetime( self.__year, 1, 1 )
				return self.newyearsday
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
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
				__delta = (__start - __end).days
				for i in range( __delta ):
					d = datetime( self.__year, 1, __start.day + i )
					if (15 < d.day < 31) and datetime( self.__year, 1, d.day ).isoweekday( ) == 1:
						self.__martinlutherking = datetime( self.__year, 1, d.day )
						return self.__martinlutherking
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
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
				__delta = (__start - __end).days
				for i in range( __delta ):
					d = datetime( self.__year, 2, __start.day + i )
					if (15 < d.day < 28) and datetime( self.__year, 2, d.day ).isoweekday( ) == 1:
						self.__washingtons = datetime( self.__year, 2, d.day )
						return self.__washingtons
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
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
				__delta = (__start - __end).days
				for i in range( 15, 31 ):
					d = datetime( self.__year, 5, i )
					if (21 < d.day < 31) and datetime( self.__year, 5, d.day ).isoweekday( ) == 1:
						self.__memorial = datetime( self.__year, 5, d.day )
						return self.__memorial
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'FederalHoliday'
			_exc.method = 'get_memorial_day( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def get_juneteenth_day( self ) -> datetime:
		'''Juneteenth National Independence Day, June 19'''
		try:
			if self.__year is not None:
				self.uneteenth = datetime( self.__year, 6, 19 )
				return self.uneteenth
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
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
			_exc.module = 'Ninja'
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
			_exc.module = 'Ninja'
			_exc.cause = 'FederalHoliday'
			_exc.method = 'get_labor_day( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def day_of_week( self ) -> str:
		try:
			if 0 < self.__day < 8 and self.__day == 1:
				self.dayofweek = 'Monday'
				return self.dayofweek
			elif 0 < self.__day < 8 and self.__day == 2:
				self.dayofweek = 'Tuesday'
				return self.dayofweek
			elif 0 < self.__day < 8 and self.__day == 3:
				self.dayofweek = 'Wednesday'
				return self.dayofweek
			elif 0 < self.__day < 8 and self.__day == 4:
				self.dayofweek = 'Thursday'
				return self.dayofweek
			elif 0 < self.__day < 8 and self.__day == 5:
				self.dayofweek = 'Friday'
				return self.dayofweek
			elif 0 < self.__day < 8 and self.__day == 6:
				self.dayofweek = 'Saturday'
				return self.dayofweek
			elif 0 < self.__day < 8 and self.__day == 7:
				self.dayofweek = 'Sunday'
				return self.dayofweek
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'FederalHoliday'
			_exc.method = 'day_of_week( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def is_weekday( self ) -> bool:
		try:
			if 1 <= self.date.isoweekday( ) <= 5:
				return True
			else:
				return False
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'FederalHoliday'
			_exc.method = 'is_weekday( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def is_weekend( self ) -> bool:
		try:
			if 5 < self.date.isoweekday( ) <= 7:
				return True
			else:
				return False
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'FederalHoliday'
			_exc.method = 'is_weekend( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def set_date( self, name: str ):
		try:
			if isinstance( name, str ) and name in self.holidays:
				if name == 'ColumbusDay':
					self.date = self.get_columbus_day( )
					return self.date
				elif name == 'VeteransDay':
					self.date = self.get_veterans_day( )
					return self.date
				elif name == 'ThanksgivingDay':
					self.date = self.get_thanksgiving_day( )
					return self.date
				elif name == 'ChristmasDay':
					self.date = self.get_christmas_day( )
					return self.date
				elif name == 'NewYearsDay':
					self.date = self.get_newyears_day( )
					return self.date
				elif name == 'MartinLutherKingDay':
					self.date = self.get_martinlutherking_day( )
					return self.date
				elif name == 'PresidentsDay':
					self.date = self.get_presidents_day( )
					return self.date
				elif name == 'MemorialDay':
					self.date = self.get_memorial_day( )
					return self.date
				elif name == 'JuneteenthDay':
					self.date = self.get_juneteenth_day( )
					return self.date
				elif name == 'LaborDay':
					self.date = self.get_labor_day( )
					return self.date
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'FederalHoliday'
			_exc.method = 'set_date( self, value )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def set_name( self, name: str ):
		try:
			if isinstance( name, str ) and name in self.holidays:
				self.name = name
				return self.name
			else:
				self.name = 'NS'
				return self.name
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'FederalHoliday'
			_exc.method = 'set_name( self, value  ) '
			_err = ErrorDialog( _exc )
			_err.show( )

class FullTimeEquivalent( ):
	'''

    Constructor: FullTimeEquivalent( bfy: str, fund: str,
        provider: Provider=Provider.SQLite )

    Purpose:  Object representing Operating Plan FTE

    '''
	

	def __init__( self, bfy: str, fund: str, provider: Provider=Provider.SQLite ):
		self.provider = provider
		self.source = Source.FullTimeEquivalents
		self.bfy = bfy
		self.fundcode = fund
		self.fields = [ 'FullTimeEquivalentsId',
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

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'bfy', 'efy', 'fund_code', 'fund_name', 'rpio_code', 'rpio_name',
		         'ah_code', 'ah_name', 'org_code', 'org_name', 'account_code',
		         'boc_code', 'boc_name', 'rc_code', 'rc_name', 'account_code',
		         'program_project_code', 'program_project_name', 'program_area_code',
		         'program_area_name', 'npm_code', 'npm_name', 'goal_code', 'goal_name',
		         'objective_code', 'objective_name', 'amount', 'npm_code', 'npm_name',
		         'main_account', 'treasury_account_code', 'treasury_account_name',
		         'budget_account_code', 'budget_account_name',
		         'data', 'fields',
		         'getdata', 'getframe' ]

	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'FundCode' ]
			_values = ( self.bfy, self.fundcode,)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'FullTimeEquivalent'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'FullTimeEquivalent'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class GeneralLedgerAccount( ):
	'''
    Constructor:
    GeneralLedgerAccount( bfy: str, number: str,
        provider: Provider=Provider.SQLite  )

    Purpose:
    Class defines object representing General Ledger Accounts
    '''
	

	def __init__( self, bfy: str, number: str, provider: Provider=Provider.SQLite ):
		self.bfy = bfy
		self.accountnumber = number
		self.provider = provider
		self.source = Source.GeneralLedgerAccounts
		self.fields = [ 'GeneralLedgerAccountsId',
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

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'fields', 'data',
		         'frame', 'getdata', 'getframe' ]

	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'Code', ]
			_values = ( self.code, )
			_dbcfg = DbConfig( _source, _provider )
			_sqlcfg = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbcfg, _sqlcfg )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.command_text
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'GeneralLedgerAccounts'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''

        Purpose:

        Parameters:

        Returns:

        '''

		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'GeneralLedgerAccounts'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class Goal( ):
	'''
    Constructor:
    Goal( code: str, provider: Provider=Provider.SQLite )

    Purpose:
    Class defines object representing EPA  Goals
    '''
	

	def __init__( self, code: str, provider: Provider=Provider.SQLite ):
		self.provider = provider
		self.source = Source.Goals
		self.code = code
		self.fields = [ 'GoalsId',
		                  'Code',
		                  'Name',
		                  'Title' ]

	def __str__( self ) -> str:
		if isinstance( self.code, str ) and self.code != '':
			return self.code

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'code', 'name',
		         'fields', 'data', 'frame',
		         'getdata', 'getframe' ]

	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'Code', ]
			_values = ( self.code, )
			_dbcfg = DbConfig( _source, _provider )
			_sqlcfg = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbcfg, _sqlcfg )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.command_text
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Goals'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''

        Purpose:

        Parameters:

        Returns:

        '''

		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Goals'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class HeadquartersAuthority( ):
	'''
    Constructor:
    HeadquartersAuthority( bfy, rpio, pvdr = Provider.SQLite )

    Purpose:
    Class defines object representing HQ Allocation
    '''
	

	def __init__( self, bfy: str, efy: str, rpio: str, provider: Provider=Provider.SQLite ):
		self.source = Source.HeadquartersAuthority
		self.provider = provider
		self.bfy = bfy
		self.efy = efy
		self.rpiocode = rpio
		self.fields = [ 'HeadquartersAuthorityId',
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

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'bfy', 'efy', 'fund_code', 'fund_name', 'rpio_code', 'rpio_name',
		         'ah_code', 'ah_name', 'org_code', 'org_name', 'account_code',
		         'boc_code', 'boc_name', 'rc_code', 'rc_name',
		         'program_project_code', 'program_project_name', 'program_area_code',
		         'program_area_name', 'npm_code', 'npm_name', 'goal_code', 'goal_name',
		         'objective_code', 'objective_name', 'budgeted', 'posted', 'open_commitments',
		         'obligations', 'unliquidated_obligations', 'expenditures', 'used', 'available',
		         'main_account', 'treasury_account_code', 'treasury_account_name',
		         'budget_account_code', 'budget_account_name',
		         'data', 'fields',
		         'getdata', 'getframe' ]

	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'RpioCode' ]
			_values = ( self.bfy, self.rpiocode )
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'HeadquartersAuthority'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'HeadquartersAuthority'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class HeadquartersOffice( ):
	'''
    Constructor:
    HeadquartersOffice( code: str, provider: Provider=Provider.SQLite )

    Prupose:
    Class defines object representing RPIO'''
	

	def __init__( self, code: str, provider: Provider=Provider.SQLite ):
		self.rpiocode = code
		self.provider = provider
		self.source = Source.HeadquartersOffices
		self.fields = [ 'HeadquartersOfficesId',
		                  'ResourcePlanningOfficesId',
		                  'RpioCode',
		                  'RpioName' ]

	def __str__( self ) -> str:
		if self.rpiocode is not None:
			return self.rpiocode

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'rpio_code', 'rpio_name',
		         'fields', 'data', 'frame', 'getdata', 'getframe' ]

	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'RpioCode', ]
			_values = ( self.rpiocode,)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'HeadquartersOffice'
			_exc.method = 'getdata( self ) '
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''Method returning pandas dataframe
        comprised of datatable data'''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'HeadquartersOffice'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class InflationReductionActCarryoverEstimate( ):
	'''
    Constructor:
    InflationReductionActCarryoverEstimate( bfy: str,
        provider: Provider=Provider.SQLite )

    Purpose:
    Class defines object providing IRA Carryover Estimates
    '''
	

	def __init__( self, bfy: str, provider: Provider=Provider.SQLite ):
		self.provider = provider
		self.source = Source.AnnualCarryoverEstimates
		self.bfy = bfy
		self.fields = [ 'AnnualCarryoverEstimatesId',
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
		                  'OpenCommitments',
		                  'UnobligatedAuthority' ]

	def __str__( self ) -> str:
		if self.fundcode is not None:
			return self.fundcode

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'bfy', 'efy', 'rpio_code', 'rpio_name',
		         'fund_code', 'fund_name', 'amount', 'available',
		         'open_commitments', 'obligations', 'main_account',
		         'treasury_account_code', 'treasury_account_name',
		         'budget_account_code', 'budget_account_name',
		         'fields', 'data', 'frame', 'getdata', 'getframe' ]

	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'EFY' ]
			_values = ( self.bfy, self.efy)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Reporting'
			_exc.cause = 'CarryoverEstimate'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Reporting'
			_exc.cause = 'CarryoverEstimate'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class JobsActCarryoverEstimate( ):
	'''

    Constructor:
    JobsActCarryoverEstimate( bfy )

    Purpose:
    Class defines object providing IIJA Carryover Estimate data for

    '''
	

	def __init__( self, bfy: str, provider: Provider=Provider.SQLite ):
		self.provider = provider
		self.source = Source.JobsActCarryoverEstimates
		self.bfy = bfy
		self.fields = [ 'CarryoverEstimatesId',
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
		                  'OpenCommitments',
		                  'UnobligatedAuthority' ]

	def __str__( self ) -> str:
		if self.fundcode is not None:
			return self.fundcode

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'fields', 'data', 'frame', 'getdata', 'getframe' ]

	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'EFY' ]
			_values = ( self.bfy, self.efy)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Reporting'
			_exc.cause = 'CarryoverEstimate'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Reporting'
			_exc.cause = 'CarryoverEstimate'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class MainAccount( ):
	'''
	Constructor:
	MainAccounts( bfy: str, code: str )

	Purpose:
	class models the OMB Budget Account
	'''
	

	def __init__( self, code: str, provider: Provider=Provider.SQLite ):
		self.code = code
		self.provider = provider

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'code', 'subfunction_code', 'subfunction_name',
				 'budget_enforcement_act_category',
				 'budget_account_code', 'budget_account_name',
		         'fields', 'data', 'frame', 'getdata', 'getframe' ]

	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'FundCode' ]
			_values = ( self.bfy, self.fundcode )
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'MainAccounts'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''

        Purpose:

        Parameters:

        Returns:

        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'MainAccounts'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class MonthlyActual( ):
	'''
    Constructor:
    Actual( bfy = None, fund = None, pvdr = Provider.SQLite )

    Purpose:
    Class defines object representing expenditure data
    '''
	

	def __init__( self, bfy:str = None, fund: str = None,
	              provider: Provider=Provider.SQLite ):
		self.provider = provider
		self.source = Source.MonthlyActuals
		self.bfy = bfy if isinstance( bfy, str ) and len( bfy ) == 4 else None
		self.fundcode = fund if isinstance( fund, str ) and fund != '' else None
		self.fields = [ 'ActualsId',
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
		                  'UnliquidatedObligations',
		                  'Obligations',
		                  'Balance',
		                  'ProgramAreaCode',
		                  'ProgramAreaName',
		                  'GoalCode',
		                  'GoalName',
		                  'ObjectiveCode',
		                  'ObjectiveName' ]

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members
		'''
		return [ 'id', 'bfy', 'efy', 'fund_code', 'fund_name', 'rpio_code', 'rpio_name',
		         'ah_code', 'ah_name', 'org_code', 'org_name', 'account_code',
		         'boc_code', 'boc_name', 'program_project_code',
		         'program_project_name', 'npm_code', 'npm_name',
		         'goal_code', 'goal_name',
		         'gross_outlays', 'net_outlays', 'obligations',
		         'main_account', 'treasury_account_code', 'treasury_account_name',
		         'budget_account_code', 'budget_account_name',
		         'data', 'fields',
		         'getdata', 'getframe' ]

	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'FundCode' ]
			_values = ( self.bfy, self.fundcode )
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Actual'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Actual'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class MonthlyOutlay( ):
	'''
    Constructor:
    MonthlyOutlay( bfy, efy, main )

    Purpose:
    Class defines object providing OMB outlay data
    '''
	

	def __init__( self, bfy, efy, account, provider: Provider=Provider.SQLite ):
		self.provider = provider
		self.source = Source.MonthlyOutlays
		self.bfy = bfy
		self.efy = efy
		self.budgetaccountcode = account
		self.fields = [ 'MonthlyOutlaysId',
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

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'line_number', 'line_name', 'bfy', 'efy',
		         'fund_code', 'fund_name', 'taxation_code',
		         'treasury_agency_code', 'january',
		         'feburary', 'march', 'april',
		         'may', 'june', 'july', 'august',
		         'september', 'october', 'november',
		         'january', 'main_account', 'treasury_account_code',
		         'treasury_account_name', 'budget_account_code', 'budget_account_name',
		         'fields', 'data', 'frame',
		         'getdata', 'getframe' ]


	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'EFY', 'OmbAccountCode', ]
			_values = ( self.bfy, self.efy, self.budgetaccountcode )
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Reporting'
			_exc.cause = 'MonthlyOutlay'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Reporting'
			_exc.cause = 'MonthlyOutlay'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class NationalProgram( ):
	'''
    Constructor:
    NationalProgram( code: str, pvdr = Provider.SQLite )

    Purpose:
    Class defines object representing the NationalProgram Class'''
	

	def __init__( self, code: str, provider: Provider=Provider.SQLite ):
		self.provider = provider
		self.source = Source.NationalPrograms
		self.code = code
		self.fields = [ 'NationalProgramsId',
		                  'Code',
		                  'Name',
		                  'RpioCode',
		                  'Title' ]

	def __str__( self ) -> str:
		if isinstance( self.code, str ) and self.code != '':
			return self.code

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'fields', 'data', 'frame', 'getdata', 'getframe' ]

	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'Code', ]
			_values = ( self.code, )
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'NationalProgram'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'NationalProgram'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class Objective( ):
	'''
    Constructor:
    Objective( code: str, provider: Provider=Provider.SQLite )


    Purpose:
    Class defines object representing the Objective Class
    '''
	

	def __init__( self, code: str, provider: Provider=Provider.SQLite ):
		self.provider = provider
		self.source = Source.Objectives
		self.code = code
		self.fields = [ 'ObjectivesId',
		                  'Code',
		                  'Name',
		                  'Title' ]

	def __str__( self ) -> str:
		if isinstance( self.code, str ) and self.code != '':
			return self.code

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'fields', 'data', 'frame', 'getdata', 'getframe' ]

	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_source = Source.Objectives
			_provider = Provider.SQLite
			_names = [ 'Code', ]
			_values = ( self.code, )
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Objective'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Objective'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class Organization( ):
	'''
    Constructor:
    Organization( code: str, provider: Provider=Provider.SQLite  )

    Purpose:
    Class defines object representing the Organization Codes'''
	

	def __init__( self, code: str, provider: Provider=Provider.SQLite ):
		self.provider = provider
		self.source = Source.Organizations
		self.code = code
		self.fields = [ 'OrganizationsId',
		                  'Code',
		                  'Name' ]

	def __str__( self ) -> str:
		if self.code is not None:
			return self.code

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'fields', 'data', 'frame', 'getdata', 'getframe' ]

	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_source = self.source
			_provider = self.provider
			_command = SQL.SELECTALL
			_names = [ 'BFY', 'EFY', 'FundCode', 'RpioCode', 'AhCode',
			           'AccountCode', 'BocCode', 'Amount' ]
			_values = ( self.bfy, self.efy, self.fundcode, self.rpiocode,
			           self.ahcode, self.accountcode, self.boccode, self.amount )
			_db = DataBuilder( _source, _provider, _command, _names, _values )
			self.data = _db.createtable( )
			return [ (i) for i in self.data ]
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Organizations'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''

        Purpose:

        Parameters:

        Returns:

        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Organizations'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class OperatingPlan( ):
	'''
    Constructor:
    OperatingPlan( bfy, efy, treas, pvdr = Provider.SQLite )

    Purpose:
    Class defining object representing Operating plan allocations
    '''
	

	def __init__( self, bfy: str, fund: str, provider: Provider=Provider.SQLite ):
		self.source = Source.OperatingPlans
		self.provider = provider
		self.bfy = bfy
		self.fundcode = fund
		self.fields = [ 'OperatingPlansId', 'RpioCode', 'RpioName', 'BFY', 'EFY', 'AhCode',
		                  'FundCode', 'OrgCode', 'AccountCode', 'RcCode', 'BocCode', 'BocName',
		                  'Amount', 'ITProjectCode', 'ProjectCode', 'ProjectName', 'NpmCode',
		                  'ProjectTypeName', 'ProjectTypeCode', 'ProgramProjectCode',
		                  'ProgramAreaCode',
		                  'NpmName', 'AhName', 'FundName', 'OrgName', 'RcName',
		                  'ProgramProjectName',
		                  'ActivityCode', 'ActivityName', 'LocalCode', 'LocalCodeName',
		                  'ProgramAreaName',
		                  'CostAreaCode', 'CostAreaName', 'GoalCode', 'GoalName',
		                  'ObjectiveCode', 'ObjectiveName' ]

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'bfy', 'efy', 'fund_code', 'fund_name', 'rpio_code', 'rpio_name',
		         'ah_code', 'ah_name', 'org_code', 'org_name', 'account_code',
		         'boc_code', 'boc_name', 'rc_code', 'rc_name', 'amount',
		         'program_project_code', 'program_project_name', 'program_area_code',
		         'program_area_name', 'npm_code', 'npm_name', 'goal_code', 'goal_name',
		         'objective_code', 'objective_name',
		         'main_account', 'treasury_account_code', 'treasury_account_name',
		         'budget_account_code', 'budget_account_name',
		         'data', 'fields',
		         'getdata', 'getframe' ]

	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_names = [ 'BFY', 'FundCode' ]
			_values = ( self.bfy, self.fundcode )
			_dbconfig = DbConfig( self.source, self.provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'OperatingPlan'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'OperatingPlan'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class OpenCommitment( ):
	'''
    Constructor:
    OpenCommitment( bfy: str, efy: str, fund: str,
                  account: str, boc: str, provider: Provider=Provider.SQLite )

    Purpose:
    Class defines object providing OpenCommitment data.
    '''


	def __init__( self, bfy: str, efy: str, fund: str,
	              account: str, boc: str, provider: Provider=Provider.SQLite ):
		self.provider = provider
		self.source = Source.OpenCommitments
		self.bfy = bfy
		self.efy = efy
		self.fundcode = fund
		self.accountcode = account
		self.boccode = boc
		self.fields = [ 'OpenCommitmentsId',
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
		                  'OpenCommitments',
		                  'Obligations',
		                  'UnliquidatedObligations',
		                  'Expenditures' ]

	def __str__( self ) -> str:
		if self.accountcode is not None:
			return self.accountcode

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'bfy', 'efy', 'fund_code', 'fund_name', 'rpio_code', 'rpio_name',
		         'ah_code', 'ah_name', 'org_code', 'org_name', 'account_code',
		         'boc_code', 'boc_name', 'rc_code', 'rc_name',
		         'program_project_code', 'program_project_name', 'program_area_code',
		         'program_area_name', 'npm_code', 'npm_name', 'goal_code', 'goal_name',
		         'objective_code', 'objective_name', 'document_type',
		         'document_number', 'document_control_number', 'rerference_document_number',
		         'last_activity_date', 'processed_date', 'age', 'vendor_code', 'vendor_name',
		         'foc_code', 'foc_name', 'amount',
		         'main_account', 'treasury_account_code', 'treasury_account_name',
		         'budget_account_code', 'budget_account_name',
		         'data', 'fields',
		         'getdata', 'getframe' ]

	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'FundCode', 'AccountCode', 'BocCode' ]
			_values = ( self.bfy, self.fundcode, self.accountcode, self.boccode )
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'OpenCommitment'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''Method returning pandas dataframe
        comprised of datatable data'''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'OpenCommitment'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class Obligation( ):
	'''
    Constructor:  Obligation( bfy: str, efy: str, fund: str,
                  account: str, boc: str, provider: Provider=Provider.SQLite )

    Purpose:  Class defines object providing Obligation data'''


	def __init__( self, bfy: str, efy: str, fund: str,
	              account: str=None, boc: str=None, provider: Provider=Provider.SQLite ):
		self.provider = provider
		self.source = Source.Obligations
		self.bfy = bfy
		self.efy = efy
		self.fundcode = fund
		self.accountcode = account
		self.boccode = boc
		self.fields = [ 'ObligationsId',
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
		                  'OpenCommitments',
		                  'Obligations',
		                  'UnliquidatedObligations',
		                  'Expenditures' ]

	def __str__( self ) -> str:
		if self.amount is not None:
			return str( self.amount )

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'bfy', 'efy', 'fund_code', 'fund_name', 'rpio_code', 'rpio_name',
		         'ah_code', 'ah_name', 'org_code', 'org_name', 'account_code',
		         'boc_code', 'boc_name', 'rc_code', 'rc_name',
		         'program_project_code', 'program_project_name', 'program_area_code',
		         'program_area_name', 'npm_code', 'npm_name', 'goal_code', 'goal_name',
		         'objective_code', 'objective_name', 'document_type',
		         'document_number', 'document_control_number', 'rerference_document_number',
		         'last_activity_date', 'processed_date', 'age', 'vendor_code', 'vendor_name',
		         'foc_code', 'foc_name', 'amount',
		         'main_account', 'treasury_account_code', 'treasury_account_name',
		         'budget_account_code', 'budget_account_name',
		         'data', 'fields',
		         'getdata', 'getframe' ]

	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'FundCode', 'AccountCode', 'BocCode' ]
			_values = ( self.bfy, self.fundcode, self.accountcode, self.boccode )
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Obligaions'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''Method returning pandas dataframe
        comprised of datatable data'''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Obligation'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class OutlayRate( ):
	'''
    Constructor:
    Outlay( account: str, provider: Provider=Provider.SQLite  )

    Purpose:
    Class defines object that provides OMB data
    '''


	def __init__( self, account: str, provider: Provider=Provider.SQLite ):
		self.provider = provider
		self.source = Source.Outlays
		self.budgetaccountcode = account
		self.fields = [ 'BudgetOutlaysId',
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

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'report_year', 'line_number',
		         'line_section', 'line_name', 'line_category',
		         'bea_category', 'main_account', 'treasury_account_code',
		         'treasury_account_name', 'budget_account_code', 'budget_account_name',
		         'prior_year', 'current_year', 'budget_year', 'out_year_1', 'out_year_2',
		         'out_year_3', 'out_year_4', 'out_year_5', 'out_year_6', 'out_year_7',
		         'out_year_8', 'out_year_9',
		         'fields', 'data', 'frame',
		         'getdata', 'getframe' ]

	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'OmbAccountCode', ]
			_values = ( self.budgetaccountcode,)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Reporting'
			_exc.cause = 'BudgetOutlay'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Reporting'
			_exc.cause = 'BudgetOutlay'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class PublicLaw( ):
	'''
    Constructor: PublicLaw( bfy: str, efy: str,
                  number: str, provider: Provider=Provider.SQLite  )

    Purpose:
    '''


	def __init__( self, bfy: str, efy: str,
	              number: str, provider: Provider=Provider.SQLite ):
		self.bfy = bfy
		self.efy = efy
		self.lawnumber = number
		self.provider = provider
		self.source = Source.PublicLaws
		self.fields = [ 'PublicLawsId',
		                  'LawNumber',
		                  'BillTitle',
		                  'EnactedDate',
		                  'Congress',
		                  'BFY' ]

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'fields', 'data',
		         'frame', 'getdata', 'getframe' ]

	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_source = self.source
			_provider = self.provider
			_command = SQL.SELECTALL
			_names = [ 'BFY', 'EFY', 'FundCode', 'RpioCode', 'AhCode',
			           'AccountCode', 'BocCode', 'Amount' ]
			_values = ( self.bfy, self.efy, self.fundcode, self.rpiocode,
			           self.ahcode, self.accountcode, self.boccode, self.amount)
			_db = DataBuilder( _source, _provider, _command, _names, _values )
			self.data = _db.createtable( )
			return [ (i) for i in self.data ]
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'PublicLaws'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''

        Purpose:

        Parameters:

        Returns:

        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'PublicLaws'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class Project( ):
	'''
    Constructor:  Project( code: str, provider: Provider=Provider.SQLite )

    Purpoe:  Class defines the Organization Class'''
	

	def __init__( self, code: str, provider: Provider=Provider.SQLite ):
		self.provider = provider
		self.source = Source.Projects
		self.code = code
		self.fields = [ 'ProjectId',
		                  'Code',
		                  'Name' ]

	def __str__( self ) -> str:
		if self.code is not None:
			return self.code

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'code', 'name', 'fields', 'data',
		         'frame', 'getdata', 'getframe' ]

	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'Code', ]
			_values = ( self.code, )
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Project'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''Method returning pandas dataframe
        comprised of datatable data'''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Project'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class ProgramArea( ):
	'''
    Constructor:   ProgramArea( code: str, provider: Provider=Provider.SQLite  )

    Purpose:  defines the ProgramArea class
    '''
	

	def __init__( self, code: str, provider: Provider=Provider.SQLite ):
		self.provider = provider
		self.source = Source.ProgramAreas
		self.code = code
		self.fields = [ 'ProgramAreasId',
		                  'Code',
		                  'Name' ]

	def __str__( self ) -> str:
		if self.code is not None:
			return self.code

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'fields', 'data', 'frame', 'getdata', 'getframe' ]

	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'Code', ]
			_values = ( self.code, )
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'ProgramArea'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''Method returning pandas dataframe
        comprised of datatable data'''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'ProgramArea'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class ProgramProject( ):
	'''
    Constructor:  ProgramProject( code: str, provider: Provider=Provider.SQLite )

    Purpose:  Defines the ProgramProject Class
    '''
	

	def __init__( self, code: str, provider: Provider=Provider.SQLite ):
		self.provider = provider
		self.source = Source.ProgramProjects
		self.code = code
		self.fields = [ 'ProgramProjectsId',
		                  'Code',
		                  'Name',
		                  'ProgramAreaCode',
		                  'ProgramAreaName' ]

	def __str__( self ) -> str:
		if self.code is not None:
			return self.code

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'fields', 'data', 'frame', 'getdata', 'getframe' ]

	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_source = self.source
			_provider = self.provider
			_command = SQL.SELECTALL
			_names = [ 'BFY', 'EFY', 'FundCode', 'RpioCode', 'AhCode',
			           'AccountCode', 'BocCode', 'Amount' ]
			_values = ( self.bfy, self.efy, self.fundcode, self.rpiocode,
			           self.ahcode, self.accountcode, self.boccode, self.amount)
			_db = DataBuilder( _source, _provider, _command, _names, _values )
			self.data = _db.createtable( )
			return [ (i) for i in self.data ]
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'ProgramProjects'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''

        Purpose:

        Parameters:

        Returns:

        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'ProgramProjects'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class ProgramResultsCode( ):
	'''
    Constructor:   ProgramResultsCode( bfy: str=None, efy: str=None, fund: str=None,
                  rpio: str=None, ah: str=None, account: str=None, boc: str=None,
                  amount: float = 0.0, provider: Provider=Provider.SQLite )

    Purpose:  Class defines the PRCs
    '''
	source: Source=None
	provider: Provider=None
	id = None
	rpiocode: str=None
	rpioname: str=None
	bfy: str=None
	efy: str=None
	ahcode: str=None
	ahname: str=None
	fundcode: str=None
	fundname: str=None
	orgcode: str=None
	orgname: str=None
	accountcode: str=None
	accountname = None
	activitycode: str=None
	activityname = None
	rccode: str=None
	rcname: str=None
	boccode: str=None
	bocname: str=None
	amount: float=None
	programprojectcode: str=None
	programprojectname: str=None
	programareacode: str=None
	programareaname: str=None
	goalcode: str=None
	goalname: str=None
	objectivecode: str=None
	objectivename: str=None
	npmcode: str=None
	npmname: str=None
	fields:  list[ str ]=None
	data: list[ Row ]=None
	frame: DataFrame=None

	@property
	def id( self ) -> int:
		if self.id is not None:
			return self.id

	@id.setter
	def id( self, value: int ):
		if value is not None:
			self.id = value

	@property
	def bfy( self ) -> str:
		if self.bfy is not None:
			return self.bfy

	@bfy.setter
	def bfy( self, value: str ):
		if value is not None:
			self.bfy = value

	@property
	def efy( self ) -> str:
		if self.efy is not None:
			return self.efy

	@efy.setter
	def efy( self, value: str ):
		if value is not None:
			self.efy = value

	@property
	def rpio_code( self ) -> str:
		if self.rpiocode is not None:
			return self.rpiocode

	@rpio_code.setter
	def rpio_code( self, value: str ):
		if value is not None:
			self.rpiocode = value

	@property
	def rpio_name( self ) -> str:
		if self.rpioname is not None:
			return self.rpioname

	@rpio_name.setter
	def rpio_name( self, value: str ):
		if value is not None:
			self.rpioname = value

	@property
	def ah_code( self ) -> str:
		if self.ahcode is not None:
			return self.ahcode

	@ah_code.setter
	def ah_code( self, value: str ):
		if value is not None:
			self.ahcode = value

	@property
	def ah_name( self ) -> str:
		if self.ahname is not None:
			return self.ahname

	@ah_name.setter
	def ah_name( self, value: str ):
		if value is not None:
			self.ahname = value

	@property
	def fund_code( self ) -> str:
		if self.fundcode is not None:
			return self.fundcode

	@fund_code.setter
	def fund_code( self, value: str ):
		if value is not None:
			self.fundcode = value

	@property
	def fund_name( self ) -> str:
		if self.fundname is not None:
			return self.fundname

	@fund_name.setter
	def fund_name( self, value: str ):
		if value is not None:
			self.fundname = value

	@property
	def org_code( self ) -> str:
		if self.orgcode is not None:
			return self.orgcode

	@org_code.setter
	def org_code( self, value: str ):
		if value is not None:
			self.orgcode = value

	@property
	def org_name( self ):
		if self.orgname is not None:
			return self.orgname

	@org_name.setter
	def org_name( self, value ):
		if value is not None:
			self.orgname = value

	@property
	def account_code( self ) -> str:
		if self.accountcode is not None:
			return self.accountcode

	@account_code.setter
	def account_code( self, value: str ):
		if value is not None:
			self.accountcode = value

	@property
	def boc_code( self ) -> str:
		if self.boccode is not None:
			return self.boccode

	@boc_code.setter
	def boc_code( self, value: str ):
		if value is not None:
			self.boccode = value

	@property
	def boc_name( self ) -> str:
		if self.bocname is not None:
			return self.bocname

	@boc_name.setter
	def boc_name( self, value: str ):
		if value is not None:
			self.bocname = value

	@property
	def rc_code( self ) -> str:
		if self.rccode is not None:
			return self.rccode

	@rc_code.setter
	def rc_code( self, value: str ):
		if value is not None:
			self.rccode = value

	@property
	def rc_name( self ) -> str:
		if self.rcname is not None:
			return self.rcname

	@rc_name.setter
	def rc_name( self, value: str ):
		if value is not None:
			self.rcname = value

	@property
	def amount( self ) -> float:
		if self.amount is not None:
			return self.amount

	@amount.setter
	def amount( self, value: float ):
		if value is not None:
			self.amount = value

	@property
	def program_project_code( self ) -> str:
		if self.programprojectcode is not None:
			return self.programprojectcode

	@program_project_code.setter
	def program_project_code( self, value: str ):
		if value is not None:
			self.programprojectcode = value

	@property
	def program_project_name( self ) -> str:
		if self.programprojectname is not None:
			return self.programprojectname

	@program_project_name.setter
	def program_project_name( self, value: str ):
		if value is not None:
			self.programprojectname = value

	@property
	def program_area_code( self ) -> str:
		if self.programareacode is not None:
			return self.programareacode

	@program_area_code.setter
	def program_area_code( self, value: str ):
		if value is not None:
			self.programareacode = value

	@property
	def program_area_name( self ) -> str:
		if self.programareaname is not None:
			return self.programareaname

	@program_area_name.setter
	def program_area_name( self, value: str ):
		if value is not None:
			self.programareaname = value

	@property
	def goal_code( self ) -> str:
		if self.goalcode is not None:
			return self.goalcode

	@goal_code.setter
	def goal_code( self, value: str ):
		if value is not None:
			self.goalcode = value

	@property
	def goal_name( self ) -> str:
		if self.goalname is not None:
			return self.goalname

	@goal_name.setter
	def goal_name( self, value: str ):
		if value is not None:
			self.goalname = value

	@property
	def objective_code( self ) -> str:
		if self.objectivecode is not None:
			return self.objectivecode

	@objective_code.setter
	def objective_code( self, value: str ):
		if value is not None:
			self.objectivecode = value

	@property
	def objective_name( self ) -> str:
		if self.objectivename is not None:
			return self.objectivename

	@objective_name.setter
	def objective_name( self, value: str ):
		if value is not None:
			self.objectivename = value

	@property
	def npm_code( self ) -> str:
		if self.npmcode is not None:
			return self.npmcode

	@npm_code.setter
	def npm_code( self, value: str ):
		if value is not None:
			self.npmcode = value

	@property
	def npm_name( self ) -> str:
		if self.npmname is not None:
			return self.npmname

	@npm_name.setter
	def npm_name( self, value: str ):
		if value is not None:
			self.npmname = value

	@property
	def activity_code( self ) -> str:
		if self.activitycode is not None:
			return self.activitycode

	@activity_code.setter
	def activity_code( self, value: str ):
		if value is not None:
			self.activitycode = value

	@property
	def activity_name( self ) -> str:
		if self.activityname is not None:
			return self.activityname

	@activity_name.setter
	def activity_name( self, value: str ):
		if value is not None:
			self.activityname = value

	@property
	def data( self ) -> list[ Row ]:
		if self.data is not None:
			return self.data

	@data.setter
	def data( self, value: list[ Row ] ):
		if isinstance( value, list ):
			self.data = value

	@property
	def frame( self ) -> DataFrame:
		if self.frame is not None:
			return self.frame

	@frame.setter
	def frame( self, value: DataFrame ):
		if value is not None:
			self.frame = value

	@property
	def fields( self ) -> list[ str ]:
		if self.fields is not None:
			return self.fields

	@property
	def fields( self ) -> list[ str ]:
		if self.fields is not None:
			return self.fields

	@fields.setter
	def fields( self, value: list[ str ] ):
		if value is not None:
			self.fields = value

	def __init__( self, bfy: str=None, efy: str=None, fund: str=None,
	              rpio: str=None, ah: str=None, account: str=None, boc: str=None,
	              amount: float = 0.0, provider: Provider=Provider.SQLite ):
		self.provider = provider
		self.source = Source.Allocations
		self.accountcode = account
		self.bfy = bfy
		self.efy = efy
		self.fundcode = fund
		self.rpiocode = rpio
		self.ahcode = ah
		self.boccode = boc
		self.amount = amount
		self.fields = [ 'AllocationsId',
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
		                  'ActivityCode',
		                  'ActivityName',
		                  'NpmCode',
		                  'NpmName',
		                  'ObjectiveCode',
		                  'ObjectiveName',
		                  'MainAccount',
		                  'TreasuryAccountCode',
		                  'TreasuryAccountName',
		                  'BudgetAccountCode',
		                  'BudgetAccountName' ]

	def __str__( self ) -> str:
		if self.fundcode is not None:
			return self.fundcode

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'bfy', 'efy', 'fund_code', 'fund_name', 'rpio_code', 'rpio_name',
		         'ah_code', 'ah_name', 'org_code', 'org_name', 'account_code',
		         'boc_code', 'boc_name', 'rc_code', 'rc_name',
		         'program_project_code', 'program_project_name', 'program_area_code',
		         'program_area_name', 'npm_code', 'npm_name', 'goal_code', 'goal_name',
		         'objective_code', 'objective_name', 'activity_code', 'activity_name',
		         'amount', 'main_account', 'treasury_account_code',
		         'treasury_account_name', 'budget_account_code', 'budget_account_name',
		         'data', 'fields', 'getdata', 'getframe' ]

	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_source = self.source
			_provider = self.provider
			_command = SQL.SELECTALL
			_names = [ 'BFY', 'EFY', 'FundCode', 'RpioCode', 'AhCode',
			           'AccountCode', 'BocCode', 'Amount' ]
			_values = ( self.bfy, self.efy, self.fundcode, self.rpiocode,
			           self.ahcode, self.accountcode, self.boccode, self.amount)
			_db = DataBuilder( _source, _provider, _command, _names, _values )
			self.data = _db.createtable( )
			return [ (i) for i in self.data ]
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'ProgramResultsCode'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'ProgramResultsCode'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class ReportingLine( ):
	'''
	Constructor:
	ReportingLines( bfy: str, code: str )

	Purpose:
	class models the lines on the SF-133 and SF-132
	'''


	def __init__( self, bfy: str, code: str, provider: Provider=Provider.SQLite ):
		self.bfy = bfy
		self.code = code
		self.provider = provider
		self.source = Source.ReportingLines

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'fields', 'data', 'frame', 'getdata', 'getframe' ]

	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'Code', ]
			_values = ( self.code, )
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'ReportingLines'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''

        Purpose:

        Parameters:

        Returns:

        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'ReportingLines'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class ResponsibilityCenter( ):
	'''
    Constructor:
    ResponsibilityCenter( code: str, provider: Provider=Provider.SQLite  )

    Purpose:
    Class defines the ResponsibilityCenter Class
    '''


	def __init__( self, code: str, provider: Provider=Provider.SQLite ):
		self.provider = provider
		self.source = Source.ResponsibilityCenters
		self.code = code if isinstance( code, str ) else None
		self.fields = [ 'ResponsibilityCentersId',
		                  'Code',
		                  'Name',
		                  'Title' ]

	def __str__( self ) -> str:
		if self.code is not None:
			return self.code

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'fields', 'data', 'frame', 'getdata', 'getframe' ]

	def getdata( self ) -> list[ tuple ]:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'Code', ]
			_values = ( self.code, )
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'ResponsibilityCenter'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'ResponsibilityCenter'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class ResourcePlanningOffice( ):
	'''
    Constuctor:
    ResourcePlanningOffice( code: str, provider: Provider=Provider.SQLite )

    Purpose:
    Defines the ResponsiblePlanningOffice class
    '''


	def __init__( self, code: str, provider: Provider=Provider.SQLite ):
		self.provider = provider
		self.source = Source.ResourcePlanningOffices
		self.code = code
		self.fields = [ 'ResourcePlanningOfficesId',
		                  'Code',
		                  'Name' ]

	def __str__( self ) -> str:
		if self.code is not None:
			return self.code

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'fields', 'data', 'frame', 'getdata', 'getframe' ]

	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'Code', ]
			_values = ( self.code, )
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'ResourcePlanningOffice'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'ResourcePlanningOffice'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class RegionalOffice( ):
	'''
    Constructor:
    RegionalOffice( code: str, provider: Provider=Provider.SQLite )

    Purpose:
    Defines a regional RPIO
    '''


	def __init__( self, code: str, provider: Provider=Provider.SQLite ):
		self.provider = provider
		self.source = Source.ResourcePlanningOffices
		self.rpiocode = code
		self.fields = [ 'RegionalOfficesId',
		                  'ResourcePlanningOfficesId',
		                  'RpioCode',
		                  'RpioName' ]

	def __str__( self ) -> str:
		if self.rpiocode is not None:
			return self.rpiocode

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'rpio_code', 'rpio_name', 'fields',
		         'data', 'frame', 'getdata', 'getframe' ]

	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'Code', ]
			_values = ( self.rpiocode,)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'RegionalOffice'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class ReimbursableAgreement( ):
	'''
    Constructor:
    ReimbursableAgreement( number: str, provider: Provider=Provider.SQLite  )

    Purpose:
    Class defines object representing Reimbursable Agreements
    '''


	def __init__( self, number: str, provider: Provider=Provider.SQLite ):
		self.provider = provider
		self.source = Source.ReimbursableAgreements
		self.__agreementnumber = number
		self.fields = [ 'ReimbursableAgreementsId'
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
		                  'OpenCommitments',
		                  'Obligations',
		                  'UnliquidatedObligations',
		                  'Available' ]

	def __str__( self ) -> str:
		if self.__agreementnumber is not None:
			return self.__agreementnumber

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'fields', 'data', 'frame', 'getdata', 'getframe' ]

	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', ]
			_values = ( self.bfy,)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Reporting'
			_exc.cause = 'ObjectClassOutlay'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Reporting'
			_exc.cause = 'ObjectClassOutlay'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class RegionalAuthority( ):
	'''
    Constructor:
    RegionalAuthority( bfy: str, efy: str, fund: str, provider: Provider=Provider.SQLite )

    Purpose:
    Class defines object representing Regional Allocation
    '''


	def __init__( self, bfy: str, efy: str, fund: str,
	              provider: Provider=Provider.SQLite ):
		self.source = Source.RegionalAuthority
		self.provider = provider
		self.bfy = bfy
		self.efy = efy
		self.fundcode = fund
		self.fields = [ 'RegionalAuthorityId',
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

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'bfy', 'efy', 'fund_code', 'fund_name', 'rpio_code', 'rpio_name',
		         'ah_code', 'ah_name', 'org_code', 'org_name', 'account_code',
		         'boc_code', 'boc_name', 'rc_code', 'rc_name',
		         'program_project_code', 'program_project_name', 'program_area_code',
		         'program_area_name', 'npm_code', 'npm_name', 'goal_code', 'goal_name',
		         'objective_code', 'objective_name', 'budgeted', 'posted', 'open_commitments',
		         'obligations', 'unliquidated_obligations', 'expenditures', 'used', 'available',
		         'main_account', 'treasury_account_code', 'treasury_account_name',
		         'budget_account_code', 'budget_account_name',
		         'data', 'fields',
		         'getdata', 'getframe' ]

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'fields', 'data', 'frame', 'getdata', 'getframe' ]

	def getdata( self ) -> list[ Row ]:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'RpioCode' ]
			_values = ( self.bfy, self.rpiocode )
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'RegionalAuthority'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'RegionalAuthority'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class StatusOfFunds( ):
	'''
    Constructor:
    StatusOfFunds( bfy: str, fund: str, provider: Provider=Provider.SQLite )

    Purpose:
    Class defines object representing execution data
    '''


	def __init__( self, bfy: str, fund: str, provider: Provider=Provider.SQLite ):
		self.source = Source.StatusOfFunds
		self.provider = provider
		self.bfy = bfy
		self.fundcode = fund
		self.fields = [ 'StatusOfFundsId',
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
		                  'OpenCommitments',
		                  'UnliquidatedObligations',
		                  'Expenditure',
		                  'Obligations',
		                  'Used',
		                  'Available',
		                  'NpmCode',
		                  'NpmName' ]

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'bfy', 'efy', 'fund_code', 'fund_name', 'rpio_code', 'rpio_name',
		         'ah_code', 'ah_name', 'org_code', 'org_name', 'account_code',
		         'boc_code', 'boc_name', 'rc_code', 'rc_name',
		         'program_project_code', 'program_project_name', 'program_area_code',
		         'program_area_name', 'npm_code', 'npm_name', 'goal_code', 'goal_name',
		         'objective_code', 'objective_name', 'budgeted', 'posted', 'open_commitments',
		         'obligations', 'unliquidated_obligations', 'expenditures', 'used', 'available',
		         'main_account', 'treasury_account_code', 'treasury_account_name',
		         'budget_account_code', 'budget_account_name',
		         'data', 'fields',
		         'getdata', 'getframe' ]

	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_source = self.source
			_provider = self.provider
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'StatusOfFunds'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''Method returning pandas dataframe
        comprised of datatable data'''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'StatusOfFunds'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class StatusOfBudgetaryResources( ):
	'''
    Constructor:
    StatusOfBudgetaryResources( tsym: str )

    Purpose:
    Class representing the Monthly SF-133
    '''


	def __init__( self, year: str, account: str, provider: Provider=Provider.SQLite ):
		self.provider = provider
		self.source = Source.StatusOfBudgetaryResources
		self.fiscalyear = year
		self.budgetaccountcode = account

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'fiscal_year', 'bfy', 'efy',
		         'fund_code', 'fund_name', 'begging_period_availability',
		         'ending_period_availability', 'january',
		         'feburary', 'march', 'april',
		         'may', 'june', 'july', 'august',
		         'september', 'october', 'november',
		         'january', 'fields', 'data', 'frame',
		         'getdata', 'getframe' ]

	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'FundCode' ]
			_values = ( self.bfy, self.fundcode )
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'StatusOfBudgetaryResources'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''Method returning pandas dataframe
        comprised of datatable data'''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'StatusOfBudgetaryResources'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class StatusOfBudgetExecution( ):
	'''
    Constructor:
    StatusOfBudgetaryResources( tsym: str )

    Purpose:
    Class representing the Monthly SF-133
    '''


	def __init__( self, account: str, provider: Provider=Provider.SQLite ):
		self.source = Source.StatusOfBudgetExecution
		self.treasuryaccountcode = account
		self.provider = provider

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'fiscal_year', 'bfy', 'efy',
		         'section_name', 'section_number', 'line_number',
		         'amount', 'treasury_account_code', 'treasury_account_name',
		         'budget_accocunt_code', 'budget_account_name',
		         'fields', 'data', 'frame',
		         'getdata', 'getframe' ]

	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'FundCode' ]
			_values = ( self.bfy, self.fundcode )
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'StatusOfBudgetExecution'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''

        Purpose:  Method returning pandas dataframe
        comprised of datatable data


        Parameters:

        Returns:

        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'StatusOfBudgetExecution'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class StatusOfSupplementalFunding( ):
	'''
    Constructor:
    StatusOfFunds( bfy: str, efy: str, fund: str, provider: Provider=Provider.SQLite )

    Purpose:
    Class representing Supplemental Funding execution data
    '''


	def __init__( self, bfy: str, efy: str, fund: str, 
	              provider: Provider=Provider.SQLite ):
		self.source = Source.StatusOfSupplementalFunding
		self.provider = provider
		self.bfy = bfy
		self.efy = efy
		self.fundcode = fund
		self.fields = [ 'StatusOfFundsId',
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
		                  'OpenCommitments',
		                  'UnliquidatedObligations',
		                  'Expenditure',
		                  'Obligations',
		                  'Used',
		                  'Available',
		                  'NpmCode',
		                  'NpmName' ]

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'bfy', 'efy', 'fund_code', 'fund_name', 'rpio_code', 'rpio_name',
		         'ah_code', 'ah_name', 'org_code', 'org_name', 'account_code',
		         'boc_code', 'boc_name', 'rc_code', 'rc_name',
		         'program_project_code', 'program_project_name', 'program_area_code',
		         'program_area_name', 'npm_code', 'npm_name', 'goal_code', 'goal_name',
		         'objective_code', 'objective_name', 'budgeted', 'posted', 'open_commitments',
		         'obligations', 'unliquidated_obligations', 'expenditures', 'used', 'available',
		         'main_account', 'treasury_account_code', 'treasury_account_name',
		         'budget_account_code', 'budget_account_name',
		         'data', 'fields',
		         'getdata', 'getframe' ]

	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'FundCode' ]
			_values = ( self.bfy, self.fundcode )
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'StatusOfSupplementalFunding'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''Method returning pandas dataframe
        comprised of datatable data'''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'StatusOfSupplementalFunding'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class StateGrantObligations( ):
	'''
    Constructor:
    StateGrantObligation( bfy: str, rpio: str, provider: Provider=Provider.SQLite )

    Purpose:
    Class defines object representing the BIS
    '''


	def __init__( self, bfy: str, rpio: str, provider: Provider=Provider.SQLite ):
		self.source = Source.StateGrantObligations
		self.provider = provider
		self.bfy = bfy
		self.rpiocode = rpio
		self.fields = [ 'StateGrantObligationsId',
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

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'bfy', 'efy', 'fund_code', 'fund_name', 'rpio_code', 'rpio_name',
		         'ah_code', 'ah_name', 'org_code', 'org_name', 'account_code',
		         'boc_code', 'boc_name', 'rc_code', 'rc_name',
		         'program_project_code', 'program_project_name', 'program_area_code',
		         'program_area_name', 'npm_code', 'npm_name', 'goal_code', 'goal_name',
		         'objective_code', 'objective_name', 'document_type',
		         'document_number', 'document_control_number', 'rerference_document_number',
		         'last_activity_date', 'processed_date', 'age', 'vendor_code', 'vendor_name',
		         'foc_code', 'foc_name', 'amount',
		         'main_account', 'treasury_account_code', 'treasury_account_name',
		         'budget_account_code', 'budget_account_name',
		         'data', 'fields',
		         'getdata', 'getframe' ]

	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'RpioCode' ]
			_values = ( self.rpiocode, self.rpiocode )
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'StateGrantObligation'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''Method returning pandas dataframe
        comprised of datatable data'''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'StateGrantObligation'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class StatusOfSpecialAccountFunds( ):
	'''
     Constructor:
     StatusOfSpecialAccountFunds( bfy = None, fund = None,
                                 account = None, boc = None, pvdr = Provider.SQLite )

     Purpose:
     Class defines object providing SF Special Account data
     '''


	def __init__( self, bfy = None, fund = None, account = None, 
	              provider: Provider=Provider.SQLite ):
		self.provider = provider
		self.source = Source.StatusOfSpecialAccountFunds
		self.bfy = bfy
		self.fundcode = fund
		self.__programcode = account
		self.fields = [ 'SpecialAccountsId',
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
		                  'OpenCommitments',
		                  'Obligations',
		                  'UnliquidatedObligations',
		                  'Disbursements',
		                  'UnpaidBalances',
		                  'Collections',
		                  'CumulativeReceipts' ]

	def __str__( self ) -> str:
		if self.__sitecode is not None:
			return self.__sitecode

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'fields', 'data', 'frame', 'getdata', 'getframe' ]

	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'FundCode', 'AccountCode', 'BocCode' ]
			_values = ( self.bfy, self.fundcode, self.__programcode, self.__interestdate )
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'StatusOfSpecialAccountFunds'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'StatusOfSpecialAccountFunds'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class SubAppropriation( ):
	'''

    Constructor:
    SubAppropriation( bfy: str, efy: str, code: str, provider: Provider=Provider.SQLite )

    Purpose:
    Class defines object representing the Sub-Appropriations

    '''


	def __init__( self, bfy: str, efy: str, code: str, 
	              provider: Provider=Provider.SQLite ):
		self.provider = provider
		self.source = Source.Appropriations
		self.bfy = bfy
		self.efy = efy
		self.code = code
		self.fields = [ 'SubAppropriationsId',
		                  'Code',
		                  'Name' ]

	def __str__( self ) -> str:
		if self.code is not None:
			return self.code

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'fields', 'data', 'frame', 'getdata', 'getframe' ]

	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'Code' ]
			_values = ( self.code, )
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'SubAppropriation'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Appropriation'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class StateOrganization( ):
	'''
    Constructor:
    StateOrganization( code: str, provider: Provider=Provider.SQLite )

    Purpose:
    Class defines object representing state organization codes
    '''


	def __init__( self, code: str, provider: Provider=Provider.SQLite ):
		self.provider = provider
		self.source = Source.StateOrganizations
		self.code = code
		self.fields = [ 'StateOrganizationsId',
		                  'Name',
		                  'Code',
		                  'RpioName',
		                  'RpioCode' ]

	def __str__( self ) -> str:
		if self.code is not None:
			return self.code

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'fields', 'data', 'frame', 'getdata', 'getframe' ]

	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'Code', ]
			_values = ( self.code, )
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'StateOrganization'
			_exc.method = 'getdata( self ) '
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'StateOrganization'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class StatusOfAppropriations( ):
	'''
    Constructor:
    StatusOfAppropriations( bfy: str, efy: str, fund: str, provider: Provider=Provider.SQLite )

    Purpose:
    Class defines object representing Appropriation-level execution data
    '''


	def __init__( self, bfy: str, efy: str, fund: str, 
	              provider: Provider=Provider.SQLite ):
		self.provider = provider
		self.source = Source.StatusOfAppropriations
		self.bfy = bfy
		self.efy = efy
		self.appropriationfundcode = fund
		self.fields = [ 'StatusOfAppropriationsId',
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
		                  'UnliquidatedObligations',
		                  'VoidedAmount',
		                  'TotalUsedAmount',
		                  'AvailableAmount' ]

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'fields', 'data', 'frame', 'getdata', 'getframe' ]

	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'EFY', 'AppropriationFundCode', ]
			_values = ( self.bfy, self.efy, self.appropriationfundcode )
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Reporting'
			_exc.cause = 'StatusOfAppropriations'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Reporting'
			_exc.cause = 'StatusOfAppropriations'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class SpendingRate( ):
	'''
    Constructor:
    SpendingRate( accountcode: str, provider: Provider=Provider.SQLite )

    Purpose:
    Class object providing OMB spending rate data
    '''


	def __init__( self, account: str, provider: Provider=Provider.SQLite ):
		self.provider = provider
		self.source = Source.SpendingRates
		self.budgetaccountcode = account
		self.fields = [ 'SpendingRatesId',
		                  'OmbAgencyCode',
		                  'OmbAgencyName',
		                  'OmbBureauCode',
		                  'OmbBureauName',
		                  'TreausuryAgencyCode',
		                  'TreausuryAccountCode',
		                  'TreausuryAccountName',
		                  'BudgetAccountCode',
		                  'BudgetAccountName',
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

	def __dir__( self ) -> list[ str ]:
		'''

		returns a list[ str ] of class members

		'''
		return [ 'id', 'treasury_agency_code', 'treasury_agency_name',
		         'omb_agency_code', 'omb_agency_name', 'main_account',
		         'treasury_account_code', 'treasury_account_name',
		         'budget_account_code', 'budget_account_name', 'subaccount',
		         'subcategory', 'subfunction', 'category',
		         'line_number', 'line_name', 'year_of_authority',
		         'budget_authority', 'out_year_1', 'out_year_2', 'out_year_3',
				 'out_year_4', 'out_year_5', 'out_year_6',
				 'out_year_7', 'out_year_8', 'out_year_9',
				 'out_year_10', 'out_year_11', 'total_spendout',
		         'fields', 'data', 'frame', 'getdata', 'getframe' ]

	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_source = self.source
			_provider = self.provider
			_command = SQL.SELECTALL
			_names = [ 'BudgetAccountCode', ]
			_values = ( self.budgetaccountcode,)
			_db = DataBuilder( _source, _provider, _command, _names, _values )
			self.data = [ i for i in _db.createtable( ) ]
			return [ i for i in self.data ]
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Reporting'
			_exc.cause = 'SpendingRate'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Reporting'
			_exc.cause = 'SpendingRate'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class StatusOfSupplementalFunds( ):
	'''
    Constructor:
    StatusOfSupplementalFunds( bfy, efy, fund, pvdr = Provider.SQLite )

    Purpose:
    Class defines object used for reporting on Supplemental funding
    '''


	def __init__( self, bfy: str, efy: str, fund: str, 
	              provider: Provider=Provider.SQLite ):
		self.provider = provider
		self.source = Source.StatusOfSupplementalFunding
		self.bfy = bfy
		self.efy = efy
		self.fundcode = fund
		self.fields = [ 'StatusOfSupplementalFundsId',
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
		                  'OpenCommitments',
		                  'UnliquidatedObligations',
		                  'Expenditure',
		                  'Obligations',
		                  'Used',
		                  'Available',
		                  'NpmCode',
		                  'NpmName' ]

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'bfy', 'efy', 'fund_code', 'fund_name', 'rpio_code', 'rpio_name',
		         'ah_code', 'ah_name', 'org_code', 'org_name', 'account_code',
		         'boc_code', 'boc_name', 'rc_code', 'rc_name',
		         'program_project_code', 'program_project_name', 'program_area_code',
		         'program_area_name', 'npm_code', 'npm_name', 'goal_code', 'goal_name',
		         'objective_code', 'objective_name', 'budgeted', 'posted', 'open_commitments',
		         'obligations', 'unliquidated_obligations', 'expenditures', 'used', 'available',
		         'main_account', 'treasury_account_code', 'treasury_account_name',
		         'budget_account_code', 'budget_account_name',
		         'data', 'fields',
		         'getdata', 'getframe' ]

	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'EFY', 'FundCode' ]
			_values = ( self.bfy, self.fundcode, self.accountcode, self.boccode )
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'StatusOfSupplementalFunds'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'StatusOfSupplementalFunds'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class StatusOfJobsActFunding( ):
	'''
    Constructor:
    StatusOfJobsActFunding(  bfy: str, efy: str,
        fundcode: str, pvdr = Provider.SQLite )

    Purpose:
    Class defines object for reporting on IIJA funds
    '''


	def __init__( self, bfy: str, efy: str, fundcode: str,
	              provider: Provider=Provider.SQLite ):
		self.bfy = bfy
		self.efy = efy
		self.fundcode = fundcode
		self.provider = provider
		self.source = Source.StatusOfJobsActFunding
		self.fields = [ 'StatusOfJobsActFundingId',
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
		                  'OpenCommitments',
		                  'UnliquidatedObligations',
		                  'Expenditure',
		                  'Obligations',
		                  'Used',
		                  'Available',
		                  'MainAccount',
		                  'TreasuryAccountCode',
		                  'TreasuryAccountName',
		                  'BudgetAccountCode',
		                  'BudgetAccountName' ]

	def __str__( self ) -> str:
		if self.fundname is not None:
			return self.fundname

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'bfy', 'efy', 'fund_code', 'fund_name', 'rpio_code', 'rpio_name',
		         'ah_code', 'ah_name', 'org_code', 'org_name', 'account_code',
		         'boc_code', 'boc_name', 'rc_code', 'rc_name',
		         'program_project_code', 'program_project_name', 'program_area_code',
		         'program_area_name', 'npm_code', 'npm_name', 'goal_code', 'goal_name',
		         'objective_code', 'objective_name', 'budgeted', 'posted', 'open_commitments',
		         'obligations', 'unliquidated_obligations', 'expenditures', 'used', 'available',
		         'main_account', 'treasury_account_code', 'treasury_account_name',
		         'budget_account_code', 'budget_account_name',
		         'data', 'fields',
		         'getdata', 'getframe' ]

	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'EFY', 'FundCode' ]
			_values = ( self.bfy, self.fundcode, self.accountcode, self.boccode )
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'StatusOfJobsActFunding'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'StatusOfJobsActFunding'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class StatusOfEarmarks( ):
	'''
    Constructor:
    StatusOfEarmarks(  bfy: str, efy: str, fundcode: str, pvdr = Provider.SQLite )

     Purpose:
     Class defines object for reporting on Earmarks
    '''


	def __init__( self, bfy: str, efy: str,
	              fundcode: str, provider: Provider=Provider.SQLite ):
		self.bfy = bfy
		self.efy = efy
		self.fundcode = fundcode
		self.provider = provider
		self.source = Source.StatusOfEarmarks
		self.fields = [ 'StatusOfEarmarksId',
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
		                  'StateCode',
		                  'ZipCode'
		                  'StateName',
		                  'Amount',
		                  'Budgeted',
		                  'Posted',
		                  'OpenCommitments',
		                  'UnliquidatedObligations',
		                  'Expenditures',
		                  'Obligations',
		                  'Used',
		                  'Available' 
		                  'MainAccount',
		                  'TreasuryAccountCode',
		                  'TreasuryAccountName',
		                  'BudgetAccountCode',
		                  'BudgetAccountName' ]

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'bfy', 'efy', 'fund_code', 'fund_name', 'rpio_code', 'rpio_name',
		         'ah_code', 'ah_name', 'org_code', 'org_name', 'account_code',
		         'boc_code', 'boc_name', 'rc_code', 'rc_name',
		         'program_project_code', 'program_project_name', 'program_area_code',
		         'program_area_name', 'npm_code', 'npm_name', 'goal_code', 'goal_name',
		         'objective_code', 'objective_name', 'state_code', 'state_name', 'zip_code',
		         'county_name', 'city_name', 'site_id', 'site_name',
		         'budgeted', 'posted', 'open_commitments',
		         'obligations', 'unliquidated_obligations', 'expenditures', 'used', 'available',
		         'main_account', 'treasury_account_code', 'treasury_account_name',
		         'budget_account_code', 'budget_account_name',
		         'data', 'fields',
		         'getdata', 'getframe' ]

	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'FundCode' ]
			_values = ( self.bfy, self.fundcode )
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'StatusOfEarmark'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''

        Purpose:  Method returning pandas dataframe
        comprised of datatable data


        Parameters:

        Returns:

        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'StatusOfEarmark'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class StatusOfSuperfundSites( ):
	'''
    Constructor:
    StatusOfSuperfundSites(  bfy: str, efy: str, fundcode: str, pvdr = Provider.SQLite )

     Purpose:
     Class defines object for reporting on Earmarks
    '''


	def __init__( self, bfy: str, efy: str, rpio: str,
	              provider: Provider=Provider.SQLite ):
		self.provider = provider
		self.source = Source.StatusOfSuperfundSites
		self.bfy = bfy
		self.efy = efy
		self.rpiocode = super( ).code
		self.fields = [ 'SiteActivityId',
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
		                  'Expenditures' 
		                  'MainAccount',
		                  'TreasuryAccountCode',
		                  'TreasuryAccountName',
		                  'BudgetAccountCode',
		                  'BudgetAccountName' ]

	def __str__( self ):
		if self.__sitename is not None:
			return self.__sitename

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'bfy', 'efy', 'fund_code', 'fund_name', 'rpio_code', 'rpio_name',
		         'ah_code', 'ah_name', 'org_code', 'org_name', 'account_code',
		         'boc_code', 'boc_name', 'rc_code', 'rc_name',
		         'program_project_code', 'program_project_name', 'program_area_code',
		         'program_area_name', 'npm_code', 'npm_name', 'goal_code', 'goal_name',
		         'objective_code', 'objective_name', 'state_code', 'state_name', 'zip_code',
		         'county_name', 'city_name', 'site_id', 'site_name',
		         'budgeted', 'posted', 'open_commitments',
		         'obligations', 'deobligations', 'expenditures',
		         'main_account', 'treasury_account_code', 'treasury_account_name',
		         'budget_account_code', 'budget_account_name',
		         'data', 'fields',
		         'getdata', 'getframe' ]

	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'RpioCode' ]
			_values = ( self.bfy, self.rpiocode )
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'StatusOfSuperfundSites'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'StatusOfSuperfundSites'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class SpendingDocument( ):
	'''
    Constructor:
    SpendingDocument(  bfy: str, efy: str, fund: str, account: str,
                  boc: str, pvdr = Provider.SQLite )

    Purpose:
    Class defines object representing Spending documnets
    '''


	def __init__( self, bfy: str, efy: str, fund: str, account: str,
	              boc: str, provider: Provider=Provider.SQLite ):
		self.provider = provider
		self.source = Source.Obligations
		self.bfy = bfy
		self.efy = efy
		self.fundcode = fund
		self.accountcode = account
		self.boccode = boc
		self.fields = [ 'ObligationsId',
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
		                  'OpenCommitments',
		                  'Obligations',
		                  'UnliquidatedObligations',
		                  'Expenditures' ]

	def __str__( self ) -> float:
		if self.amount is not None:
			return self.amount

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'fields', 'data', 'frame', 'getdata', 'getframe' ]

	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'FundCode', 'AccountCode', 'BocCode' ]
			_values = ( self.bfy, self.fundcode, self.accountcode, self.boccode )
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'SpendingDocuments'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'SpendingDocuments'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class SupplementalCarryoverEstimate( ):
	'''

    Constructor:
    CarryoverEstimate( bfy: str, provider: Provider=Provider.SQLite )

    Purpose:
    Class defines object providing Supplemental Carryover Estimates

    '''


	def __init__( self, bfy: str, provider: Provider=Provider.SQLite ):
		self.provider = provider
		self.source = Source.SupplementalCarryoverEstimates
		self.bfy = bfy
		self.fields = [ 'CarryoverEstimatesId',
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
		                  'OpenCommitments',
		                  'UnobligatedAuthority' ]

	def __str__( self ) -> str:
		if self.rpiocode is not None:
			return self.rpiocode

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'fields', 'data', 'frame', 'getdata', 'getframe' ]

	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'EFY' ]
			_values = ( self.bfy, self.efy)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Reporting'
			_exc.cause = 'CarryoverEstimate'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Reporting'
			_exc.cause = 'CarryoverEstimate'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class SupplementalObligationEstimate( ):
	'''
    Constructor:
    CarryoverEstimate( bfy: str, provider: Provider=Provider.SQLite )

    Purpose:
    Class defines object providing Supplemental Carryover Estimate data for
    '''


	def __init__( self, bfy: str, provider: Provider=Provider.SQLite ):
		self.provider = provider
		self.source = Source.SupplementalCarryoverEstimates
		self.bfy = bfy
		self.fields = [ 'CarryoverEstimatesId',
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
		                  'OpenCommitments',
		                  'UnobligatedAuthority' ]

	def __str__( self ) -> str:
		if self.rpiocode is not None:
			return self.rpiocode

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'fields', 'data', 'frame', 'getdata', 'getframe' ]

	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'EFY' ]
			_values = ( self.bfy, self.efy)
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Reporting'
			_exc.cause = 'CarryoverEstimate'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Reporting'
			_exc.cause = 'CarryoverEstimate'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class TreasurySymbol( ):
	'''
    Constructor:
    TreasurySymbol( bfy: str, efy: str, treas: str, provider: Provider=Provider.SQLite )

    Purpose:
    Class defines object that represents a TAFS
    '''


	def __init__( self, bfy: str, efy: str, account: str,
	              provider: Provider=Provider.SQLite ):
		self.provider = provider
		self.__soruce = Source.FundSymbols
		self.bfy = bfy
		self.efy = efy
		self.treasuryaccountcode = account
		self.fields = [ 'TreasurySymbolsId',
		                  'BFY',
		                  'EFY',
		                  'FundCode',
		                  'FundName',
		                  'MainAccount',
		                  'TreasuryAccountCode',
		                  'TreasuryAccountName',
		                  'BudgetAccountCode',
		                  'BudgetAccountName',
		                  'ApportionmentAccountCode' ]

	def __str__( self ) -> str:
		if self.treasuryaccountname is not None:
			return self.treasuryaccountname

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'bfy', 'efy',
		         'main_account', 'treasury_account_code',
		         'treasury_account_name', 'budget_account_code',
		         'budget_account_name', 'fields', 'data',
		         'frame', 'getdata', 'getframe' ]

	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_source = self.source
			_provider = self.provider
			command = SQL.SELECTALL
			_names = [ 'BFY', 'EFY', 'TreasuryAccountCode' ]
			_values = ( self.bfy, self.efy, self.treasuryaccountcode )
			dbcfg = DbConfig( _source, _provider )
			sqlcfg = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( dbcfg, sqlcfg )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'TreasurySymbol'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'TreasurySymbol'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class Transfer( ):
	'''
     Constructor:
     Transfer( documentnumber: str, pvdr = Provider.SQLite )

     Purpose:
     Class defines object representing EPA reprogrammings
     '''


	def __init__( self, documentnumber: str, provider: Provider=Provider.SQLite ):
		self.provider = provider
		self.source = Source.Transfers
		self.documentnumber = documentnumber
		self.fields = [ 'TransfersId',
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

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'fields', 'data', 'frame', 'getdata', 'getframe' ]

	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_source = self.source
			command = SQL.SELECTALL
			_names = [ 'DocumentNumber', ]
			_values = ( self.documentnumber,)
			_dbconfig = DbConfig( _source )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Transfer'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'Transfer'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class TransType( ):
	'''
    Constructor:
    TransType( bfy: str, fundcode: str, pvdr = Provider.SQLite )

    Purpose:
    Class defines object representing trans types
    '''


	def __init__( self, bfy: str, fundcode: str, provider: Provider=Provider.SQLite ):
		self.provider = provider
		self.source = Source.TransTypes
		self.bfy = bfy
		self.fundcode = fundcode
		self.fields = [ 'TransTypesId',
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

	def __dir__( self ) -> list[ str ]:
		return [ 'id', 'fields', 'data', 'frame', 'getdata', 'getframe' ]

	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'FundCode' ]
			_values = ( self.bfy, self.fundcode )
			_dbconfig = DbConfig( _source, _provider )
			_sqlconfig = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_sql = SqlStatement( _dbconfig, _sqlconfig )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _sql.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'TransTypes'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''

        Purpose:  Method returning pandas dataframe
        comprised of datatable data


        Parameters:

        Returns:

        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'TransTypes'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class UnliquidatedObligation( ):
	'''
    Constructor:
    UnliquidatedObligation( bfy: str, fund: str, account: str, 
        boc: str, pvdr = Provider.SQLite )

    Purpose:
    Class defines object providing ULO data
    '''


	def __init__( self, bfy: str, efy: str, fund: str, account: str=None,
	              boc: str=None, provider: Provider=Provider.SQLite ):
		self.provider = provider
		self.source = Source.UnliquidatedObligations
		self.bfy = bfy
		self.fundcode = fund
		self.accountcode = account
		self.boccode = boc
		self.fields = [ 'UnliquidatedObligationsId'
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
		                  'OpenCommitments',
		                  'Obligations',
		                  'UnliquidatedObligations',
		                  'Expenditures' ]

	def __str__( self ) -> str:
		if self.amount is not None:
			return self.amount

	def __dir__( self ) -> list[ str ]:
		'''

		:return: a list[ str ] of object members

		'''
		return [ 'id', 'bfy', 'efy', 'fund_code', 'fund_name', 'rpio_code', 'rpio_name',
		         'ah_code', 'ah_name', 'org_code', 'org_name', 'account_code',
		         'boc_code', 'boc_name', 'rc_code', 'rc_name',
		         'program_project_code', 'program_project_name', 'program_area_code',
		         'program_area_name', 'npm_code', 'npm_name', 'goal_code', 'goal_name',
		         'objective_code', 'objective_name', 'document_type',
		         'document_number', 'document_control_number', 'rerference_document_number',
		         'last_activity_date', 'processed_date', 'age', 'vendor_code', 'vendor_name',
		         'foc_code', 'foc_name', 'amount',
		         'main_account', 'treasury_account_code', 'treasury_account_name',
		         'budget_account_code', 'budget_account_name',
		         'data', 'fields',
		         'getdata', 'getframe' ]

	def getdata( self ) -> list[ Row ]:
		'''

        :return: list[ Row ]

        :param: self

		:purpose:

        '''

		try:
			_source = self.source
			_provider = self.provider
			_names = [ 'BFY', 'FundCode', 'AccountCode', 'BocCode' ]
			_values = ( self.bfy, self.fundcode, self.accountcode, self.boccode )
			_dbcfg = DbConfig( _source, _provider )
			_sqlcfg = SqlConfig( _names, _values )
			_connection = Connection( self.source )
			_command = SqlStatement( _dbcfg, _sqlcfg )
			_sqlite = _connection.connect( )
			_cursor = _sqlite.cursor( )
			_query = _command.__getquerytext( )
			_db = _cursor.execute( _query )
			self.data = [ i for i in _db.fetchall( ) ]
			_cursor.close( )
			_sqlite.close( )
			return self.data
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'UnliquidatedObligations'
			_exc.method = 'getdata( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def getframe( self ) -> DataFrame:
		'''
        Purpose:

        Parameters:

        Returns:
        '''
		try:
			_source = self.source
			_data = BudgetData( _source )
			return _data.create_frame( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Ninja'
			_exc.cause = 'UnliquidatedObligations'
			_exc.method = 'getframe( self )'
			_err = ErrorDialog( _exc )
			_err.show( )
