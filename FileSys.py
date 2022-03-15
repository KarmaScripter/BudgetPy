import os

import os as fp
import io as fi
import datetime as dt
import openpyxl as xl
import zipfile as zp

class BudgetPath():
    '''Defines the BudgetPath class'''
    __base = None
    __path = None
    __ext = None
    __currdir = None
    __report = None

    @property
    def base( self ):
        if self.__base is not None:
            return self.__base

    @base.setter
    def base( self, path ):
        if path is not None and fp.path.exists( path ):
            self.__base = str( path )

    @property
    def name( self ):
        '''Returns string representing the name of the path 'base' '''
        if fp.path.exists( self.__base ):
            return str( list( fp.path.split( self.__base ) )[ 1 ] )

    @name.setter
    def name( self, path ):
        '''Returns string representing the name of the path 'base' '''
        if fp.path.exists( path ):
            self.__path = str( list( fp.path.split( self.__base ) )[ 1 ] )

    @property
    def path( self ):
        if self.__path is not None:
            return self.__path

    @path.setter
    def path( self, base ):
        if fp.path.exists( base ):
            self.__path = base

    @property
    def exists( self ):
        if fp.path.exists( self.__path ):
            return True

    @property
    def isfolder( self ):
        if fp.path.isdir( self.__path ):
            return True

    @property
    def isfile( self ):
        if fp.path.isfile( self.__path ):
            return True

    @property
    def extension( self ):
        if self.__ext is not None:
            return str( self.__ext )

    @extension.setter
    def extension( self, ext ):
        if ext is not None:
            self.__ext = str( ext )

    @property
    def current( self ):
        if fp.path.exists( self.__currdir ):
            return self.__currdir

    @current.setter
    def current( self, path ):
        '''Set the current directory to 'path' '''
        if fp.path.exists( path ):
            fp.chdir( path )
            self.__currdir = path

    def verify( self, other ):
        '''Verifies if the parameter 'other' exists'''
        if fp.path.exists( other ):
            return True

    def getextension( self, other ):
        '''Returns string representing the file extension of 'other' '''
        if fp.path.exists( other ):
            return list( fp.path.splitext( other ) )[ 1 ]

    def getreport( self ):
        if self.__report is not None:
            return self.__report

    def join( self, first, second ):
        ''' Concatenates 'first' to 'second' '''
        if fp.path.exists( first ) and fp.path.exists( second ):
            return fp.path.join( first, second )

    def __init__( self, filepath ):
        self.__base = str( filepath )
        self.__path = self.__base
        self.__currdir = fp.getcwd()
        self.__ext = fp.path.split( self.__path )
        self.__report = r'etc\templates\report\ReportBase.xlsx'

