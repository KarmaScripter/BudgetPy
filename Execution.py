import datetime as dt
import pandas as pd

class Account( ):
    '''defines the Account Code class'''
    __code = None
    __name = None
    __goal = None
    __objective = None
    __npm = None
    __programproject = None
    __data = None
    __frame = None

    @property
    def code( self ):
        if self.__code:
            return self.__code

    @code.setter
    def code( self, code ):
        if code is not None:
            self.__code = str( code )
            self.__data[ 'fund' ] = self.__code

    @property
    def name( self ):
        if self.__name:
            return self.__name

    @name.setter
    def name( self, name ):
        if name is not None:
            self.__name = str( name )
            self.__data[ 'name' ] = self.__name

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
        if code is not None:
            self.__npm = str( code )
            self.__data[ 'npm' ] = self.__npm

    @property
    def programproject( self ):
        if self.__programproject is not None:
            return self.__programproject

    @programproject.setter
    def programproject( self, code ):
        if code is not None:
            self.__programproject = str( code )
            self.__data[ 'programproject' ] = self.__programproject

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, cache ):
        if isinstance( cache, dict ):
            self.__data = cache

    @property
    def table( self ):
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, frame ):
        if isinstance( frame, pd.DataFrame ):
            self.__frame = frame

    def __str__( self ):
        if self.__code is not None:
            return self.__code

    def __init__( self, code ):
        self.__data = { }
        self.__code = code if isinstance( code, str ) else 'NS'
        self.__goal = self.__code[ 0 ]
        self.__objective = self.__code[ 1:3 ]
        self.__npm = self.__code[ 3 ]
        self.__programproject = self.__code[ 4:6 ]
        self.__frame = pd.DataFrame( self.__data )


class Activity( ):
    '''Defines the Activity Class'''
    __code = None
    __name = None
    __data = None
    __frame = None

    @property
    def code( self ):
        if self.__code is not None:
            return self.__code

    @code.setter
    def code( self, code ):
        if isinstance( code, str ) and code != '':
            self.__code = str( code )
            self.__data[ 'fund' ] = self.__code

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, name ):
        if isinstance( name, str ) and name != '':
            self.__name = str( name )
            self.__data[ 'name' ] = self.__name

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, cache ):
        if isinstance( cache, dict ):
            self.__data = cache

    @property
    def table( self ):
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, frame ):
        if isinstance( frame, pd.DataFrame ):
            self.__frame = frame

    def __str__( self ):
        return self.__code

    def __init__( self, code ):
        self.__data = { }
        self.__code = str( code )
        self.__frame = pd.DataFrame


class AllowanceHolder( ):
    '''Defines the AllowanceHolder Class'''
    __code = None
    __name = None
    __data = None
    __frame = None

    @property
    def code( self ):
        if self.__code is not None:
            return self.__code

    @code.setter
    def code( self, code ):
        if code is not None:
            self.__code = str( code )
            self.__data[ 'fund' ] = self.__code

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, name ):
        if name is not None:
            self.__name = str( name )
            self.__data[ 'name' ] = self.__name

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, cache ):
        if isinstance( cache, dict ):
            self.__data = cache

    @property
    def table( self ):
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, frame ):
        if isinstance( frame, pd.DataFrame ):
            self.__frame = frame

    def __str__( self ):
        if not self.__code == '':
            return self.__code

    def __init__( self, code ):
        self.__data = { }
        self.__code = str( code )
        self.__frame = pd.DataFrame


class Appropriation( ):
    '''Defines the Appropriation Class'''
    __fund = None
    __code = None
    __name = None
    __title = None
    __bfy = None
    __data = None
    __frame = None

    @property
    def code( self ):
        if self.__code is not None:
            return self.__code

    @code.setter
    def code( self, code ):
        if code is not None:
            self.__code = str( code )

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, name ):
        if name is not None:
            self.__name = str( name )
            self.__data[ 'name' ] = self.__name

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
        if code is not None:
            self.__fund = Fund( str( code ) )
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
    def data( self, cache ):
        if isinstance( cache, dict ):
            self.__data = cache

    @property
    def table( self ):
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, frame ):
        if isinstance( frame, pd.DataFrame ):
            self.__frame = frame

    def __str__( self ):
        return self.__code

    def __init__( self, code ):
        self.__code = str( code )
        self.__fund = Fund( self.__code )
        self.__data = { 'code': self.__code,
                        'fund': self.__fund }


class BudgetFiscalYear( ):
    '''Class to describe the federal fiscal year'''
    __base = None
    __bfy = None
    __efy = None
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
    __frame = None

    @property
    def firstyear( self ):
        if self.__base is not None:
            return self.__bfy

    @firstyear.setter
    def firstyear( self, yr ):
        if yr is not None:
            self.__bfy = str( yr )
            self.__data[ 'firstyear' ] = self.__bfy

    @property
    def lastyear( self ):
        if self.__efy is not None:
            return self.__efy

    @lastyear.setter
    def lastyear( self, yr ):
        if yr is not None:
            self.__efy = str( yr )
            self.__data[ 'lastyear' ] = self.__efy

    @property
    def calendaryear( self ):
        if self.__year:
            return self.__year

    @calendaryear.setter
    def calendaryear( self, yr ):
        if yr is not None:
            self.__year = int( yr )
            self.__data[ 'calendaryear' ] = self.__year

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
        if self.__weekends is not None:
            return self.__weekends

    @weekends.setter
    def weekends( self, end ):
        if isinstance( end, int ):
            self.__weekends = end
            self.__data[ 'weekends' ] = self.__weekends

    @property
    def workdays( self ):
        if self.__workdays is not None:
            return float( self.__workdays )

    @workdays.setter
    def workdays( self, work ):
        if isinstance( work, float ):
            self.__workdays = work
            self.__data[ 'workdays' ] = self.__workdays

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
        if isinstance( today, int ):
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
    def data( self, cache ):
        if isinstance( cache, dict ):
            self.__data = cache

    @property
    def table( self ):
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, frame ):
        if isinstance( frame, pd.DataFrame ):
            self.__frame = frame

    def __str__( self ):
        return str( self.__year )

    def __init__( self, bfy ):
        self.__today = dt.date.today( )
        self.__base = bfy if isinstance( bfy, str ) else str( dt.date.year )
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
        self.__frame = pd.DataFrame


