from mrjob.job import MRJob
from mrjob.job import MRStep


class P3(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper, reducer=self.reducer1),
            MRStep(reducer=self.reducer2)
        ]

    def mapper(self, _, line):
        user,movie,rating,genre,date = line.split(',')
        yield date, 1

    def reducer1(self, date, values):
        total = sum(values)
        yield None, (total, date)

    def reducer2(self, date, values):
        min_value = min(values)
        yield "Date min movies", min_value[1]


if __name__ == '__main__':
    P3.run()
