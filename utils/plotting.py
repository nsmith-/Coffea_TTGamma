import matplotlib.pyplot as plt
from cycler import cycler
from coffea import hist

def plotWithRatio(h, hData, overlay, invertStack=True, lumi=35.9, label="CMS Preliminary",colors=None,ratio=[0.5,1.5], xRange=None, yRange=None, logY=False,extraText = None):

    # make a nice ratio plot
    plt.rcParams.update({
        'font.size': 14,
        'axes.titlesize': 18,
        'axes.labelsize': 18,
        'xtick.labelsize': 12,
        'ytick.labelsize': 12
    })
    if not hData is None:
        fig, (ax, rax) = plt.subplots(2, 1, figsize=(7,7), gridspec_kw={"height_ratios": (3, 1)}, sharex=True)
        fig.subplots_adjust(hspace=.07)
    else:
        fig, ax = plt.subplots(1, 1, figsize=(7,7))#, gridspec_kw={"height_ratios": (3, 1)}, sharex=True)

    # Here is an example of setting up a color cycler to color the various fill patches
    # http://colorbrewer2.org/#type=qualitative&scheme=Paired&n=6
    from cycler import cycler
    if colors is None:
        colors = ['#a6cee3','#1f78b4','#b2df8a','#33a02c','#fb9a99','#e31a1c','#fdbf6f','#ff7f00','#cab2d6','#6a3d9a','#ffff99','#b15928']
#        colors = ['#a6cee3','#1f78b4','#b2df8a','#33a02c','#fb9a99','#e31a1c','#fdbf6f','#ff7f00','#cab2d6','#6a3d9a']
    if invertStack: 
        _n = len(h.identifiers(overlay))-1
        colors = colors[_n::-1]
    ax.set_prop_cycle(cycler(color=colors))

    fill_opts = {
        'edgecolor': (0,0,0,0.3),
        'alpha': 0.8
    }
    error_opts = {
        'label':'Stat. Unc.',
        'hatch':'///',
        'facecolor':'none',
        'edgecolor':(0,0,0,.5),
        'linewidth': 0
    }
    data_err_opts = {
        'linestyle':'none',
        'marker': '.',
        'markersize': 10.,
        'color':'k',
        'elinewidth': 1,
        'emarker': '_'
    }

    if invertStack:
        h._axes[0]._sorted.reverse()
    hist.plot1d(h,
                overlay=overlay,
#                 invertStack=True,
                ax=ax,
                clear=False,
                stack=True,
                line_opts=None,
                fill_opts=fill_opts,
                error_opts=error_opts
               )
    if invertStack:
        h._axes[0]._sorted.reverse()

    if not hData is None:
        hist.plot1d(hData,
                    overlay=overlay,
                    ax=ax,
                    clear=False,
                    error_opts=data_err_opts
                   )

    ax.autoscale(axis='x', tight=True)
    ax.set_ylim(0, None)
    ax.set_xlabel(None)
    if invertStack:
        handles, labels = ax.get_legend_handles_labels()
        if hData is None:
            handles = handles[-2::-1]+handles[-1:-2:-1]
            labels = labels[-2::-1]+labels[-1:-2:-1]            
        else:
            handles = handles[-1:-2:-1] +handles[-3::-1]+handles[-2:-3:-1]
            labels = labels[-1:-2:-1] +labels[-3::-1]+labels[-2:-3:-1]
        ax.legend(handles, labels,bbox_to_anchor=(1., 1.),loc='upper left')
    else:
        leg = ax.legend(loc='upper right')
        ax.legend(bbox_to_anchor=(1., 1.))

    
    
    if not hData is None:
        hist.plotratio(hData.sum(overlay), h.sum(overlay),
                       ax=rax,
                       error_opts=data_err_opts,
                       denom_fill_opts={},
                       guide_opts={},
                       unc='num'
                      )
        rax.set_ylabel('Ratio')
        rax.set_ylim(ratio[0],ratio[1])

    
    if logY:
        ax.set_yscale("log")
        ax.set_ylim(1,ax.get_ylim()[1]*5)        

    if not xRange is None:
        ax.set_xlim(xRange[0],xRange[1])
    if not yRange is None:
        ax.set_ylim(yRange[0],yRange[1])

    CMS = plt.text(0., 1., r"$\bf{CMS}$ Preliminary",
                    fontsize=16,
                    horizontalalignment='left',
                    verticalalignment='bottom',
                    transform=ax.transAxes
                   )

    if not extraText is None:
        
        extraLabel = plt.text(0.02, .99, extraText,
                        fontsize=16,
                        horizontalalignment='left',
                        verticalalignment='top',
                        transform=ax.transAxes
                       )
        ax.set_ylim(0,ax.get_ylim()[1]*1.1)
    
    lumi = plt.text(1., 1., r"%.1f fb$^{-1}$ (13 TeV)"%(lumi),
                    fontsize=16,
                    horizontalalignment='right',
                    verticalalignment='bottom',
                    transform=ax.transAxes
                   )

