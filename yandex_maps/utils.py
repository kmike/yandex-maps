from yandex_maps.api import geocode, get_map_url

import warnings
msg = 'yandex_maps.utils is deprecated. Import from yandex_maps.api instead.'
warnings.warn(msg, DeprecationWarning, stacklevel=2)
