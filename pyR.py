import ROOT
h = ROOT.TH1F("Random stuff","Random;X;# of entries",100,-5,5)
h.FillRandom("gaus")
h.Draw()
proceed = raw_input()
