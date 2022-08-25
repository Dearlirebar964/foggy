from dataclasses import dataclass, asdict
# #####################################

@dataclass
class CacheSize:
    disk:   int = 0
    ram:    int = 0
    # #####################################

    def __add__(self, other):
        return CacheSize(
            self.disk + other.disk,
            self.ram + other.ram
        )
    # #####################################
    
    def __str__(self) -> str:
        return ', '.join([
            '%s: %s' % (n, humanized(v))
            for n, v in asdict(self).items()
        ])
    # #####################################


def humanized(v: int, base: int=1024, suffix='o') -> str:
    units = ['', 'k', 'M', 'G', 'T']
    for unit in units:
        if v < base: break
        v /= base
    return '%.1f%s%s' % (v, unit, suffix)
# #####################################
