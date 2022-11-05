from mrjob.job import MRJob
from mrjob.job import MRStep


class P7(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper1, reducer=self.reducer1),
            MRStep(mapper=self.mapper2, reducer=self.reducer2),
        ]

    def mapper1(self, _, line):
        user,movie,rating,genre,date = line.split(',')
        yield (movie, genre), int(rating)

    def reducer1(self, data, values):
        l = list(values)
        avg = sum(l) / len(l)
        yield data, avg

    def mapper2(self, data, values):
         yield data[1], (values, data[0])

    def reducer2(self, genre, values):
        l = list(values)
        min_rating = min(l)
        max_rating = max(l)
        yield ["Genre:", genre] , (["Worst:", min_rating[1]], ["Best:", max_rating[1]])


if __name__ == '__main__':
    P7.run()
