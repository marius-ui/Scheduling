import math
import random
import time as t
import numpy as np
import json
import copy
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt

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


class Scenario:
    def __init__(self,instance):
        self.instance = instance
        self.p = np.zeros((instance.m, instance.n))
        for x in range(instance.m):
            for y in range(instance.n):
                support = instance.processing_times['M'+str(x)][y]['a']
                probas = instance.processing_times['M'+str(x)][y]['p']
                self.p[x,y] = np.random.choice(support,p=probas)

class Instance:
    def __init__(self, deadline_type, job_deadlines, job_type, m, machine_type, n, processing_times,
                 seed, speeds, tau, weights, weights_type, number_train_scenarios=100):
        self.deadline_type = deadline_type
        self.job_dealines = job_deadlines
        self.job_type = job_type
        self.m = m
        self.machine_type = machine_type
        self.n = n
        self.processing_times = processing_times
        self.seed = seed
        self.speeds = speeds
        self.tau = tau
        self.weights = weights
        self.weights_type = weights_type
        self.number_train_scenarios = number_train_scenarios
        self.generate_training_set()

    def generate_training_set(self):
        if self.seed:
            np.random.seed(self.seed)
        self.training_set = [Scenario(self) for i in range(self.number_train_scenarios)]

    def get_EPij(self, i, j):
        support = self.processing_times['M' + str(i)][j]['a']
        probas = self.processing_times['M' + str(i)][j]['p']
        return np.array(support).dot(probas)

    def cancelEle(self,Element, List):
        """

        :param Element: ist ein einfaches Element
        :param List: ist eine List von Elementen <class 'list'>
        :return: Die Funktion auf der gegebenen List das Element im Parameter und löscht es
        """
        for ele in List:
            if ele == Element:
                index = List.index(ele)
                List.pop(index)

    def get_EPij_NantSup(self, i, j, a):
        """
        :param instance: ist eine Instanz
        :param i:  ist eine Zahl
        :param a:  ist eine Zufallsvariable
        :param j: ist eine Zahl(Interger)
        :return: den bedingten Erwartungswert E[P_{i,j}|P_{i,j}>a]
        """

        support = self.processing_times['M' + str(i)][j]['a']
        tmpS = copy.deepcopy(support)
        probas = self.processing_times['M' + str(i)][j]['p']
        tmpP = copy.deepcopy(probas)
        newS = []
        newP = []
        for x in support:
            if x > a:
                newS.append(x)

        for x in newS:
            newP.append(probas[support.index(x)])
                #self.cancelEle(a,tmpS)
                #index = support.index(a)
                #self.cancelEle(probas[index],tmpP)
        try:
            return np.array(newS).dot(newP) / sum(newP)
        except ZeroDivisionError:
            print('Fehler')
        if len(newP) == 0:
            raise ZeroDivisionError('Teilen durch 0')

class MachineState(object):
    def __init__(self,available=False,shutdown=False,busy=False,job_being_processed=None,job_started_at=None):
        assert int(available) + int(shutdown) + int(busy) == 1, "exactly one of these vars must be True"
        self.available = available
        self.shutdown=shutdown
        self.busy=busy
        if self.busy:
            assert job_being_processed is not None
            assert job_started_at is not None
            self.job_being_processed = job_being_processed
            self.job_started_at = job_started_at

class Action(object):
    def __init__(self, start=True,job=None,machine=None,shutdown=False):
        assert not(start and shutdown)
        self.start = start
        self.shutdown = shutdown
        if self.start:
            assert (self.job is not None) and (self.machine is not None)
        if self.shutdown:
            assert self.machine is not None

class Schedule(object):
    def __init__(self, instance, C, S, A, L):

        pass # TODO store C,S,A,L
    def evaulate(self):
        instance = self.instance
        m, n = instance.m, instance.n
        d = instance.job_dealines
        w = instance.weights
        cost = 0
        for j in range(n):
            cost += (w[j] * max(self.C[j] - d[j], 0))
        return cost

    def visualize(self):
        pass # TODO