class BudgetObjectClass( ):
    '''Defines the BudgetObjectClass Class'''
    __code = None
    __name = None
    __value = None
    __data = None
    __frame = None

    @property
    def code( self ):
        if self.__code is not None:
            return self.__code

    @code.setter
    def code( self, code ):
        if code is not None:
            self.__code = str( code )
            self.__data[ 'fund' ] = self.__code

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, name ):
        if name is not None:
            self.__name = str( name )
            self.__data[ 'name' ] = self.__name

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
    def data( self, cache ):
        if isinstance( cache, dict ):
            self.__data = cache

    @property
    def table( self ):
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, frame ):
        if isinstance( frame, pd.DataFrame ):
            self.__frame = frame

    def __str__( self ):
        return self.__code

    def __init__( self, code ):
        self.__code = code if isinstance( code, str ) else 'NS'
        self.__data = { 'fund': self.__code }
        self.__frame = pd.DataFrame


class Division( ):
    '''Defines the Division Class'''
    __code = None
    __name = None
    __data = None

    @property
    def code( self ):
        if self.__code is not None:
            return self.__code

    @code.setter
    def code( self, code ):
        if code is not None:
            self.__code = str( code )
            self.__data[ 'fund' ] = self.__code

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, name ):
        if name is not None:
            self.__name = str( name )
            self.__data[ 'name' ] = self.__name

    @property
    def data( self ):
        ''' Property that provides the account elements of a Division'''
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, cache ):
        if isinstance( cache, dict ):
            self.__data = cache

    def __init__( self, code ):
        self.__code = str( code )
        self.__data = { 'fund': self.__code }

    def __str__( self ):
        if not self.__code == '':
            return self.__code


class FinanceObjectClass( ):
    '''Defines the Finance Object Class'''
    __code = None
    __name = None
    __data = None
    __frame = None

    @property
    def code( self ):
        if self.__code is not None:
            return self.__code

    @code.setter
    def code( self, code ):
        if code is not None:
            self.__code = str( code )
            self.__data[ 'fund' ] = self.__code

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, name ):
        if name is not None:
            self.__name = str( name )
            self.__data[ 'name' ] = self.__name

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, cache ):
        if isinstance( cache, dict ):
            self.__data = cache

    @property
    def table( self ):
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, frame ):
        if isinstance( frame, pd.DataFrame ):
            self.__frame = frame

    def __str__( self ):
        if not self.__code == '':
            return self.__code

    def __init__( self, code ):
        self.__code = code if isinstance( code, str ) else 'NS'
        self.__data = { 'fund': self.__code }
        self.__frame = pd.DataFrame


class Fund( ):
    '''Defines the Fund Class'''
    __code = None
    __name = None
    __title = None
    __data = None
    __frame = None

    @property
    def code( self ):
        if self.__code is not None:
            return self.__code

    @code.setter
    def code( self, code ):
        if code is not None:
            self.__code = str( code )
            self.__data[ 'fund' ] = self.__code

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, name ):
        if name is not None:
            self.__name = str( name )
            self.__data[ 'name' ] = self.__name

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
    def data( self, cache ):
        if isinstance( cache, dict ):
            self.__data = cache

    @property
    def table( self ):
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, frame ):
        if isinstance( frame, pd.DataFrame ):
            self.__frame = frame

    def __str__( self ):
        return self.__code

    def __init__( self, code ):
        self.__code = str( code )
        self.__data = { 'fund': self.__code }
        self.__frame = pd.DataFrame


class Goal( ):
    '''Defines the Goal Class'''
    __code = None
    __name = None
    __data = None
    __frame = None

    @property
    def code( self ):
        if self.__code is not None:
            return self.__code

    @code.setter
    def code( self, code ):
        if code is not None:
            self.__code = str( code )
            self.__data[ 'fund' ] = self.__code

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, name ):
        if name is not None:
            self.__name = str( name )
            self.__data[ 'name' ] = self.__name

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, cache ):
        if isinstance( cache, dict ):
            self.__data = cache

    @property
    def table( self ):
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, frame ):
        if isinstance( frame, pd.DataFrame ):
            self.__frame = frame

    def __str__( self ):
        return self.__code

    def __init__( self, code ):
        self.__code = str( code )
        self.__data = { 'fund': self.__code }


class NationalProgram( ):
    '''Defines the NationalProgram Class'''
    __code = None
    __name = None
    __rpio = None
    __title = None
    __data = None
    __frame = None

    @property
    def code( self ):
        if self.__code is not None:
            return self.__code

    @code.setter
    def code( self, code ):
        if code is not None:
            self.__code = str( code )
            self.__data[ 'fund' ] = self.__code

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, name ):
        if name is not None:
            self.__name = str( name )
            self.__data[ 'name' ] = self.__name

    @property
    def rpio( self ):
        if self.__rpio is not None:
            return self.__rpio

    @rpio.setter
    def rpio( self, code ):
        if code is not None:
            self.__rpio = str( code )
            self.__data[ 'rpio' ] = self.__rpio

    @property
    def title( self ):
        if self.__title is not None:
            return self.__title

    @title.setter
    def title( self, name ):
        if name is not None:
            self.__title = str( name )
            self.__data[ 'title' ] = self.__title

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, cache ):
        if isinstance( cache, dict ):
            self.__data = cache

    @property
    def table( self ):
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, frame ):
        if isinstance( frame, pd.DataFrame ):
            self.__frame = frame

    def __str__( self ):
        return self.__code

    def __init__( self, code ):
        self.__code = str( code )
        self.__data = { 'fund': self.__code }
        self.__frame = pd.DataFrame


