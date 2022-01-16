import datetime as dt
import pandas as pd
import sqlite3 as sl

class Account():
    '''defines the Account Code class'''
    __code = ''
    __name = ''
    __goal = ''
    __objective = ''
    __npm = ''
    __programproject = ''
    __data = None
    __dataframe = None

    @property
    def code( self ):
        if self.__code:
            return self.__code

    @code.setter
    def code( self, code ):
        if not code == '':
            self.__code = code
            self.__data[ 'code' ] = code

    @property
    def name( self ):
        if self.__name:
            return self.__name

    @name.setter
    def name( self, name ):
        if not name == '':
            self.__name = name
            self.__data[ 'name' ] = name

    @property
    def goal( self ):
        if self.__goal is not None:
            return self.__goal

    @goal.setter
    def goal( self, goal ):
        if goal is not None:
            self.__goal = str( goal )
            self.__data[ 'goal' ] = self.__goal

    @property
    def objective( self ):
        if self.__objective is not None:
            return self.__objective

    @objective.setter
    def objective( self, obj ):
        if obj is not None:
            self.__objective = str( obj )
            self.__data[ 'objective' ] = self.__objective

    @property
    def npm( self ):
        if self.__npm is not None:
            return self.__npm

    @npm.setter
    def npm( self, code ):
        if not code == '':
            self.__npm = code
            self.__data[ 'npm' ] = self.__npm

    @property
    def programproject( self ):
        if self.__programproject is not None:
            return self.__programproject

    @programproject.setter
    def programproject( self, code ):
        if not code == '':
            self.__programproject = code
            self.__data[ 'programproject' ] = self.__programproject

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @property
    def table( self ):
        if self.__dataframe is not None:
            return self.__dataframe

    def __init__( self, code ):
        self.__data = { }
        self.__code = code
        self.__goal = str( self.__code[ 0 ] )
        self.__objective = str( self.__code[ 1:3 ] )
        self.__npm = str( self.__code[ 3 ] )
        self.__programproject = str( self.__code[ 4:6 ] )
        self.__dataframe = pd.DataFrame

    def __str__( self ):
        if not self.__code == '':
            return self.__code

class Activity():
    '''Defines the Activity Class'''
    __code = ''
    __name = ''
    __data = None
    __dataframe = None

    @property
    def code( self ):
        if not self.__code == '':
            return self.__code

    @code.setter
    def code( self, code ):
        if not code == '':
            self.__code = code
            self.__data[ 'code' ] = code

    @property
    def name( self ):
        if not self.__name == '':
            return self.__name

    @name.setter
    def name( self, name ):
        if not name == '':
            self.__name = name
            self.__data[ 'name' ] = name

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, src ):
        if isinstance( src, pd.DataFrame ):
            self.__data = src

    @property
    def table( self ):
        if self.__dataframe is not None:
            return self.__dataframe

    def __init__( self, code ):
        self.__data = { }
        self.__code = code
        self.__dataframe = pd.DataFrame

    def __str__( self ):
        return self.__code

class AllowanceHolder():
    '''Defines the AllowanceHolder Class'''
    __code = ''
    __name = ''
    __data = None
    __dataframe = None

    @property
    def code( self ):
        if not self.__code == '':
            return self.__code

    @code.setter
    def code( self, code ):
        if not code == '':
            self.__code = code
            self.__data[ 'code' ] = code

    @property
    def name( self ):
        if not self.__name == '':
            return self.__name

    @name.setter
    def name( self, name ):
        if not name == '':
            self.__name = name
            self.__data[ 'name' ] = name

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, src ):
        if isinstance( src, pd.DataFrame ):
            self.__data = src

    @property
    def table( self ):
        if self.__dataframe is not None:
            return self.__dataframe

    def __init__( self, code ):
        self.__data = { }
        self.__code = code
        self.__dataframe = pd.DataFrame

    def __str__( self ):
        if not self.__code == '':
            return self.__code

class Appropriation():
    '''Defines the Appropriation Class'''
    __fund = None
    __code = ''
    __name = ''
    __title = None
    __bfy = None
    __data = None
    __dataframe = None

    @property
    def code( self ):
        if not self.__code == '':
            return self.__code

    @code.setter
    def code( self, code ):
        if not code == '':
            self.__code = code

    @property
    def name( self ):
        if not self.__name == '':
            return self.__name

    @name.setter
    def name( self, name ):
        if not name == '':
            self.__name = name
            self.__data[ 'name' ] = name

    @property
    def fiscalyear( self ):
        if self.__bfy is not None:
            return self.__bfy

    @fiscalyear.setter
    def fiscalyear( self, bfy ):
        if bfy is not None:
            self.__bfy = str( bfy )
            self.__data[ 'bfy' ] = self.__bfy

    @property
    def fund( self ):
        if self.__fund is not None:
            return self.__fund

    @fund.setter
    def fund( self, code ):
        if not code == '':
            self.__fund = Fund( code )
            self.__data[ 'fund' ] = self.__fund

    @property
    def title( self ):
        if self.__title is not None:
            return self.__title

    @title.setter
    def title( self, title ):
        if title is not None:
            self.__title = str( title )
            self.__data[ 'title' ] = self.__title

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, src ):
        if isinstance( src, pd.DataFrame ):
            self.__data = src

    @property
    def table( self ):
        if self.__dataframe is not None:
            return self.__dataframe

    def __init__( self, code ):
        self.__code = code
        self.__fund = Fund( self.__code )
        self.__data = { 'code': self.__code,
                        'fund': self.__fund }

    def __str__( self ):
        return self.__code

