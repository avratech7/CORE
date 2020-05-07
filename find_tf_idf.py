import math
import numpy as np

first_string = "sport includes all forms of competitive physical activity or games which,[1] through casual or organized participation, at least in part aim to use, maintain or improve physical ability and skills while providing enjoyment to participants, and in some cases, entertainment for spectators.[2] Sports can bring positive results to one's physical health. Hundreds of sports exist, from those between single contestants, through to those with hundreds of simultaneous participants, either in teams or competing as individuals. In certain sports such as racing, many contestants may compete, simultaneously or consecutively, with one winner; "

second_string = "in others, the contest (a match) is between two sides, each attempting to exceed the other. Some sports allow a tie or draw, in which there is no single winner; others provide tie-breaking methods to ensure one winner and one loser. A number of contests may be arranged in a tournament producing a champion. Many sports leagues make an annual champion by arranging games in a regular sports season, followed in some cases by playoffs."

third_string = "sport is generally recognised as system of activities which are based in physical athleticism or physical dexterity, with the largest major competitions such as the Olympic Games admitting only sports meeting this definition,[3] and other organisations such as the Council of Europe using definitions precluding activities without a physical element from classification as sports.[2] However, a number of competitive, but non-physical, activities claim recognition as mind sports. The International Olympic "

six_string = "medicine is the science and practice of establishing the diagnosis, prognosis, treatment, and prevention of disease. Medicine encompasses a variety of health care practices evolved to maintain and restore health by the prevention and treatment of illness. Contemporary medicine applies biomedical sciences, biomedical research, genetics, and medical technology to diagnose, treat, and prevent injury and disease, typically through pharmaceuticals or surgery, but also through therapies as diverse as psychotherapy, external splints and traction, medical devices, biologics, and ionizing radiation, amongst others.[1]"

seven_string = "medicine has been around for thousands of years, during most of which it was an art (an area of skill and knowledge) frequently having connections to the religious and philosophical beliefs of local culture. For example, a medicine man would apply herbs and say prayers for healing, or an ancient philosopher and physician would apply bloodletting according to the theories of humorism. In recent centuries, since the advent of modern science, most medicine has become a combination of art and science (both basic and applied, under the umbrella of medical science). While stitching technique for sutures is an art learned through practice, the knowledge of what happens at the cellular and molecular level in the tissues being stitched arises through science. "

eight_string = "Prescientific forms of medicine are now known as traditional medicine and folk medicine, though they do not fall within the modern definition of “medicine” which is based in medical science. Traditional medicine and folk medicine remain commonly used with, or instead of, scientific medicine and are thus called alternative medicine (meaning “[something] other than medicine”, from Latin alter, “other”). For example, evidence on the effectiveness of acupuncture is variable and inconsistent for any condition,[2] but is generally safe when done by an appropriately trained practitioner.[3] In contrast, alternative treatments outside the bounds not just of scientific medicine, but also outside the bounds of safety and efficacy are termed quackery. "

four_string = "sport is usually governed by a set of rules or customs, which serve to ensure fair competition, and allow consistent adjudication of the winner. Winning can be determined by physical events such as scoring goals or crossing a line first. It can also be determined by judges who are scoring elements of the sporting performance, including objective or subjective measures such as technical performance or artistic impression. "
four_string_list = four_string.split(" ")

list_of_all_documents = [first_string,second_string,third_string,six_string,seven_string,eight_string]
list_of_all_documents_terms = []
list_of_all_terms_and_values = []
new_document_list_of_all_terms_and_values = []
new_list_of_all_documents_term = []

for document in list_of_all_documents:
    list_of_all_documents_terms.append(document.split(" "))

print(np.matrix(list_of_all_documents_terms))
# use by the tf function
def max_term_in_d(d_terms_list):
    max = 0
    for i in d_terms_list:
        if d_terms_list.count(i) / len(d_terms_list) > max:
            max = d_terms_list.count(i) / len(d_terms_list)
    return max

def tf(term,d_terms_list):
    return (0.5+0.5*((d_terms_list.count(term)/ len(d_terms_list)) / max_term_in_d(d_terms_list)))

# use by the idf function
def num_docs_has_the_term(term,list_of_documents):
    count = 0
    for i in list_of_documents:
        if term in i:
            count += 1
    return count

def idf(term,list_of_documents):
    return math.log(len(list_of_documents) / num_docs_has_the_term(term,list_of_documents))

def tfidf(term,d_terms_list,list_of_documents):
    return tf(term,d_terms_list) * idf(term,list_of_documents)

for list_of_terms_in_document in list_of_all_documents_terms:
     for term in list_of_terms_in_document:
       list_of_all_terms_and_values.append([term,tfidf(term,list_of_terms_in_document,list_of_all_documents_terms)])
       print(term,tfidf(term,list_of_terms_in_document,list_of_all_documents_terms))

new_list_of_all_documents_term = list_of_all_documents_terms
new_list_of_all_documents_term.append(four_string_list)
print(len(new_list_of_all_documents_term))
for term in four_string_list:
    new_document_list_of_all_terms_and_values.append([term,tfidf(term,four_string_list,new_list_of_all_documents_term)])