class State(object):
    def __init__(self, time, remaining_jobs, machine_states):
        # current time
        self.time = time
        # list of remaining jobs
        self.remaining_jobs = remaining_jobs
        # list of m machine states
        self.machine_states = machine_states

    def is_there_available_machine(self):
        return any([mstate.available for mstate in self.machine_states])


    def getRemainingJobs(self):
        if len(self.Jobs)==0:
            return 'Es gibt keinen Job mehr'
        else:
            return self.Jobs

class Policy(object):
    def __init__(self,instance,scenario):
        self.instance = instance
        self.scenario = scenario

    def get_initial_state(self):
        time= 0
        remaining_jobs = list(range(self.instance.n))
        machine_states = [MachineState(available=True) for i in range(self.instance.m)]
        return State(time,remaining_jobs,machine_states)

    def simulate(self,scenario):
        instance = self.instance
        self.current_state = self.get_initial_state()
        m, n = instance.m, instance.n
        C = [None] * n  # completion times
        S = [None] * n  # starting times
        A = [None] * n  # assignement
        L = [0] * m  # machine load (latest completion time)
        while len(self.current_state.remaining_jobs) > 0:
            action = self.step()
            #start a job
            if action.start:
                i,j = action.machine, action.job
                assert self.current_state.machine_states[i].available
                C[j] = self.current_state.time + scenario[i][j]
                S[j] = self.current_state.time
                L[i] = C[j]
                A[j] = i
            elif action.shutdown:
                i = action.machine
                assert self.current_state.machine_states[i].available
            #compute the next state
            self.update_state(action, scenario)

        return S,C,A,L    # TODO put S,C,A,L in a Schedule object

    def step(self):
        """should be defined in child classes
        returns an action to take in the state stored in self.current_state
        """
        pass

    def update_state(self, action, scenario):
        m = self.instance.m
        remaining_jobs = self.current_state.remaining_jobs[:]
        old_time = self.current_state.time
        if action.start:
            remaining_jobs.remove(action.job)
        machine_states = [None] * m
        if action.shutdown:
            machine_states[action.machine] = MachineState(True)
        for i,ms in enumerate(self.current_state.machine_states):
            if ms.shutdown:
                machine_states[i] = MachineState(True)
        if not(action.start) and not(action.shutdown):
            time = old_time + 1
        else:
            pass
            #TODO compute the next time (find which machine becomes available first

        # TODO compute new machine state of each macine not shutdown (availbe or busy)

        assert all([ms is not None for ms in machine_states])
        return State(time,remaining_jobs,machine_states)

    def neighbor(self,Jobs):
        #TODO define in child class
        pass


    def optimize(self):
        #TODO implement a local search
        pass

    def expected_cost(self,F,scenario,train=True,N=0):
        if train:
            training_set = self.instance.training_set
        else:
            assert N>0
            training_set = [Scenario(self.instance) for i in range(N)]
        costs = []
        for sc in training_set:
            schedule = self.simulate(sc)
            costs.append(schedule.evaluate())
        return np.mean(costs), costs