class BudgetFiscalYear():
    '''Class to describe the federal fiscal year'''
    __base = ''
    __bfy = ''
    __efy = ''
    __today = None
    __date = None
    __startdate = None
    __enddate = None
    __expiration = None
    __weekends = 0
    __workdays = 0
    __year = None
    __month = None
    __day = None
    __holidays = None
    __data = None
    __dataframe = None

    @property
    def firstyear( self ):
        if not self.__bfy == '':
            return self.__bfy

    @firstyear.setter
    def firstyear( self, yr ):
        if not yr == '':
            self.__bfy = yr
            self.__data[ 'firstyear' ] = yr

    @property
    def lastyear( self ):
        if not self.__efy == '':
            return self.__efy

    @lastyear.setter
    def lastyear( self, yr ):
        if not yr == '':
            self.__efy = yr
            self.__data[ 'lastyear' ] = yr

    @property
    def calendaryear( self ):
        if not self.__year == '':
            return self.__year

    @calendaryear.setter
    def calendaryear( self, yr ):
        if not yr == '':
            self.__year = yr
            self.__data[ 'calendaryear' ] = yr

    @property
    def startdate( self ):
        if isinstance( self.__startdate, dt.date ):
            return self.__startdate

    @startdate.setter
    def startdate( self, start ):
        if isinstance( start, dt.date ):
            self.__startdate = start
            self.__data[ 'startdate' ] = self.__startdate

    @property
    def enddate( self ):
        if isinstance( self.__enddate, dt.date ):
            return self.__enddate

    @enddate.setter
    def enddate( self, end ):
        if isinstance( end, dt.date ):
            self.__enddate = end
            self.__data[ 'enddate' ] = self.__enddate

    @property
    def expiration( self ):
        if isinstance( self.__expiration, dt.date ):
            return self.__expiration

    @expiration.setter
    def expiration( self, exp ):
        if isinstance( exp, dt.date ):
            self.__expiration = exp
            self.__data[ 'expiration' ] = self.__expiration

    @property
    def weekends( self ):
        if self.__weekends > 0:
            return self.__weekends

    @weekends.setter
    def weekends( self, end ):
        if isinstance( end, int ) and end > 0:
            self.__weekends = end
            self.__data[ 'weekends' ] = end

    @property
    def workdays( self ):
        if self.__workdays > 0:
            return self.__workdays

    @workdays.setter
    def workdays( self, work ):
        if isinstance( work, int ) and work > 0:
            self.__workdays = work
            self.__data[ 'workdays' ] = work

    @property
    def date( self ):
        if isinstance( self.__date, dt.date ):
            return self.__date

    @date.setter
    def date( self, today ):
        if isinstance( today, dt.date ):
            self.__date = today
            self.__data[ 'date' ] = self.__date

    @property
    def day( self ):
        if self.__day is not None:
            return self.__day

    @day.setter
    def day( self, today ):
        if isinstance( today, dt.date ):
            self.__day = today
            self.__data[ 'day' ] = self.__day

    @property
    def month( self ):
        if self.__month is not None:
            return self.__month

    @property
    def holidays( self ):
        if self.__holidays is not None:
            return self.__holidays

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, src ):
        if isinstance( src, pd.DataFrame ):
            self.__data = src

    @property
    def table( self ):
        if self.__dataframe is not None:
            return self.__dataframe

    def __init__( self, bfy ):
        self.__today = dt.date.today()
        self.__base = str( bfy )
        self.__date = self.__today
        self.__year = int( self.__base )
        self.__day = self.__date.day
        self.__month = self.__date.month
        self.__startdate = dt.date( self.__year, 10, 1 )
        self.__bfy = str( self.__startdate.year )
        self.__enddate = dt.date( self.__year + 1, 9, 30 )
        self.__efy = str( self.__enddate.year )
        self.__data = { 'base': self.__base,
                        'date': self.__date,
                        'calendaryear': self.__year,
                        'day': self.__day,
                        'month': self.__month,
                        'startdate': self.__startdate,
                        'enddate': self.__enddate }
        self.__dataframe = pd.DataFrame

    def __str__( self ):
        return str( self.__year )

class BudgetObjectClass():
    '''Defines the BudgetObjectClass Class'''
    __code = ''
    __name = ''
    __value = None
    __data = None
    __dataframe = None

    @property
    def code( self ):
        if not self.__code == '':
            return self.__code

    @code.setter
    def code( self, code ):
        if not code == '':
            self.__code = code
            self.__data[ 'code' ] = code

    @property
    def name( self ):
        if not self.__name == '':
            return self.__name

    @name.setter
    def name( self, name ):
        if not name == '':
            self.__name = name
            self.__data[ 'name' ] = name

    @property
    def value( self ):
        if self.__value is not None:
            return self.__value

    @value.setter
    def value( self, val ):
        if val is not None:
            self.__value = str( val )
            self.__data[ 'value' ] = self.__value

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, src ):
        if isinstance( src, pd.DataFrame ):
            self.__data = src

    @property
    def table( self ):
        if self.__dataframe is not None:
            return self.__dataframe

    def __init__( self, code ):
        self.__code = code
        self.__data = { 'code': self.__code  }
        self.__dataframe = pd.DataFrame

    def __str__( self ):
        return self.__code

