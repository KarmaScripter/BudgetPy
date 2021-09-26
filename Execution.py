import datetime
import pandas as pd

class Account():
    '''defines the Account Code class'''
    __id = None
    __code = None
    __name = None
    __goal = None
    __objective = None
    __npm = None
    __programproject = None
    __data = None
    __dataframe = None

    @property
    def id( self ):
        if not self.__id < 0:
            return int( self.__id )
        else:
            return -1

    @property
    def code( self ):
        if self.__code:
            return str( self.__code )

    @property
    def name( self ):
        if self.__name:
            return str( self.__name )
        elif self.__programproject:
            return ProgramProject( self.__programproject ).name

    @property
    def goal( self ):
        if self.__goal is not None:
            return Goal( self.__goal )

    @property
    def objective( self ):
        if self.__objective is not None:
            return Objective( self.__objective )

    @property
    def npm( self ):
        if self.__npm is not None:
            return NationalProgram( self.__npm )

    @property
    def programproject( self ):
        if self.__programproject is not None:
            return ProgramProject( self.__programproject )

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @property
    def table( self ):
        if self.__dataframe is not None:
            return self.__dataframe

    def __init__( self, code, name = None, index = None ):
        self.__id = int( index )
        self.__code = str( code )
        self.__name = str( name )
        self.__goal = list( code )[ 0 ]
        self.__objective = str( list( code )[ 1:3 ] )
        self.__npm = list( code )[ 3 ]
        self.__programproject = str( list( code )[ 4:6 ] )
        self.__data = [ self.__id, self.__code, self.__name,
                 self.__programproject, self.__goal, self.__objective ]
        self.__dataframe = pd.DataFrame

    def __str__( self ):
        if self.__code is not None:
            return self.__code

class Activity():
    '''Defines the Activity Class'''
    __id = None
    __code = None
    __name = None
    __data = None
    __dataframe = None

    @property
    def id( self ):
        if self.__id is not None:
            return self.__id
        else:
            return -1

    @property
    def code( self ):
        if self.__code is not None:
            return self.__code
        else:
            return 'NS'

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name
        else:
            return 'NS'

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @property
    def table( self ):
        if self.__dataframe is not None:
            return self.__dataframe

    def __init__( self, code, name = None, index = None ):
        self.__id = int( index )
        self.__code = str( code )
        self.__name = str( name )
        self.__data = [ self.__id, self.__code, self.__name ]
        self.__dataframe = pd.DataFrame

    def __str__( self ):
        return self.__code

class AllowanceHolder():
    '''Defines the AllowanceHolder Class'''
    __id = None
    __code = None
    __name = None
    __data = None
    __dataframe = None

    @property
    def id( self ):
        if self.__id is not None:
            return self.__id

    @property
    def code( self ):
        if not self.__code == '':
            return self.__code

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @property
    def table( self ):
        if self.__dataframe is not None:
            return self.__dataframe

    def __init__( self, code, name = None, index = None ):
        self.__id = int( index )
        self.__code = code
        self.__name = name
        self.__data = [ self.__id, self.__code, self.__name ]
        self.__dataframe = pd.DataFrame

    def __str__( self ):
        if self.__code is not None:
            return self.__code

class Appropriation():
    '''Defines the Appropriation Class'''
    __id = None
    __code = None
    __name = None
    __title = None
    __bfy = None

    @property
    def id( self ):
        if self.__id > 0:
            return self.__id
        else:
            return -1

    @property
    def code( self ):
        if self.__code is not None:
            return self.__code
        else:
            return 'NS'

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name
        else:
            return 'NS'

    @property
    def fiscalyear( self ):
        if self.__bfy is not None:
            return self.__bfy
        else:
            return 'NS'

    @property
    def title( self ):
        if self.__title is not None:
            return self.__title
        else:
            return 'NS'

    @property
    def data( self ):
        return [ self.__id, self.__code, self.__name,
                 self.__bfy, self.__title ]

    def __init__( self, code, name = None,
                  bfy = None, title = None,
                  index = None ):
        self.__id = int( index )
        self.__code = str( code )
        self.__bfy = str( bfy )
        self.__name = str( name )
        self.__title = str( title )

    def __str__( self ):
        return self.__code

