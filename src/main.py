import userinput
import datastruct
import view
import crystal
import moiresim
import moirerec
import numpy as np

# simple test

filename = 'example\Silicon.dm3'
im = userinput.read_dm3(filename)
view.imview(im.data)
view.imview_fft(im.data)

userinput.crystal_info(im, 543.1, 543.1, 543.1, 90, 90, 90, 'FCC')
userinput.exp_info(im, 120, [[1, 1, 0], [0, 0, 1], [1, -1, 0]])

crystal.list_reflections(im, 10)

moiresim.simulate_moire_sampling(im)
view.imview_sim(im)

moire_masked = moirerec.masking_moire_ft(50, 25, im)
view.imview(np.log10(np.abs(moire_masked)), vmin=0)

rec = moirerec.moire_reconstruction(im, 7)
view.imview(np.abs(rec))
view.imview_fft(np.abs(rec), vmin=0)

if __name__ == '__main__':
    print('Letss Gooo!!')
