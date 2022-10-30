import numpy as np
import json
import ast
import copy

instanz1 = json.load(
    open('/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed1_wgtrandom_deadlinejobsCmax_wgt_mj_factor1.000.json',
         'r'))
instanz2 = json.load(
    open('/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed1_wgtrandom_deadlinejobsCmax_wgt_mj_factor3.333.json',
         'r'))
instanz3 = json.load(open(
    '/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed1_wgtrandom_deadlinejobsexpected_wgt_mj_factor1.000.json',
    'r'))
instanz4 = json.load(open(
    '/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed1_wgtrandom_deadlinejobsexpected_wgt_mj_factor3.333.json',
    'r'))
instanz5 = json.load(open(
    '/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed1_wgtrandom_deadlinejobsmachinesCmax_wgt_mj_factor1.000.json',
    'r'))
instanz6 = json.load(open(
    '/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed1_wgtrandom_deadlinejobsmachinesCmax_wgt_mj_factor3.333.json',
    'r'))
instanz7 = json.load(open(
    '/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed1_wgtrandom_deadlinejobsmachinesexpected_wgt_mj_factor1.000.json',
    'r'))
instanz8 = json.load(open(
    '/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed1_wgtrandom_deadlinejobsmachinesexpected_wgt_mj_factor3.333.json',
    'r'))
instanz9 = json.load(open(
    '/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed1_wgtrandom_deadlinejobsmachinestight_wgt_mj_factor1.000.json',
    'r'))
instanz10 = json.load(open(
    '/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed1_wgtrandom_deadlinejobsmachinestight_wgt_mj_factor3.333.json',
    'r'))
instanz11 = json.load(
    open('/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed1_wgtrandom_deadlinejobstight_wgt_mj_factor1.000.json',
         'r'))
instanz12 = json.load(
    open('/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed1_wgtrandom_deadlinejobstight_wgt_mj_factor3.333.json',
         'r'))
instanz13 = json.load(open(
    '/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed1_wgtrandom_deadlinemachinesCmax_wgt_mj_factor1.000.json',
    'r'))
instanz14 = json.load(open(
    '/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed1_wgtrandom_deadlinemachinesCmax_wgt_mj_factor3.333.json',
    'r'))
instanz15 = json.load(open(
    '/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed1_wgtrandom_deadlinemachinesexpected_wgt_mj_factor1.000.json',
    'r'))
instanz16 = json.load(open(
    '/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed1_wgtrandom_deadlinemachinesexpected_wgt_mj_factor3.333.json',
    'r'))
instanz17 = json.load(open(
    '/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed1_wgtrandom_deadlinemachinestight_wgt_mj_factor1.000.json',
    'r'))
instanz18 = json.load(open(
    '/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed1_wgtrandom_deadlinemachinestight_wgt_mj_factor3.333.json',
    'r'))
instanz19 = json.load(
    open('/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed1_wgtrandom_deadlineNone_wgt_mj_factor1.000.json',
         'r'))
instanz20 = json.load(
    open('/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed1_wgtrandom_deadlineNone_wgt_mj_factor3.333.json',
         'r'))
instanz21 = json.load(
    open('/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed2_wgtrandom_deadlinejobsCmax_wgt_mj_factor1.000.json',
         'r'))
instanz22 = json.load(
    open('/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed2_wgtrandom_deadlinejobsCmax_wgt_mj_factor3.333.json',
         'r'))
instanz23 = json.load(open(
    '/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed2_wgtrandom_deadlinejobsexpected_wgt_mj_factor1.000.json',
    'r'))
instanz24 = json.load(open(
    '/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed2_wgtrandom_deadlinejobsexpected_wgt_mj_factor3.333.json',
    'r'))
instanz25 = json.load(open(
    '/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed2_wgtrandom_deadlinejobsmachinesCmax_wgt_mj_factor1.000.json',
    'r'))
instanz26 = json.load(open(
    '/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed2_wgtrandom_deadlinejobsmachinesCmax_wgt_mj_factor3.333.json',
    'r'))
instanz27 = json.load(open(
    '/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed2_wgtrandom_deadlinejobsmachinesexpected_wgt_mj_factor1.000.json',
    'r'))