class BudgetFiscalYear():
    '''Class to describe the federal fiscal year'''
    __id = None
    __base = None
    __beginyear = None
    __endyear = None
    __today = None
    __date = None
    __startdate = None
    __enddate = None
    __expiration = None
    __weekends = 0
    __workdays = 0
    __year = None
    __month = ''
    __day = ''
    __holidays = { }
    __data = None
    __dataframe = None

    @property
    def id( self ):
        if self.__id is not None:
            return int( self.__id )

    @property
    def beginyear( self ):
        if self.__base is not None:
            return self.__beginyear

    @property
    def endyear( self ):
        if self.__endyear is not None:
            return self.__endyear

    @property
    def calendaryear( self ):
        if self.__year:
            return str( self.__year )

    @property
    def startdate( self ):
        if isinstance( self.__startdate, datetime.datetime ):
            return datetime.date( self.__startdate.year, self.__startdate.month,
                self.__startdate.day )

    @property
    def enddate( self ):
        if isinstance( self.__enddate, datetime.datetime ):
            return datetime.datetime( self.__enddate.year, self.__enddate.month,
                self.__enddate.day )

    @property
    def expiration( self ):
        if isinstance( self.__expiration, datetime.datetime ):
            return datetime.datetime( self.__expiration.year, self.__expiration.month,
                self.__expiration.day )

    @property
    def weekends( self ):
        if self.__weekends is not None:
            return self.__weekends

    @property
    def workdays( self ):
        if self.__workdays is not None:
            return float( self.__workdays )

    @property
    def date( self ):
        if isinstance( self.__date, datetime.datetime):
            return datetime.date( self.__date.year, self.__month,
                self.__date.day )

    @property
    def day( self ):
        if self.__day is not None:
            return str( self.__day )

    @property
    def month( self ):
        if self.__month is not None:
            return str( self.__month )

    @property
    def holidays( self ):
        if self.__holidays is not None:
            return self.__holidays

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @property
    def table( self ):
        if self.__dataframe is not None:
            return self.__dataframe

    def __init__( self, bfy, efy = None,
                  index = None ):
        self.__today = datetime.date.today()
        self.__id = index
        self.__base = str( bfy )
        self.__date = datetime.date
        self.__year = int( bfy )
        self.__startdate = datetime.date( self.__year, 10, 1 )
        self.__enddate = datetime.date( ( self.__year + 1 ), 9, 30 )
        self.__day = self.__today.day
        self.__month = self.__today.month
        self.__beginyear = self.__year
        self.__endyear = int( efy )
        self.__data = [ self.__id, self.__year, self.__month,
                        self.__day, self.__startdate, self.__enddate ]
        self.__dataframe = pd.DataFrame

    def __str__( self ):
        return str( self.__year )

class BudgetObjectClass():
    '''Defines the BudgetObjectClass Class'''
    __code = None
    __name = None
    __value = None
    __data = None
    __dataframe = None

    @property
    def code( self ):
        if self.__code is not None:
            return self.__code

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    @property
    def value( self ):
        if self.__value is not None:
            return self.__value

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @property
    def table( self ):
        if self.__dataframe is not None:
            return self.__dataframe

    def __init__( self, code, name = None, value = None ):
        self.__code = code
        self.__name = name
        self.__value = value
        self.__data = [ self.__code, self.__name, self.__value ]
        self.__dataframe = pd.DataFrame

    def __str__( self ):
        return self.__code

class Division():
    '''Defines the Division Class'''
    __code = None
    __name = None

    @property
    def code( self ):
        if self.__code is not None:
            return self.__code

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    def __init__( self, code, name = None ):
        self.__code = code
        self.__name = name

    def __str__( self ):
        return self.__code

class FinanceObjectClass():
    '''Defines the FinanceObjectClass Class'''
    __code = None
    __name = None
    __data = None
    __dataframe = None

    @property
    def code( self ):
        if self.__code is not None:
            return self.__code

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @property
    def table( self ):
        if self.__dataframe is not None:
            return self.__dataframe

    def __init__( self, code, name = None ):
        self.__code = code
        self.__name = name
        self.__data = [ self.__code, self.__name ]
        self.__dataframe = pd.DataFrame

    def __str__( self ):
        return self.__code

