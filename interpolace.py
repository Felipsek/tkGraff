import pylab as lab
import scipy.interpolate as inp

x= [0, 0.3, 0.5, 0.8, 1,  2,  3 ]
y= [0, 0.1, 0.5, 1,   3, 10, 30]

x= "0 0.3 0.5 0.8 1  2  3".split()
y= "0 0.1 0.5 1   3 10 30".split()

x = list(map(float,x))
y = list(map(float,y))

lab.plot(x,y,"ro",label = "puvodní hodnoty")


cunkce = inp.CubicSpline(x,y)
newx= lab.linspace(0, 3, 99)
newy = cunkce(newx)

lab.plot(newx,newy,label = "CubicSpline")


#lab.plot(newx, inp.Akima1DInterpolator(x,y)(newx), label = "Akima1DInterpolator")
#lab.plot(newx, inp.PchipInterpolator(x,y)(newx), label = "PchipInterpolator")
lab.plot(newx, inp.UnivariateSpline(x,y)(newx), label = "UnivariateSpline")


lab.legend()
lab.grid(1)
lab.show()





