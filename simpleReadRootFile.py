import ROOT
from ROOT import gROOT, gStyle, TFile, TTree, TH1F, TF1, TCanvas, TPaveText, TLegend, TLatex, kBlack, kRed, TColor,TGaxis,kBlue,THStack

infile1 = ROOT.TFile("new-file.root")

tree1 = infile1.Get("Events")
print('tree1', tree1)

hist1 = ROOT.TH1F("hist1", "pt", 20,0,500)

for entry in tree1:

#for entry in range(tree1.GetEntries()):
        #myentry = tree1.GetEntry(entry)
   #print(entry)

   print(entry.lepton_pT)
   hist1.Fill(entry.lepton_pT)

canvas1 = ROOT.TCanvas("canvas1", "c1", 800, 600)
hist1.GetXaxis().SetTitle("pt (GeV)")
hist1.GetYaxis().SetTitle("no. events")
hist1.Draw()
canvas1.SaveAs('pt.png')