class Fund():
    '''Defines the Fund Class'''
    __code = None
    __name = None
    __title = None
    __data = None
    __dataframe = None

    @property
    def code( self ):
        if self.__code is not None:
            return self.__code

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    @property
    def title( self ):
        if self.__title is not None:
            return self.__title

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @property
    def table( self ):
        if self.__dataframe is not None:
            return self.__dataframe

    def __init__( self, code, name = None,
                  title = None ):
        self.__code = code
        self.__name = name
        self.__title = title
        self.__data = [ self.__code, self.__name, self.__title ]
        self.__dataframe = pd.DataFrame

    def __str__( self ):
        return self.__code

class Goal():
    '''Defines the Goal Class'''
    __code = None
    __name = None
    __data = None

    @property
    def code( self ):
        if not self.__code == '':
            return self.__code

    @property
    def name( self ):
        if not self.__name == '':
            return self.__name

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    def __init__( self, code, name = None ):
        self.__code = code
        self.__name = name
        self.__data = [ self.__code, self.__name ]

    def __str__( self ):
        return self.__code

class NationalProgram():
    '''Defines the NationalProgram Class'''
    __code = None
    __name = None
    __rpio = None
    __title = None
    __data = None
    __dataframe = None

    @property
    def code( self ):
        if not self.__code == '':
            return self.__code

    @property
    def name( self ):
        if not self.__name == '':
            return self.__name

    @property
    def rpio( self ):
        if self.__rpio is not None:
            return self.__rpio

    @property
    def title( self ):
        if self.__title is not None:
            return self.__title

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @property
    def table( self ):
        if self.__dataframe is not None:
            return self.__dataframe

    def __init__( self, code, name = None,
                 rpio = None, title = None):
        self.__code = code
        self.__name = name
        self.__rpio = rpio
        self.__title = title
        self.__data = [ self.__code, self.__name, self.__rpio,
                        self.__rpio, self.__title ]
        self.__dataframe = pd.DataFrame

    def __str__( self ):
        return self.__code

class Objective():
    '''Defines the Objective Class'''
    __code = None
    __name = None
    __data = None

    @property
    def code( self ):
        if not self.__code == '':
            return self.__code

    @property
    def name( self ):
        if not self.__name == '':
            return self.__name

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    def __init__( self, code, name = '' ):
        self.__code = code
        self.__name = name
        self.__data = [ self.__code, self.__name ]

    def __str__( self ):
        return self.__code

class Organization():
    '''Defines the Organization Class'''
    __code = None
    __name = None
    __data = None
    __dataframe = None

    @property
    def code( self ):
        if self.__code is not None:
            return str( self.__code )

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @property
    def table( self ):
        if self.__dataframe is not None:
            return self.__dataframe

    def __init__( self, code, name = '' ):
        self.__code = code
        self.__name = name
        self.__data = [ self.__code, self.__name ]
        self.__dataframe = pd.DataFrame

    def __str__( self ):
        return self.__code

class Project():
    '''Defines the Organization Class'''
    __code = None
    __name = None
    __data = None
    __dataframe = None

    @property
    def code( self ):
        if self.__code is not None:
            return self.__code

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @property
    def table( self ):
        if self.__dataframe is not None:
            return self.__dataframe

    def __init__( self, code, name = '' ):
        self.__code = code
        self.__name = name
        self.__data = [ self.__code, self.__name ]
        self.__dataframe = pd.DataFrame

    def __str__( self ):
        if self.__code:
            return self.__code

class ItProjectCode():
    '''Defines the Organization Class'''
    __code = None
    __name = None
    __data = None
    __dataframe = None

    @property
    def code( self ):
        if self.__code is not None:
            return self.__code

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @property
    def table( self ):
        if self.__dataframe is not None:
            return self.__dataframe

    def __init__( self, code, name = '' ):
        self.__code = code
        self.__name = name
        self.__data = [ self.__code, self.__name ]
        self.__dataframe = pd.DataFrame

    def __str__( self ):
        return self.__code