instanz28 = json.load(open(
    '/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed2_wgtrandom_deadlinejobsmachinesexpected_wgt_mj_factor3.333.json',
    'r'))
instanz29 = json.load(open(
    '/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed2_wgtrandom_deadlinejobsmachinestight_wgt_mj_factor1.000.json',
    'r'))
instanz30 = json.load(open(
    '/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed2_wgtrandom_deadlinejobsmachinestight_wgt_mj_factor3.333.json',
    'r'))
instanz31 = json.load(
    open('/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed2_wgtrandom_deadlinejobstight_wgt_mj_factor1.000.json',
         'r'))
instanz32 = json.load(
    open('/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed2_wgtrandom_deadlinejobstight_wgt_mj_factor3.333.json',
         'r'))
instanz33 = json.load(open(
    '/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed2_wgtrandom_deadlinemachinesCmax_wgt_mj_factor1.000.json',
    'r'))
instanz34 = json.load(open(
    '/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed2_wgtrandom_deadlinemachinesCmax_wgt_mj_factor3.333.json',
    'r'))
instanz35 = json.load(open(
    '/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed2_wgtrandom_deadlinemachinesexpected_wgt_mj_factor1.000.json',
    'r'))
instanz36 = json.load(open(
    '/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed2_wgtrandom_deadlinemachinesexpected_wgt_mj_factor1.000.json',
    'r'))
instanz37 = json.load(open(
    '/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed2_wgtrandom_deadlinemachinestight_wgt_mj_factor1.000.json',
    'r'))
instanz38 = json.load(open(
    '/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed2_wgtrandom_deadlinemachinestight_wgt_mj_factor3.333.json',
    'r'))
instanz39 = json.load(
    open('/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed2_wgtrandom_deadlineNone_wgt_mj_factor1.000.json',
         'r'))
instanz40 = json.load(
    open('/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed2_wgtrandom_deadlineNone_wgt_mj_factor3.333.json',
         'r'))
instanz41 = json.load(
    open('/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed3_wgtrandom_deadlinejobsCmax_wgt_mj_factor1.000.json',
         'r'))
instanz42 = json.load(
    open('/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed3_wgtrandom_deadlinejobsCmax_wgt_mj_factor3.333.json',
         'r'))
instanz43 = json.load(open(
    '/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed3_wgtrandom_deadlinejobsexpected_wgt_mj_factor1.000.json',
    'r'))
instanz44 = json.load(open(
    '/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed3_wgtrandom_deadlinejobsexpected_wgt_mj_factor3.333.json',
    'r'))
instanz45 = json.load(open(
    '/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed3_wgtrandom_deadlinejobsmachinesCmax_wgt_mj_factor1.000.json',
    'r'))
instanz46 = json.load(open(
    '/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed3_wgtrandom_deadlinejobsmachinesCmax_wgt_mj_factor3.333.json',
    'r'))
instanz47 = json.load(open(
    '/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed3_wgtrandom_deadlinejobsmachinesexpected_wgt_mj_factor1.000.json',
    'r'))
instanz48 = json.load(open(
    '/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed3_wgtrandom_deadlinejobsmachinesexpected_wgt_mj_factor3.333.json',
    'r'))
instanz49 = json.load(open(
    '/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed3_wgtrandom_deadlinejobsmachinestight_wgt_mj_factor1.000.json',
    'r'))
instanz50 = json.load(open(
    '/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed3_wgtrandom_deadlinejobsmachinestight_wgt_mj_factor3.333.json',
    'r'))
instanz51 = json.load(
    open('/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed3_wgtrandom_deadlinejobstight_wgt_mj_factor1.000.json',
         'r'))
instanz52 = json.load(
    open('/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed3_wgtrandom_deadlinejobstight_wgt_mj_factor3.333.json',
         'r'))
instanz53 = json.load(open(
    '/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed3_wgtrandom_deadlinemachinesCmax_wgt_mj_factor1.000.json',
    'r'))
instanz54 = json.load(open(
    '/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed3_wgtrandom_deadlinemachinesCmax_wgt_mj_factor3.333.json',
    'r'))
instanz55 = json.load(open(
    '/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed3_wgtrandom_deadlinemachinesexpected_wgt_mj_factor1.000.json',
    'r'))
