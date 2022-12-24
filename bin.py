import ROOT
from ROOT import gROOT, gStyle, TFile, TTree, TH1F, TF1, TCanvas, TPaveText, TLegend, TLatex, kBlack, kRed, TColor,TGaxis,kBlue,THStack
from ROOT import TH1F, TF1, TGraphAsymmErrors
import math

infile1 = ROOT.TFile("file.root", "READ")

c = ROOT.TCanvas("c", "c", 800,600)
h2 = infile1.Get("h2")
h2.Draw()
c.Print("hist.pdf")

#h2 has 100 bins from -1 to 1

print('minimum', h2.GetMinimumBin())
print('maximum bin', h2.GetMaximumBin())
print('get nbinsX', h2.GetNbinsX())

print('h2.Integral(0,-1)', h2.Integral(0,-1))

print('h2.Integral(3,-1)', h2.Integral(3,-1))


print('h2.Integral(60,100)', h2.Integral(60,100))

print('h2.Integral(0,100)', h2.Integral(0,100))
print('h2.Integral(0,101)', h2.Integral(0,101))

print('h2.Integral(0,100,0.2)', h2.Integral(0,100,"width"))


print('h2.GetBinContent(1)', h2.GetBinContent(1))

print('h2.GetBinContent(0)', h2.GetBinContent(0))

print('h2.getBinWidth(1)', h2.GetBinWidth(1))
print('h2.getBinWidth(2)', h2.GetBinWidth(2))

print('h2.GetNdivisions', h2.GetNdivisions())

binmax = h2.GetMaximumBin()
x = h2.GetXaxis().GetBinCenter(binmax);
print('binmax, x', binmax, x)

y = h2.GetXaxis().GetBinCenter(60);
print('y', y)

#print('h2.Integral("width")', h2.Integral("width")

#      For all histogram types: nbins, xlow, xup
#        bin = 0;       underflow bin
#        bin = 1;       first bin with low-edge xlow INCLUDED
#        bin = nbins;   last bin with upper-edge xup EXCLUDED
#        bin = nbins+1; overflow bin