class FixedAssigment(Policy,State):
    def __init__(self,instance,scenario):
        Policy.__init__(self,instance,scenario)
        self.assignment()

    def assignment(self):
        # compute an assignment for a fixed-assignment policy
        # with a greedy algorithm that considers the jobs in the order 0,...,n-1
        # and sequentially insert them on the machine where it would terminate first (in expectation)
        remaining_jobs = list(range(self.instance.n))
        machine_states = [[] for i in range(self.instance.m)]# job-to-machine assignment
        L = [0 for i in range(self.instance.m)]# expected load
        for j in remaining_jobs:
            completion_on_machine = []
            for i in range(self.instance.m):
                completion_on_machine.append(L[i]+self.instance.get_EPij(i,j))
                #take the machine where the job completes the earliest
            i = np.argmin(completion_on_machine)
            machine_states[i].append(j)
            L[i]+=self.instance.get_EPij(i,j)
        self.assignment_set = machine_states
    def simulate(self,scenario):
        m, n = self.instance.m, self.instance.n
        C = [None] * n  # completion times
        S = [None] * n  # starting times
        A = [None] * n  # assignement
        L = [0] * m  # machine load (latest completion time)
        #machine_states = self.assignment()
        for i in range(m):
            for j in self.machine_states[i]:
                S[j] = L[i]
                L[i] += scenario.p[i][j]
                C[j] = L[i]
                A[j] = i
        return C, S, A, L


    def neighbor(self):
       assigment =  self.assigment(instance)
       Job1 = 0
       Job2 = 0

       random_machine1 = random.choice(assigment)
       IndexMachine1 = assigment.index(random_machine1)
       random_machine2 = random.choice(assigment)
       IndexMachine2 = assigment.index(random_machine2)

       while random_machine1 != random_machine2:
           Job1 = random.choice(random_machine1)
           IndexJob1 = random_machine1.index(Job1)
           Job2 = random.choice(random_machine2)
           IndexJob2 = random_machine2.index(Job2)
           tmp = random_machine1[IndexJob1]
           random_machine1[IndexJob1] = random_machine2[IndexJob2]
           random_machine2[IndexJob2] = tmp
           assigment[IndexMachine1] = random_machine1
           assigment[IndexMachine2] = random_machine2
       return assigment
"""    def generate_scenario(self, instance):
        P = np.zeros((instance.m, instance.n))
        for i in range(instance.m):
            for j in range(instance.n):
                support = instance.processing_times['M' + str(i)][j]['a']
                probas = instance.processing_times['M' + str(i)][j]['p']
                P[i, j] = np.random.choice(support, p=probas)
        return P

    def assigment(self, instance):

        :param scenario:
        :return: compute an assignment for a fixed-assignment policy
        with a greedy algorithm that considers the jobs in the order 0,...,n-1
        and sequentially insert them on the machine where it would terminate first (in expectation)
        
        m, n = instance.m,instance.n
        for j in range(n):
            completion_on_machine = []
            for i in range(m):
                completion_on_machine.append(self.time[i] + instance.get_EPij(i, j))
            # take the machine where the job completes the earliest
            i = np.argmin(completion_on_machine)
            # put job j on this machine
            self.Machines[i].append(j)
            self.time[i] += instance.get_EPij(i,j)

    
    def simulate(self,instance,scenario):
        m, n = instance.m, instance.n
        C = [None] * n  # completion times
        S = [None] * n  # starting times
        A = [None] * n  # assignement
        L = [0] * m  # machine load (latest completion time)
        for i in range(m):
            for j in self.Machines[i]:
                S[j] = L[i]
                L[i] += scenario[i][j]
                C[j] = L[i]
                A[j] = i
        return S,C,A,L
    def evaluate(self,instance,scenario):

        m, n = instance.m, instance.n
        d = instance.job_dealines
        w = instance.weights
        Si, Ci, Ai, Li = self.simulate(instance,scenario)
        cost = 0
        for j in range(n):
            cost += (w[j] * max(Ci[j] - d[j], 0))
        return cost
    def expected_cost(self,F,instance, N):
        #simulate the fixed assignment policy N times and return the expected costs
        costs = []
        for counter in range(N):
            if counter % 1000 == 0:
                print(str(counter), end="\r")
                scen = self.generate_scenario(instance)
                costs.append(self.evaluate(instance,scen))
        return np.mean(costs)
    def visualization(self, instance,scenario):
        Jobs = [0,1,2,3,4,5,6,7,8,9]
        Si, Ci, Ai, Li = self.simulate(instance,scenario)
        for  j in range(len(Si)):
            Si[j]+=1
            Ci[j]+=1
        print(self.Machines,Si[1],Ci[1],Si[2],Ci[2])

        df = pd.DataFrame([
            dict(Task= "Job"+str(Jobs[0]), Start='2022-12-' + str(int(Si[0])), Finish='2022-12-' + str(int(Ci[0])),Resource="Machine"+str(Ai[0])),
            dict(Task="Job" + str(Jobs[1]), Start='2022-12-' + str(int(Si[1])), Finish='2022-12-' + str(int(Ci[1])),Resource="Machine" + str(Ai[1])),
            dict(Task="Job" + str(Jobs[2]), Start='2022-12-' + str(int(Si[2])), Finish='2022-12-' + str(int(Ci[2])),Resource="Machine" + str(Ai[2])),
            dict(Task="Job" + str(Jobs[3]), Start='2022-12-' + str(int(Si[3])), Finish='2022-12-' + str(int(Ci[3])),Resource="Machine" + str(Ai[3])),
            dict(Task="Job" + str(Jobs[4]), Start='2022-12-' + str(int(Si[4])), Finish='2022-12-' + str(int(Ci[4])),Resource="Machine" + str(Ai[4])),
            dict(Task="Job" + str(Jobs[5]), Start='2022-12-' + str(int(Si[5])), Finish='2022-12-' + str(int(Ci[5])),Resource="Machine" + str(Ai[5])),
            dict(Task="Job" + str(Jobs[6]), Start='2022-12-' + str(int(Si[6])), Finish='2022-12-' + str(int(Ci[6])),Resource="Machine" + str(Ai[6])),
            dict(Task="Job" + str(Jobs[7]), Start='2022-12-' + str(int(Si[7])), Finish='2022-12-' + str(int(Ci[7])),Resource="Machine" + str(Ai[7])),
            dict(Task= "Job"+str(Jobs[8]), Start='2022-12-' + str(int(Si[8])), Finish='2022-12-' + str(int(Ci[8])),Resource="Machine"+str(Ai[8])),
            dict(Task= "Job"+str(Jobs[9]), Start='2022-12-' + str(int(Si[9])), Finish='2022-12-' + str(int(Ci[9])),Resource="Machine"+str(Ai[9]))
        ])

        fig = px.timeline(df, x_start="Start", x_end="Finish", y="Resource", color="Task",title='Scheduling with fixe_assignment', text='Task')
        fig.show()"""