class Objective( ):
    '''Defines the Objective Class'''
    __code = None
    __name = None
    __data = None
    __frame = None

    @property
    def code( self ):
        if self.__code is not None:
            return self.__code

    @code.setter
    def code( self, code ):
        if code is not None:
            self.__code = str( code )
            self.__data[ 'fund' ] = Objective( self.__code )

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, name ):
        if name is not None:
            self.__name = str( name )
            self.__data[ 'name' ] = self.__name

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, cache ):
        if isinstance( cache, dict ):
            self.__data = cache

    @property
    def table( self ):
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, frame ):
        if isinstance( frame, pd.DataFrame ):
            self.__frame = frame

    def __str__( self ):
        return self.__code

    def __init__( self, code ):
        self.__code = Objective( str( code ) )
        self.__data = { 'fund': self.__code }
        self.__frame = pd.DataFrame


class Organization( ):
    '''Defines the Organization Class'''
    __code = None
    __name = None
    __data = None
    __frame = None

    @property
    def code( self ):
        if self.__code is not None:
            return self.__code

    @code.setter
    def code( self, code ):
        if code is not None:
            self.__code = str( code )
            self.__data[ 'fund' ] = self.__code

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, name ):
        if name is not None:
            self.__name = str( name )
            self.__data[ 'name' ] = self.__name

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, cache ):
        if isinstance( cache, dict ):
            self.__data = cache

    @property
    def table( self ):
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, frame ):
        if isinstance( frame, pd.DataFrame ):
            self.__frame = frame

    def __str__( self ):
        return self.__code

    def __init__( self, code ):
        self.__code = code
        self.__data = { 'fund': self.__code }
        self.__frame = pd.DataFrame


class Project( ):
    '''Defines the Organization Class'''
    __code = None
    __name = None
    __data = None
    __frame = None

    @property
    def code( self ):
        if self.__code is not None:
            return self.__code

    @code.setter
    def code( self, code ):
        if code is not None:
            self.__code = str( code )
            self.__data[ 'fund' ] = self.__code

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, name ):
        if name is not None:
            self.__name = str( name )
            self.__data[ 'name' ] = self.__name

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, cache ):
        if isinstance( cache, dict ):
            self.__data = cache

    @property
    def table( self ):
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, frame ):
        if isinstance( frame, pd.DataFrame ):
            self.__frame = frame

    def __str__( self ):
        if self.__code:
            return self.__code

    def __init__( self, code ):
        self.__code = str( code )
        self.__data = { 'fund': self.__code }
        self.__frame = pd.DataFrame


class ItProjectCode( ):
    '''Defines the Organization Class'''
    __code = None
    __name = None
    __data = None
    __frame = None

    @property
    def code( self ):
        if self.__code is not None:
            return self.__code

    @code.setter
    def code( self, code ):
        if code is not None:
            self.__code = str( code )
            self.__data[ 'fund' ] = self.__code

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, name ):
        if name is not None:
            self.__name = str( name )
            self.__data[ 'name' ] = self.__name

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, cache ):
        if isinstance( cache, dict ):
            self.__data = cache

    @property
    def table( self ):
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, frame ):
        if isinstance( frame, pd.DataFrame ):
            self.__frame = frame

    def __str__( self ):
        return self.__code

    def __init__( self, code ):
        self.__code = str( code )
        self.__data = { 'fund': self.__code }
        self.__frame = pd.DataFrame


class SiteProjectCode( ):
    '''Defines the Organization Class'''
    __code = None
    __name = None
    __data = None
    __frame = None

    @property
    def code( self ):
        if self.__code is not None:
            return self.__code

    @code.setter
    def code( self, code ):
        if code is not None:
            self.__code = str( code )
            self.__data[ 'fund' ] = self.__code

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, name ):
        if name is not None:
            self.__name = str( name )
            self.__data[ 'name' ] = self.__name

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, cache ):
        if isinstance( cache, dict ):
            self.__data = cache

    @property
    def table( self ):
        if self.__frame is not None:
            return self.__frame

    def __str__( self ):
        return self.__code

    def __init__( self, code ):
        self.__code = str( code )
        self.__data = { 'fund': self.__code }
        self.__frame = pd.DataFrame


class HumanResourceOrganization( ):
    '''Defines the Organization Class'''
    __code = None
    __name = None
    __data = None
    __frame = None

    @property
    def code( self ):
        if self.__code is not None:
            return self.__code

    @code.setter
    def code( self, code ):
        if isinstance( code, str ) and code != '':
            self.__code = str( code )
            self.__data[ 'fund' ] = self.__code

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, name ):
        if name is not None:
            self.__name = str( name )
            self.__data[ 'name' ] = self.__name

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, cache ):
        if isinstance( cache, dict ):
            self.__data = cache

    @property
    def table( self ):
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, frame ):
        if isinstance( frame, pd.DataFrame ):
            self.__frame = frame

    def __str__( self ):
        return self.__code

    def __init__( self, code ):
        self.__code = str( code )
        self.__data = { 'fund': self.__code }
        self.__frame = pd.DataFrame


class WorkCode( ):
    '''Defines the Organization Class'''
    __code = None
    __name = None
    __data = None
    __frame = None

    @property
    def code( self ):
        if self.__code is not None:
            return self.__code

    @code.setter
    def code( self, code ):
        if code is not None:
            self.__code = str( code )
            self.__data[ 'fund' ] = self.__code

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, name ):
        if name is not None:
            self.__name = str( name )
            self.__data[ 'name' ] = self.__name

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, cache ):
        if isinstance( cache, dict ):
            self.__data = cache

    @property
    def table( self ):
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, frame ):
        if isinstance( frame, pd.DataFrame ):
            self.__frame = frame

    def __str__( self ):
        return self.__code

    def __init__( self, code ):
        self.__code = str( code )
        self.__data = { 'fund': self.__code }
        self.__frame = pd.DataFrame


