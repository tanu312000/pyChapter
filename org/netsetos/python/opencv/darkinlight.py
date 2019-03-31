import rawpy, imageio
raw = rawpy.imread('/home/tanu/Downloads/1_4O40J3bf3mpVZiRNu-H3-w.png')
raw = raw.postprocess()
imageio.imsave('image.png',raw)