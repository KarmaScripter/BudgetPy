import os
from PIL import Image, ImageTk, ImageSequence
import PySimpleGUI as sg
import fitz
import tkinter as tk
from sys import exit
import Static
from Ninja import *
from Static import *
import textwrap
import datetime
import random
import io
from googlesearch import search
from Minion import App
import smtplib as smtp
from email.message import EmailMessage
import queue
import logging
import threading
import time


# ButtonIcon( png )
class ButtonIcon( ):
    '''class representing form images'''
    __button = None
    __name = None
    __filepath = None

    @property
    def folder( self ):
        if isinstance( self.__button, str ) and self.__button != '':
            return self.__button

    @folder.setter
    def folder( self, value ):
        if isinstance( value, str ) and value != '':
            self.__button = value

    @property
    def name( self ):
        if isinstance( self.__name, str ) and self.__name != '':
            return self.__name

    @name.setter
    def name( self, value ):
        if isinstance( value, str ):
            self.__name = value

    @property
    def filepath( self ):
        if isinstance( self.__filepath, str ) and self.__filepath != '':
            return self.__filepath

    @filepath.setter
    def filepath( self, value ):
        if isinstance( value, str ) and value != '':
            self.__filepath = value

    def __init__( self, png ):
        self.__name = png.name if isinstance( png, PNG ) else None
        self.__button = r'C:\Users\terry\source\repos\BudgetPy\etc\img\button'
        self.__filepath = self.__button + r'\\' + self.__name + '.png'

    def __str__( self ):
        if isinstance( self.__filepath, str ):
            return self.__filepath


# TitleIcon( ico )
class TitleIcon( ):
    '''class representing form images'''
    __folder = None
    __name = None
    __filepath = None

    @property
    def folder( self ):
        if isinstance( self.__button, str ) and self.__button != '':
            return self.__button

    @folder.setter
    def folder( self, value ):
        if isinstance( value, str ) and value != '':
            self.__button = value

    @property
    def name( self ):
        if isinstance( self.__name, str ) and self.__name != '':
            return self.__name

    @name.setter
    def name( self, value ):
        if isinstance( value, str ):
            self.__name = value

    @property
    def filepath( self ):
        if isinstance( self.__filepath, str ) and self.__filepath != '':
            return self.__filepath

    @filepath.setter
    def filepath( self, value ):
        if isinstance( value, str ) and value != '':
            self.__filepath = value

    def __init__( self, ico ):
        self.__name = ico.name if isinstance( ico, ICO ) else None
        self.__folder = r'C:\Users\terry\source\repos\BudgetPy\etc\ico'
        self.__filepath = self.__folder + r'\\' + self.__name + r'.ico'

    def __str__( self ):
        if isinstance( self.__filepath, str ):
            return self.__filepath


class Sith( ):
    '''Base class for the dark-mode controls'''
    __themebackground = None
    __elementbackcolor = None
    __elementforecolor = None
    __themetextcolor = None
    __textbackcolor = None
    __inputbackcolor = None
    __inputforecolor = None
    __buttoncolor = None
    __icon = None
    __themefont = None
    __scrollbar = None
    __progressbar = None

    @property
    def themebackground( self ):
        if isinstance( self.__themebackground, str ) and self.__themebackground != '':
            return self.__themebackground

    @themebackground.setter
    def themebackground( self, value ):
        if isinstance( value, str ) and value != '':
            self.__themebackground = value

    @property
    def elementbackcolor( self ):
        if isinstance( self.__elementbackcolor, str ) and self.__elementbackcolor != '':
            return self.__elementbackcolor

    @elementbackcolor.setter
    def elementbackcolor( self, value ):
        if isinstance( value, str ) and value != '':
            self.__elementbackcolor = value

    @property
    def elementforecolor( self ):
        if isinstance( self.__elementforecolor, str ) and self.__elementforecolor != '':
            return self.__elementforecolor

    @elementbackcolor.setter
    def elementforecolor( self, value ):
        if isinstance( value, str ) and value != '':
            self.__elementforecolor = value

    @property
    def textforecolor( self ):
        if isinstance( self.__themetextcolor, str ) and self.__themetextcolor != '':
            return self.__themetextcolor

    @textforecolor.setter
    def textforecolor( self, value ):
        if isinstance( value, str ) and value != '':
            self.__themetextcolor = value

    @property
    def textbackcolor( self ):
        if isinstance( self.__textbackcolor, str ) and self.__textbackcolor != '':
            return self.__textbackcolor

    @textbackcolor.setter
    def textbackcolor( self, value ):
        if isinstance( value, str ) and value != '':
            self.__textbackcolor = value

    @property
    def inputbackcolor( self ):
        if isinstance( self.__inputbackcolor, str ) and self.__inputbackcolor != '':
            return self.__inputbackcolor

    @inputbackcolor.setter
    def inputbackcolor( self, value ):
        if isinstance( value, str ) and value != '':
            self.__inputbackcolor = value

    @property
    def inputforecolor( self ):
        if isinstance( self.__inputforecolor, str ) and self.__inputforecolor != '':
            return self.__inputforecolor

    @inputforecolor.setter
    def inputforecolor( self, value ):
        if isinstance( value, str ) and value != '':
            self.__inputforecolor = value

    @property
    def buttoncolor( self ):
        if isinstance( self.__buttoncolor, str ) and self.__buttoncolor != '':
            return self.__buttoncolor

    @buttoncolor.setter
    def buttoncolor( self, value ):
        if isinstance( value, str ) and value != '':
            self.__buttoncolor = value

    @property
    def iconpath( self ):
        if isinstance( self.__icon, str ) and self.__icon != '':
            return self.__icon

    @iconpath.setter
    def iconpath( self, value ):
        if isinstance( value, str ) and value != '':
            self.__icon = value

    @property
    def themefont( self ):
        if isinstance( self.__themefont, tuple ) :
            return self.__themefont

    @themefont.setter
    def themefont( self, value ):
        if isinstance( value, tuple ) :
            self.__themefont = value

    @property
    def scrollbarcolor( self ):
        if isinstance( self.__scrollbar, str ) and self.__scrollbar != '':
            return self.__scrollbar

    @scrollbarcolor.setter
    def scrollbarcolor( self, value ):
        if isinstance( value, str ) and value != '':
            self.__scrollbar = value

    @property
    def progressbarcolor( self ):
        if isinstance( self.__progressbar, tuple ) :
            return self.__progressbar

    @progressbarcolor.setter
    def progressbarcolor( self, value ):
        if isinstance( value, tuple ) :
            self.__progressbar = value

    def __init__( self ):
        self.__themebackground = '#0F0F0F'
        self.__themetextcolor = '#D3D3D3'
        self.__elementbackcolor = '#0F0F0F'
        self.__elementforecolor = '#D3D3D3'
        self.__textbackcolor = '#0F0F0F'
        self.__inputforecolor = '#FFFFFF'
        self.__inputbackcolor = '#282828'
        self.__buttoncolor = '#163754'
        self.__icon = r'C:\Users\terry\source\repos\BudgetPy\etc\ico\ninja.ico'
        self.__themefont = ( 'Roboto', 9 )
        self.__scrollbar = '#A87C03'
        self.__progressbar = '#18ADF2'
        sg.theme_background_color( self.__themebackground )
        sg.theme_element_background_color( self.__elementbackcolor )
        sg.theme_element_text_color( self.__elementforecolor )
        sg.theme_input_text_color( self.__inputforecolor )
        sg.theme_text_element_background_color( self.__textbackcolor )
        sg.theme_input_background_color( self.__inputbackcolor )
        sg.theme_text_color( self.__themetextcolor )
        sg.theme_button_color( self.__buttoncolor )
        sg.theme_progress_bar_color( self.__progressbar )


# FileDialog( ) -> str
class FileDialog( Sith ):
    '''class that renames a file'''
    __themebackground = None
    __elementbackcolor = None
    __elementforecolor = None
    __themetextcolor = None
    __textbackcolor = None
    __inputbackcolor = None
    __inputforecolor = None
    __buttoncolor = None
    __icon = None
    __themefont = None
    __filepath = None
    __formsize = None

    @property
    def size( self ):
        if isinstance( self.__formsize, tuple ) :
            return self.__formsize

    @size.setter
    def size( self, value ):
        if isinstance( value, tuple ) :
            self.__formsize = value

    @property
    def filepath( self ):
        if isinstance( self.__filepath, str ) and self.__filepath != '':
            return self.__filepath

    @filepath.setter
    def filepath( self, value ):
        if isinstance( value, str ) and value != '':
            self.__filepath = value

    def __init__( self ):
        super( Sith, self ).__init__( )
        self.__themebackground = Sith( ).themebackground
        self.__themefont = Sith( ).themefont
        self.__icon = Sith( ).iconpath
        self.__elementbackcolor = Sith( ).elementbackcolor
        self.__elementforecolor = Sith( ).elementforecolor
        self.__themetextcolor = Sith( ).textforecolor
        self.__textbackcolor = Sith( ).textbackcolor
        self.__inputbackcolor = Sith( ).inputbackcolor
        self.__inputforecolor = Sith( ).inputforecolor
        self.__buttoncolor = Sith( ).buttoncolor
        self.__formsize = ( 450, 200 )
        self.__filepath = None

    def __str__( self ):
        if isinstance( self.__filepath, str ):
            return self.__filepath

    def show( self ):
        layout = [ [ sg.Text( r'' ) ],
           [ sg.Text( 'Search for File' ) ],
           [ sg.Text( r'' ) ],
           [ sg.Input( key = '-PATH-' ), sg.FileBrowse( size = ( 15, 1 ) ) ],
           [ sg.Text( r'' ) ],
           [ sg.Text( r'' ) ],
           [ sg.OK( size = ( 8, 1 ),  ), sg.Cancel( size = ( 10, 1 )  ) ] ]

        window = sg.Window( 'Budget Execution', layout,
            font = self.__themefont,
            icon = self.__icon,
            size = self.__formsize )

        while True:
            event, values = window.read( )
            if event in ( sg.WIN_CLOSED, sg.WIN_X_EVENT, 'Cancel' ):
                break
            elif event == 'OK':
                self.__filepath = values[ '-PATH-' ]
                sg.popup_ok( self.__filepath,
                    title = 'Results',
                    icon = self.__icon,
                    font = self.__themefont )

        window.close( )


# FolderDialog( ) -> str
class FolderDialog( Sith ):
    '''class that renames a folder'''
    __themebackground = None
    __elementbackcolor = None
    __elementforecolor = None
    __themetextcolor = None
    __textbackcolor = None
    __inputbackcolor = None
    __inputforecolor = None
    __buttoncolor = None
    __icon = None
    __formsize = None
    __themefont = None
    __folderpath = None


    @property
    def size( self ):
        if isinstance( self.__formsize, tuple ) :
            return self.__formsize

    @size.setter
    def size( self, value ):
        if isinstance( value, tuple ) :
            self.__formsize = value

    @property
    def folderpath( self ):
        if isinstance( self.__folderpath, str ) and self.__folderpath != '':
            return self.__folderpath

    @folderpath.setter
    def folderpath( self, value ):
        if isinstance( value, str ) and value != '':
            self.__folderpath = value

    def __init__( self ):
        super( Sith, self ).__init__( )
        self.__themebackground = Sith( ).themebackground
        self.__themefont = Sith( ).themefont
        self.__icon = Sith( ).iconpath
        self.__elementbackcolor = Sith( ).elementbackcolor
        self.__elementforecolor = Sith( ).elementforecolor
        self.__themetextcolor = Sith( ).textforecolor
        self.__textbackcolor = Sith( ).textbackcolor
        self.__inputbackcolor = Sith( ).inputbackcolor
        self.__inputforecolor = Sith( ).inputforecolor
        self.__buttoncolor = Sith( ).buttoncolor
        self.__formsize = ( 450, 200 )
        self.__folderpath = None

    def __str__( self ):
        if isinstance( self.__filepath, str ):
            return self.__filepath

    def show( self ):
        layout = [ [ sg.Text( r'' ) ],
           [ sg.Text( 'Search for Directory' ) ],
           [ sg.Text( r'' ) ],
           [ sg.Input( ), sg.FolderBrowse( size = ( 15, 1 ) ) ],
           [ sg.Text( r'', size = ( 100, 1 ) ) ],
           [ sg.Text( r'', size = ( 100, 1 ) ) ],
           [ sg.OK( size = ( 8, 1 ) ), sg.Cancel( size = ( 10, 1 ) ) ] ]

        window = sg.Window( 'Budget Execution', layout,
            font = self.__themefont,
            icon = self.__icon,
            size = self.__formsize )

        while True:
            event, values = window.read( )
            if event in ( sg.WIN_CLOSED, sg.WIN_X_EVENT, 'Cancel' ):
                break

        window.close( )


# SaveFileDialog( path )
class SaveFileDialog( Sith ):
    '''class provides form to located file destinations'''
    __themebackground = None
    __elementbackcolor = None
    __elementforecolor = None
    __themetextcolor = None
    __textbackcolor = None
    __inputbackcolor = None
    __inputforecolor = None
    __buttoncolor = None
    __icon = None
    __formsize = None
    __themefont = None
    __original = None
    __filename = None

    @property
    def text( self ):
        if isinstance( self.__text, str ) and self.__text != '':
            return self.__text

    @text.setter
    def text( self, value ):
        if isinstance( value, str ) and value != '':
            self.__text = value

    @property
    def size( self ):
        if isinstance( self.__formsize, tuple ) :
            return self.__formsize

    @size.setter
    def size( self, value ):
        if isinstance( value, tuple ) :
            self.__formsize = value

    @property
    def original( self ):
        if isinstance( self.__original, str ) and self.__original != '':
            return self.__original

    @original.setter
    def original( self, value ):
        if isinstance( value, str) and os.path.exists( value ):
            self_original = value

    def __init__( self, path = None ):
        super( Sith, self ).__init__( )
        self.__themebackground = Sith( ).themebackground
        self.__themefont = Sith( ).themefont
        self.__icon = Sith( ).iconpath
        self.__elementbackcolor = Sith( ).elementbackcolor
        self.__elementforecolor = Sith( ).elementforecolor
        self.__themetextcolor = Sith( ).textforecolor
        self.__textbackcolor = Sith( ).textbackcolor
        self.__inputbackcolor = Sith( ).inputbackcolor
        self.__inputforecolor = Sith( ).inputforecolor
        self.__buttoncolor = Sith( ).buttoncolor
        self.__formsize = ( 400, 200 )
        self.__original = path if isinstance( path, str) and os.path.isfile( path ) else None

    def show( self ):
        username = os.environ.get( 'USERNAME' )
        startpath = f'C:\\Users\\{username}\\Desktop'
        filename = sg.popup_get_file( 'Select Location / Enter File Name',
            default_path = startpath,
            title = 'Budget Execution',
            font = self.__themefont,
            icon = self.__icon,
            save_as = True )

        if isinstance( self.__original, str) and os.path.exists( self.__original ):
            src = io.open( self.__original, 'r' ).read( )
            new = io.open( filename, 'w+' ).write( src )