class ProgramArea( ):
    '''defines the ProgramArea class'''
    __code = None
    __name = None
    __data = None
    __frame = None

    @property
    def code( self ):
        if self.__code is not None:
            return self.__code

    @code.setter
    def code( self, code ):
        if code is not None:
            self.__code = str( code )

    @property
    def name( self ):
        if self.__name is not None:
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
    def data( self, cache ):
        if isinstance( cache, dict ):
            self.__data = cache

    @property
    def table( self ):
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, frame ):
        if isinstance( frame, pd.DataFrame ):
            self.__frame = frame

    def __str__( self ):
        return self.__code

    def __init__( self, code ):
        self.__code = str( code )
        self.__data = { 'fund': self.__code }
        self.__frame = pd.DataFrame


class ProgramProject( ):
    '''Defines the ProgramProject Class'''
    __code = None
    __name = None
    __description = None
    __data = None
    __frame = None

    @property
    def code( self ):
        if self.__code is not None:
            return self.__code

    @code.setter
    def code( self, code ):
        if code is not None:
            self.__code = str( code )

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, name ):
        if name is not None:
            self.__name = str( name )

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

    @data.setter
    def data( self, cache ):
        if isinstance( cache, dict ):
            self.__data = cache

    @property
    def table( self ):
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, frame ):
        if isinstance( frame, pd.DataFrame ):
            self.__frame = frame

    def __str__( self ):
        return self.__code

    def __init__( self, code ):
        self.__code = str( code )
        self.__data = { 'fund': self.__code }
        self.__frame = pd.DataFrame


class ResponsibilityCenter( ):
    '''Defines the ResponsibilityCenter Class'''
    __code = None
    __name = None
    __data = None
    __frame = None

    @property
    def code( self ):
        if self.__code is not None:
            return self.__code

    @code.setter
    def code( self, code ):
        if code is not None:
            self.__code = str( code )

    @property
    def name( self ):
        if self.__name is not None:
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
    def data( self, value ):
        if isinstance( value, dict ):
            self.__data = value

    @property
    def table( self ):
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, value ):
        if isinstance( value, pd.DataFrame ):
            self.__frame = value

    def __str__( self ):
        return self.__code

    def __init__( self, code ):
        self.__code = str( code )
        self.__data = { 'fund': self.__code }
        self.__frame = pd.DataFrame


class ResourcePlanningOffice( ):
    '''defines the ResponsiblePlanningOffice class'''
    __code = None
    __name = None
    __data = None
    __frame = None

    @property
    def code( self ):
        if self.__code is not None:
            return self.__code

    @code.setter
    def code( self, code ):
        if code is not None:
            self.__code = str( code )

    @property
    def name( self ):
        if self.__name is not None:
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
    def data( self, cache ):
        if isinstance( cache, dict ):
            self.__data = cache

    @property
    def table( self ):
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, frame ):
        if isinstance( frame, pd.DataFrame ):
            self.__frame = frame

    def __str__( self ):
        return self.__code

    def __init__( self, code ):
        self.__code = str( code )
        self.__data = { 'fund': self.__code }
        self.__frame = pd.DataFrame


class ProgramResultsCode( ):
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
    __frame = None

    @property
    def rpio( self ):
        if self.__rpio is not None:
            return self.__rpio

    @rpio.setter
    def rpio( self, code ):
        if code is not None:
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
        if code is not None:
            self.__fund = ResourcePlanningOffice( str( code ) )
            self.__data[ 'Fund' ] = self.__fund.code

    @property
    def ah( self ):
        if self.__ah is not None:
            return AllowanceHolder( self.__ah )

    @ah.setter
    def ah( self, code ):
        if code is not None:
            self.__ah = AllowanceHolder( str( code ) )
            self.__data[ 'AH' ] = self.__ah.code

    @property
    def account( self ):
        if self.__account is not None:
            return self.__account

    @account.setter
    def account( self, code ):
        if code is not None:
            self.__account = Account( str( code ) )
            self.__data[ 'Account' ] = self.__account.code

    @property
    def activity( self ):
        if self.__account is not None:
            self.__activity = str( self.__account[ 5:2 ] )
            return Activity( self.__activity )

    @activity.setter
    def activity( self, code ):
        if code is not None:
            self.__activity = Activity( str( code ) )
            self.__data[ 'Activity' ] = self.__activity.code

    @property
    def org( self ):
        if self.__org is not None:
            return Organization( self.__org )

    @org.setter
    def org( self, code ):
        if code is not None:
            self.__org = Organization( str( code ) )
            self.__data[ 'ORG' ] = self.__org.code

    @property
    def rc( self ):
        if self.__rc is not None:
            return self.__rc

    @rc.setter
    def rc( self, code ):
        if code is not None:
            self.__rc = ResponsibilityCenter( str( code ) )
            self.__data[ 'RC' ] = self.__rc.code

    @property
    def boc( self ):
        if self.__boc is not None:
            return self.__boc

    @boc.setter
    def boc( self, code ):
        if code is not None:
            self.__rpio = BudgetObjectClass( str( code ) )
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

    @data.setter
    def data( self, cache ):
        if isinstance( cache, dict ):
            self.__data = cache

    @property
    def table( self ):
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, frame ):
        if isinstance( frame, pd.DataFrame ):
            self.__frame = frame

    def __str__( self ):
        if self.__account.code is not None:
            return self.__account.code

    def __init__( self, code, amount = 0 ):
        '''Initializes the PRC class'''
        self.__account = Account( str( code ) )
        self.__bfy = BudgetFiscalYear( dt.datetime.year )
        self.__amount = amount
        self.__data = { 'fund': self.__account.code,
                        'account': self.__account,
                        'amount': self.__amount }
        self.__frame = pd.DataFrame


