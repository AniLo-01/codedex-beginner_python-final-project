import imageio.v3 as iio
filenames = ['AnimeEyesOpened.', 'AnimeEyesClosed']
images = [ ]
for filename in filenames:
  images.append(iio.imread(filename))
  iio.imwrite('AnimeEyes.gif', images, duration = 350, loop = 0)