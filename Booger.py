from PIL import Image, ImageTk, ImageSequence
import PySimpleGUI as sg


class FileBrowser(  ):
    '''class that renames a file'''
    sg.theme( 'Dark Grey 14' )

    def show( self ):
        __textcolor = '#d3d3d3'
        __backcolor = '#222323'
        __font = 'Roboto 9'
        layout = [ [ sg.Text( 'Search for File' ) ],
                   [ sg.Input( ), sg.FileBrowse( ) ],
                   [ sg.OK( ), sg.Cancel( ) ] ]
        window = sg.Window( 'Budget Execution', layout,
            background_color = __backcolor,
            font = __font,
            text_color = __textcolor )
        event, values = window.read( )
        window.close( )


class FolderBrowser( ):
    '''class that renames a folder'''
    sg.theme( 'Dark Grey 14' )

    def show( self ):
        __textcolor = '#d3d3d3'
        __backcolor = '#222323'
        __font = 'Roboto 9'
        layout = [ [ sg.Text( 'Search for Directory' ) ],
                   [ sg.Input( ), sg.FolderBrowse( ) ],
                   [ sg.OK( ), sg.Cancel( ) ] ]
        window = sg.Window( 'Budget Execution', layout,
            background_color = __backcolor,
            font = __font )
        event, values = window.read( )
        window.close( )


class ErrorDialog( ):
    '''class that displays error message'''
    sg.theme( 'Dark Grey 14' )

    def show( self ):
        __textcolor = '#d3d3d3'
        __backcolor = '#222323'
        __font = 'Roboto 9'
        sg.popup_error( title = 'Budget Execution Error',
            background_color = __backcolor,
            font = __font,
            text_color = __textcolor )


class ContactForm( ):
    '''class that produces a contact input form'''
    sg.theme( 'Dark Grey 14')

    def show( self ):
        __textcolor = '#d3d3d3'
        __backcolor = '#222323'
        __font = 'Roboto 9'
        layout = [
                [ sg.Text( 'Please enter your Name, Address, Phone' ) ],
                [ sg.Text( 'Name', size = (15, 1) ), sg.InputText( '1', key = '-NAME-' ) ],
                [ sg.Text( 'Address', size = (15, 1) ), sg.InputText( '2', key = '-ADDRESS-' ) ],
                [ sg.Text( 'Phone', size = (15, 1) ), sg.InputText( '3', key = '-PHONE-' ) ],
                [ sg.Submit( ), sg.Cancel( ) ] ]
        window = sg.Window( 'Budget Contact Form', layout )
        event, values = window.read( )
        window.close( )
        sg.popup( event, values, values[ '-NAME-' ], values[ '-ADDRESS-' ], values[ '-PHONE-' ] )


class GridForm( ):
    '''object providing form that simulates a datagrid '''
    sg.theme( 'Dark Grey 14' )

    def show( self ):
        headings = [ 'HEADER 1', 'HEADER 2', 'HEADER 3', 'HEADER 4' ]
        header = [ [ sg.Text( '  ' ) ] \
                   + [ sg.Text( h, size = ( 15, 1 ) ) for h in headings ] ]
        input_rows = [ [ sg.Input( size = ( 17, 1 ), pad = ( 0, 0 ) ) for col in range( 4 ) ] for row in range( 10 ) ]
        layout = header + input_rows
        window = sg.Window( 'Budget Grid', layout, font = 'Roboto 11' )
        event, values = window.read( )


class LoadingDialog( ):
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
            element_padding = ( 0, 0 ), finalize = True )
        window[ '-T-' ].expand( True, True, True )
        interframe_duration = Image.open( gif_filename ).info[ 'duration' ]
        while True:
            for frame in ImageSequence.Iterator( Image.open( gif_filename ) ):
                event, values = window.read( timeout = interframe_duration )
                if event == sg.WIN_CLOSED:
                    exit( 0 )
                window[ '-IMAGE-' ].update( data = ImageTk.PhotoImage( frame ) )


class LoaderDialog( ):
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
            margins = (0, 0),
            element_padding = (0, 0), finalize = True )
        window[ '-T-' ].expand( True, True, True )
        interframe_duration = Image.open( gif_filename ).info[ 'duration' ]
        while True:
            for frame in ImageSequence.Iterator( Image.open( gif_filename ) ):
                event, values = window.read( timeout = interframe_duration )
                if event == sg.WIN_CLOSED:
                    exit( 0 )
                window[ '-IMAGE-' ].update( data = ImageTk.PhotoImage( frame ) )


class ProcessingDialog( ):
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
            margins = (0, 0),
            element_padding = (0, 0), finalize = True )
        window[ '-T-' ].expand( True, True, True )
        interframe_duration = Image.open( gif_filename ).info[ 'duration' ]
        while True:
            for frame in ImageSequence.Iterator( Image.open( gif_filename ) ):
                event, values = window.read( timeout = interframe_duration )
                if event == sg.WIN_CLOSED:
                    exit( 0 )
                window[ '-IMAGE-' ].update( data = ImageTk.PhotoImage( frame ) )
