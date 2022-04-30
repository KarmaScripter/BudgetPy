from PIL import Image, ImageTk, ImageSequence
import PySimpleGUI as sg
from sys import exit


class FileDialog( ):
    '''class that renames a file'''
    def show( self ):
        sg.theme_background_color( '#0F0F0F' )
        sg.theme_element_text_color( '#ADDFF7' )
        sg.theme_input_background_color( '#0F0F0F' )
        sg.theme_text_color( '#ADDFF7' )
        sg.theme_element_background_color( '#0F0F0F' )
        sg.theme_text_element_background_color( '#0F0F0F' )
        __icon = r'C:\Users\terry\source\repos\BudgetPy\etc\ico\ninja.ico'
        __font = 'Roboto 8'
        layout = [ [ sg.Text( 'Search for File' ) ],
                   [ sg.Input( ), sg.FileBrowse( ) ],
                   [ sg.OK( ), sg.Cancel( ) ] ]
        window = sg.Window( 'Budget Execution', layout,
            font = __font,
            icon = __icon )
        event, values = window.read( )
        window.close( )


class FolderDialog( ):
    '''class that renames a folder'''
    def show( self ):
        sg.theme_background_color( '#0F0F0F' )
        sg.theme_element_text_color( '#ADDFF7' )
        sg.theme_input_background_color( '#0F0F0F' )
        sg.theme_text_color( '#ADDFF7' )
        sg.theme_element_background_color( '#0F0F0F' )
        sg.theme_text_element_background_color( '#0F0F0F' )
        __icon = r'C:\Users\terry\source\repos\BudgetPy\etc\ico\ninja.ico'
        __font = 'Roboto 8'
        layout = [ [ sg.Text( 'Search for Directory' ) ],
                   [ sg.Input( ), sg.FolderBrowse( ) ],
                   [ sg.OK( ), sg.Cancel( ) ] ]
        window = sg.Window( 'Budget Execution', layout,
            font = __font,
            icon = __icon )
        event, values = window.read( )
        window.close( )


class Error( ):
    '''class that displays error message'''
    def show( self ):
        sg.theme_background_color( '#0F0F0F' )
        sg.theme_element_text_color( '#ADDFF7' )
        sg.theme_input_background_color( '#0F0F0F' )
        sg.theme_text_color( '#ADDFF7' )
        sg.theme_element_background_color( '#0F0F0F' )
        sg.theme_text_element_background_color( '#0F0F0F' )
        __icon = r'C:\Users\terry\source\repos\BudgetPy\etc\ico\error.ico'
        __font = 'Roboto 9'
        __size = ( 500, 250 )
        layout = [ [ sg.Text( r'' ) ],
                   [ sg.Text( r'This is error text', font = 'Roboto 10', text_color = '#FF0820' ) ],
                   [ sg.Text( r'' ) ],
                   [ sg.Text( 'Module:', size = ( 10, 1 ) ), sg.Text( __name__, key = '-MOD-', size = ( 150, 1 )  ) ],
                   [ sg.Text( 'Class:', size = ( 10, 1 ) ), sg.Text( __class__.__name__, key = '-CLS-', size = ( 150, 1 )  ) ],
                   [ sg.Text( 'Method:', size = ( 10, 1 ) ), sg.Text( 'show( )', key = '-METHOD-', size = ( 150, 1 )  ) ],
                   [ sg.Text( r'', size = ( 1, 1 ) ) ],
                   [ sg.Text( r'', size = ( 1, 1 ) ) ] ]
        window = sg.Window( r'  Budget Execution', layout,
            icon = __icon,
            font = __font,
            size = __size )
        event, values = window.read( )
        sg.popup( 'Budget Error', event, values, values[ '-MOD-' ],
            values[ '-CLS-' ],
            values[ '-METHOD-' ],
            text_color = r'#ADDFF7',
            font = __font,
            icon = __icon )
        if event == sg.WIN_CLOSED or event == sg.WIN_X_EVENT:
            exit( 0 )
        window.close( )


class ContactForm( ):
    '''class that produces a contact input form'''
    def show( self ):
        sg.theme_background_color( '#0F0F0F' )
        sg.theme_element_text_color( '#ADDFF7' )
        sg.theme_input_background_color( '#0F0F0F' )
        sg.theme_text_color( '#ADDFF7' )
        sg.theme_element_background_color( '#0F0F0F' )
        sg.theme_text_element_background_color( '#0F0F0F' )
        __icon = r'C:\Users\terry\source\repos\BudgetPy\etc\ico\ninja.ico'
        __font = 'Roboto 8'
        __size = ( 15, 1 )
        layout = [ [ sg.Text( r'Please enter your Name, Address, Phone' ) ],
                   [ sg.Text( 'Name', size = __size ), sg.InputText( '1', key = '-NAME-' ) ],
                   [ sg.Text( 'Address', size = __size ), sg.InputText( '2', key = '-ADDRESS-' ) ],
                   [ sg.Text( 'Phone', size = __size ), sg.InputText( '3', key = '-PHONE-' ) ],
                   [ sg.Submit( ), sg.Cancel( ) ] ]
        window = sg.Window( 'Budget Contact Form', layout,
            font = __font,
            icon = __icon,
            size = __size )
        event, values = window.read( )
        window.close( )
        sg.popup( event, values, values[ '-NAME-' ],
            values[ '-ADDRESS-' ],
            values[ '-PHONE-' ],
            text_color = r'#ADDFF7',
            font = __font,
            icon = __icon )


