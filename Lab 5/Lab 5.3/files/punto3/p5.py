from mrjob.job import MRJob
from mrjob.job import MRStep


class P5(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper, reducer=self.reducer1),
            MRStep(reducer=self.reducer2)
        ]

    def mapper(self, _, line):
        user,movie,rating,genre,date = line.split(',')
        yield date, int(rating)

    def reducer1(self, date, values):
        l = list(values)
        avg = sum(l) / len(l)
        yield None, (avg, date)

    def reducer2(self, date, values):
        min_rating = min(values)
        yield "Date min rating", min_rating[1]


if __name__ == '__main__':
    P5.run()
