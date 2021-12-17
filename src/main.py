import userinput
import datastruct
import view
import crystal

# simple test

filename = 'example\Silicon.dm3'
im = userinput.read_dm3(filename)
view.imview(im.data)
view.imview_fft(im.data)

userinput.crystal_info(im, 543.1, 543.1, 543.1, 90, 90, 90, 'FCC')
userinput.exp_info(im, 120, [[1, 1, 0], [0, 0, 1], [1, -1, 0]])

crystal.list_reflections(im, 10)

if __name__ == '__main__':
    print('Letss Gooo!!')