class GridForm( ):
    '''object providing form that simulates a datagrid '''
    def show( self ):
        sg.theme_background_color( '#0F0F0F' )
        sg.theme_element_text_color( '#ADDFF7' )
        sg.theme_input_background_color( '#0F0F0F' )
        sg.theme_text_color( '#ADDFF7' )
        sg.theme_element_background_color( '#0F0F0F' )
        sg.theme_text_element_background_color( '#0F0F0F' )
        __icon = r'C:\Users\terry\source\repos\BudgetPy\etc\ico\ninja.ico'
        __font = 'Roboto 8'
        __size = ( 15, 1 )
        headings = [ 'HEADER 1', 'HEADER 2', 'HEADER 3', 'HEADER 4' ]
        header = [ [ sg.Text( '  ' ) ] \
                   + [ sg.Text( h, size = ( 15, 1 ) ) for h in headings ] ]
        input_rows = [ [ sg.Input( size = ( 17, 1 ), pad = ( 0, 0 ), font = __font ) for col in range( 4 ) ] for row in range( 10 ) ]
        layout = header + input_rows
        window = sg.Window( 'Budget Grid', layout,
            font = __font,
            icon = __icon )
        event, values = window.read( )


class Loading( ):
    '''object providing form loading behavior '''

    def show( self ):
        gif_filename = r'C:\Users\terry\source\repos\BudgetPy\etc\img\loaders\loading.gif'
        layout = [ [ sg.Text( '',
            background_color = '#000000',
            text_color = '#FFF000',
            justification = 'c',
            key = '-T-',
            font = ( "Bodoni MT", 40 ) ) ], [ sg.Image( key = '-IMAGE-' ) ] ]
        window = sg.Window( 'Loading', layout,
            element_justification = 'c',
            margins = ( 0, 0 ),
            size = ( 600, 600 ),
            element_padding = ( 0, 0 ), finalize = True )
        window[ '-T-' ].expand( True, True, True )
        interframe_duration = Image.open( gif_filename ).info[ 'duration' ]
        while True:
            for frame in ImageSequence.Iterator( Image.open( gif_filename ) ):
                event, values = window.read( timeout = interframe_duration )
                if event == sg.WIN_CLOSED or event == sg.WIN_X_EVENT:
                    exit( 0 )
                window[ '-IMAGE-' ].update( data = ImageTk.PhotoImage( frame ) )
            window.close()


class Waiting( ):
    '''object providing form loader behavior '''

    def show( self ):
        gif_filename = r'C:\Users\terry\source\repos\BudgetPy\etc\img\loaders\loader.gif'
        layout = [ [ sg.Text( '',
            background_color = '#000000',
            text_color = '#FFF000',
            justification = 'c',
            key = '-T-',
            font = ("Bodoni MT", 40) ) ], [ sg.Image( key = '-IMAGE-' ) ] ]
        window = sg.Window( 'Loading', layout,
            element_justification = 'c',
            margins = ( 0, 0 ),
            element_padding = ( 0, 0 ),
            size = ( 600, 600 ),
            finalize = True )
        window[ '-T-' ].expand( True, True, True )
        interframe_duration = Image.open( gif_filename ).info[ 'duration' ]
        while True:
            for frame in ImageSequence.Iterator( Image.open( gif_filename ) ):
                event, values = window.read( timeout = interframe_duration )
                if event == sg.WIN_CLOSED:
                    exit( 0 )
                window[ '-IMAGE-' ].update( data = ImageTk.PhotoImage( frame ) )
            window.close()


class Processing( ):
    '''object providing form processing behavior '''

    def show( self ):
        gif_filename = r'C:\Users\terry\source\repos\BudgetPy\etc\img\loaders\processing.gif'
        layout = [ [ sg.Text( '',
            background_color = '#000000',
            text_color = '#FFF000',
            justification = 'c',
            key = '-T-',
            font = ("Bodoni MT", 40) ) ], [ sg.Image( key = '-IMAGE-' ) ] ]
        window = sg.Window( 'Loading', layout,
            element_justification = 'c',
            margins = ( 0, 0 ),
            size = ( 600, 600 ),
            element_padding = ( 0, 0 ), finalize = True )
        window[ '-T-' ].expand( True, True, True )
        interframe_duration = Image.open( gif_filename ).info[ 'duration' ]
        while True:
            for frame in ImageSequence.Iterator( Image.open( gif_filename ) ):
                event, values = window.read( timeout = interframe_duration )
                if event == sg.WIN_CLOSED or event == sg.WIN_X_EVENT:
                    exit( 0 )
                window[ '-IMAGE-' ].update( data = ImageTk.PhotoImage( frame ) )
            window.close()