class Division():
    '''Defines the Division Class'''
    __code = ''
    __name = ''
    __data = None

    @property
    def code( self ):
        if not self.__code == '':
            return self.__code

    @code.setter
    def code( self, code ):
        if not code == '':
            self.__code = code
            self.__data[ 'code' ] = code

    @property
    def name( self ):
        if not self.__name == '':
            return self.__name

    @name.setter
    def name( self, name ):
        if not name == '':
            self.__name = name
            self.__data[ 'name' ] = name

    @property
    def data( self ):
        ''' Property that provides the account elements of a Division'''
        if self.__data is not None:
            return self.__data

    def __init__( self, code ):
        self.__code = code
        self.__data = { 'code': self.__code }

    def __str__( self ):
        if not self.__code == '':
            return self.__code

class FinanceObjectClass():
    '''Defines the FinanceObjectClass Class'''
    __code = ''
    __name = ''
    __data = None
    __dataframe = None

    @property
    def code( self ):
        if not self.__code == '':
            return self.__code

    @code.setter
    def code( self, code ):
        if not code == '':
            self.__code = code
            self.__data[ 'code' ] = code

    @property
    def name( self ):
        if not self.__name == '':
            return self.__name

    @name.setter
    def name( self, name ):
        if not name == '':
            self.__name = name
            self.__data[ 'name' ] = name

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, src ):
        if isinstance( src, pd.DataFrame ):
            self.__data = src

    @property
    def table( self ):
        if self.__dataframe is not None:
            return self.__dataframe

    def __init__( self, code ):
        self.__code = code
        self.__data = { 'code': self.__code }
        self.__dataframe = pd.DataFrame

    def __str__( self ):
        if not self.__code == '':
            return self.__code

class Fund():
    '''Defines the Fund Class'''
    __code = ''
    __name = ''
    __title = ''
    __data = None
    __dataframe = None

    @property
    def code( self ):
        if not self.__code == '':
            return self.__code

    @code.setter
    def code( self, code ):
        if not code == '':
            self.__code = code
            self.__data[ 'code' ] = code

    @property
    def name( self ):
        if not self.__name == '':
            return self.__name

    @name.setter
    def name( self, name ):
        if not name == '':
            self.__name = name
            self.__data[ 'name' ] = name

    @property
    def title( self ):
        if self.__title is not None:
            return self.__title

    @title.setter
    def title( self, title ):
        if not title == '':
            self.__title = title
            self.__data[ 'title' ] = title

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, src ):
        if isinstance( src, pd.DataFrame ):
            self.__data = src

    @property
    def table( self ):
        if self.__dataframe is not None:
            return self.__dataframe

    def __init__( self, code ):
        self.__code = code
        self.__data = { 'code': self.__code }
        self.__dataframe = pd.DataFrame

    def __str__( self ):
        return self.__code

class Goal():
    '''Defines the Goal Class'''
    __code = ''
    __name = ''
    __data = None
    __dataframe = None

    @property
    def code( self ):
        if not self.__code == '':
            return self.__code

    @code.setter
    def code( self, code ):
        if not code == '':
            self.__code = code
            self.__data[ 'code' ] = code

    @property
    def name( self ):
        if not self.__name == '':
            return self.__name

    @name.setter
    def name( self, name ):
        if not name == '':
            self.__name = name
            self.__data[ 'name' ] = name

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, src ):
        if isinstance( src, pd.DataFrame ):
            self.__data = src

    @property
    def table( self ):
        if self.__dataframe is not None:
            return self.__dataframe

    def __init__( self, code ):
        self.__code = code
        self.__data = { 'code': self.__code }

    def __str__( self ):
        return self.__code

class NationalProgram():
    '''Defines the NationalProgram Class'''
    __code = ''
    __name = ''
    __rpio = ''
    __title = ''
    __data = None
    __dataframe = None

    @property
    def code( self ):
        if not self.__code == '':
            return self.__code

    @code.setter
    def code( self, code ):
        if not code == '':
            self.__code = code
            self.__data[ 'code' ] = code

    @property
    def name( self ):
        if not self.__name == '':
            return self.__name

    @name.setter
    def name( self, name ):
        if not name == '':
            self.__name = name
            self.__data[ 'name' ] = name

    @property
    def rpio( self ):
        if self.__rpio is not None:
            return self.__rpio

    @rpio.setter
    def rpio( self, code ):
        if not code == '':
            self.__rpio = code
            self.__data[ 'rpio' ] = code

    @property
    def title( self ):
        if self.__title is not None:
            return self.__title

    @title.setter
    def title( self, name ):
        if not name == '':
            self.__title = name
            self.__data[ 'title' ] = name

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, src ):
        if isinstance( src, pd.DataFrame ):
            self.__data = src

    @property
    def table( self ):
        if self.__dataframe is not None:
            return self.__dataframe

    def __init__( self, code ):
        self.__code = code
        self.__data = { 'code': self.__code }
        self.__dataframe = pd.DataFrame

    def __str__( self ):
        return self.__code

class Objective():
    '''Defines the Objective Class'''
    __code = ''
    __name = ''
    __data = None

    @property
    def code( self ):
        if not self.__code == '':
            return self.__code

    @code.setter
    def code( self, code ):
        if not code == '':
            self.__code = code
            self.__data[ 'code' ] = code

    @property
    def name( self ):
        if not self.__name == '':
            return self.__name

    @name.setter
    def name( self, name ):
        if not name == '':
            self.__name = name
            self.__data[ 'name' ] = name

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    def __init__( self, code ):
        self.__code = code
        self.__data = { 'code': self.__code }

    def __str__( self ):
        return self.__code