instanz56 = json.load(open(
    '/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed3_wgtrandom_deadlinemachinesexpected_wgt_mj_factor3.333.json',
    'r'))
instanz57 = json.load(open(
    '/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed3_wgtrandom_deadlinemachinestight_wgt_mj_factor1.000.json',
    'r'))
instanz58 = json.load(open(
    '/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed3_wgtrandom_deadlinemachinestight_wgt_mj_factor3.333.json',
    'r'))
instanz59 = json.load(
    open('/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed3_wgtrandom_deadlineNone_wgt_mj_factor1.000.json',
         'r'))
instanz60 = json.load(
    open('/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed3_wgtrandom_deadlineNone_wgt_mj_factor3.333.json',
         'r'))
instanz61 = json.load(
    open('/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed4_wgtrandom_deadlinejobsCmax_wgt_mj_factor1.000.json',
         'r'))
instanz62 = json.load(
    open('/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed4_wgtrandom_deadlinejobsCmax_wgt_mj_factor3.333.json',
         'r'))
instanz63 = json.load(open(
    '/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed4_wgtrandom_deadlinejobsexpected_wgt_mj_factor1.000.json',
    'r'))
instanz64 = json.load(open(
    '/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed4_wgtrandom_deadlinejobsexpected_wgt_mj_factor3.333.json',
    'r'))
instanz65 = json.load(open(
    '/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed4_wgtrandom_deadlinejobsmachinesCmax_wgt_mj_factor1.000.json',
    'r'))
instanz66 = json.load(open(
    '/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed4_wgtrandom_deadlinejobsmachinesCmax_wgt_mj_factor3.333.json',
    'r'))
instanz67 = json.load(open(
    '/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed4_wgtrandom_deadlinejobsmachinesexpected_wgt_mj_factor1.000.json',
    'r'))
instanz68 = json.load(open(
    '/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed4_wgtrandom_deadlinejobsmachinesexpected_wgt_mj_factor3.333.json',
    'r'))
instanz69 = json.load(open(
    '/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed4_wgtrandom_deadlinejobsmachinestight_wgt_mj_factor1.000.json',
    'r'))
instanz70 = json.load(open(
    '/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed4_wgtrandom_deadlinejobsmachinestight_wgt_mj_factor3.333.json',
    'r'))
instanz71 = json.load(
    open('/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed4_wgtrandom_deadlinejobstight_wgt_mj_factor1.000.json',
         'r'))
instanz72 = json.load(
    open('/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed4_wgtrandom_deadlinejobstight_wgt_mj_factor3.333.json',
         'r'))
instanz73 = json.load(open(
    '/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed4_wgtrandom_deadlinemachinesCmax_wgt_mj_factor1.000.json',
    'r'))
instanz74 = json.load(open(
    '/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed4_wgtrandom_deadlinemachinesCmax_wgt_mj_factor3.333.json',
    'r'))
instanz75 = json.load(open(
    '/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed4_wgtrandom_deadlinemachinesexpected_wgt_mj_factor1.000.json',
    'r'))
instanz76 = json.load(open(
    '/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed4_wgtrandom_deadlinemachinesexpected_wgt_mj_factor3.333.json',
    'r'))
instanz77 = json.load(open(
    '/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed4_wgtrandom_deadlinemachinestight_wgt_mj_factor1.000.json',
    'r'))
instanz78 = json.load(open(
    '/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed4_wgtrandom_deadlinemachinestight_wgt_mj_factor3.333.json',
    'r'))
instanz79 = json.load(
    open('/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed4_wgtrandom_deadlineNone_wgt_mj_factor1.000.json',
         'r'))
instanz80 = json.load(
    open('/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed4_wgtrandom_deadlineNone_wgt_mj_factor3.333.json',
         'r'))
instanz81 = json.load(
    open('/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed5_wgtrandom_deadlinejobsCmax_wgt_mj_factor1.000.json',
         'r'))
instanz82 = json.load(
    open('/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed5_wgtrandom_deadlinejobsCmax_wgt_mj_factor3.333.json',
         'r'))
