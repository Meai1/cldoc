# This file is part of cldoc.  cldoc is free software: you can
# redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, version 2.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 51
# Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
import os, subprocess

devnull = open(os.devnull)
p = subprocess.Popen(['clang++', '-E', '-xc++', '-v', '-'],
                     stdin=devnull,
                     stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE)
devnull.close()

lines = p.communicate()[1].splitlines()
init = False
paths = []

for line in lines:
    if line.startswith('#include <...>'):
        init = True
    elif line.startswith('End of search list.'):
        init = False
    elif init:
        paths.append(line.strip())

flags = ['-I{0}'.format(x) for x in paths]

__all__ = ['flags']