class Organization():
    '''Defines the Organization Class'''
    __code = ''
    __name = ''
    __data = None
    __dataframe = None

    @property
    def code( self ):
        if not self.__code == '':
            return self.__code

    @code.setter
    def code( self, code ):
        if not code == '':
            self.__code = code
            self.__data[ 'code' ] = code

    @property
    def name( self ):
        if not self.__name == '':
            return self.__name

    @name.setter
    def name( self, name ):
        if not name == '':
            self.__name = name
            self.__data[ 'name' ] = name

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, src ):
        if isinstance( src, pd.DataFrame ):
            self.__data = src

    @property
    def table( self ):
        if self.__dataframe is not None:
            return self.__dataframe

    def __init__( self, code ):
        self.__code = code
        self.__data = { 'code': code }
        self.__dataframe = pd.DataFrame

    def __str__( self ):
        return self.__code

class Project():
    '''Defines the Organization Class'''
    __code = ''
    __name = ''
    __data = None
    __dataframe = None

    @property
    def code( self ):
        if not self.__code == '':
            return self.__code

    @code.setter
    def code( self, code ):
        if not code == '':
            self.__code = code
            self.__data[ 'code' ] = code

    @property
    def name( self ):
        if not self.__name == '':
            return self.__name

    @name.setter
    def name( self, name ):
        if not name == '':
            self.__name = name
            self.__data[ 'name' ] = name

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, src ):
        if isinstance( src, pd.DataFrame ):
            self.__data = src

    @property
    def table( self ):
        if self.__dataframe is not None:
            return self.__dataframe

    def __init__( self, code ):
        self.__code = code
        self.__data = { 'code': self.__code }
        self.__dataframe = pd.DataFrame

    def __str__( self ):
        if self.__code:
            return self.__code

class ItProjectCode():
    '''Defines the Organization Class'''
    __code = ''
    __name = ''
    __data = None
    __dataframe = None

    @property
    def code( self ):
        if not self.__code == '':
            return self.__code

    @code.setter
    def code( self, code ):
        if not code == '':
            self.__code = code
            self.__data[ 'code' ] = code

    @property
    def name( self ):
        if not self.__name == '':
            return self.__name

    @name.setter
    def name( self, name ):
        if not name == '':
            self.__name = name
            self.__data[ 'name' ] = name

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, src ):
        if isinstance( src, pd.DataFrame ):
            self.__data = src

    @property
    def table( self ):
        if self.__dataframe is not None:
            return self.__dataframe

    def __init__( self, code ):
        self.__code = code
        self.__data = { 'code': self.__code }
        self.__dataframe = pd.DataFrame

    def __str__( self ):
        return self.__code

class SiteProjectCode():
    '''Defines the Organization Class'''
    __code = ''
    __name = ''
    __data = None
    __dataframe = None

    @property
    def code( self ):
        if not self.__code == '':
            return self.__code

    @code.setter
    def code( self, code ):
        if not code == '':
            self.__code = code
            self.__data[ 'code' ] = code

    @property
    def name( self ):
        if not self.__name == '':
            return self.__name

    @name.setter
    def name( self, name ):
        if not name == '':
            self.__name = name
            self.__data[ 'name' ] = name

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, src ):
        if isinstance( src, pd.DataFrame ):
            self.__data = src

    @property
    def table( self ):
        if self.__dataframe is not None:
            return self.__dataframe

    def __init__( self, code ):
        self.__code = code
        self.__data = { 'code': self.__code }
        self.__dataframe = pd.DataFrame

    def __str__( self ):
        return self.__code

class HumanResourceOrganization():
    '''Defines the Organization Class'''
    __code = ''
    __name = ''
    __data = None
    __dataframe = None

    @property
    def code( self ):
        if not self.__code == '':
            return self.__code

    @code.setter
    def code( self, code ):
        if not code == '':
            self.__code = code
            self.__data[ 'code' ] = code

    @property
    def name( self ):
        if not self.__name == '':
            return self.__name

    @name.setter
    def name( self, name ):
        if not name == '':
            self.__name = name
            self.__data[ 'name' ] = name

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, src ):
        if isinstance( src, pd.DataFrame ):
            self.__data = src

    @property
    def table( self ):
        if self.__dataframe is not None:
            return self.__dataframe

    def __init__( self, code ):
        self.__code = code
        self.__data = { 'code': self.__code }
        self.__dataframe = pd.DataFrame

    def __str__( self ):
        return self.__code

class WorkCode():
    '''Defines the Organization Class'''
    __code = ''
    __name = ''
    __data = None
    __dataframe = None

    @property
    def code( self ):
        if not self.__code == '':
            return self.__code

    @code.setter
    def code( self, code ):
        if not code == '':
            self.__code = code
            self.__data[ 'code' ] = code

    @property
    def name( self ):
        if not self.__name == '':
            return self.__name

    @name.setter
    def name( self, name ):
        if not name == '':
            self.__name = name
            self.__data[ 'name' ] = name

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @property
    def table( self ):
        if self.__dataframe is not None:
            return self.__dataframe

    def __init__( self, code ):
        self.__code = code
        self.__data = { 'code': self.__code }
        self.__dataframe = pd.DataFrame

    def __str__( self ):
        return self.__code

class ProgramArea():
    '''defines the ProgramArea class'''
    __code = ''
    __name = ''
    __data = None
    __dataframe = None

    @property
    def code( self ):
        if not self.__code == '':
            return self.__code

    @code.setter
    def code( self, code ):
        if not code == '':
            self.__code = code

    @property
    def name( self ):
        if not self.__name == '':
            return self.__name

    @name.setter
    def name( self, name ):
        if not name == '':
            self.__name = name

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @property
    def table( self ):
        if self.__dataframe is not None:
            return self.__dataframe

    def __init__( self, code ):
        self.__code = code
        self.__data = { 'code': self.__code }
        self.__dataframe = pd.DataFrame

    def __str__( self ):
        return self.__code

