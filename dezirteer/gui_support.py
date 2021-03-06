# -*- coding: utf-8 -*-
from math import *
#import sys
import ctypes
try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

from const import *

class NoGrainsError(Exception):
    pass

#class containing settings to be applied to graph
class GraphSettings(object):
    def __init__(self, show_multiple=False, conc_type=0, eclipses_at=1, fit_disc=False,
                 anchored=False, pdp_kde_hist=0, do_hist=False, bandwidth=50, binwidth=50, keep_previous=False):
        self.__show_multiple = show_multiple
        self.__conc_type = conc_type
        self.__eclipses_at = eclipses_at
        self.__fit_disc = fit_disc
        self.__anchored = anchored
        self.__pdp_kde_hist = pdp_kde_hist
        self.__do_hist = do_hist
        self.__bandwidth = bandwidth
        self.__binwidth = binwidth
        self.__keep_previous = keep_previous

    @property
    def show_multiple(self):
        return self.__show_multiple

    @show_multiple.setter
    def show_multiple(self, value):
        self.__show_multiple = value

    @property
    def conc_type(self):
        return self.__conc_type

    @conc_type.setter
    def conc_type(self, value):
        self.__conc_type = value

    @property
    def eclipses_at(self):
        return self.__eclipses_at

    @eclipses_at.setter
    def eclipses_at(self, value):
        self.__eclipses_at = value

    @property
    def fit_disc(self):
        return self.__fit_disc

    @fit_disc.setter
    def fit_disc(self, value):
        self.__fit_disc = value

    @property
    def anchored(self):
        return self.__anchored

    @anchored.setter
    def anchored(self, value):
        self.__anchored = value

    @property
    def pdp_kde_hist(self):
        return self.__pdp_kde_hist

    @pdp_kde_hist.setter
    def pdp_kde_hist(self, value):
        self.__pdp_kde_hist = value

    @property
    def do_hist(self):
        return self.__do_hist

    @do_hist.setter
    def do_hist(self, value):
        self.__do_hist = value

    @property
    def bandwidth(self):
        return self.__bandwidth

    @bandwidth.setter
    def bandwidth(self, value):
        self.__bandwidth = value

    @property
    def binwidth(self):
        return self.__binwidth

    @binwidth.setter
    def binwidth(self, value):
        self.__binwidth = value

    @property
    def keep_previous(self):
        return self.__keep_previous

    @keep_previous.setter
    def keep_previous(self, value):
        self.__keep_previous = value


def onChange(p_number_in_list, p_value, pars, *args, **kwargs):
    #'''p_filters, p_table, p_grainset, p_colnames''' p_table, p_grainset, p_filters, p_colnames
    if p_number_in_list == 1:
        pars[0].show_multiple = p_value
    elif p_number_in_list == 2:
        pars[0].filter_by_uconc[0] = p_value
        if p_value == True:
            args[0].configure(state=NORMAL)
        else:
            args[0].configure(state=DISABLED)
    elif p_number_in_list == 3:
        pars[0].which_age[0] = p_value
        if p_value == 1:
            args[0].configure(state=NORMAL)
        else:
            args[0].configure(state=DISABLED)
    elif p_number_in_list == 4:
        pars[0].use_pbc = p_value
    elif p_number_in_list == 5:
        pars[0].filter_by_err[0] = p_value
        if p_value == True:
            args[0].configure(state=NORMAL)
            args[1].configure(state=NORMAL)
        else:
            args[0].configure(state=DISABLED)
            args[1].configure(state=DISABLED)
    elif p_number_in_list == 6:
        pars[0].pos_disc_filter = p_value/100
    elif p_number_in_list == 7:
        pars[0].neg_disc_filter = p_value/100
    elif p_number_in_list == 8:
        pars[0].disc_type = [p_value, args[0].get()]
        if p_value == 1:
            args[0].configure(state=NORMAL)
        else:
            args[0].configure(state=DISABLED)
    elif p_number_in_list == 9:
        pars[0].conc_type = p_value
    elif p_number_in_list == 11:
        pars[0].fit_disc = p_value
    elif p_number_in_list == 12:
        pars[0].anchored = p_value
    elif p_number_in_list == 13:
        pars[0].do_pdp = p_value
    elif p_number_in_list == 14:
        pars[0].do_kde = p_value
    elif p_number_in_list == 15:
        pars[0].do_cpdp = p_value
    elif p_number_in_list == 16:
        pars[0].do_ckde = p_value
    elif p_number_in_list == 17:
        pars[0].do_hist = p_value
    elif p_number_in_list == 18:
        pars[0].filter_by_uconc[1] = p_value
    elif p_number_in_list == 19:
        pars[0].which_age[1] = p_value
    elif p_number_in_list == 20:
        pars[0].filter_by_err[1] = p_value/100
    elif p_number_in_list == 21:
       if varDiscLinked2Age.get() == 1:
           args[4].set(args[5].get()) #set the slider
           args[varAgebased.get()].select()
           for i in range(0, len(args)): #disable all controls
               args[i].configure(state=DISABLED)
       elif varDiscLinked2Age.get() == 0:
           for i in args:
            i.configure(state=NORMAL)
    elif p_number_in_list == 22:
        pars[0].include207235Err = p_value
    elif p_number_in_list == 23:
        pars[0].unc_type = p_value
    elif p_number_in_list == 24:
        pars[0].filter_by_commPb = p_value
    elif p_number_in_list == 25:
        pars[0].disc_type[1] = p_value

    elif p_number_in_list == 26:
        if varMinAgeCrop.get() == 0: #12345
            pars[0].minAgeCrop = 0
            args[0].configure(state=DISABLED)
        else:
            args[0].configure(state=NORMAL)
            try:
                pars[0].minAgeCrop = float(p_value)
            except ValueError:
                pars[0].minAgeCrop = 0
                args[0].insert(0, '0')


    elif p_number_in_list == 27:
        if varMaxAgeCrop.get() == 0:
            pars[0].maxAgeCrop = EarthAge
            args[0].configure(state=DISABLED)
        else:
            args[0].configure(state=NORMAL)
            try:
                pars[0].maxAgeCrop = float(p_value)
            except ValueError:
                pars[0].maxAgeCrop = 0
                args[0].insert(0, EarthAge)



    sys.stdout.flush()
    fill_data_table(pars[1], pars[2], pars[0], pars[3])
