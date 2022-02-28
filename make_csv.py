import random
import os


src = 'slt'
trg = 'rms'


head = f'https://github.com/pengyuk/pengyuk.github.io/tree/main/{language}'

files = os.listdir('D://0_research/2019_spring/amt_ceting/audio_git/mos2/%s-to-%s/dnn'%(src, trg))
files = [fn.split('.')[0].split('-')[1] for fn in files]
systems = ['cyclegan','dnn','vcc2018','seq2seqvc', 'proposed']

def _get_fn(ind, type):
    if type=='cyclegan':
        return 'cyclegan-' + ind + '.wav'
    elif type=='dnn':
        return 'dnn-' + ind + '.wav'
    elif type=='proposed':
        return 'Wav_arctic_' + ind + '_ref_%s_VC.wav'%trg
    elif type=='vcc2018':
        return 'vcc2018-' + ind + '.wav'
    elif type=='seq2seqvc':
        return 'seq2seqvc-' + ind + '.wav'
    else:
        raise ValueError


with open('MOS_slt2rms.csv','w') as fp:
    for i in range(100):
        if i == 0:
            titles = 'link1'
        else:
            titles += ',link%d'%(i+1)
    fp.write(titles+'\n')
    for i in range(5): #5 hits
        line = ''
        for filename in files:
            random.shuffle(systems)
            for sys in systems:
                line += head+sys+'/'+_get_fn(filename,sys) +','
        line = line[:-1]
        fp.write(line+'\n')