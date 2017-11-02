
type Classifier struct {
    classPerWordCount map[string]int
    classPerDocument  map[string]int
    wordClassCount    map[string]map[string]int
    documentsCount    int
}

# Train the classifier with text and its class.
func (c *Classifier) Train(words []string, class string) {
    c.documentsCount++
    c.incrementDocumentPerClass(class)

    for _, word := range words {
        c.incrementWordClass(word, class)
        c.incrementClassPerWord(class)
    }
}

func (c *Classifier) Classify(words []string) (string, float64) {
    var score float64
    var prediction string

    for _, class := range c.classes() {
        var probability = c.probability(words, class)

        if score < probability {
            score = probability
            prediction = class
        }
    }

    return prediction, score
}