class ProgramProject():
    '''Defines the ProgramProject Class'''
    __code = ''
    __name = ''
    __description = None
    __data = None
    __dataframe = None

    @property
    def code( self ):
        if not self.__code == '':
            return self.__code

    @code.setter
    def code( self, code ):
        if not code == '':
            self.__code = code

    @property
    def name( self ):
        if not self.__name == '':
            return self.__name

    @name.setter
    def name( self, name ):
        if not name == '':
            self.__name = name

    @property
    def description( self ):
        if self.__description is not None:
            return self.__description

    @description.setter
    def description( self, text ):
        if text is not None:
            self.__description = str( text )

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @property
    def table( self ):
        if self.__dataframe is not None:
            return self.__dataframe

    def __init__( self, code, name = ''  ):
        self.__code = code
        self.__name = name
        self.__data = { 'code': self.__code, 'name': name }
        self.__dataframe = pd.DataFrame

    def __str__( self ):
        return self.__code

class ResponsibilityCenter():
    '''Defines the ResponsibilityCenter Class'''
    __code = ''
    __name = ''
    __data = None
    __dataframe = None

    @property
    def code( self ):
        if not self.__code == '':
            return self.__code

    @code.setter
    def code( self, code ):
        if not code == '':
            self.__code = code

    @property
    def name( self ):
        if not self.__name == '':
            return self.__name

    @name.setter
    def name( self, name ):
        if not name == '':
            self.__name = name

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @property
    def table( self ):
        if self.__dataframe is not None:
            return self.__dataframe

    def __init__( self, code, name = ''  ):
        self.__code = code
        self.__name = name
        self.__data = { 'code': code, 'name': name }
        self.__dataframe = pd.DataFrame

    def __str__( self ):
        return self.__code

class ResourcePlanningOffice():
    '''defines the ResponsiblePlanningOffice class'''
    __code = ''
    __name = ''
    __data = None
    __dataframe = None

    @property
    def code( self ):
        if not self.__code == '':
            return self.__code

    @code.setter
    def code( self, code ):
        if not code == '':
            self.__code = code

    @property
    def name( self ):
        if not self.__name == '':
            return self.__name

    @name.setter
    def name( self, name ):
        if not name == '':
            self.__name = name

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
        self.__data = { 'code': code, 'name': name }
        self.__dataframe = pd.DataFrame

    def __str__( self ):
        return self.__code

class ProgramResultsCode():
    '''Defines the PRC class'''
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
    def rpio( self ):
        if self.__rpio is not None:
            return self.__rpio

    @rpio.setter
    def rpio( self, code ):
        if not code == '':
            self.__rpio = ResourcePlanningOffice( code )
            self.__data[ 'RPIO' ] = self.__rpio.code

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return BudgetFiscalYear( self.__bfy )

    @bfy.setter
    def bfy( self, year ):
        if year is not None:
            self.__rpio = BudgetFiscalYear( year )
            self.__data[ 'BFY' ] = self.__bfy.firstyear

    @property
    def fund( self ):
        if self.__fund.code is not None:
            return Fund( self.__fund.code )

    @fund.setter
    def fund( self, code ):
        if not code == '':
            self.__fund = ResourcePlanningOffice( code )
            self.__data[ 'Fund' ] = self.__fund.code

    @property
    def ah( self ):
        if self.__ah is not None:
            return AllowanceHolder( self.__ah )

    @ah.setter
    def ah( self, code ):
        if not code == '':
            self.__ah = AllowanceHolder( code )
            self.__data[ 'AH' ] = self.__ah.code

    @property
    def account( self ):
        if self.__account is not None:
            return self.__account

    @account.setter
    def account( self, code ):
        if not code == '':
            self.__account = Account( code )
            self.__data[ 'Account' ] = self.__account.code

    @property
    def activity( self ):
        if self.__account is not None:
            self.__activity = str( self.__account[ 5:2 ] )
            return Activity( self.__activity )

    @activity.setter
    def activity( self, code ):
        if not code == '':
            self.__activity = Activity( code )
            self.__data[ 'Activity' ] = self.__activity.code

    @property
    def org( self ):
        if self.__org is not None:
            return Organization( self.__org )

    @org.setter
    def org( self, code ):
        if not code == '':
            self.__org = Organization( code )
            self.__data[ 'ORG' ] = self.__org.code

    @property
    def rc( self ):
        if self.__rc is not None:
            return self.__rc

    @rc.setter
    def rc( self, code ):
        if not code == '':
            self.__rc = ResponsibilityCenter( code )
            self.__data[ 'RC' ] = self.__rc.code

    @property
    def boc( self ):
        if self.__boc is not None:
            return self.__boc

    @boc.setter
    def boc( self, code ):
        if not code == '':
            self.__rpio = BudgetObjectClass( code )
            self.__data[ 'BOC' ] = self.__boc.code

    @property
    def amount( self ):
        if self.__amount is not None:
            return self.__amount

    @amount.setter
    def amount( self, value ):
        if value is not None:
            self.__amount = value
            self.__data[ 'Amount' ] = self.__amount

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @property
    def table( self ):
        if self.__dataframe is not None:
            return self.__dataframe

    def __init__( self, code, amount = 0 ):
        '''Initializes the PRC class'''
        self.__account = Account( code )
        self.__amount = amount
        self.__data = { 'code': self.__account.code,
                        'account': self.__account,
                        'amount': self.__amount }
        self.__dataframe = pd.DataFrame

    def __str__( self ):
        if self.__account.code is not None:
            return self.__account.code