class BudgetFile( fi.FileIO ):
    '''Defines the BudgetFile Class'''
    __base = None
    __name = None
    __path = None
    __size = None
    __extension = None
    __directory = None
    __drive = None
    __created = None
    __modified = None
    __accessed = None
    __currdir = None
    __contents = [ ]

    @property
    def base( self ):
        if self.__base is not None:
            return self.__base

    @base.setter
    def base( self, path ):
        if isinstance( path , str ) and not path == '':
            self.__base = path

    @property
    def name( self ):
        '''Get the name property'''
        if not self.__name == '':
            return self.__name

    @name.setter
    def name( self, path ):
        '''Set the name property'''
        if fp.path.exists( path ):
            self.__name = fp.path.basename( path )

    @property
    def path( self ):
        if fp.path.isfile( self.__path ):
            return str( self.__path )

    @path.setter
    def path( self, base ):
        if fp.path.exists( base ):
            self.__path = str( base )

    @property
    def size( self ):
        if self.__base is not None:
            return float( self.__size )

    @size.setter
    def size( self, num ):
        if num is not None:
            self.__size = float( num )

    @property
    def directory( self ):
        if self.__directory is not None:
            return self.__directory

    @directory.setter
    def directory( self, path ):
        if fp.path.isdir( path ):
            self.__directory = str( fp.path.dirname( path ) )

    @property
    def extension( self ):
        if self.__extension is not None:
            return self.__extension

    @extension.setter
    def extension( self, ext ):
        if ext is not None:
            self.__extension = ext

    @property
    def drive( self ):
        if self.__drive is not None:
            return self.__drive

    @drive.setter
    def drive( self, path ):
        if fp.path.ismount( path ):
            self.__drive = str( path )

    @property
    def modified( self ):
        if self.__modified is not None:
            return self.__modified

    @modified.setter
    def modified( self, yr, mo = 1, dy = 1 ):
        if dt.date( yr, mo, dy ):
            self.__modified = dt.date( yr, mo, dy )

    @property
    def accessed( self ):
        if self.__accessed is not None:
            return self.__accessed

    @accessed.setter
    def accessed( self, yr, mo = 1, dy = 1 ):
        if dt.date( yr, mo, dy ):
            self.__accessed = dt.date( yr, mo, dy )

    @property
    def created( self ):
        if self.__created is not None:
            return self.__created

    @created.setter
    def created( self, yr, mo = 1, dy = 1 ):
        if dt.date( yr, mo, dy ):
            self.__created = dt.date( yr, mo, dy )

    @property
    def current( self ):
        if fp.path.exists( self.__currdir ):
            return self.__currdir

    @current.setter
    def current( self, path ):
        '''Set the current directory to 'path' '''
        if fp.path.exists( path ):
            fp.chdir( path )
            self.__currdir = path

    def rename( self, other ):
        '''Renames the current file to 'other' '''
        if isinstance( other, str ) and not other == '':
            fp.rename( self.__name, other )
            self.__name = other
            return self.__name

    def move( self, destination ):
        '''renames current file'''
        if fp.path.exists( self.__base ):
            return fp.path.join( self.__name, destination )

    def create( self, other ):
        ''' creates and returns 'path' file '''
        if other is not None:
            fp.mkdir( other )

    def exists( self, other ):
        '''determines if an external file exists'''
        if other is not None:
            return fp.path.exists( other )

    def delete( self, other ):
        ''' deletes file at 'self.__opath'   '''
        if fp.path.isfile( other ):
            fp.remove( other )

    def getsize( self, other ):
        '''gets the size of another file'''
        if self.__base is not None and fp.path.exists( other ):
            return fp.path.getsize( other )

    def getdrive( self, other ):
        '''gets the drive of another file'''
        if fp.path.exists( other ):
            return str( list( fp.path.splitdrive( other ) )[ 0 ] )

    def getextension( self, other ):
        ''' gets and returns extension of 'path' 'file' '''
        if other is not None and fp.path.isfile( other ):
            return str( list( fp.path.splitext( other ) )[ 1 ] )

    def readlines( self, other ):
        '''reads all lines in 'path' into a list
            then returns the list '''
        lines = [ ]
        count = len( self.__contents )
        if other is not None and fp.path.isfile( other ):
            file = open( other, 'r' )
            for line in file.readlines():
                lines.append( line )
            self.__contents.append( lines )
        if len( lines ) > 0 and len( self.__contents ) > count:
            return lines

    def readline( self, other ):
        '''reads a single line from the file into a string
            then returns the string'''
        count = len( self.__content )
        if fp.path.isfile( other ):
            line = open( self.__path, 'r' ).readline()
            self.__content.append( line )
            if len( self.__content ) > count:
                yield from iter( self.__content )

    def writelines( self, lines = None ):
        ''' writes the contents of 'lines' to self.__contents '''
        if fp.path.isfile( self.__path ) and isinstance( lines, list ):
            for line in lines:
                self.__contents.append( open( self.__path, 'w' ).write( line ) )

    def __init__( self, base ):
        super().__init__( base )
        self.__base =  base if not self.__base == '' else 'NS'
        self.__path = self.__base if not self.__base == '' else 'NS'
        self.__name = fp.path.basename( base ) if not base == '' else 'NS'
        self.__size = fp.path.getsize( base ) if not base == '' else 'NS'
        self.__directory = fp.path.dirname( self.__path ) \
            if fp.path.exists( base ) else 'NS'
        self.__extension = list( fp.path.splitext( base ) )[ 1 ] \
            if not base == '' else 'NS'
        self.__created = fp.path.getctime( base ) if not base == '' else 'NS'
        self.__accessed = fp.path.getatime( base ) if not base == '' else 'NS'
        self.__modified = fp.path.getmtime( base ) if not base == '' else 'NS'
        self.__currdir = fp.getcwd()
        self.__drive = str( list( fp.path.splitdrive( self.__path ) )[ 0 ] ) \
            if not base == '' else 'NS'
        self.__content = list()

