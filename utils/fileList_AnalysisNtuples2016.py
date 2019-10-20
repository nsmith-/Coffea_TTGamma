
year = 2016
eosDir ="root://cmseos.fnal.gov//store/user/lpctop/TTGamma_FullRun2/AnalysisNtuples/%i/"%year

fileset2016 = {
    "TTGamma2l_2016":[eosDir+"TTGamma_Dilepton_%i_AnalysisNtuple.root"%year],
    "TTGamma1l_2016":[eosDir+"TTGamma_SingleLept_%i_AnalysisNtuple.root"%year],
    "TTGamma0l_2016":[eosDir+"TTGamma_Hadronic_%i_AnalysisNtuple.root"%year],

    "TTbar2l_2016":[eosDir+"TTbarPowheg_Dilepton_%i_AnalysisNtuple.root"%year],
    "TTbar1l_2016":[eosDir+"TTbarPowheg_Semilept_%i_AnalysisNtuple.root"%year],
    "TTbar0l_2016":[eosDir+"TTbarPowheg_Hadronic_%i_AnalysisNtuple.root"%year],

    "ST_2016":[eosDir+"ST_tW_channel_%i_AnalysisNtuple.root"%year,
          eosDir+"ST_tbarW_channel_%i_AnalysisNtuple.root"%year,
          eosDir+"ST_t_channel_%i_AnalysisNtuple.root"%year,
          eosDir+"ST_s_channel_%i_AnalysisNtuple.root"%year,
          eosDir+"ST_tbar_channel_%i_AnalysisNtuple.root"%year,
          eosDir+"TGJets_%i_AnalysisNtuple.root"%year,
         ],
    "Wjets_2016":[eosDir+"W1jets_%i_AnalysisNtuple.root"%year,
             eosDir+"W2jets_%i_AnalysisNtuple.root"%year,
             eosDir+"W3jets_%i_AnalysisNtuple.root"%year,
             eosDir+"W4jets_%i_AnalysisNtuple.root"%year,
            ],
    "DY_2016":[eosDir+"DYjetsM10to50_%i_AnalysisNtuple.root"%year,
           eosDir+"DYjetsM50_%i_AnalysisNtuple.root"%year,
           ],
    
    "WGamma_2016":[eosDir+"WGamma_01J_5f_%i_AnalysisNtuple.root"%year],
    "ZGamma_2016":[eosDir+"ZGamma_01J_5f_lowMass_%i_AnalysisNtuple.root"%year],

    "Diboson_2016":[eosDir+"WW_%i_AnalysisNtuple.root"%year,
               eosDir+"WZ_%i_AnalysisNtuple.root"%year,
               eosDir+"ZZ_%i_AnalysisNtuple.root"%year,
              ],
    "TTV_2016":[eosDir+"TTWtoLNu_%i_AnalysisNtuple.root"%year,
           eosDir+"TTWtoQQ_%i_AnalysisNtuple.root"%year,
#            eosDir+"TTZtoLL_%i_AnalysisNtuple.root"%year,
          ],
    "QCD_2016":[eosDir+"GJets_HT100To200_%i_AnalysisNtuple.root"%year,
           eosDir+"GJets_HT200To400_%i_AnalysisNtuple.root"%year,
           eosDir+"GJets_HT400To600_%i_AnalysisNtuple.root"%year,
           eosDir+"GJets_HT40To100_%i_AnalysisNtuple.root"%year,
           eosDir+"GJets_HT600ToInf_%i_AnalysisNtuple.root"%year,
           eosDir+"QCD_Pt1000toInf_Mu_%i_AnalysisNtuple.root"%year,
           eosDir+"QCD_Pt120to170_Ele_%i_AnalysisNtuple.root"%year,
           eosDir+"QCD_Pt120to170_Mu_%i_AnalysisNtuple.root"%year,
           eosDir+"QCD_Pt170to300_Ele_%i_AnalysisNtuple.root"%year,
           eosDir+"QCD_Pt170to300_Mu_%i_AnalysisNtuple.root"%year,
           eosDir+"QCD_Pt20to30_Ele_%i_AnalysisNtuple.root"%year,
           eosDir+"QCD_Pt20to30_Mu_%i_AnalysisNtuple.root"%year,
           eosDir+"QCD_Pt300to470_Mu_%i_AnalysisNtuple.root"%year,
           eosDir+"QCD_Pt300toInf_Ele_%i_AnalysisNtuple.root"%year,
           eosDir+"QCD_Pt30to50_Ele_%i_AnalysisNtuple.root"%year,
           eosDir+"QCD_Pt30to50_Mu_%i_AnalysisNtuple.root"%year,
           eosDir+"QCD_Pt470to600_Mu_%i_AnalysisNtuple.root"%year,
           eosDir+"QCD_Pt50to80_Ele_%i_AnalysisNtuple.root"%year,
           eosDir+"QCD_Pt50to80_Mu_%i_AnalysisNtuple.root"%year,
           eosDir+"QCD_Pt600to800_Mu_%i_AnalysisNtuple.root"%year,
           eosDir+"QCD_Pt800to1000_Mu_%i_AnalysisNtuple.root"%year,
           eosDir+"QCD_Pt80to120_Ele_%i_AnalysisNtuple.root"%year,
           eosDir+"QCD_Pt80to120_Mu_%i_AnalysisNtuple.root"%year,
          ],
    
}


fileset_Data2016 = {
    "DataB_Ele_2016":[eosDir+"Data_SingleEle_b_%i_AnalysisNtuple.root"%year],
    "DataC_Ele_2016":[eosDir+"Data_SingleEle_c_%i_AnalysisNtuple.root"%year],
    "DataD_Ele_2016":[eosDir+"Data_SingleEle_d_%i_AnalysisNtuple.root"%year],
    "DataE_Ele_2016":[eosDir+"Data_SingleEle_e_%i_AnalysisNtuple.root"%year],
    "DataF_Ele_2016":[eosDir+"Data_SingleEle_f_%i_AnalysisNtuple.root"%year],
    "DataG_Ele_2016":[eosDir+"Data_SingleEle_g_%i_AnalysisNtuple.root"%year],
    "DataH_Ele_2016":[eosDir+"Data_SingleEle_h_%i_AnalysisNtuple.root"%year],

    "DataB_Mu_2016":[eosDir+"Data_SingleMu_b_%i_AnalysisNtuple.root"%year],
    "DataC_Mu_2016":[eosDir+"Data_SingleMu_c_%i_AnalysisNtuple.root"%year],
    "DataD_Mu_2016":[eosDir+"Data_SingleMu_d_%i_AnalysisNtuple.root"%year],
    "DataE_Mu_2016":[eosDir+"Data_SingleMu_e_%i_AnalysisNtuple.root"%year],
    "DataF_Mu_2016":[eosDir+"Data_SingleMu_f_%i_AnalysisNtuple.root"%year],
    "DataG_Mu_2016":[eosDir+"Data_SingleMu_g_%i_AnalysisNtuple.root"%year],
    "DataH_Mu_2016":[eosDir+"Data_SingleMu_h_%i_AnalysisNtuple.root"%year],

}




filesetTest2016 = {
    "TTGamma2l_2016":[eosDir+"TTGamma_Dilepton_%i_AnalysisNtuple.root"%year],
    "TTGamma1l_2016":[eosDir+"TTGamma_SingleLept_%i_AnalysisNtuple.root"%year],
    "TTGamma0l_2016":[eosDir+"TTGamma_Hadronic_%i_AnalysisNtuple.root"%year],
}