# GoogleDialog(  ) -> list
class GoogleDialog( Sith ):
    '''class that renames a folder'''
    __themebackground = None
    __elementbackcolor = None
    __elementforecolor = None
    __themetextcolor = None
    __textbackcolor = None
    __inputbackcolor = None
    __inputforecolor = None
    __buttoncolor = None
    __icon = None
    __formsize = None
    __themefont = None
    __image = None
    __querytext = None
    __results = None

    @property
    def size( self ):
        if isinstance( self.__formsize, tuple ) :
            return self.__formsize

    @size.setter
    def size( self, value ):
        if isinstance( value, tuple ) :
            self.__formsize = value

    @property
    def search( self ):
        if isinstance( self.__querytext, str ) and self.__querytext != '':
            return self.__querytext

    @search.setter
    def search( self, value ):
        if isinstance( value, str ) and value != '':
            self.__querytext = value

    @property
    def image( self ):
        if isinstance( self.__image, str ) and self.__image != '':
            return self.__image

    @image.setter
    def image( self, value ):
        if isinstance( value, str ) and value != '':
            self.__image = value

    @property
    def results( self ):
        if isinstance( self.__results, str ) and self.__results != '':
            return self.__results

    @search.setter
    def results( self, value ):
        if isinstance( value, str ) and value != '':
            self.__results = value

    def __init__( self ):
        super( Sith, self ).__init__( )
        self.__themebackground = Sith( ).themebackground
        self.__themefont = Sith( ).themefont
        self.__icon = Sith( ).iconpath
        self.__elementbackcolor = Sith( ).elementbackcolor
        self.__elementforecolor = Sith( ).elementforecolor
        self.__themetextcolor = Sith( ).textforecolor
        self.__textbackcolor = Sith( ).textbackcolor
        self.__inputbackcolor = Sith( ).inputbackcolor
        self.__inputforecolor = Sith( ).inputforecolor
        self.__buttoncolor = Sith( ).buttoncolor
        self.__formsize = ( 450, 200 )
        self.__image = r'C:\Users\terry\source\repos\BudgetPy\etc\img\app\web\google.png'
        self.__querytext = None
        self.__results = [ ]

    def __str__( self ):
        if isinstance( self.__filepath, str ):
            return self.__filepath

    def show( self ):
        layout =  [ [ sg.Text( r'' ) ],
            [ sg.Image( filename = self.__image ) ],
            [ sg.Text( '', size = ( 10, 1 ) ), sg.Input( '', key = '-QUERY-', size = ( 40, 2 ) ) ],
            [ sg.Text( r'', size = ( 100, 1 ) ) ],
            [ sg.Text( r'', size = ( 100, 1 ) ) ],
            [ sg.Text( r'', size = ( 10, 1 ) ), sg.Submit( size = ( 15, 1 ) ),
              sg.Text( r'', size = ( 10, 1 ) ), sg.Cancel( size = ( 15, 1 ) ) ] ]

        window = sg.Window( 'Budget Execution', layout,
            icon = self.__icon,
            font = self.__themefont,
            size = self.__formsize )

        while True:
            event, values = window.read( )
            if event in ( sg.WIN_X_EVENT, sg.WIN_CLOSED, 'Cancel' ):
                break
            elif event == 'Submit':
                self.__querytext = values[ '-QUERY-' ]
                window.close( )
                query = search( term = self.__querytext, num_results = 5, lang = 'en' )
                chrome = Client.Chrome
                app = App( chrome )
                for result in query:
                    app.runargs( result )

        window.close( )


class EmailDialog( Sith ):
    '''class that renames a folder'''
    __themebackground = None
    __elementbackcolor = None
    __elementforecolor = None
    __themetextcolor = None
    __textbackcolor = None
    __inputbackcolor = None
    __inputforecolor = None
    __buttoncolor = None
    __icon = None
    __image = None
    __formsize = None
    __themefont = None
    __folderpath = None


    @property
    def size( self ):
        if isinstance( self.__formsize, tuple ) :
            return self.__formsize

    @size.setter
    def size( self, value ):
        if isinstance( value, tuple ) :
            self.__formsize = value

    @property
    def folderpath( self ):
        if isinstance( self.__folderpath, str ) and self.__folderpath != '':
            return self.__folderpath

    @folderpath.setter
    def folderpath( self, value ):
        if isinstance( value, str ) and value != '':
            self.__folderpath = value

    def __init__( self ):
        super( Sith, self ).__init__( )
        self.__themebackground = Sith( ).themebackground
        self.__themefont = Sith( ).themefont
        self.__icon = Sith( ).iconpath
        self.__elementbackcolor = Sith( ).elementbackcolor
        self.__elementforecolor = Sith( ).elementforecolor
        self.__themetextcolor = Sith( ).textforecolor
        self.__textbackcolor = Sith( ).textbackcolor
        self.__inputbackcolor = Sith( ).inputbackcolor
        self.__inputforecolor = Sith( ).inputforecolor
        self.__buttoncolor = Sith( ).buttoncolor
        self.__image = r'C:\Users\terry\source\repos\BudgetPy\etc\img\app\web\outlook.png'
        self.__formsize = ( 600, 500 )
        self.__folderpath = None

    def __str__( self ):
        if isinstance( self.__filepath, str ):
            return self.__filepath

    def show( self ):
        btn = ( 20, 1 )
        inp = ( 35, 1 )
        spc = ( 5, 1 )
        layout = [ [ sg.T( ' ', size = spc ), ],
           [ sg.T( ' ', size = spc ), sg.Image( filename = self.__image ) ],
           [ sg.T( ' ', size = spc ), ],
           [ sg.T( ' ', size = spc ), sg.T( 'From:', size = btn ), sg.Input( key = '-EMAIL FROM-', size = ( 35,1 ) ) ],
           [ sg.T( ' ', size = spc ), sg.T( 'To:', size = btn ),  sg.Input(key = '-EMAIL TO-', size = ( 35,1 ) ) ],
           [ sg.T( ' ', size = spc ), sg.T( 'Subject:', size = btn ), sg.Input( key = '-EMAIL SUBJECT-', size = ( 35,1 ) ) ],
           [ sg.T( ' ', size = spc ), sg.T( '' ) ],
           [ sg.T( ' ', size = spc ), sg.T( 'Username:', size = btn ), sg.Input( key='-USER-', size=( 35,1 ) ) ],
           [ sg.T( ' ', size = spc ), sg.T( 'Password:', size = btn ), sg.Input(password_char='*', key = '-PASSWORD-', size= ( 35,1 ) ) ],
           [ sg.T( ' ', size = spc ) ],
           [ sg.T( ' ', size = spc ), sg.Multiline( 'Type your message here', size = ( 65, 10 ), key = '-EMAIL TEXT-' ) ],
           [ sg.T( ' ', size = ( 100, 1 ) ) ],
           [ sg.T( ' ', size = spc ),  sg.Button( 'Send', size = btn ),
             sg.T( ' ', size = btn ), sg.Button( 'Cancel', size = ( 20, 1 ) ) ] ]

        window = sg.Window( 'Budget Execution', layout,
            icon = self.__icon,
            background_color = self.__themebackground,
            font = self.__themefont,
            button_color = self.__buttoncolor,
            size = self.__formsize )

        while True:  # Event Loop
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'Cancel', 'Exit' ):
                break
            if event == 'Send':
                sg.popup_quick_message( 'Sending your message... this will take a moment...', background_color='red')
                send_an_email( from_address = values[ '-EMAIL FROM-' ],
                    to_address=values['-EMAIL TO-'],
                    subject=values['-EMAIL SUBJECT-'],
                    message_text=values['-EMAIL TEXT-'],
                    user=values['-USER-'],
                    password=values['-PASSWORD-'])

        window.close()


# MessageDialog( text )
class MessageDialog( Sith ):
    ''' class that provides form to display informational messages '''
    __themebackground = None
    __elementbackcolor = None
    __elementforecolor = None
    __themetextcolor = None
    __textbackcolor = None
    __inputbackcolor = None
    __inputforecolor = None
    __buttoncolor = None
    __icon = None
    __formsize = None
    __themefont = None
    __text = None

    @property
    def text( self ):
        if isinstance( self.__text, str ) and self.__text != '':
            return self.__text

    @text.setter
    def text( self, value ):
        if isinstance( value, str ) and value != '':
            self.__text = value

    @property
    def size( self ):
        if isinstance( self.__formsize, tuple ) :
            return self.__formsize

    @size.setter
    def size( self, value ):
        if isinstance( value, tuple ) :
            self.__formsize = value

    def __init__( self, text ):
        self.__text = text if isinstance( text, str ) and text != '' else None
        super( Sith, self ).__init__( )
        self.__themebackground = Sith( ).themebackground
        self.__themefont = Sith( ).themefont
        self.__icon = Sith( ).iconpath
        self.__elementbackcolor = Sith( ).elementbackcolor
        self.__elementforecolor = Sith( ).elementforecolor
        self.__themetextcolor = Sith( ).textforecolor
        self.__textbackcolor = Sith( ).textbackcolor
        self.__inputbackcolor = Sith( ).inputbackcolor
        self.__inputforecolor = Sith( ).inputforecolor
        self.__buttoncolor = Sith( ).buttoncolor
        self.__formsize = ( 400, 200 )

    def __str__( self ):
        if isinstance( self.__text, str ):
            return self.__text

    def show( self ):
        layout = [ [ sg.Text( r'', size = ( 100, 1 ) ) ],
           [ sg.Text( r'', size = (100, 1) ) ],
           [ sg.Text( r'', size = ( 5, 1 ) ),  sg.Text( self.__text, font = ( 'Roboto', 9, 'bold' ), text_color = '#FFFFFF', size = ( 80, 1 ) ) ],
           [ sg.Text( r'', size = ( 100, 1 ) ) ],
           [ sg.Text( r'', size = ( 100, 1 ) ) ],
           [ sg.Text( r'', size = ( 100, 1 ) ) ],
           [ sg.Text( r'', size = (5, 1) ), sg.Ok( size = (10, 1) ), 
             sg.Text( r'', size = (15, 1) ), sg.Cancel( size = (10, 1) ) ] ]

        window = sg.Window( r'  Budget Execution', layout,
            icon = self.__icon,
            font = self.__themefont,
            size = self.__formsize )

        while True:
            event, values = window.read( )
            if event in ( sg.WIN_CLOSED, sg.WIN_X_EVENT, 'Ok', 'Cancel' ):
                break

        window.close( )


# ErrorDialog( exception )
class ErrorDialog( Sith ):
    '''class that displays error message'''
    __message = None
    __cause = None
    __method = None
    __exception = None
    __themebackground = None
    __elementbackcolor = None
    __elementforecolor = None
    __themetextcolor = None
    __textbackcolor = None
    __inputbackcolor = None
    __inputforecolor = None
    __buttoncolor = None
    __icon = None
    __formsize = None
    __themefont = None

    @property
    def size( self ):
        if isinstance( self.__formsize, tuple ) :
            return self.__formsize

    @size.setter
    def size( self, value ):
        if isinstance( value, tuple ) :
            self.__formsize = value

    @property
    def message( self ):
        if isinstance( self.__message, str ) and self.__message != '':
            return self.__message

    @message.setter
    def message( self, value ):
        if isinstance( value, str ) and value != '':
            self.__message = value

    def __init__( self, exception = None ):
        super( Sith, self ).__init__( )
        self.__themebackground = Sith( ).themebackground
        self.__exception = exception if isinstance( exception, BudgetError ) else None
        self.__message = self.__exception.message if isinstance( exception, BudgetError ) else None
        self.__cause = self.__exception.cause if isinstance( exception, BudgetError ) else ''
        self.__method = self.__exception.method if isinstance( exception, BudgetError ) else ''
        self.__themefont = Sith( ).themefont
        self.__icon = Sith( ).iconpath
        self.__elementbackcolor = Sith( ).elementbackcolor
        self.__elementforecolor = Sith( ).elementforecolor
        self.__themetextcolor = Sith( ).textforecolor
        self.__textbackcolor = Sith( ).textbackcolor
        self.__inputbackcolor = Sith( ).inputbackcolor
        self.__inputforecolor = Sith( ).inputforecolor
        self.__buttoncolor = Sith( ).buttoncolor
        self.__formsize = ( 500, 275 )

    def __str__( self ):
        if isinstance( self.__message, str ):
            return self.__message

    def show( self ):
        layout = [ [ sg.Text( r'', size = ( 150, 1 ) ) ],
           [ sg.Text( 'Source:', size = ( 10, 1 ) ), sg.Text( self.__cause, size = ( 80, 1 ) ) ],
           [ sg.Text( 'Method:', size = ( 10, 1 ) ), sg.Text( self.__method, size = ( 80, 1 ) ) ],
           [ sg.Text( r'', size = ( 150, 1 ) ) ],
           [ sg.Multiline( self.__message, size = ( 80, 7 ) ) ],
           [ sg.Text( r'' ) ],
           [ sg.Text( r'', size = ( 20, 1 ) ), sg.Cancel( size = ( 15, 1 ) ),
             sg.Text( r'', size = ( 10, 1 ) ), sg.Ok( size = ( 15, 1 ), key = '-OK-' ) ] ]

        window = sg.Window( r'  Budget Execution', layout,
            icon = self.__icon,
            font = self.__themefont,
            size = self.__formsize )

        while True:
            event, values = window.read( )
            if event in ( sg.WIN_CLOSED, sg.WIN_X_EVENT, '-OK-' ):
                break

        window.close( )