class SiteProjectCode():
    '''Defines the Organization Class'''
    __code = None
    __name = None
    __data = None
    __dataframe = None

    @property
    def code( self ):
        if self.__code is not None:
            return self.__code

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @property
    def table( self ):
        if self.__dataframe is not None:
            return self.__dataframe

    def __init__( self, code, name = '' ):
        self.__code = code
        self.__name = name
        self.__data = [ self.__code, self.__name ]
        self.__dataframe = pd.DataFrame

    def __str__( self ):
        return self.__code

class HumanResourceOrganization():
    '''Defines the Organization Class'''
    __code = None
    __name = None
    __data = None
    __dataframe = None

    @property
    def code( self ):
        if self.__code is not None:
            return self.__code

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @property
    def table( self ):
        if self.__dataframe is not None:
            return self.__dataframe

    def __init__( self, code, name = '' ):
        self.__code = code
        self.__name = name
        self.__data = [ self.__code, self.__name ]
        self.__dataframe = pd.DataFrame

    def __str__( self ):
        return self.__code

class WorkCode():
    '''Defines the Organization Class'''
    __code = None
    __name = None
    __data = None
    __dataframe = None

    @property
    def code( self ):
        if self.__code is not None:
            return self.__code

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @property
    def table( self ):
        if self.__dataframe is not None:
            return self.__dataframe

    def __init__( self, code, name = '' ):
        self.__code = code
        self.__name = name
        self.__data = [ self.__code, self.__name ]
        self.__dataframe = pd.DataFrame

    def __str__( self ):
        return self.__code

class ProgramArea():
    '''defines the ProgramArea class'''
    __code = None
    __name = None
    __data = None
    __dataframe = None

    @property
    def code( self ):
        if self.__code is not None:
            return self.__code

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @property
    def table( self ):
        if self.__dataframe is not None:
            return self.__dataframe

    def __init__( self, code, name = '' ):
        self.__code = code
        self.__name = name
        self.__data = [ self.__code, self.__name ]
        self.__dataframe = pd.DataFrame

    def __str__( self ):
        return self.__code

class ProgramProject():
    '''Defines the ProgramProject Class'''
    __code = None
    __name = None
    __description = None
    __data = None
    __dataframe = None

    @property
    def code( self ):
        if self.__code is not None:
            return self.__code

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @property
    def table( self ):
        if self.__dataframe is not None:
            return self.__dataframe

    def __init__( self, code, name = None,
                  description = None ):
        self.__code = str( code )
        self.__name = str( name )
        self.__description = str( description )
        self.__data = [ self.__code, self.__name, self.__description ]
        self.__dataframe = pd.DataFrame

    def __str__( self ):
        return self.__code

class ResponsibilityCenter():
    '''Defines the ResponsibilityCenter Class'''
    __code = None
    __name = None
    __data = None
    __dataframe = None

    @property
    def code( self ):
        if self.__code is not None:
            return self.__code

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @property
    def table( self ):
        if self.__dataframe is not None:
            return self.__dataframe

    def __init__( self, code, name = '' ):
        self.__code = code
        self.__name = name
        self.__data = [ self.__code, self.__name ]
        self.__dataframe = pd.DataFrame

    def __str__( self ):
        return self.__code

class ResourcePlanningImplementationOffice():
    '''defines the ResponsiblePlanningOffice class'''
    __code = None
    __name = None
    __data = None
    __dataframe = None

    @property
    def code( self ):
        if self.__code is not None:
            return self.__code

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @property
    def table( self ):
        if self.__dataframe is not None:
            return self.__dataframe

    def __init__( self, code, name = '' ):
        self.__code = code
        self.__name = name
        self.__data = [ self.__code, self.__name ]
        self.__dataframe = pd.DataFrame

    def __str__( self ):
        return self.__code