class RegionalOffice( ):
    '''Defines a regional RPIO'''
    __rpio = None
    __name = None
    __data = None
    __frame = None

    @property
    def rpio( self ):
        if self.__rpio is not None:
            return self.__rpio

    @rpio.setter
    def rpio( self, code ):
        if code is not None:
            self.__rpio = ResourcePlanningOffice( code )
            self.__data[ 'rpio' ] = self.__rpio

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, name ):
        if name is not None:
            self.__name = str( name )
            self.__data[ 'name' ] = self.__name

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, cache ):
        if isinstance( cache, dict ):
            self.__data = cache

    @property
    def table( self ):
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, frame ):
        if isinstance( frame, pd.DataFrame ):
            self.__frame = frame

    def __str__( self ):
        if self.__rpio is not None:
            return str( self.__rpio )

    def __init__( self, rpio ):
        self.__rpio = ResourcePlanningOffice( str( rpio ) )
        self.__name = self.__rpio.name
        self.__data = { 'rpio': self.__rpio,
                        'name': self.__name }
        self.__frame = pd.DataFrame


class SiteProject( ):
    '''Defines the Site Project Code Class'''
    __epaid = None
    __ssid = None
    __actioncode = None
    __operableunit = None
    __code = None
    __name = None
    __data = None
    __frame = None

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
        if code is not None:
            self.__actioncode = str( code )
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
        if self.__code is not None:
            return self.__code

    @code.setter
    def code( self, code ):
        if code is not None:
            self.__code = str( code )
            self.__data[ 'fund' ] = self.__code

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, name ):
        if name is not None:
            self.__name = str( name )
            self.__data[ 'name' ] = self.__name

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, cache ):
        if isinstance( cache, dict ):
            self.__data = cache

    @property
    def table( self ):
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, frame ):
        if isinstance( frame, pd.DataFrame ):
            self.__frame = frame

    def __str__( self ):
        return self.__code

    def __init__( self, code ):
        self.__code = str( code )
        self.__ssid = self.__code[ 0: 4 ]
        self.__actioncode = self.__code[ 4:6 ]
        self.__operableunit = self.__code[ 6:9 ]
        self.__data = { 'fund': self.__code }
        self.__frame = pd.DataFrame


class HeadquartersOffice( ):
    '''Defines the HQ class'''
    __rpio = None
    __name = None
    __title = None
    __data = None
    __frame = None

    @property
    def rpio( self ):
        if self.__rpio is not None:
            return self.__rpio

    @rpio.setter
    def rpio( self, code ):
        if code is not None:
            self.__rpio = str( code )
            self.__data[ 'rpio' ] = ResourcePlanningOffice( self.__rpio )

    @property
    def name( self ):
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, name ):
        if name is not None:
            self.__name = str( name )
            self.__data[ 'name' ] = self.__name

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
    def data( self, cache ):
        if isinstance( cache, dict ):
            self.__data = cache

    @property
    def table( self ):
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, frame ):
        if isinstance( frame, pd.DataFrame ):
            self.__frame = frame

    def __str__( self ):
        if not self.__name == '':
            return self.__name

    def __init__( self, rpio ):
        self.__rpio = ResourcePlanningOffice( str( rpio ) )
        self.__name = self.__rpio.name
        self.__data = { 'rpio': self.__rpio,
                        'name': self.__name }
        self.__frame = pd.DataFrame


