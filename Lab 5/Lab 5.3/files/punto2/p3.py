from mrjob.job import MRJob
from mrjob.job import MRStep


class P3(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper1, reducer=self.reducer1),
            MRStep(mapper=self.mapper2, reducer=self.reducer2),
            MRStep(reducer=self.reducer3),
        ]

    def mapper1(self, _, line):
        company,price,date = line.split(',')
        yield company, (float(price), date)

    def reducer1(self, company, values):
        l = list(values)
        min_price = min(l)
        yield company, min_price[1]

    def mapper2(self, company, values):
        yield values, 1

    def reducer2(self, date, values):
        l = list(values)
        total = sum(l)
        yield None, (total, date)
    
    def reducer3(self, date, values):
        l = list(values)
        max_date = max(l)
        yield "Date", max_date[1]


if __name__ == '__main__':
    P3.run()