class ProgramResultsCode():
    '''Defines the PRC class'''
    __id = None
    __rpio = None
    __bfy = None
    __ah = None
    __fund = None
    __org = None
    __account = None
    __activity = None
    __rc = None
    __boc = None
    __amount = None
    __data = None
    __dataframe = None

    @property
    def id( self ):
        if self.__id is not None:
            return self.__id

    @property
    def rpio( self ):
        if self.__rpio is not None:
            return self.__rpio

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return BudgetFiscalYear( self.__bfy )

    @property
    def fund( self ):
        if self.__fund.code is not None:
            return Fund( self.__fund.code )

    @property
    def ah( self ):
        if self.__ah is not None:
            return AllowanceHolder( self.__ah )

    @property
    def account( self ):
        if self.__account is not None:
            return self.__account

    @property
    def activity( self ):
        if self.__account is not None:
            self.__activity = str( self.__account[ 5:2 ] )
            return Activity( self.__activity )

    @property
    def org( self ):
        if self.__org is not None:
            return Organization( self.__org )

    @property
    def rc( self ):
        if self.__rc is not None:
            return ResponsibilityCenter( self.__rc )

    @property
    def boc( self ):
        if self.__boc is not None:
            return BudgetObjectClass( self.__boc )

    @property
    def amount( self ):
        if self.__amount is not None:
            return self.__amount

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @property
    def table( self ):
        if self.__dataframe is not None:
            return self.__dataframe

    def __init__( self, code, rpio = None, bfy = None,
                  ah = None, fund = None,
                  boc = None, org = None,
                  amount = 0 ):
        '''Initializes the PRC class'''

        self.__rpio = ResourcePlanningImplementationOffice( rpio )
        self.__bfy = BudgetFiscalYear( bfy )
        self.__ah = AllowanceHolder( ah )
        self.__fund = Fund( fund )
        self.__account = Account( code )
        self.__org = Organization( org )
        self.__boc = BudgetObjectClass( boc )
        self.__amount = amount
        self.__data = [ self.__rpio.code, self.__bfy.beginyear, self.__ah.code,
                        self.__fund.code, self.__account.code, self.__org.code,
                        self.__boc.code, self.__amount ]
        self.__dataframe = pd.DataFrame

    def __str__( self ):
        if self.__account.code is not None:
            return self.__account.code

class RegionalOffice():
    '''Defines a regional RPIO'''
    __rpio = None
    __name = None
    __data = None
    __dataframe = None

    @property
    def rpio( self ):
        if self.__rpio is not None:
            return self.__rpio

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @property
    def table( self ):
        if self.__dataframe is not None:
            return self.__dataframe

    def __init__( self, rpio ):
        self.__rpio = ResourcePlanningImplementationOffice( str( rpio ) )
        self.__name = self.__rpio.name
        self.__data = [ self.__rpio, self.__name ]
        self.__dataframe = pd.DataFrame

    def __str__(self):
        if self.__rpio is not None:
            return str( self.__rpio )

class HeadQuartersOffice():
    '''Defines the HQ class'''
    __rpio = None
    __name = None
    __title = None
    __data = None
    __dataframe = None

    @property
    def rpio( self ):
        if self.__rpio is not None:
            return self.__rpio

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    @property
    def title( self ):
        if self.__title is not None:
            return self.__title

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @property
    def table( self ):
        if self.__dataframe is not None:
            return self.__dataframe

    def __init__( self, rpio, name = None,
                  title = None):
        self.__rpio = rpio
        self.__name = name
        self.__title = title
        self.__data = [ self.__rpio, self.__name, self.__title ]
        self.__dataframe = pd.DataFrame

    def __str__( self ):
        if self.__name is not None:
            return str( self.__name )

class Holiday():
    '''Defines the Holiday class'''
    __bfy = None
    __name = None
    __date = None
    __day = None
    __data = None
    __dataframe = None

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return self.__bfy

    @property
    def date( self ):
        if self.__date is not None:
            return self.__date

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    @property
    def day( self ):
        if self.__day is not None:
            return self.__day

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @property
    def table( self ):
        if self.__dataframe is not None:
            return self.__dataframe

    def __init__( self, bfy, date = None,
                  name = None, day = None ):
        self.__bfy = bfy
        self.__name = name
        self.__day = day
        self.__date = date
        self.__data = [ self.__bfy, self.__name, self.__date,
                        self.__day ]
        self.__dataframe = pd.DataFrame

    def __str__(self):
        if self.__name is not None:
            return str( self.__name )

