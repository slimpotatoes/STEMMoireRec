import userinput
import datastruct
import view

# simple test

filename = 'example\Silicon.dm3'
im = userinput.read_dm3(filename)
view.imview(im.data)


if __name__ == '__main__':
    print('Letss Gooo!!')
