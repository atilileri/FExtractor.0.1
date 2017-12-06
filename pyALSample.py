# use for lpc, then lsp calculations
"""
LPC plot with DFT, showing two formants (magnitude peaks)
"""

from audiolazy import sHz, sin_table, str2freq, lpc
import pylab

rate = 22050
s, Hz = sHz(rate)
size = 512
table = sin_table.harmonize({1: 1, 2: 5, 3: 3, 4: 2, 6: 9, 8: 1}).normalize()

data = table(str2freq("Bb3") * Hz).take(size)
filt = lpc(data, order=14) # Analysis filter
gain = 1e-2 # Gain just for alignment with DFT

# Plots the synthesis filter
# - If blk is given, plots the block DFT together with the filter
# - If rate is given, shows the frequency range in Hz
(gain / filt).plot(blk=data, rate=rate, samples=1024, unwrap=False)
pylab.ioff()
pylab.show()
