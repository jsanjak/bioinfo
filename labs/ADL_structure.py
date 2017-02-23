import sys
import os
import fnmatch

def makedir(base,sample,experiment):
    home=os.getcwd()
    os.chdir(base)
    if (not os.path.exists(sample)) :
        os.mkdir(sample)
    os.chdir(sample)
    if (not os.path.exists(experiment)):
        os.mkdir(experiment)
    os.chdir(home)
    path = "/".join([base,sample,experiment])
    return(path)

def main():
    experiments = ["DNAseq","ATACseq","RNAseq"]
    home=os.getcwd()
    #DNA seq stuff
    path = "Bioinformatics_Course/"+experiments[0]
    FwdRev = {'1':'F','2':'R'}
    DNA_samples = {"ADL06":"A4","ADL09":"A5","ADL10":"A6","ADL14":"A7"}
    DNA_seqs = fnmatch.filter(os.listdir(path),'ADL*')

    for i in range(len(DNA_seqs)):
        expinfo = DNA_seqs[i].split(".")[0].split("_")
        sample_name = DNA_samples[expinfo[0]]
        fpath = makedir("ADL_data",sample_name,"DNAseq")
        fname = fpath + "/rep."+expinfo[1] + "."+FwdRev[expinfo[2]] + ".fq.gz"
        if ( not os.path.islink(fname)):
            os.symlink(home + "/" +path+"/"+DNA_seqs[i], fname)

    #ATAC seq stuff
    path = "Bioinformatics_Course/"+experiments[1]
    finfo = open(path+"/info.txt","r")
    ATACseq_info = finfo.readlines()
    finfo.close()
    #ATAC_seqs = fnmatch.filter(os.listdir(path),'Sample*')

    for i in range(len(ATACseq_info)-1):
        inf  = ATACseq_info[i+1].split()
        ATAC_seqs = fnmatch.filter(os.listdir(path),'Sample*'+inf[0]+"*.fq.gz")
        fpath = makedir("ADL_data",inf[1],"ATACseq")
        fnameF = fpath + "/"+inf[2]+".rep."+inf[3]+".F.fq.gz"
        fnameR = fpath + "/"+inf[2]+".rep."+inf[3]+".R.fq.gz"
        if ( not os.path.islink(fnameF)):
            os.symlink(home + "/" + path+"/"+ATAC_seqs[0], fnameF)
        if ( not os.path.islink(fnameR)):
            os.symlink(home + "/" + path+"/"+ATAC_seqs[1], fnameR)
    
    #RNA seq stuff
    path = "Bioinformatics_Course/"+experiments[2]
    finfo = open(path+"/RNAseq384_SampleCoding.txt","r")
    RNAseq_info = finfo.readlines()
    finfo.close()
    
    tissues = {"BodyPlate":"Body","HeadPlate":"Head","EmbyroPlate":"Embryo","PupaPlate":"Pupa"}
    home=os.getcwd()
    for i in range(len(RNAseq_info)-1):
        inf = RNAseq_info[i+1].split()
        sample = inf[0]
        plex = inf[1].split("_")[0]
        tiss = tissues[inf[4]]
        samplepath = path + "/RNAseq384plex_flowcell01/Project_" + plex+ "/Sample_" + inf[0] +"/"  
        RNA_seqs = fnmatch.filter(os.listdir(samplepath),"*.fastq.gz")
        #make the directory for the symlinked data
        os.chdir("ADL_data/RNAseq")
        if (not os.path.exists(tiss)):
            os.mkdir(tiss)           
        os.chdir(home)
        fpath = "/".join(["ADL_data/RNAseq",tiss])
        fnameF = fpath + "/Sample"+inf[0]+".RIL." + inf[8] + "."+ inf[3] +  ".F.fq.gz"
        fnameR = fpath + "/Sample"+inf[0]+".RIL." + inf[8] + "."+ inf[3] +  ".R.fq.gz"
        if ( not os.path.islink(fnameF) ):
            os.symlink(home + "/" + samplepath + RNA_seqs[0], fnameR)
        if ( not os.path.islink(fnameR) ):
            os.symlink(home + "/" + samplepath + RNA_seqs[1], fnameF)
 
if __name__ == "__main__":
    main()
