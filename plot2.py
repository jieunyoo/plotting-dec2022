import ROOT
from ROOT import gROOT, gStyle, TFile, TTree, TH1F, TF1, TCanvas, TPaveText, TLegend, TLatex, kBlack, kRed, TColor,TGaxis,kBlue,THStack

infile1 = ROOT.TFile("jets2.root", "READ")
#infile2 = ROOT.TFile("training_trees_pt10To100_chs_94X.root")
#infile3 = ROOT.TFile("training_trees_pt10To100_gen_94X.root")

c = ROOT.TCanvas("c", "c", 800,600)
h1 = infile1.Get("hist1")
h2 = infile1.Get("hist2")
h3 = infile1.Get("hist3")

c=TCanvas("canv")

c.SetLogy()
h2.SetMinimum(1)
h2.Draw()
h1.Draw("same")
h3.Draw("same")


h1.SetLineColor(kBlack)
h2.SetLineColor(kBlue)
h3.SetLineColor(kRed)

h1.SetLineWidth(3)
h2.SetLineWidth(3)
h3.SetLineWidth(3)


#leg = TLegend(.73,.32,.97,.53)
#leg.SetBorderSize(0)
#leg.SetFillColor(0)
#leg.SetFillStyle(0)
#leg.SetTextFont(42)
#leg.SetTextSize(0.035)
#leg.AddEntry(h2,"chs","L")
#leg.AddEntry(h1,"puppi","L")
#leg.AddEntry(h3,"gen","L")
#leg.Draw()

c.SaveAs("plot2.png")
