#!/usr/bin/python2
import ROOT
import os
os.system("clear")
y = ROOT.TF1("lorentz","1.0/(1.0-(x*x/300000**2))",0.,300000.)
y.SetTitle("Lorentz Factor; v(m/s); y")
y.Draw()
proceed = raw_input("Enter ")