class List_Policy(Policy,State):
    def __init__(self,scenario,instance,time,Jobs,Machines):
        Policy.__init__(self,instance,scenario)
        State.__init__(self,time,Jobs,Machines)
    def neighbor(self,Jobs):
        #TODO define in child class
        tmp = copy.deepcopy(Jobs)
        Job1 ,Job2 = random.choice(tmp),random.choice(tmp)
        Job1Index,Job2Index = tmp.index(Job1), tmp.index(Job2)
        while Job1 == Job2:
            Job1, Job2 = random.choice(tmp), random.choice(tmp)
            Job1Index, Job2Index = tmp.index(Job1), tmp.index(Job2)
            tmp[Job1Index], tmp[Job2Index] = tmp[Job2Index], tmp[Job1Index]
        tmp[Job1Index],tmp[Job2Index]=tmp[Job2Index],tmp[Job1Index]
        return tmp
    """def putJobonMachine(self, time, Job, machines, instance):
        completion_on_machine = []
        for i in range(len(machines)):
            completion_on_machine.append(time[i] + instance.get_EPij(i,Job))
        i = np.argmin(completion_on_machine)
        print(completion_on_machine)
        machines[i].append(Job)
        time[i]+=instance.get_EPij(i,Job)
        return time,machines
    def ShutDmachine(self,time,machines):
        for i in range(len(machines)):
            if len(machines[i])==0:
                machines.remove(machines[i])
                time.remove(time[i])
            else:
                t.sleep(time[i])
        return time,machines
    def putJobOnAvalaibeMachine(self,time,Job,machines,instance):
        for i in range (len(machines)):
            if len(machines[i])==0:
                machines[i].append(Job)
                time[i]+=instance.get_EPij(i,Job)
        return time,machines"""

    """def simulate(self,instance,scenario):
        m, n = instance.m, instance.n
        Ci = [None] * n  # completion times
        Si = [None] * n  # starting times
        Ai = [None] * n  # assignement
        Li = [0] * m  # machine load (latest completion time
        time = []
        machines =[]
        while self.Jobs:
            Job = self.Jobs.pop(0)
            # Put the Job in a available machine
            #print(machines)
            # take the machine where the job completes the earliest
            time,machines = self.putJobonMachine(self.time,Job,self.Machines,instance)
            #time, machines=self.putJobOnAvalaibeMachine(self.time,Job,self.Machines,instance)
            print(machines)
        # shut a available machine
        time,machines = self.ShutDmachine(self.time,self.Machines)
        self.time,self.Machines= time,machines
        for i in range(len(self.Machines)):
            for j in self.Machines[i]:
                Si[j] = Li[i]
                Li[i] += (scenario[i][j])
                Ci[j] = Li[i]
                Ai[j] = i
        return Si, Ci, Ai, Li"""