class BudgetFolder():
    '''Defines the BudgetFolder Class'''
    __base = None
    __name = None
    __path = None
    __parent = None
    __dir = None
    __drive = None
    __current = None

    @property
    def base( self ):
        '''Get the base property'''
        if self.__base is not None:
            return self.__base

    @base.setter
    def base( self, path ):
        '''Set the base property'''
        if path is not None:
            self.__base = str( path )

    @property
    def name( self ):
        '''Returns string representing the name of the path 'base' '''
        if fp.path.exists( self.__base ):
            return str( list( fp.path.split( self.__base ) )[ 1 ] )

    @name.setter
    def name( self, path ):
        '''Returns string representing the name of the path 'base' '''
        if path is not None:
            self.__path = str( list( fp.path.split( self.__base ) )[ 1 ] )

    @property
    def directory( self ):
        '''Returns string representing the name of the path 'base' '''
        if not self.__dir == '':
            return self.__dir

    @directory.setter
    def directory( self, path ):
        '''Returns string representing the name of the path 'base' '''
        if os.path.isdir( path ):
            self.__dir = path

    @property
    def path( self ):
        if not self.__path == '':
            return self.__path

    @path.setter
    def path( self, base ):
        if fp.path.exists( base ):
            self.__path = str( base )

    @property
    def parent( self ):
        if self.__parent is not None:
            return self.__parent

    @parent.setter
    def parent( self, path ):
        if fp.path.isdir( path ):
            self.__parent = str( path )

    @property
    def drive( self ):
        if self.__drive is not None:
            return self.__drive

    @drive.setter
    def drive( self, path ):
        if fp.path.ismount( path ):
            self.__drive = str( path )

    @property
    def current( self ):
        if self.__current is not None:
            return self.__current

    @current.setter
    def current( self, path ):
        if fp.path.exists( path ):
            fp.chdir( path )

    def files( self ):
        '''Iterates files in the base directory'''
        if fp.path.isdir( self.__base ):
            file_list = []
            for file in os.listdir( self.__base ):
                if os.path.isfile( file ):
                    file_list.append( file )

            return file_list

    def rename( self, new_name ):
        '''renames current file'''
        if self.__name is not None and isinstance( new_name, str ):
            return fp.rename( self.__name, new_name )

    def move( self, destination ):
        '''renames current file'''
        if not destination == '' and not fp.path.exists( destination ):
            return fp.path.join( self.__name, destination )

    def exists( self, other ):
        '''determines if the base file exists'''
        if not other == '' and fp.path.isdir( other ):
            return True

    def create( self, other ):
        if other is not None:
            fp.mkdir( other )

    def delete( self, other ):
        ''' deletes 'path' directory '''
        if other is not None and fp.path.isdir( other ):
            fp.rmdir( other )

    def getsize( self, other ):
        ''' gets and returns size of 'path' '''
        if other is not None and fp.path.isdir( other ):
            return fp.path.getsize( other )

    def getdrive( self, other ):
        ''' gets and returns parent directory of 'path' '''
        if other is not None and fp.path.isdir( other ):
            return fp.path.splitdrive( other )[ 0 ]

    def iterate( self ):
        '''iterates files in the base directory'''
        if fp.path.isdir( self.__base ):
            for i in fp.scandir( self.__base ):
                yield i

    def getfiles( self, other ):
        '''iterates files in the directory provided by 'other' '''
        if fp.path.exists( other ) and fp.path.isdir( other ):
            yield from fp.scandir( self.__base )

    def __init__( self, base ):
        self.__base = base
        self.__name = fp.path.basename( base ) if not base == '' else 'NS'
        self.__path = self.__base if not self.__base == '' else 'NS'
        self.__dir = fp.mkdir( self.__path )
        self.__parent = fp.path.dirname( base ) if not base == '' else 'NS'

