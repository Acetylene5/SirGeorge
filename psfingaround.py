import scipy
import numpy
import matplotlib.pyplot as pyplot

#Sets up the figure object
fig = pyplot.figure(0)
fig.clear()

#Creates the subplots
ax1 = fig.add_axes([0.1, 0.5, 0.4, 0.4])
ax2 = fig.add_axes([0.5, 0.5, 0.4, 0.4])
ax3 = fig.add_axes([0.1, 0.1, 0.4, 0.4])
ax4 = fig.add_axes([0.5, 0.1, 0.4, 0.4])

#Generates the pupil illumination
pupil = numpy.zeros([1000, 1000], dtype=numpy.float)

#Center coordinates of the pupil
ycent = 500
xcent = 500

beam_radius = 20

#Creates a top-hat beam profile
for x in range(1000):
    for y in range(1000):
        if ((x - xcent)**2.0 + (y - ycent)**2.0) < beam_radius**2.0:
            pupil[x][y] = 1.0

#Plots the beam in axis 1
im1 = ax1.imshow(pupil)
#cb1 = fig.colorbar(im1)

#Plots the profile of the beam in axis 2
ax2.plot(pupil[500])


freq = numpy.fft.fft2(pupil)
freq_star = numpy.conj(freq)

#Calculates the logarithm of the absolute value of the square of 2-D FFT of the pupil
#psf = numpy.log10(numpy.sqrt((freq*freq_star)*(freq*freq_star)))
psf = numpy.log10(numpy.abs(freq*freq_star))
#psf = numpy.abs(freq*freq_star)

#Plots the psf in axis 3
im3= ax3.imshow(numpy.fft.fftshift(psf))
#cb3 = fig.colorbar(im3)

#Plots the collapsed profile of the Psf in axis 4
ax4.plot(numpy.fft.fftshift(psf)[500])

fig.show()
fig.savefig("PSF_tester.png")
