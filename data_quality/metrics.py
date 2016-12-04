class Metrics(object):

    def __init__(self, num_true_positives, num_true_negatives, num_false_positives, num_false_negatives):
        self._num_true_positives = num_true_positives
        self._num_true_negatives = num_true_negatives
        self._num_false_positives = num_false_positives
        self._num_false_negatives = num_false_negatives

    def compute_precision(self):
        denominator = float(self._num_true_positives + self._num_false_positives)
        if denominator == 0:
            return float('inf')
        return self._num_true_positives / denominator

    def compute_recall(self):
        denominator = float(self._num_true_positives + self._num_false_negatives)
        if denominator == 0:
            return float('inf')
        return self._num_true_positives / denominator

    def compute_accuracy(self):
        numerator = (self._num_true_positives + self._num_true_negatives)
        denominator = (self._num_true_positives + self._num_true_negatives +
                       self._num_false_positives + self._num_false_negatives)

        return numerator / float(denominator)

    def __repr__(self):
        return "Metrics(precision={0}," \
               "        recall={1}," \
               "        accuracy={2})".format(self.compute_precision(),
                                              self.compute_recall(),
                                              self.compute_accuracy())