instanz83 = json.load(open(
    '/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed5_wgtrandom_deadlinejobsexpected_wgt_mj_factor1.000.json',
    'r'))
instanz84 = json.load(open(
    '/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed5_wgtrandom_deadlinejobsexpected_wgt_mj_factor3.333.json',
    'r'))
instanz85 = json.load(open(
    '/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed5_wgtrandom_deadlinejobsmachinesCmax_wgt_mj_factor1.000.json',
    'r'))
instanz86 = json.load(open(
    '/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed5_wgtrandom_deadlinejobsmachinesCmax_wgt_mj_factor3.333.json',
    'r'))
instanz87 = json.load(open(
    '/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed5_wgtrandom_deadlinejobsmachinesexpected_wgt_mj_factor1.000.json',
    'r'))
instanz88 = json.load(open(
    '/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed5_wgtrandom_deadlinejobsmachinesexpected_wgt_mj_factor3.333.json',
    'r'))
instanz89 = json.load(open(
    '/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed5_wgtrandom_deadlinejobsmachinestight_wgt_mj_factor1.000.json',
    'r'))
instanz90 = json.load(open(
    '/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed5_wgtrandom_deadlinejobsmachinestight_wgt_mj_factor3.333.json',
    'r'))
instanz91 = json.load(
    open('/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed5_wgtrandom_deadlinejobstight_wgt_mj_factor1.000.json',
         'r'))
instanz92 = json.load(
    open('/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed5_wgtrandom_deadlinejobstight_wgt_mj_factor3.333.json',
         'r'))
instanz93 = json.load(open(
    '/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed5_wgtrandom_deadlinemachinesCmax_wgt_mj_factor1.000.json',
    'r'))
instanz94 = json.load(open(
    '/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed5_wgtrandom_deadlinemachinesCmax_wgt_mj_factor3.333.json',
    'r'))
instanz95 = json.load(open(
    '/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed5_wgtrandom_deadlinemachinesexpected_wgt_mj_factor1.000.json',
    'r'))
instanz96 = json.load(open(
    '/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed5_wgtrandom_deadlinemachinesexpected_wgt_mj_factor3.333.json',
    'r'))
instanz97 = json.load(open(
    '/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed5_wgtrandom_deadlinemachinestight_wgt_mj_factor1.000.json',
    'r'))
instanz98 = json.load(open(
    '/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed5_wgtrandom_deadlinemachinestight_wgt_mj_factor3.333.json',
    'r'))
instanz99 = json.load(
    open('/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed5_wgtrandom_deadlineNone_wgt_mj_factor1.000.json',
         'r'))
instanz100 = json.load(
    open('/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed5_wgtrandom_deadlineNone_wgt_mj_factor3.333.json',
         'r'))
instanz101 = json.load(open(
    '/home/tchiapi/Downloads/instancesII/R3_10_uniform_discrete_seed2_wgtrandom_deadlinejobsmachinesCmax_wgt_mj_factor3.333.json',
    'r'))
ListVonInstanzen = [instanz1, instanz2, instanz3, instanz4, instanz5, instanz6, instanz7, instanz8, instanz9, instanz10,
                    instanz11, instanz12, instanz13, instanz14, instanz15, instanz16, instanz17, instanz18, instanz19,
                    instanz20, instanz21, instanz22, instanz23, instanz24, instanz25, instanz26, instanz27, instanz28,
                    instanz29, instanz30, instanz31, instanz32, instanz33, instanz34, instanz35, instanz36, instanz37,
                    instanz38, instanz39, instanz40, instanz41, instanz42,
                    instanz43, instanz44, instanz45, instanz46, instanz47, instanz48, instanz49, instanz50, instanz51,
                    instanz52, instanz53, instanz54, instanz55, instanz56, instanz57, instanz58, instanz59, instanz60,
                    instanz61, instanz62, instanz63, instanz64, instanz65, instanz66, instanz67, instanz68, instanz69,
                    instanz70, instanz71, instanz72, instanz73, instanz74, instanz75
    , instanz76, instanz77, instanz78, instanz79, instanz80, instanz81, instanz82, instanz83, instanz84, instanz85,
                    instanz86, instanz87, instanz88, instanz89, instanz90
    , instanz91, instanz92, instanz93, instanz94, instanz95, instanz96, instanz97, instanz98, instanz99, instanz100,
                    instanz101]