class Commitment:
    '''Defines the commitment class.'''
    __amount = None
    __account = None
    __document = None
    __bfy = None
    __fund = None
    __org = None
    __boc = None
    __data = None
    __dataframe = None

    @property
    def amount( self ):
        if self.__amount is not None:
            return self.__amount

    @property
    def account( self ):
        if self.__account is not None:
            return Account( self.__account )

    @property
    def document( self ):
        if self.__document is not None:
            return self.__document

    @property
    def org( self ):
        if self.__org is not None:
            return Organization( self.__org )

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return BudgetFiscalYear( self.__bfy )

    @property
    def fund( self ):
        if self.__fund is not None:
            return Fund( self.__fund )

    @property
    def boc( self ):
        if self.__boc is not None:
            return BudgetObjectClass( self.__boc )

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @property
    def table( self ):
        if self.__dataframe is not None:
            return self.__dataframe

    def __init__(self, amount, account = None,
                 document = None, bfy = None,
                 org = None, boc = None):
        self.__amount = amount
        self.__account = account
        self.__document = document
        self.__boc = boc
        self.__org = org
        self.__bfy = bfy
        self.__data = [ self.__amount, self.__account, self.__document,
                        self.__boc.code, self.__bfy.beginyear, self.__org.code ]
        self.__dataframe = pd.DataFrame

    def __str__( self ):
        if self.__amount is not None:
            return str( self.__amount )

class OpenCommitment:
    '''Defines the commitment class.'''
    __amount = None
    __account = None
    __document = None
    __bfy = None
    __fund = None
    __org = None
    __boc = None
    __data = None
    __dataframe = None

    @property
    def amount( self ):
        if self.__amount is not None:
            return self.__amount

    @property
    def account( self ):
        if self.__account is not None:
            return Account( self.__account )

    @property
    def document( self ):
        if self.__document is not None:
            return self.__document

    @property
    def org( self ):
        if self.__org is not None:
            return Organization( self.__org )

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return BudgetFiscalYear( self.__bfy )

    @property
    def fund( self ):
        if self.__fund is not None:
            return Fund( self.__fund )

    @property
    def boc( self ):
        if self.__boc is not None:
            return BudgetObjectClass( self.__boc )

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @property
    def table( self ):
        if self.__dataframe is not None:
            return self.__dataframe

    def __init__( self, amount, account = None,
                  doc = None, bfy = None,
                  org = None, boc = None ):
        self.__amount = float( amount )
        self.__account = str( account )
        self.__document = str( doc )
        self.__boc = boc
        self.__org = org
        self.__bfy = bfy
        self.__data = [ self.__amount, self.__account, self.__document,
                        self.__boc.code, self.__org.code, self.__bfy.beginyear ]
        self.__dataframe = pd.DataFrame

    def __str__( self ):
        if self.__amount is not None:
            return str( self.__amount )

class Obligation:
    '''Defines the commitment class.'''
    __amount = None
    __account = None
    __document = None
    __bfy = None
    __fund = None
    __org = None
    __boc = None
    __data = None
    __dataframe = None

    @property
    def amount( self ):
        if self.__amount is not None:
            return self.__amount

    @property
    def account( self ):
        if self.__account is not None:
            return Account( self.__account )

    @property
    def dcn( self ):
        if self.__document is not None:
            return self.__document

    @property
    def org( self ):
        if self.__org is not None:
            return Organization( self.__org )

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return BudgetFiscalYear( self.__bfy )

    @property
    def fund( self ):
        if self.__fund is not None:
            return Fund( self.__fund )

    @property
    def boc( self ):
        if self.__boc is not None:
            return BudgetObjectClass( self.__boc )

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @property
    def table( self ):
        if self.__dataframe is not None:
            return self.__dataframe

    def __init__( self, amount, account = None,
                  dcn = None, bfy = None,
                  org = None, boc = None ):
        self.__amount = amount
        self.__account = account
        self.__document = dcn
        self.__boc = boc
        self.__org = org
        self.__bfy = bfy

    def __str__( self ):
        if self.__amount is not None:
            return str( self.__amount )