"""    def evaluate(self,instance ,scenario):
        m, n = instance.m, instance.n
        d = instance.job_dealines
        w = instance.weights
        Si, Ci, Ai, Li = self.simulate(instance,scenario)
        cost = 0
        for j in range(n):
            cost += (w[j] * max(Ci[j] - d[j], 0))
        return cost
    def generate_scenario(self, instance):
        P = np.zeros((instance.m, instance.n))
        for i in range(instance.m):
            for j in range(instance.n):
                support = instance.processing_times['M' + str(i)][j]['a']
                probas = instance.processing_times['M' + str(i)][j]['p']
                P[i, j] = np.random.choice(support, p=probas)
        return p
    def expected_cost(self,instance, N=100000):
        #simulate the fixed assignment policy N times and return the expected costs
        costs = []
        for counter in range(N):
            if counter % 1000 == 0:
                scen = self.generate_scenario(instance)
                costs.append(self.evaluate(instance,scen))
        return np.mean(costs)"""

"""  def visualization(self, instance, scenario):
        Jobs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        Si, Ci, Ai, Li = self.simulate(instance, scenario)
        for j in range(len(Si)):
            Si[j] += 1
            Ci[j] += 1
        print(self.Machines, Si[1], Ci[1], Si[2], Ci[2])

        df = pd.DataFrame([
            dict(Task="Job" + str(Jobs[0]), Start='2022-12-' + str(int(Si[0])), Finish='2022-12-' + str(int(Ci[0])),
                 Resource="Machine" + str(Ai[0])),
            dict(Task="Job" + str(Jobs[1]), Start='2022-12-' + str(int(Si[1])), Finish='2022-12-' + str(int(Ci[1])),
                 Resource="Machine" + str(Ai[1])),
            dict(Task="Job" + str(Jobs[2]), Start='2022-12-' + str(int(Si[2])), Finish='2022-12-' + str(int(Ci[2])),
                 Resource="Machine" + str(Ai[2])),
            dict(Task="Job" + str(Jobs[3]), Start='2022-12-' + str(int(Si[3])), Finish='2022-12-' + str(int(Ci[3])),
                 Resource="Machine" + str(Ai[3])),
            dict(Task="Job" + str(Jobs[4]), Start='2022-12-' + str(int(Si[4])), Finish='2022-12-' + str(int(Ci[4])),
                 Resource="Machine" + str(Ai[4])),
            dict(Task="Job" + str(Jobs[5]), Start='2022-12-' + str(int(Si[5])), Finish='2022-12-' + str(int(Ci[5])),
                 Resource="Machine" + str(Ai[5])),
            dict(Task="Job" + str(Jobs[6]), Start='2022-12-' + str(int(Si[6])), Finish='2022-12-' + str(int(Ci[6])),
                 Resource="Machine" + str(Ai[6])),
            dict(Task="Job" + str(Jobs[7]), Start='2022-12-' + str(int(Si[7])), Finish='2022-12-' + str(int(Ci[7])),
                 Resource="Machine" + str(Ai[7])),
            dict(Task="Job" + str(Jobs[8]), Start='2022-12-' + str(int(Si[8])), Finish='2022-12-' + str(int(Ci[8])),
                 Resource="Machine" + str(Ai[8])),
            dict(Task="Job" + str(Jobs[9]), Start='2022-12-' + str(int(Si[9])), Finish='2022-12-' + str(int(Ci[9])),
                 Resource="Machine" + str(Ai[9]))
        ])

        fig = px.timeline(df, x_start="Start", x_end="Finish", y="Resource", color="Task",title='Scheduling with List_policy', text='Task')
        fig.show()"""