class FederalHoliday( ):
    '''Defines the FederalHoliday class'''
    __bfy = None
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
    __list = None
    __date = None
    __day = None
    __month = None
    __year = None
    __data = None
    __frame = None

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
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, name ):
        if name in self.__list:
            self.__name = name

    @property
    def date( self ):
        if self.__date is not None:
            return self.__date

    @property
    def day( self ):
        if self.__day is not None:
            return self.__day

    @property
    def month( self ):
        if self.__month is not None:
            return self.__month

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, cache ):
        if isinstance( cache, dict ):
            self.__data = cache

    @property
    def list( self ):
        if self.__list is not None:
            return self.__list

    @property
    def table( self ):
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, frame ):
        if isinstance( frame, pd.DataFrame ):
            self.__frame = frame

    @property
    def observance( self ):
        if self.__observance is not None:
            return self.__observance

    def columbusday( self ):
        if self.__year is not None:
            __start = dt.datetime( self.__year, 10, 1 )
            __end = dt.datetime( self.__year, 10, 31 )
            __delta = ( __start - __end ).days
            for i in range( 1, __delta - 1 ):
                d = dt.datetime( self.__year, 10, __start.day + i )
                if ( 15 < d.day < 28 ) and dt.datetime( self.__year, 10, d.day ).isoweekday( ) == 1:
                    self.__columbus = dt.datetime( self.__year, 10, d.day )
                    return self.__columbus

    def veteransday( self ):
        if self.__year is not None:
            self.__veterans = dt.datetime( self.__year, 11, 11 )
            return self.__veterans

    def thanksgivingday( self ):
        if self.__year is not None:
            __thursday = list( )
            __month = dt.datetime( self.__year, 11, 15 ) - dt.datetime( self.__year, 11, 31 )
            for i in range( 1, __month.days - 1 ):
                if dt.datetime( self.__year, 11, i ).isoweekday( ) == 4:
                    __thursday.append( dt.datetime( self.__year, 11, i ) )
            m = len( __thursday )
            if m == 4:
                y = __thursday[ m ].date().year
                m = __thursday[ m ].date().month
                d = __thursday[ m ].date().day
                self.__thanksgiving = dt.datetime( y, m, d )
                return self.__thanksgiving

    def christmasday( self ):
        if self.__year is not None:
            self.__christmas = dt.datetime( self.__year, 12, 25 )
            return self.__christmas

    def newyearsday( self ):
        if self.__year is not None:
            self.__newyearsday = dt.datetime( self.__year, 1, 1 )
            return self.__newyearsday

    def martinlutherkingday( self ):
        if self.__year is not None:
            __start = dt.datetime( self.__year, 1, 15 )
            __end = dt.datetime( self.__year, 1, 31 )
            __delta = ( __start - __end ).days
            for i in range( __delta ):
                d = dt.datetime( self.__year, 1, __start.day + i )
                if ( 15 < d.day < 31) and dt.datetime( self.__year, 1, d.day ).isoweekday( ) == 1:
                    self.__martinlutherking = dt.datetime( self.__year, 1, d.day )
                    return self.__martinlutherking

    def washingtonsday( self ):
        if self.__year is not None:
            __start = dt.datetime( self.__year, 2, 15 )
            __end = dt.datetime( self.__year, 2, 28 )
            __delta = ( __start - __end ).days
            for i in range( __delta ):
                d = dt.datetime( self.__year, 2, __start.day + i )
                if (15 < d.day < 28) and dt.datetime( self.__year, 2, d.day ).isoweekday( ) == 1:
                    self.__washingtons = dt.datetime( self.__year, 2, d.day )
                    return self.__washingtons

    def memorialday( self ):
        if self.__year is not None:
            __monday = list( )
            __month = dt.datetime( self.__year, 5, 1 ) - dt.datetime( self.__year, 5, 31 )
            for i in range( 1, __month.days - 1 ):
                if dt.datetime( self.__year, 5, i ).isoweekday( ) == 1:
                    __monday.append( dt.datetime( self.__year, 5, i ) )
            m = len( __monday )
            y = __monday[ 0 ].date( ).year
            m = __monday[ 0 ].date( ).month
            d = __monday[ 0 ].date( ).day
            self.__memorial = dt.datetime( y, m, d )
            return self.__memorial

    def juneteenthday( self ):
        if self.__year is not None:
            self.__juneteenth = dt.datetime( self.__year, 6, 19 )
            return self.__juneteenth

    def independence( self ):
        if self.__year is not None:
            self.__independence = dt.datetime( self.__year, 7, 4 )
            return self.__independence

    def laborday( self ):
        if self.__year is not None:
            __monday = list( )
            __month = dt.date( self.__year, 9, 1 ) - dt.date( self.__year, 9, 31 )
            for i in range( 1, __month.days - 1 ):
                if dt.datetime( self.__year, 9, i ).isoweekday( ) == 1:
                    __monday.append( dt.datetime( self.__year, 9, i ) )
            y = __monday[ 0 ].date( ).year
            m = __monday[ 0 ].date( ).month
            d = __monday[ 0 ].date( ).day
            self.__labor = dt.datetime( y, m, d )
            return self.__labor

    def dayofweek( self, day ):
        if 0 < int( day ) < 8 and int( day ) == 1:
            self.__day = 'Monday'
            return self.__day
        elif 0 < int( day ) < 8 and int( day ) == 2:
            self.__day = 'Tuesday'
            return self.__day
        elif 0 < int( day ) < 8 and int( day ) == 3:
            self.__day = 'Wednesday'
            return self.__day
        elif 0 < int( day ) < 8 and int( day ) == 4:
            self.__day = 'Thursday'
            return self.__day
        elif 0 < int( day ) < 8 and int( day ) == 5:
            self.__day = 'Friday'
            return self.__day
        elif 0 < int( day ) < 8 and int( day ) == 6:
            self.__day = 'Saturday'
            return self.__day
        elif 0 < int( day ) < 8 and int( day ) == 7:
            self.__day = 'Sunday'
            return self.__day

    def setdate( self, name ):
        if isinstance( name, str ) and name in self.__list:
            if name == 'Columbus':
                self.__date = self.columbusday( )
                return dt.datetime( self.__date.year,
                    self.__month, self.__day )
            elif name == 'Veterans':
                self.__date = self.veteransday( )
                return dt.datetime( self.__date.year,
                    self.__month, self.__day )
            elif name == 'Thanksgiving':
                self.__date = self.thanksgivingday( )
                return dt.datetime( self.__date.year,
                    self.__month, self.__day )
            elif name == 'Christmas':
                self.__date = self.christmasday( )
                return dt.datetime( self.__date.year,
                    self.__month, self.__day )
            elif name == 'NewYearsDay':
                self.__date = self.newyearsday( )
                return dt.datetime( self.__date.year,
                    self.__month, self.__day )
            elif name == 'MartinLutherKing':
                self.__date = self.martinlutherkingday( )
                return dt.datetime( self.__date.year,
                    self.__month, self.__day )
            elif name == 'Washingtons':
                self.__date = self.washingtonsday( )
                return dt.datetime( self.__date.year,
                    self.__month, self.__day )
            elif name == 'Memorial':
                self.__date = self.memorialday( )
                return dt.datetime( self.__date.year,
                    self.__month, self.__day )
            elif name == 'Juneteenth':
                self.__date = self.juneteenthday( )
                return dt.datetime( self.__date.year,
                    self.__month, self.__day )
            elif name == 'Labor':
                self.__date = self.laborday( )
                return dt.datetime( self.__date.year,
                    self.__month, self.__day )

    def setname( self, name ):
        if isinstance( name, str ) and name != '':
            if name in self.__list and name == 'NewYearsDay':
                self.__name = name
                return self.__name
            elif name == 'MartinLutherKing':
                self.__name = name
                return self.__name
            elif name == 'Veterans':
                self.__name = name
                return self.__name
            elif name == 'Washingtons':
                self.__name = name
                return self.__name
            elif name == 'Memorial':
                self.__name = name
                return self.__name
            elif name == 'Juneteenth':
                self.__name = name
                return self.__name
            elif name == 'Independence':
                self.__name = name
                return self.__name
            elif name == 'Labor':
                self.__name = name
                return self.__name
            elif name == 'Thanksgiving':
                self.__name = name
                return self.__name
            elif name == 'Christmas':
                self.__name = name
                return self.__name
            else:
                self.__name = 'NS'
                return self.__name

    def __str__( self ):
        if not self.__name == '':
            return self.__name

    def __init__( self, bfy, name ):
        self.__list = [ 'NewYearsDay', 'MartinLutherKing', 'Washingtons',
                        'Memorial', 'Juneteenth', 'Independence', 'Labor',
                        'Columbus', 'Veterans', 'Thanksgiving', 'Christmas' ]
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
        self.__bfy = bfy if isinstance( bfy, str ) else str( dt.date.year )
        self.__name = self.setname( name )
        self.__date = self.setdate( name )
        self.__day = self.dayofweek( self.__date.day )
        self.__month = self.__date.month
        self.__year = self.__date.year
        self.__data = { 'bfy': self.__bfy,
                        'name': self.__name }
        self.__frame = pd.DataFrame


