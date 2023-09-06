import pstats

# this is a common way to read the output from cProfle
def main():
    '''read in the profile output file then print the results'''
    # be careful with the path to the file - depends where you run python
    p = pstats.Stats('performance/profile_output')
    p.print_stats()

if __name__ == '__main__':
    main()