class EmailMessage():
    ''' Represents an Email Item '''
    __from = None
    __to = None
    __subject = None
    __message = None
    __others = None

    @property
    def sender( self ):
        ''' Gets the sender's email address '''
        if self.__from is not None:
            return self.__from

    @sender.setter
    def sender( self, frm ):
        ''' Set the sender's email address '''
        if frm is not None:
            self.__from = str( frm )

    @property
    def receiver( self ):
        ''' Gets the sender's email address '''
        if self.__to is not None:
            return self.__to

    @receiver.setter
    def receiver( self, rec ):
        ''' Sets the receiver's email address '''
        if rec is not None:
            self.__to = str( rec )

    @property
    def subject( self ):
        ''' Gets the email's subject line '''
        if self.__subject is not None:
            return self.__subject

    @subject.setter
    def subject( self, sub ):
        ''' Sets the email's subject line '''
        if sub is not None:
            self.__to = str( sub )

    @property
    def body( self ):
        ''' Gets the email's subject line '''
        if self.__message is not None:
            return self.__message

    @body.setter
    def body( self, msg ):
        ''' Sets the email's subject line '''
        if msg is not None:
            self.__to = str( msg )

    @property
    def copy( self ):
        ''' Gets the addresses to send copies  '''
        if self.__others is not None:
            return self.__others

    @copy.setter
    def copy( self, copy ):
        ''' Sets the address's to send copies  '''
        if copy is not None:
            self.__others = list( copy )

    def __init__( self, frm = None, to = None,
                  body = None, sub = None, copy = None ):
        self.__from = str( frm )
        self.__to = str( to )
        self.__message = str( body )
        self.__others = list( copy )
        self.__subject = str( sub )

    def __str__( self ):
        if self.__message is not None:
            return self.__message

class EmailBuilder():
    ''' Helper class for generating email messages '''
    __from = None
    __to = None
    __subject = None
    __message = None
    __others = None

    @property
    def sender( self ):
        ''' Gets the sender's email address '''
        if self.__from is not None:
            return self.__from

    @sender.setter
    def sender( self, frm ):
        ''' Set the sender's email address '''
        if frm is not None:
            self.__from = str( frm )

    @property
    def receiver( self ):
        ''' Gets the sender's email address '''
        if self.__to is not None:
            return self.__to

    @receiver.setter
    def receiver( self, rec ):
        ''' Sets the receiver's email address '''
        if rec is not None:
            self.__to = str( rec )

    @property
    def subject( self ):
        ''' Gets the email's subject line '''
        if self.__subject is not None:
            return self.__subject

    @subject.setter
    def subject( self, sub ):
        ''' Sets the email's subject line '''
        if sub is not None:
            self.__to = str( sub )

    @property
    def body( self ):
        ''' Gets the email's subject line '''
        if self.__message is not None:
            return self.__message

    @body.setter
    def body( self, msg ):
        ''' Sets the email's subject line '''
        if msg is not None:
            self.__to = str( msg )

    @property
    def copy( self ):
        ''' Gets the addresses to send copies  '''
        if self.__others is not None:
            return self.__others

    @copy.setter
    def copy( self, copy ):
        ''' Sets the address's to send copies  '''
        if copy is not None:
            self.__others = list( copy )

    def __init__( self, frm, to,
                  body, sub, copy = None ):
        self.__from = str( frm )
        self.__to = str( to )
        self.__message = str( body )
        self.__others = list( copy )
        self.__subject = str( sub )

    def __str__( self ):
        if self.__message is not None:
            return self.__message