class Commitment( ):
    '''Defines the commitment class.'''
    __amount = None
    __account = None
    __document = None
    __bfy = None
    __fund = None
    __org = None
    __boc = None
    __data = None
    __frame = None

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
        if code is not None:
            self.__account = code
            self.__data[ 'account' ] = self.__account

    @property
    def document( self ):
        if self.__document is not None:
            return self.__document

    @document.setter
    def document( self, doc ):
        if doc is not None:
            self.__document = doc
            self.__data[ 'document' ] = self.__document

    @property
    def org( self ):
        if self.__org is not None:
            return self.__org

    @org.setter
    def org( self, code ):
        if code is not None:
            self.__org = Organization( code )
            self.__data[ 'org' ] = self.__org.code

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, year ):
        if isinstance( BudgetFiscalYear, year ):
            self.__bfy = year
            self.__data[ 'bfy' ] = self.__bfy.firstyear

    @property
    def fund( self ):
        if self.__fund is not None:
            return self.__fund

    @fund.setter
    def fund( self, code ):
        if code is not None:
            self.__fund = Fund( code )
            self.__data[ 'fund' ] = code

    @property
    def boc( self ):
        if self.__boc is not None:
            return self.__boc

    @boc.setter
    def boc( self, code ):
        if code is not None:
            self.__boc = BudgetObjectClass( code )
            self.__data[ 'boc' ] = code

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, cache ):
        if isinstance( cache, dict ):
            self.__data = cache

    @property
    def table( self ):
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, frame ):
        if isinstance( frame, pd.DataFrame ):
            self.__frame = frame

    def __str__( self ):
        if self.__amount is not None:
            return str( self.__amount )

    def __init__( self, amount ):
        self.__amount = float( amount )
        self.__data = { 'amount': self.__amount,
                        'account': None,
                        'document': None,
                        'org': None,
                        'bfy': None,
                        'fund': None,
                        'boc': None }
        self.__frame = pd.DataFrame


class OpenCommitment( ):
    '''Defines the commitment class.'''
    __amount = None
    __account = None
    __document = None
    __bfy = None
    __fund = None
    __org = None
    __boc = None
    __data = None
    __frame = None

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
        if code is not None:
            self.__account = Account( code )
            self.__data[ 'account' ] = code

    @property
    def document( self ):
        if self.__document is not None:
            return self.__document

    @document.setter
    def document( self, doc ):
        if doc is not None:
            self.__document = doc
            self.__data[ 'document' ] = doc

    @property
    def org( self ):
        if self.__org is not None:
            return self.__org

    @org.setter
    def org( self, code ):
        if code is not None:
            self.__org = Organization( code )
            self.__data[ 'org' ] = code

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, year ):
        if year is not None:
            self.__bfy = BudgetFiscalYear( year )
            self.__data[ 'bfy' ] = year

    @property
    def fund( self ):
        if self.__fund is not None:
            return self.__fund

    @fund.setter
    def fund( self, code ):
        if code is not None:
            self.__fund = Fund( code )
            self.__data[ 'fund' ] = code

    @property
    def boc( self ):
        if self.__boc is not None:
            return self.__boc

    @boc.setter
    def boc( self, code ):
        if code is not None:
            self.__boc = BudgetObjectClass( code )
            self.__data[ 'boc' ] = code

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, cache ):
        if isinstance( cache, dict ):
            self.__data = cache

    @property
    def table( self ):
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, frame ):
        if isinstance( frame, pd.DataFrame ):
            self.__frame = frame

    def __str__( self ):
        if self.__amount is not None:
            return str( self.__amount )

    def __init__( self, amount ):
        self.__amount = float( amount )
        self.__data = { 'amount': self.__amount,
                        'account': None,
                        'document': None,
                        'org': None,
                        'bfy': None,
                        'fund': None,
                        'boc': None }
        self.__frame = pd.DataFrame


class Obligation( ):
    '''Defines the commitment class.'''
    __amount = None
    __account = None
    __document = None
    __bfy = None
    __fund = None
    __org = None
    __boc = None
    __data = None
    __frame = None

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
        if code is not None:
            self.__account = Account( code )
            self.__data[ 'account' ] = code

    @property
    def document( self ):
        if self.__document is not None:
            return self.__document

    @document.setter
    def document( self, doc ):
        if doc is not None:
            self.__document = doc
            self.__data[ 'document' ] = doc

    @property
    def org( self ):
        if self.__org is not None:
            return self.__org

    @org.setter
    def org( self, code ):
        if code is not None:
            self.__org = Organization( code )
            self.__data[ 'org' ] = code

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, year ):
        if year is not None:
            self.__bfy = BudgetFiscalYear( year )
            self.__data[ 'bfy' ] = year

    @property
    def fund( self ):
        if self.__fund is not None:
            return self.__fund

    @fund.setter
    def fund( self, code ):
        if code is not None:
            self.__fund = Fund( code )
            self.__data[ 'fund' ] = code

    @property
    def boc( self ):
        if self.__boc is not None:
            return self.__boc

    @boc.setter
    def boc( self, code ):
        if code is not None:
            self.__boc = BudgetObjectClass( code )
            self.__data[ 'boc' ] = code

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, cache ):
        if isinstance( cache, dict ):
            self.__data = cache

    @property
    def table( self ):
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, frame ):
        if isinstance( frame, pd.DataFrame ):
            self.__frame = frame

    def __str__( self ):
        if self.__amount is not None:
            return str( self.__amount )

    def __init__( self, amount ):
        self.__amount = float( amount )
        self.__data = { 'amount': self.__amount,
                        'account': None,
                        'document': None,
                        'org': None,
                        'bfy': None,
                        'fund': None,
                        'boc': None }
        self.__frame = pd.DataFrame