class RegionalOffice():
    '''Defines a regional RPIO'''
    __rpio = None
    __code = ''
    __name = ''
    __data = None
    __dataframe = None

    @property
    def rpio( self ):
        if self.__rpio is not None:
            return self.__rpio

    @rpio.setter
    def rpio( self, code ):
        if not code == '':
            self.__rpio = ResourcePlanningOffice( code )
            self.__data[ 'rpio' ] = self.__rpio

    @property
    def name( self ):
        if not self.__name == '':
            return self.__name

    @name.setter
    def name( self, name ):
        if not name == '':
            self.__name = name
            self.__data[ 'name' ] = name

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @property
    def table( self ):
        if self.__dataframe is not None:
            return self.__dataframe

    def __init__( self, rpio, name = ''  ):
        self.__rpio = ResourcePlanningOffice( rpio )
        self.__name = name
        self.__data = { 'rpio': rpio,
                        'name': name }
        self.__dataframe = pd.DataFrame

    def __str__( self ):
        if self.__rpio is not None:
            return str( self.__rpio )

class SiteProject():
    '''Defines the Site Project Code Class'''
    __epaid = ''
    __ssid = ''
    __actioncode = ''
    __operableunit = ''
    __code = ''
    __name = ''
    __data = None
    __dataframe = None

    @property
    def ssid( self ):
        if self.__ssid is not None:
            return self.__ssid

    @ssid.setter
    def ssid( self, ssid ):
        if ssid is not None:
            self.__ssid = str( ssid )
            self.__data[ 'ssid' ] = self.__ssid

    @property
    def actioncode( self ):
        if self.__actioncode is not None:
            return self.__actioncode

    @actioncode.setter
    def actioncode( self, code ):
        if not code == '':
            self.__actioncode = code
            self.__data[ 'actioncode' ] = self.__actioncode

    @property
    def operableunit( self ):
        if self.__operableunit is not None:
            return self.__operableunit

    @operableunit.setter
    def operableunit( self, unit ):
        if unit is not None:
            self.__operableunit = str( unit )
            self.__data[ 'operableunit' ] = self.__operableunit

    @property
    def epaid( self ):
        if self.__epaid is not None:
            return self.__epaid

    @epaid.setter
    def epaid( self, eid ):
        if eid is not None:
            self.__epaid = str( eid )
            self.__data[ 'epaid' ] = self.__epaid

    @property
    def code( self ):
        if not self.__code == '':
            return self.__code

    @code.setter
    def code( self, code ):
        if not code == '':
            self.__code = code
            self.__data[ 'code' ] = code

    @property
    def name( self ):
        if not self.__name == '':
            return self.__name

    @name.setter
    def name( self, name ):
        if not name == '':
            self.__name = name
            self.__data[ 'name' ] = name

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @property
    def table( self ):
        if self.__dataframe is not None:
            return self.__dataframe

    def __init__( self, code ):
        self.__code = code
        self.__ssid = self.__code[ 0: 4 ]
        self.__actioncode = self.__code[ 4:6 ]
        self.__operableunit = self.__code[ 6:9 ]
        self.__data = { 'code': self.__code }
        self.__dataframe = pd.DataFrame

    def __str__( self ):
        return self.__code

class HeadQuartersOffice():
    '''Defines the HQ class'''
    __rpio = None
    __name = ''
    __title = None
    __data = None
    __dataframe = None

    @property
    def rpio( self ):
        if self.__rpio is not None:
            return self.__rpio

    @rpio.setter
    def rpio( self, code ):
        if not code == '':
            self.__rpio = code
            self.__data[ 'rpio' ] = self.__rpio

    @property
    def name( self ):
        if not self.__name == '':
            return self.__name

    @name.setter
    def name( self, name ):
        if not name == '':
            self.__name = name
            self.__data[ 'name' ] = name

    @property
    def title( self ):
        if self.__title is not None:
            return self.__title

    @title.setter
    def title( self, title ):
        if title is not None:
            self.__title = str( title )
            self.__data[ 'title' ] = self.__title

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @property
    def table( self ):
        if self.__dataframe is not None:
            return self.__dataframe

    def __init__( self, rpio ):
        self.__rpio = ResourcePlanningOffice( str( rpio ) )
        self.__name = self.__rpio.name
        self.__data = { 'rpio': self.__rpio,
                        'name': self.__name }
        self.__dataframe = pd.DataFrame

    def __str__( self ):
        if not self.__name == '':
            return self.__name

