from ROOT import TCanvas, TFile, TProfile, TNtuple, TH1F, TH2F, TChain
from ROOT import gROOT, gBenchmark, gRandom, gSystem, Double
import sys
from AngryTops.features import *

def draw_contour(attribute_name, treename='fitted.root', dir=training_dir):
    # Create a new canvas, and customize it.
    #c1 = TCanvas( 'c1', 'Contour Plot for ', attribute_name, 200, 10, 700, 500 )
    c1 = TCanvas()
    c1.SetFillColor( 42 )
    c1.GetFrame().SetFillColor( 21 )
    c1.GetFrame().SetBorderSize( 6 )
    c1.GetFrame().SetBorderMode( -1 )

    # Open tree
    ttree = TChain('nominal', 'nominal')
    ttree.AddFile("{0}/{1}".format(dir, treename))

    # Draw and save contour plot
    ttree.Draw("{0}_true:{0}_fitted".format(attribute_name), "", "colz")
    c1.SaveAs("{0}/ContourPlots/{1}.jpg".format(dir, attribute_name))

if __name__=="__main__":
    for att in attributes:
        draw_contour(att, treename='fitted.root', dir=sys.argv[1])