class Advanced_List_policy(Policy,State):
    def __init__(self,scenario,instance,time,Jobs,Machines):
        Policy.__init__(self,instance,scenario)
        State.__init__(self,time,Jobs,Machines)
    """def simulate(self,instance,scenario):
        m, n = instance.m, instance.n
        Ci = [None] * n  # completion times
        Si = [None] * n  # starting times
        Ai = [None] * n  # assignement
        Li = [0] * m  # machine load (latest completion time
        Job1 = self.Jobs.pop(0)
        Job2 = self.Jobs.pop(0)
        Job3 = self.Jobs.pop(0)
        S = [None] * n
        L = [0] * m
        self.Machines[0].append(Job1)
        self.Machines[1].append(Job2)
        self.Machines[2].append(Job3)
        S[Job1] = L[0]
        L[0] += scenario[0][Job1]
        S[Job2] = L[1]
        L[1] += scenario[1][Job2]
        S[Job3] = L[2]
        L[2] += scenario[2][Job3]
        self.time[0]+=instance.get_EPij(0,Job1)
        self.time[1] += instance.get_EPij(1, Job2)
        self.time[2] += instance.get_EPij(2, Job3)
        while self.Jobs:
            Job = self.Jobs.pop(0)
            completion_on_machine = []
            for i in range(len(self.Machines)):
                S[Job] =L[i]
                L[i]+=scenario[i][Job]
                print(S,L)
                #completion_on_machine.append(self.time[i] + instance.get_EPij(instance, i, Job))
                j = self.Machines[i][-1]
                #t = instance.processing_times['M' + str(i)][j]['a']
                print(self.time[i],instance.get_EPij_NantSup(i,j,L[i]))
                completion_on_machine.append(self.time[i]+instance.get_EPij_NantSup(i,j,math.ceil(self.time[i]))+instance.get_EPij(i,Job))
            i = np.argmin(completion_on_machine)
            #print(completion_on_machine)
            j = self.Machines[i][-1]
            self.time[i]+=(instance.get_EPij_NantSup(i, j, math.ceil(self.time[i])) + instance.get_EPij(i, Job))
            self.Machines[i].append(Job)
            completion_on_machine1 =[]
            for i in range (len(self.Machines)):
                #j = self.Machines[i][-1]
                #t = instance.processing_times['M' + str(i)][j]['a']
                sum_support = self.getProcTime(instance,self.Machines[i],i)
                new_t = 0
                if self.time[i] != sum_support:
                    new_t = self.time[i]-sum_support
                completion_on_machine1.append(sum_support+instance.get_EPij_NantSup(i,j,math.ceil(new_t))+instance.get_EPij(i,Job))
            i = np.argmin(completion_on_machine1)
            j = self.Machines[i][-1]
            sum_support = self.getProcTime(instance, self.Machines[i], i)
            new_t = self.time[i] - sum_support
            self.time[i]+=(sum_support + instance.get_EPij_NantSup(i, j, new_t) + instance.get_EPij(i, Job))
            self.Machines[i].append(Job)
        for i in range(len(self.Machines)):
            for j in self.Machines[i]:
                Si[j] = Li[i]
                Li[i] += (scenario[i][j])
                Ci[j] = Li[i]
                Ai[j] = i
        return Si, Ci, Ai, Li
    def getProcTime(self,instance,machine,i):
        sum_support = 0
        for Job in machine:
            sum_support+=instance.get_EPij(i,Job)
        return sum_support
    def evaluate(self,instance,scenario):
        m, n = instance.m, instance.n
        d = instance.job_dealines
        w = instance.weights
        Si, Ci, Ai, Li = self.simulate(instance,scenario)
        cost = 0
        for j in range(n):
            cost += (w[j] * max(Ci[j] - d[j], 0))
        return cost
    def expected_cost(self,instance, N=100000):
        #simulate the fixed assignment policy N times and return the expected costs
        costs = []
        for counter in range(N):
            if counter % 1000 == 0:
                scen = self.generate_scenario(instance)
                costs.append(self.evaluate(instance,scen))
        return np.mean(costs)
    def generate_scenario(self, instance):
        P = np.zeros((instance.m, instance.n))
        for i in range(instance.m):
            for j in range(instance.n):
                support = instance.processing_times['M' + str(i)][j]['a']
                probas = instance.processing_times['M' + str(i)][j]['p']
                P[i, j] = np.random.choice(support, p=probas)
        return P
    def visualization(self, instance, scenario):
        Jobs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        Si, Ci, Ai, Li = self.simulate(instance, scenario)
        for j in range(len(Si)):
            Si[j] += 1
            Ci[j] += 1


        df = pd.DataFrame([
            dict(Task="Job" + str(Jobs[0]), Start='2022-12-' + str(int(Si[0])), Finish='2022-12-' + str(int(Ci[0])),
                 Resource="Machine" + str(Ai[0])),
            dict(Task="Job" + str(Jobs[1]), Start='2022-12-' + str(int(Si[1])), Finish='2022-12-' + str(int(Ci[1])),
                 Resource="Machine" + str(Ai[1])),
            dict(Task="Job" + str(Jobs[2]), Start='2022-12-' + str(int(Si[2])), Finish='2022-12-' + str(int(Ci[2])),
                 Resource="Machine" + str(Ai[2])),
            dict(Task="Job" + str(Jobs[3]), Start='2022-12-' + str(int(Si[3])), Finish='2022-12-' + str(int(Ci[3])),
                 Resource="Machine" + str(Ai[3])),
            dict(Task="Job" + str(Jobs[4]), Start='2022-12-' + str(int(Si[4])), Finish='2022-12-' + str(int(Ci[4])),
                 Resource="Machine" + str(Ai[4])),
            dict(Task="Job" + str(Jobs[5]), Start='2022-12-' + str(int(Si[5])), Finish='2022-12-' + str(int(Ci[5])),
                 Resource="Machine" + str(Ai[5])),
            dict(Task="Job" + str(Jobs[6]), Start='2022-12-' + str(int(Si[6])), Finish='2022-12-' + str(int(Ci[6])),
                 Resource="Machine" + str(Ai[6])),
            dict(Task="Job" + str(Jobs[7]), Start='2022-12-' + str(int(Si[7])), Finish='2022-12-' + str(int(Ci[7])),
                 Resource="Machine" + str(Ai[7])),
            dict(Task="Job" + str(Jobs[8]), Start='2022-12-' + str(int(Si[8])), Finish='2022-12-' + str(int(Ci[8])),
                 Resource="Machine" + str(Ai[8])),
            dict(Task="Job" + str(Jobs[9]), Start='2022-12-' + str(int(Si[9])), Finish='2022-12-' + str(int(Ci[9])),
                 Resource="Machine" + str(Ai[9]))
        ])

        fig = px.timeline(df, x_start="Start", x_end="Finish", y="Resource", color="Task",title='Scheduling with Advanced_List', text='Task')
        fig.show()"""

#def F(pi):
if __name__ == "__main__":
    #instanceloader
    def instanceloader(fileName):
        i = json.load(open(fileName, "r"))
        return Instance(i["deadline_type"], i["job_deadlines"], i["job_type"], i["m"], i["machine_type"], i["n"],
                        i["processing_times"], i["seed"], i["speeds"], i["tau"], i["weights"], i["weights_type"])


    instance = instanceloader("/home/tchiapi/Downloads/instancesII/R3_10_discrete_seed1_wgtrandom_deadlinejobsCmax_wgt_mj_factor1.000.json")
    scenario = Scenario(instance)
    pol1 = Policy(instance,scenario)
    Jobs1 = [0,1,2,3,4,5,6,7,8,9]
    fix = FixedAssigment(instance,scenario)
    print(fix.assignment_set)
    #state = State([0, 0, 0], Jobs1, [[], [], []])

