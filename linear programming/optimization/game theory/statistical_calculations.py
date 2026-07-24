import numpy as np
import pandas as pd
import random
import math
from itertools import combinations
import statistics

#import scipy.stats as stats
#import matplotlib.pyplot as plt


""""
-> have a die with 6 sides(1,2,3,4,5,6)
-> create a sample of size n
-> for each sample calculate the mean,variance
-> fit distributions for both mean and variance

"""

class StatisticalCalculator:

    def create_samples(population) -> []:

        sample_size = int(input("Enter the number you want your sample size to be : "))
        length_population = len(population)
        sampling_ways = math.comb(length_population, sample_size)
        print(f"there are {sampling_ways} possible ways of sampling")

        if sample_size > length_population:
            print("sample size must be smaller or equal to max number of the die")
        else:
            samples = list(combinations(die, sample_size))

        return samples
    def get_means(samples):
        sample_means = []
        for sample in samples:
            sample_mean = statistics.mean(sample)
            sample_means.append(sample_mean)
        return sample_means
    def get_variances(samples):
        sample_variances = []
        for sample in samples:
            sample_variance = statistics.variance(sample)
            sample_variances.append(sample_variance)
        return sample_variances
    def distribution(samples) -> pd.DataFrame:
        len_sample = len(sample_means)
        from collections import Counter
        counting_elements = Counter(sample)
        probabilities = []
        keys_list = list(counting_elements.keys()) # GIVES MEAN / VARIANCE VALUES
        values_list = list(counting_elements.values()) # GIVES COUNT NUMBER OF EACH MEAN OR VARIANCE VALUE
        for index, value in enumerate(values_list):
            probability = value / len_sample
            probabilities.append(probability)
            
        data = {
            "value": keys_list,
            "P(value)":probabilities
        }
        distribution = pd.DataFrame(data)
        return distribution
        
        
if __name__ == "__main__":

    die = []
    for i in range(1,7,1):
        die.append(i)

    sample = StatisticalCalculator.create_samples(die)
    sample_means = StatisticalCalculator.get_means(sample)
    sample_variances = StatisticalCalculator.get_variances(sample)
    population_variance = statistics.variance(sample_means)
    print(f"These are your samples : {sample}")
    print(f"These are your means : {sample_means}")
    print(f"This is your variance : {population_variance}")
    distribution = StatisticalCalculator.distribution(sample_means)
    print(print(sum(sample_means)))
    
    