# Input( question )
class InputDialog( Sith ):
    '''class that produces a contact input form'''
    __question = None
    __response = None
    __themebackground = None
    __elementbackcolor = None
    __elementforecolor = None
    __themetextcolor = None
    __textbackcolor = None
    __inputbackcolor = None
    __inputforecolor = None
    __buttoncolor = None
    __icon = None
    __formsize = None
    __themefont = None

    @property
    def size( self ):
        if isinstance( self.__formsize, tuple ) :
            return self.__formsize

    @size.setter
    def size( self, value ):
        if isinstance( value, tuple ) :
            self.__formsize = value

    @property
    def question( self ):
        if isinstance( self.__question, str ) and self.__question != '':
            return self.__question

    @question.setter
    def question( self, value ):
        if isinstance( value, str ) and value != '':
            self.__question = value

    @property
    def response( self ):
        if isinstance( self.__response, str ) and self.__response != '':
            return self.__response

    @response.setter
    def response( self, value ):
        if isinstance( value, str ) and value != '':
            self.__response= value

    def __init__( self, question ):
        super( Sith, self ).__init__( )
        self.__themebackground = Sith( ).themebackground
        self.__question = question if isinstance( question, str ) and question != '' else None
        self.__themefont = Sith( ).themefont
        self.__icon = Sith( ).iconpath
        self.__elementbackcolor = Sith( ).elementbackcolor
        self.__elementforecolor = Sith( ).elementforecolor
        self.__themetextcolor = Sith( ).textforecolor
        self.__textbackcolor = Sith( ).textbackcolor
        self.__inputbackcolor = Sith( ).inputbackcolor
        self.__inputforecolor = Sith( ).inputforecolor
        self.__buttoncolor = Sith( ).buttoncolor
        self.__formsize = ( 450, 200 )
        self.__response = None

    def show( self ):
        layout =  [ [ sg.Text( r'' ) ],
            [ sg.Text( self.__question, font = ( 'Roboto', 9, 'bold' ) ) ],
            [ sg.Text( r'' ) ],
            [ sg.Text( 'Enter:', size = ( 10, 2 ) ), sg.InputText( key = '-INPUT-', size = ( 40, 2 ) ) ],
            [ sg.Text( r'', size = ( 100, 1 ) ) ],
            [ sg.Text( r'', size = ( 100, 1 ) ) ],
            [ sg.Text( r'', size = ( 10, 1 ) ), sg.Submit( size = ( 15, 1 ), key = '-SUBMIT-' ),
              sg.Text( r'', size = ( 5, 1 ) ), sg.Cancel( size = ( 15, 1 ), key = '-CANCEL-' ) ] ]

        window = sg.Window( '  Budget Execution', layout,
            icon = self.__icon,
            font = self.__themefont,
            size = self.__formsize )

        while True:
            event, values = window.read( )
            sg.popup( event, values, values[ '-INPUT-' ],
                text_color = self.__themetextcolor,
                font = self.__themefont,
                icon = self.__icon )

            if event in ( sg.WIN_X_EVENT, sg.WIN_CLOSED, 'Cancel', 'Exit' ):
                break

        window.close( )


# ContactForm( contact )
class ContactForm( Sith ):
    '''class that produces a contact input form'''
    __themebackground = None
    __elementbackcolor = None
    __elementforecolor = None
    __themetextcolor = None
    __textbackcolor = None
    __inputbackcolor = None
    __inputforecolor = None
    __buttoncolor = None
    __icon = None
    __formsize = None
    __themefont = None

    @property
    def size( self ):
        if isinstance( self.__formsize, tuple ) :
            return self.__formsize

    @size.setter
    def size( self, value ):
        if isinstance( value, tuple ) :
            self.__formsize = value

    def __init__( self ):
        super( Sith, self ).__init__( )
        self.__themebackground = Sith( ).themebackground
        self.__themefont = Sith( ).themefont
        self.__icon = Sith( ).iconpath
        self.__elementbackcolor = Sith( ).elementbackcolor
        self.__elementforecolor = Sith( ).elementforecolor
        self.__themetextcolor = Sith( ).textforecolor
        self.__textbackcolor = Sith( ).textbackcolor
        self.__inputbackcolor = Sith( ).inputbackcolor
        self.__inputforecolor = Sith( ).inputforecolor
        self.__buttoncolor = Sith( ).buttoncolor
        self.__image = r'C:\Users\terry\source\repos\BudgetPy\etc\img\app\web\outlook.png'
        self.__formsize = ( 450, 200 )

    def show( self ):
        sg.theme_background_color( self.__themebackground )
        sg.theme_element_background_color( self.__elementbackcolor )
        sg.theme_element_text_color( self.__elementforecolor )
        sg.theme_input_text_color( self.__inputforecolor )
        sg.theme_text_element_background_color( self.__textbackcolor )
        sg.theme_input_background_color( self.__inputbackcolor )
        sg.theme_text_color( self.__themetextcolor )
        sg.theme_button_color( self.__buttoncolor )

        layout =  [ [ sg.Text( r'', size = ( 100, 1 ) ) ],
                    [ sg.Text( r'Enter Contact Details' ) ],
                    [ sg.Text( r'', size = ( 100, 1 ) ) ],
                    [ sg.Text( 'Name', size = ( 10, 1 ) ), sg.InputText( '1', size = ( 80, 1 ),  key = '-NAME-' ) ],
                    [ sg.Text( 'Address', size = ( 10, 1 ) ), sg.InputText( '2', size = ( 80, 1 ), key = '-ADDRESS-' ) ],
                    [ sg.Text( 'Phone', size = ( 10, 1 ) ), sg.InputText( '3', size = ( 80, 1 ), key = '-PHONE-' ) ],
                    [ sg.Text( r'', size = ( 100, 1 ) ) ],
                    [ sg.Text( r'', size = ( 100, 1 ) ) ],
                    [ sg.Text( r'', size = ( 10, 1) ), sg.Submit( size = ( 10, 1 ) ),
                      sg.Text( r'', size = ( 20, 1) ),  sg.Cancel( size = ( 10, 1 ) ) ] ]

        window = sg.Window( 'Budget Execution', layout,
            icon = self.__icon,
            font = self.__themefont,
            size = self.__formsize )

        while True:
            event, values = window.read( )
            sg.popup( 'Results', values, values[ '-NAME-' ],
                values[ '-ADDRESS-' ],
                values[ '-PHONE-' ],
                text_color = self.__themetextcolor,
                font = self.__themefont,
                icon = self.__icon )

            if event in ( sg.WIN_CLOSED, sg.WIN_X_EVENT, 'Cancel' ):
                break

        window.close( )


class GridForm( Sith ):
    '''object providing form that simulates a datagrid '''
    __themebackground = None
    __elementbackcolor = None
    __elementforecolor = None
    __themetextcolor = None
    __textbackcolor = None
    __inputbackcolor = None
    __inputforecolor = None
    __buttoncolor = None
    __icon = None
    __formsize = None
    __fieldwidth = None
    __themefont = None
    __rows = None
    __columns = None

    @property
    def size( self ):
        if isinstance( self.__formsize, tuple ) :
            return self.__formsize

    @size.setter
    def size( self, value ):
        if isinstance( value, tuple ) :
            self.__formsize = value

    @property
    def fieldwidth( self ):
        if isinstance( self.__fieldwidth, tuple ):
            return self.__fieldwidth

    @fieldwidth.setter
    def fieldwidth( self, value ):
        if isinstance( value, tuple ) and len( value ) == 2:
            self.__fieldwidth = value

    @property
    def rows( self ):
        if isinstance( self.__rows, int ):
            return self.__rows

    @rows.setter
    def rows( self, value ):
        if isinstance( value, int ):
            self.__rows = value

    @property
    def columns( self ):
        if isinstance( self.__columns, str ) and self.__columns != '':
            return self.__columns

    @columns.setter
    def columns( self, value ):
        if isinstance( value, int ):
            self.__columns = value

    def __init__( self, rows = 10, columns = 4 ):
        super( Sith, self ).__init__( )
        self.__themebackground = Sith( ).themebackground
        self.__themefont = Sith( ).themefont
        self.__icon = Sith( ).iconpath
        self.__elementbackcolor = Sith( ).elementbackcolor
        self.__elementforecolor = Sith( ).elementforecolor
        self.__themetextcolor = Sith( ).textforecolor
        self.__textbackcolor = Sith( ).textbackcolor
        self.__inputbackcolor = Sith( ).inputbackcolor
        self.__inputforecolor = Sith( ).inputforecolor
        self.__buttoncolor = Sith( ).buttoncolor
        self.__image = r'C:\Users\terry\source\repos\BudgetPy\etc\img\app\web\outlook.png'
        self.__fieldwidth = ( 17, 1 )
        self.__rows = rows
        self.__columns = columns

    def show( self ):
        headings = [ 'HEADER 1', 'HEADER 2', 'HEADER 3', 'HEADER 4' ]
        space = [ [ sg.Text( ' ' ) ] ]
        header = [ [ sg.Text( ' ' ) ] + [ sg.Text( h, size = ( 15, 1 ) ) for h in headings ] ]
        records = [ [ [ sg.Input( size = self.__fieldwidth, pad = ( 0, 0 ), font = self.__themefont ) for c in range( self.__columns ) ] for r in range( self.__rows ) ],
                 [ sg.Text( '' ) ] ]
        buttons = [ [ sg.Text( '', size = ( 35, 1 ) ), sg.Submit( size = ( 10, 1 ), key = '-SUBMIT-'  ),
                      sg.Text( '', size = ( 5, 1 ) ), sg.Cancel( size = ( 10, 1 ), key = '-CANCEL-' ) ] ]
        layout = space + header + records + buttons

        window = sg.Window( 'Budget Execution', layout,
            icon = self.__icon,
            font = self.__themefont  )

        while True:
            event, values = window.read( )
            if event in ( sg.WIN_CLOSED, sg.WIN_X_EVENT, '-CANCEL-' ):
                break

        window.close( )


class LoadingPanel( Sith ):
    '''object providing form loading behavior '''
    __themebackground = None
    __elementbackcolor = None
    __elementforecolor = None
    __themetextcolor = None
    __textbackcolor = None
    __inputbackcolor = None
    __inputforecolor = None
    __buttoncolor = None
    __icon = None
    __formsize = None
    __themefont = None
    __image = None

    @property
    def size( self ):
        if isinstance( self.__formsize, tuple ) :
            return self.__formsize

    @size.setter
    def size( self, value ):
        if isinstance( value, tuple ) :
            self.__formsize = value

    def __init__( self ):
        super( Sith, self ).__init__( )
        self.__themebackground = Sith( ).themebackground
        self.__themefont = Sith( ).themefont
        self.__icon = Sith( ).iconpath
        self.__elementbackcolor = Sith( ).elementbackcolor
        self.__elementforecolor = Sith( ).elementforecolor
        self.__themetextcolor = Sith( ).textforecolor
        self.__textbackcolor = Sith( ).textbackcolor
        self.__inputbackcolor = Sith( ).inputbackcolor
        self.__inputforecolor = Sith( ).inputforecolor
        self.__buttoncolor = Sith( ).buttoncolor
        self.__image = r'C:\Users\terry\source\repos\BudgetPy\etc\img\loaders\loading.gif'
        self.__formsize = ( 800, 600 )

    def show( self ):
        layout = [ [ sg.Text( '',
            background_color = '#000000',
            text_color = '#FFF000',
            justification = 'c',
            key = '-T-',
            font = ( 'Bodoni MT', 40 ) ) ], [ sg.Image( key = '-IMAGE-' ) ] ]

        window = sg.Window( 'Loading', layout,
            icon = self.__icon,
            element_justification = 'c',
            margins = ( 0, 0 ),
            size = ( 800, 600 ),
            element_padding = ( 0, 0 ), finalize = True )

        window[ '-T-' ].expand( True, True, True )
        interframe_duration = Image.open( self.__image ).info[ 'duration' ]

        while True:
            for frame in ImageSequence.Iterator( Image.open( self.__image ) ):
                event, values = window.read( timeout = interframe_duration )
                if event == sg.WIN_CLOSED or event == sg.WIN_X_EVENT:
                    exit( 0 )
                window[ '-IMAGE-' ].update( data = ImageTk.PhotoImage( frame ) )

        window.close()


class WaitingPanel( Sith ):
    '''object providing form loader behavior '''
    __themebackground = None
    __elementbackcolor = None
    __elementforecolor = None
    __themetextcolor = None
    __textbackcolor = None
    __inputbackcolor = None
    __inputforecolor = None
    __buttoncolor = None
    __icon = None
    __formsize = None
    __themefont = None
    __image = None

    @property
    def size( self ):
        if isinstance( self.__formsize, tuple ) :
            return self.__formsize

    @size.setter
    def size( self, value ):
        if isinstance( value, tuple ) :
            self.__formsize = value

    def __init__( self ):
        super( Sith, self ).__init__( )
        self.__themebackground = Sith( ).themebackground
        self.__themefont = Sith( ).themefont
        self.__icon = Sith( ).iconpath
        self.__elementbackcolor = Sith( ).elementbackcolor
        self.__elementforecolor = Sith( ).elementforecolor
        self.__themetextcolor = Sith( ).textforecolor
        self.__textbackcolor = Sith( ).textbackcolor
        self.__inputbackcolor = Sith( ).inputbackcolor
        self.__inputforecolor = Sith( ).inputforecolor
        self.__buttoncolor = Sith( ).buttoncolor
        self.__image = r'C:\Users\terry\source\repos\BudgetPy\etc\img\loaders\loader.gif'
        self.__themefont = ( 'Roboto', 9 )
        self.__formsize = ( 800, 600 )

    def show( self ):
        layout = [ [ sg.Text( '',
            background_color = '#000000',
            text_color = '#FFF000',
            justification = 'c',
            key = '-T-',
            font = ('Bodoni MT', 40) ) ], [ sg.Image( key = '-IMAGE-' ) ] ]

        window = sg.Window( 'Loading', layout,
            icon = self.__icon,
            element_justification = 'c',
            margins = ( 0, 0 ),
            element_padding = ( 0, 0 ),
            size = ( 800, 600 ),
            finalize = True )

        window[ '-T-' ].expand( True, True, True )
        interframe_duration = Image.open( self.__image ).info[ 'duration' ]

        while True:
            for frame in ImageSequence.Iterator( Image.open( self.__image ) ):
                event, values = window.read( timeout = interframe_duration )
                if event == sg.WIN_CLOSED:
                    exit( 0 )
                window[ '-IMAGE-' ].update( data = ImageTk.PhotoImage( frame ) )

        window.close()


