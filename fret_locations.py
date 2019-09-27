class ConstructionConsts:
    """
    scale_len -- Length from the nut to the saddle;
                 alternatively: twice length from the nut to the 12th fret
    temperament -- Count of notes per octave.
                   Assumes equal temperament.
    """
    def __init__(self, scale_len, temperament=12):
        self.scale_len = scale_len
        self.temperament = temperament

    """
    Returns the ratio of adjacent frequencies in the octave.
    Derived by:
        f_n = r f_(n-1) = r^n f_0
        f_temperament = 2 f_0
    """
    def freq_ratio(self):
        return 2.0 ** (1.0 / self.temperament)

    """
    Returns the location of the nth fret, measured from the nut.
    Derived by:
        r^n = f_n / f_0
            = ((1/L_n) sqrt(T/rho)) / ((1/L_0) sqrt(T/rho))
            = L_0 / L_n
        where: r is the frequency ratio between notes in the octave
               L_x is the distance from the xth fret and the saddle
               L_0 is the scale length
    """
    def fret_loc(self, n):
        return self.scale_len * (1.0 - 1.0 / (self.freq_ratio() ** n))

    """
    Computes the distance from the nth fret to the previous fret.
    """
    def fret_size(self, n):
        return self.fret_loc(n) - self.fret_loc(n-1)