class Holiday():
    '''Defines the Holiday class'''
    __bfy = None
    __name = ''
    __date = None
    __day = None
    __data = None
    __dataframe = None

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, year ):
        if year is not None:
            self.__bfy = str( year )
            self.__data[ 'bfy' ] = self.__bfy

    @property
    def name( self ):
        if not self.__name == '':
            return self.__name

    @name.setter
    def name( self, name ):
        if not name == '':
            self.__name = name
            self.__data[ 'name' ] = name

    @property
    def date( self ):
        if self.__date is not None:
            return self.__date

    @date.setter
    def date( self, date ):
        if isinstance( date, dt.date ):
            self.__date = date
            self.__data[ 'date' ] = str( self.__date )

    @property
    def day( self ):
        if self.__day is not None:
            return self.__day

    @day.setter
    def day( self, day ):
        if isinstance( day, int ):
            self.__day = day
            self.__data[ 'day' ] = str( self.__day )

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @property
    def table( self ):
        if self.__dataframe is not None:
            return self.__dataframe

    def __init__( self, bfy, name ):
        self.__bfy = str( bfy )
        self.__name = name
        self.__date = dt.date.today()
        self.__day = self.__date.day
        self.__data = { 'bfy': self.__bfy,
                        'name': self.__name }
        self.__dataframe = pd.DataFrame

    def __str__( self ):
        if not self.__name == '':
            return self.__name

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

    @amount.setter
    def amount( self, value ):
        if value is not None:
            self.__amount = float( value )
            self.__data[ 'amount' ] = self.__amount

    @property
    def account( self ):
        if self.__account is not None:
            return self.__account

    @account.setter
    def account( self, code ):
        if not code == '':
            self.__account = Account( code )
            self.__data[ 'account' ] = code

    @property
    def document( self ):
        if self.__document is not None:
            return self.__document

    @document.setter
    def document( self, doc ):
        if doc is not None:
            self.__document = str( doc )
            self.__data[ 'document' ] = self.__document

    @property
    def org( self ):
        if self.__org is not None:
            return self.__org

    @org.setter
    def org( self, code ):
        if not code == '':
            self.__org = Organization( code )
            self.__data[ 'org' ] = code

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, year ):
        if not year == '':
            self.__bfy = BudgetFiscalYear( year )
            self.__data[ 'bfy' ] = year

    @property
    def fund( self ):
        if self.__fund is not None:
            return self.__fund

    @fund.setter
    def fund( self, code ):
        if not code == '':
            self.__fund = Fund( code )
            self.__data[ 'fund' ] = code

    @property
    def boc( self ):
        if self.__boc is not None:
            return self.__boc

    @boc.setter
    def boc( self, code ):
        if not code == '':
            self.__boc = BudgetObjectClass( code )
            self.__data[ 'boc' ] = code

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @property
    def table( self ):
        if self.__dataframe is not None:
            return self.__dataframe

    def __init__( self, amount  ):
        self.__amount = float( amount )
        self.__data = { 'amount': self.__amount,
                        'account': None,
                        'document': None,
                        'org': None,
                        'bfy': None,
                        'fund': None,
                        'boc': None }
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

    @amount.setter
    def amount( self, value ):
        if value is not None:
            self.__amount = float( value )
            self.__data[ 'amount' ] = self.__amount

    @property
    def account( self ):
        if self.__account is not None:
            return self.__account

    @account.setter
    def account( self, code ):
        if not code == '':
            self.__account = Account( code )
            self.__data[ 'account' ] = code

    @property
    def document( self ):
        if self.__document is not None:
            return self.__document

    @document.setter
    def document( self, doc ):
        if doc is not None:
            self.__document = str( doc )
            self.__data[ 'document' ] = self.__document

    @property
    def org( self ):
        if self.__org is not None:
            return self.__org

    @org.setter
    def org( self, code ):
        if not code == '':
            self.__org = Organization( code )
            self.__data[ 'org' ] = code

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, year ):
        if not year == '':
            self.__bfy = BudgetFiscalYear( year )
            self.__data[ 'bfy' ] = year

    @property
    def fund( self ):
        if self.__fund is not None:
            return self.__fund

    @fund.setter
    def fund( self, code ):
        if not code == '':
            self.__fund = Fund( code )
            self.__data[ 'fund' ] = code

    @property
    def boc( self ):
        if self.__boc is not None:
            return self.__boc

    @boc.setter
    def boc( self, code ):
        if not code == '':
            self.__boc = BudgetObjectClass( code )
            self.__data[ 'boc' ] = code

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @property
    def table( self ):
        if self.__dataframe is not None:
            return self.__dataframe

    def __init__( self, amount ):
        self.__amount = float( amount )
        self.__data = { 'amount': self.__amount,
                        'account': None,
                        'document': None,
                        'org': None,
                        'bfy': None,
                        'fund': None,
                        'boc': None }
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

    @amount.setter
    def amount( self, value ):
        if value is not None:
            self.__amount = float( value )
            self.__data[ 'amount' ] = self.__amount

    @property
    def account( self ):
        if self.__account is not None:
            return self.__account

    @account.setter
    def account( self, code ):
        if not code == '':
            self.__account = Account( code )
            self.__data[ 'account' ] = code

    @property
    def document( self ):
        if self.__document is not None:
            return self.__document

    @document.setter
    def document( self, doc ):
        if doc is not None:
            self.__document = str( doc )
            self.__data[ 'document' ] = self.__document

    @property
    def org( self ):
        if self.__org is not None:
            return self.__org

    @org.setter
    def org( self, code ):
        if not code == '':
            self.__org = Organization( code )
            self.__data[ 'org' ] = code

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, year ):
        if not year == '':
            self.__bfy = BudgetFiscalYear( year )
            self.__data[ 'bfy' ] = year

    @property
    def fund( self ):
        if self.__fund is not None:
            return self.__fund

    @fund.setter
    def fund( self, code ):
        if not code == '':
            self.__fund = Fund( code )
            self.__data[ 'fund' ] = code

    @property
    def boc( self ):
        if self.__boc is not None:
            return self.__boc

    @boc.setter
    def boc( self, code ):
        if not code == '':
            self.__boc = BudgetObjectClass( code )
            self.__data[ 'boc' ] = code

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @property
    def table( self ):
        if self.__dataframe is not None:
            return self.__dataframe

    def __init__( self, amount ):
        self.__amount = float( amount )
        self.__data = { 'amount': self.__amount,
                        'account': None,
                        'document': None,
                        'org': None,
                        'bfy': None,
                        'fund': None,
                        'boc': None }
        self.__dataframe = pd.DataFrame

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

    @amount.setter
    def amount( self, value ):
        if value is not None:
            self.__amount = float( value )
            self.__data[ 'amount' ] = self.__amount

    @property
    def account( self ):
        if self.__account is not None:
            return self.__account

    @account.setter
    def account( self, code ):
        if not code == '':
            self.__account = Account( code )
            self.__data[ 'account' ] = code

    @property
    def dcn( self ):
        if self.__document is not None:
            return self.__document

    @dcn.setter
    def dcn( self, doc ):
        if doc is not None:
            self.__document = str( doc )
            self.__data[ 'document' ] = self.__document

    @property
    def org( self ):
        if self.__org is not None:
            return self.__org

    @org.setter
    def org( self, code ):
        if not code == '':
            self.__org = Organization( code )
            self.__data[ 'org' ] = code

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, year ):
        if not year == '':
            self.__bfy = BudgetFiscalYear( year )
            self.__data[ 'bfy' ] = year

    @property
    def fund( self ):
        if self.__fund is not None:
            return self.__fund

    @fund.setter
    def fund( self, code ):
        if not code == '':
            self.__fund = Fund( code )
            self.__data[ 'fund' ] = code

    @property
    def boc( self ):
        if self.__boc is not None:
            return self.__boc

    @boc.setter
    def boc( self, code ):
        if not code == '':
            self.__boc = BudgetObjectClass( code )
            self.__data[ 'boc' ] = code

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @property
    def table( self ):
        if self.__dataframe is not None:
            return self.__dataframe

    def __init__( self, amount ):
        self.__amount = float( amount )
        self.__data = { 'amount': self.__amount,
                        'account': None,
                        'document': None,
                        'org': None,
                        'bfy': None,
                        'fund': None,
                        'boc': None }
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

    @amount.setter
    def amount( self, value ):
        if value is not None:
            self.__amount = float( value )
            self.__data[ 'amount' ] = self.__amount

    @property
    def account( self ):
        if self.__account is not None:
            return self.__account

    @account.setter
    def account( self, code ):
        if not code == '':
            self.__account = Account( code )
            self.__data[ 'account' ] = code

    @property
    def document( self ):
        if not self.__document == '':
            return self.__document

    @document.setter
    def document( self, doc ):
        if not doc == '':
            self.__document = doc
            self.__data[ 'document' ] = doc

    @property
    def org( self ):
        if not self.__org == '':
            return self.__org

    @org.setter
    def org( self, code ):
        if not code == '':
            self.__org = Organization( code )
            self.__data[ 'org' ] = code

    @property
    def bfy( self ):
        if not self.__bfy == '':
            return self.__bfy

    @bfy.setter
    def bfy( self, year ):
        if not year == '':
            self.__bfy = BudgetFiscalYear( year )
            self.__data[ 'bfy' ] = year

    @property
    def fund( self ):
        if not self.__fund == '':
            return self.__fund

    @fund.setter
    def fund( self, code ):
        if not code == '':
            self.__fund = Fund( code )
            self.__data[ 'fund' ] = code

    @property
    def boc( self ):
        if self.__boc is not None:
            return self.__boc

    @boc.setter
    def boc( self, code ):
        if not code == '':
            self.__boc = BudgetObjectClass( code )
            self.__data[ 'boc' ] = code

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @property
    def table( self ):
        if self.__dataframe is not None:
            return self.__dataframe

    def __init__( self, amount ):
        self.__amount = float( amount )
        self.__data = { 'amount': self.__amount,
                        'account': None,
                        'document': None,
                        'org': None,
                        'bfy': None,
                        'fund': None,
                        'boc': None }
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

    @amount.setter
    def amount( self, value ):
        if value is not None:
            self.__amount = float( value )
            self.__data[ 'amount' ] = self.__amount

    @property
    def account( self ):
        if self.__account is not None:
            return self.__account

    @account.setter
    def account( self, code ):
        if not code == '':
            self.__account = Account( code )
            self.__data[ 'account' ] = code

    @property
    def document( self ):
        if self.__document is not None:
            return self.__document

    @document.setter
    def document( self, doc ):
        if doc is not None:
            self.__document = str( doc )
            self.__data[ 'document' ] = self.__document

    @property
    def org( self ):
        if self.__org is not None:
            return self.__org

    @org.setter
    def org( self, code ):
        if not code == '':
            self.__org = Organization( code )
            self.__data[ 'org' ] = code

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, year ):
        if not year == '':
            self.__bfy = BudgetFiscalYear( year )
            self.__data[ 'bfy' ] = year

    @property
    def fund( self ):
        if self.__fund is not None:
            return self.__fund

    @fund.setter
    def fund( self, code ):
        if not code == '':
            self.__fund = Fund( code )
            self.__data[ 'fund' ] = code

    @property
    def boc( self ):
        if self.__boc is not None:
            return self.__boc

    @boc.setter
    def boc( self, code ):
        if not code == '':
            self.__boc = BudgetObjectClass( code )
            self.__data[ 'boc' ] = code

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @property
    def table( self ):
        if self.__dataframe is not None:
            return self.__dataframe

    def __init__( self, amount ):
        self.__amount = float( amount )
        self.__data = { 'amount': self.__amount,
                        'account': None,
                        'document': None,
                        'org': None,
                        'bfy': None,
                        'fund': None,
                        'boc': None }
        self.__dataframe = pd.DataFrame
        self.__dataframe = pd.DataFrame

    def __str__( self ):
        if self.__amount is not None:
            return str( self.__amount )