class ProcessingPanel( Sith ):
    '''object providing form processing behavior '''
    __themebackground = None
    __elementbackcolor = None
    __elementforecolor = None
    __themetextcolor = None
    __textbackcolor = None
    __inputbackcolor = None
    __inputforecolor = None
    __buttoncolor = None
    __icon = None
    __formsize = None
    __themefont = None
    __image = None

    @property
    def size( self ):
        if isinstance( self.__formsize, tuple ) :
            return self.__formsize

    @size.setter
    def size( self, value ):
        if isinstance( value, tuple ) :
            self.__formsize = value

    def __init__( self ):
        super( Sith, self ).__init__()
        self.__themebackground = Sith( ).themebackground
        self.__themefont = Sith( ).themefont
        self.__icon = Sith( ).iconpath
        self.__elementbackcolor = Sith( ).elementbackcolor
        self.__elementforecolor = Sith( ).elementforecolor
        self.__themetextcolor = Sith( ).textforecolor
        self.__textbackcolor = Sith( ).textbackcolor
        self.__inputbackcolor = Sith( ).inputbackcolor
        self.__inputforecolor = Sith( ).inputforecolor
        self.__buttoncolor = Sith( ).buttoncolor
        self.__image = r'C:\Users\terry\source\repos\BudgetPy\etc\img\loaders\processing.gif'
        self.__formsize = ( 800, 600 )

    def show( self ):
        layout = [ [ sg.Text( '',
            background_color = '#000000',
            text_color = '#FFF000',
            justification = 'c',
            key = '-T-',
            font = ('Bodoni MT', 40) ) ], [ sg.Image( key = '-IMAGE-' ) ] ]

        window = sg.Window( 'Loading', layout,
            element_justification = 'c',
            icon = self.__icon,
            margins = ( 0, 0 ),
            size = ( 800, 600 ),
            element_padding = ( 0, 0 ),
            finalize = True )

        window[ '-T-' ].expand( True, True, True )
        interframe_duration = Image.open( self.__image ).info[ 'duration' ]

        while True:
            for frame in ImageSequence.Iterator( Image.open( self.__image ) ):
                event, values = window.read( timeout = interframe_duration )
                if event == sg.WIN_CLOSED or event == sg.WIN_X_EVENT:
                    exit( 0 )
                window[ '-IMAGE-' ].update( data = ImageTk.PhotoImage( frame ) )

        window.close()


class SplashPanel( Sith ):
    '''Class providing splash dialog behavior'''
    __themebackground = None
    __elementbackcolor = None
    __elementforecolor = None
    __themetextcolor = None
    __textbackcolor = None
    __inputbackcolor = None
    __inputforecolor = None
    __buttoncolor = None
    __icon = None
    __formsize = None
    __themefont = None
    __image = None

    @property
    def formsize( self ):
        if isinstance( self.__formsize, tuple ) :
            return self.__formsize

    @formsize.setter
    def formsize( self, value ):
        if isinstance( value, tuple ) :
            self.__formsize = value

    def __init__( self ):
        super( Sith, self ).__init__()
        self.__themebackground = Sith( ).themebackground
        self.__themefont = Sith( ).themefont
        self.__icon = Sith( ).iconpath
        self.__elementbackcolor = Sith( ).elementbackcolor
        self.__elementforecolor = Sith( ).elementforecolor
        self.__themetextcolor = Sith( ).textforecolor
        self.__textbackcolor = Sith( ).textbackcolor
        self.__inputbackcolor = Sith( ).inputbackcolor
        self.__inputforecolor = Sith( ).inputforecolor
        self.__buttoncolor = Sith( ).buttoncolor
        self.__image = r'C:\Users\terry\source\repos\BudgetPy\etc\img\BudgetEx.png'
        self.__formsize = ( 800, 600 )
        self.__timeout = 4000

    def show( self ):
        layout = [ [ sg.Image( filename=self.__image ) ] ]
        window = sg.Window( 'Window Title', layout,
                    transparent_color = self.__themebackground,
                    no_titlebar = True,
                    keep_on_top = True )

        while True:
            event, values = window.read( timeout = self.__timeout, close = True )
            if event in ( sg.WIN_CLOSED, 'Exit' ):  # always check for closed window
                break

        window.close()


# Notification( message )
class Notification( Sith ):
    '''Class provides splash notification behaviors'''
    __themebackground = None
    __elementbackcolor = None
    __elementforecolor = None
    __themetextcolor = None
    __textbackcolor = None
    __inputbackcolor = None
    __inputforecolor = None
    __buttoncolor = None
    __icon = None
    __formsize = None
    __themefont = None
    __image = None
    __message = None

    @property
    def formsize( self ):
        if isinstance( self.__formsize, tuple ) :
            return self.__formsize

    @formsize.setter
    def formsize( self, value ):
        if isinstance( value, tuple ) :
            self.__formsize = value

    @property
    def message( self ):
        if isinstance( self.__message, str ) and self.__message != '':
            return self.__message

    @message.setter
    def message( self, value ):
        if isinstance( value, str ) and value != '':
            self.__message = value

    @property
    def imagepath( self ):
        if isinstance( self.__image, str ) and image != '':
            return self.__image

    @imagepath.setter
    def imagepath( self, value ):
        if isinstance( value, str ) and value != '':
            return self.__image


    def __init__( self, message ):
        super( Sith, self ).__init__()
        self.__themefont = Sith( ).themefont
        self.__themebackground = Sith( ).themebackground
        self.__icon = Sith( ).iconpath
        self.__elementbackcolor = Sith( ).elementbackcolor
        self.__elementforecolor = Sith( ).elementforecolor
        self.__themetextcolor = Sith( ).textforecolor
        self.__textbackcolor = Sith( ).textbackcolor
        self.__inputbackcolor = Sith( ).inputbackcolor
        self.__inputforecolor = Sith( ).inputforecolor
        self.__buttoncolor = Sith( ).buttoncolor
        self.__image = r'C:\Users\terry\source\repos\BudgetPy\etc\img\app\notification\NotifyNinja.png'
        self.__message = '  ' + message if isinstance( message, str ) and message != '' else None

    def show( self ):
        return sg.popup_notify( self.__message,
            title = ' ' + 'Budget Execution',
            icon = self.__image,
            display_duration_in_ms = 9000,
            fade_in_duration = 5000,
            alpha = 1 )


class PdfForm( Sith ):
    '''Creates form to view a PDF'''
    __themebackground = None
    __elementbackcolor = None
    __elementforecolor = None
    __themetextcolor = None
    __textbackcolor = None
    __inputbackcolor = None
    __inputforecolor = None
    __buttoncolor = None
    __icon = None
    __formsize = None
    __themefont = None

    @property
    def size( self ):
        if isinstance( self.__formsize, tuple ) :
            return self.__formsize

    @size.setter
    def size( self, value ):
        if isinstance( value, tuple ) :
            self.__formsize = value

    def __init__( self ):
        super( Sith, self ).__init__()
        self.__themebackground = Sith( ).themebackground
        self.__themefont = Sith( ).themefont
        self.__icon = Sith( ).iconpath
        self.__elementbackcolor = Sith( ).elementbackcolor
        self.__elementforecolor = Sith( ).elementforecolor
        self.__themetextcolor = Sith( ).textforecolor
        self.__textbackcolor = Sith( ).textbackcolor
        self.__inputbackcolor = Sith( ).inputbackcolor
        self.__inputforecolor = Sith( ).inputforecolor
        self.__buttoncolor = Sith( ).buttoncolor
        self.__formsize = ( 600, 400 )

    def show( self ):
        filename = sg.popup_get_file( title = 'Budget Execution',
            message = 'PDF to open',
            file_types = ( ("PDF Files", "*.pdf"),
                           ("XPS Files", "*.*xps"),
                           ("Epub Files", "*.epub"),
                           ("HTML",   "*.htm*") ),
            icon = self.__icon )

        if filename is None:
            sg.popup_cancel( 'Cancelling', icon = self.__icon  )
            exit( 0 )

        document = fitz.open( filename )
        pages = len( document )
        tablist = [ None ] * pages
        title = f'Budget Execution display of { filename }, pages: { pages }'

        def get_page( pno, zoom = 0 ):
            displaylist = tablist[ pno ]
            if not displaylist:
                tablist[ pno ] = document[ pno ].get_displaylist( )
                displaylist = tablist[ pno ]

            r = displaylist.rect
            mp = r.tl + ( r.br - r.tl ) * 0.5
            mt = r.tl + ( r.tr - r.tl ) * 0.5
            ml = r.tl + ( r.bl - r.tl ) * 0.5
            mr = r.tr + ( r.br - r.tr ) * 0.5
            mb = r.bl + ( r.br - r.bl ) * 0.5
            mat = fitz.Matrix( 2, 2 )

            if zoom == 1:
                clip = fitz.Rect( r.tl, mp )
            elif zoom == 4:
                clip = fitz.Rect( mp, r.br )
            elif zoom == 2:
                clip = fitz.Rect( mt, mr )
            elif zoom == 3:
                clip = fitz.Rect( ml, mb )
            if zoom == 0:
                pix = displaylist.get_pixmap( alpha = False )
            else:
                pix = displaylist.get_pixmap( alpha = False,
                    matrix = mat, clip = clip )

            return pix

        currentpage = 0
        data = get_page( currentpage )
        image_elem = sg.Image( data = data )
        goto = sg.InputText( str( currentpage + 1 ), size = ( 5, 1 ) )

        layout = [ [ sg.Button( 'Prev' ), sg.Button( 'Next' ), sg.Text( 'Page:' ), goto, ],
                   [ sg.Text( 'Zoom:' ), sg.Button( 'Top-L' ), sg.Button( 'Top-R' ),
                     sg.Button( 'Bot-L' ),  sg.Button( 'Bot-R' ), ],
                   [ image_elem ],  ]

        pdfkeys = ( 'Next', 'Next:34', 'Prev', 'Prior:33',
            'Top-L', 'Top-R', 'Bot-L', 'Bot-R', 'MouseWheel:Down', 'MouseWheel:Up' )
        zoombuttons = ( 'Top-L', 'Top-R', 'Bot-L', 'Bot-R' )

        window = sg.Window( 'Budget Executon', layout,
            return_keyboard_events = True,
            icon = self.__icon,
            use_default_focus = False )

        oldpage = 0
        oldzoom = 0

        while True:
            event, values = window.read( timeout = 100 )
            zoom = 0
            forcepage = False
            if event == sg.WIN_CLOSED:
                break
            if event in ( 'Escape:27', ):
                break
            if event[ 0 ] == chr( 13 ):
                try:
                    while currentpage < 0:
                        currentpage += pages
                except:
                    currentpage = 0
                goto.update( str( currentpage + 1 ) )
            elif event in ( 'Next', 'Next:34', 'MouseWheel:Down' ):
                currentpage += 1
            elif event in ( 'Prev', 'Prior:33', 'MouseWheel:Up' ):
                currentpage -= 1
            elif event == 'Top-L':
                zoom = 1
            elif event == 'Top-R':
                zoom = 2
            elif event == 'Bot-L':
                zoom = 3
            elif event == 'Bot-R':
                zoom = 4
            if currentpage >= pages:
                currentpage = 0
            while currentpage < 0:
                currentpage += pages
            if currentpage != oldpage:
                zoom = oldzoom = 0
                forcepage = True
            if event in zoombuttons:
                if 0 < zoom == oldzoom:
                    zoom = 0
                    forcepage = True

                if zoom != oldzoom:
                    forcepage = True
            if forcepage:
                data = get_page( currentpage, zoom )
                image_elem.update( data = data )
                oldpage = currentpage
            oldzoom = zoom
            if event in pdfkeys or not values[ 0 ]:
                goto.update( str( currentpage + 1 ) )


# CalendarDialog( ) -> ( mm, dd, yyyy )
class CalendarDialog( Sith ):
    '''class creates form providing date selection behavior'''
    __themebackground = None
    __elementbackcolor = None
    __elementforecolor = None
    __themetextcolor = None
    __textbackcolor = None
    __inputbackcolor = None
    __inputforecolor = None
    __buttoncolor = None
    __icon = None
    __formsize = None
    __themefont = None
    __date = None

    @property
    def size( self ):
        if isinstance( self.__formsize, tuple ) :
            return self.__formsize

    @size.setter
    def size( self, value ):
        if isinstance( value, tuple ) :
            self.__formsize = value

    def __init__( self ):
        super( Sith, self ).__init__()
        self.__themebackground = Sith( ).themebackground
        self.__themefont = Sith( ).themefont
        self.__icon = Sith( ).iconpath
        self.__elementbackcolor = Sith( ).elementbackcolor
        self.__elementforecolor = Sith( ).elementforecolor
        self.__themetextcolor = Sith( ).textforecolor
        self.__textbackcolor = Sith( ).textbackcolor
        self.__inputbackcolor = Sith( ).inputbackcolor
        self.__inputforecolor = Sith( ).inputforecolor
        self.__buttoncolor = Sith( ).buttoncolor
        self.__formsize = ( 450, 250 )

    def show( self ):
        __btnsize = ( 20, 1 )
        __calendar = ( 200, 200 )

        months = [ 'JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL',
        'AUG', 'SEP', 'OCT', 'NOV', 'DEC' ]

        days = [ 'SUN', 'MON', 'TUE', 'WEC', 'THU', 'FRI', 'SAT' ]

        cal = sg.popup_get_date( title = 'Calendar',
                                 no_titlebar = False,
                                 icon = self.__icon,
                                 month_names = months,
                                 day_abbreviations = days,
                                 close_when_chosen = True )


