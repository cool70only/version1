

import random
import similarity_core
import json

question_list = [
"What is the format of a dividing complex numbers problem?",
"What type of number can a, b, c, and d be?",
"What is i?",
"When you divide two complex numbers, what is the primary goal you are trying to achieve?",
"How do you rationalize the denominator when you divide two complex numbers?",
"What is the definition of the conjugate?",
"If the denominator is represented by the expression c+di, what would its conjugate be?",
"Once you set up the problem to multiply the numerator and denominator by the conjugate of the denominator, what process do you use to carry out the multiplication?",
"What does FOIL stand for and where does it come from?",
"What do you get when you FOIL the numerator?",
"What do you get when you FOIL the denominator?",
"What do you do after you have FOILed the numerator and denominator?",
"What do you get after you have combined the like terms?"
    ]

answer_list1 = [
"It has a numerator of the format a+bi and denominator of the form c+di",
"a, b, c, d are real  numbers.",
"I is the square root of minus 1",
"Rationalize the denominator.",
"You divide both numerator and denominator by the conjugate of the denominator?",
"The conjugate is the complex number with sign between real and imaginary part changed.",
"c-di",
"FOIL",
"FOIL stands for First, Outer, Inner, Last. It comes from the distributive property.",
"(ac-adi+bci-bdi^2)” or “(ac-adi+bci+bd)",
"(c^2-cdi+cdi-d^2i^2)” or “(c^-cdi+cdi+d^2)",
"Combine like terms",
"((ac+bd)+(bc-ad)i)/(c^2+d^2)"
               ]

answer_list2 = [
    "When you divide two complex numbers, the numerator has the form a+bi and the denominator has the form c+di",
"a, b, c, and d are real numbers. They can be positive or negative. Often they are integers.",
"I is the square root of minus 1",
"When you divide two complex numbers, your primary goal is to rationalize the denominator.",
"To rationalize the denominator, you divide both numerator and denominator by the conjugate of the denominator.",
"The conjugate is the complex number with sign between real and imaginary part changed.",
"If the denominator is represented by the expression c+di, its conjugate is c-di.",
"Once you set up the problem to multiply the numerator and denominator by the conjugate of the denominator, you use FOIL to carry out the multiplication",
"FOIL stands for First, Outer, Inner, Last. It comes from the distributive property.",
"When you FOIL the numerator you get (ac-adi+bci-bdi^2) which equals ac-adi+bci+bd",
"When you FOIL the denominator you get (c^2-cdi+cdi-d^2i^2)” or “(c^-cdi+cdi+d^2)",
"After you have FOILed the numerator and denominator, you combine like terms.",
"After you combine like terms, you get ((ac+bd)+(bc-ad)i)/(c^2+d^2)"
               ]





class feedback_CN:

    def getquestion(self):
        out1 = []
        for i in range(len(question_list)):
            tmp = {}
            tmp["id"] = i
            tmp["question"] = question_list[i]
            out1.append(tmp)
        out2 = {"content":out1}

        out3 = json.dumps(out2)


        return out3

    def checkanswer(self, answer = " answer ", question_id = 0):

        score = self.core.get_score(answer, answer_list1[question_id], word_list)
        if score[0] < 0.85:
            return 0, answer_list2[question_id]

        return 1, answer_list2[question_id]



    def __init__(self, core):
        self.core = core



# tmp = similarity_core.similarity_core()
# tmp2 = feedback_CN("")
# print(tmp2.getquestion())
# print(tmp2.checkanswer("gooood"))