class ExcelFile():
    ''' Provides the spreadsheet for Budget Py reports '''
    __path = None
    __workbook = None
    __worksheet = None
    __name = None

    @property
    def name( self ):
        ''' Get the name of the workbook '''
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, filename ):
        if filename is not None and len( filename ) > 0:
            self.__name = str( filename )

    @property
    def workbook( self ):
        ''' Gets the report template '''
        if self.__path is not None:
            self.__workbook = self.__path
            return self.__workbook

    @workbook.setter
    def workbook( self, path ):
        ''' Gets the report template '''
        if fp.path.exists( path ):
            self.__workbook = path

    @property
    def worksheet( self ):
        ''' Gets the workbooks worksheet '''
        if self.__worksheet is not None:
            return self.__worksheet

    @worksheet.setter
    def worksheet( self, name ):
        ''' Gets the workbooks worksheet '''
        if not name == '':
            self.__worksheet = name

    def __init__( self, name ):
        self.__path = r'etc\templates\report\Excel.xlsx'
        self.__name = name if not name == '' else 'NS'

class ExcelReport():
    ''' Provides the spreadsheet for Budget Py reports '''
    __path = None
    __workbook = None
    __worksheet = None
    __name = None
    __rows = None
    __columns = None
    __dimensions = None

    @property
    def name( self ):
        ''' Get the name of the workbook '''
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, filename ):
        if filename is not None and len( filename ) > 0:
            self.__name = str( filename )

    @property
    def rows( self ):
        if self.__rows is not None:
            return self.__rows

    @rows.setter
    def rows( self, count ):
        if isinstance( count, int ) and count > 0:
            self.__rows = count

    @property
    def columns( self ):
        if self.__columns is not None:
            return self.__columns

    @columns.setter
    def columns( self, count ):
        if isinstance( count, int ) and count > 0:
            self.__columns = count

    @property
    def dimensions( self ):
        if self.__dimensions is not None:
            return self.__dimensions

    @dimensions.setter
    def dimensions( self, grid = () ):
        if isinstance( grid, tuple ) and len( grid ) < 3:
            self.__dimensions = grid

    @property
    def workbook( self ):
        ''' Gets the report template '''
        if self.__path is not None:
            self.__workbook = xl.open( self.__path )
            return self.__workbook

    @workbook.setter
    def workbook( self, path ):
        ''' Gets the report template '''
        if path is not None and fp.path.exists( path ):
            self.__workbook = xl.open( path )

    @property
    def worksheet( self ):
        ''' Gets the workbooks worksheet '''
        if self.__worksheet is not None:
            return self.__worksheet

    @worksheet.setter
    def worksheet( self, name ):
        ''' Gets the workbooks worksheet '''
        if self.__workbook is not None and name is not None:
            self.__workbook.worksheets.clear()
            self.__worksheet = self.__workbook.create_sheet( title = name, index = 1 )

    def __init__( self, name, rows = 46, cols = 12 ):
        self.__path = r'etc\templates\report\Excel.xlsx'
        self.__name = str( name )
        self.__rows = int( rows )
        self.__columns = int( cols )
        self.__dimensions = ( self.__rows, self.__columns )

class ZipFile():
    __name = None
    __opath = None
    __oext = None
    __zpath = None
    __zext = None
    __bfile = None

    @property
    def path( self ):
        if not self.__zpath == '':
            return self.__zpath

    @path.setter
    def path( self, pt ):
        if fp.path.exists( pt ) and fp.path.isfile( pt ):
            self.__opath = pt

    @property
    def name( self ):
        if not self.__name == '':
            return self.__name

    @name.setter
    def name( self, nm ):
        if not nm == '':
            self.__name = nm

    def create( self ):
        ''' Creates zip file'''
        if not self.__opath == '':
            zp.ZipFile( self.__zpath, 'w' ).write( self.__opath, self.__name )

    def unzip( self ):
        ''' Extracts zip file contents '''
        if fp.path.exists( self.__zpath ):
            file = zp.ZipFile( self.__zpath )
            file.extractall( self, self.__zpath )

    def __init__(self, path ):
        self.__zext = '.zip'
        self.__opath = str( path )
        self.__bfile = BudgetFile( self.__opath )
        self.__oext = self.__bfile.extension
        self.__zpath = self.__opath.replace( self.__oext, self.__zext )
        self.__name = os.path.basename( self.__opath )
