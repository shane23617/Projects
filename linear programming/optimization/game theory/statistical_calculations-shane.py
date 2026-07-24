import numpy as np
import pandas as pd
import random
import math
from itertools import combinations
import statistics
import scipy.stats as stats
import matplotlib.pyplot as plt


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
    def visuals(samples):
        plt.hist(samples, density = True)
        plt.show()


if __name__ == "__main__":

    die = [168,175,185,173,171,172]
    #for i in range(1,7,1):
     #   die.append(i)

    sample = StatisticalCalculator.create_samples(die)
    sample_means = StatisticalCalculator.get_means(sample)
    sample_variances = StatisticalCalculator.get_variances(sample)
    print(f"These are your samples : {sample}")
    print(f"These are your means : {sample_means}")
    print(f"These are your variances : {sample_variances}")
"""
    plt.figure( figsize = (5,5))
    plt.hist(sample, density = True)
    plt.show()

"""