#'''p_filters, p_table, p_grainset, p_colnames''' p_table, p_grainset, p_filters, p_colnames


def onGraphChange(p_graph_settings, p_number_in_list, p_value, *args, **kwargs):
    if p_number_in_list == 0:
        p_graph_settings.conc_type = p_value
    elif p_number_in_list == 1:
        p_graph_settings.conc_type = p_value
    elif p_number_in_list == 2:
        p_graph_settings.eclipses_at = p_value
    elif p_number_in_list == 7:
        p_graph_settings.pdp_kde_hist = p_value
    elif p_number_in_list == 8:
        p_graph_settings.pdp_kde_hist = p_value
    elif p_number_in_list == 11:
        p_graph_settings.bandwidth = p_value
    elif p_number_in_list == 12:
        p_graph_settings.binwidth = p_value
    elif p_number_in_list == 13:
        if p_value.get() == 1:
            args[0].deselect()
    sys.stdout.flush()

def TableOnDoubleClick(event):
    #item = p_table.selection()[0]
    print("you clicked on")#, p_table.item(item, "text"))


#sets form variables
def set_Tk_var():
    global varUConc, varAgebased, varUncorrOrPbc, varErrFilter, varDiscType, varConcType, varEclipseSigma
    global varShowMultiple, varDrawKde, varPosDiscFilter, varNegDiscFilter, varFitDiscordia, varDrawPDP
    global varDrawKDE, varDrawCPDP, varDrawCKDE, varDrawHist, var_pdp_kde_hist, varAnchored, varDiscLinked2Age
    global varKeepPrev, varTypePbc, varShowCalc, varInclude207235Err, varLimitAgeSpectrum, varUncType
    global varCommPb, varMinAgeCrop, varMaxAgeCrop
    varUConc = IntVar()
    varDiscType = IntVar()
    varConcType = IntVar()
    varConcType.set(0)
    varEclipseSigma = IntVar()
    varAgebased = IntVar()
    varUncorrOrPbc = IntVar()
    varErrFilter = IntVar()
    varShowMultiple = IntVar()
    varDrawKde = IntVar()
    varPosDiscFilter = IntVar()
    varNegDiscFilter = IntVar()
    varFitDiscordia = IntVar()
    varDrawPDP = IntVar()
    varDrawKDE = IntVar()
    varDrawCPDP = IntVar()
    varDrawCKDE = IntVar()
    varDrawHist = IntVar()
    var_pdp_kde_hist = IntVar()
    varAnchored = IntVar()
    varDiscLinked2Age = IntVar()
    varDiscLinked2Age.set(1)
    varKeepPrev = IntVar()
    varKeepPrev.set(0)
    varTypePbc = IntVar()
    varShowCalc = IntVar()
    varInclude207235Err = IntVar()
    varLimitAgeSpectrum = IntVar()
    varUncType = IntVar()
    varCommPb = IntVar()
    varMinAgeCrop = IntVar()
    varMaxAgeCrop = IntVar()


