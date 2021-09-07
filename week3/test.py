'''
Assume df is a pandas dataframe object of the dataset given
'''
import numpy as np
import pandas as pd
import random

'''Calculate the entropy of the enitre dataset'''
    #input:pandas_dataframe
    #output:int/float/double/large

def get_entropy_of_dataset(df):
    df_col = df.iloc[:,-1]
    norm_counts = np.unique(df_col, return_counts=True)[1] / len(df_col)
    return -(norm_counts * np.log(norm_counts)/np.log(2)).sum()



'''Return entropy of the attribute provided as parameter'''
    #input:pandas_dataframe,str   {i.e the column name ,ex: Temperature in the Play tennis dataset}
    #output:int/float/double/large
def get_avg_info_of_attribute(df,attribute):
    entropy = 0
    for i in np.unique(df[attribute]):
        df_sub = df.loc[df[attribute] == i]
        entropy += ((df_sub.shape[0]/df.shape[0])*get_entropy_of_dataset(df_sub))
    return abs(entropy)



'''Return Information Gain of the attribute provided as parameter'''
    #input:int/float/double/large,int/float/double/large
    #output:int/float/double/large
def get_information_gain(df,attribute):
    return get_entropy_of_dataset(df) - get_avg_info_of_attribute(df, attribute)



''' Returns Attribute with highest info gain'''
    #input: pandas_dataframe
    #output: ({dict},'str')
def get_selected_attribute(df):

    information_gains=dict()
    selected_column=selected_column_max_value=None

    '''
    Return a tuple with the first element as a dictionary which has IG of all columns
    and the second element as a string with the name of the column selected
    example : ({'A':0.123,'B':0.768,'C':1.23} , 'C')
    '''
    for column_name in list(df.columns)[: -1]:
        information_gains[column_name] = get_information_gain(df, column_name)
        if selected_column_max_value == None or selected_column_max_value < information_gains[column_name]:
            selected_column_max_value = information_gains[column_name]
            selected_column = column_name

    return (information_gains,selected_column)

