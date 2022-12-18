import ROOT
from ROOT import gROOT, gStyle, TFile, TTree, TH1F, TF1, TCanvas, TPaveText, TLegend, TLatex, kBlack, kRed, TColor,TGaxis,kBlue,THStack
from ROOT import TH1F, TF1, TGraphAsymmErrors
import math

infile1 = ROOT.TFile("new-file.root")
tree1 = infile1.Get("Events")

infile2 = ROOT.TFile("new-fileTrigger.root")
tree2 = infile2.Get("Events")

hist1 = ROOT.TH1F("hist1", "pt", 20,0,500)
hist2 = ROOT.TH1F("hist2", "pt", 20,0,500)
heff = TH1F( "heff", "Efficiency;Jet p_{T} (GeV);Efficiency", 100, 0, 1000 )
heff.SetMinimum(0)
heff.SetMaximum(1.2)
heff.SetStats(0)

for entry in tree1:
   hist1.Fill(entry.lepton_pT)
   print(entry.lepton_pT)


for entry in tree2:
   hist2.Fill(entry.lepton_pT)
   print(entry.lepton_pT)


gEff = TGraphAsymmErrors()
gEff.Divide(hist2, hist1)
gEff.SetMarkerStyle( 20 )
gEff.SetMarkerSize( 1.0 )

c = TCanvas("Eff")
c.cd()
heff.DrawCopy()

gEff.Draw("p")

c.Modified()
c.Update()
c.SaveAs('Eff.png')
