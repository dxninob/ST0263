from mrjob.job import MRJob


class P3(MRJob):

    def mapper(self, _, line):
        idemp, sector,salary,year = line.split(',')
        yield idemp, sector

    def reducer(self, idemp, values):
        l = len(set(values))
        yield idemp, l


if __name__ == '__main__':
    P3.run()
