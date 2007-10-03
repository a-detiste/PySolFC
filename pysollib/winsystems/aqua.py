##---------------------------------------------------------------------------##
##
## PySol -- a Python Solitaire game
##
## This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program; see the file COPYING.
## If not, write to the Free Software Foundation, Inc.,
## 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
##
##---------------------------------------------------------------------------##

import sys, os
import Tkinter

from pysollib.settings import TOOLKIT, USE_TILE
from pysollib.tile import Tile
from pysollib.macosx.appSupport import hideTkConsole

from common import base_init_root_window, BaseTkSettings


def init_root_window(root, app):
    base_init_root_window(root, app)
    if TOOLKIT == 'tk':
        hideTkConsole(root)
    if TOOLKIT == 'gtk':
        pass
    elif USE_TILE:
        style = Tile.Style(root)
        color = style.lookup('.', 'background')
        if color:
            root.tk_setPalette(color)   # for non-Tile widgets

        if app.opt.tile_theme == 'aqua':
            # standard Tk scrollbars work on OS X, but Tile ones look weird
            Tile.Scrollbar = Tkinter.Scrollbar

    else:                               # pure Tk
        #root.option_add(...)
        pass


class TkSettings(BaseTkSettings):
    pass