def init(pTop, pGui, *args, **kwargs):
    global w, top_level, root
    w = pGui
    top_level = pTop
    root = pTop


def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None


def export_table(p_grainset, p_filters, p_colnames, p_graph_settings, p_filename, p_probcum_filename):
    try:
        file = p_filename
        i = 0
        j = 0
        unc_type = int(p_filters.unc_type)
        an_list = p_grainset.analyses_list
        p_grainset.good_bad_sets(p_filters)
        file.write("Analysis name"+',')
        while i < len(p_colnames):
            file.write(p_colnames[i]+',')
            i += 1
        file.write("\n")
        while j < len(p_grainset):
            '''name = str(an_list[j])
            
            rat208232 = str(an_list[j].pb208_th232[0])
            errRat208232Int = str(an_list[j].pb208_th232[1])
            errRat208232Prop = str(an_list[j].pb208_th232[2])

            rat207206 = str(an_list[j].pb207_pb206[0])
            errRat207206Int = str(an_list[j].pb207_pb206[1])
            errRat207206Prop = str(an_list[j].pb207_pb206[2])
            
            rat207235 = str(an_list[j].pb207_u235[0])
            errRat207235Int = str(an_list[j].pb207_u235[1])
            errRat207235Prop = str(an_list[j].pb207_u235[2])

            rat206238 = str(an_list[j].pb206_u238[0])
            errRat206238Int = str(an_list[j].pb206_u238[1])
            errRat206238Prop = str(an_list[j].pb206_u238[2])

            corr_coef_75_68 = str(an_list[j].corr_coef_75_68)
            corr_coef_86_76 = str(an_list[j].corr_coef_86_76)

            u_conc =  str(an_list[j].u_conc[0])
            errU_concInt= str(an_list[j].u_conc[1])
            errU_concProp = str(an_list[j].u_conc[2])
            
            pbc = str(an_list[j].pbc[0])
            errPbcInt = str(an_list[j].pbc[1])
            errPbcProp = str(an_list[j].pbc[2])
            
            rat206_204 = str(an_list[j].pb206_pb204[0])
            errRat206_204Int = str(an_list[j].pb206_pb204[1])
            errRat206_204 = str(an_list[j].pb206_pb204[2])

            rat207_204 = str(an_list[j].pb207_pb204[0])
            errRat207_204Int = str(an_list[j].pb207_pb204[1])
            errRat207_204Prop = str(an_list[j].pb207_pb204[2])

            rat208_204 = str(an_list[j].pb208_pb204[0])
            errRat208_204Int = str(an_list[j].pb208_pb204[1])
            errRat208_204Prop = str(an_list[j].pb208_pb204[2])

            rat232_204 = str(an_list[j].th232_pb204[0])
            errRat232_204Int = str(an_list[j].th232_pb204[1])
            errRat232_204Prop = str(an_list[j].th232_pb204[2])

            rat238_204 = str(an_list[j].u238_pb204[0])
            errRat238_204Int = str(an_list[j].u238_pb204[1])
            errRat238_204Prop = str(an_list[j].u238_pb204[2])
            
            age208_232 = str(an_list[j].calc_age(2, int_prop)[0])
            errAge208_232Int = age208_232 = str(an_list[j].calc_age(2, int_prop)[1])
            errAge208_232Prop =age208_232 = str(an_list[j].calc_age(2, int_prop)[2])'''

            l_str = ('\n' +
                       str(an_list[j]) + ',' +
                       str(an_list[j].pb208_th232[0]) + ',' +
                       str(an_list[j].pb208_th232[1]) + ',' +
                       str(an_list[j].pb208_th232[2]) + ',' +

                       str(an_list[j].pb207_pb206[0]) + ',' +
                       str(an_list[j].pb207_pb206[1]) + ',' +
                       str(an_list[j].pb207_pb206[2]) + ',' +

                       str(an_list[j].pb207_u235[0]) + ',' +
                       str(an_list[j].pb207_u235[1]) + ',' +
                       str(an_list[j].pb207_u235[2]) + ',' +

                       str(an_list[j].pb206_u238[0]) + ',' +
                       str(an_list[j].pb206_u238[1]) + ',' +
                       str(an_list[j].pb206_u238[2]) + ',' +

                       str(an_list[j].corr_coef_75_68) + ',' +
                       str(an_list[j].corr_coef_86_76) + ',' +

                       str(an_list[j].u_conc[0]) + ',' +
                       str(an_list[j].u_conc[1]) + ',' +
                       str(an_list[j].u_conc[2]) + ',' +

                       str(an_list[j].pbc[0]) + ',' +
                       str(an_list[j].pbc[1]) + ',' +
                       str(an_list[j].pbc[2]) + ',' +

                       str(an_list[j].pb206_pb204[0]) + ',' +
                       str(an_list[j].pb206_pb204[1]) + ',' +
                       str(an_list[j].pb206_pb204[2]) + ',' +

                       str(an_list[j].pb207_pb204[0]) + ',' +
                       str(an_list[j].pb207_pb204[1]) + ',' +
                       str(an_list[j].pb207_pb204[2]) + ',' +

                       str(an_list[j].pb208_pb204[0]) + ',' +
                       str(an_list[j].pb208_pb204[1]) + ',' +
                       str(an_list[j].pb208_pb204[2]) + ',' +

                       str(an_list[j].th232_pb204[0]) + ',' +
                       str(an_list[j].th232_pb204[1]) + ',' +
                       str(an_list[j].th232_pb204[2]) + ',' +

                       str(an_list[j].u238_pb204[0]) + ',' +
                       str(an_list[j].u238_pb204[1]) + ',' +
                       str(an_list[j].u238_pb204[2]) + ',' +

                       str(an_list[j].calc_age(2)[0]) + ',' +
                       str(an_list[j].calc_age(2)[1]) + ',' +
                       str(an_list[j].calc_age(2)[2]) + ',' +

                       str(an_list[j].calc_age(3)[0]) + ',' +
                       str(an_list[j].calc_age(3)[1]) + ',' +
                       str(an_list[j].calc_age(3)[2]) + ',' +

                       str(an_list[j].calc_age(1)[0]) + ',' +
                       str(an_list[j].calc_age(1)[1]) + ',' +
                       str(an_list[j].calc_age(1)[2]) + ',' +

                       str(an_list[j].calc_age(0)[0]) + ',' +
                       str(an_list[j].calc_age(0)[1]) + ',' +
                       str(an_list[j].calc_age(0)[2]) + ',' +

                       str(an_list[j].calc_discordance(2, p_filters.disc_type[1])) + ',' +
                       str(an_list[j].calc_discordance(3, p_filters.disc_type[1])) + ',' +

                       str(an_list[j].is_grain_good(p_filters)[0]) + ',' +
                       str(an_list[j].is_grain_good(p_filters)[1]) + ',' +

                       str(an_list[j].calc_age(an_list[j].is_grain_good(p_filters)[1])[0]) + ',' +
                       str(an_list[j].calc_age(an_list[j].is_grain_good(p_filters)[1])[unc_type]))
            file.write(l_str)
            j += 1
        file.write("\n" * 2)

        file.write("filter by U conc?, Uconc filter value (if used), correction by Pbc, filter by measurement's error, "
                   "measurement's error value (if used), Positive discordance filter, Negative discordance filter, "
                   "Which age was used, age cutoff (if used), How was discordance calculated, age cutoff (if used), "
                   "internal or propagated, errors \n " +
            str(p_filters.filter_by_uconc[0]) + ',' + str(p_filters.filter_by_uconc[1]) + ',' + str(p_filters.use_pbc) +
                   ',' + str(p_filters.filter_by_err[0]) + ',' + str(p_filters.filter_by_err[1]) + ',' +
                   str(p_filters.pos_disc_filter) + ',' + str(p_filters.neg_disc_filter) + ',' +
                   str(p_filters.which_age[0]) + ',' + str(p_filters.which_age[1]) + ',' + str(p_filters.disc_type[0]) +
                   ',' + str(p_filters.disc_type[1]) + ',' + str(p_filters.unc_type))

        file.close()

        probcum_file = open(p_probcum_filename, "w")
        age = 0
        bandwidth = p_graph_settings.bandwidth
        pdp_list = p_grainset.pdp(int(p_filters.unc_type))
        kde_list = p_grainset.kde(bandwidth)
        cpdp_list = p_grainset.cpdp(int(p_filters.unc_type))
        ckde_list = p_grainset.ckde(bandwidth)

        probcum_file.write("Age" + ',' + "PDP" + ',' + "CPDP" + ',' + "KDE" + ',' + "CKDE" + ',' +
                           'bandwidth=' + str(bandwidth))
        while age < EarthAge:
            probcum_file.write('\n' + str(age) + ',' + str(pdp_list[0][age]) + ',' + str(cpdp_list[age]) + ',' +
                               str(kde_list[0][age]) + ',' + str(ckde_list[age]))
            age += 1
        probcum_file.close()

    except AttributeError:
        pass