class DatePanel( Sith ):
    ''' Desktop widget displaying date time text'''
    __themebackground = None
    __elementbackcolor = None
    __elementforecolor = None
    __themetextcolor = None
    __textbackcolor = None
    __inputbackcolor = None
    __inputforecolor = None
    __buttoncolor = None
    __icon = None
    __formsize = None
    __themefont = None
    __date = None

    @property
    def size( self ):
        if isinstance( self.__formsize, tuple ) :
            return self.__formsize

    @size.setter
    def size( self, value ):
        if isinstance( value, tuple ) :
            self.__formsize = value

    def __init__( self ):
        super( Sith, self ).__init__()
        self.__themebackground = Sith( ).themebackground
        self.__themefont = Sith( ).themefont
        self.__icon = Sith( ).iconpath
        self.__elementbackcolor = Sith( ).elementbackcolor
        self.__elementforecolor = Sith( ).elementforecolor
        self.__themetextcolor = Sith( ).textforecolor
        self.__textbackcolor = Sith( ).textbackcolor
        self.__inputbackcolor = Sith( ).inputbackcolor
        self.__inputforecolor = Sith( ).inputforecolor
        self.__buttoncolor = Sith( ).buttoncolor
        self.__formsize = ( 450, 250 )

    def show( self ):
        ALPHA = 0.9  # Initial alpha until user changes
        THEME = 'Dark green 3'  # Initial theme until user changes
        refresh_font = title_font = 'Roboto 8'
        main_info_font = 'Roboto 20'
        main_info_size = (10, 1)
        UPDATE_FREQUENCY_MILLISECONDS = 1000 * 60 * 60  # update every hour by default until set
        # by user

        def choose_theme( location, size ):
            """
            A window to allow new themes to be tried out.
            Changes the theme to the newly chosen one and returns theme's name
            Automaticallyi switches to new theme and saves the setting in user settings file

            :param location: (x,y) location of the Widget's window
            :type location:  Tuple[int, int]
            :param size: Size in pixels of the Widget's window
            :type size: Tuple[int, int]
            :return: The name of the newly selected theme
            :rtype: None | str
            """
            layout = [ [ sg.Text( 'Try a theme' ) ],
                       [ sg.Listbox( values = sg.theme_list( ), size = (20, 20), key = '-LIST-',
                           enable_events = True ) ],
                       [ sg.OK( ), sg.Cancel( ) ] ]

            window = sg.Window( 'Look and Feel Browser', layout, location = location,
                keep_on_top = True )
            old_theme = sg.theme( )
            while True:  # Event Loop
                event, values = window.read( )
                if event in (sg.WIN_CLOSED, 'Exit', 'OK', 'Cancel'):
                    break
                sg.theme( values[ '-LIST-' ][ 0 ] )
                window.hide( )
                # make at test window to the left of the current one
                test_window = make_window(
                    location = ((location[ 0 ] - size[ 0 ] * 1.2, location[ 1 ])),
                    test_window = True )
                test_window.read( close = True )
                window.un_hide( )
            window.close( )

            # after choice made, save theme or restore the old one
            if event == 'OK' and values[ '-LIST-' ]:
                sg.theme( values[ '-LIST-' ][ 0 ] )
                sg.user_settings_set_entry( '-theme-', values[ '-LIST-' ][ 0 ] )
                return values[ '-LIST-' ][ 0 ]
            else:
                sg.theme( old_theme )
            return None

        def make_window( location, test_window = False ):
            """
            Defines the layout and creates the window for the main window
            If the parm test_window is True, then a simplified, and EASY to close version is shown

            :param location: (x,y) location to create the window
            :type location: Tuple[int, int]
            :param test_window: If True, then this is a test window & will close by clicking on it
            :type test_window: bool
            :return: newly created window
            :rtype: sg.Window
            """
            title = sg.user_settings_get_entry( '-title-', '' )
            if not test_window:
                theme = sg.user_settings_get_entry( '-theme-', THEME )
                sg.theme( theme )

            # ------------------- Window Layout -------------------
            # If this is a test window (for choosing theme), then uses some extra Text Elements
            # to display theme text
            # and also enables events for the elements to make the window easy to close
            if test_window:
                top_elements = [ [ sg.Text( title, size = (20, 1), font = title_font,
                    justification = 'c', k = '-TITLE-', enable_events = True ) ],
                                 [ sg.Text( 'Click to close', font = title_font,
                                     enable_events = True ) ],
                                 [ sg.Text( 'This is theme', font = title_font,
                                     enable_events = True ) ],
                                 [ sg.Text( sg.theme( ), font = title_font,
                                     enable_events = True ) ] ]
                right_click_menu = [ [ '' ], [ 'Exit', ] ]
            else:
                top_elements = [ [ sg.Text( title, size = (20, 1), font = title_font,
                    justification = 'c', k = '-TITLE-' ) ] ]
                right_click_menu = [ [ '' ],
                                     [ 'Choose Title', 'Edit Me', 'New Theme', 'Save Location',
                                       'Refresh', 'Set Refresh Rate', 'Show Refresh Info',
                                       'Hide Refresh Info', 'Alpha',
                                       [ str( x ) for x in range( 1, 11 ) ], 'Exit', ] ]

            layout = top_elements + \
                     [ [ sg.Text( '0', size = main_info_size, font = main_info_font,
                         k = '-MAIN INFO-', justification = 'c', enable_events = test_window ) ],
                       [ sg.pin( sg.Text( size = (15, 2), font = refresh_font, k = '-REFRESHED-',
                           justification = 'c',
                           visible = sg.user_settings_get_entry( '-show refresh-', True ) ) ) ] ]

            # ------------------- Window Creation -------------------
            return sg.Window( 'Desktop Widget Template', layout, location = location,
                no_titlebar = True, grab_anywhere = True, margins = (0, 0),
                element_justification = 'c',
                element_padding = (0, 0),
                alpha_channel = sg.user_settings_get_entry( '-alpha-', ALPHA ), finalize = True,
                right_click_menu = right_click_menu, keep_on_top = True )

        def main( location ):
            """
            Where execution begins
            The Event Loop lives here, but the window creation is done in another function
            This is an important design pattern

            :param location: Location to create the main window if one is not found in the user
            settings
            :type location: Tuple[int, int]
            """

            window = make_window( sg.user_settings_get_entry( '-location-', location ) )

            refresh_frequency = sg.user_settings_get_entry( '-fresh frequency-',
                UPDATE_FREQUENCY_MILLISECONDS )

            while True:  # Event Loop
                # Normally a window.read goes here, but first we're updating the values in the
                # window, then reading it
                # First update the status text
                window[ '-MAIN INFO-' ].update( 'Your Info' )
                # for debugging show the last update date time
                window[ '-REFRESHED-' ].update(
                    datetime.datetime.now( ).strftime( "%m/%d/%Y\n%I:%M:%S %p" ) )

                # -------------- Start of normal event loop --------------
                event, values = window.read( timeout = refresh_frequency )
                print( event, values )
                if event in (sg.WIN_CLOSED, 'Exit'):  # standard exit test... ALWAYS do this
                    break
                if event == 'Edit Me':
                    sg.execute_editor( __file__ )
                elif event == 'Choose Title':
                    new_title = sg.popup_get_text( 'Choose a title for your Widget',
                        location = window.current_location( ), keep_on_top = True )
                    if new_title is not None:
                        window[ '-TITLE-' ].update( new_title )
                        sg.user_settings_set_entry( '-title-', new_title )
                elif event == 'Show Refresh Info':
                    window[ '-REFRESHED-' ].update( visible = True )
                    sg.user_settings_set_entry( '-show refresh-', True )
                elif event == 'Save Location':
                    sg.user_settings_set_entry( '-location-', window.current_location( ) )
                elif event == 'Hide Refresh Info':
                    window[ '-REFRESHED-' ].update( visible = False )
                    sg.user_settings_set_entry( '-show refresh-', False )
                elif event in [ str( x ) for x in range( 1, 11 ) ]:  # if Alpha Channel was chosen
                    window.set_alpha( int( event ) / 10 )
                    sg.user_settings_set_entry( '-alpha-', int( event ) / 10 )
                elif event == 'Set Refresh Rate':
                    choice = sg.popup_get_text(
                        'How frequently to update window in seconds? (can be a float)',
                        default_text = sg.user_settings_get_entry( '-fresh frequency-',
                            UPDATE_FREQUENCY_MILLISECONDS ) / 1000,
                        location = window.current_location( ), keep_on_top = True )
                    if choice is not None:
                        try:
                            refresh_frequency = float( choice ) * 1000  # convert to milliseconds
                            sg.user_settings_set_entry( '-fresh frequency-',
                                float( refresh_frequency ) )
                        except Exception as e:
                            sg.popup_error( f'You entered an incorrect number of seconds: {choice}',
                                f'Error: {e}', location = window.current_location( ),
                                keep_on_top = True )
                elif event == 'New Theme':
                    loc = window.current_location( )
                    if choose_theme( window.current_location( ), window.size ) is not None:
                        window.close( )  # out with the old...
                        window = make_window( loc )  # in with the new

            window.close( )

        if __name__ == '__main__':
            # To start the window at a specific location, get this location on the command line
            # The location should be in form x,y with no spaces
            location = (None, None)  # assume no location provided
            if len( sys.argv ) > 1:
                location = sys.argv[ 1 ].split( ',' )
                location = (int( location[ 0 ] ), int( location[ 1 ] ))
            main( location )


class ComboBoxDialog( Sith ):
    '''Logger object provides form for log printing'''
    __themebackground = None
    __elementbackcolor = None
    __elementforecolor = None
    __themetextcolor = None
    __textbackcolor = None
    __inputbackcolor = None
    __inputforecolor = None
    __buttoncolor = None
    __icon = None
    __formsize = None
    __themefont = None
    __items = None

    @property
    def size( self ):
        if isinstance( self.__formsize, tuple ) :
            return self.__formsize

    @size.setter
    def size( self, value ):
        if isinstance( value, tuple ) :
            self.__formsize = value

    @property
    def entry( self ):
        if isinstance( self.__entry, str )  and self.__entry != '':
            return self.__entry

    @entry.setter
    def entry( self, value ):
        if isinstance( value, str )  and value != '':
            self.__entry = value

    def __init__( self, data = None):
        super( Sith, self ).__init__( )
        self.__themebackground = Sith( ).themebackground
        self.__themefont = Sith( ).themefont
        self.__icon = Sith( ).iconpath
        self.__elementbackcolor = Sith( ).elementbackcolor
        self.__elementforecolor = Sith( ).elementforecolor
        self.__themetextcolor = Sith( ).textforecolor
        self.__textbackcolor = Sith( ).textbackcolor
        self.__inputbackcolor = Sith( ).inputbackcolor
        self.__inputforecolor = Sith( ).inputforecolor
        self.__buttoncolor = Sith( ).buttoncolor
        self.__formsize = ( 400, 150 )
        self.__items = data if isinstance( data, list ) and len( data ) > 0 else None

    def show( self ):
        btnsize = ( 10 , 1 )
        space = ( 5, 1 )
        if self.__items == None:
            self.__items = [ f'choice { x } ' for x in range( 30 ) ]
            values = self.__items

        layout = [ [ sg.Text( size = space ), sg.Text( size = space ) ],
                   [ sg.Text( size = space ), sg.Text( 'Make Selection' ) ],
                   [ sg.Text( size = space ) , sg.DropDown( values, key = '-ITEM-', size = ( 35, 1 ) ) ],
                   [ sg.Text( size = space ), sg.Text( size = space ) ],
                   [ sg.Text( size = space ), sg.OK( size = btnsize ), sg.Text( size = ( 8, 1 ) ), sg.Cancel( size = btnsize ) ] ]

        window = sg.Window( 'Budget Execution', layout,
            icon = self.__icon,
            size = self.__formsize )

        while True:
            event, values = window.read( )
            if event in ( sg.WIN_CLOSED, 'Exit', 'Cancel' ):
                break

        window.close()


# ListBoxDialog( data )
class ListBoxDialog( Sith ):
    '''List search and selection'''
    __themebackground = None
    __elementbackcolor = None
    __elementforecolor = None
    __themetextcolor = None
    __textbackcolor = None
    __inputbackcolor = None
    __inputforecolor = None
    __buttoncolor = None
    __icon = None
    __formsize = None
    __themefont = None
    __selecteditem = None
    __items = None
    __image = None

    @property
    def size( self ):
        if isinstance( self.__formsize, tuple ) :
            return self.__formsize

    @size.setter
    def size( self, value ):
        if isinstance( value, tuple ) :
            self.__formsize = value

    @property
    def selecteditem( self ):
        if isinstance( self.__selecteditem, str ) and self.__selecteditem != '':
            return self.__selecteditem

    @selecteditem.setter
    def selecteditem( self, value ):
        if isinstance( value, str ) and value != '':
            self.__selecteditem = value

    @property
    def items( self ):
        if isinstance( self.__items, list ):
            return self.__items

    @selecteditem.setter
    def items( self, value ):
        if isinstance( value, list ):
            self.__items = value

    def __init__( self, data = None ):
        self.__items = data if isinstance( data, list ) else [ ]
        super( Sith, self ).__init__()
        self.__themebackground = Sith( ).themebackground
        self.__themefont = Sith( ).themefont
        self.__icon = Sith( ).iconpath
        self.__elementbackcolor = Sith( ).elementbackcolor
        self.__elementforecolor = Sith( ).elementforecolor
        self.__themetextcolor = Sith( ).textforecolor
        self.__textbackcolor = Sith( ).textbackcolor
        self.__inputbackcolor = Sith( ).inputbackcolor
        self.__inputforecolor = Sith( ).inputforecolor
        self.__buttoncolor = Sith( ).buttoncolor
        self.__formsize = ( 400, 250 )
        self.__image = r'C:\Users\terry\source\repos\BudgetPy\etc\img\app\dialog\lookup.png'

    def show( self ):
        btnsize = ( 10, 1 )
        space = ( 10, 1 )
        line = ( 100, 1 )
        txtsize = ( 25, 1 )
        inpsize = ( 25, 1 )
        lstsize = ( 25, 5 )

        names = [ src for src in list( self.__items ) if src != 'NS' ]
        layout = [ [ sg.Text( '', size = space ), sg.Text( r'', size = line ) ],
                   [ sg.Text( '', size = space ), sg.Text( r'Search:' ) ],
                   [ sg.Text( '', size = space ), sg.Input( size = inpsize, enable_events = True, key = '-INPUT-' ) ],
                   [ sg.Text( '', size = space ), sg.Text( r'', size = line ) ],
                   [ sg.Text( '', size = space ), sg.Listbox( names, size = lstsize, enable_events = True, key = '-LIST-', font = self.__themefont ) ],
                   [ sg.Text( '', size = space ), sg.Text( r'', size = line ) ],
                   [ sg.Text( '', size = space ), sg.Button( 'Select', size = btnsize ), sg.Text( '', size = ( 3, 1 ) ), sg.Button( 'Exit', size = btnsize  ) ] ]

        window = sg.Window( '  Budget Execution', layout,
            size = self.__formsize,
            font = self.__themefont,
            icon = self.__icon )
        
        while True:
            event, values = window.read( )
            if event in ( sg.WIN_CLOSED, 'Exit' ):  # always check for closed window
                break
            if values[ '-INPUT-' ] != '':  # if a keystroke entered in search field
                search = values[ '-INPUT-' ]
                new_values = [ x for x in names if search in x ]  # do the filtering
                window[ '-LIST-' ].update( new_values )  # display in the listbox
            else:
                window[ '-LIST-' ].update( names )
            if event == '-LIST-' and len( values[ '-LIST-' ] ):
                sg.popup( 'Selected', values[ '-LIST-' ],
                    font = self.__themefont,
                    icon = self.__icon  )

        window.close( )