class Deobligation:
    '''Defines the commitment class.'''
    __amount = None
    __account = None
    __document = None
    __bfy = None
    __fund = None
    __org = None
    __boc = None
    __data = None
    __dataframe = None

    @property
    def amount( self ):
        if self.__amount is not None:
            return self.__amount

    @property
    def account( self ):
        if self.__account is not None:
            return Account( self.__account )

    @property
    def dcn( self ):
        if self.__document is not None:
            return self.__document

    @property
    def org( self ):
        if self.__org is not None:
            return Organization( self.__org )

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return BudgetFiscalYear( self.__bfy )

    @property
    def fund( self ):
        if self.__fund is not None:
            return Fund( self.__fund )

    @property
    def boc( self ):
        if self.__boc is not None:
            return BudgetObjectClass( self.__boc )

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @property
    def table( self ):
        if self.__dataframe is not None:
            return self.__dataframe

    def __init__( self, amount, account = None,
                  dcn = None, bfy = None,
                  org = None, boc = None ):
        self.__amount = amount
        self.__account = account
        self.__document = dcn
        self.__boc = boc
        self.__org = org
        self.__bfy = bfy
        self.__data = [ self.__amount, self.__account, self.__document,
                        self.__bfy, self.__org ]
        self.__dataframe = pd.DataFrame

    def __str__( self ):
        if self.__amount is not None:
            return str( self.__amount )

class ULO:
    '''Defines the commitment class.'''
    __amount = None
    __account = None
    __document = None
    __bfy = None
    __fund = None
    __org = None
    __boc = None
    __data = None
    __dataframe = None

    @property
    def amount( self ):
        if self.__amount is not None:
            return self.__amount

    @property
    def account( self ):
        if self.__account is not None:
            return Account( self.__account )

    @property
    def dcn( self ):
        if self.__document is not None:
            return self.__document

    @property
    def org( self ):
        if self.__org is not None:
            return Organization( self.__org )

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return BudgetFiscalYear( self.__bfy )

    @property
    def fund( self ):
        if self.__fund is not None:
            return Fund( self.__fund )

    @property
    def boc( self ):
        if self.__boc is not None:
            return BudgetObjectClass( self.__boc )

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @property
    def table( self ):
        if self.__dataframe is not None:
            return self.__dataframe

    def __init__( self, amount, account = None,
                  dcn = None, bfy = None,
                  org = None, boc = None ):
        self.__amount = amount
        self.__account = account
        self.__document = dcn
        self.__boc = boc
        self.__org = org
        self.__bfy = bfy
        self.__data = [ self.__amount, self.__account, self.__document,
                        self.__boc, self.__org, self.__bfy ]
        self.__dataframe = pd.DataFrame

    def __str__( self ):
        if self.__amount is not None:
            return str( self.__amount )

class Expenditure:
    '''Defines the commitment class.'''
    __amount = None
    __account = None
    __document = None
    __bfy = None
    __fund = None
    __org = None
    __boc = None
    __data = None
    __dataframe = None

    @property
    def amount( self ):
        if self.__amount is not None:
            return self.__amount

    @property
    def account( self ):
        if self.__account is not None:
            return Account( self.__account )

    @property
    def dcn( self ):
        if self.__document is not None:
            return self.__document

    @property
    def org( self ):
        if self.__org is not None:
            return Organization( self.__org )

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return BudgetFiscalYear( self.__bfy )

    @property
    def fund( self ):
        if self.__fund is not None:
            return Fund( self.__fund )

    @property
    def boc( self ):
        if self.__boc is not None:
            return BudgetObjectClass( self.__boc )

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @property
    def table( self ):
        if self.__dataframe is not None:
            return self.__dataframe

    def __init__( self, amount, account = None,
                  dcn = None, bfy = None,
                  org = None, boc = None ):
        self.__amount = amount
        self.__account = account
        self.__document = dcn
        self.__boc = boc
        self.__org = org
        self.__bfy = bfy
        self.__data = [ self.__amount, self.__account, self.__document,
                        self.__boc, self.__org, self.__bfy ]
        self.__dataframe = pd.DataFrame

    def __str__( self ):
        if self.__amount is not None:
            return str( self.__amount )