def fill_data_table(p_table, p_grainset, p_filters, p_colnames, *args):
    if p_grainset.analyses_list == []:
        pass
    for ch in p_table.get_children():
        p_table.delete(ch)
    i = 0
    j = 0
    unc_type = int(p_filters.unc_type)
    an_list = p_grainset.analyses_list
    good_grains = p_grainset.good_bad_sets(p_filters)
    grainset = p_grainset
    filters = p_filters
    p_table.heading("#0", text="Analysis name", anchor='c')
    while i < len(p_colnames):
        p_table.heading(p_colnames[i], text=p_colnames[i], anchor='c')
        p_table.column(i, width="100", anchor="c")
        while j < len(grainset):
            p_table.insert('', 'end', text=(an_list[j]), values=(
                    round(an_list[j].pb208_th232[0], 4),
                    round(an_list[j].pb208_th232[1], 4),
                    round(an_list[j].pb208_th232[2], 4),

                    round(an_list[j].pb207_pb206[0], 4),
                    round(an_list[j].pb207_pb206[1], 4),
                    round(an_list[j].pb207_pb206[2], 4),

                    round(an_list[j].pb207_u235[0], 4),
                    round(an_list[j].pb207_u235[1], 4),
                    round(an_list[j].pb207_u235[2], 4),

                    round(an_list[j].pb206_u238[0], 4),
                    round(an_list[j].pb206_u238[1], 4),
                    round(an_list[j].pb206_u238[2], 4),

                    round(an_list[j].corr_coef_75_68, 2),
                    round(an_list[j].corr_coef_86_76, 2),

                    round(an_list[j].u_conc[0], 4),
                    round(an_list[j].u_conc[1], 4),
                    round(an_list[j].u_conc[2], 4),

                    round(an_list[j].pbc[0], 4),
                    round(an_list[j].pbc[1], 4),
                    round(an_list[j].pbc[2], 4),

                    round(an_list[j].pb206_pb204[0], 1),
                    round(an_list[j].pb206_pb204[1], 1),
                    round(an_list[j].pb206_pb204[2], 1),

                    round(an_list[j].pb207_pb204[0], 1),
                    round(an_list[j].pb207_pb204[1], 1),
                    round(an_list[j].pb207_pb204[2], 1),

                    round(an_list[j].pb208_pb204[0], 1),
                    round(an_list[j].pb208_pb204[1], 1),
                    round(an_list[j].pb208_pb204[2], 1),

                    round(an_list[j].th232_pb204[0], 1),
                    round(an_list[j].th232_pb204[1], 1),
                    round(an_list[j].th232_pb204[2], 1),

                    round(an_list[j].u238_pb204[0], 1),
                    round(an_list[j].u238_pb204[1], 1),
                    round(an_list[j].u238_pb204[2], 1),

                    int(an_list[j].calc_age(2)[0]),
                    int(an_list[j].calc_age(2)[1]),
                    int(an_list[j].calc_age(2)[2]),

                    int(an_list[j].calc_age(3)[0]),
                    int(an_list[j].calc_age(3)[1]),
                    int(an_list[j].calc_age(3)[2]),

                    int(an_list[j].calc_age(1)[0]),
                    int(an_list[j].calc_age(1)[1]),
                    int(an_list[j].calc_age(1)[2]),

                    int(an_list[j].calc_age(0)[0]),
                    int(an_list[j].calc_age(0)[1]),
                    int(an_list[j].calc_age(0)[2]),

                    int(100*an_list[j].calc_discordance(2, p_filters.disc_type[1])),
                    int(100*an_list[j].calc_discordance(3, p_filters.disc_type[1])),
                    str(an_list[j].is_grain_good(filters)[0]),
                    str(an_list[j].is_grain_good(filters)[1]),
                    int(an_list[j].calc_age(an_list[j].is_grain_good(filters)[1])[0]),
                    int(an_list[j].calc_age(an_list[j].is_grain_good(filters)[1])[unc_type])
                    ),
                    tags=str(an_list[j].is_grain_good(filters)[0]))

            j += 1
        i += 1

    p_table.tag_configure("False", background="red")
    return good_grains



