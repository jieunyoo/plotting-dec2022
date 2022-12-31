void getHistos(){

//PUPPI
TFile *_file0 = TFile::Open("tmva_output_Pt10To100_Eta0p0To2p5_puppi.root");
TH1F* hist0;
hist0 = (TH1F*)_file0->Get("BDT_chs_94X/Method_BDT/BDT/MVA_BDT_rejBvsS");



//CHS
TFile *_file1 = TFile::Open("tmva_output_Pt10To100_Eta0p0To2p5_chs.root");
TH1F* hist1;
hist1 = (TH1F*)_file1->Get("BDT_chs_94X/Method_BDT/BDT/MVA_BDT_rejBvsS");


TCanvas* c1 = new TCanvas();

hist0->SetLineColor(kBlue);
hist1->SetLineColor(kRed);
hist0->SetStats(0);
hist1->SetStats(1);

hist0->SetLineWidth(2);
hist1->SetLineWidth(2);

hist0->Draw();
hist1->Draw("same");

TLegend *leg = new TLegend(0.25,0.20,0.40,0.4);
leg->AddEntry(hist0, "puppi");
leg->AddEntry(hist1, "chs");
leg->SetTextSize(0.030);
leg->Draw();

c1->SaveAs("firstBin.png");

}
