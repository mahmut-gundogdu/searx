'''
searx is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

searx is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with searx. If not, see < http://www.gnu.org/licenses/ >.

(C) 2015 by Adam Tauber, <asciimoo@gmail.com>
'''

from flask_babel import gettext
import re
from searx.url_utils import urlunparse, parse_qsl, urlencode
import requests

name = gettext('Block some domains')
description = gettext('This plugins block some domains from result. This domains list int blocked_domains.txt')
default_on = True
preference_section = 'privacy'
textFile = open('searx/plugins/blocked_domains.txt', 'r')
blocked_domain_list = textFile.read().splitlines()

def on_result(request, search, result):
    if 'parsed_url' not in result:
        return True

    result['template'] = 'blocked_domains.html'
    domain = result['parsed_url'].netloc

    is_blocked = False
    for line in blocked_domain_list:
        if re.search(line,domain) != None :
            is_blocked = True
            break

    result['is_blocked'] = is_blocked
    return True