class ColorDialog( Sith ):
    '''class provides a form to select colors returning string values'''
    __themebackground = None
    __elementbackcolor = None
    __elementforecolor = None
    __themetextcolor = None
    __textbackcolor = None
    __inputbackcolor = None
    __inputforecolor = None
    __buttoncolor = None
    __icon = None
    __formsize = None
    __themefont = None
    __rgb = None
    __hex = None
    __html = None
    __argb = None

    @property
    def rgb( self ):
        if isinstance( self.__rgb, str ) and self.__rgb != '':
            return self.__rgb

    @rgb.setter
    def rgb( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rgb = value

    @property
    def hex( self ):
        if isinstance( self.__hex, str ) and self.__hex != '':
            return self.__hex

    @hex.setter
    def hex( self, value ):
        if isinstance( value, str ) and value != '':
            self.__hex = value

    @property
    def argb( self ):
        if isinstance( self.__argb, str ) and self.__argb != '':
            return self.__argb

    @argb.setter
    def argb( self, value ):
        if isinstance( value, str ) and value != '':
            self.__argb = value

    @property
    def html( self ):
        if isinstance( self.__html, str ) and self.__html != '':
            return self.__html

    @html.setter
    def html( self, value ):
        if isinstance( value, str ) and value != '':
            self.__html = value

    @property
    def size( self ):
        if isinstance( self.__formsize, tuple ) :
            return self.__formsize

    @size.setter
    def size( self, value ):
        if isinstance( value, tuple ) :
            self.__formsize = value

    def __init__( self ):
        super( Sith, self ).__init__()
        self.__themebackground = Sith( ).themebackground
        self.__themefont = Sith( ).themefont
        self.__icon = Sith( ).iconpath
        self.__elementbackcolor = Sith( ).elementbackcolor
        self.__elementforecolor = Sith( ).elementforecolor
        self.__themetextcolor = Sith( ).textforecolor
        self.__textbackcolor = Sith( ).textbackcolor
        self.__inputbackcolor = Sith( ).inputbackcolor
        self.__inputforecolor = Sith( ).inputforecolor
        self.__buttoncolor = Sith( ).buttoncolor
        self.__formsize = ( 450, 450 )

    def show( self ):
        import sys
        color_map = { 'alice blue': '#F0F8FF', 
                      'AliceBlue': '#F0F8FF',
                      'antique white': '#FAEBD7', 
                      'AntiqueWhite': '#FAEBD7',
                      'AntiqueWhite1': '#FFEFDB', 
                      'AntiqueWhite2': '#EEDFCC',
                      'AntiqueWhite3': '#CDC0B0',  
                      'AntiqueWhite4': '#8B8378',
                      'aquamarine': '#7FFFD4',  
                      'aquamarine1': '#7FFFD4',
                      'aquamarine2': '#76EEC6', 
                      'aquamarine3': '#66CDAA',
                      'aquamarine4': '#458B74', 
                      'azure': '#F0FFFF',
                      'azure1': '#F0FFFF',
                      'azure2': '#E0EEEE',
                      'azure3': '#C1CDCD',
                      'azure4': '#838B8B',
                      'beige': '#F5F5DC',
                      'bisque':  '#FFE4C4',
                      'bisque1':  '#FFE4C4',
                      'bisque2':  '#EED5B7',
                      'bisque3':  '#CDB79E',
                      'bisque4':  '#8B7D6B',
                      'black':  '#000000',
                      'blanched almond':  '#FFEBCD',
                      'BlanchedAlmond':  '#FFEBCD',
                      'blue':  '#0000FF',
                      'blue violet':  '#8A2BE2',
                      'blue1':  '#0000FF',
                      'blue2':  '#0000EE',
                      'blue3':  '#0000CD',
                      'blue4':  '#00008B',
                      'BlueViolet':  '#8A2BE2',
                      'brown':  '#A52A2A',
                      'brown1':  '#FF4040',
                      'brown2':  '#EE3B3B',
                      'brown3':  '#CD3333',
                      'brown4':  '#8B2323',
                      'burlywood':  '#DEB887',
                      'burlywood1':  '#FFD39B',
                      'burlywood2':  '#EEC591',
                      'burlywood3':  '#CDAA7D',
                      'burlywood4':  '#8B7355',
                      'cadet blue':  '#5F9EA0',
                      'CadetBlue':  '#5F9EA0',
                      'CadetBlue1':  '#98F5FF',
                      'CadetBlue2':  '#8EE5EE',
                      'CadetBlue3':  '#7AC5CD',
                      'CadetBlue4':  '#53868B',
                      'chartreuse':  '#7FFF00',
                      'chartreuse1':  '#7FFF00',
                      'chartreuse2':  '#76EE00',
                      'chartreuse3':  '#66CD00',
                      'chartreuse4':  '#458B00',
                      'chocolate':  '#D2691E',
                      'chocolate1':  '#FF7F24',
                      'chocolate2':  '#EE7621',
                      'chocolate3':  '#CD661D',
                      'chocolate4':  '#8B4513',
                      'coral':  '#FF7F50',
                      'coral1':  '#FF7256',
                      'coral2':  '#EE6A50',
                      'coral3':  '#CD5B45',
                      'coral4':  '#8B3E2F',
                      'cornflower blue':  '#6495ED',
                      'CornflowerBlue':  '#6495ED',
                      'cornsilk':  '#FFF8DC',
                      'cornsilk1':  '#FFF8DC',
                      'cornsilk2':  '#EEE8CD',
                      'cornsilk3':  '#CDC8B1',
                      'cornsilk4':  '#8B8878',
                      'cyan':  '#00FFFF',
                      'cyan1':  '#00FFFF',
                      'cyan2':  '#00EEEE',
                      'cyan3':  '#00CDCD',
                      'cyan4':  '#008B8B',
                      'dark blue':  '#00008B',
                      'dark cyan':  '#008B8B',
                      'dark goldenrod':  '#B8860B',
                      'dark gray':  '#A9A9A9',
                      'dark green':  '#006400',
                      'dark grey':  '#A9A9A9',
                      'dark khaki':  '#BDB76B',
                      'dark magenta':  '#8B008B',
                      'dark olive green':  '#556B2F',
                      'dark orange':  '#FF8C00',
                      'dark orchid':  '#9932CC',
                      'dark red':  '#8B0000',
                      'dark salmon':  '#E9967A',
                      'dark sea green':  '#8FBC8F',
                      'dark slate blue':  '#483D8B',
                      'dark slate gray':  '#2F4F4F',
                      'dark slate grey':  '#2F4F4F',
                      'dark turquoise':  '#00CED1',
                      'dark violet':  '#9400D3',
                      'DarkBlue':  '#00008B',
                      'DarkCyan':  '#008B8B',
                      'DarkGoldenrod':  '#B8860B',
                      'DarkGoldenrod1':  '#FFB90F',
                      'DarkGoldenrod2':  '#EEAD0E',
                      'DarkGoldenrod3':  '#CD950C',
                      'DarkGoldenrod4':  '#8B6508',
                      'DarkGray':  '#A9A9A9',
                      'DarkGreen':  '#006400',
                      'DarkGrey':  '#A9A9A9',
                      'DarkKhaki':  '#BDB76B',
                      'DarkMagenta':  '#8B008B',
                      'DarkOliveGreen':  '#556B2F',
                      'DarkOliveGreen1':  '#CAFF70',
                      'DarkOliveGreen2':  '#BCEE68',
                      'DarkOliveGreen3':  '#A2CD5A',
                      'DarkOliveGreen4':  '#6E8B3D',
                      'DarkOrange':  '#FF8C00',
                      'DarkOrange1':  '#FF7F00',
                      'DarkOrange2':  '#EE7600',
                      'DarkOrange3':  '#CD6600',
                      'DarkOrange4':  '#8B4500',
                      'DarkOrchid':  '#9932CC',
                      'DarkOrchid1':  '#BF3EFF',
                      'DarkOrchid2':  '#B23AEE',
                      'DarkOrchid3':  '#9A32CD',
                      'DarkOrchid4':  '#68228B',
                      'DarkRed':  '#8B0000',
                      'DarkSalmon':  '#E9967A',
                      'DarkSeaGreen':  '#8FBC8F',
                      'DarkSeaGreen1':  '#C1FFC1',
                      'DarkSeaGreen2':  '#B4EEB4',
                      'DarkSeaGreen3':  '#9BCD9B',
                      'DarkSeaGreen4':  '#698B69',
                      'DarkSlateBlue':  '#483D8B',
                      'DarkSlateGray':  '#2F4F4F',
                      'DarkSlateGray1':  '#97FFFF',
                      'DarkSlateGray2':  '#8DEEEE',
                      'DarkSlateGray3':  '#79CDCD',
                      'DarkSlateGray4':  '#528B8B',
                      'DarkSlateGrey':  '#2F4F4F',
                      'DarkTurquoise':  '#00CED1',
                      'DarkViolet':  '#9400D3',
                      'deep pink':  '#FF1493',
                      'deep sky blue':  '#00BFFF',
                      'DeepPink':  '#FF1493',
                      'DeepPink1':  '#FF1493',
                      'DeepPink2':  '#EE1289',
                      'DeepPink3':  '#CD1076',
                      'DeepPink4':  '#8B0A50',
                      'DeepSkyBlue':  '#00BFFF',
                      'DeepSkyBlue1':  '#00BFFF',
                      'DeepSkyBlue2':  '#00B2EE',
                      'DeepSkyBlue3':  '#009ACD',
                      'DeepSkyBlue4':  '#00688B',
                      'dim gray':  '#696969',
                      'dim grey':  '#696969',
                      'DimGray':  '#696969',
                      'DimGrey':  '#696969',
                      'dodger blue':  '#1E90FF',
                      'DodgerBlue':  '#1E90FF',
                      'DodgerBlue1':  '#1E90FF',
                      'DodgerBlue2':  '#1C86EE',
                      'DodgerBlue3':  '#1874CD',
                      'DodgerBlue4':  '#104E8B',
                      'firebrick':  '#B22222',
                      'firebrick1':  '#FF3030',
                      'firebrick2':  '#EE2C2C',
                      'firebrick3':  '#CD2626',
                      'firebrick4':  '#8B1A1A',
                      'floral white':  '#FFFAF0',
                      'FloralWhite':  '#FFFAF0',
                      'forest green':  '#228B22',
                      'ForestGreen':  '#228B22',
                      'gainsboro':  '#DCDCDC',
                      'ghost white':  '#F8F8FF',
                      'GhostWhite':  '#F8F8FF',
                      'gold':  '#FFD700',
                      'gold1':  '#FFD700',
                      'gold2':  '#EEC900',
                      'gold3':  '#CDAD00',
                      'gold4':  '#8B7500',
                      'goldenrod':  '#DAA520',
                      'goldenrod1':  '#FFC125',
                      'goldenrod2':  '#EEB422',
                      'goldenrod3':  '#CD9B1D',
                      'goldenrod4':  '#8B6914',
                      'green':  '#00FF00',
                      'green yellow':  '#ADFF2F',
                      'green1':  '#00FF00',
                      'green2':  '#00EE00',
                      'green3':  '#00CD00',
                      'green4':  '#008B00',
                      'GreenYellow':  '#ADFF2F',
                      'grey':  '#BEBEBE',
                      'grey0':  '#000000',
                      'grey1':  '#030303',
                      'grey2':  '#050505',
                      'grey3':  '#080808',
                      'grey4':  '#0A0A0A',
                      'grey5':  '#0D0D0D',
                      'grey6':  '#0F0F0F',
                      'grey7':  '#121212',
                      'grey8':  '#141414',
                      'grey9':  '#171717',
                      'grey10':  '#1A1A1A',
                      'grey11':  '#1C1C1C',
                      'grey12':  '#1F1F1F',
                      'grey13':  '#212121',
                      'grey14':  '#242424',
                      'grey15':  '#262626',
                      'grey16':  '#292929',
                      'grey17':  '#2B2B2B',
                      'grey18':  '#2E2E2E',
                      'grey19':  '#303030',
                      'grey20':  '#333333',
                      'grey21':  '#363636',
                      'grey22':  '#383838',
                      'grey23':  '#3B3B3B',
                      'grey24':  '#3D3D3D',
                      'grey25':  '#404040',
                      'grey26':  '#424242',
                      'grey27':  '#454545',
                      'grey28':  '#474747',
                      'grey29':  '#4A4A4A',
                      'grey30':  '#4D4D4D',
                      'grey31':  '#4F4F4F',
                      'grey32':  '#525252',
                      'grey33':  '#545454',
                      'grey34':  '#575757',
                      'grey35':  '#595959',
                      'grey36':  '#5C5C5C',
                      'grey37':  '#5E5E5E',
                      'grey38':  '#616161',
                      'grey39':  '#636363',
                      'grey40':  '#666666',
                      'grey41':  '#696969',
                      'grey42':  '#6B6B6B',
                      'grey43':  '#6E6E6E',
                      'grey44':  '#707070',
                      'grey45':  '#737373',
                      'grey46':  '#757575',
                      'grey47':  '#787878',
                      'grey48':  '#7A7A7A',
                      'grey49':  '#7D7D7D',
                      'grey50':  '#7F7F7F',
                      'grey51':  '#828282',
                      'grey52':  '#858585',
                      'grey53':  '#878787',
                      'grey54':  '#8A8A8A',
                      'grey55':  '#8C8C8C',
                      'grey56':  '#8F8F8F',
                      'grey57':  '#919191',
                      'grey58':  '#949494',
                      'grey59':  '#969696',
                      'grey60':  '#999999',
                      'grey61':  '#9C9C9C',
                      'grey62':  '#9E9E9E',
                      'grey63':  '#A1A1A1',
                      'grey64':  '#A3A3A3',
                      'grey65':  '#A6A6A6',
                      'grey66':  '#A8A8A8',
                      'grey67':  '#ABABAB',
                      'grey68':  '#ADADAD',
                      'grey69':  '#B0B0B0',
                      'grey70':  '#B3B3B3',
                      'grey71':  '#B5B5B5',
                      'grey72':  '#B8B8B8',
                      'grey73':  '#BABABA',
                      'grey74':  '#BDBDBD',
                      'grey75':  '#BFBFBF',
                      'grey76':  '#C2C2C2',
                      'grey77':  '#C4C4C4',
                      'grey78':  '#C7C7C7',
                      'grey79':  '#C9C9C9',
                      'grey80':  '#CCCCCC',
                      'grey81':  '#CFCFCF',
                      'grey82':  '#D1D1D1',
                      'grey83':  '#D4D4D4',
                      'grey84':  '#D6D6D6',
                      'grey85':  '#D9D9D9',
                      'grey86':  '#DBDBDB',
                      'grey87':  '#DEDEDE',
                      'grey88':  '#E0E0E0',
                      'grey89':  '#E3E3E3',
                      'grey90':  '#E5E5E5',
                      'grey91':  '#E8E8E8',
                      'grey92':  '#EBEBEB',
                      'grey93':  '#EDEDED',
                      'grey94':  '#F0F0F0',
                      'grey95':  '#F2F2F2',
                      'grey96':  '#F5F5F5',
                      'grey97':  '#F7F7F7',
                      'grey98':  '#FAFAFA',
                      'grey99':  '#FCFCFC',
                      'grey100':  '#FFFFFF',
                      'honeydew':  '#F0FFF0',
                      'honeydew1':  '#F0FFF0',
                      'honeydew2':  '#E0EEE0',
                      'honeydew3':  '#C1CDC1',
                      'honeydew4':  '#838B83',
                      'hot pink':  '#FF69B4',
                      'HotPink':  '#FF69B4',
                      'HotPink1':  '#FF6EB4',
                      'HotPink2':  '#EE6AA7',
                      'HotPink3':  '#CD6090',
                      'HotPink4':  '#8B3A62',
                      'indian red':  '#CD5C5C',
                      'IndianRed':  '#CD5C5C',
                      'IndianRed1':  '#FF6A6A',
                      'IndianRed2':  '#EE6363',
                      'IndianRed3':  '#CD5555',
                      'IndianRed4':  '#8B3A3A',
                      'ivory':  '#FFFFF0',
                      'ivory1':  '#FFFFF0',
                      'ivory2':  '#EEEEE0',
                      'ivory3':  '#CDCDC1',
                      'ivory4':  '#8B8B83',
                      'khaki':  '#F0E68C',
                      'khaki1':  '#FFF68F',
                      'khaki2':  '#EEE685',
                      'khaki3':  '#CDC673',
                      'khaki4':  '#8B864E',
                      'lavender':  '#E6E6FA',
                      'lavender blush':  '#FFF0F5',
                      'LavenderBlush':  '#FFF0F5',
                      'LavenderBlush1':  '#FFF0F5',
                      'LavenderBlush2':  '#EEE0E5',
                      'LavenderBlush3':  '#CDC1C5',
                      'LavenderBlush4':  '#8B8386',
                      'lawn green':  '#7CFC00',
                      'LawnGreen':  '#7CFC00',
                      'lemon chiffon':  '#FFFACD',
                      'LemonChiffon':  '#FFFACD',
                      'LemonChiffon1':  '#FFFACD',
                      'LemonChiffon2':  '#EEE9BF',
                      'LemonChiffon3':  '#CDC9A5',
                      'LemonChiffon4':  '#8B8970',
                      'light blue':  '#ADD8E6',
                      'light coral':  '#F08080',
                      'light cyan':  '#E0FFFF',
                      'light goldenrod':  '#EEDD82',
                      'light goldenrod yellow': '#FAFAD2',
                      'light gray':  '#D3D3D3',
                      'light green':  '#90EE90',
                      'light grey':  '#D3D3D3',
                      'light pink':  '#FFB6C1',
                      'light salmon':  '#FFA07A',
                      'light sea green':  '#20B2AA',
                      'light sky blue':  '#87CEFA',
                      'light slate blue':  '#8470FF',
                      'light slate gray':  '#778899',
                      'light slate grey':  '#778899',
                      'light steel blue':  '#B0C4DE',
                      'light yellow':  '#FFFFE0',
                      'LightBlue':  '#ADD8E6',
                      'LightBlue1':  '#BFEFFF',
                      'LightBlue2':  '#B2DFEE',
                      'LightBlue3':  '#9AC0CD',
                      'LightBlue4':  '#68838B',
                      'LightCoral':  '#F08080',
                      'LightCyan':  '#E0FFFF',
                      'LightCyan1':  '#E0FFFF',
                      'LightCyan2':  '#D1EEEE',
                      'LightCyan3':  '#B4CDCD',
                      'LightCyan4':  '#7A8B8B',
                      'LightGoldenrod':  '#EEDD82',
                      'LightGoldenrod1':  '#FFEC8B',
                      'LightGoldenrod2':  '#EEDC82',
                      'LightGoldenrod3':  '#CDBE70',
                      'LightGoldenrod4':  '#8B814C',
                      'LightGoldenrodYellow':   '#FAFAD2',
                      'LightGray':  '#D3D3D3',
                      'LightGreen':  '#90EE90',
                      'LightGrey':  '#D3D3D3',
                      'LightPink':  '#FFB6C1',
                      'LightPink1':  '#FFAEB9',
                      'LightPink2':  '#EEA2AD',
                      'LightPink3':  '#CD8C95',
                      'LightPink4':  '#8B5F65',
                      'LightSalmon':  '#FFA07A',
                      'LightSalmon1':  '#FFA07A',
                      'LightSalmon2':  '#EE9572',
                      'LightSalmon3':  '#CD8162',
                      'LightSalmon4':  '#8B5742',
                      'LightSeaGreen':  '#20B2AA',
                      'LightSkyBlue':  '#87CEFA',
                      'LightSkyBlue1':  '#B0E2FF',
                      'LightSkyBlue2':  '#A4D3EE',
                      'LightSkyBlue3':  '#8DB6CD',
                      'LightSkyBlue4':  '#607B8B',
                      'LightSlateBlue':  '#8470FF',
                      'LightSlateGray':  '#778899',
                      'LightSlateGrey':  '#778899',
                      'LightSteelBlue':  '#B0C4DE',
                      'LightSteelBlue1':  '#CAE1FF',
                      'LightSteelBlue2':  '#BCD2EE',
                      'LightSteelBlue3':  '#A2B5CD',
                      'LightSteelBlue4':  '#6E7B8B',
                      'LightYellow':  '#FFFFE0',
                      'LightYellow1':  '#FFFFE0',
                      'LightYellow2':  '#EEEED1',
                      'LightYellow3':  '#CDCDB4',
                      'LightYellow4':  '#8B8B7A',
                      'lime green':  '#32CD32',
                      'LimeGreen':  '#32CD32',
                      'linen':  '#FAF0E6',
                      'magenta':  '#FF00FF',
                      'magenta1':  '#FF00FF',
                      'magenta2':  '#EE00EE',
                      'magenta3':  '#CD00CD',
                      'magenta4':  '#8B008B',
                      'maroon':  '#B03060',
                      'maroon1':  '#FF34B3',
                      'maroon2':  '#EE30A7',
                      'maroon3':  '#CD2990',
                      'maroon4':  '#8B1C62',
                      'medium aquamarine':      '#66CDAA',
                      'medium blue':  '#0000CD',
                      'medium orchid':  '#BA55D3',
                      'medium purple':  '#9370DB',
                      'medium sea green':  '#3CB371',
                      'medium slate blue':      '#7B68EE',
                      'medium spring green':    '#00FA9A',
                      'medium turquoise':  '#48D1CC',
                      'medium violet red':      '#C71585',
                      'MediumAquamarine':  '#66CDAA',
                      'MediumBlue':  '#0000CD',
                      'MediumOrchid':  '#BA55D3',
                      'MediumOrchid1':  '#E066FF',
                      'MediumOrchid2':  '#D15FEE',
                      'MediumOrchid3':  '#B452CD',
                      'MediumOrchid4':  '#7A378B',
                      'MediumPurple':  '#9370DB',
                      'MediumPurple1':  '#AB82FF',
                      'MediumPurple2':  '#9F79EE',
                      'MediumPurple3':  '#8968CD',
                      'MediumPurple4':  '#5D478B',
                      'MediumSeaGreen':  '#3CB371',
                      'MediumSlateBlue':  '#7B68EE',
                      'MediumSpringGreen':      '#00FA9A',
                      'MediumTurquoise':  '#48D1CC',
                      'MediumVioletRed':  '#C71585',
                      'midnight blue':  '#191970',
                      'MidnightBlue':  '#191970',
                      'mint cream':  '#F5FFFA',
                      'MintCream':  '#F5FFFA',
                      'misty rose':  '#FFE4E1',
                      'MistyRose':  '#FFE4E1',
                      'MistyRose1':  '#FFE4E1',
                      'MistyRose2':  '#EED5D2',
                      'MistyRose3':  '#CDB7B5',
                      'MistyRose4':  '#8B7D7B',
                      'moccasin':  '#FFE4B5',
                      'navajo white':  '#FFDEAD',
                      'NavajoWhite':  '#FFDEAD',
                      'NavajoWhite1':  '#FFDEAD',
                      'NavajoWhite2':  '#EECFA1',
                      'NavajoWhite3':  '#CDB38B',
                      'NavajoWhite4':  '#8B795E',
                      'navy':  '#000080',
                      'navy blue':  '#000080',
                      'NavyBlue':  '#000080',
                      'old lace':  '#FDF5E6',
                      'OldLace':  '#FDF5E6',
                      'olive drab':  '#6B8E23',
                      'OliveDrab':  '#6B8E23',
                      'OliveDrab1':  '#C0FF3E',
                      'OliveDrab2':  '#B3EE3A',
                      'OliveDrab3':  '#9ACD32',
                      'OliveDrab4':  '#698B22',
                      'orange':  '#FFA500',
                      'orange red':  '#FF4500',
                      'orange1':  '#FFA500',
                      'orange2':  '#EE9A00',
                      'orange3':  '#CD8500',
                      'orange4':  '#8B5A00',
                      'OrangeRed':  '#FF4500',
                      'OrangeRed1':  '#FF4500',
                      'OrangeRed2':  '#EE4000',
                      'OrangeRed3':  '#CD3700',
                      'OrangeRed4':  '#8B2500',
                      'orchid':  '#DA70D6',
                      'orchid1':  '#FF83FA',
                      'orchid2':  '#EE7AE9',
                      'orchid3':  '#CD69C9',
                      'orchid4':  '#8B4789',
                      'pale goldenrod':  '#EEE8AA',
                      'pale green':  '#98FB98',
                      'pale turquoise':  '#AFEEEE',
                      'pale violet red':  '#DB7093',
                      'PaleGoldenrod':  '#EEE8AA',
                      'PaleGreen':  '#98FB98',
                      'PaleGreen1':  '#9AFF9A',
                      'PaleGreen2':  '#90EE90',
                      'PaleGreen3':  '#7CCD7C',
                      'PaleGreen4':  '#548B54',
                      'PaleTurquoise':  '#AFEEEE',
                      'PaleTurquoise1':  '#BBFFFF',
                      'PaleTurquoise2':  '#AEEEEE',
                      'PaleTurquoise3':  '#96CDCD',
                      'PaleTurquoise4':  '#668B8B',
                      'PaleVioletRed':  '#DB7093',
                      'PaleVioletRed1':  '#FF82AB',
                      'PaleVioletRed2':  '#EE799F',
                      'PaleVioletRed3':  '#CD687F',
                      'PaleVioletRed4':  '#8B475D',
                      'papaya whip':  '#FFEFD5',
                      'PapayaWhip':  '#FFEFD5',
                      'peach puff':  '#FFDAB9',
                      'PeachPuff':  '#FFDAB9',
                      'PeachPuff1':  '#FFDAB9',
                      'PeachPuff2':  '#EECBAD',
                      'PeachPuff3':  '#CDAF95',
                      'PeachPuff4':  '#8B7765',
                      'peru':  '#CD853F',
                      'pink':  '#FFC0CB',
                      'pink1':  '#FFB5C5',
                      'pink2':  '#EEA9B8',
                      'pink3':  '#CD919E',
                      'pink4':  '#8B636C',
                      'plum':  '#DDA0DD',
                      'plum1':  '#FFBBFF',
                      'plum2':  '#EEAEEE',
                      'plum3':  '#CD96CD',
                      'plum4':  '#8B668B',
                      'powder blue':  '#B0E0E6',
                      'PowderBlue':  '#B0E0E6',
                      'purple':  '#A020F0',
                      'purple1':  '#9B30FF',
                      'purple2':  '#912CEE',
                      'purple3':  '#7D26CD',
                      'purple4':  '#551A8B',
                      'red':  '#FF0000',
                      'red1':  '#FF0000',
                      'red2':  '#EE0000',
                      'red3':  '#CD0000',
                      'red4':  '#8B0000',
                      'rosy brown':  '#BC8F8F',
                      'RosyBrown':  '#BC8F8F',
                      'RosyBrown1':  '#FFC1C1',
                      'RosyBrown2':  '#EEB4B4',
                      'RosyBrown3':  '#CD9B9B',
                      'RosyBrown4':  '#8B6969',
                      'royal blue':  '#4169E1',
                      'RoyalBlue':  '#4169E1',
                      'RoyalBlue1':  '#4876FF',
                      'RoyalBlue2':  '#436EEE',
                      'RoyalBlue3':  '#3A5FCD',
                      'RoyalBlue4':  '#27408B',
                      'saddle brown':  '#8B4513',
                      'SaddleBrown':  '#8B4513',
                      'salmon':  '#FA8072',
                      'salmon1':  '#FF8C69',
                      'salmon2':  '#EE8262',
                      'salmon3':  '#CD7054',
                      'salmon4':  '#8B4C39',
                      'sandy brown':  '#F4A460',
                      'SandyBrown':  '#F4A460',
                      'sea green':  '#2E8B57',
                      'SeaGreen':  '#2E8B57',
                      'SeaGreen1':  '#54FF9F',
                      'SeaGreen2':  '#4EEE94',
                      'SeaGreen3':  '#43CD80',
                      'SeaGreen4':  '#2E8B57',
                      'seashell':  '#FFF5EE',
                      'seashell1':  '#FFF5EE',
                      'seashell2':  '#EEE5DE',
                      'seashell3':  '#CDC5BF',
                      'seashell4':  '#8B8682',
                      'sienna':  '#A0522D',
                      'sienna1':  '#FF8247',
                      'sienna2':  '#EE7942',
                      'sienna3':  '#CD6839',
                      'sienna4':  '#8B4726',
                      'sky blue':  '#87CEEB',
                      'SkyBlue':  '#87CEEB',
                      'SkyBlue1':  '#87CEFF',
                      'SkyBlue2':  '#7EC0EE',
                      'SkyBlue3':  '#6CA6CD',
                      'SkyBlue4':  '#4A708B',
                      'slate blue':  '#6A5ACD',
                      'slate gray':  '#708090',
                      'slate grey':  '#708090',
                      'SlateBlue':  '#6A5ACD',
                      'SlateBlue1':  '#836FFF',
                      'SlateBlue2':  '#7A67EE',
                      'SlateBlue3':  '#6959CD',
                      'SlateBlue4':  '#473C8B',
                      'SlateGray':  '#708090',
                      'SlateGray1':  '#C6E2FF',
                      'SlateGray2':  '#B9D3EE',
                      'SlateGray3':  '#9FB6CD',
                      'SlateGray4':  '#6C7B8B',
                      'SlateGrey':  '#708090',
                      'snow':  '#FFFAFA',
                      'snow1':  '#FFFAFA',
                      'snow2':  '#EEE9E9',
                      'snow3':  '#CDC9C9',
                      'snow4':  '#8B8989',
                      'spring green':  '#00FF7F',
                      'SpringGreen':  '#00FF7F',
                      'SpringGreen1':  '#00FF7F',
                      'SpringGreen2':  '#00EE76',
                      'SpringGreen3':  '#00CD66',
                      'SpringGreen4':  '#008B45',
                      'steel blue':  '#4682B4',
                      'SteelBlue':  '#4682B4',
                      'SteelBlue1':  '#63B8FF',
                      'SteelBlue2':  '#5CACEE',
                      'SteelBlue3':  '#4F94CD',
                      'SteelBlue4':  '#36648B',
                      'tan':  '#D2B48C',
                      'tan1':  '#FFA54F',
                      'tan2':  '#EE9A49',
                      'tan3':  '#CD853F',
                      'tan4':  '#8B5A2B',
                      'thistle':  '#D8BFD8',
                      'thistle1':  '#FFE1FF',
                      'thistle2':  '#EED2EE',
                      'thistle3':  '#CDB5CD',
                      'thistle4':  '#8B7B8B',
                      'tomato':  '#FF6347',
                      'tomato1':  '#FF6347',
                      'tomato2':  '#EE5C42',
                      'tomato3':  '#CD4F39',
                      'tomato4':  '#8B3626',
                      'turquoise':  '#40E0D0',
                      'turquoise1':  '#00F5FF',
                      'turquoise2':  '#00E5EE',
                      'turquoise3':  '#00C5CD',
                      'turquoise4':  '#00868B',
                      'violet':  '#EE82EE',
                      'violet red':  '#D02090',
                      'VioletRed':  '#D02090',
                      'VioletRed1':  '#FF3E96',
                      'VioletRed2':  '#EE3A8C',
                      'VioletRed3':  '#CD3278',
                      'VioletRed4':  '#8B2252',
                      'wheat':  '#F5DEB3',
                      'wheat1':  '#FFE7BA',
                      'wheat2':  '#EED8AE',
                      'wheat3':  '#CDBA96',
                      'wheat4':  '#8B7E66',
                      'white':  '#FFFFFF',
                      'white smoke':  '#F5F5F5',
                      'WhiteSmoke':  '#F5F5F5',
                      'yellow':  '#FFFF00',
                      'yellow green':  '#9ACD32',
                      'yellow1':  '#FFFF00',
                      'yellow2':  '#EEEE00',
                      'yellow3':  '#CDCD00',
                      'yellow4':  '#8B8B00',
                      'YellowGreen':  '#9ACD32' }
        hex_to_color = { v: k for k, v in color_map.items( ) }
        color_list = list( color_map.keys( ) )
        COLORS_PER_ROW = 40
        font_size = 9

        def make_window( ):
            layout = [ [ sg.Text( '' ), ],
                       [ sg.Text( f'{ len( color_list ) } Colors', font = self.__themefont ), ],
                       [ sg.Text( ' ', size = ( 5, 1 ) ), ] ]

            for rows in range( len( color_list ) // COLORS_PER_ROW+1 ):
                row = [ ]

                for i in range( COLORS_PER_ROW ):
                    try:
                        color = color_list[ rows * COLORS_PER_ROW + i ]
                        row.append( sg.T( ' ', s = 1, background_color = color, text_color = color, font = self.__themefont , right_click_menu = [ '_', color_map[ color ] ],
                            tooltip = color, enable_events = True, key = ( color, color_map[ color ] ) ) )
                    except IndexError as e:
                        break
                    except Exception as e:
                        sg.popup_error( f'Error while creating color window....', e,
                            f'rows = { rows }  i = { i }' )
                        break
                layout.append( row )
            layout.append( [ sg.Text( ' ', size = ( 10, 1 ) ), ] )
            layout.append( [ sg.Text( ' ', size = ( 10, 1 ) ), ] )
            layout.append( [ sg.Text( ' ', size = ( 50, 1 ) ), sg.Cancel( size = ( 20, 1 )  ), ] )

            return sg.Window( 'Budget Execution', layout,
                font = self.__themefont,
                size = self.__formsize,
                element_padding = ( 1, 1 ),
                border_depth = 0,
                icon = self.__icon,
                right_click_menu = sg.MENU_RIGHT_CLICK_EDITME_EXIT,
                use_ttk_buttons = True )

        window = make_window( )

        while True:
            event, values = window.read( )
            if event in ( sg.WIN_CLOSED, 'Cancel', 'Exit' ):
                break
            if event == 'Edit me':
                sg.execute_editor( __file__ )
                continue
            elif isinstance(event, tuple):
                color, color_hex = event[ 0 ], event[ 1 ]
            else:
                color, color_hex = hex_to_color[ event ], event

            layout2 = [ [ sg.Text( color_hex + ' on clipboard' ) ],
                       [ sg.DummyButton( color, button_color = self.__buttoncolor, tooltip = color_hex ),
                        sg.DummyButton( color, button_color = self.__buttoncolor, tooltip = color_hex ) ] ]

            window2 = sg.Window( 'Buttons with white and black text', layout2,
                keep_on_top = True,
                finalize = True,
                size = self.__formsize,
                icon = self.__icon )

            sg.clipboard_set(color_hex)

        window.close()

        sg.popup_quick_message('Building window... one moment please...',
            background_color = self.__themebackground,
            icon = self.__icon,
            text_color = self.__themetextcolor,
            font = self.__themefont )

        sg.set_options( button_element_size = (12, 1),
            element_padding = (0, 0),
            auto_size_buttons = False,
            border_width = 1,
            tooltip_time = 100)


class Dashboard( Sith ):
    '''class defining basic dashboard for the application'''
    __themebackground = None
    __elementbackcolor = None
    __elementforecolor = None
    __themetextcolor = None
    __textbackcolor = None
    __inputbackcolor = None
    __inputforecolor = None
    __buttoncolor = None
    __icon = None
    __image = None
    __formsize = None
    __themefont = None
    __title = None
    __header = None

    @property
    def title( self ):
        if isinstance( self.__title, str ) and self.__title != '':
            return self.__title

    @title.setter
    def title( self, value ):
        if isinstance( value, str ) and value != '':
            self.__title = value

    @property
    def header( self ):
        if isinstance( self.__header, str ) and self.__header != '':
            return self.__header

    @header.setter
    def header( self, value ):
        if isinstance( value, str ) and value != '':
            self.__header = value

    @property
    def size( self ):
        if isinstance( self.__formsize, tuple ) :
            return self.__formsize

    @size.setter
    def size( self, value ):
        if isinstance( value, tuple ) :
            self.__formsize = value

    def __init__( self ):
        super( Sith, self ).__init__( )
        self.__themebackground = Sith( ).themebackground
        self.__themefont = Sith( ).themefont
        self.__icon = Sith( ).iconpath
        self.__elementbackcolor = Sith( ).elementbackcolor
        self.__elementforecolor = Sith( ).elementforecolor
        self.__themetextcolor = Sith( ).textforecolor
        self.__textbackcolor = Sith( ).textbackcolor
        self.__inputbackcolor = Sith( ).inputbackcolor
        self.__inputforecolor = Sith( ).inputforecolor
        self.__buttoncolor = Sith( ).buttoncolor
        self.__formsize = ( 960, 600 )
        self.__image = r'C:\Users\terry\source\repos\BudgetPy\etc\img\BudgetEx.png'

    def show( self ):
        BORDER_COLOR = '#C7D5E0'
        DARK_HEADER_COLOR = '#1B2838'
        BPAD_TOP = ((20,20), (20, 10))
        BPAD_LEFT = ((20,10), (0, 0))
        BPAD_LEFT_INSIDE = (0, (10, 0))
        BPAD_RIGHT = ((10,20), (10, 0))

        top_banner = [
                [sg.Text('Budget Execution', font='Roboto 20', background_color=DARK_HEADER_COLOR, enable_events=True, grab=False), sg.Push(background_color=DARK_HEADER_COLOR),
                 sg.Text('Wednesday 27 Oct 2021', font='Roboto20', background_color=DARK_HEADER_COLOR)],
        ]

        top  = [[sg.Push(), sg.Text('Weather Could Go Here', font='Roboto 20'), sg.Push()],
                [sg.T('This Frame has a relief while the others do not')],
                [sg.T('This window is resizable (see that sizegrip in the bottom right?)')]]

        block_3 = [[sg.Text('Block 3', font='Roboto 20')],
                   [sg.Input(), sg.Text('Some Text')],
                   [sg.T('This frame has element_justification="c"')],
                   [sg.Button('Go'), sg.Button('Exit')]  ]


        block_2 = [[sg.Text('Block 2', font='Roboto 20')],
                   [sg.T('This is some random text')],
                   [sg.Image( source = self.__image, enable_events = True ) ]  ]

        block_4 = [[sg.Text('Block 4', font='Roboto 20')],
                   [sg.T('You can move the window by grabbing this block (and the top banner)')],
                   [sg.T('This block is a Column Element')],
                   [sg.T('The others are all frames')],
                   [sg.T('The Frame Element, with a border_width=0\n    and no title is just like a Column')],
                   [sg.T('Frames that have a fixed size \n    handle element_justification better than Columns')]]


        layout = [
                [sg.Frame('', top_banner,   pad=(0,0), background_color=DARK_HEADER_COLOR,  expand_x=True, border_width=0, grab=True)],
                [sg.Frame('', top, size=(920, 100), pad=BPAD_TOP,  expand_x=True,  relief=sg.RELIEF_GROOVE, border_width=3)],
                [sg.Frame('', [[sg.Frame('', block_2, size=(450,150), pad=BPAD_LEFT_INSIDE, border_width=0, expand_x=True, expand_y=True, )],
                               [sg.Frame('', block_3, size=(450,150),  pad=BPAD_LEFT_INSIDE, border_width=0, expand_x=True, expand_y=True, element_justification='c')]],
                    pad=BPAD_LEFT, background_color=BORDER_COLOR, border_width=0, expand_x=True, expand_y=True),
                 sg.Column(block_4, size=(450, 320), pad=BPAD_RIGHT,  expand_x=True, expand_y=True, grab=True),],[sg.Sizegrip(background_color=BORDER_COLOR)]]

        window = sg.Window('Budget Execution', layout, margins=(0,0), background_color=BORDER_COLOR, no_titlebar=True, resizable=True, right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_LOC_EXIT)

        while True:             # Event Loop
            event, values = window.read()
            print(event, values)
            if event == sg.WIN_CLOSED or event == 'Exit':
                break
            elif event == 'Edit Me':
                sg.execute_editor(__file__)
            elif event == 'Version':
                sg.popup_scrolled(sg.get_versions(), keep_on_top=True)
            elif event == 'File Location':
                sg.popup_scrolled('This Python file is:', __file__)
        window.close()


class ChartPanel( Sith ):
    ''' Provides form with a bar chart '''
    __themebackground = None
    __elementbackcolor = None
    __elementforecolor = None
    __themetextcolor = None
    __textbackcolor = None
    __inputbackcolor = None
    __inputforecolor = None
    __buttoncolor = None
    __icon = None
    __formsize = None
    __themefont = None

    @property
    def header( self ):
        if isin( self.__header, str ) and self.__header != '':
            return self.__header

    @header.setter
    def header( self, value ):
        if isinstance( value, str ) and value != '':
            self.__header = value

    @property
    def size( self ):
        if isinstance( self.__formsize, tuple ) :
            return self.__formsize

    @size.setter
    def size( self, value ):
        if isinstance( value, tuple ) :
            self.__formsize = value

    def __init__( self ):
        super( Sith, self ).__init__()
        self.__themebackground = Sith( ).themebackground
        self.__themefont = Sith( ).themefont
        self.__icon = Sith( ).iconpath
        self.__elementbackcolor = Sith( ).elementbackcolor
        self.__elementforecolor = Sith( ).elementforecolor
        self.__themetextcolor = Sith( ).textforecolor
        self.__textbackcolor = Sith( ).textbackcolor
        self.__inputbackcolor = Sith( ).inputbackcolor
        self.__inputforecolor = Sith( ).inputforecolor
        self.__buttoncolor = Sith( ).buttoncolor
        self.__formsize = ( 700, 600 )

    def show( self ):
        small = ( 10, 1 )
        medium = ( 15, 1 )
        large = ( 20, 1 )
        xlarge = ( 100, 1 )
        barwidth = 50
        barspacing = 75
        edgeoffset = 3
        graphsize = datasize = ( 600, 500 )

        layout = [ [ sg.Text( '', size = small ), sg.Text( '', size = xlarge ) ],
                   [ sg.Text( '', size = small ), sg.Graph( graphsize, ( 0, 0 ), datasize, k='-GRAPH-', pad = 3 ) ],
                   [ sg.Text( '', size = small ), sg.Text( '', size = xlarge ) ],
                   [ sg.Text( '', size = large ), sg.Button( 'Next', size = medium ),
                     sg.Text( '', size = large ), sg.Exit( size = medium ) ] ]

        window = sg.Window( 'Budget Execution', layout,
            finalize = True,
            icon = self.__icon,
            font = self.__themefont,
            size = self.__formsize,
            resizable = True )

        graph = window[ '-GRAPH-' ]

        while True:
            graph.erase( )
            for i in range( 7 ):
                graph_value = random.randint( 0, graphsize[ 1 ] )
                graph.draw_rectangle( top_left = ( i * barspacing + edgeoffset, graph_value ),
                    bottom_right = (i * barspacing + edgeoffset + barwidth, 0 ),
                    fill_color = self.__buttoncolor )

                graph.draw_text( text = graph_value, color = self.__themetextcolor,
                    location = ( i * barspacing + edgeoffset + 25, graph_value + 10 ) )

            event, values = window.read( )
            if event in ( sg.WIN_CLOSED, 'Exit' ):
                break

        window.close( )