def addInstanzen(n):
    ListVonInstanzen = []
    summe = 1
    a = 'instanz'
    while len(ListVonInstanzen) < n:
        if len(a) < 9:
            a += str(summe)
            ListVonInstanzen.append(a)
            summe += 1
            a = 'instanz'
        else:
            print(summe)
            conv = a + str(summe)
            ListVonInstanzen.append(conv)
            summe += 1

    return ListVonInstanzen


class Instance:
    def __init__(self, n, m, Pij, Dj, wj):
        self.n = n
        self.m = m
        self.Pij = Pij
        self.Dj = Dj
        self.wj = wj

    def Training_set(self,scenario):
        """
        @:parameter scenrario:ist die Anzahl von Szenarien
        :return: eine Liste von Szenarien
        """
        ListVonSzenarien = []
        for x in range(scenario):
            n, m = ListVonInstanzen[x]['n'], ListVonInstanzen[x]['m']
            p = np.zeros((m, n))
            for i in range(m):
                for j in range(n):
                    support = ListVonInstanzen[x]['processing_times']['M' + str(i)][j]['a']
                    proba = ListVonInstanzen[x]['processing_times']['M' + str(i)][j]['p']
                    p[i, j] = np.random.choice(support, p=proba)
            ListVonSzenarien.append(p)
        return ListVonSzenarien

    def get_EPij(self,instance, i, j):
        support = instance['processing_times']['M' + str(i)][j]['a']
        probas = instance['processing_times']['M' + str(i)][j]['p']
        return np.array(support).dot(probas)

    def cancelEle(self,element, Liste):
        for ele in Liste:
            if ele == element:
                index = Liste.index(ele)
                Liste.pop(ele)

    def get_EPij_NantSup(self,instance, i, j, a):
        """
        :param instance: ist eine Instanz
        :param i:  ist eine Zahl
        :param a:  ist eine Zufallsvariable
        :param j: ist eine Zahl(Interger)
        :return: den Erwartungswert
        """

        support = instance['processing_times']['M' + str(i)][j]['a']
        tmpS = copy.deepcopy(support)
        probas = instance['processing_times']['M' + str(i)][j]['p']
        tmpP = copy.deepcopy(probas)
        for x in support:
            if x > a:
                self.cancelEle(a,tmpS)
                index = support.index(a)
                self.cancelEle(probas[index],tmpP)
        return  np.array(tmpS).dot(tmpP)/sum(tmpP)

    def get_EPij_NantInf(self, instance, i, j, a):
        """
        :param instance: ist eine Instanz
        :param i:  ist eine Zahl
        :param a:  ist eine Zufallsvariable
        :param j: ist eine Zahl(Interger)
        :return: den Erwartungswert
        """

        support = instance['processing_times']['M' + str(i)][j]['a']
        tmpS = copy.deepcopy(support)
        probas = instance['processing_times']['M' + str(i)][j]['p']
        tmpP = copy.deepcopy(probas)
        for x in support:
            if x < a:
                self.cancelEle(a, tmpS)
                index = support.index(a)
                self.cancelEle(probas[index], tmpP)
        return np.array(tmpS).dot(tmpP) / sum(tmpP)

    def get_EPij_NantEqu(self, instance, i, j, a):
        """
        :param instance: ist eine Instanz
        :param i:  ist eine Zahl
        :param a:  ist eine Zufallsvariable
        :param j: ist eine Zahl(Interger)
        :return: den Erwartungswert
        """

        support = instance['processing_times']['M' + str(i)][j]['a']
        newSupport =[]
        probas = instance['processing_times']['M' + str(i)][j]['p']
        newProbas = []

        for x in support:
            if x == a:
                newSupport.append(x)
                index = support.index(x)
                newProbas.append(probas[index])
        return np.array(newSupport).dot(newProbas) / sum(newProbas)

    # def Validation_Set(self):


if __name__ == "__main__":
    s = Instance
    b = s.Training_set(30)


class Policy:
    def simulate(self, n, Szenario):
        for x in range(len(ListVonInstanzen)):
            m, n = ListVonInstanzen['m'], instance['n']

# class Fixed_assignment(Policy):