class Deobligation( ):
    '''Defines the commitment class.'''
    __amount = None
    __account = None
    __document = None
    __bfy = None
    __fund = None
    __org = None
    __boc = None
    __data = None
    __frame = None

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
        if code is not None:
            self.__account = Account( code )
            self.__data[ 'account' ] = code

    @property
    def dcn( self ):
        if self.__document is not None:
            return self.__document

    @dcn.setter
    def dcn( self, doc ):
        if doc is not None:
            self.__document = doc
            self.__data[ 'document' ] = doc

    @property
    def org( self ):
        if self.__org is not None:
            return self.__org

    @org.setter
    def org( self, code ):
        if code is not None:
            self.__org = Organization( code )
            self.__data[ 'org' ] = code

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, year ):
        if year is not None:
            self.__bfy = BudgetFiscalYear( year )
            self.__data[ 'bfy' ] = year

    @property
    def fund( self ):
        if self.__fund is not None:
            return self.__fund

    @fund.setter
    def fund( self, code ):
        if code is not None:
            self.__fund = Fund( code )
            self.__data[ 'fund' ] = code

    @property
    def boc( self ):
        if self.__boc is not None:
            return self.__boc

    @boc.setter
    def boc( self, code ):
        if code is not None:
            self.__boc = BudgetObjectClass( code )
            self.__data[ 'boc' ] = code

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, cache ):
        if isinstance( cache, dict ):
            self.__data = cache

    @property
    def table( self ):
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, frame ):
        if isinstance( frame, pd.DataFrame ):
            self.__frame = frame

    def __str__( self ):
        if self.__amount is not None:
            return str( self.__amount )

    def __init__( self, amount ):
        self.__amount = float( amount )
        self.__data = { 'amount': self.__amount,
                        'account': None,
                        'document': None,
                        'org': None,
                        'bfy': None,
                        'fund': None,
                        'boc': None }
        self.__frame = pd.DataFrame


class UnliquidatedObligation( ):
    '''Defines the commitment class.'''
    __amount = None
    __account = None
    __document = None
    __bfy = None
    __fund = None
    __org = None
    __boc = None
    __data = None
    __frame = None

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
        if isinstance( doc, str ):
            self.__document = doc

    @property
    def org( self ):
        if self.__org is not None:
            return self.__org

    @org.setter
    def org( self, oc ):
        if oc is not None:
            self.__org = Organization( oc )
            self.__data[ 'org' ] = self.__org.code

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return self.__bfy.firstyear

    @bfy.setter
    def bfy( self, year ):
        if year is not None:
            self.__bfy = BudgetFiscalYear( year )
            self.__data[ 'bfy' ] = year

    @property
    def fund( self ):
        if self.__fund is not None:
            return self.__fund

    @fund.setter
    def fund( self, fund ):
        if isinstance( fund, Fund ):
            self.__fund = fund

    @property
    def boc( self ):
        if self.__boc is not None:
            return self.__boc

    @boc.setter
    def boc( self, code ):
        if code is not None and isinstance( code, str ):
            self.__boc = BudgetObjectClass( code )

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @data.setter
    def data( self, cache ):
        if isinstance( cache, dict ):
            self.__data = cache

    @property
    def table( self ):
        if self.__frame is not None:
            return self.__frame

    @table.setter
    def table( self, frame ):
        if isinstance( frame, pd.DataFrame ):
            self.__frame = frame

    def __str__( self ):
        if self.__amount is not None:
            return str( self.__amount )

    def __init__( self, amount ):
        self.__amount = float( amount )
        self.__data = { 'amount': self.__amount,
                        'account': None,
                        'document': None,
                        'org': None,
                        'bfy': None,
                        'fund': None,
                        'boc': None }
        self.__frame = pd.DataFrame


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
    __frame = None

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
        if code is not None:
            self.__account = Account( code )
            self.__data[ 'account' ] = code

    @property
    def document( self ):
        if self.__document is not None:
            return self.__document

    @document.setter
    def document( self, doc ):
        if not doc == '':
            self.__document = doc

    @property
    def org( self ):
        if self.__org is not None:
            return self.__org

    @org.setter
    def org( self, code ):
        if code is not None:
            self.__org = Organization( code )
            self.__data[ 'org' ] = self.__org.code

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, year ):
        if isinstance( year, BudgetFiscalYear ):
            self.__bfy = year

    @property
    def fund( self ):
        if self.__fund is not None:
            return self.__fund

    @fund.setter
    def fund( self, fc ):
        if isinstance( fc, Fund ):
            self.__fund = fc

    @property
    def boc( self ):
        if self.__boc is not None:
            return self.__boc

    @boc.setter
    def boc( self, bc ):
        if isinstance( bc, BudgetObjectClass ):
            self.__boc = bc

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @property
    def table( self ):
        if self.__frame is not None:
            return self.__frame

    def __str__( self ):
        if self.__amount is not None:
            return str( self.__amount )

    def __init__( self, amount ):
        self.__amount = float( amount )
        self.__data = { 'amount': self.__amount,
                        'account': None,
                        'document': None,
                        'org': None,
                        'bfy': None,
                        'fund': None,
                        'boc': None }
        self.__frame = pd.DataFrame
        self.__frame = pd.DataFrame
